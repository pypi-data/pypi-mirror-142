# Copyright Okera Inc.

from __future__ import absolute_import

import collections
import datetime
import functools
import hashlib
import heapq
import json
import time
import sys

from okera._thrift_api import TAuthorizeQueryClient
from okera._thrift_api import TAuthorizeQueryParams
from okera._thrift_api import TGetDatasetsParams
from okera._thrift_api import TErrorCode
from okera._thrift_api import TRecordServiceException

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Value to use in masking policy when the user does not have access to the column
NO_ACCESS_VALUE = 'NULL'

SNOWFLAKE_ROW_POLICY_PREAMBLE = """
CREATE OR REPLACE ROW ACCESS POLICY %s AS (%s) RETURNS boolean ->
"""

SNOWFLAKE_MASKING_POLICY_PREAMBLE = """
CREATE OR REPLACE MASKING POLICY %s AS (%s %s) RETURNS %s ->
"""

# These are (partial) statements that are okay to fail. Snowflake doesn't accept
# 'IF NOT EXISTS' in these statements so we have to try ignore errors.
ACCEPTABLE_ERROR_QUERIES = [
  'DROP ROW ACCESS POLICY',
  'DROP MASKING POLICY',
]

# And expected errors for those policies
APPLY_POLICY_NOT_EXISTS_SENTINEL1 = 'does not exist or not authorized.'
APPLY_POLICY_NOT_EXISTS_SENTINEL2 = 'is not attached to'

# Table property to control if syncing is enabled
TBL_PROP_DRIVER = 'driver'
TBL_PROP_SYNC_ENABLED = 'okera.policy-sync.enabled'

# Table properties to control the users to sync
TBL_PROP_USERS_ADDITIONAL = 'okera.policy-sync.users.additional'
TBL_PROP_USERS_BLACKLIST = 'okera.policy-sync.users.blacklist'
TBL_PROP_USERS_LIST = 'okera.policy-sync.users.list'
TBL_PROP_USERS_WHITELIST = 'okera.policy-sync.users.whitelist'

# Table properties for policy sync status
# Keep in sync with PolicySync.java
TBL_PROP_POLICY_LAST_ERROR = "policy-sync.last-syncing-utc"
TBL_PROP_POLICY_LAST_QUEUED = "policy-sync.last-queued-utc"
TBL_PROP_POLICY_LAST_SYNC = "policy-sync.last-sync-utc"
TBL_PROP_POLICY_LAST_SYNCING = "policy-sync.last-syncing-utc"
TBL_PROP_POLICY_SYNC_MD5 = "policy-sync.md5"
TBL_PROP_POLICY_SYNC_ERROR_MSG = "policy-sync.error-message"
TBL_PROP_POLICY_SYNC_STATUS_MSG = "policy-sync.status-message"

def _masking_policy_name(tbl, col):
    return "%s_%s_masking_policy" % (tbl, col)

def _row_policy_name(tbl):
    return tbl + '_row_policy'

class CoalescingEventQueue():
    """ A coalescing producer/consumer event queue. The only difference is it adds
        coalescing. This means that if the same key is enqueue in a short window, only
        one (the last) event will be dequeued. This is used typically to model a
        triggering pattern and only the last event in a burst should trigger.

        This is done by delaying when a enqueued event can be dequeued and then
        scanning the queue for other events with the same event at dequeue time. If
        another of the same event is found, the earlier event is ignored (removed from
        queue and not returned.
    """
    def __init__(self, delay_ms, max_ms):
        """ delay_ms is the time to wait before an enqueue is visible for
            dequeue. It is the time to wait for coalescing.

            max_ms is the maximum time to wait before an event is triggered
            and will not longer be eligible for coalescing.
        """
        self.delay_ms = delay_ms
        self.max_ms = max_ms
        self.heap = []

    def enqueue(self, e):
        _enqueue(e, __now())

    def dequeue(self):
        return self._dequeue(__now())

    # Test helpers to control the clock.
    def _enqueue(self, e, ts):
        heapq.heappush(self.heap, (ts + self.delay_ms, e, ts))

    def _dequeue(self, now):
        print(self.heap)
        while self.heap:
            v = self.heap[0]
            if self.max_ms and v[2] + self.max_ms < now:
                # Handle max_ms
                heappq.heappop(self.heap)
                return v[1]

            if v[0] > now:
                return None

            heapq.heappop(self.heap)
            for e in self.heap:
                if e[1] == v[1]:
                    # Found another entry, ignore this one
                    v = None
                    break
            if not v:
                continue
            return v[1]

        return None

    def __now(self):
        return round(time.timme() * 1000)

class Policy():
    def __init__(self, user):
        self.user = user
        self.filters = []

        # Empty indicates access to all columns
        self.column_restrictions = {}

    def __repr__(self):
        return 'User: %s. Filters: %s. Columns: %s' % \
            (self.user, self.filters, self.column_restrictions)

def _compute_hash(*args):
    s = ''
    for a in args:
        s += str(a)
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def _generate_grants(
        users, policies, single_grant_role, per_user_role_grants, tbl, role_pattern):
    result = []
    roles = []
    if single_grant_role:
        roles.append(single_grant_role)
        for u, p in policies.items():
            if p:
                result.append('GRANT SELECT ON %s TO ROLE %s' % \
                    (tbl, single_grant_role))
            else:
                result.append('REVOKE SELECT ON %s FROM ROLE %s' % \
                    (tbl, single_grant_role))
    elif per_user_role_grants:
        for u, p in policies.items():
            role = role_pattern % u
            roles.insert(0, role)
            if p:
                result.append('GRANT SELECT ON %s TO ROLE %s' % (tbl, role))
                namespaces = tbl.split('.')
                # TODO relax this
                assert len(namespaces) == 3
                result.append(
                    'GRANT USAGE ON DATABASE %s TO ROLE %s' % (namespaces[0], role))
                result.append(
                    'GRANT USAGE ON SCHEMA %s.%s TO ROLE %s' % (
                        namespaces[0], namespaces[1], role))
            else:
                result.append('REVOKE SELECT ON %s FROM ROLE %s' % (tbl, role))
            if u in users:
                result.append('GRANT ROLE %s TO USER "%s"' % (role, u))
    for role in roles:
        result.insert(0, 'CREATE ROLE IF NOT EXISTS %s' % role)
    return result

def _none_safe_cmp(x, y):
    if isinstance(x, tuple):
        for i in range(0, len(x)):
            v = _none_safe_cmp(x[i], y[i])
            if v:
                return v
        return 0
    if x is None or y is None:
        if x is None and y is None:
            return 0
        elif x is None:
            return -1
        else:
            return 1
    else:
        if x == y:
            return 0
        elif x < y:
            return -1
        else:
            return 1

def _generate_row_filters(policies, tbl, column_signatures):
    need_filter_policy = False
    # Map of filter to users with that filter. Empty string indicates no filter
    filter_policies = {}
    for u, p in policies.items():
        if not p:
            need_filter_policy = True
            continue
        k = None
        if not p or not p.filters:
            k = ''
        else:
            need_filter_policy = True
            k = ' AND '.join(p.filters)

        if k not in filter_policies:
            filter_policies[k] = []
        filter_policies[k].append(u)

    if not need_filter_policy or not column_signatures:
        return None, None

    policy_name = _row_policy_name(tbl)

    # For each filter, generate the case statement
    policy = SNOWFLAKE_ROW_POLICY_PREAMBLE % (policy_name, ', '.join(column_signatures))
    policy += 'CASE\n'
    for p, u in filter_policies.items():
        users = []
        for user in u:
            users.append("'%s'" % user)
        if not p:
            p = 'TRUE'
        case = '    WHEN current_user() in (%s) THEN %s\n' % (', '.join(users), p)
        policy += case
    policy += '    ELSE FALSE\n'
    policy += 'END'

    return policy, policy_name

def _generate_column_policies(policies, tbl):
    # Map of (col -> map of(transform -> list of users)
    partial_access_users = {}
    no_access_users = []
    all_access_users = []

    referenced_columns = {}

    for u, p in policies.items():
        if not p:
            no_access_users.append("'%s'" % u)
            continue
        if not p.column_restrictions:
            all_access_users.append("'%s'" % u)
            continue

        for col, access in p.column_restrictions.items():
            if col not in partial_access_users:
                partial_access_users[col] = {}

            if access.transform:
                v = access.transform
            elif access.accessible:
                v = col
            else:
                v = None

            if v not in partial_access_users[col]:
                partial_access_users[col][v] = []
            partial_access_users[col][v].append(u)
            referenced_columns[col] = access.column

    if not partial_access_users:
        # No partial access, no need to produce column policy
        return None

    partial_access_users = collections.OrderedDict(
        sorted(partial_access_users.items(), key=functools.cmp_to_key(_none_safe_cmp)))

    # Collection of masking policies. This will be populated for each column
    # that needs a masking policy.
    masking_policies = []
    for col, p in partial_access_users.items():
        col_desc = referenced_columns[col]
        policy_name = _masking_policy_name(tbl, col)
        policy = SNOWFLAKE_MASKING_POLICY_PREAMBLE % \
            (policy_name, col_desc.name, col_desc.type, col_desc.type)
        policy += 'CASE\n'

        # Add the cases for each type of transform
        p = collections.OrderedDict(
            sorted(p.items(), key=functools.cmp_to_key(_none_safe_cmp)))

        # Handle users with full access
        full_access_users = all_access_users.copy()
        for t, u in p.items():
            if t == col:
                for user in u:
                    full_access_users.append("'%s'" % user)
        case = '    WHEN current_user() in (%s) THEN %s\n' % \
            (', '.join(full_access_users), col)
        policy += case

        # In the case where the only policies with all users having full access,
        # no need to create a column policy.
        need_to_add = False

        # 't' is the target transformed value and u is the list of users needing
        # this transform.
        for t, u in p.items():
            # v is the expression to transform to
            if t == col:
                # Handled above with all_access_users
                continue

            need_to_add = True
            v = t
            if t is None:
                v = NO_ACCESS_VALUE

            # Collect all the users that need this transform on this column
            users = []
            for user in u:
                users.append("'%s'" % user)
            case = '    WHEN current_user() in (%s) THEN %s\n' % \
                (', '.join(users), v)
            policy += case

        if need_to_add:
            policy += '    ELSE %s\n' % NO_ACCESS_VALUE
            policy += 'END'
            masking_policies.append((col, policy_name, policy))
    return masking_policies

def debug_print(grants, pre_alters, row_filters, column_policies, post_alters):
    print("GRANTS:")
    print("--------------------------------------------------------------")
    for grant in grants:
        print(grant + ';')
    print("--------------------------------------------------------------")

    print("ROW FILTER:")
    print("--------------------------------------------------------------")
    if row_filters:
        print(row_filters + ';')
    print("--------------------------------------------------------------")

    print("COLUMN POLICIES:")
    print("--------------------------------------------------------------")
    if column_policies:
        for p in column_policies:
            print(p[2] + ';')
    print("--------------------------------------------------------------")

    print("PRE-ALTERS:")
    print("--------------------------------------------------------------")
    for alter in pre_alters:
        print(alter + ';')
    print("--------------------------------------------------------------")

    print("POST-ALTERS:")
    print("--------------------------------------------------------------")
    for alter in post_alters:
        print(alter + ';')
    print("--------------------------------------------------------------")

def generate_policies(
        conn, users, db_name, tbl_name, okera_tbl,
        single_grant_role=None,
        per_user_role_grants=True,
        role_pattern='"%s_ROLE"',
        client=TAuthorizeQueryClient.SNOWFLAKE):
    """ Generates the set of DDL needed to update this table for all users

        This does not mutate the underlying database at all. It only generates
        the required SQL and does not run them.

        Parameters
        ----------
        conn :
            Okera planner connection.

        users : list[str]
            Total list of users to generate policies for.

        db_name : str
            Database, in the okera catalog to generate policies for.

        okera_tbl : obj
            Okera table object

        tbl_name : str
            Table in database, in the okera catalog to generate policies for.

        Returns
        -------
        Tuple of different types of DDL to run.
    """

    if client != TAuthorizeQueryClient.SNOWFLAKE:
        raise RuntimeError("Only SNOWFLAKE is a supported client currently.")

    input_users = users.copy()
    # Adding system user to this list to ensure we can get metadata back
    if 'okera' not in users:
        users.append('okera')

    # For every user, look up the policies and populate 'policies'
    # Users that have no access will have None as the map value
    policies = {}

    # Columns and types used across all filters across all users
    row_filter_column_names = []
    row_filter_column_signatures = []

    # Table name in snowflake
    sf_table_name = None
    fq_tbl_name = db_name + '.' + tbl_name

    for user in users:
        request = TAuthorizeQueryParams()
        request.client = TAuthorizeQueryClient.SNOWFLAKE_POLICY_SYNC
        request.db = [db_name]
        request.dataset = tbl_name
        request.requesting_user = user

        try:
            result = conn.service.client.AuthorizeQuery(request)
            p = Policy(user)
            policies[user] = p

            if result.jdbc_referenced_tables and \
                    fq_tbl_name in result.jdbc_referenced_tables:
                sf_table_name = result.jdbc_referenced_tables[fq_tbl_name].jdbc_fq_tbl_name

            if result.filters:
                p.filters += result.filters.filters

                for col in result.filters.columns:
                    if col.name in row_filter_column_names:
                        # Already seen this column.
                        continue
                    row_filter_column_names.append(col.name)
                    row_filter_column_signatures.append('%s %s' % (col.name, col.type))

            if result.column_access:
                p.column_restrictions = result.column_access
        except TRecordServiceException as ex:
            if ex.code == TErrorCode.AUTHENTICATION_ERROR:
                policies[user] = None
            else:
                raise ex

    if not sf_table_name:
        raise RuntimeError("Could not determine Snowflake table name. Cannot sync.")

    sf_columns = []
    for col in okera_tbl.schema.cols:
        sf_columns.append(col.name.upper())

    # Sort the policies by user for stability
    policies = collections.OrderedDict(
        sorted(policies.items(), key=functools.cmp_to_key(_none_safe_cmp)))

    # Generate the grants
    grants = _generate_grants(
        input_users, policies, single_grant_role, per_user_role_grants, sf_table_name,
        role_pattern)

    # Generate the row filters
    row_filter_policy, row_filter_policy_name = _generate_row_filters(
        policies, sf_table_name, row_filter_column_signatures)

    # Generate the column masking policies
    column_policies = _generate_column_policies(
        policies, sf_table_name)

    # Generate the alters
    pre_alters = []
    post_alters = []

    # We need to reset the state of this table before we proceed, so
    # drop any previously set policies.
    # Note: some of these fail with a "not exists" error that should be ignored.
    pre_alters.append(
        'ALTER TABLE %s DROP ROW ACCESS POLICY %s' % \
        (sf_table_name, _row_policy_name(sf_table_name)))
    for sf_col in sf_columns:
      pre_alters.append(
          'ALTER TABLE %s MODIFY COLUMN %s UNSET MASKING POLICY' % \
          (sf_table_name, sf_col))
      pre_alters.append(
          'DROP MASKING POLICY %s' % (_masking_policy_name(sf_table_name, sf_col)))

    if row_filter_policy:
        post_alters.append(
            'ALTER TABLE %s ADD ROW ACCESS POLICY %s ON(%s)' % \
            (sf_table_name, row_filter_policy_name, ', '.join(row_filter_column_names)))
    if column_policies:
        for col, policy, _ in column_policies:
            post_alters.append(
                'ALTER TABLE %s MODIFY COLUMN %s SET MASKING POLICY %s' % \
                (sf_table_name, col, policy))

    md5 = _compute_hash(\
        grants, pre_alters, row_filter_policy, column_policies, post_alters);
    return grants, pre_alters, row_filter_policy, column_policies, post_alters, md5

def get_snowflake_users(conn, before_role=None, after_role=None):
    if before_role:
        conn.query_request("USE ROLE {}".format(before_role))
    result = conn.query_request("SHOW USERS")
    if after_role:
        conn.query_request("USE ROLE {}".format(after_role))
    users = []
    for u in result['rowset']:
        users.append(u[0])
    return users

def get_sync_users(users, tbl_params):
    """ Computes the users to sync combining the input users with the configs on
        the table. 'users' typically will come from the underlying db.
    """
    if not tbl_params:
        return users

    result = users.copy()

    def to_list(v):
        l = []
        for u in v.split(','):
            u = u.strip()
            if u:
                l.append(u)
        return l

    if TBL_PROP_USERS_LIST in tbl_params:
        # Set in table properties, use that
        v = tbl_params[TBL_PROP_USERS_LIST]
        result = []
        for u in to_list(v):
            result.append(u)
        return result

    if TBL_PROP_USERS_ADDITIONAL in tbl_params:
        # Add any additional users
        v = tbl_params[TBL_PROP_USERS_ADDITIONAL]
        for u in to_list(v):
            result.append(u)

    if TBL_PROP_USERS_BLACKLIST in tbl_params:
        # Remove any blacklist users
        v = tbl_params[TBL_PROP_USERS_BLACKLIST]
        for u in to_list(v):
            if u in result:
                result.remove(u)

    if TBL_PROP_USERS_WHITELIST in tbl_params:
        # Only return whitelist users
        v = tbl_params[TBL_PROP_USERS_WHITELIST]
        whitelist = []
        for u in to_list(v):
            if u in result:
                whitelist.append(u)
        return whitelist

    return result

def sync_policies(
        planner_conn, db_conn, db_name, tbl_name, role, users=None,
        role_pattern='"%s_ROLE"',
        per_user_role_grants=True,
        dry_run=False,
        client=TAuthorizeQueryClient.SNOWFLAKE):
    """ Synchronizes the policies for this table.

        Parameters
        ----------
        planner_conn :
            Okera planner connection.

        db_conn :
            Connection to the underlying DB.

        users : list[str], optional
            If set, the users to generate for, otherwise, determine them from the
            environment.

        db_name : str
            Database, in the okera catalog to generate policies for.

        tbl_name : str
            Table in database, in the okera catalog to generate policies for.
    """

    eprint('Syncing table %s.%s...' % (db_name, tbl_name))

    # Get the okera table object
    request = TGetDatasetsParams()
    request.dataset_names = ['{}.{}'.format(db_name, tbl_name)]
    request.with_schema = True
    okera_tbl = planner_conn.service.client.GetDatasets(request).datasets[0]

    # Update the last time a syncing operation begun
    now = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    properties = [
        "'%s'='%s'" % (TBL_PROP_POLICY_LAST_SYNCING, now),
    ]
    sql = 'ALTER TABLE `%s`.`%s` SET TBLPROPERTIES(%s)' % (db_name, tbl_name, ','.join(properties))
    if not dry_run:
        planner_conn.execute_ddl(sql)

    if not users:
        eprint('  Querying snowflake for users...')
        users = get_snowflake_users(db_conn, before_role=role)
    eprint('  Users: %s' % users)

    users = get_sync_users(users, okera_tbl.metadata)
    eprint('  Users after table configs: %s' % users)

    grants, pre_alters, row_filters, column_policies, post_alters, md5 = \
        generate_policies(planner_conn, users, db_name, tbl_name, okera_tbl,
                          per_user_role_grants=per_user_role_grants,
                          role_pattern=role_pattern)
    debug_print(grants, pre_alters, row_filters, column_policies, post_alters)

    def run(sql):
        eprint('...running: %s' % sql)
        if not dry_run:
            try:
                db_conn.query_request(sql)
            except Exception as e:
                if e.__str__().endswith(APPLY_POLICY_NOT_EXISTS_SENTINEL1) or \
                    APPLY_POLICY_NOT_EXISTS_SENTINEL2 in e.__str__():
                    for q in ACCEPTABLE_ERROR_QUERIES:
                        if q in sql:
                          eprint('......Skipping query with expected error.')
                          return
                eprint('Could not run DDL: %s' % sql)
                raise

    eprint('Running DDL against snowflake...')
    start = time.time()
    num_ddls = 0
    if grants:
        for g in grants:
            num_ddls += 1
            run(g)
    if pre_alters:
        for a in pre_alters:
            num_ddls += 1
            run(a)
    if row_filters:
        num_ddls += 1
        run(row_filters)
    if column_policies:
        for c in column_policies:
            num_ddls += 1
            run(c[2])
    if post_alters:
        for a in post_alters:
            num_ddls += 1
            run(a)
    eprint('Done updating snowflake(total ddl: %s) in %ss\n' %\
           (num_ddls, time.time() - start))

    eprint('Updating Okera catalog...')
    now = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    properties = [
        "'%s'='%s'" % (TBL_PROP_POLICY_SYNC_MD5, md5),
        "'%s'='%s'" % (TBL_PROP_POLICY_LAST_SYNC, now),
    ]
    sql = 'ALTER TABLE `%s`.`%s` SET TBLPROPERTIES(%s)' % (db_name, tbl_name, ','.join(properties))
    eprint('...Alter DDL: %s' % sql)
    if not dry_run:
        planner_conn.execute_ddl(sql)
    return grants, pre_alters, row_filters, column_policies, post_alters, md5

def sync_catalog(planner_conn, db_conn, db_role, stats, whitelist_dbs=None,
                 blacklist_dbs=None, max_syncs_per_minute=None,
                 users=None, role_pattern='"%s_ROLE"', dry_run=False):
    """
    Synchronizes all policies on all tables in the catalog.

    Parameters
    ----------
    planner_conn :
        Okera planner connection.

    db_conn :
        Connection to the underlying DB.

    whitelist_dbs: list[str], optional
        If set, only dbs that exist in the white list are synced.

    blacklist_dbs : list[str], optional
        If set, dbs in this list are not synced.

    max_syncs_per_minute : int, optional
        The maximum number of table syncs we will run per minute, rate
        limiting the process. This function will sleep if we are going
        too fast.

    dry_run : bool, optional
        If true, only run read only commands and output DDL but do not
        mutate any state.
    """

    dbs = planner_conn.list_databases()
    eprint('[sync] Syncing %s total dbs...' % len(dbs))
    total = 0
    for db in dbs:
        if whitelist_dbs is not None and db not in whitelist_dbs:
            eprint('Skipping db, did not match whitelist: %s' % db)
            continue
        if blacklist_dbs is not None and db in blacklist_dbs:
            eprint('Skipping db, part of blacklist: %s' % db)
            continue

        eprint('[sync] Syncing tables in db: %s...' % db)

        tbls = planner_conn.list_datasets(db)
        eprint('[sync] ...iterating over %s tbls.' % len(tbls))
        for tbl in tbls:
            md = tbl.metadata
            name = tbl.name
            if TBL_PROP_SYNC_ENABLED not in md or \
                  'true' != md[TBL_PROP_SYNC_ENABLED].lower():
                eprint('......skipping table which does not have sync enabled: %s.%s' %\
                    (db, name))
                continue
            if TBL_PROP_DRIVER not in md or 'snowflake' != md[TBL_PROP_DRIVER].lower():
                eprint('......skipping non-snowflake table: %s.%s' % (db, name))
                continue

            eprint('[sync] ......syncing table: %s.%s' % (db, name))
            sync_policies(planner_conn, db_conn, db, name, db_role, users=users,
                          role_pattern=role_pattern, dry_run=dry_run)
            total += 1

            # Update some stats
            now = datetime.datetime.utcnow()
            now_str = now.strftime('%Y-%m-%d %H:%M')
            if now_str not in stats:
                stats[now_str] = 0
            stats[now_str] += 1
            sync_per_min = stats[now_str]
            if max_syncs_per_minute and sync_per_min >= max_syncs_per_minute:
                # Sleep the rest of the minute
                eprint('...sleeping the rest of the minute: %ssec' % (60 - now.second))
                time.sleep(60 - now.second)
    return total

def sync_catalog_loop(planner_conn, db_conn, db_role, whitelist_dbs=None,
                      blacklist_dbs=None, max_table_syncs_per_minute=None,
                      min_sync_time_secs=None, users=None, role_pattern='"%s_ROLE"',
                      dry_run=False, iters=None):
    """
    Main loop that is expected to run forever (except for testing) to sync the
    entire catalog.
    """
    stats = {}
    n = 0
    while iters is None or n < iters:
        now = datetime.datetime.utcnow()
        start = time.time()
        eprint('[sync] ----------------------------------------------------------')
        eprint('[sync] Starting full catalog sync at %s...' % now)

        synced = sync_catalog(
            planner_conn, db_conn, db_role, stats, whitelist_dbs=whitelist_dbs,
            blacklist_dbs=blacklist_dbs, max_syncs_per_minute=max_table_syncs_per_minute,
            users=users, role_pattern=role_pattern, dry_run=dry_run)
        elapsed_sec = round(time.time() - start)

        eprint('[sync] Full catalog sync complete @ %s. Elapsed time: %s s' % \
            (datetime.datetime.utcnow(), elapsed_sec))
        eprint('[sync] ...tables synced: %s' % synced)
        eprint('Stats:')
        eprint(stats)
        eprint('[sync] ----------------------------------------------------------')

        if min_sync_time_secs and elapsed_sec < min_sync_time_secs:
            wait_sec = min_sync_time_secs - elapsed_sec
            eprint('[sync] Sleeping %s sec before next sync...' % wait_sec)
            time.sleep(wait_sec)
        n += 1


# Copyright 2019 Okera Inc. All Rights Reserved.

import json
import pytest
import unittest

from okera._thrift_api import TAuthorizeQueryClient
from okera._thrift_api import TGetDatasetsParams
from okera._thrift_api import TRecordServiceException

from okera import policy_sync
from okera.tests import pycerebro_test_common as common
from okera.tests import snowflake_cte_test_cases

from sf_test import get_snowflake_test_context, get_snowflake

SKIP_LEVELS = ["smoke", "dev", "all", "checkin"]

@pytest.mark.skip(reason="Tests legacy, unmaintained version of policy sync")
class PolicySyncTests(common.TestBase):

    def test_coalescing_queue(self):
        q = policy_sync.CoalescingEventQueue(1, 5)
        q._enqueue('a', 1)
        q._enqueue('b', 0)
        # Not visible, delay of 1
        self.assertEqual(None, q._dequeue(0))
        # Only b visible
        self.assertEqual('b', q._dequeue(1))
        self.assertEqual(None, q._dequeue(1))
        # a visible @ t=2
        self.assertEqual('a', q._dequeue(2))
        self.assertEqual(None, q._dequeue(2))

        q._enqueue('a', 1)
        q._enqueue('a', 3)
        q._enqueue('a', 5)
        self.assertEqual(None, q._dequeue(1))
        self.assertEqual(None, q._dequeue(2))
        self.assertEqual(None, q._dequeue(3))
        self.assertEqual(None, q._dequeue(4))
        self.assertEqual(None, q._dequeue(5))
        self.assertEqual('a', q._dequeue(6))

    def _init_harness1(self, conn, db, tbl):
        grant1 = """
        GRANT SELECT ON TABLE %s.%s
        WHERE if (`int` > 100, true, false)
        TO ROLE sf_test_role1
        """ % (db, tbl)

        grant2 = """
        GRANT SELECT(`int`) ON TABLE %s.%s
        TO ROLE sf_test_role2
        """ % (db, tbl)

        grant3 = """
        GRANT SELECT ON TABLE %s.%s
        TRANSFORM snowflake_test.attr with tokenize()
        TO ROLE sf_test_role3
        """ % (db, tbl)

        self._recreate_test_role(conn, 'sf_test_role1', ['sf_testuser1'])
        self._recreate_test_role(conn, 'sf_test_role2', ['sf_testuser2'])
        self._recreate_test_role(conn, 'sf_test_role3', ['sf_testuser3'])
        conn.execute_ddl('DROP ATTRIBUTE IF EXISTS snowflake_test.attr')
        conn.execute_ddl('CREATE ATTRIBUTE snowflake_test.attr')
        conn.execute_ddl(
            'ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE `int` %s'\
                % (db, tbl, 'snowflake_test.attr'))
        conn.execute_ddl(
            'ALTER TABLE %s.%s ADD COLUMN ATTRIBUTE `string` %s'\
                % (db, tbl, 'snowflake_test.attr'))
        conn.execute_ddl(grant1)
        conn.execute_ddl(grant2)
        conn.execute_ddl(grant3)

    def snowflake_basic_test(self, db, tbl, sf_tbl):
        sf_db = sf_tbl.split('.')[0]
        sf_schema = '.'.join(sf_tbl.split('.')[0:2])

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            self._init_harness1(conn, db, tbl)
            users = ['sf_testuser1', 'sf_testuser2', 'sf_testuser3', 'noone']

            request = TGetDatasetsParams()
            request.dataset_names = ['{}.{}'.format(db, tbl)]
            request.with_schema = True
            okera_tbl = conn.service.client.GetDatasets(request).datasets[0]

            grants, pre_alters, row_filters, column_policies, post_alters, md5 = \
                policy_sync.generate_policies(
                    conn, users, db, tbl, okera_tbl, per_user_role_grants=True)
            policy_sync.debug_print(
                grants, pre_alters, row_filters, column_policies, post_alters)

            string_col_policy = None
            bool_col_policy = None
            if column_policies:
                for p in column_policies:
                    if p[0] == 'string':
                        string_col_policy = p[2]
                    if p[0] == 'boolean':
                        bool_col_policy = p[2]

            self.assertEqual('bb92f9b724f790e2bcf5d801cb942b7f', md5)
            expected_grants = [
                'CREATE ROLE IF NOT EXISTS "noone_ROLE"',
                'CREATE ROLE IF NOT EXISTS "okera_ROLE"',
                'CREATE ROLE IF NOT EXISTS "sf_testuser1_ROLE"',
                'CREATE ROLE IF NOT EXISTS "sf_testuser2_ROLE"',
                'CREATE ROLE IF NOT EXISTS "sf_testuser3_ROLE"',
                'REVOKE SELECT ON %s FROM ROLE "noone_ROLE"' % sf_tbl,
                'GRANT ROLE "noone_ROLE" TO USER "noone"',
                'GRANT SELECT ON %s TO ROLE "okera_ROLE"' % sf_tbl,
                'GRANT USAGE ON DATABASE %s TO ROLE "okera_ROLE"' % sf_db,
                'GRANT USAGE ON SCHEMA %s TO ROLE "okera_ROLE"' % sf_schema,
                'GRANT SELECT ON %s TO ROLE "sf_testuser1_ROLE"' % sf_tbl,
                'GRANT USAGE ON DATABASE %s TO ROLE "sf_testuser1_ROLE"' % sf_db,
                'GRANT USAGE ON SCHEMA %s TO ROLE "sf_testuser1_ROLE"' % sf_schema,
                'GRANT ROLE "sf_testuser1_ROLE" TO USER "sf_testuser1"',
                'GRANT SELECT ON %s TO ROLE "sf_testuser2_ROLE"' % sf_tbl,
                'GRANT USAGE ON DATABASE %s TO ROLE "sf_testuser2_ROLE"' % sf_db,
                'GRANT USAGE ON SCHEMA %s TO ROLE "sf_testuser2_ROLE"' % sf_schema,
                'GRANT ROLE "sf_testuser2_ROLE" TO USER "sf_testuser2"',
                'GRANT SELECT ON %s TO ROLE "sf_testuser3_ROLE"' % sf_tbl,
                'GRANT USAGE ON DATABASE %s TO ROLE "sf_testuser3_ROLE"' % sf_db,
                'GRANT USAGE ON SCHEMA %s TO ROLE "sf_testuser3_ROLE"' % sf_schema,
                'GRANT ROLE "sf_testuser3_ROLE" TO USER "sf_testuser3"',
            ]

            expected_row_filters = '''
CREATE OR REPLACE ROW ACCESS POLICY %s_row_policy AS (int BIGINT) RETURNS boolean ->
CASE
    WHEN current_user() in ('okera', 'sf_testuser2', 'sf_testuser3') THEN TRUE
    WHEN current_user() in ('sf_testuser1') THEN iff("INT" > 100, TRUE, FALSE)
    ELSE FALSE
END''' % sf_tbl

            expected_string_col_policy = '''
CREATE OR REPLACE MASKING POLICY %s_string_masking_policy AS (string STRING) RETURNS STRING ->
CASE
    WHEN current_user() in ('okera', 'sf_testuser1') THEN string
    WHEN current_user() in ('sf_testuser2') THEN NULL
    WHEN current_user() in ('sf_testuser3') THEN okera_udfs.public.tokenize("STRING", last_query_id())
    ELSE NULL
END''' % sf_tbl

            expected_boolean_col_policy = '''
CREATE OR REPLACE MASKING POLICY %s_boolean_masking_policy AS (boolean BOOLEAN) RETURNS BOOLEAN ->
CASE
    WHEN current_user() in ('okera', 'sf_testuser1', 'sf_testuser3') THEN boolean
    WHEN current_user() in ('sf_testuser2') THEN NULL
    ELSE NULL
END''' % sf_tbl

            expected_pre_alters = [
                'ALTER TABLE %s DROP ROW ACCESS POLICY %s_row_policy' % (sf_tbl, sf_tbl),
                'ALTER TABLE %s MODIFY COLUMN VARCHAR UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_VARCHAR_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN STRING UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_STRING_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN TEXT UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_TEXT_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN SMALLINT UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_SMALLINT_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN INT UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_INT_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN BIGINT UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_BIGINT_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN INTEGER UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_INTEGER_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN DOUBLE UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_DOUBLE_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN NUMERIC UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_NUMERIC_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN NUMBER UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_NUMBER_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN DECIMAL UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_DECIMAL_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN TIMESTAMP UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_TIMESTAMP_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN CHAR UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_CHAR_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN BOOLEAN UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_BOOLEAN_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN BINARY UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_BINARY_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN VARBINARY UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_VARBINARY_masking_policy' % sf_tbl,
                'ALTER TABLE %s MODIFY COLUMN REAL UNSET MASKING POLICY' % sf_tbl,
                'DROP MASKING POLICY %s_REAL_masking_policy' % sf_tbl]

            expected_post_alters = [
                'ALTER TABLE %s ADD ROW ACCESS POLICY %s_row_policy ON(int)' % (sf_tbl, sf_tbl),
                'ALTER TABLE %s MODIFY COLUMN bigint SET MASKING POLICY %s_bigint_masking_policy' % (sf_tbl, sf_tbl)]

            self.assertEqual(expected_grants, grants)
            self.assertEqual(expected_pre_alters, pre_alters[0:len(expected_pre_alters)])
            self.assertEqual(expected_row_filters, row_filters)
            self.assertEqual(expected_string_col_policy, string_col_policy)
            self.assertEqual(expected_boolean_col_policy, bool_col_policy)
            self.assertEqual(
                expected_post_alters, post_alters[0:len(expected_post_alters)])

    def test_snowflake_policy_gen(self):
        self.maxDiff = None
        self.snowflake_basic_test(
            'jdbc_test_snowflake', 'all_types', 'DEMO_DB.JDBC_TEST.ALL_TYPES')

    def test_snowflake_test_get_users(self):
        self.maxDiff = None
        sf_ctx = get_snowflake_test_context(username='SFV3ADMIN')
        with get_snowflake(sf_ctx) as conn:
            users = policy_sync.get_snowflake_users(conn, before_role='ACCOUNTADMIN')
            self.assertTrue('OKERA_ANALYST' in users)

    def test_compute_users(self):
        users = ['a', 'b', 'c']
        props = {}

        self.assertEqual(['a', 'b', 'c'], policy_sync.get_sync_users(users, None))
        self.assertEqual(['a', 'b', 'c'], policy_sync.get_sync_users(users, props))

        props[policy_sync.TBL_PROP_USERS_LIST] = 'd,e'
        self.assertEqual(['d', 'e'], policy_sync.get_sync_users(users, props))

        props = {}
        props[policy_sync.TBL_PROP_USERS_ADDITIONAL] = 'd,e'
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], policy_sync.get_sync_users(
            users, props))

        props = {}
        props[policy_sync.TBL_PROP_USERS_BLACKLIST] = 'd,e'
        self.assertEqual(['a', 'b', 'c'], policy_sync.get_sync_users(
            users, props))
        props[policy_sync.TBL_PROP_USERS_BLACKLIST] = 'b,d,e'
        self.assertEqual(['a', 'c'], policy_sync.get_sync_users(
            users, props))

        props = {}
        props[policy_sync.TBL_PROP_USERS_WHITELIST] = 'd,e'
        self.assertEqual([], policy_sync.get_sync_users(
            users, props))
        props[policy_sync.TBL_PROP_USERS_WHITELIST] = 'b,d,e'
        self.assertEqual(['b'], policy_sync.get_sync_users(
            users, props))

        props = {}
        props[policy_sync.TBL_PROP_USERS_ADDITIONAL] = 'd,e'
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], policy_sync.get_sync_users(
            users, props))
        props[policy_sync.TBL_PROP_USERS_WHITELIST] = 'a,d,e'
        self.assertEqual(['a', 'd', 'e'], policy_sync.get_sync_users(
            users, props))
        props[policy_sync.TBL_PROP_USERS_BLACKLIST] = 'e'
        self.assertEqual(['a', 'd'], policy_sync.get_sync_users(
            users, props))

    def test_snowflake_policy_e2e(self):
        self.maxDiff = None
        sf_ctx = get_snowflake_test_context(username='SFV3ADMIN')
        ctx = common.get_test_context()

        DB = 'snowflake_policy_sync_test'
        TBL = 'all_types'
        CXN = 'snowflake_policy_sync_test_cxn'

        drc = self._get_snowflake_data_reg_connection_obj(CXN)
        drc.default_catalog = "POLICY_SYNC_TEST"
        drc.default_schema = "PUBLIC"
        drc.connection_properties = {'defaultDb':'PUBLIC'}

        with common.get_planner(ctx) as conn:
            conn.execute_ddl('DROP DATABASE IF EXISTS %s CASCADE' % DB)
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS %s' % CXN)
            drcs = conn.manage_data_reg_connection("CREATE", drc)
            conn.execute_ddl("""CREATE DATABASE %s DBPROPERTIES(
                'okera.connection.name' = '%s',
                'okera.autotagger.skip'='true')""" % (DB, CXN))
            conn.execute_ddl('ALTER DATABASE %s LOAD DEFINITIONS()' % DB)
            self._init_harness1(conn, DB, TBL)

            with get_snowflake(sf_ctx) as sf_conn:
                policy_sync.sync_policies(
                    conn, sf_conn, DB, TBL, 'ACCOUNTADMIN',
                    role_pattern='"OKERA_CI_TEST_%s_ROLE"')

    def _init_adhoc(self, conn, auto_sync):
        DB = 'snowflake_policy_sync_adhoc'
        TBL = 'patient'
        CXN = 'snowflake_policy_sync_adhoc_test_cxn'

        drc = self._get_snowflake_data_reg_connection_obj(CXN)
        drc.default_catalog = "POLICY_SYNC_ADHOC"
        drc.default_schema = "HEALTHCARE"
        drc.connection_properties = {'defaultDb':'PUBLIC'}

        self._recreate_test_role(
            conn, 'sf_test_adhoc_role',
            ['sf_testuser1', 'SFV3TEST'])

        conn.execute_ddl('DROP DATABASE IF EXISTS %s CASCADE' % DB)
        conn.execute_ddl('DROP DATACONNECTION IF EXISTS %s' % CXN)
        drcs = conn.manage_data_reg_connection("CREATE", drc)
        conn.execute_ddl("""CREATE DATABASE %s DBPROPERTIES(
            'okera.connection.name' = '%s',
            'okera.policy-sync.enabled' = 'true',
            'okera.policy-sync.auto-sync' = '%s',
            'okera.autotagger.skip'='true')""" % (DB, CXN, auto_sync))
        conn.execute_ddl('ALTER DATABASE %s LOAD DEFINITIONS()' % DB)

    def snowflake_sync_adhoc(self, auto_sync):
        ctx = common.get_test_context()

        self.maxDiff = None
        sf_ctx = get_snowflake_test_context(username='SFV3TEST')
        sf_query = 'SELECT * FROM POLICY_SYNC_ADHOC.HEALTHCARE.PATIENT LIMIT 2'

        with get_snowflake(sf_ctx) as sf_conn:
            with common.get_planner(ctx) as conn:
                self._init_adhoc(conn, auto_sync)

                # Basic just loading it, no roles, policies or attributes
                if not auto_sync:
                    conn.execute_ddl('ALTER TABLE snowflake_policy_sync_adhoc.patient EXECUTE policy_sync')
                md5_0 = conn.list_datasets(db=DB, name=TBL)[0].metadata['policy-sync.md5']
                if not auto_sync:
                    conn.execute_ddl('ALTER TABLE snowflake_policy_sync_adhoc.patient EXECUTE policy_sync')
                md5_1 = conn.list_datasets(db=DB, name=TBL)[0].metadata['policy-sync.md5']
                self.assertEqual(md5_0, md5_1)

                # Initialize this connection to use the OKERA role created by our policy
                # sync
                sf_conn.query_request('USE ROLE %s' % '"OKERA_ADHOC_SFV3TEST_ROLE"')

                # Should fail, user has no access
                with self.assertRaises(Exception) as ex_ctx:
                    sf_conn.query_request(sf_query)
                self.assertTrue(
                    'does not exist or not authorized' in str(ex_ctx.exception))

                # Grant full table access
                conn.execute_ddl("""
                    GRANT SELECT ON TABLE %s.%s
                    TO ROLE sf_test_adhoc_role
                """ % (DB, TBL))
                if not auto_sync:
                    conn.execute_ddl('ALTER TABLE snowflake_policy_sync_adhoc.patient EXECUTE policy_sync')
                md5_2 = conn.list_datasets(db=DB, name=TBL)[0].metadata['policy-sync.md5']
                self.assertTrue(md5_0 != md5_2)
                result = sf_conn.query_request(sf_query)
                self.assertEqual(result['rowset'][0][2], 'Cristy')
                self.assertEqual(result['rowset'][1][4], '337-35-7356')

                # Revoke and try again
                conn.execute_ddl("""
                    REVOKE SELECT ON TABLE %s.%s
                    FROM ROLE sf_test_adhoc_role
                """ % (DB, TBL))
                if not auto_sync:
                    conn.execute_ddl('ALTER TABLE snowflake_policy_sync_adhoc.patient EXECUTE policy_sync')
                with self.assertRaises(Exception) as ex_ctx:
                    sf_conn.query_request(sf_query)
                self.assertTrue('does not exist or not authorized' in str(ex_ctx.exception))

    @unittest.skip("Adhoc example. Cannot be run concurrently.")
    def test_snowflake_sync_adhoc(self):
        self.maxDiff = None
        self.snowflake_sync_adhoc(False)

    @unittest.skip("Adhoc example. Cannot be run concurrently.")
    def test_snowflake_auto_sync_adhoc(self):
        self.maxDiff = None
        self.snowflake_sync_adhoc(True)

    def test_catalog_sync(self):
        # Test only makes sense to run if dry_run=True
        self.maxDiff = None
        ctx = common.get_test_context()
        sf_ctx = get_snowflake_test_context(username='SFV3ADMIN')
        with get_snowflake(sf_ctx) as sf_conn:
            with common.get_planner(ctx) as conn:
                self._init_adhoc(conn, False)
                policy_sync.sync_catalog_loop(
                    conn, sf_conn, 'ACCOUNTADMIN', min_sync_time_secs=15, iters=1,
                    dry_run=True)

if __name__ == "__main__":
    unittest.main()

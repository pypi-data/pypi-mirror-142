# Copyright 2021 Okera Inc. All Rights Reserved.
#
# Latency perf suite.
#
# pylint: disable=global-statement
# pylint: disable=no-self-use

"""
+----------------------+--------------------------+-----------------+---------+---------+---------+---------+---------+-------+
|         rpc          |           name           |       user      |   mean  |   50%   |   90%   |   99%   |   max   | iters |
+----------------------+--------------------------+-----------------+---------+---------+---------+---------+---------+-------+
|   authorize_query    |      speed of light      |      admin      |  0.363  |  0.278  |  0.338  |  8.051  |  8.051  |  100  |
| get_protocol_version |   get_protocol_version   |      admin      |  0.134  |  0.131  |  0.141  |  0.200  |  0.200  |  100  |
|  get_server_version  |    get_server_version    |      admin      |  0.157  |  0.154  |  0.163  |  0.226  |  0.226  |  100  |
|   set_application    |     set_application      |      admin      |  0.144  |  0.142  |  0.148  |  0.245  |  0.245  |  100  |
| get_protocol_version |   get_protocol_version   | many_attrs_user |  0.142  |  0.139  |  0.146  |  0.211  |  0.211  |  100  |
|  get_server_version  |    get_server_version    | many_attrs_user |  0.159  |  0.160  |  0.168  |  0.221  |  0.221  |  100  |
|   set_application    |     set_application      | many_attrs_user |  0.127  |  0.126  |  0.129  |  0.187  |  0.187  |  100  |
|    list_datasets     | Wide table w/ attributes |      admin      |  58.085 |  57.021 |  59.195 |  94.535 |  94.535 |  100  |
|      get_schema      |   Wide table w/ attrs    |      admin      |  91.831 |  90.575 |  97.486 | 104.049 | 104.049 |  100  |
|    list_datasets     | Wide table w/ attributes |     testuser    | 157.722 | 155.523 | 158.222 | 193.572 | 193.572 |  100  |
|      get_schema      |   Wide table w/ attrs    |  pythonperfuser | 276.474 | 274.844 | 280.171 | 331.880 | 331.880 |  100  |
|     scan_as_json     | Wide table w/ many attrs |      admin      |  73.918 |  73.374 |  76.420 |  82.545 |  82.545 |  100  |
|      get_schema      | Wide table w/ many attrs |      admin      |  54.787 |  52.513 |  59.750 |  83.996 |  83.996 |  100  |
|     scan_as_json     | Wide table w/ many attrs | many_attrs_user | 499.488 | 490.157 | 512.780 | 772.903 | 772.903 |  100  |
|      get_schema      | Wide table w/ many attrs | many_attrs_user | 442.111 | 438.563 | 451.890 | 503.797 | 503.797 |  100  |
+----------------------+--------------------------+-----------------+---------+---------+---------+---------+---------+-------+

+--------------------+------------------+----------+---------+---------+---------+---------+---------+-------+
|        rpc         |       name       |   user   |   mean  |   50%   |   90%   |   99%   |   max   | iters |
+--------------------+------------------+----------+---------+---------+---------+---------+---------+-------+
| list_dataset_names | Many wide tables |  admin   |  15.462 |  14.772 |  16.967 |  24.237 |  24.237 |   50  |
| list_dataset_names | Many wide tables | testuser | 259.072 | 250.976 | 283.031 | 481.884 | 481.884 |   50  |
+--------------------+------------------+----------+---------+---------+---------+---------+---------+-------+
"""
import unittest
import pytest

from okera import policy_sync
from okera import _thrift_api
from okera._thrift_api import (
    TAccessPermissionLevel,
    TAccessPermissionScope,
    TAttributeMatchLevel,
    TAuthorizeQueryClient,
    TGetDatasetsParams,
    TPlanRequestParams,
    TRequestType,
)
from okera.tests import create_test_data
from okera.tests import pycerebro_test_common as common

from sf_test import get_snowflake_test_context, get_snowflake

ATTR = "perf_test.attr1"
DB = "python_perf_test_db"

TBL1 = "tbl1"
TBL2 = "tbl2"
ROLE = "python_perf_test_role"
TEST_USER = "pythonperfuser"

MANY_ATTRS_DB = "many_attrs_db"
MANY_ATTRS_TABLE = "many_attrs_tbl"
MANY_ATTRS_ROLE = "many_attrs_role"
MANY_ATTRS_USER = "many_attrs_user"

PERF = common.PerfResults()

def _create_wide_view(db, tbl, multiple, source_db, source_tbl):
    cols = []
    for idx in range(multiple):
        cols.extend([
            "uid AS uid%04d" % (idx),
            "dob AS dob%04d" % (idx),
            "gender AS gender%04d" % (idx),
            "ccn AS ccn%04d" % (idx),
        ])
    stmt = "CREATE VIEW %s.%s AS SELECT %s FROM %s.%s" % (
        db, tbl, ', '.join(cols), source_db, source_tbl)

    return stmt

@pytest.mark.perf
class PerfTest(common.TestBase):
    @classmethod
    def tearDownClass(cls):
        PERF.finalize_results()

    @classmethod
    def setUpClass(cls):
        if not PERF.run_perf():
            return
        if PERF.skip_data_load():
            print("Skipping data load.")
            return

        print("\n\nSetting up perf test.")

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            print("...Creating wide view")
            ddls = [
                "DROP ATTRIBUTE IF EXISTS %s" % (ATTR),
                "CREATE ATTRIBUTE %s" % (ATTR),

                "DROP DATABASE IF EXISTS %s CASCADE" % (DB),
                "CREATE DATABASE %s" % (DB),

                """CREATE TABLE {db}.users (
                  uid STRING ATTRIBUTE {attr},
                  dob STRING ATTRIBUTE {attr},
                  gender STRING ATTRIBUTE {attr},
                  ccn STRING ATTRIBUTE {attr}
                )""".format(db=DB, attr=ATTR),

                _create_wide_view(DB, TBL1, 100, DB, 'users'),

                "DROP ROLE IF EXISTS %s" % (ROLE),
                "CREATE ROLE %s WITH GROUPS %s" % (ROLE, TEST_USER),
                "GRANT SELECT ON DATABASE %s HAVING ATTRIBUTE IN (%s) TO ROLE %s" % \
                    (DB, ATTR, ROLE),
            ]

            for ddl in ddls:
                conn.execute_ddl(ddl)

            print("...Creating xilinx test case")
            create_test_data.create_xilinx_tbl1(
                conn, MANY_ATTRS_DB, MANY_ATTRS_TABLE, MANY_ATTRS_ROLE, MANY_ATTRS_USER)
        print("...Done setting up perf test")

    @unittest.skipIf(not PERF.run_perf(), "Skipping perf tests")
    def test_list_roles(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            print("...Setting up list_roles test")
            total_roles = 150
            role_prefix = "list_roles_test"
            user_prefix = "list_roles_user"
            for i in range(total_roles):
                role_name = role_prefix + str(i)
                user_name = user_prefix + str(i)
                conn.execute_ddl("CREATE ROLE IF NOT EXISTS %s WITH GROUPS %s" % \
                                 (role_name, user_name))
                conn.execute_ddl("""
                GRANT IF NOT EXISTS SELECT ON DATABASE %s
                HAVING ATTRIBUTE IN (%s)
                TO ROLE %s
                POLICYPROPERTIES(
                    'enabled'='true',
                    'start_datetime'='543453453',
                    'end_datetime'='543453459')
                """ % (DB, ATTR, role_name))
                conn.execute_ddl("""
                GRANT IF NOT EXISTS SELECT ON TABLE %s.%s
                TO ROLE %s
                POLICYPROPERTIES('enabled'='true')
                """ % (DB, TBL1, role_name))

            def list(t_params, expected_results):
                def get():
                    t_params.return_structured_exprs = True
                    t_params.limit = 10000
                    roles = conn._underlying_client().ListRoles(t_params)
                    assert len(roles.roles) == expected_results
                return get

            print("...starting perf run for list_roles")

            t_params = _thrift_api.TListRolesParams()
            PERF.measure(list(t_params, total_roles + 7), "Listing Roles",
                         "admin", "ListRoles")

            t_params = _thrift_api.TListRolesParams()
            t_params.scopes = [TAccessPermissionScope.DATABASE]
            PERF.measure(list(t_params, total_roles + 3), "Listing Roles w/scope filter",
                         "admin", "ListRoles")

            t_params = _thrift_api.TListRolesParams()
            t_params.group_names = [
                "list_roles_user1",
                "list_roles_user125",
                "list_roles_user10",
                "no_match"]
            PERF.measure(list(t_params, 3), "Listing Roles w/group_names filter",
                         "admin", "ListRoles")

            t_params = _thrift_api.TListRolesParams()
            t_params.role_name_substring = role_prefix
            PERF.measure(list(t_params, total_roles),
                         "Listing Roles w/role name substring filter",
                         "admin", "ListRoles")

    def _init_snowflake_setup(self, conn, ddls_params):
        setup_ddls = [
            "DROP DATABASE IF EXISTS {db} CASCADE INCLUDING PERMISSIONS",
            "CREATE DATABASE {db}",
            """
              CREATE DATACONNECTION IF NOT EXISTS {conn} CXNPROPERTIES
                (
                  'connection_type' = 'JDBC',
                  'driver' = 'snowflake',
                  'account' = 'vq85960',
                  'host' = 'vq85960.snowflakecomputing.com',
                  'port'= '443',
                  'user'= 'awssm://okera/demo/snowflake/username',
                  'password' = 'awssm://okera/demo/snowflake/password',
                  'jdbc.db.name' = 'OKERA_DEMO'
                )""",
            """
              CREATE EXTERNAL TABLE {db}.hospital_discharge
              STORED AS JDBC
              TBLPROPERTIES(
                'driver' = 'snowflake',
                'okera.connection.name' = '{conn}',
                'jdbc.db.name' = 'OKERA_DEMO',
                'jdbc.schema.name' = 'HEALTHCARE',
                'table' = 'HOSPITAL_DISCHARGE'
              )
            """,
            """
              CREATE EXTERNAL TABLE {db}.patient
              STORED AS JDBC
              TBLPROPERTIES(
                'driver' = 'snowflake',
                'okera.connection.name' = '{conn}',
                'jdbc.db.name' = 'OKERA_DEMO',
                'jdbc.schema.name' = 'HEALTHCARE',
                'table' = 'PATIENT'
              )
            """,
            "DROP ROLE IF EXISTS {role}",
            "CREATE ROLE {role}",
            "GRANT ROLE {role} TO GROUP {group}",
            "GRANT SELECT ON DATABASE {db} TO ROLE {role}",
        ]

        for ddl_tmpl in setup_ddls:
            ddl = ddl_tmpl.format(**ddls_params)
            conn.execute_ddl(ddl)

    @unittest.skipIf(not PERF.run_perf_snowflake(), "Skipping snowflake perf tests")
    def test_measure_snowflake_speed_of_light(self):
        sf_ctx = get_snowflake_test_context()
        setup_ddls_params = {
            'conn' : 'snowflake_connection_demo',
            'group' : sf_ctx.username,
            'role' : 'test_perf_sf_role',
            'db' : 'test_perf_sf',
        }

        planner_ctx = common.get_test_context()
        with common.get_planner(planner_ctx) as conn:
            self._init_snowflake_setup(conn, setup_ddls_params)

        def conn_query(conn):
            def get():
                res = conn.query_request(
                    "SELECT * FROM OKERA_DEMO.HEALTHCARE.PATIENT LIMIT 1")
                assert len(res.get('rowset')) == 1
            return get

        with get_snowflake(sf_ctx) as conn:
            conn.query_request("USE ROLE {}".format(sf_ctx.user_role))
            PERF.measure(conn_query(conn), "sfproxy: speed of light",
                         sf_ctx.username, "sfproxy_query_request")

    @unittest.skipIf(not PERF.run_perf_snowflake(), "Skipping snowflake perf tests")
    def test_measure_snowflake_generate_policy_sync(self):
        sf_ctx = get_snowflake_test_context(username='SFV3ADMIN')
        setup_ddls_params = {
            'conn' : 'snowflake_connection_demo',
            'group' : sf_ctx.username,
            'role' : 'test_perf_sf_role',
            'db' : 'test_perf_sf',
        }

        planner_ctx = common.get_test_context()
        with common.get_planner(planner_ctx) as conn:
            self._init_snowflake_setup(conn, setup_ddls_params)
            request = TGetDatasetsParams()
            request.dataset_names = ['{}.{}'.format('test_perf_sf', 'patient')]
            request.with_schema = True
            okera_tbl = conn.service.client.GetDatasets(request).datasets[0]

        with get_snowflake(sf_ctx) as conn:
            users = policy_sync.get_snowflake_users(conn, before_role='ACCOUNTADMIN')

        def generate(conn):
            def get():
                res = policy_sync.generate_policies(
                    conn, users, 'test_perf_sf', 'patient', okera_tbl)
                assert res is not None
            return get

        with common.get_planner(planner_ctx) as conn:
            PERF.measure(generate(conn), "generate policy sync (all sf users)",
                         'admin', "generate_policies")

    @unittest.skipIf(not PERF.run_perf(), "Skipping perf tests")
    def test_wide_table_with_attributes(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            def list(tbl):
                def get():
                    datasets = conn.list_datasets(DB, name=tbl)
                    assert len(datasets) >= 1
                return get

            def describe(user, plan):
                def fn():
                    params = TPlanRequestParams()
                    params.request_type = TRequestType.Sql
                    params.requesting_user = user
                    params.sql_stmt = \
                        'select * from %s.%s' % (DB, TBL1)
                    if plan:
                        conn.service.client.PlanRequest(params)
                    else:
                        conn.service.client.GetSchema(params)
                return fn

            PERF.measure(list(TBL1), "Wide table w/ attributes",
                         "admin", "list_datasets")
            PERF.measure(describe(None, False), "Wide table w/ attrs",
                         "admin", "get_schema")
            PERF.measure(describe(None, True), "Wide table w/ attrs",
                         "admin", "plan_request")

            ctx.enable_token_auth(token_str=TEST_USER)
            PERF.measure(list(TBL1), "Wide table w/ attributes",
                         TEST_USER, "list_datasets")
            PERF.measure(describe(TEST_USER, False), "Wide table w/ attrs",
                         TEST_USER, "get_schema")
            PERF.measure(describe(TEST_USER, True), "Wide table w/ attrs",
                         TEST_USER, "plan_request")

    @unittest.skipIf(not PERF.run_perf(), "Skipping perf tests")
    def test_xilinx_table(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            def scan():
                conn.scan_as_json(
                    'select * from %s.%s' % (MANY_ATTRS_DB, MANY_ATTRS_TABLE))

            def describe(user, plan):
                def fn():
                    params = TPlanRequestParams()
                    params.request_type = TRequestType.Sql
                    params.requesting_user = user
                    params.sql_stmt = \
                        'select * from %s.%s' % (MANY_ATTRS_DB, MANY_ATTRS_TABLE)
                    if plan:
                        conn.service.client.PlanRequest(params)
                    else:
                        conn.service.client.GetSchema(params)
                return fn

            PERF.measure(scan, "Wide table w/ many attrs",
                         "admin", "scan_as_json")
            PERF.measure(describe(None, False), "Wide table w/ many attrs",
                         "admin", "get_schema")
            PERF.measure(describe(None, True), "Wide table w/ many attrs",
                         "admin", "plan_request")

            ctx.enable_token_auth(token_str=MANY_ATTRS_USER)
            PERF.measure(scan, "Wide table w/ many attrs",
                         MANY_ATTRS_USER, "scan_as_json")
            PERF.measure(describe(MANY_ATTRS_USER, False), "Wide table w/ many attrs",
                         MANY_ATTRS_USER, "get_schema")
            PERF.measure(describe(MANY_ATTRS_USER, True), "Wide table w/ many attrs",
                         MANY_ATTRS_USER, "plan_request")

    @unittest.skipIf(not PERF.run_perf(), "Skipping perf tests")
    def test_measure_speed_of_light(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            def get():
                self.authorize_query(
                    conn, "select 1", client=TAuthorizeQueryClient.TEST_ACK)
            PERF.measure(get, "speed of light",
                         "admin", "authorize_query")

    @unittest.skipIf(not PERF.run_perf(), "Skipping perf tests")
    def test_measure_status_apis(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            def set_application():
                conn.service.client.SetApplication('perf-test')
            def get_metric():
                conn.service.client.GetMetric('perf-test')

            PERF.measure(lambda: conn.get_protocol_version(),
                         'get_protocol_version', 'admin', 'get_protocol_version')
            PERF.measure(lambda: conn.get_server_version(),
                         'get_server_version', 'admin', 'get_server_version')
            PERF.measure(lambda: conn.set_application('perf-test'),
                         'set_application', 'admin', 'set_application')
            PERF.measure(get_metric, 'get_metric', 'admin', 'get_metric')
            ctx.enable_token_auth(token_str=MANY_ATTRS_USER)
            PERF.measure(lambda: conn.get_protocol_version(),
                         'get_protocol_version', MANY_ATTRS_USER, 'get_protocol_version')
            PERF.measure(lambda: conn.get_server_version(),
                         'get_server_version', MANY_ATTRS_USER, 'get_server_version')
            PERF.measure(lambda: conn.set_application('perf-test'),
                         'init_application', MANY_ATTRS_USER, 'init_application')
            PERF.measure(set_application,
                         'set_application', MANY_ATTRS_USER, 'set_application')

    @unittest.skipIf(not PERF.run_perf(), "Skipping perf tests")
    def test_measure_list_datbases_api(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            def list_db(db=None, pattern=None, tags=None, match_level=None, privilege=None):
                def get():
                    if db is not None:
                        result = conn.list_databases_v2(exact_names_filter=[db])
                        assert len(result.databases) >= 1
                    if pattern is not None:
                        result = conn.list_databases_v2(name_pattern_filter=pattern)
                        assert len(result.databases) >= 1
                    if privilege is not None:
                        result = conn.list_databases_v2(privilege=privilege, limit=1000)
                        returned_dbs = []
                        for database in result.databases:
                            returned_dbs.append(database.name)
                            print("shashi : %s" % database.name)
                        assert ([DB] in returned_dbs)
                    if tags is not None:
                        result = conn.list_databases_v2(
                            tags=tags, tag_match_level=match_level)
                        assert len(result.databases) >= 1
                return get

            pattern = '*perf_test*'
            attr = common.TestBase._get_t_attribute_obj('perf_test', 'attr1')
            priv = TAccessPermissionLevel.SELECT

            PERF.measure(list_db(db=DB), "Exact name filter",
                         "admin", "list_databases_v2")
            PERF.measure(list_db(pattern=pattern), "Pattern filter",
                         "admin", "list_databases_v2")
            PERF.measure(list_db(privilege=priv), "Privilege filter",
                         "admin", "list_databases_v2")
            PERF.measure(list_db(tags=[attr],
                         match_level=TAttributeMatchLevel.DATABASE_PLUS),
                         "Attributes filter", "admin", "list_databases_v2")

            ctx.enable_token_auth(token_str=TEST_USER)
            PERF.measure(list_db(db=DB), "Exact name filter",
                         TEST_USER, "list_databases_v2")
            PERF.measure(list_db(pattern=pattern), "Pattern filter",
                         TEST_USER, "list_databases_v2")
            PERF.measure(list_db(privilege=priv), "Privilege filter",
                         TEST_USER, "list_databases_v2")
            PERF.measure(list_db(tags=[attr],
                         match_level=TAttributeMatchLevel.DATABASE_PLUS),
                         "Attributes filter", TEST_USER, "list_databases_v2")

    @unittest.skipIf(not PERF.run_perf(), "Skipping perf tests")
    def test_measure_list_datasets(self):
        TEST_ROLE1 = "test_list_datasets_role1"
        TEST_USER1 = "test_list_datasets_user1"
        TEST_ROLE2 = "test_list_datasets_role2"
        TEST_USER2 = "test_list_datasets_user2"
        TEST_ROLE3 = "test_list_datasets_role3"
        TEST_USER3 = "test_list_datasets_user3"
        db = 'perf_test_db_many_wide_tables'
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            db = create_test_data.require(
                PERF, conn, create_test_data.DataHarness.LARGE_DB_WIDE_TABLES, db=db)
            def list(user=None):
                def get():
                    datasets = conn.list_datasets(db, requesting_user=user)
                    assert len(datasets) == 25
                return get

            self._recreate_test_role(conn, TEST_ROLE1, [TEST_USER1])
            self._recreate_test_role(conn, TEST_ROLE2, [TEST_USER2])
            self._recreate_test_role(conn, TEST_ROLE3, [TEST_USER3])

            conn.execute_ddl(('GRANT SELECT ON DATABASE %s ' +
                              'TRANSFORM %s.email WITH sha2() ' +
                              'TO ROLE %s') % (db, db, TEST_ROLE1))
            conn.execute_ddl(('GRANT SELECT ON CATALOG ' +
                              'TRANSFORM %s.email WITH sha2() ' +
                              'TO ROLE %s') % (db, TEST_ROLE2))
            conn.execute_ddl(('GRANT SELECT ON CATALOG HAVING ATTRIBUTE %s.email ' +
                              'TRANSFORM %s.email WITH sha2() ' +
                              'TO ROLE %s') % (db, db, TEST_ROLE3))

            PERF.measure(list(), "multiple wide tables in db",
                         "admin", "list_datasets")
            PERF.measure(list(TEST_USER1), "multiple wide tables in db",
                         TEST_USER1, "list_datasets")
            PERF.measure(list(TEST_USER2), "multiple wide tables in db",
                         TEST_USER2, "list_datasets")
            #PERF.measure(list(TEST_USER3), "multiple wide tables in db",
            #             TEST_USER3, "list_datasets")

    @unittest.skipIf(not PERF.run_perf(), "Skipping perf tests")
    def test_measure_recover_partitions(self):
        db = 'perf_test_trial_analytics'
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            def recover():
                self._recreate_test_db(conn, db)
                conn.execute_ddl('''
                    CREATE EXTERNAL TABLE %s.audit_logs(
                      request_time STRING
                    )
                    PARTITIONED BY (tenant string, ymd string)
                    STORED AS JSON
                    LOCATION 's3://okera-trial-us-west-2-e71015d/tenants/logs/audit/'
                    ''' % db)
                conn.execute_ddl('''
                    CREATE EXTERNAL TABLE %s.web_analytics(
                      event_time STRING
                    )
                    PARTITIONED BY (tenant string, ymd string)
                    STORED AS JSON
                    LOCATION 's3://okera-trial-us-west-2-e71015d/tenants/logs/analytics/'
                    ''' % db)
                conn.execute_ddl(
                    'ALTER TABLE %s.audit_logs RECOVER PARTITIONS' %  db)
                conn.execute_ddl(
                    'ALTER TABLE %s.web_analytics RECOVER PARTITIONS' % db)
            PERF.measure(recover, 'recover partition with many folders and files',
                         None, '', iters=5)

            def show():
                res = conn.execute_ddl('SHOW PARTITIONS %s.audit_logs' % db)
                self.assertTrue(len(res) > 2000)
            def show_files():
                res = conn.execute_ddl('SHOW FILES IN %s.audit_logs' % db)
            PERF.measure(show, 'show thousands partitions',
                         None, '')
            PERF.measure(show_files, 'show thousands files in partitions',
                         None, '')

    @unittest.skipIf(not PERF.run_perf(), "Skipping perf tests")
    def test_list_table_names(self):
        db = 'perf_test_large_db'
        ctx = common.get_test_context()
        role = 'perf_test_large_db_role'
        user = 'perf_test_large_db_user'
        with common.get_planner(ctx) as conn:
            self._recreate_test_role(conn, role, [user])
            conn.delete_attribute(db, 'financial')
            conn.create_attribute(db, 'financial')
            conn.delete_attribute(db, 'phone_number')
            conn.create_attribute(db, 'phone_number')
            conn.delete_attribute(db, 'credit_card')
            conn.create_attribute(db, 'credit_card')
            create_test_data.create_large_db_wide_tables_attributes(conn, db, 1000)
            conn.execute_ddl(('GRANT SELECT ON CATALOG ' +
                              'HAVING ATTRIBUTE NOT IN (%s.financial) ' +
                              'TRANSFORM %s.email WITH sha2() ' +
                              'TRANSFORM %s.phone_number WITH sha2() ' +
                              'TRANSFORM %s.credit_card WITH mask() ' +
                              'TRANSFORM %s.person WITH mask() ' +
                              'TO ROLE %s') % (db, db, db, db, db, role))

            def ls():
                conn.list_dataset_names(db)

            PERF.measure(ls, "Many wide tables", "admin", "list_dataset_names")

            ctx.enable_token_auth(token_str=user)
            PERF.measure(ls, "Many wide tables", "testuser", "list_dataset_names")


    # TODO: missing RPCs
    # TExecDDLResult ExecuteDDL2(1:TExecDDLParams ddl)
    # throws(1:RecordService.TRecordServiceException ex);
    # TGetInfoResult GetInfo(1: TGetInfoParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    #
    # TGetAuthenticatedUserResult AuthenticatedUser(1:string token)
    # throws(1:RecordService.TRecordServiceException ex);
    #
    # TGetDatabasesResult GetDatabases(1:TGetDatabasesParams params)
    #     throws(1:TRecordServiceException ex);
    # TGetTablesResult GetTables(1:TGetTablesParams params)
    # throws(1:TRecordServiceException ex);
    # TGetPartitionsResult GetPartitions(1:TGetPartitionsParams params)
    # throws(1:TRecordServiceException ex);
    # TGetDatasetsResult GetDatasets(1:TGetDatasetsParams params)
    # throws(1:RecordService.TRecordServiceException ex);
    #
    # TGetAccessPermissionsResult GetAccessPermissions(1: TGetAccessPermissionsParams p)
    # throws(1:RecordService.TRecordServiceException ex);
    # TGetRoleProvenanceResult GetRoleProvenance(1: TGetRoleProvenanceParams params)
    # throws(1:RecordService.TRecordServiceException ex);
    # TGetGrantableRolesResult GetGrantableRoles(1: TGetGrantableRolesParams params)
    # throws(1:RecordService.TRecordServiceException ex);
    #
    # TGetUdfsResult GetUdfs(1:TGetUdfsParams params)
    # throws(1:RecordService.TRecordServiceException ex);
    #
    # TAddRemovePartitionsResult AddRemovePartitions(1:TAddRemovePartitionsParams params)
    # throws(1:RecordService.TRecordServiceException ex);
    #
    # TListFilesResult ListFiles(1:TListFilesParams params)
    # throws(1:RecordService.TRecordServiceException ex);
    # TGetRegisteredObjectsResult GetRegisteredObjects(1: TGetRegisteredObjectsParams p)
    #  throws(1:RecordService.TRecordServiceException ex);
    #
    # TCreateAttributesResult CreateAttributes(1:TCreateAttributesParams params)
    #  throws(1:RecordService.TRecordServiceException ex);
    # TGetAttributesResult GetAttributes(1: TGetAttributesParams params)
    #  throws(1:RecordService.TRecordServiceException ex);
    # TGetCountResult GetRecordCount(1: TGetCountParams params)
    #  throws(1:RecordService.TRecordServiceException ex);
    # TAssignAttributesResult AssignAttributes(1: TAssignAttributesParams params)
    #  throws(1:RecordService.TRecordServiceException ex);
    # TUnassignAttributesResult UnassignAttributes(1: TUnassignAttributesParams params)
    #  throws(1:RecordService.TRecordServiceException ex);
    # TDeleteAttributesResult DeleteAttributes(1: TDeleteAttributesParams params)
    #  throws(1:RecordService.TRecordServiceException ex);
    # TGetAttributeNamespacesResult GetAttributeNamespaces(
    #    1: TGetAttributeNamespacesParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    # TSetAttributesResult SetAttributes(1: TSetAttributesParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    # TUpdateAttributeMappingsResult UpdateAttributeMappings(
    #    1: TUpdateAttributeMappingsParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    #
    # TConfigChangeResult UpsertConfig(1: TConfigUpsertParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    # TConfigChangeResult DeleteConfig(1: TConfigDeleteParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    #
    # TLogInfoResult LogInfo(1: TLogInfoParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    #
    # TRefreshCredentialsResult RefreshCredentials(1: TRefreshCredentialsParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    #
    # TDataRegConnectionResult ManageDataRegConnection(1: TDataRegConnectionParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    # TDiscoverCrawlerResult DiscoverCrawler(1: TDiscoverCrawlerParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    # TCrawlerResult ManageCrawler(1: TCrawlerParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    # TCrawlDatasetResult ManageCrawlerDataset(1: TCrawlDatasetParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    #
    # TAuditQueryResult AuditQuery(1: TAuditQueryParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    #
    # TListCatalogsResult ListCatalogs(1: TListCatalogsParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    # TListDatabasesResult ListDatabases(1: TListDatabasesParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    #
    # TKvStoreGetResult GetFromKvStore(1: TKvStoreGetParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    # TKvStorePutResult PutToKvStore(1: TKvStorePutParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    #
    # TGetUserAttributesResult GetUserAttributes(1: TGetUserAttributesParams params)
    #    throws(1:RecordService.TRecordServiceException ex);
    #
    # TEvalResult Eval(1: TEvalParams params)
    #    throws(1:RecordService.TRecordServiceException ex);


# Copyright 2020 Okera Inc. All Rights Reserved.
#
# Some integration tests for auth in PyOkera
#
# pylint: disable=global-statement
# pylint: disable=no-self-use
# pylint: disable=no-else-return
# pylint: disable=duplicate-code

import unittest

#from okera import context, _thrift_api
#from datetime import datetime
from okera.tests import pycerebro_test_common as common
from okera._thrift_api import (
    TDataRegConnection, TRecordServiceException, TCrawlStatus,
    TAccessPermissionLevel, TDataRegConnection)

from okera import _thrift_api

EMPTY_DRC = TDataRegConnection()
EMPTY_DRC.name = ''

# level, can show, can alter, can drop, can use
CONNECTION_PRIVILEGES = [
    (TAccessPermissionLevel.ALL, True, True, True, True),
    (TAccessPermissionLevel.SHOW, True, False, False, False),
    (TAccessPermissionLevel.ALTER, True, True, False, False),
    (TAccessPermissionLevel.DROP, True, False, True, False),
    (TAccessPermissionLevel.USE, True, False, False, True),
]

def get_connection_as_root(conn, name, resolve_creds=None):
    drc = TDataRegConnection()
    drc.name = name

    orig_user = conn.ctx._get_user()
    conn.ctx.disable_auth()
    connections = conn.manage_data_reg_connection("GET", drc,
            resolve_creds=resolve_creds).connections
    conn.ctx.enable_token_auth(token_str=orig_user)

    return connections[0]

def get_connection(conn, name, resolve_creds=None):
    drc = TDataRegConnection()
    drc.name = name

    connections = conn.manage_data_reg_connection("GET", drc,
            resolve_creds=resolve_creds).connections
    return connections[0]

def delete_connection(conn, name):
    drc = get_connection_as_root(conn, name)

    return conn.manage_data_reg_connection("DELETE", drc)

def update_connection(conn, name):
    drc = get_connection_as_root(conn, name)

    return conn.manage_data_reg_connection("UPDATE", drc)

def create_connection(conn, drc):
    return conn.manage_data_reg_connection("CREATE", drc)

def run_test_connection(conn, name):
    drc = get_connection_as_root(conn, name)

    return conn.manage_data_reg_connection("TEST_EXISTING", drc)

# Run TEST on a connection prior to it being created
def run_test_connection_on_new(conn, drc):
    return conn.manage_data_reg_connection("TEST_CREATE", drc)

def discover_crawler(conn, name):
    drc = get_connection_as_root(conn, name)

    return conn.discover_crawler(drc)

def manage_crawler(conn, name):
    drc = get_connection_as_root(conn, name)

    return conn.manage_crawler(drc)

class DataRegistrationTest(common.TestBase):
    @classmethod
    def setUpClass(cls):
        """ Initializes one time state that is shared across test cases. This is used
            to speed up the tests. State that can be shared across (but still stable)
            should be here instead of __cleanup()."""
        super(DataRegistrationTest, cls).setUpClass()
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS test_connection_name')
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS test_connection_name_2')
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS mysql_test_connection')
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS mssql_test_connection')
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS snwflk_test_connection')

    @staticmethod
    def _contains_attribute(namespace, key, attributes):
        for attr in attributes:
            if attr.attribute_namespace == namespace and attr.key == key:
                return True
        return False

    def _get_psqltest_data_reg_connection_obj(self, name):
        data_reg_connection = TDataRegConnection()
        data_reg_connection.name = name
        data_reg_connection.type = "JDBC"
        data_reg_connection.data_source_path = 's3://cerebro-datasets/' \
            'jdbc_demo/jdbc_test_psql.conf'
        data_reg_connection.jdbc_driver = "postgresql"
        data_reg_connection.host = "jdbcpsqltest.cyn8yfvyuugz.us-west-2.rds.amazonaws.com"
        data_reg_connection.port = 5432
        data_reg_connection.user_key = "awssm://postgres-jdbcpsqltest-username"
        data_reg_connection.password_key = "awssm://postgres-jdbcpsqltest-password"
        data_reg_connection.default_catalog = "jdbc_test"
        data_reg_connection.default_schema = "public"
        data_reg_connection.is_active = True
        data_reg_connection.connection_properties = {'ssl':'False'}
        return data_reg_connection

    def _get_mysqltest_data_reg_connection_obj(self, name):
        data_reg_connection = TDataRegConnection()
        data_reg_connection.name = name
        data_reg_connection.type = "JDBC"
        data_reg_connection.data_source_path = None
        data_reg_connection.jdbc_driver = "mysql"
        data_reg_connection.host = 'cerebro-db-test-long-running.cyn8yfvyuugz.' \
            'us-west-2.rds.amazonaws.com'
        data_reg_connection.port = 3306
        data_reg_connection.user_key = "awssm://mysql-username"
        data_reg_connection.password_key = "awssm://mysql-password"
        data_reg_connection.default_catalog = "jdbc_test"
        data_reg_connection.default_schema = None
        data_reg_connection.is_active = True
        data_reg_connection.connection_properties = {'ssl':'False'}
        return data_reg_connection

    def _get_mssqltest_data_reg_connection_obj(self, name):
        data_reg_connection = TDataRegConnection()
        data_reg_connection.name = name
        data_reg_connection.type = "JDBC"
        data_reg_connection.data_source_path = None
        data_reg_connection.jdbc_driver = "sqlserver"
        data_reg_connection.host = 'mssql-server-test.cyn8yfvyuugz.' \
            'us-west-2.rds.amazonaws.com'
        data_reg_connection.port = 1433
        data_reg_connection.user_key = "awssm://mssql-username"
        data_reg_connection.password_key = "awssm://mssql-password"
        data_reg_connection.default_catalog = "okera_test"
        data_reg_connection.default_schema = None
        data_reg_connection.is_active = True
        data_reg_connection.connection_properties = {'ssl':'False'}
        return data_reg_connection

    def _verify_mssql_table_schema(self, ret_list_jdbc_datasets, \
        ret_jdbc_schema, ret_jdbc_table):
        for dataset in ret_list_jdbc_datasets:
            if dataset.jdbc_schema == ret_jdbc_schema and \
                dataset.jdbc_table == ret_jdbc_table:
                for col in dataset.schema.cols:
                    if col.name == 'varchar':
                        self.assertTrue(col.type.type_id == 8) #TTypeId=8=VARCHAR
                        self.assertTrue(col.type.len == 20)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'text':
                        self.assertTrue(col.type.type_id == 7)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'tinyint':
                        self.assertTrue(col.type.type_id == 1)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'smallint':
                        self.assertTrue(col.type.type_id == 2)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'int':
                        self.assertTrue(col.type.type_id == 3)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'bigint':
                        self.assertTrue(col.type.type_id == 4)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'date':
                        self.assertTrue(col.type.type_id == 16)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'float_col':
                        self.assertTrue(col.type.type_id == 6)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'decimal':
                        self.assertTrue(col.type.type_id == 10)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision == 10)
                        self.assertTrue(col.type.scale == 2)
                    elif col.name == 'datetime':
                        self.assertTrue(col.type.type_id == 11)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'timestamp':
                        self.assertTrue(col.type.type_id == 15)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'time':
                        self.assertTrue(col.type.type_id == 11)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'char':
                        self.assertTrue(col.type.type_id == 9)
                        self.assertTrue(col.type.len == 10)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'binary':
                        self.assertTrue(col.type.type_id == 15)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'varbinary':
                        self.assertTrue(col.type.type_id == 15)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)

    def _verify_mysql_table_schema(self, ret_list_jdbc_datasets, \
        ret_jdbc_schema, ret_jdbc_table):
        for dataset in ret_list_jdbc_datasets:
            if dataset.jdbc_schema == ret_jdbc_schema and \
                dataset.jdbc_table == ret_jdbc_table:
                for col in dataset.schema.cols:
                    if col.name == 'varchar':
                        self.assertTrue(col.type.type_id == 8) #TTypeId=8=VARCHAR
                        self.assertTrue(col.type.len == 20)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'text':
                        self.assertTrue(col.type.type_id == 8)
                        self.assertTrue(col.type.len == 65355)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'double':
                        self.assertTrue(col.type.type_id == 6)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'date':
                        self.assertTrue(col.type.type_id == 16)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'float':
                        self.assertTrue(col.type.type_id == 6)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'decimal':
                        self.assertTrue(col.type.type_id == 10)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision == 10)
                        self.assertTrue(col.type.scale == 2)
                    elif col.name == 'datetime':
                        self.assertTrue(col.type.type_id == 11)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'timestamp':
                        self.assertTrue(col.type.type_id == 11)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'time':
                        self.assertTrue(col.type.type_id == 11)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'year':
                        self.assertTrue(col.type.type_id == 16)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'char':
                        self.assertTrue(col.type.type_id == 9)
                        self.assertTrue(col.type.len == 10)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'enum':
                        self.assertTrue(col.type.type_id == 9)
                        self.assertTrue(col.type.len == 1)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'set':
                        self.assertTrue(col.type.type_id == 9)
                        self.assertTrue(col.type.len == 5)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)
                    elif col.name == 'bool':
                        self.assertTrue(col.type.type_id == 0)
                        self.assertTrue(col.type.len is None)
                        self.assertTrue(col.type.precision is None)
                        self.assertTrue(col.type.scale is None)

    def test_drc_crud_backwards_compat_test(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:

            # Clean if already exists
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS test_connection_name_bc')
            drc = self._get_psqltest_data_reg_connection_obj("test_connection_name_bc")

            # create test
            drc.username = "awssm://postgres-jdbcpsqltest-username"
            drc.password = "awssm://postgres-jdbcpsqltest-password"
            drcs = conn.manage_data_reg_connection("CREATE", drc)
            self.assertTrue(len(drcs.connections) == 1)

            # update test
            drc.host = "test_host_name_mod_bc"
            drcs = conn.manage_data_reg_connection("UPDATE", drc)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertEqual(drcs.connections[0].host,
                             "test_host_name_mod_bc",
                             "Update data registration object connection failed.")

            # get test
            drcs = conn.manage_data_reg_connection("GET", drc)
            self.assertTrue(len(drcs.connections) == 1)

            # list with filters works as expected
            drcs = conn.manage_data_reg_connection(
                "LIST", drc, ["test_connection_name_bc"])
            self.assertTrue(len(drcs.connections) >= 1)
            connection_names = [names.name for names in drcs.connections]
            self.assertTrue("test_connection_name_bc" in connection_names,
                            "list data registration object connection failed.")

            # create another one
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS test_connection_name_mysql')
            drc = self._get_mysqltest_data_reg_connection_obj("test_connection_name_mysql")
            drcs = conn.manage_data_reg_connection("CREATE", drc)
            self.assertTrue(len(drcs.connections) == 1)

            # list with empty filter should still return all
            drcs = conn.manage_data_reg_connection(
                "LIST", drc, [])
            self.assertTrue(len(drcs.connections) >= 2)
            connection_names = [names.name for names in drcs.connections]
            self.assertTrue("test_connection_name_bc" in connection_names,
                            "list data registration object connection failed.")
            self.assertTrue("test_connection_name_mysql" in connection_names,
                            "list data registration object connection failed.")

            # list with pattern search works as expected
            drcs = conn.manage_data_reg_connection(
                "LIST", drc, ["test_connection_name_bc", "test_connection_name_mysql"])
            self.assertTrue(len(drcs.connections) >= 2)

            # list with jdbc driver search works as expected
            drcs = conn.manage_data_reg_connection(
                "LIST", drc, jdbc_driver="mysql")
            self.assertTrue(len(drcs.connections) >= 1)
            connection_names = [names.name for names in drcs.connections]
            self.assertTrue("test_connection_name_mysql" in connection_names,
                            "list data registration object connection failed.")
            self.assertTrue("test_connection_name_bc" not in connection_names,
                            "list data registration object connection failed.")

            # create another mysql connection
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS test_connection_name_2_mysql')
            drc = self._get_mysqltest_data_reg_connection_obj("test_connection_name_2_mysql")
            drcs = conn.manage_data_reg_connection("CREATE", drc)
            self.assertTrue(len(drcs.connections) == 1)

            # list with connection_pattern and jdbc driver search works as expected
            drcs = conn.manage_data_reg_connection(
                "LIST", drc, connection_pattern="test_connection_name_bc", jdbc_driver="mysql")
            self.assertFalse(len(drcs.connections))
            drcs = conn.manage_data_reg_connection(
                "LIST", drc, connection_pattern="test_connection_name_2_mysql", jdbc_driver="mysql")
            self.assertTrue(len(drcs.connections) == 1)

            # delete test
            drcs = conn.manage_data_reg_connection("DELETE", drc)
            self.assertTrue(len(drcs.connections) == 0)

            # get again returns empty
            drcs = conn.manage_data_reg_connection("GET", drc)
            self.assertTrue(len(drcs.connections) == 0)

    def test_drc_crud(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            # create test
            drc = self._get_psqltest_data_reg_connection_obj("test_connection_name")
            drcs = conn.manage_data_reg_connection("CREATE", drc)
            self.assertTrue(len(drcs.connections) == 1)

            # update test
            drc.host = "test_host_name_mod"
            drcs = conn.manage_data_reg_connection("UPDATE", drc)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertEqual(drcs.connections[0].host,
                             "test_host_name_mod",
                             "Update data registration object connection failed.")

            # get test
            drcs = conn.manage_data_reg_connection("GET", drc)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertEqual(drcs.connections[0].user_key, 'awssm://postgres-jdbcpsqltest-username')
            self.assertEqual(drcs.connections[0].password_key, 'awssm://postgres-jdbcpsqltest-password')

            # get test (with resolved credentials)
            drcs = conn.manage_data_reg_connection("GET", drc, resolve_creds=True)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertEqual(drcs.connections[0].user_key, 'cerebro')
            self.assertEqual(drcs.connections[0].password_key, 'cerebro1')

            # list with filters works as expected
            drcs = conn.manage_data_reg_connection(
                "LIST", drc, ["test_connection_name"])
            self.assertTrue(len(drcs.connections) >= 1)
            connection_names = [names.name for names in drcs.connections]
            self.assertTrue("test_connection_name" in connection_names,
                            "list data registration object connection failed.")

            # create another one
            drc = self._get_mysqltest_data_reg_connection_obj("test_connection_name_2")
            drcs = conn.manage_data_reg_connection("CREATE", drc)
            self.assertTrue(len(drcs.connections) == 1)

            # list with empty filter should still return all
            drcs = conn.manage_data_reg_connection(
                "LIST", drc, [])
            self.assertTrue(len(drcs.connections) >= 2)
            connection_names = [names.name for names in drcs.connections]
            self.assertTrue("test_connection_name" in connection_names,
                            "list data registration object connection failed.")
            self.assertTrue("test_connection_name_2" in connection_names,
                            "list data registration object connection failed.")

            # list with pattern search works as expected
            drcs = conn.manage_data_reg_connection(
                "LIST", drc, ["test_connection_name", "test_connection_name_2"])
            self.assertTrue(len(drcs.connections) >= 2)

            # list with jdbc driver search works as expected
            drcs = conn.manage_data_reg_connection(
                "LIST", drc, jdbc_driver="mysql")
            self.assertTrue(len(drcs.connections) >= 1)
            connection_names = [names.name for names in drcs.connections]
            self.assertTrue("test_connection_name_2" in connection_names,
                            "list data registration object connection failed.")
            self.assertTrue("test_connection_name_bc" not in connection_names,
                            "list data registration object connection failed.")

            # create another mysql connection
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS test_connection_name_2_mysql')
            drc = self._get_mysqltest_data_reg_connection_obj("test_connection_name_2_mysql")
            drcs = conn.manage_data_reg_connection("CREATE", drc)
            self.assertTrue(len(drcs.connections) == 1)

            # list with connection_pattern and jdbc driver search works as expected
            drcs = conn.manage_data_reg_connection(
                "LIST", drc, connection_pattern="test_connection_name_bc", jdbc_driver="mysql")
            self.assertFalse(len(drcs.connections))
            drcs = conn.manage_data_reg_connection(
                "LIST", drc, connection_pattern="test_connection_name_2_mysql", jdbc_driver="mysql")
            self.assertTrue(len(drcs.connections) == 1)

            ## Fixme: This is broken, looks like was always broken
            # self.assertEqual(drcs.connections[0].name,
            #                  "test_connection_name",
            #                  "list data registration object connection failed.")
            # self.assertEqual(drcs.connections[1].name,
            #                  "test_connection_name_2",
            #                  "list data registration object connection failed.")

            # Fixme:: Not yet working, returns all
            # list with pattern search works as expected
            # drcs = conn.manage_data_reg_connection(
            #     "LIST", drc, [], "test_connection_name_2")
            # print(drcs.connections)
            # self.assertTrue(len(drcs.connections) == 1)
            # self.assertEqual(drcs.connections[0].name,
            #                  "test_connection_name_2",
            #                  "list data registration object connection failed." +
            #                  len(drcs.connections))

            # delete test
            drcs = conn.manage_data_reg_connection("DELETE", drc)
            self.assertTrue(len(drcs.connections) == 0)

            # get again returns empty
            drcs = conn.manage_data_reg_connection("GET", drc)
            self.assertTrue(len(drcs.connections) == 0)

            # create data connection test with whitespace in user key and password key
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS test_connection_with_whitespace')
            drc = self._get_psqltest_data_reg_connection_obj("test_connection_with_whitespace")

            # add whitespace and verify connection creation
            drc.username = " awssm://postgres-jdbcpsqltest-username    "
            drc.password = " awssm://postgres-jdbcpsqltest-password    "
            drcs = conn.manage_data_reg_connection("CREATE", drc)
            self.assertTrue(len(drcs.connections) == 1)

    def test_drc_crud_saas_direct_credentials(self):
        """ In SaaS environment, users can enter the credentials directly i.e. in plain
            text. Okera generates secret key_ids for such credentials and stores them
            in a secret store. BE is not supposed to return the actual password
            to UI for security. Instead, BE would return password field as blank.
        """
        MYSQL_CXN = 'test_drc_crud_saas_direct_credentials_mysql_conn'
        PSQL_CXN  = 'test_drc_crud_saas_direct_credentials_psql_conn'
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ##### CREATE
            # create a connection with direct_credentials=True
            # The returned conn object should have clear text username but blank password.
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS %s' % (MYSQL_CXN))
            drc = self._get_mysqltest_data_reg_connection_obj(MYSQL_CXN)
            drc.user_key = "cerebro"
            drc.password_key = "cerebro1"
            drcs = conn.manage_data_reg_connection("CREATE", drc, direct_credentials=True)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertEqual(drcs.connections[0].user_key, 'cerebro')
            self.assertEqual(drcs.connections[0].password_key, '')

            ##### GET
            # Fetch the newly created connection with direct_credentials=False
            # It should return secret key_ids for username and password instead of
            # clear-text username and blank password.
            drcs = conn.manage_data_reg_connection("GET", drc, direct_credentials=False)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertTrue('%s/mysql/user' % MYSQL_CXN in drcs.connections[0].user_key)
            self.assertTrue('%s/mysql/password' % MYSQL_CXN in drcs.connections[0].password_key)

            ##### GET and UPDATE (modify any field other than password)
            # Fetch the same connection with direct_credentials=True so that
            # the returned conn object has clear-text username but blank password.
            # Now, update conn object and modify field(s) other than the password (ex. default_catalog)
            # BE checks the password field and as it is blank, it uses the existing
            # password with the modified connection object to store it in Okera.
            drc = conn.manage_data_reg_connection("GET", drc, direct_credentials=True).connections[0]
            self.assertEqual(drc.user_key, 'cerebro')
            self.assertEqual(drc.password_key, '')
            self.assertEqual(drc.default_catalog, 'jdbc_test')
            # modify default_catalog and update
            drc.default_catalog = 'jdbc_demo'
            drcs = conn.manage_data_reg_connection("UPDATE", drc, direct_credentials=True)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertEqual(drcs.connections[0].default_catalog, 'jdbc_demo')
            self.assertEqual(drcs.connections[0].user_key, 'cerebro')
            self.assertEqual(drcs.connections[0].password_key, '')

            ##### GET and UPDATE (modify the password field)
            # Fetch the updated connection with direct_credentials=True so that
            # the returned conn object has clear-text username but blank password.
            # Now, update conn object and modify the password (here we are updating it to
            # same value, otherwise connection to MySql would fail).
            # BE checks the password field and as it is not blank, it uses the new
            # password and store it in Okera.
            drc = conn.manage_data_reg_connection("GET", drc, direct_credentials=True).connections[0]
            drc.password_key = 'cerebro1'
            drcs = conn.manage_data_reg_connection("UPDATE", drc, direct_credentials=True)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertEqual(drcs.connections[0].default_catalog, 'jdbc_demo')
            self.assertEqual(drcs.connections[0].user_key, 'cerebro')
            self.assertEqual(drcs.connections[0].password_key, '')
            ##### DELETE
            drcs = conn.manage_data_reg_connection("DELETE", drc, direct_credentials=True)
            self.assertTrue(len(drcs.connections) == 0)

    def test_drc_testconnection_as_admin(self):
        MYSQL_CXN = 'test_drc_testconnection_as_admin_mysql_conn'
        SNWFLK_CXN = 'test_drc_testconnection_as_admin_snwflk_conn'
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()
            ddls = [
                "DROP DATACONNECTION IF EXISTS %s" % (MYSQL_CXN),
                "DROP DATACONNECTION IF EXISTS %s" % (SNWFLK_CXN),
            ]
            for ddl in ddls:
                conn.execute_ddl(ddl)

            # Test Connection in "CREATE WORKFLOW" with valid connection details, TEST should succeed
            drc = self._get_mysqltest_data_reg_connection_obj(MYSQL_CXN)
            drcs = conn.manage_data_reg_connection("TEST_CREATE", drc)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertTrue(drcs.connections[0].test_status == "SUCCESS")
            self.assertTrue(drcs.connections[0].test_error_details == "")
            self.assertTrue(drcs.connections[0].tested_at is not None)
            # The connection should not get created as it is just a TEST
            drcs = conn.manage_data_reg_connection("GET", drc)
            self.assertTrue(len(drcs.connections) == 0)

            # Test Connection in "CREATE WORKFLOW" with missing default db, TEST should fail
            drc = self._get_mysqltest_data_reg_connection_obj(MYSQL_CXN)
            # set the default catalog to be Null
            drc.default_catalog = None
            drcs = conn.manage_data_reg_connection("TEST_CREATE", drc)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertTrue(drcs.connections[0].test_status == "FAILED")
            self.assertEqual(drcs.connections[0].test_error_details,
                "'jdbc.db.name' is a required parameter for a data connection.")
            self.assertTrue(drcs.connections[0].tested_at is not None)
            # The connection should not get created as it is just a TEST
            drcs = conn.manage_data_reg_connection("GET", drc)
            self.assertTrue(len(drcs.connections) == 0)

            # Test Connection in "EDIT WORKFLOW" with invalid connection details, TEST should fail
            drc = self._get_mysqltest_data_reg_connection_obj(MYSQL_CXN)
            # create a connection
            drcs1 = conn.manage_data_reg_connection("CREATE", drc)
            self.assertTrue(len(drcs1.connections) == 1)
            # Now edit some connection details and test the updated connection
            drc.host = "invalid_mysql_host"
            drcs2 = conn.manage_data_reg_connection("TEST_EDIT", drc)
            self.assertTrue(len(drcs2.connections) == 1)
            self.assertTrue(drcs2.connections[0].test_status == "FAILED")
            self.assertEqual(drcs2.connections[0].test_error_details,
                "UnknownHostException: invalid_mysql_host: Name or service not known")
            self.assertTrue(drcs2.connections[0].tested_at is not None)

            # Test Connection in "EDIT WORKFLOW" with invalid connection details, TEST should fail
            drc = self._get_snowflake_data_reg_connection_obj(SNWFLK_CXN)
            # create a connection
            drcs1 = conn.manage_data_reg_connection("CREATE", drc)
            self.assertTrue(len(drcs1.connections) == 1)
            # Now edit the userkey to be mysql's userkey and test the updated connection
            drc.user_key = "awssm://mysql-username"
            drcs2 = conn.manage_data_reg_connection("TEST_EDIT", drc)
            self.assertTrue(len(drcs2.connections) == 1)
            self.assertTrue(drcs2.connections[0].test_status == "FAILED")
            self.assertEqual(drcs2.connections[0].test_error_details,
                "SnowflakeSQLException: Incorrect username or password was specified.")
            self.assertTrue(drcs2.connections[0].tested_at is not None)

            # "TEST EXISTING" connection with valid connection details, TEST should succeed
            drc = self._get_mysqltest_data_reg_connection_obj(MYSQL_CXN)
            # drop connection if exists
            drcs1 = conn.manage_data_reg_connection("DELETE", drc)
            # create a connection
            drcs1 = conn.manage_data_reg_connection("CREATE", drc)
            self.assertTrue(len(drcs1.connections) == 1)
            # Now test an existing connection
            drcs2 = conn.manage_data_reg_connection("TEST_EXISTING", drc)
            self.assertTrue(len(drcs2.connections) == 1)
            self.assertTrue(drcs2.connections[0].test_status == "SUCCESS")
            self.assertTrue(drcs2.connections[0].test_error_details == "")
            self.assertTrue(drcs2.connections[0].tested_at is not None)
            # The existing connection should get updated with latest test information
            drcs3 = conn.manage_data_reg_connection("GET", drc)
            self.assertTrue(len(drcs3.connections) == 1)
            self.assertTrue(drcs3.connections[0].test_status == "SUCCESS")
            self.assertTrue(drcs3.connections[0].test_error_details == "")
            self.assertTrue(drcs3.connections[0].tested_at is not None)
            # the 'tested_at' timestamp should match
            # Note that we round the milliseconds away as some DB engines
            # (such as MySQL) do the same thing, and we just care that
            # overall they are similar.
            self.assertEqual(round(drcs2.connections[0].tested_at / 1000),
                round(drcs3.connections[0].tested_at / 1000))

    def test_invalid_jdbc_props(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            invalid_path = 'some-invalid-path'

            # validation for invalid path
            drc = self._get_psqltest_data_reg_connection_obj('test_conn_invalid_path')
            drc.data_source_path = 's3://%s/test.conf' % invalid_path
            try:
                drcs = conn.manage_data_reg_connection('CREATE', drc)
                assert drcs
            except TRecordServiceException as ex:
                assert 'Bucket %s does not exist' % invalid_path in str(ex.detail)

            drc = self._get_psqltest_data_reg_connection_obj('test_conn_invalid_path')
            drcs = conn.manage_data_reg_connection('CREATE', drc)
            self.assertTrue(len(drcs.connections) == 1)

            # validation for invalid path update
            drc.data_source_path = 's3://%s/test.conf' % invalid_path
            try:
                drcs = conn.manage_data_reg_connection('UPDATE', drc)
                assert drcs
            except TRecordServiceException as ex:
                assert 'Bucket %s does not exist' % invalid_path in str(ex.detail)

            drcs = conn.manage_data_reg_connection('DELETE', drc)
            self.assertTrue(len(drcs.connections) == 0)

            # validation for invalid username
            drc = self._get_snowflake_data_reg_connection_obj('test_conn_invalid_username')
            drc.user_key = 'awssm://mysql-username'
            try:
                drcs = conn.manage_data_reg_connection('TEST_CREATE', drc)
                assert drcs
            except TRecordServiceException as ex:
                assert 'Incorrect username or password was specified.' in str(ex.detail)

            # validation for invalid port
            drc = self._get_mysqltest_data_reg_connection_obj('test_conn_invalid_port')
            drc.port = 8080
            try:
                drcs = conn.manage_data_reg_connection('CREATE', drc)
                assert drcs
            except TRecordServiceException as ex:
                assert 'SocketTimeoutException: connect timed out' in str(ex.detail)

    def test_discover_crawler_catalog(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            #MySQL Test
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS mysql_test_connection')
            drc = self._get_mysqltest_data_reg_connection_obj('mysql_test_connection')
            drcs = conn.manage_data_reg_connection('CREATE', drc)
            ret_crawler_objects = conn.discover_crawler(drc)
            ret_list_jdbc_datasets = ret_crawler_objects.crawler_discover_datasets[0] \
                .jdbc_datasets
            self.assertTrue(len(ret_crawler_objects.crawler_discover_datasets) == 1)
            self.assertIsNotNone(ret_list_jdbc_datasets)
            self.assertTrue(any(x.jdbc_catalog == 'jdbc_test'\
                for x in ret_list_jdbc_datasets))

            #Microsoft SQL Server Test
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS mssql_test_connection')
            drc = self._get_mssqltest_data_reg_connection_obj('mssql_test_connection')
            drcs = conn.manage_data_reg_connection('CREATE', drc)
            ret_crawler_objects = conn.discover_crawler(drc)
            ret_list_jdbc_datasets = ret_crawler_objects.crawler_discover_datasets[0] \
                .jdbc_datasets

            self.assertTrue(len(ret_crawler_objects.crawler_discover_datasets) == 1)
            self.assertIsNotNone(ret_list_jdbc_datasets)
            self.assertTrue(any(x.jdbc_catalog == 'okera_test'\
                for x in ret_list_jdbc_datasets))

    def test_crawler(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            drc = self._get_psqltest_data_reg_connection_obj('test_conn_crawler')
            drc.data_source_path = 's3://cerebro-datasets/jdbc_demo/jdbc_test_psql.conf'
            # delete if it exists then create
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS test_conn_crawler')
            drcs = conn.manage_data_reg_connection("CREATE", drc)
            resp = conn.manage_crawler(drc)
            self.assertTrue(resp.status == TCrawlStatus.CRAWLING)

            drc = self._get_psqltest_data_reg_connection_obj('test_conn_crawler_s3')
            drc.type = "S3"
            drc.data_source_path = 's3://cerebrodata-test/tpch-nation/'
            resp = conn.manage_crawler(drc)
            self.assertTrue(resp.status == TCrawlStatus.CRAWLING)

    def test_discover_crawler_schema(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS mssql_test_connection')
            drc = self._get_mssqltest_data_reg_connection_obj('mssql_test_connection')
            drcs = conn.manage_data_reg_connection('CREATE', drc)
            ret_crawler_objects = conn.discover_crawler(drc, 'okera_test')
            ret_list_jdbc_datasets = ret_crawler_objects.crawler_discover_datasets[0] \
                .jdbc_datasets

            self.assertTrue(len(ret_crawler_objects.crawler_discover_datasets) == 1)
            self.assertIsNotNone(ret_list_jdbc_datasets)
            self.assertTrue(any(x.jdbc_catalog == 'okera_test' \
                for x in ret_list_jdbc_datasets))
            #for dataset in ret_list_jdbc_datasets:
            #    print(dataset.jdbc_schema)
            self.assertTrue(any(x.jdbc_schema == 'marketing' \
                for x in ret_list_jdbc_datasets))
            self.assertTrue(any(x.jdbc_schema == 'dbo' \
                for x in ret_list_jdbc_datasets))
            self.assertFalse(any(x.jdbc_schema == 'INFORMATION_SCHEMA' \
                for x in ret_list_jdbc_datasets))
            drcs = conn.manage_data_reg_connection('DELETE', drc)
            self.assertTrue(len(drcs.connections) == 0)

    def test_discover_crawler_table_schema(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            #MySQL Test
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS mysql_test_connection')
            drc = self._get_mysqltest_data_reg_connection_obj('mysql_test_connection')
            drcs = conn.manage_data_reg_connection('CREATE', drc)
            ret_crawler_objects = conn.discover_crawler(drc, 'jdbc_test')
            ret_list_jdbc_datasets = ret_crawler_objects.crawler_discover_datasets[0] \
                .jdbc_datasets

            self.assertTrue(len(ret_crawler_objects.crawler_discover_datasets) == 1)
            self.assertIsNotNone(ret_list_jdbc_datasets)
            self.assertTrue(any(x.jdbc_catalog == 'jdbc_test'\
                for x in ret_list_jdbc_datasets))
            #for dataset in ret_list_jdbc_datasets:
            #    print(dataset)
            self.assertTrue(any(x.jdbc_table == 'all_data_types' \
                for x in ret_list_jdbc_datasets))
            self._verify_mysql_table_schema(ret_list_jdbc_datasets, \
                None, 'all_data_types')
            drcs = conn.manage_data_reg_connection('DELETE', drc)
            self.assertTrue(len(drcs.connections) == 0)

            #Microsoft SQL Server Test
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS mssql_test_connection')
            drc = self._get_mssqltest_data_reg_connection_obj('mssql_test_connection')
            drcs = conn.manage_data_reg_connection('CREATE', drc)
            ret_crawler_objects = conn.discover_crawler(drc, 'okera_test',\
                 'okera_test.dbo')
            ret_list_jdbc_datasets = ret_crawler_objects.crawler_discover_datasets[0]\
                .jdbc_datasets

            self.assertTrue(len(ret_crawler_objects.crawler_discover_datasets) == 1)
            self.assertIsNotNone(ret_list_jdbc_datasets)
            self.assertTrue(any(x.jdbc_catalog == 'okera_test' \
                for x in ret_list_jdbc_datasets))
            self.assertTrue(any(x.jdbc_schema == 'okera_test.dbo' \
                for x in ret_list_jdbc_datasets))
            #for dataset in ret_list_jdbc_datasets:
            #    print(dataset.jdbc_table)
            self.assertTrue(any(x.jdbc_table == 'all_data_types' \
                for x in ret_list_jdbc_datasets))

            for dataset in ret_list_jdbc_datasets:
                if dataset.jdbc_schema == 'okera_test.dbo' and \
                   dataset.jdbc_table == 'dbo.all_data_types':
                    self.assertTrue(any(x.name == 'varchar' \
                        for x in dataset.schema.cols))
            self._verify_mssql_table_schema(ret_list_jdbc_datasets, \
                'okera_test.dbo', 'dbo.all_data_types')
            #for dataset in ret_list_jdbc_datasets:
            #    print(dataset)

            drcs = conn.manage_data_reg_connection('DELETE', drc)
            self.assertTrue(len(drcs.connections) == 0)

    def test_dataconnection_privileges(self):
        CXN = 'test_privileges_connection_privileges'
        CXN2 = 'test_privileges_connection_privileges_2'
        ROLE = "test_privileges_connection_role"

        USER = "test_privileges_connection_user"
        USER_NO_ACCESS = "test_privileges_connection_user_no_access"

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            for is_catalog in [False, True]:
                for level_test in CONNECTION_PRIVILEGES:
                    for is_ddl in [True, False]:
                        ctx.disable_auth()

                        level, can_show, can_alter, can_drop, can_use = level_test
                        level_name = TAccessPermissionLevel._VALUES_TO_NAMES[level]
                        ddls = [
                            "DROP DATACONNECTION IF EXISTS %s" % (CXN),
                            "DROP DATACONNECTION IF EXISTS %s" % (CXN2),
                            "DROP ROLE IF EXISTS %s" % (ROLE),

                            # Create the connection
                            """CREATE DATACONNECTION %s CXNPROPERTIES
                                (
                                'connection_type'='JDBC',
                                'jdbc_driver'='mysql',
                                'host'='cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com',
                                'port'='3306',
                                'user_key'='awsps:///mysql/username',
                                'password_key'='awsps:///mysql/password',
                                'jdbc.db.name'='jdbc_test'
                                )
                            """ % (CXN),

                            # Create the connection
                            """CREATE DATACONNECTION %s CXNPROPERTIES
                                (
                                'connection_type'='JDBC',
                                'jdbc_driver'='mysql',
                                'host'='cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com',
                                'port'='3306',
                                'user_key'='awsps:///mysql/username',
                                'password_key'='awsps:///mysql/password',
                                'jdbc.db.name'='jdbc_test'
                                )
                            """ % (CXN2),

                            # Create the role and grant it to the user
                            "CREATE ROLE %s" % (ROLE),
                            "GRANT ROLE %s TO GROUP %s" % (ROLE, USER),
                        ]


                        if is_catalog:
                            # TODO: CATALOG doesn't support ALTER
                            if level == TAccessPermissionLevel.ALTER:
                                continue

                            ddls += [
                                "GRANT %s ON CATALOG TO ROLE %s" % (level_name, ROLE)
                            ]
                        else:
                            ddls += [
                                "GRANT %s ON DATACONNECTION %s TO ROLE %s" % (level_name, CXN, ROLE)
                            ]

                        for ddl in ddls:
                            conn.execute_ddl(ddl)

                        # Verify that the root user can see both connections
                        ctx.disable_auth()
                        connections = conn.manage_data_reg_connection("LIST", EMPTY_DRC, connection_pattern=CXN).connections
                        assert len(connections) == 2
                        sorted_names = sorted([connection.name for connection in connections])
                        assert sorted_names[0] == CXN
                        assert sorted_names[1] == CXN2

                        ctx.enable_token_auth(token_str=USER)

                        connections = conn.manage_data_reg_connection("LIST", EMPTY_DRC, connection_pattern=CXN).connections
                        if can_show:
                            # Check to ensure the connection is visible. Note that if the permission we have
                            # is on the catalog level, we will be able to see both connections, so check
                            # for that explicitly.
                            if is_catalog:
                                assert len(connections) == 2
                                sorted_names = sorted([connection.name for connection in connections])
                                assert sorted_names[0] == CXN
                                assert sorted_names[1] == CXN2
                            else:
                                assert len(connections) == 1
                                assert connections[0].name == CXN
                        else:
                            assert len(connections) == 0

                        if is_ddl:
                            stmt = """ALTER DATACONNECTION %s CXNPROPERTIES
                                        (
                                        'connection_type'='JDBC',
                                        'jdbc_driver'='mysql',
                                        'host'='cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com',
                                        'port'='3306',
                                        'user_key'='awsps:///mysql/username',
                                        'password_key'='awsps:///mysql/password',
                                        'jdbc.db.name'='jdbc_test',
                                        'foo'='bar'
                                        )""" % (CXN)
                            if can_alter:
                                conn.execute_ddl(stmt)
                            else:
                                with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                                    conn.execute_ddl(stmt)
                                self.assertTrue('ALTER this data connection' in str(ex_ctx.exception))
                        else:
                            if can_alter:
                                update_connection(conn, CXN)
                            else:
                                with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                                    update_connection(conn, CXN)
                                self.assertTrue('ALTER this data connection' in str(ex_ctx.exception))

                        # USE should give us the ability to TEST a connection
                        if is_ddl:
                            # Only test it via API, there is no TEST DDL for connections
                            pass
                        else:
                            if can_use:
                                run_test_connection(conn, CXN)
                            else:
                                with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                                    run_test_connection(conn, CXN)
                                self.assertTrue('test this data connection' in str(ex_ctx.exception))

                        if is_ddl:
                            # Only test it via API, there is no SHOW DDL for connections
                            pass
                        else:
                            if can_show:
                                get_connection(conn, CXN)
                            else:
                                with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                                    get_connection(conn, CXN)
                                self.assertTrue('SHOW this data connection' in str(ex_ctx.exception))

                        if is_ddl:
                            stmt = "DROP DATACONNECTION IF EXISTS %s" % (CXN)
                            if can_drop:
                                conn.execute_ddl(stmt)
                            else:
                                with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                                    conn.execute_ddl(stmt)
                                self.assertTrue('DROP this data connection' in str(ex_ctx.exception))
                        else:
                            if can_drop:
                                delete_connection(conn, CXN)
                            else:
                                with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                                    delete_connection(conn, CXN)
                                self.assertTrue('DROP this data connection' in str(ex_ctx.exception))


                        # Verify that a user with no access can't see the connection
                        ctx.enable_token_auth(token_str=USER_NO_ACCESS)
                        connections = conn.manage_data_reg_connection("LIST", EMPTY_DRC, connection_pattern=CXN).connections
                        assert len(connections) == 0

    def test_dataconnection_create_as_owner(self):
        CXN = 'test_privileges_connection_create_as_owner'
        ROLE = "test_privileges_connection_role"

        USER = "test_privileges_connection_user"
        USER_NO_ACCESS = "test_privileges_connection_user_no_access"

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            for is_ddl in [True, False]:
                ctx.disable_auth()

                ddls = [
                    "DROP DATACONNECTION IF EXISTS %s" % (CXN),
                    "DROP ROLE IF EXISTS %s" % (ROLE),

                    # Create the role and grant it to the user
                    "CREATE ROLE %s" % (ROLE),
                    "GRANT ROLE %s TO GROUP %s" % (ROLE, USER),

                    "GRANT CREATE_DATACONNECTION_AS_OWNER ON CATALOG TO ROLE %s" % (ROLE),
                ]

                for ddl in ddls:
                    conn.execute_ddl(ddl)

                if is_ddl:
                    create_stmt = """CREATE DATACONNECTION %s CXNPROPERTIES
                        (
                        'connection_type'='JDBC',
                        'jdbc_driver'='mysql',
                        'host'='cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com',
                        'port'='3306',
                        'user_key'='awsps:///mysql/username',
                        'password_key'='awsps:///mysql/password',
                        'jdbc.db.name'='jdbc_test'
                        )
                    """ % (CXN)
                    for user, can_create in [(USER, True), (USER_NO_ACCESS, False)]:
                        ctx.enable_token_auth(token_str=user)
                        if can_create:
                            conn.execute_ddl(create_stmt)

                            # Since we did create as owner, we can drop it
                            stmt = "DROP DATACONNECTION IF EXISTS %s" % (CXN)
                            conn.execute_ddl(stmt)
                        else:
                            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                                conn.execute_ddl(create_stmt)
                            self.assertTrue('CREATE this data connection' in str(ex_ctx.exception))
                else:
                    drc = TDataRegConnection()
                    drc.name = CXN
                    drc.type = "JDBC"
                    drc.jdbc_driver = "mysql"
                    drc.host = "cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com"
                    drc.port = 3306
                    drc.user_key = "awsps:///mysql/username"
                    drc.password_key = "awsps:///mysql/password"
                    drc.default_catalog = "jdbc_test"
                    drc.is_active = True
                    for user, can_create in [(USER, True), (USER_NO_ACCESS, False)]:
                        ctx.enable_token_auth(token_str=user)
                        if can_create:
                            create_connection(conn, drc)

                            # Since we did create as owner, we can drop it
                            delete_connection(conn, CXN)
                        else:
                            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                                create_connection(conn, drc)
                            self.assertTrue('CREATE this data connection' in str(ex_ctx.exception))

    def test_dataconnection_use_table(self):
        CXN = 'test_privileges_connection_use_table'
        ROLE = "test_privileges_connection_role"
        DB1 = "test_privileges_connection_db"
        TBL1 = "%s.tbl" % DB1
        USER = "testprivuser1"

        # Set up the NO_ACCESS user
        DB2 = "test_privileges_connection_db2"
        TBL2 = "%s.tbl2" % DB2
        ROLE2 = "test_privileges_connection_role2"
        USER_NO_ACCESS = "testprivuser2"

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()

            ddls = [
                "DROP DATABASE IF EXISTS %s cascade" % (DB1),
                "DROP DATABASE IF EXISTS %s cascade" % (DB2),
                "DROP DATACONNECTION IF EXISTS %s" % (CXN),
                "DROP ROLE IF EXISTS %s" % (ROLE),
                "DROP ROLE IF EXISTS %s" % (ROLE2),

                # Create the role and grant it to the user
                "CREATE ROLE %s" % (ROLE),
                "CREATE ROLE %s" % (ROLE2),
                "GRANT ROLE %s TO GROUP %s" % (ROLE, USER),
                "GRANT ROLE %s TO GROUP %s" % (ROLE2, USER_NO_ACCESS),

                # Create the DB
                "CREATE DATABASE %s" % (DB1),
                "CREATE DATABASE %s" % (DB2),

                # Create the connection and grant USE on it
                """CREATE DATACONNECTION %s CXNPROPERTIES
                    (
                    'connection_type'='JDBC',
                    'jdbc_driver'='mysql',
                    'host'='cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com',
                    'port'='3306',
                    'user_key'='awsps:///mysql/username',
                    'password_key'='awsps:///mysql/password',
                    'jdbc.db.name'='jdbc_test'
                    )
                """ % (CXN),
                "GRANT USE ON DATACONNECTION %s TO ROLE %s" % (CXN, ROLE),

                # TODO: FIXME: why does this not work?
                #"GRANT CREATE_AS_OWNER ON DATABASE %s TO ROLE %s" % (DB1, ROLE),
                "GRANT CREATE ON CATALOG TO ROLE %s" % (ROLE),

                # Give the no access user only the ability to create but not use
                # TODO: FIXME: why does this not work?
                #"GRANT CREATE_AS_OWNER ON DATABASE %s TO ROLE %s" % (DB2, ROLE2),
                "GRANT CREATE ON CATALOG TO ROLE %s" % (ROLE2),
            ]

            for ddl in ddls:
                conn.execute_ddl(ddl)

            for user, can_use, tbl in [(USER, True, TBL1), (USER_NO_ACCESS, False, TBL2)]:
                create_stmt = """CREATE EXTERNAL TABLE %s STORED as JDBC
                        TBLPROPERTIES(
                        'driver' = 'mysql',
                        'okera.connection.name' = '%s',
                        'jdbc.db.name'='jdbc_test',
                        'jdbc.schema.name'='public',
                        'table' = 'filter_pushdown_test'
                    )""" % (tbl, CXN)
                create_as_view_stmt = "%s USING VIEW AS 'select 1 as x'" % create_stmt

                ctx.enable_token_auth(token_str=user)
                if can_use:
                    conn.execute_ddl(create_stmt)

                    # Now we drop it and create a table using AS VIEW
                    conn.execute_ddl('DROP TABLE %s' % tbl)
                    conn.execute_ddl(create_as_view_stmt)
                else:
                    with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                        conn.execute_ddl(create_stmt)
                    self.assertTrue('USE the connection' in str(ex_ctx.exception))

                    with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                        conn.execute_ddl(create_as_view_stmt)
                    self.assertTrue('USE the connection' in str(ex_ctx.exception))

    def test_dataconnection_use_database(self):
        CXN = 'test_privileges_connection_use_database'
        ROLE = "test_privileges_connection_role"
        DB1 = "test_privileges_connection_db"
        USER = "testprivuser1"

        # Set up the NO_ACCESS user
        DB2 = "test_privileges_connection_db2"
        ROLE2 = "test_privileges_connection_role2"
        USER_NO_ACCESS = "testprivuser2"

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()

            ddls = [
                "DROP DATABASE IF EXISTS %s cascade" % (DB1),
                "DROP DATABASE IF EXISTS %s cascade" % (DB2),
                "DROP DATACONNECTION IF EXISTS %s" % (CXN),
                "DROP ROLE IF EXISTS %s" % (ROLE),
                "DROP ROLE IF EXISTS %s" % (ROLE2),

                # Create the role and grant it to the user
                "CREATE ROLE %s" % (ROLE),
                "CREATE ROLE %s" % (ROLE2),
                "GRANT ROLE %s TO GROUP %s" % (ROLE, USER),
                "GRANT ROLE %s TO GROUP %s" % (ROLE2, USER_NO_ACCESS),

                # Create the connection and grant USE on it
                """CREATE DATACONNECTION %s CXNPROPERTIES
                    (
                    'connection_type'='JDBC',
                    'jdbc_driver'='mysql',
                    'host'='cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com',
                    'port'='3306',
                    'user_key'='awsps:///mysql/username',
                    'password_key'='awsps:///mysql/password',
                    'jdbc.db.name'='jdbc_test'
                    )
                """ % (CXN),
                "GRANT USE ON DATACONNECTION %s TO ROLE %s" % (CXN, ROLE),

                "GRANT CREATE_AS_OWNER ON CATALOG TO ROLE %s" % (ROLE),

                # Give the no access user only the ability to create but not use
                "GRANT CREATE_AS_OWNER ON CATALOG TO ROLE %s" % (ROLE2),
            ]

            for ddl in ddls:
                conn.execute_ddl(ddl)

            for user, can_use, db in [(USER, True, DB1), (USER_NO_ACCESS, False, DB2)]:
                create_stmt = """CREATE DATABASE %s DBPROPERTIES
                                 ('okera.connection.name' = '%s');""" % (db, CXN)
                ctx.enable_token_auth(token_str=user)
                if can_use:
                    conn.execute_ddl(create_stmt)
                else:
                    with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                        conn.execute_ddl(create_stmt)
                    self.assertTrue('USE the connection' in str(ex_ctx.exception))

    def test_dataconnection_use_database_alter(self):
        CXN = 'test_privileges_connection_alter'
        ROLE = "test_privileges_connection_role"
        DB1 = "test_privileges_connection_db"
        USER = "testprivuser1"

        ROLE2 = "test_privileges_connection_role2"
        USER_NO_ACCESS = "testprivuser2"

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()

            ddls = [
                "DROP DATABASE IF EXISTS %s cascade" % (DB1),
                "DROP DATACONNECTION IF EXISTS %s" % (CXN),
                "DROP ROLE IF EXISTS %s" % (ROLE),
                "DROP ROLE IF EXISTS %s" % (ROLE2),

                # Create the role and grant it to the user
                "CREATE ROLE %s" % (ROLE),
                "CREATE ROLE %s" % (ROLE2),
                "GRANT ROLE %s TO GROUP %s" % (ROLE, USER),
                "GRANT ROLE %s TO GROUP %s" % (ROLE2, USER_NO_ACCESS),

                # Create the connection and grant USE on it
                """CREATE DATACONNECTION %s CXNPROPERTIES
                    (
                    'connection_type'='JDBC',
                    'jdbc_driver'='mysql',
                    'host'='cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com',
                    'port'='3306',
                    'user_key'='awsps:///mysql/username',
                    'password_key'='awsps:///mysql/password',
                    'jdbc.db.name'='jdbc_test'
                    )
                """ % (CXN),
                """CREATE DATABASE %s DBPROPERTIES (
                    'okera.connection.name' = '%s');""" % (DB1, CXN),

                "GRANT USE ON DATACONNECTION %s TO ROLE %s" % (CXN, ROLE),
                "GRANT ALTER ON DATABASE %s TO ROLE %s" % (DB1, ROLE),

                # Give the no access user only the ability to ALTER but not use
                "GRANT ALTER ON DATABASE %s TO ROLE %s" % (DB1, ROLE2),
            ]

            for ddl in ddls:
                conn.execute_ddl(ddl)

            for user, can_alter in [(USER, True), (USER_NO_ACCESS, False)]:
                alter_stmt = "ALTER DATABASE %s LOAD DEFINITIONS ()" % (DB1)
                alter_props_stmt = "ALTER DATABASE %s SET DBPROPERTIES ('okera.connection.name'='%s')" % (DB1, CXN)
                ctx.enable_token_auth(token_str=user)
                if can_alter:
                    conn.execute_ddl(alter_stmt)
                    conn.execute_ddl(alter_props_stmt)
                else:
                    with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                        conn.execute_ddl(alter_stmt)
                    self.assertTrue('USE the connection' in str(ex_ctx.exception))
                    with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                        conn.execute_ddl(alter_props_stmt)
                    self.assertTrue('USE the connection' in str(ex_ctx.exception))

    def test_dataconnection_use_crawler(self):
        CXN = 'test_privileges_connection_crawler'
        ROLE = "test_privileges_connection_role"
        DB1 = "test_privileges_connection_db"
        USER = "testprivuser1"

        ROLE2 = "test_privileges_connection_role2"
        USER_NO_ACCESS = "testprivuser2"

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()

            ddls = [
                "DROP DATABASE IF EXISTS %s CASCADE" % (DB1),
                "DROP DATABASE IF EXISTS _okera_crawler_%s CASCADE" % (CXN),
                "DROP DATACONNECTION IF EXISTS %s" % (CXN),
                "DROP ROLE IF EXISTS %s" % (ROLE),
                "DROP ROLE IF EXISTS %s" % (ROLE2),

                # Create the role and grant it to the user
                "CREATE ROLE %s" % (ROLE),
                "CREATE ROLE %s" % (ROLE2),
                "GRANT ROLE %s TO GROUP %s" % (ROLE, USER),
                "GRANT ROLE %s TO GROUP %s" % (ROLE2, USER_NO_ACCESS),

                # Create the connection and grant USE on it
                """CREATE DATACONNECTION %s CXNPROPERTIES
                    (
                    'connection_type'='JDBC',
                    'jdbc_driver'='mysql',
                    'host'='cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com',
                    'port'='3306',
                    'user_key'='awsps:///mysql/username',
                    'password_key'='awsps:///mysql/password',
                    'jdbc.db.name'='jdbc_test'
                    )
                """ % (CXN),
                """CREATE DATABASE %s DBPROPERTIES (
                    'okera.connection.name' = '%s');""" % (DB1, CXN),

                "GRANT USE ON DATACONNECTION %s TO ROLE %s" % (CXN, ROLE),
            ]

            for ddl in ddls:
                conn.execute_ddl(ddl)

            for user, can_use_crawler in [(USER, True), (USER, True)]:
                ctx.enable_token_auth(token_str=user)
                if can_use_crawler:
                    discover_crawler(conn, CXN)
                    manage_crawler(conn, CXN)
                else:
                    with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                        discover_crawler(conn, CXN)
                        manage_crawler(conn, CXN)
                    self.assertTrue('USE this data connection' in str(ex_ctx.exception))

    def test_dataconnection_privileges_while_listing(self):
        CXN = 'test_privileges_connection_listing_cxn'
        CXN2 = 'test_privileges_connection_listing_cxn2'

        ROLE = "test_privileges_connection_listing_role"
        USER = "test_privileges_connection_listing_user1"

        ROLE2 = "test_privileges_connection_listing_role2"
        USER_NO_ACCESS = "test_privileges_connection_listing_user2"
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:

            ddls = [
                "DROP DATACONNECTION IF EXISTS %s" % (CXN),
                "DROP DATACONNECTION IF EXISTS %s" % (CXN2),
                "DROP ROLE IF EXISTS %s" % (ROLE),
                "DROP ROLE IF EXISTS %s" % (ROLE2),

                # Create the connection
                """CREATE DATACONNECTION %s CXNPROPERTIES
                    (
                    'connection_type'='JDBC',
                    'jdbc_driver'='mysql',
                    'host'='cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com',
                    'port'='3306',
                    'user_key'='awsps:///mysql/username',
                    'password_key'='awsps:///mysql/password',
                    'jdbc.db.name'='jdbc_test'
                    )
                """ % (CXN),

                # Create the connection
                """CREATE DATACONNECTION %s CXNPROPERTIES
                    (
                    'connection_type'='JDBC',
                    'jdbc_driver'='mysql',
                    'host'='cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com',
                    'port'='3306',
                    'user_key'='awsps:///mysql/username',
                    'password_key'='awsps:///mysql/password',
                    'jdbc.db.name'='jdbc_test'
                    )
                """ % (CXN2),

                # Create the role and grant it to the user
                "CREATE ROLE %s" % (ROLE),
                "GRANT ROLE %s TO GROUP %s" % (ROLE, USER),

                "CREATE ROLE %s" % (ROLE2),
                "GRANT ROLE %s TO GROUP %s" % (ROLE2, USER_NO_ACCESS),

                "GRANT %s ON CATALOG TO ROLE %s" % ('CREATE_AS_OWNER', ROLE),
                "GRANT %s ON CATALOG TO ROLE %s" % ('CREATE_DATACONNECTION_AS_OWNER', ROLE),

                "GRANT %s ON DATACONNECTION %s TO ROLE %s" % ('SHOW', CXN, ROLE),
                "GRANT %s ON DATACONNECTION %s TO ROLE %s" % ('DROP', CXN, ROLE),
                "GRANT %s ON DATACONNECTION %s TO ROLE %s" % ('ALTER', CXN, ROLE),
                "GRANT %s ON DATACONNECTION %s TO ROLE %s" % ('USE', CXN, ROLE),

                "GRANT %s ON DATACONNECTION %s TO ROLE %s" % ('ALL', CXN2, ROLE),
                "GRANT %s ON DATACONNECTION %s TO ROLE %s" % ('USE', CXN2, ROLE)
            ]

            for ddl in ddls:
                conn.execute_ddl(ddl)

            # Verify that the root user (admin) can see both connections
            # If authorization is disabled or if user is an admin or if it's an internal
            # request, the user will always have 'ALL' permission
            ctx.disable_auth()
            connections = conn.manage_data_reg_connection("LIST", EMPTY_DRC, connection_pattern=CXN).connections
            assert len(connections) == 2
            sorted_names = sorted([connection.name for connection in connections])
            assert sorted_names[0] == CXN
            assert sorted_names[1] == CXN2
            for connection in connections:
                if connection.name in [CXN,CXN2]:
                    assert TAccessPermissionLevel.ALL in connection.access_levels

            ctx.enable_token_auth(token_str=USER)

            connections = conn.manage_data_reg_connection("LIST", EMPTY_DRC, connection_pattern=CXN).connections
            assert len(connections) == 2
            sorted_names = sorted([connection.name for connection in connections])
            assert sorted_names[0] == CXN
            assert sorted_names[1] == CXN2

            for connection in connections:
                if connection.name == CXN:
                    assert TAccessPermissionLevel.CREATE_DATACONNECTION_AS_OWNER not in connection.access_levels
                    assert TAccessPermissionLevel.SHOW in connection.access_levels
                    assert TAccessPermissionLevel.DROP in connection.access_levels
                    assert TAccessPermissionLevel.ALTER in connection.access_levels
                    assert TAccessPermissionLevel.USE in connection.access_levels
                if connection.name == CXN2:
                    assert TAccessPermissionLevel.CREATE_DATACONNECTION_AS_OWNER not in connection.access_levels
                    assert TAccessPermissionLevel.ALL in connection.access_levels
                    assert TAccessPermissionLevel.USE in connection.access_levels

            # Verify that a user with no access can't see the connection
            ctx.enable_token_auth(token_str=USER_NO_ACCESS)
            connections = conn.manage_data_reg_connection("LIST", EMPTY_DRC, connection_pattern=CXN).connections
            assert len(connections) == 0

    def test_dataconnection_connection_name_validation(self):
        CXN1 = 'test_connection_name_with_special_char_*'
        CXN2 = 'test_connection_name_with_special_char_$'
        CXN3 = 'test_connection_name_with_hyphen-'
        CXN4 = 'test_connection_name_   with_spaces_in_between'
        CXN5 = '    test_connection_name_with_leading_or_trailing_spaces    '
        VALID_CXN_NAME = 'test_valid_CONNECTION_name_123'

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            with self.assertRaises(TRecordServiceException) as ex_ctx:
                drc = self._get_mysqltest_data_reg_connection_obj(CXN1)
                conn.manage_data_reg_connection('CREATE', drc)
            self.assertTrue(
                "Connection names can only contain characters, numbers and '_'"
                in str(ex_ctx.exception))

            with self.assertRaises(TRecordServiceException) as ex_ctx:
                drc = self._get_mysqltest_data_reg_connection_obj(CXN2)
                conn.manage_data_reg_connection('CREATE', drc)
            self.assertTrue(
                "Connection names can only contain characters, numbers and '_'"
                in str(ex_ctx.exception))

            with self.assertRaises(TRecordServiceException) as ex_ctx:
                drc = self._get_mysqltest_data_reg_connection_obj(CXN3)
                conn.manage_data_reg_connection('CREATE', drc)
            self.assertTrue(
                "Connection names can only contain characters, numbers and '_'"
                in str(ex_ctx.exception))

            with self.assertRaises(TRecordServiceException) as ex_ctx:
                drc = self._get_mysqltest_data_reg_connection_obj(CXN4)
                conn.manage_data_reg_connection('CREATE', drc)
            self.assertTrue(
                "Connection names can only contain characters, numbers and '_'"
                in str(ex_ctx.exception))

            with self.assertRaises(TRecordServiceException) as ex_ctx:
                drc = self._get_mysqltest_data_reg_connection_obj(CXN5)
                conn.manage_data_reg_connection('CREATE', drc)
            self.assertTrue(
                "Connection names can only contain characters, numbers and '_'"
                in str(ex_ctx.exception))

            drc = self._get_mysqltest_data_reg_connection_obj(VALID_CXN_NAME)
            drcs = conn.manage_data_reg_connection('CREATE', drc)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertEqual(drcs.connections[0].name, VALID_CXN_NAME,
                             "Test for valid connection name failed.")
            # Delete connection after the test
            drcs = conn.manage_data_reg_connection('DELETE', drc)
            self.assertTrue(len(drcs.connections) == 0)

    def test_dataconnection_delegated_test_connection(self):
        CXN1 = 'test_privileges_connection_test1'
        CXN2 = 'test_privileges_connection_test2'
        CXN3 = 'test_privileges_connection_test3'
        ROLE1 = 'test_privileges_connection_role1'
        ROLE2 = 'test_privileges_connection_role2'
        USER1 = "test_privileges_connection_user1"
        USER2 = "test_privileges_connection_user2"
        USER_NO_ACCESS = "test_privileges_connection_user_no_access"
        ROOT = 'root'

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()

            ddls = [
                "DROP DATACONNECTION IF EXISTS %s" % (CXN1),
                "DROP DATACONNECTION IF EXISTS %s" % (CXN2),
                "DROP DATACONNECTION IF EXISTS %s" % (CXN3),
                "DROP ROLE IF EXISTS %s" % (ROLE1),
                "DROP ROLE IF EXISTS %s" % (ROLE2),

                # Create the role and grant it to the user
                "CREATE ROLE %s" % (ROLE1),
                "GRANT ROLE %s TO GROUP %s" % (ROLE1, USER1),
                "CREATE ROLE %s" % (ROLE2),
                "GRANT ROLE %s TO GROUP %s" % (ROLE2, USER2),

                # Grant the user the right permissions
                "GRANT CREATE_DATACONNECTION_AS_OWNER ON CATALOG TO ROLE %s" % (ROLE1),
            ]

            for ddl in ddls:
                conn.execute_ddl(ddl)

            # USER1 should be able to test the connection while creating it as it has
            # CREATE_DATACONNECTION_AS_OWNER access on the CATALOG
            ctx.enable_token_auth(token_str=USER1)
            drc_cxn1 = self._get_mysqltest_data_reg_connection_obj(CXN1)
            # test the connection
            drcs = conn.manage_data_reg_connection("TEST_CREATE", drc_cxn1)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertTrue(drcs.connections[0].test_status == "SUCCESS")
            # create the connection after successful testing
            conn.manage_data_reg_connection("CREATE", drc_cxn1)

            # USER2 should not be able to test CXN1.
            # USER2 must have 'ALL' or at least 'USE' access on CXN1
            ctx.enable_token_auth(token_str=USER2)
            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                conn.manage_data_reg_connection("TEST_EXISTING", drc_cxn1)
            self.assertTrue('The user must have the appropriate permissions' in str(ex_ctx.exception))

            # Grant 'USE' on CXN1 to USER2
            ctx.enable_token_auth(token_str=ROOT)
            conn.execute_ddl('GRANT USE ON DATACONNECTION %s TO ROLE %s' % (CXN1, ROLE2))

            # Now, USER2 should be able to test CXN1
            ctx.enable_token_auth(token_str=USER2)
            drcs = conn.manage_data_reg_connection("TEST_EXISTING", drc_cxn1)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertTrue(drcs.connections[0].test_status == "SUCCESS")

            # USER2 should NOT be able to test the connection (CXN2) while creating it as
            # it does not have CREATE_DATACONNECTION_AS_OWNER or ALL access on the CATALOG
            ctx.enable_token_auth(token_str=USER2)
            drc_cxn2 = self._get_mysqltest_data_reg_connection_obj(CXN2)
            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                conn.manage_data_reg_connection("TEST_CREATE", drc_cxn2)
            self.assertTrue('The user must have the appropriate permissions' in str(ex_ctx.exception))

            # Grant 'CREATE_DATACONNECTION_AS_OWNER' to USER2 on CATALOG
            ctx.enable_token_auth(token_str=ROOT)
            conn.execute_ddl('GRANT CREATE_DATACONNECTION_AS_OWNER ON CATALOG TO ROLE %s' % (ROLE2))

            # Now, USER2 should be able to test CXN2 while creating
            ctx.enable_token_auth(token_str=USER2)
            drcs = conn.manage_data_reg_connection("TEST_CREATE", drc_cxn2)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertTrue(drcs.connections[0].test_status == "SUCCESS")
            # create the connection after successful testing
            conn.manage_data_reg_connection("CREATE", drc_cxn2)

            # USER2 should also be able to test CXN2 while editing
            # test fails as the host is invalid
            ctx.enable_token_auth(token_str=USER2)
            drc_cxn2.host = 'invalid_mysql_host'
            drcs = conn.manage_data_reg_connection("TEST_EDIT", drc_cxn2)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertTrue(drcs.connections[0].test_status == "FAILED")

            # USER_NO_ACCESS should not be able to test any connection (CXN1 or CXN2)
            ctx.enable_token_auth(token_str=USER_NO_ACCESS)
            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                conn.manage_data_reg_connection("TEST_EXISTING", drc_cxn1)
            self.assertTrue('The user must have the appropriate permissions' in str(ex_ctx.exception))

            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                conn.manage_data_reg_connection("TEST_EXISTING", drc_cxn2)
            self.assertTrue('The user must have the appropriate permissions' in str(ex_ctx.exception))

            # If USER2 tries to test a connection with same name as CXN1 (which was created by USER1)
            # System throws an error asking user to use a different connection name.
            ctx.enable_token_auth(token_str=USER2)
            drc_cxn1 = self._get_mysqltest_data_reg_connection_obj(CXN1)
            # test the connection
            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                conn.manage_data_reg_connection("TEST_CREATE", drc_cxn1)
            self.assertTrue('Please use a different conneciton name.' in str(ex_ctx.exception))

            # 1. Lets create CXN3 with USER1.
            # 2. USER2 should not be able to test CXN3 even though it has
            #   'CREATE_DATACONNECTION_AS_OWNER' on the CATALOG because CXN3 is not
            #    created by USER2.
            # 3. USER2 must have 'ALL' or at least 'USE' access on CXN3
            ctx.enable_token_auth(token_str=USER1)
            drc_cxn3 = self._get_mysqltest_data_reg_connection_obj(CXN3)
            # create the connection
            conn.manage_data_reg_connection("CREATE", drc_cxn3)
            # try to test CXN2 with USER2, it would not be able to.
            ctx.enable_token_auth(token_str=USER2)
            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                conn.manage_data_reg_connection("TEST_EXISTING", drc_cxn3)
            self.assertTrue('The user must have the appropriate permissions' in str(ex_ctx.exception))

    def test_if_exists_clause_when_drop_connection(self):
        """ 'IF EXISTS' clause can not be specified through API calls.
            This test just verifies that the overall 'drop/delete connection'
            functionality works as expected.
        """
        MYSQL_CXN = 'test_if_exists_clause_mysql_conn'
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()

            # DELETE a connection which does not exist, it should throw an error
            drc = TDataRegConnection()
            drc.name = MYSQL_CXN
            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                conn.manage_data_reg_connection('DELETE', drc)
            self.assertTrue('Connection does not exist: %s' % MYSQL_CXN in str(ex_ctx.exception))

            # create a connection
            drc_cxn = self._get_mysqltest_data_reg_connection_obj(MYSQL_CXN)
            conn.manage_data_reg_connection("CREATE", drc_cxn)

            # ensure that the connection is successfully created
            drcs = conn.manage_data_reg_connection("GET", drc_cxn)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertTrue(drcs.connections[0].name == MYSQL_CXN)

            # DELETE the newly created connection
            drcs = conn.manage_data_reg_connection("DELETE", drc_cxn)
            self.assertTrue(len(drcs.connections) == 0)

            # get again and it returns empty
            drcs = conn.manage_data_reg_connection("GET", drc_cxn)
            self.assertTrue(len(drcs.connections) == 0)

    def test_if_not_exists_clause_when_create_connection(self):
        """ 'IF NOT EXISTS' clause can not be specified through API calls.
            This test just verifies that the overall 'create connection'
            functionality works as expected.
        """
        MYSQL_CXN = 'test_if_not_exists_clause_mysql_conn'
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()
            # Delete if exists
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS %s' % MYSQL_CXN)

            # create a connection
            drc_cxn = self._get_mysqltest_data_reg_connection_obj(MYSQL_CXN)
            conn.manage_data_reg_connection("CREATE", drc_cxn)

            # ensure that the connection is successfully created
            drcs = conn.manage_data_reg_connection("GET", drc_cxn)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertTrue(drcs.connections[0].name == MYSQL_CXN)

            # Try to create the same connection, it should throw an error.
            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
                conn.manage_data_reg_connection("CREATE", drc_cxn)
            self.assertTrue('Connection already exists: %s' % MYSQL_CXN in str(ex_ctx.exception))

            # DELETE the connection
            drcs = conn.manage_data_reg_connection("DELETE", drc_cxn)
            self.assertTrue(len(drcs.connections) == 0)

            # Re-create the connection and it should work
            drc_cxn = self._get_mysqltest_data_reg_connection_obj(MYSQL_CXN)
            conn.manage_data_reg_connection("CREATE", drc_cxn)

            # ensure that the connection is successfully created
            drcs = conn.manage_data_reg_connection("GET", drc_cxn)
            self.assertTrue(len(drcs.connections) == 1)
            self.assertTrue(drcs.connections[0].name == MYSQL_CXN)

    def test_snowflake_tags(self):
        """ Test that ensures we can sync tags from SF. This is based on the
            Nong Tags CI SF notebook (in their UI). """
        CXN = 'test_sf_tags_connection'
        DB = 'test_sf_tags_db'

        drc = self._get_snowflake_data_reg_connection_obj(CXN)
        drc.default_catalog = "TAGS_TEST_DB"
        drc.default_schema = "PUBLIC"
        drc.connection_properties = {'defaultDb':'PUBLIC'}

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            # The registration will automatically make them, clean these up in case
            # they exist
            conn.delete_attribute('DOMAIN_TYPE', 'table')
            conn.delete_attribute('domain_type', 'view')
            conn.delete_attribute('pii_type', 'restricted')
            conn.delete_attribute('pii_type', 'top secret')

            # Run this twice. We only run the clean up above for tags to test the
            # the case they already exist
            for _ in range(0, 1):
                conn.execute_ddl('DROP DATABASE IF EXISTS %s CASCADE' % DB)
                conn.execute_ddl('DROP DATACONNECTION IF EXISTS %s' % CXN)
                drcs = conn.manage_data_reg_connection("CREATE", drc)
                self.assertTrue(len(drcs.connections) == 1)

                conn.execute_ddl('DROP DATABASE IF EXISTS %s CASCADE' % DB)
                conn.execute_ddl("""CREATE DATABASE %s DBPROPERTIES(
                    'okera.connection.name' = '%s',
                    'supports.tags'='true',
                    'okera.autotagger.skip'='true')""" % (DB, CXN))
                conn.execute_ddl('ALTER DATABASE %s LOAD DEFINITIONS()' % DB)

                datasets = conn.list_dataset_names(DB)
                self.assertTrue('test_sf_tags_db.tag_demo_table' in datasets)
                self.assertTrue('test_sf_tags_db.tag_demo_view' in datasets)

                # Ensure they got created
                attrs = conn.list_attributes('domain_type')
                self.assertTrue(self._contains_attribute('domain_type', 'table', attrs))
                self.assertTrue(self._contains_attribute('domain_type', 'view', attrs))
                attrs = conn.list_attributes('pii_type')
                self.assertTrue(self._contains_attribute('pii_type', 'restricted', attrs))
                self.assertTrue(self._contains_attribute('pii_type', 'top secret', attrs))

                # Validate the tags
                ds = conn.list_datasets(DB, name='tag_demo_table')[0]

                # Table
                attr = ds.attribute_values[0].attribute
                self.assertEqual('domain_type', attr.attribute_namespace)
                self.assertEqual('table', attr.key)

                # Col tags (order is non deterministic)
                attr1 = ds.schema.cols[0].attribute_values[0].attribute
                attr2 = ds.schema.cols[0].attribute_values[1].attribute
                if attr1.attribute_namespace == 'domain_type':
                    self.assertEqual('table', attr1.key)
                    self.assertEqual('pii_type', attr2.attribute_namespace)
                    self.assertEqual('restricted', attr2.key)
                else:
                    self.assertEqual('domain_type', attr2.attribute_namespace)
                    self.assertEqual('table', attr2.key)
                    self.assertEqual('pii_type', attr1.attribute_namespace)
                    self.assertEqual('restricted', attr1.key)
                attr = ds.schema.cols[1].attribute_values[0].attribute
                self.assertEqual('domain_type', attr.attribute_namespace)
                self.assertEqual('table', attr.key)

                # View
                ds = conn.list_datasets(DB, name='tag_demo_view')[0]
                self.assertEqual('domain_type', attr.attribute_namespace)
                self.assertEqual('table', attr.key)

                # Col tags
                attr1 = ds.schema.cols[0].attribute_values[0].attribute
                attr2 = ds.schema.cols[0].attribute_values[1].attribute
                if attr1.attribute_namespace == 'domain_type':
                    self.assertEqual('view', attr1.key)
                    self.assertEqual('pii_type', attr2.attribute_namespace)
                    self.assertEqual('top secret', attr2.key)
                else:
                    self.assertEqual('domain_type', attr2.attribute_namespace)
                    self.assertEqual('view', attr2.key)
                    self.assertEqual('pii_type', attr1.attribute_namespace)
                    self.assertEqual('top secret', attr1.key)
                attr = ds.schema.cols[1].attribute_values[0].attribute
                self.assertEqual('domain_type', attr.attribute_namespace)
                self.assertEqual('view', attr.key)

                # Issue an alter to resync
                conn.execute_ddl('ALTER DATABASE %s LOAD DEFINITIONS(tag_demo_table)' % DB)

    @unittest.skip("This is not a CI test.")
    def test_snowflake_tags_demo(self):
        """ This is not really a test but some of the steps for an e2e demo. Parts of are
            tested above but this is used to validate the demo is working with changing
            state on the SF side. """
        CXN = 'test_sf_tags_connection'
        DB = 'test_sf_tags_db'

        drc = self._get_snowflake_data_reg_connection_obj(CXN)
        drc.default_catalog = "OKERA_DEMO"
        drc.default_schema = "HEALTHCARE"
        drc.connection_properties = {'defaultDb':'PUBLIC'}

        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            # The registration will automatically make them, clean these up in case
            # they exist
            conn.delete_attribute('DOMAIN_TYPE', 'table')
            conn.delete_attribute('domain_type', 'view')
            conn.delete_attribute('pii_type', 'restricted')
            conn.delete_attribute('pii_type', 'top secret')

            conn.execute_ddl('DROP DATABASE IF EXISTS %s CASCADE' % DB)
            conn.execute_ddl('DROP DATACONNECTION IF EXISTS %s' % CXN)
            drcs = conn.manage_data_reg_connection("CREATE", drc)
            self.assertTrue(len(drcs.connections) == 1)

            conn.execute_ddl('DROP DATABASE IF EXISTS %s CASCADE' % DB)
            conn.execute_ddl("""CREATE DATABASE %s DBPROPERTIES(
                'okera.connection.name' = '%s',
                'supports.tags'='true',
                'okera.autotagger.skip'='true')""" % (DB, CXN))
            conn.execute_ddl('ALTER DATABASE %s LOAD DEFINITIONS(PATIENT)' % DB)

            datasets = conn.list_dataset_names(DB)
            print(datasets)
            print(conn.execute_ddl('describe formatted test_sf_tags_db.patient'))

if __name__ == "__main__":
    unittest.main()

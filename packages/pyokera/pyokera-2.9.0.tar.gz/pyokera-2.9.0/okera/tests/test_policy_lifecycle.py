from datetime import datetime, timedelta, timezone
import time
import unittest

from okera import _thrift_api
from okera.tests import pycerebro_test_common as common

TEST_DB = "policy_lifecycle_test_db"
TEST_TBL = "test_tbl"
JDBC_TBL = "jdbc_tbl"
TEST_USER = "policy_lifecycle_user"
TEST_ROLE = "policy_lifecycle_role"
ATTRIBUTE_NAMESPACE = "policy_lifecycle"
ATTRIBUTE_NAME = "test_tag"
ATTRIBUTE = ATTRIBUTE_NAMESPACE + "." + ATTRIBUTE_NAME
CXN = "policy_lifecycle_steward_test_connection"

class PolicyLifecycleTest(common.TestBase):
    @classmethod
    def setUpClass(cls):
        super(PolicyLifecycleTest, cls).setUpClass()
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            conn.execute_ddl("DROP TABLE IF EXISTS %s.%s" % (TEST_DB, TEST_TBL))
            conn.execute_ddl("DROP TABLE IF EXISTS %s.%s" % (TEST_DB, JDBC_TBL))
            conn.execute_ddl("DROP DATABASE IF EXISTS %s" % (TEST_DB))
            conn.execute_ddl("DROP ROLE IF EXISTS %s" % TEST_ROLE)

            conn.execute_ddl("CREATE DATABASE %s" % TEST_DB)
            conn.create_attribute(ATTRIBUTE_NAMESPACE, ATTRIBUTE_NAME)
            conn.execute_ddl("CREATE TABLE %s.%s (col1 int) ATTRIBUTE %s" % (TEST_DB, TEST_TBL, ATTRIBUTE))

    def setUp(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
          conn.execute_ddl("CREATE ROLE %s" % TEST_ROLE)
          conn.execute_ddl("GRANT ROLE %s to GROUP %s" % (TEST_ROLE, TEST_USER))

    def tearDown(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            conn.execute_ddl("DROP ROLE IF EXISTS %s" % TEST_ROLE)

    def test_rbac_policy_respects_enabled_flag(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            # We should be starting in a fresh state with no access
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            self.assertEqual(0, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # Check that legacy grant works
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO ROLE %s""" % (TEST_DB, TEST_TBL, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)

            # No op
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO ROLE %s""" % (TEST_DB, TEST_TBL, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)

            ctx.disable_auth()
            conn.execute_ddl("""
              REVOKE SELECT ON TABLE %s.%s
              FROM %s""" % (TEST_DB, TEST_TBL, TEST_ROLE))

            # Revoke should have completed successfully
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)

            # Disabled GRANT should not give privileges to the table
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('enabled'='false')""" % (TEST_DB, TEST_TBL, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect no access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            # One disabled policy should be viewable
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # Enabled GRANT should give privileges to the table
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('enabled'='true')""" % (TEST_DB, TEST_TBL, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)
            # Still expect only one policy
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

    def test_abac_policy_respects_enabled_flag(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            # We should be starting in a fresh state with no access
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            self.assertEqual(0, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # Check that legacy grant works
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON DATABASE %s
              HAVING ATTRIBUTE(%s)
              TO ROLE %s""" % (TEST_DB, ATTRIBUTE, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)

            ctx.disable_auth()
            conn.execute_ddl("""
              REVOKE SELECT ON DATABASE %s
              HAVING ATTRIBUTE(%s)
              FROM ROLE %s""" % (TEST_DB, ATTRIBUTE, TEST_ROLE))

            # Revoke should have completed successfully
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)

            # Disabled GRANT should not give privileges to the table
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON DATABASE %s
              HAVING ATTRIBUTE(%s)
              TO ROLE %s
              POLICYPROPERTIES('enabled'='false')""" % (TEST_DB, ATTRIBUTE, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect no access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            # One disabled policy should be viewable
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # Enabled GRANT should give privileges to the table
            ctx.disable_auth()
            # This revoke is a bit strange. As of right now it isn't possible to have
            # privileges that differ only in their policyproperties, but if you could
            # this would break.
            conn.execute_ddl("""
              REVOKE SELECT ON DATABASE %s
              HAVING ATTRIBUTE(%s)
              FROM ROLE %s""" % (TEST_DB, ATTRIBUTE, TEST_ROLE))
            conn.execute_ddl("""
              GRANT SELECT ON DATABASE %s
              HAVING ATTRIBUTE(%s)
              TO ROLE %s
              POLICYPROPERTIES('enabled'='true')""" % (TEST_DB, ATTRIBUTE, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)
            # Still expect only one policy
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

    def test_rbac_policy_respects_start_time(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            # We should be starting in a fresh state with no access
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            self.assertEqual(0, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # Check that legacy grant works
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO ROLE %s""" % (TEST_DB, TEST_TBL, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)

            ctx.disable_auth()
            conn.execute_ddl("""
              REVOKE SELECT ON TABLE %s.%s
              FROM %s""" % (TEST_DB, TEST_TBL, TEST_ROLE))

            # Revoke should have completed successfully
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)

            # GRANT that starts in the future should not give privileges to the table
            one_hour_from_now = int(time.time()) + timedelta(hours=1).total_seconds()
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('start_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, TEST_ROLE, one_hour_from_now))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect no access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            # One disabled policy should be viewable
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # GRANT that starts in the past should give privileges to the table
            one_hour_ago = int(time.time()) - timedelta(hours=1).total_seconds()
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('start_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, TEST_ROLE, one_hour_ago))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)
            # Still expect only one policy
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

    def test_rbac_policy_respects_end_time(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            # We should be starting in a fresh state with no access
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            self.assertEqual(0, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # Check that legacy grant works
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO ROLE %s""" % (TEST_DB, TEST_TBL, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)

            ctx.disable_auth()
            conn.execute_ddl("""
              REVOKE SELECT ON TABLE %s.%s
              FROM %s""" % (TEST_DB, TEST_TBL, TEST_ROLE))

            # Revoke should have completed successfully
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)

            # GRANT that ends in the past should not give privileges to the table
            one_hour_ago = int(time.time()) - timedelta(hours=1).total_seconds()
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('end_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, TEST_ROLE, one_hour_ago))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect no access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            # One disabled policy should be viewable
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # GRANT that ends in the future should give privileges to the table
            one_hour_from_now = int(time.time()) + timedelta(hours=1).total_seconds()
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('end_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, TEST_ROLE, one_hour_from_now))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)
            # Still expect only one policy
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

    def test_rbac_policy_respects_start_and_end_times(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            # We should be starting in a fresh state with no access
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            self.assertEqual(0, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # Check that legacy grant works
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO ROLE %s""" % (TEST_DB, TEST_TBL, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)

            ctx.disable_auth()
            conn.execute_ddl("""
              REVOKE SELECT ON TABLE %s.%s
              FROM %s""" % (TEST_DB, TEST_TBL, TEST_ROLE))

            # Revoke should have completed successfully
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)

            current_time = int(time.time())
            two_hours_ago = current_time - timedelta(hours=2).total_seconds()
            one_hour_ago = current_time - timedelta(hours=1).total_seconds()
            one_hour_from_now = current_time + timedelta(hours=1).total_seconds()
            two_hours_from_now = current_time + timedelta(hours=2).total_seconds()

            # GRANT that starts and ends in the future should not give privileges
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('start_datetime'='%d', 'end_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, TEST_ROLE, one_hour_from_now, two_hours_from_now))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect no access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            # One disabled policy should be viewable
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # GRANT that starts in the past and ends in the future should give privileges
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('start_datetime'='%d', 'end_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, TEST_ROLE, one_hour_ago, one_hour_from_now))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)
            # Still expect only one policy
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # Grant that starts and ends in the past should not give privileges
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('start_datetime'='%d', 'end_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, TEST_ROLE, two_hours_ago, one_hour_ago))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect no access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            # One disabled policy should be viewable
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

    # ABAC start/end times

    def test_abac_policy_respects_start_time(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            # We should be starting in a fresh state with no access
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            self.assertEqual(0, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # Check that legacy grant works
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              TO ROLE %s""" % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)

            ctx.disable_auth()
            conn.execute_ddl("""
              REVOKE SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              FROM %s""" % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE))

            # Revoke should have completed successfully
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)

            # GRANT that starts in the future should not give privileges to the table
            one_hour_from_now = int(time.time()) + timedelta(hours=1).total_seconds()
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              TO %s
              POLICYPROPERTIES('start_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE, one_hour_from_now))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect no access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            # One disabled policy should be viewable
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # GRANT that starts in the past should give privileges to the table
            one_hour_ago = int(time.time()) - timedelta(hours=1).total_seconds()
            ctx.disable_auth()
            conn.execute_ddl("""
              REVOKE SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              FROM %s""" % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE))
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              TO %s
              POLICYPROPERTIES('start_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE, one_hour_ago))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)
            # Still expect only one policy
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

    def test_abac_policy_respects_end_time(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            # We should be starting in a fresh state with no access
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            self.assertEqual(0, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # Check that legacy grant works
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              TO ROLE %s""" % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)

            ctx.disable_auth()
            conn.execute_ddl("""
              REVOKE SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              FROM %s""" % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE))

            # Revoke should have completed successfully
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)

            # GRANT that ends in the past should not give privileges to the table
            one_hour_ago = int(time.time()) - timedelta(hours=1).total_seconds()
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              TO %s
              POLICYPROPERTIES('end_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE, one_hour_ago))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect no access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            # One disabled policy should be viewable
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # GRANT that ends in the future should give privileges to the table
            one_hour_from_now = int(time.time()) + timedelta(hours=1).total_seconds()
            ctx.disable_auth()
            conn.execute_ddl("""
              REVOKE SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              FROM %s""" % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE))
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              TO %s
              POLICYPROPERTIES('end_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE, one_hour_from_now))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)
            # Still expect only one policy
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

    def test_abac_policy_respects_start_and_end_times(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            # We should be starting in a fresh state with no access
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            self.assertEqual(0, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # Check that legacy grant works
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              TO ROLE %s""" % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE))

            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)

            ctx.disable_auth()
            conn.execute_ddl("""
              REVOKE SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              FROM %s""" % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE))

            # Revoke should have completed successfully
            ctx.enable_token_auth(token_str=TEST_USER)
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)

            current_time = int(time.time())
            two_hours_ago = current_time - timedelta(hours=2).total_seconds()
            one_hour_ago = current_time - timedelta(hours=1).total_seconds()
            one_hour_from_now = current_time + timedelta(hours=1).total_seconds()
            two_hours_from_now = current_time + timedelta(hours=2).total_seconds()

            # GRANT that starts and ends in the future should not give privileges
            ctx.disable_auth()
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              TO %s
              POLICYPROPERTIES('start_datetime'='%d', 'end_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE, one_hour_from_now, two_hours_from_now))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect no access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            # One disabled policy should be viewable
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # GRANT that starts in the past and ends in the future should give privileges
            ctx.disable_auth()
            conn.execute_ddl("""
              REVOKE SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              FROM %s""" % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE))
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              TO %s
              POLICYPROPERTIES('start_datetime'='%d', 'end_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE, one_hour_ago, one_hour_from_now))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 1)
            # Still expect only one policy
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

            # Grant that starts and ends in the past should not give privileges
            ctx.disable_auth()
            conn.execute_ddl("""
              REVOKE SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              FROM %s""" % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE))
            conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              HAVING ATTRIBUTE(%s)
              TO %s
              POLICYPROPERTIES('start_datetime'='%d', 'end_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, ATTRIBUTE, TEST_ROLE, two_hours_ago, one_hour_ago))

            ctx.enable_token_auth(token_str=TEST_USER)
            # Expect no access to the table
            self.verify_tbl_access(conn, TEST_DB, TEST_TBL, 0)
            # One disabled policy should be viewable
            self.assertEqual(1, self._ddl_count(
                    conn, 'SHOW GRANT ROLE %s ON CATALOG' % TEST_ROLE))

    # Test granting AS OWNER on the catalog for creating
    # both connections and databases
    def test_steward_create_as_owner_respects_enabled_flag(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()

            ddls = [
                "DROP DATACONNECTION IF EXISTS %s" % (CXN),

                """
                GRANT CREATE_DATACONNECTION_AS_OWNER ON CATALOG
                TO ROLE %s
                POLICYPROPERTIES('enabled'='false')
                """ % (TEST_ROLE),

                """
                GRANT CREATE_AS_OWNER ON DATABASE %s
                TO ROLE %s
                POLICYPROPERTIES('enabled'='false')
                """ % (TEST_DB, TEST_ROLE),
            ]

            for ddl in ddls:
                conn.execute_ddl(ddl)

            # Steward user should not have access because GRANTs are disabled
            ctx.enable_token_auth(token_str=TEST_USER)

            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
              conn.execute_ddl(
              """
              CREATE DATACONNECTION %s CXNPROPERTIES
              (
              'connection_type'='JDBC',
              'jdbc_driver'='mysql',
              'host'='cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com',
              'port'='3306',
              'user_key'='awsps:///mysql/username',
              'password_key'='awsps:///mysql/password',
              'jdbc.db.name'='jdbc_test'
              )
            """ % (CXN))
            self.assertTrue('not have privileges' in str(ex_ctx.exception), "DDL: %s, Exception: %s" % (ddl, str(ex_ctx.exception)))

            ctx.disable_auth()
            conn.execute_ddl("""
            REVOKE CREATE_DATACONNECTION_AS_OWNER ON CATALOG
            FROM ROLE %s
            """ % TEST_ROLE)

            conn.execute_ddl("""
            GRANT CREATE_DATACONNECTION_AS_OWNER ON CATALOG
            TO ROLE %s
            POLICYPROPERTIES('enabled'='true')
            """ % TEST_ROLE)

            ctx.enable_token_auth(token_str=TEST_USER)
            # should now be able to create data connection, but still shouldn't be able
            # to create the table
            conn.execute_ddl("""
            CREATE DATACONNECTION %s CXNPROPERTIES
            (
            'connection_type'='JDBC',
            'jdbc_driver'='mysql',
            'host'='cerebro-db-test-long-running.cyn8yfvyuugz.us-west-2.rds.amazonaws.com',
            'port'='3306',
            'user_key'='awsps:///mysql/username',
            'password_key'='awsps:///mysql/password',
            'jdbc.db.name'='jdbc_test'
            )
            """ % (CXN))

            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
              conn.execute_ddl(
              """
              CREATE EXTERNAL TABLE %s.%s STORED as JDBC
              TBLPROPERTIES(
              'driver' = 'mysql',
              'okera.connection.name' = '%s',
              'jdbc.db.name'='jdbc_test',
              'jdbc.schema.name'='public',
              'table' = 'filter_pushdown_test'
              )""" % (TEST_DB, JDBC_TBL, CXN))
            self.assertTrue('not have privileges' in str(ex_ctx.exception), "DDL: %s, Exception: %s" % (ddl, str(ex_ctx.exception)))

            ctx.disable_auth()
            conn.execute_ddl("""
            REVOKE CREATE_AS_OWNER ON DATABASE %s
            FROM ROLE %s
            """ % (TEST_DB, TEST_ROLE))

            conn.execute_ddl( """
            GRANT CREATE_AS_OWNER ON DATABASE %s
            TO ROLE %s
            POLICYPROPERTIES('enabled'='true')
            """ % (TEST_DB, TEST_ROLE),)

            # Check now that GRANTs are enabled
            ctx.enable_token_auth(token_str=TEST_USER)

            conn.execute_ddl(
            """
            CREATE EXTERNAL TABLE %s.%s STORED as JDBC
            TBLPROPERTIES(
            'driver' = 'mysql',
            'okera.connection.name' = '%s',
            'jdbc.db.name'='jdbc_test',
            'jdbc.schema.name'='public',
            'table' = 'filter_pushdown_test'
            )""" % (TEST_DB, JDBC_TBL, CXN))

            res = conn.scan_as_json('select bigint_col from %s.%s WHERE smallint_col=2' % (TEST_DB, JDBC_TBL))
            assert len(res) == 1
            assert res[0]['bigint_col'] == 4


    # Input validation tests
    def test_enabled_must_be_boolean(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()
            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
              conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('enabled'='%s')
              """ % (TEST_DB, TEST_TBL, TEST_ROLE, "ASDFASDF"))

            self.assertTrue('enabled must a boolean string' in str(ex_ctx.exception), "Exception: %s" % (str(ex_ctx.exception)))

    def test_start_datetime_must_be_long(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()
            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
              conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('start_datetime'='%s')
              """ % (TEST_DB, TEST_TBL, TEST_ROLE, "ASDFASDF"))

            self.assertTrue('start_datetime must a positive long value representing a Unix epoch time' in str(ex_ctx.exception), "Exception: %s" % (str(ex_ctx.exception)))

    def test_end_datetime_must_be_long(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()
            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
              conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('end_datetime'='%s')
              """ % (TEST_DB, TEST_TBL, TEST_ROLE, "ASDFASDF"))

            self.assertTrue('end_datetime must a positive long value representing a Unix epoch time' in str(ex_ctx.exception), "Exception: %s" % (str(ex_ctx.exception)))

    def test_start_datetime_must_be_before_end_datetime(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            ctx.disable_auth()
            one_hour_from_now = int(time.time()) + timedelta(hours=1).total_seconds()
            one_hour_ago = int(time.time()) - timedelta(hours=1).total_seconds()
            with self.assertRaises(_thrift_api.TRecordServiceException) as ex_ctx:
              conn.execute_ddl("""
              GRANT SELECT ON TABLE %s.%s
              TO %s
              POLICYPROPERTIES('start_datetime'='%d', 'end_datetime'='%d')
              """ % (TEST_DB, TEST_TBL, TEST_ROLE, one_hour_from_now, one_hour_ago))

            self.assertTrue('start_datetime must be before end_datetime' in str(ex_ctx.exception), "Exception: %s" % (str(ex_ctx.exception)))

if __name__ == '__main__':
    unittest.main()
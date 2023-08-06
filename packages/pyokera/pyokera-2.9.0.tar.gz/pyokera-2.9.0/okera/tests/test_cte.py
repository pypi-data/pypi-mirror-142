# Copyright 2019 Okera Inc. All Rights Reserved.
#
# Tests for CTE rewrite
#
#
# Note about v2 vs v3. In v2, the user is expected to author against our
# (via presto) catalog. This means the table and column names are what
# we return, not what is in the native (e.g. snowflake) system.
# In V3, the original user query is expected to be what it would author
# against the native system.
#

import pytest
import sqlparse
import unittest

from inspect import currentframe, getframeinfo

from okera._thrift_api import TAuthorizeQueryClient
from okera._thrift_api import TRecordServiceException

from okera.tests import pycerebro_test_common as common
from okera.tests import snowflake_cte_test_cases

SKIP_LEVELS = ["smoke", "dev", "all", "checkin"]

# Alias to shorten test code
PRESTO = TAuthorizeQueryClient.PRESTO
SNOWFLAKE = TAuthorizeQueryClient.SNOWFLAKE

CLIENT_NAMES = {
  PRESTO: 'presto',
  SNOWFLAKE: 'snowflake'
}

# This is created and set with a "standard" config
TEST_USER = 'testuser'
TEST_ROLE = "cte_sf_test_role"

# Format for test cases. It consists of tuples, each tuple represents a test
# query, test user and a list tuple of expected results. The list contains pairs of
# lists of clients to the expected result.
GENERAL_CASES = [
  # Two examples, first is compatible for all clients, second for snowflake only
#  (getframeinfo(currentframe()).lineno,
#      'SELECT 1', None, [(None, 'SELECT 1')]),
#  (getframeinfo(currentframe()).lineno,
#      'SELECT 1', TEST_USER, [([SNOWFLAKE], 'SELECT 1')]),
  (getframeinfo(currentframe()).lineno,
      """
      select STRING || STRING, concat(STRING, STRING)
      FROM DEMO_DB.JDBC_TEST.ALL_TYPES
      """, None, [
      ([SNOWFLAKE],
"""
SELECT concat(STRING, STRING),
       concat(STRING, STRING)
FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES" "ALL_TYPES"
""")
  ]),

#  (getframeinfo(currentframe()).lineno,
#      """
#      select '1' + 1, '1'::DOUBLE + 1;
#      FROM DEMO_DB.JDBC_TEST.ALL_TYPES
#      """, None, [
#      ([SNOWFLAKE],
#"""
#SELECT concat(STRING, STRING), concat(STRING, STRING)
#FROM demo_db.jdbc_test.all_types
#""")
#  ]),

  # Iterate over all cases, quoting and aliases (cased and quoted)
  (getframeinfo(currentframe()).lineno,
      'SELECT NATIONKEY FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], 'SELECT NATIONKEY FROM "TPCH_TEST"."PUBLIC"."NATION" "NATION"')
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT nationkey FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], 'SELECT nationkey FROM "TPCH_TEST"."PUBLIC"."NATION" "NATION"')
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT nationKey FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], 'SELECT nationKey FROM "TPCH_TEST"."PUBLIC"."NATION" "NATION"')
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT "NATIONKEY" FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], 'SELECT "NATIONKEY" FROM "TPCH_TEST"."PUBLIC"."NATION" "NATION"')
  ]),
  # This is invalid directly against snowflake due to the original query's "nationKey"
  # (wrong case and quotes)
  (getframeinfo(currentframe()).lineno,
      'SELECT "nationKey" FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], None)
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT NATIONKEY as N FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], 'SELECT NATIONKEY N FROM "TPCH_TEST"."PUBLIC"."NATION" "NATION"')
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT NATIONKEY N FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], 'SELECT NATIONKEY N FROM "TPCH_TEST"."PUBLIC"."NATION" "NATION"')
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT NATIONKEY n FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], 'SELECT NATIONKEY n FROM "TPCH_TEST"."PUBLIC"."NATION" "NATION"')
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT NATIONKEY "N" FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], 'SELECT NATIONKEY "N" FROM "TPCH_TEST"."PUBLIC"."NATION" "NATION"')
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT NATIONKEY "n" FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], 'SELECT NATIONKEY "n" FROM "TPCH_TEST"."PUBLIC"."NATION" "NATION"')
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT nationkey FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], 'SELECT nationkey FROM "TPCH_TEST"."PUBLIC"."NATION" "NATION"')
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT nationKey FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], 'SELECT nationKey FROM "TPCH_TEST"."PUBLIC"."NATION" "NATION"')
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT "NATIONKEY" FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], 'SELECT "NATIONKEY" FROM "TPCH_TEST"."PUBLIC"."NATION" "NATION"')
  ]),
  # This is invalid directly against snowflake due to the original query's, "nationKey"
  # (wrong case and quotes)
  (getframeinfo(currentframe()).lineno,
      'SELECT "nationKey" FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], None)
  ]),
  # This is invalid directly against snowflake due to the original "nationKey"
  # (wrong case and quotes)
  (getframeinfo(currentframe()).lineno,
      'SELECT "nationKey" "n" FROM TPCH_TEST.PUBLIC.NATION', None, [
      ([SNOWFLAKE], None)
  ]),

  # same as above but  for test user
  (getframeinfo(currentframe()).lineno,
      'SELECT NATIONKEY FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT NATIONKEY
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT nationkey FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT nationkey
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT nationKey FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT nationKey
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT "NATIONKEY" FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT "NATIONKEY"
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
# This is invalid directly against snowflake due to the original query's "nationKey"
# (wrong case and quotes)
#  (getframeinfo(currentframe()).lineno,
#      'SELECT "nationKey" FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
#      ([SNOWFLAKE],
#"""
#WITH okera_rewrite_tpch_test_snowflake__nation AS
#  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
#     FROM "TPCH_TEST"."PUBLIC"."NATION")
#SELECT "nationKey"
#FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
#""")
#  ]),

  (getframeinfo(currentframe()).lineno,
      'SELECT NATIONKEY as N FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT NATIONKEY N
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT NATIONKEY N FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT NATIONKEY N
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT NATIONKEY n FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT NATIONKEY n
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT NATIONKEY "N" FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT NATIONKEY "N"
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT NATIONKEY "n" FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT NATIONKEY "n"
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT nationkey FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT nationkey
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT nationkey FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT nationkey
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT "NATIONKEY" FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT "NATIONKEY"
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      'SELECT "NATIONKEY" "n" FROM TPCH_TEST.PUBLIC.NATION', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__nation AS
  (SELECT okera_udfs.public.tokenize("NATIONKEY", last_query_id()) as "NATIONKEY"
     FROM "TPCH_TEST"."PUBLIC"."NATION")
SELECT "NATIONKEY" "n"
FROM okera_rewrite_tpch_test_snowflake__nation "NATION"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      """
      select
          "a11"."SUPPKEY" "SUPPKEY",
          (sum("a11"."AVAILQTY") + sum("a11"."SUPPLYCOST")) "WJXBFS1"
          from    "TPCH_TEST"."PUBLIC"."PARTSUPP"    "a11"
          where   "a11"."SUPPKEY" = 1
          group by    "a11"."SUPPKEY"
      """, TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_tpch_test_snowflake__partsupp AS
  (SELECT okera_udfs.public.tokenize("SUPPKEY", last_query_id()) as "SUPPKEY",
          "AVAILQTY",
          "SUPPLYCOST"
   FROM "TPCH_TEST"."PUBLIC"."PARTSUPP")
SELECT "a11"."SUPPKEY" "SUPPKEY",
       (sum("a11"."AVAILQTY") + sum("a11"."SUPPLYCOST")) "WJXBFS1"
FROM okera_rewrite_tpch_test_snowflake__partsupp "a11"
WHERE ("a11"."SUPPKEY" = 1)
GROUP BY "a11"."SUPPKEY"
""")
  ]),
]

#
# These cases as nested how we alias the transformed column in the CTE block. We
# need to name these columns, preserving the original identifier so that the
# original user query works. In otherwise, the names of the columns in the CTE need
# to match the original table.
#
# For snowflake: our strategy is to always quote the original table column name
# as the alias. This works because:
#   1. Quoted upper cases is ignored, its the same as non-quoted upper case
#   2. Originally non-quoted columns in SF as stored as upper case.
#
IDENTIFIER_ALIASES = [
  (getframeinfo(currentframe()).lineno,
      'SELECT * FROM DEMO_DB.JDBC_TEST.MIXED_IDENTIFIERS', TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_jdbc_test_snowflake__mixed_identifiers AS
  (SELECT CAST(0 AS BIGINT) as "LOWER_NO_QUOTES",
          CAST(0 AS BIGINT) as "lower_quotes",
          CAST(0 AS BIGINT) as "MIXEDNOQUOTES",
          CAST(0 AS BIGINT) as "mixedQuotes",
          CAST(0 AS BIGINT) as "UPPER_NO_QUOTES",
          CAST(0 AS BIGINT) as "UPPER_QUOTES"
   FROM "DEMO_DB"."JDBC_TEST"."MIXED_IDENTIFIERS")
SELECT *
FROM okera_rewrite_jdbc_test_snowflake__mixed_identifiers "MIXED_IDENTIFIERS"
""")
  ]),
  (getframeinfo(currentframe()).lineno,
      """SELECT LOWER_NO_QUOTES,
              "lower_quotes",
              mixedNoQuotes,
              "mixedQuotes",
              UPPER_NO_QUOTES,
              "UPPER_QUOTES"
              FROM DEMO_DB.JDBC_TEST.MIXED_IDENTIFIERS""", TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_jdbc_test_snowflake__mixed_identifiers AS
  (SELECT CAST(0 AS BIGINT) as "LOWER_NO_QUOTES",
          CAST(0 AS BIGINT) as "lower_quotes",
          CAST(0 AS BIGINT) as "MIXEDNOQUOTES",
          CAST(0 AS BIGINT) as "mixedQuotes",
          CAST(0 AS BIGINT) as "UPPER_NO_QUOTES",
          CAST(0 AS BIGINT) as "UPPER_QUOTES"
   FROM "DEMO_DB"."JDBC_TEST"."MIXED_IDENTIFIERS")
SELECT LOWER_NO_QUOTES,
      "lower_quotes",
      mixedNoQuotes,
      "mixedQuotes",
      UPPER_NO_QUOTES,
      "UPPER_QUOTES"
FROM okera_rewrite_jdbc_test_snowflake__mixed_identifiers "MIXED_IDENTIFIERS"
""")
  ]),

# For columns not originally case-sensitive, try some permutations. The case sensitive
# ones fail in snowflake originally, as expected, if they don't match.
  (getframeinfo(currentframe()).lineno,
      """SELECT LOWER_NO_QUOTES,
              lower_no_QUOTES,
              mixedNoQuotes,
              mixednoquotes,
              UPPER_NO_QUOTES,
              upper_NO_quotes
              FROM DEMO_DB.JDBC_TEST.MIXED_IDENTIFIERS""", TEST_USER, [
      ([SNOWFLAKE],
"""
WITH okera_rewrite_jdbc_test_snowflake__mixed_identifiers AS
  (SELECT CAST(0 AS BIGINT) as "LOWER_NO_QUOTES",
          CAST(0 AS BIGINT) as "MIXEDNOQUOTES",
          CAST(0 AS BIGINT) as "UPPER_NO_QUOTES"
   FROM "DEMO_DB"."JDBC_TEST"."MIXED_IDENTIFIERS")
SELECT LOWER_NO_QUOTES,
       lower_no_QUOTES,
       mixedNoQuotes,
       mixednoquotes,
       UPPER_NO_QUOTES,
       upper_NO_quotes
FROM okera_rewrite_jdbc_test_snowflake__mixed_identifiers "MIXED_IDENTIFIERS"
""")
  ]),
]

class AuthorizeQueryTest(common.TestBase):
    def role_setup(self, conn):
      self._recreate_test_role(conn, TEST_ROLE, [TEST_USER])
      ddls = [
        'DROP ATTRIBUTE IF EXISTS snowflake_test.attr',
        'CREATE ATTRIBUTE snowflake_test.attr',
        'ALTER TABLE tpch_test_snowflake.nation ADD COLUMN ATTRIBUTE nationkey %s'\
             % 'snowflake_test.attr',
        'ALTER TABLE tpch_test_snowflake.partsupp ADD COLUMN ATTRIBUTE suppkey %s'\
             % 'snowflake_test.attr',
        'ALTER TABLE jdbc_test_snowflake.mixed_identifiers ADD ATTRIBUTE %s'\
             % 'snowflake_test.attr',
        ('GRANT SELECT ON TABLE tpch_test_snowflake.nation TRANSFORM %s ' +
         'WITH %s TO ROLE %s') % ('snowflake_test.attr', 'tokenize()', TEST_ROLE),
        ('GRANT SELECT ON TABLE tpch_test_snowflake.partsupp TRANSFORM %s ' +
         'WITH %s TO ROLE %s') % ('snowflake_test.attr', 'tokenize()', TEST_ROLE),
        ('GRANT SELECT ON TABLE jdbc_test_snowflake.mixed_identifiers TRANSFORM %s ' +
         'WITH %s TO ROLE %s') % ('snowflake_test.attr', 'zero()', TEST_ROLE),
      ]
      for ddl in ddls:
          conn.execute_ddl(ddl)

    def cte(self, conn, sql, client, user=None):
      result, plan, _, _ = self.cte_rewrite(
          conn, sql, user=user, client=client, generate_plan=True,
          validate_rewrite=True)
      self.assertTrue(plan is not None)
      return result

    # Runs all queries in cases that are compatible with target_client
    def run_client(self, cases, conn, target_client, user=None, test_case=None):
        for (lineno, sql, u, results) in cases:
            if u != user:
                continue
            if test_case != None and test_case != lineno:
                continue

            for clients, expected in results:
                if clients == None or target_client in clients:
                    self.role_setup(conn)

                    header = "\n------------ Test Case@%s (%s, %s) ----------------\n" % \
                        (lineno, user, CLIENT_NAMES[target_client])
                    header += sql + '\n'
                    print(header)
                    if expected:
                        result = self.cte(conn, sql, user=user, client=target_client)
                        self.assert_sql_equals(expected, result, error_header=header)
                    else:
                        # We currently can't run these tests. These require turning off ignoring
                        # case sensitivity in the driver, which breaks other tests.
                        return
                        #with self.assertRaises(TRecordServiceException) as ex:
                        #    result = self.cte(conn, sql, user=user, client=target_client)
                        #    header += 'Expected query to fail but did not.\nResult:\n'
                        #    header += result
                        #    self.assertFalse(True, msg=header)

    @unittest.skip("Ad-hoc harness for development to try a query, not a test")
    def test_snowflake_adhoc(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            sql = """
            select
                "a11"."SUPPKEY" "SUPPKEY",
                (sum("a11"."AVAILQTY") + sum("a11"."SUPPLYCOST")) "WJXBFS1"
                from    "TPCH_TEST"."PUBLIC"."PARTSUPP"    "a11"
                where   "a11"."SUPPKEY" = 1
                group by    "a11"."SUPPKEY"
            """
            print()
            print(sqlparse.format(self.cte(conn, sql, SNOWFLAKE), reindent=True))

    @unittest.skip("Does not work in CI, multi connections, same table.")
    def test_snowflake_general(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            self.run_client(GENERAL_CASES, conn, SNOWFLAKE)
            self.run_client(GENERAL_CASES, conn, SNOWFLAKE, TEST_USER)

    @unittest.skipIf(common.should_skip(SKIP_LEVELS, "snowflake-cte"), "Skip at level")
    def test_snowflake_v2(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            for (f, line, sql, expected) in snowflake_cte_test_cases.V2_PRESTO_TESTS:
                f = f.split('/')[-1]
                header = "\n--------------- Test Case@%s:%s -------------------\n" % \
                    (f, line)
                header += sql + '\n'
                print(header)
                result = self.cte(conn, sql, client=PRESTO)
                self.assert_sql_equals(expected, result, error_header=header)

    @unittest.skipIf(common.should_skip(SKIP_LEVELS, "snowflake-cte"), "Skip at level")
    def test_snowflake_identifiers(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            self.run_client(IDENTIFIER_ALIASES, conn, SNOWFLAKE, TEST_USER)

    @unittest.skipIf(common.should_skip(SKIP_LEVELS, "snowflake-cte"), "Skip at level")
    def test_snowflake_policy_v2(self):
        self.maxDiff = None
        ctx = common.get_test_context()

        # Tuple of (policy, query, expected rewrite)
        policies = [
            # Try a few cases and quotes on the STRING column
            ("""
              GRANT SELECT ON TABLE jdbc_test_snowflake.all_types
              WHERE if (`int` > 100, true, false)
              TO ROLE sf_test_role
            """,
            """SELECT "STRING" FROM jdbc_test_snowflake.all_types""",
            """
            WITH okera_rewrite_jdbc_test_snowflake__all_types AS
                (SELECT "STRING" as "string"
                FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES"
                WHERE iff("INT" > 100, TRUE, FALSE))
            SELECT "STRING" FROM okera_rewrite_jdbc_test_snowflake__all_types "all_types"
            """),
            ("""
              GRANT SELECT ON TABLE jdbc_test_snowflake.all_types
              WHERE if (`int` > 100, true, false)
              TO ROLE sf_test_role
            """,
            """SELECT STRING FROM jdbc_test_snowflake.all_types""",
            """
            WITH okera_rewrite_jdbc_test_snowflake__all_types AS
                (SELECT "STRING" as "string"
                FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES"
                WHERE iff("INT" > 100, TRUE, FALSE))
            SELECT STRING FROM okera_rewrite_jdbc_test_snowflake__all_types "all_types"
            """),
            ("""
              GRANT SELECT ON TABLE jdbc_test_snowflake.all_types
              WHERE if (`int` > 100, true, false)
              TO ROLE sf_test_role
            """,
            """SELECT "string" FROM jdbc_test_snowflake.all_types""",
            """
            WITH okera_rewrite_jdbc_test_snowflake__all_types AS
                (SELECT "STRING" as "string"
                FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES"
                WHERE iff("INT" > 100, TRUE, FALSE))
            SELECT "string" FROM okera_rewrite_jdbc_test_snowflake__all_types "all_types"
            """),

            ("""
              GRANT SELECT ON TABLE jdbc_test_snowflake.all_types
              WHERE if (`int` > 100, true, false)
              TO ROLE sf_test_role
            """,
            """SELECT "STRING" FROM jdbc_test_snowflake.all_types
               WHERE IF ("INT" > 1, true, false)""",
            """
            WITH okera_rewrite_jdbc_test_snowflake__all_types AS
              (SELECT "STRING" as "string", "INT" as "int"
               FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES"
               WHERE iff("INT" > 100, TRUE, FALSE))
            SELECT "STRING"
            FROM okera_rewrite_jdbc_test_snowflake__all_types "all_types"
            WHERE IFF(("INT" > 1), true, false)
            """),

            ("""
              GRANT SELECT ON TABLE jdbc_test_snowflake.all_types
              WHERE sets_intersect(`string`, 'hello') OR
                    sets_intersect(`string`, user_attribute('not_exist'))
              TO ROLE sf_test_role""",
            """SELECT "STRING" FROM jdbc_test_snowflake.all_types""",
            """
              WITH okera_rewrite_jdbc_test_snowflake__all_types AS
                (SELECT "STRING" as "string" FROM
                "DEMO_DB"."JDBC_TEST"."ALL_TYPES"
                WHERE arrays_overlap(split("STRING", ','), split('hello', ','))
                OR arrays_overlap(split("STRING", ','), split(NULL, ',')))
              SELECT "STRING" FROM
              okera_rewrite_jdbc_test_snowflake__all_types "all_types"
            """),
            ("""
              GRANT SELECT ON TABLE jdbc_test_snowflake.array_test
              WHERE array_contains(to_variant('donald'), to_array(column1))
              TO ROLE sf_test_role""",
            """SELECT * from jdbc_test_snowflake.array_test""",
            """
              WITH okera_rewrite_jdbc_test_snowflake__array_test AS (SELECT
              "ID" as "id",
              "COLUMN1" as "column1",
              "COLUMN2" as "column2"
              FROM "DEMO_DB"."JDBC_TEST"."ARRAY_TEST"
              WHERE "array_contains"("to_variant"('donald'), "to_array"("COLUMN1")))
              SELECT *
              FROM
              okera_rewrite_jdbc_test_snowflake__array_test "array_test"
            """),
        ]

        with common.get_planner(ctx) as conn:
            conn.execute_ddl("DROP ATTRIBUTE IF EXISTS snowflake_test.attr")
            conn.execute_ddl("CREATE ATTRIBUTE snowflake_test.attr")
            for policy, query, expected in policies:
                print("\n------------------ Test Case -------------------")
                print("Policy:")
                print(policy)
                print("Query:")
                print(query)
                self._recreate_test_role(conn, 'sf_test_role', ['sf_testuser'])
                conn.execute_ddl(policy)

                result = self.cte(conn, query,
                    user='sf_testuser', client=TAuthorizeQueryClient.PRESTO)
                self.assert_sql_equals(expected, result)

    @unittest.skipIf(common.should_skip(SKIP_LEVELS, "snowflake-cte"), "Skip at level")
    def test_snowflake_policy_v3(self):
        self.maxDiff = None
        ctx = common.get_test_context()

        # Tuple of (policy, query, expected rewrite)
        policies = [
            ("""
              GRANT SELECT ON TABLE jdbc_test_snowflake.all_types
              WHERE if (`int` > 100, true, false)
              TO ROLE sf_test_role
            """,
            """SELECT "STRING" FROM DEMO_DB.JDBC_TEST.ALL_TYPES""",
            """
            WITH okera_rewrite_jdbc_test_snowflake__all_types AS
                (SELECT "STRING" FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES"
                WHERE iff("INT" > 100, TRUE, FALSE))
            SELECT "STRING" FROM okera_rewrite_jdbc_test_snowflake__all_types "ALL_TYPES"
            """),

            ("""
              GRANT SELECT ON TABLE jdbc_test_snowflake.all_types
              WHERE if (`int` > 100, true, false)
              TO ROLE sf_test_role
            """,
            """SELECT "STRING" FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES"
               WHERE IF ("INT" > 1, true, false)""",
            """
            WITH okera_rewrite_jdbc_test_snowflake__all_types AS
              (SELECT "STRING", "INT"
               FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES"
               WHERE iff("INT" > 100, TRUE, FALSE))
            SELECT "STRING"
            FROM okera_rewrite_jdbc_test_snowflake__all_types "ALL_TYPES"
            WHERE IFF(("INT" > 1), true, false)
            """),

            ("""
              GRANT SELECT ON TABLE jdbc_test_snowflake.all_types
              WHERE sets_intersect(`string`, 'hello') OR
                    sets_intersect(`string`, user_attribute('not_exist'))
              TO ROLE sf_test_role""",
            """SELECT STRING FROM DEMO_DB.JDBC_TEST.ALL_TYPES""",
            """
              WITH okera_rewrite_jdbc_test_snowflake__all_types AS
                (SELECT "STRING" FROM
                "DEMO_DB"."JDBC_TEST"."ALL_TYPES"
                WHERE arrays_overlap(split("STRING", ','), split('hello', ','))
                OR arrays_overlap(split("STRING", ','), split(NULL, ',')))
              SELECT STRING FROM
              okera_rewrite_jdbc_test_snowflake__all_types "ALL_TYPES"
            """),
            ("""
              GRANT SELECT ON TABLE jdbc_test_snowflake.array_test
              WHERE array_contains(to_variant('donald'), to_array(column1))
              TO ROLE sf_test_role""",
            """SELECT * from DEMO_DB.JDBC_TEST.ARRAY_TEST""",
            """
              WITH okera_rewrite_jdbc_test_snowflake__array_test AS (SELECT
                "ID",
                "COLUMN1",
                "COLUMN2"
                FROM "DEMO_DB"."JDBC_TEST"."ARRAY_TEST"
                WHERE "array_contains"("to_variant"('donald'), "to_array"("COLUMN1")))
              SELECT * FROM
              okera_rewrite_jdbc_test_snowflake__array_test "ARRAY_TEST"
            """),
        ]

        with common.get_planner(ctx) as conn:
            conn.execute_ddl("DROP ATTRIBUTE IF EXISTS snowflake_test.attr")
            conn.execute_ddl("CREATE ATTRIBUTE snowflake_test.attr")
            for policy, query, expected in policies:
                print("\n------------------ Test Case -------------------")
                print("Policy:")
                print(policy)
                print("Query:")
                print(query)
                self._recreate_test_role(conn, 'sf_test_role', ['sf_testuser'])
                conn.execute_ddl(policy)

                result = self.cte(conn, query,
                    user='sf_testuser', client=TAuthorizeQueryClient.SNOWFLAKE)
                self.assert_sql_equals(expected, result)

if __name__ == "__main__":
    unittest.main()


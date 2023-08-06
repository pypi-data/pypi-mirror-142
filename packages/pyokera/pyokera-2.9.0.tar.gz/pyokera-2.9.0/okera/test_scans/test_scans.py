# Copyright 2017 Okera Inc. All Rights Reserved.
#
# Tests that should run on any configuration. The server auth can be specified
# as an environment variables before running this test.
# pylint: disable=bad-continuation,bad-indentation,global-statement,unused-argument
# pylint: disable=no-self-use
import time
import unittest
import json
import numpy

import os
import sys
sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from okera.concurrency import OkeraWorkerException
from okera._thrift_api import TTypeId

from okera.tests import pycerebro_test_common as common
from okera.tests import create_test_data
import cerebro_common as cerebro
from instrumentation import measure_duration

retry_count = 0

class BasicTest(common.TestBase):
    def test_sparse_data(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            df = planner.scan_as_pandas("rs.sparsedata")
            self.assertEqual(96, len(df), msg=df)
            self.assertEqual(68, df['age'].count(), msg=df)
            self.assertEqual(10.0, df['age'].min(), msg=df)
            self.assertEqual(96.0, df['age'].max(), msg=df)
            self.assertEqual(b'sjc', df['defaultcity'].max(), msg=df)
            self.assertEqual(86, df['description'].count(), msg=df)

    def test_nulls(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            df = planner.scan_as_pandas("select string_col from rs.alltypes_null")
            self.assertEqual(1, len(df), msg=df)
            self.assertTrue(numpy.isnan(df['string_col'][0]), msg=df)

            df = planner.scan_as_pandas(
                "select length(string_col) as c from rs.alltypes_null")
            self.assertEqual(1, len(df), msg=df)
            self.assertTrue(numpy.isnan(df['c'][0]), msg=df)

    def test_timestamp_functions(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            json = planner.scan_as_json("""
                select date_add('2009-01-01', 10) as c from okera_sample.sample""")
            self.assertTrue(len(json) == 2, msg=json)
            self.assertEqual('2009-01-11 00:00:00.000', str(json[0]['c']), msg=json)
            self.assertEqual('2009-01-11 00:00:00.000', str(json[1]['c']), msg=json)

    def test_duplicate_cols(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            json = planner.scan_as_json("""
                select record, record from okera_sample.sample""")
            self.assertTrue(len(json) == 2, msg=json)
            self.assertEqual('This is a sample test file.', str(json[0]['record']),
                             msg=json)
            self.assertEqual('This is a sample test file.', str(json[0]['record_2']),
                             msg=json)

        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            json = planner.scan_as_json("""
                select record, record as record_2, record from okera_sample.sample""")
            self.assertTrue(len(json) == 2, msg=json)
            self.assertEqual('This is a sample test file.', str(json[0]['record']),
                             msg=json)
            self.assertEqual('This is a sample test file.', str(json[0]['record_2']),
                             msg=json)
            self.assertEqual('This is a sample test file.', str(json[0]['record_2_2']),
                             msg=json)

    def test_large_decimals(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            json = planner.scan_as_json("select num from rs.large_decimals2")
            self.assertTrue(len(json) == 6, msg=json)
            self.assertEqual('9012248907891233.020304050670',
                             str(json[0]['num']), msg=json)
            self.assertEqual('2343.999900000000', str(json[1]['num']), msg=json)
            self.assertEqual('900.000000000000', str(json[2]['num']), msg=json)
            self.assertEqual('32.440000000000', str(json[3]['num']), msg=json)
            self.assertEqual('54.230000000000', str(json[4]['num']), msg=json)
            self.assertEqual('4525.340000000000', str(json[5]['num']), msg=json)

        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            df = planner.scan_as_pandas("select num from rs.large_decimals2")
            self.assertTrue(len(df) == 6, msg=df)
            self.assertEqual('9012248907891233.020304050670',
                             str(df['num'][0]), msg=df)
            self.assertEqual('2343.999900000000', str(df['num'][1]), msg=df)
            self.assertEqual('900.000000000000', str(df['num'][2]), msg=df)
            self.assertEqual('32.440000000000', str(df['num'][3]), msg=df)
            self.assertEqual('54.230000000000', str(df['num'][4]), msg=df)
            self.assertEqual('4525.340000000000', str(df['num'][5]), msg=df)

    def test_date(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            json = planner.scan_as_json("select * from datedb.date_csv")
            self.assertTrue(len(json) == 2, msg=json)
            self.assertEqual('Robert', str(json[0]['name']), msg=json)
            self.assertEqual(100, json[0]['id'], msg=json)
            self.assertEqual('1980-01-01', str(json[0]['dob']), msg=json)
            self.assertEqual('Michelle', str(json[1]['name']), msg=json)
            self.assertEqual(200, json[1]['id'], msg=json)
            self.assertEqual('1991-12-31', str(json[1]['dob']), msg=json)

        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            pd = planner.scan_as_pandas("select * from datedb.date_csv")
            self.assertTrue(len(pd) == 2, msg=pd)
            self.assertEqual(b'Robert', pd['name'][0], msg=pd)
            self.assertEqual(100, pd['id'][0], msg=pd)
            self.assertEqual('1980-01-01', str(pd['dob'][0]), msg=pd)
            self.assertEqual(b'Michelle', pd['name'][1], msg=pd)
            self.assertEqual(200, pd['id'][1], msg=pd)
            self.assertEqual('1991-12-31', str(pd['dob'][1]), msg=pd)

    def test_scan_as_json_max_records(self):
        sql = "select * from okera_sample.sample"
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            json = planner.scan_as_json(sql, max_records=1, max_client_process_count=1)
            self.assertTrue(len(json) == 1, msg='max_records not respected')
            json = planner.scan_as_json(sql, max_records=100, max_client_process_count=1)
            self.assertTrue(len(json) == 2, msg='max_records not respected')

    def test_scan_as_pandas_max_records(self):
        sql = "select * from okera_sample.sample"
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            pd = planner.scan_as_pandas(sql, max_records=1, max_client_process_count=1)
            self.assertTrue(len(pd.index) == 1, msg='max_records not respected')
            pd = planner.scan_as_pandas(sql, max_records=100, max_client_process_count=1)
            self.assertTrue(len(pd.index) == 2, msg='max_records not respected')

    def test_scan_retry(self):
        global retry_count

        sql = "select * from okera_sample.sample"
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            # First a sanity check
            pd = planner.scan_as_pandas(sql, max_records=1, max_client_process_count=1)
            self.assertTrue(len(pd.index) == 1, msg='test_scan_retry sanity check failed')

            # Patch scan_as_pandas to throw an IOError 2 times
            retry_count = 0
            def test_hook_retry(func_name, retries, attempt):
                if func_name != "plan":
                    return
                global retry_count
                retry_count = retry_count + 1
                if attempt < 2:
                    raise IOError('Fake Error')

            planner.test_hook_retry = test_hook_retry
            pd = planner.scan_as_pandas(sql, max_records=1, max_client_process_count=1)

            assert(retry_count == 3) # count = 2 failures + 1 success
            self.assertTrue(len(pd.index) == 1, msg='Failed to get data with retries')

    def test_worker_retry(self):
        global retry_count

        ctx = common.get_test_context()
        with common.get_worker(ctx) as worker:
            # First a sanity check
            v = worker.get_protocol_version()
            self.assertEqual('1.0', v)

            # Patch get_protocol_version to throw an IOError 2 times
            retry_count = 0
            def test_hook_retry(func_name, retries, attempt):
                if func_name != "get_protocol_version":
                    return
                global retry_count
                retry_count = retry_count + 1
                if attempt < 2:
                    raise IOError('Fake Error')

            worker.test_hook_retry = test_hook_retry
            v = worker.get_protocol_version()

            assert(retry_count == 3) # count = 2 failures + 1 success
            self.assertEqual('1.0', v)

    def test_overwrite_file(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            planner.execute_ddl("DROP TABLE IF EXISTS rs.dim")
            planner.execute_ddl("""CREATE EXTERNAL TABLE rs.dim
                (country_id INT, country_name STRING, country_code STRING)
                ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
                LOCATION 's3://cerebro-datasets/starschema_demo/country_dim/'
                TBLPROPERTIES ('skip.header.line.count'='1')""")

            # Copy one version of the file into the target location
            cerebro.run_shell_cmd('aws s3 cp ' +\
                's3://cerebro-datasets/country_dim_src/country_DIM.csv ' +\
                's3://cerebro-datasets/starschema_demo/country_dim/country_DIM.csv')
            before = planner.scan_as_json('rs.dim')[0]
            self.assertEqual("France", before['country_name'], msg=str(before))

            # Copy another version. This file has the same length but a different
            # character. S3 maintains time in ms timestamp, so sleep a bit.
            time.sleep(1)

            cerebro.run_shell_cmd('aws s3 cp ' +\
                's3://cerebro-datasets/country_dim_src/country_DIM2.csv ' +\
                's3://cerebro-datasets/starschema_demo/country_dim/country_DIM.csv')
            i = 0
            while i < 10:
                after = planner.scan_as_json('rs.dim')[0]
                if 'france' in after['country_name']:
                    return
                self.assertEqual("France", after['country_name'], msg=str(after))
                time.sleep(.1)
                i = i + 1
            self.fail(msg="Did not updated result in time.")

    def test_scan_as_json_newline_delimiters(self):
        sql1 = '''select
         *
        from
        okera_sample.sample'''
        sql2 = '''select
        *
        from
        okera_sample.sample'''
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            json = planner.scan_as_json(sql1, max_records=100, max_client_process_count=1)
            self.assertTrue(
                len(json) == 2,
                msg='could parse query with newline and space delimiters')
            json = planner.scan_as_json(sql2, max_records=100, max_client_process_count=1)
            self.assertTrue(
                len(json) == 2,
                msg='could parse query with newline delimiters')

    def test_scan_as_json_using_with_clause(self):
        sql1 = '''WITH male_customers AS
         (SELECT * FROM okera_sample.users WHERE gender = 'M')
         SELECT * FROM male_customers;'''
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            json = planner.scan_as_json(sql1, max_records=100, max_client_process_count=1)
            self.assertTrue(
                len(json) == 100,
                msg='could parse query that starts with "with"')

    def test_scan_as_json_serialization(self):
        sql = "select * from rs.alltypes"
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            json.loads(json.dumps(planner.scan_as_json(sql)))

    def test_das_6218(self):
        DB = "das_6218"
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            self._recreate_test_db(conn, DB)
            self._create_all_types(conn, DB)

            # Verify schema from catalog, plan and data are all timestamp
            schema = conn.plan('%s.alltypes' % DB).schema
            self.assertEqual(schema.cols[10].type.type_id, TTypeId.TIMESTAMP_NANOS)
            df = conn.scan_as_pandas('SELECT timestamp_col FROM %s.alltypes' % DB)
            self.assertEqual(str(df.dtypes[0]), 'datetime64[ns, UTC]')
            catalog_schema = conn.list_datasets(DB, name='alltypes')[0].schema
            self.assertEqual(
                catalog_schema.cols[10].type.type_id, TTypeId.TIMESTAMP_NANOS)
            print(df)

            # Create a view that is proper with the explicit cast.
            conn.execute_ddl('''
                CREATE VIEW %s.v1(ts STRING)
                AS
                SELECT cast(timestamp_col AS STRING) FROM %s.alltypes''' % (DB, DB))
            # Verify schema from catalog, plan and data are all strings
            catalog_schema = conn.list_datasets(DB, name='v1')[0].schema
            self.assertEqual(catalog_schema.cols[0].type.type_id, TTypeId.STRING)
            schema = conn.plan('%s.v1' % DB).schema
            self.assertEqual(schema.cols[0].type.type_id, TTypeId.STRING)
            df = conn.scan_as_pandas('%s.v1' % DB)
            self.assertEqual(str(df.dtypes[0]), 'object')
            print(df)

            # We want to carefully construct a view that has mismatched types with
            # the view definition. The view just selects a timestamp columns but we
            # will force the catalog type to be string, instead of timestamp.
            # This forces the planner to produce an implicit cast.
            conn.execute_ddl('''
                CREATE EXTERNAL VIEW %s.v2(ts STRING)
                SKIP_ANALYSIS USING VIEW DATA AS
                "SELECT timestamp_col FROM %s.alltypes"''' % (DB, DB))
            # Verify schema from catalog, plan and data are all strings
            catalog_schema = conn.list_datasets(DB, name='v2')[0].schema
            self.assertEqual(catalog_schema.cols[0].type.type_id, TTypeId.STRING)
            schema = conn.plan('%s.v2' % DB).schema
            self.assertEqual(schema.cols[0].type.type_id, TTypeId.STRING)
            df = conn.scan_as_pandas('%s.v2' % DB)
            self.assertEqual(str(df.dtypes[0]), 'object')
            print(df)

    def test_zd_1633(self):
        DB = "zd_1633"
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            self._recreate_test_db(conn, DB)
            conn.execute_ddl('''
                CREATE EXTERNAL TABLE %s.t(
                  s STRING)
                STORED AS TEXTFILE
                LOCATION 's3://cerebrodata-test/zd-1627/'
                ''' % DB)
            res = conn.scan_as_json('%s.t' % DB)
            # Default quote, only 1 row
            self.assertEqual(1, len(res))

            # No quote, should be 2 rows now
            conn.execute_ddl("ALTER TABLE %s.t SET SERDEPROPERTIES('quoteChar'='')" % DB)
            res = conn.scan_as_json('%s.t' % DB)
            self.assertEqual(2, len(res))

            # Recreate using table properties
            conn.execute_ddl('DROP TABLE %s.t' % DB)
            conn.execute_ddl('''
                CREATE EXTERNAL TABLE %s.t(
                  s STRING)
                STORED AS TEXTFILE
                LOCATION 's3://cerebrodata-test/zd-1627/'
                TBLPROPERTIES('okera.text-table.default-quote-char'='')
                ''' % DB)
            res = conn.scan_as_json('%s.t' % DB)
            self.assertEqual(2, len(res))

            # Explicit serde properties overrides table properties
            conn.execute_ddl('''
                ALTER TABLE %s.t SET SERDEPROPERTIES('quoteChar'='"')''' % DB)
            res = conn.scan_as_json('%s.t' % DB)
            self.assertEqual(1, len(res))

            # Table with two cols
            conn.execute_ddl('DROP TABLE %s.t' % DB)
            conn.execute_ddl('''
                CREATE EXTERNAL TABLE %s.t(
                  c1 STRING, c2 STRING)
                STORED AS TEXTFILE
                LOCATION 's3://cerebrodata-test/customers/c1/zd1633_2/'
                TBLPROPERTIES('skip.header.line.count'='1')
                ''' % DB)
            conn.execute_ddl(
                "ALTER TABLE %s.t SET SERDEPROPERTIES('field.delim'=',')" % DB)
            res = conn.scan_as_json('%s.t' % DB)
            self.assertEqual(1, len(res))

            # Remove quote handling
            conn.execute_ddl("ALTER TABLE %s.t SET SERDEPROPERTIES('quoteChar'='')" % DB)
            res = conn.scan_as_json('%s.t' % DB)
            self.assertEqual(2, len(res))
            self.assertEqual('"123', res[1]['c2'])

    def test_scan_delta_dummy_metadata(self):
        DB = "delta_dummy_scan_db"
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            self._recreate_test_db(conn, DB)
            conn.execute_ddl('''
      CREATE EXTERNAL TABLE %s.airline_events_delta (
          col array<string>)
      WITH SERDEPROPERTIES (
          'path'='s3://cerebrodata-test/delta/airlines/airline_events/',
          'serialization.format'='1')
      STORED AS TEXTFILE
      LOCATION 's3://cerebrodata-test/delta/airlines/airline_events/'
      TBLPROPERTIES (
          'totalSize'='66153', 'numRows'='-1', 'rawDataSize'='-1',
          'okera.delta.infer-schema'='true',
          'COLUMN_STATS_ACCURATE'='false',
          'spark.sql.sources.schema.part.0'='{\"type\":\"struct\",\"fields\":[]}',
          'numFiles'='1', 'spark.sql.partitionProvider'='catalog',
          'spark.sql.sources.schema.numParts'='1', 'spark.sql.sources.provider'='delta',
          'spark.sql.create.version'='3.0.1')
                ''' % DB)
            res = conn.scan_as_json('%s.airline_events_delta' % DB)
            self.assertEqual(1326, len(res))

    def test_pandas_index(self):
        ctx = common.get_test_context()
        with common.get_planner(ctx) as planner:
            # We scan a small table but with a tiny min task size, so that it is
            # guaranteed to generate more than one task. We then verify that our
            # overall row indices are correct.
            df = planner.scan_as_pandas("okera_sample.sample", min_task_size=1)

            indices = []
            for i, row in df.iterrows():
                indices.append(i)

            assert len(indices) == 2
            assert indices[0] == 0
            assert indices[1] == 1

    def test_zd1972(self):
        DB = "test_zd1972"
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            self._recreate_test_db(conn, DB)
            conn.execute_ddl('''
            CREATE EXTERNAL TABLE %s.chase_kyc_event_v001 (
              `metadata` STRUCT<event_id:STRING,created_date:BIGINT>,
                `payload` STRUCT<party_key:STRING,customer_type:STRING,cdd:STRUCT<sowFromHighRiskIndustry:ARRAY<STRING>,countriesSignifWealthGen:ARRAY<STRING>,totalAnnualNetIncomeUsd:INT,estTotalNetWorth:INT,isSrcWealthCorroborated:BOOLEAN,srcWealthCorrobPercent:STRING>,spdd:STRUCT<pepHighRisk:BOOLEAN>,add:STRUCT<exceedingCashAggregate:BOOLEAN,exceedingEFTAggregate:BOOLEAN,additionalProdServices:ARRAY<STRING>>,exceptions:ARRAY<STRUCT<exceptionType:STRING>>,risk_profile:STRUCT<riskScore:STRING,risk_level:STRING>>,
                  `previouspayload` STRUCT<party_key:STRING,customer_type:STRING,cdd:STRUCT<sowFromHighRiskIndustry:ARRAY<STRING>,countriesSignifWealthGen:ARRAY<STRING>,totalAnnualNetIncomeUsd:INT,estTotalNetWorth:INT,isSrcWealthCorroborated:BOOLEAN,srcWealthCorrobPercent:STRING>,spdd:STRUCT<pepHighRisk:BOOLEAN>,add:STRUCT<exceedingCashAggregate:BOOLEAN,exceedingEFTAggregate:BOOLEAN,additionalProdServices:ARRAY<STRING>>,exceptions:ARRAY<STRUCT<exceptionType:STRING>>,risk_profile:STRUCT<riskScore:STRING,risk_level:STRING>>
                  )
            STORED AS AVRO
            LOCATION 's3a://cerebro-test-corey.sunwold/avro-testing/repro/dt=2021-02-25'
            TBLPROPERTIES ('avro.schema.url'='s3a://cerebro-test-corey.sunwold/avro/example-schema.json')
            ''' % DB)
            res = conn.scan_as_json('%s.chase_kyc_event_v001' % DB)
            self.assertEqual(1000, len(res))

            # Spot check a few enums
            self.assertEqual('MASS_MARKET', res[10]['previouspayload']['customer_type'])
            self.assertEqual('UNKNOWN', res[100]['previouspayload']['customer_type'])
            self.assertEqual('AFFLUENT', res[500]['previouspayload']['customer_type'])
            self.assertEqual('HIGH_WEALTH', res[900]['previouspayload']['customer_type'])

    def test_zd2001(self):
        DB = "test_zd2001"
        TBL = "bad_enums_1"
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            self._recreate_test_db(conn, DB)
            ###
            # Avro Schema
            # {
            #    "type": "record",
            #    "name": "enums",
            #    "namespace": "enum_testing.avro",
            #    "fields":
            #    [
            #        {
            #            "name": "enum1",
            #            "type":
            #            {
            #                "type": "enum",
            #                "name": "test_enum",
            #                "symbols":
            #                [
            #                    "A",
            #                    "B",
            #                    "UNKNOWN"
            #                ]
            #            },
            #            "doc": "Name",
            #            "default": "UNKNOWN"
            #        }
            #    ]
            #}
            #
            #
            # bad_enums_1.avro contains a single row with a value of 10 which does not
            # map to any known enum value.
            ###
            conn.execute_ddl('''
            CREATE EXTERNAL TABLE %s.%s (
                enum1 STRING
            )
            STORED AS AVRO
            LOCATION "s3://cerebrodata-test/avro_test/enums/bad-enums/bad_enums_1.avro"
            ''' % (DB, TBL))
            with self.assertRaises(OkeraWorkerException) as ex_ctx:
                res = conn.scan_as_json('%s.%s' % (DB, TBL))

            self.assertTrue("Task failed due to an internal error." in str(ex_ctx.exception.error),
                msg=str(ex_ctx))

            # TODO The correct behavior is to deserialize the enum to the default value.
            # This is not implemented yet, and for now we will fail the query if we hit
            # a value we don't recognize. When this is fixed the below two assertions
            # should pass.
            #self.assertEqual(1, len(res))
            #self.assertEqual('UNKNOWN', res[0]['enum1'])

    def test_parquet_minmax_scanner_filter(self):
        db = "parquet_minmax_scanner_filter_db"
        tbl = "parquet_data"
        non_existent_id = 5802904565645645
        existing_id = 580389
        existing_small_int_id = 1
        non_existent_double_id = 2.5
        # we expect these queries to take less than this time
        max_duration = 40
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            create_test_data.create_parquet_table_with_stats(conn, db, tbl)
            # scan with a numeric predicate with the value that does not exist
            # so that we'd have to scan over the whole thing if the optimization
            # is not working.
            m = measure_duration('predicate with non_existent value duration')
            with m:
                res = conn.scan_as_json(
                'select trip_id from %s.%s where trip_id = %s' % (db, tbl, non_existent_id))
            print(m.duration)
            print(res)
            self.assertEqual(0, len(res))
            assert m.duration < max_duration

            m = measure_duration('predicate with existing value duration')
            with m:
                res = conn.scan_as_json(
                'select trip_id from %s.%s where trip_id = %s' % (db, tbl, existing_id))
            print(m.duration)
            print(res)
            self.assertEqual(1, len(res))
            assert m.duration < max_duration

            m = measure_duration('predicate with existing small int value duration')
            with m:
                res = conn.scan_as_json(
                'select trip_id from %s.%s where trip_id = %s' % (db, tbl, existing_small_int_id))
            print(m.duration)
            print(res)
            self.assertEqual(1, len(res))
            assert m.duration < max_duration

            m = measure_duration('predicate with non_existent double value duration')
            with m:
                res = conn.scan_as_json(
                'select trip_id from %s.%s where trip_id = %s' % (db, tbl, non_existent_double_id))
            print(m.duration)
            print(res)
            self.assertEqual(0, len(res))
            assert m.duration < max_duration

    # TODO: pushdown predicates with non-existing values do not have
    # consistent performance.
    @unittest.skip("Perf of predicate pushdown is unpredictable")
    def test_orc_minmax_scanner_filter(self):
        db = "orc_minmax_scanner_filter_db"
        tbl = "orc_data"
        non_existent_id = 5802904565645645
        existing_id = 580389
        existing_small_int_id = 1
        # we expect these queries to take less than 30 seconds
        max_duration = 30
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            create_test_data.create_orc_table_with_stats(conn, db, tbl)
            # scan with a numeric predicate with the value that does not exist
            # so that we'd have to scan over the whole thing if the optimization
            # is not working.

            m = measure_duration('predicate with non_existent value duration')
            with m:
                res = conn.scan_as_json(
                'select trip_id from %s.%s where trip_id = %s' % (db, tbl, non_existent_id))
            print(m.duration)
            print(res)
            self.assertEqual(0, len(res))

            assert m.duration < max_duration

            m = measure_duration('predicate with existing value duration')
            with m:
                res = conn.scan_as_json(
                'select trip_id from %s.%s where trip_id = %s' % (db, tbl, existing_id))
            print(m.duration)
            print(res)
            self.assertEqual(1, len(res))
            assert m.duration < max_duration

            m = measure_duration('predicate with existing small int value duration')
            with m:
                res = conn.scan_as_json(
                'select trip_id from %s.%s where trip_id = %s' % (db, tbl, existing_small_int_id))
            print(m.duration)
            print(res)
            self.assertEqual(1, len(res))
            assert m.duration < max_duration

    @unittest.skip("Need to fix bug. TDD")
    def test_zd1980(self):
        db = "zd_1980"
        ctx = common.get_test_context()
        with common.get_planner(ctx) as conn:
            self._recreate_test_db(conn, db)

            conn.execute_ddl(
'''
CREATE EXTERNAL TABLE %s.chase_fraud_cards_screening_agent_decision_v001 (
  lifecycleid STRING COMMENT 'Unique identifier for a payment',
  decision STRING COMMENT 'The decision made by the agent. The value is configurable, it can be changed later. Actually the possible values are: manually_declined, auto_declined, fraud, manually_approved, auto_approved, genuine.',
  amount DECIMAL(15,2) COMMENT 'Amount, which is always greater than zero',
  currency STRING COMMENT 'Three-letter ISO currency codes eg GBP',
  country STRING COMMENT 'ISO country codes eg UK',
  username STRING COMMENT 'The user who made the decision',
  startedat BIGINT COMMENT 'The time that the decision was requested in UTC',
  finishedat BIGINT COMMENT 'The time that the decision was made in UTC'
)
PARTITIONED BY (dt DATE)
COMMENT 'The card transaction decision made by the agent through the system Feedzai Case Manager'
WITH SERDEPROPERTIES ('avro.schema.url'='s3a://cerebrodata-test/chase/chase.fraud.cards-screening-agent-decision-v001/dt=2021-03-12/chase.fraud.cards-screening-agent-decision-v001+0+0000000000.avro')
STORED AS AVRO
LOCATION 's3a://cerebrodata-test/chase/chase.fraud.cards-screening-agent-decision-v001'
''' % db)
            conn.execute_ddl('ALTER TABLE %s.chase_fraud_cards_screening_agent_decision_v001 RECOVER PARTITIONS' % db)

            conn.execute_ddl('''
CREATE EXTERNAL TABLE %s.event_1 (
  event_id STRING,
  event_type STRING,
  event_name STRING,
  entity_key STRING,
  partition_key STRING,
  checksum STRING,
  created_at BIGINT,
  card_transaction STRUCT<
    transaction_lifecycle_id:STRING,
    card_id:STRING,
    payment_device_details:STRUCT<
      device_id:STRING,
      funding_device_id:STRING,
      logical_card_id:STRING,
      device_type:STRING,
      token_details:STRUCT<
        token_number:STRING>>,
    party_key:STRING,
    state:STRING,
    card_messages:ARRAY<
      STRUCT<
        card_message_id:STRING,
        subscription_key:STRING,
        sequence_number:INT,
        matched_message_id:STRING,
        synthetic_trace_id:STRING,
        message_type:STRING,
        processing_category:STRING,
        pos_entry_mode:STRING,
        processing_code:STRING,
        acquirer_id:STRING,
        retrieval_reference_number:STRING,
        original_currency_amount:STRUCT<
          amount:DECIMAL(17,4),
          currency:STRING>,
        conversion_rate:DECIMAL(14,7),
        amount:STRUCT<
          amount:DECIMAL(17,4),
          currency:STRING>,
        content:STRUCT<
          message_type:STRING,
          primary_account_number:STRING,
          processing_code:STRING,
          processing_code_attributes:STRUCT<
            transaction_type_code:STRING,
            from_account_type_code:STRING,
            to_account_type_code:STRING>,
          system_trace_number:STRING,
          transaction:STRUCT<
            amounts:STRUCT<
              transaction:STRUCT<
                amount:DECIMAL(17,4),
                currency:STRING>,
              settlement:STRUCT<
                amount:DECIMAL(17,4),
                currency:STRING>,
              billing:STRUCT<
                amount:DECIMAL(17,4),
                currency:STRING>,
              fee:STRUCT<
                amount:DECIMAL(17,4),
                currency:STRING>,
              additional_amounts:ARRAY<
                STRUCT<
                  account_type:STRING,
                  amount_type:STRING,
                  transaction_sign:STRING,
                  amount:STRUCT<
                    amount:DECIMAL(17,4),
                    currency:STRING>>>,
            conversion_rate:DECIMAL(14,7)>,
            network_code:STRING,
            banknet_reference_number:STRING,
            dates:STRUCT<
              transaction_date:DATE,
              transaction_time:STRING,
              settlement_date:DATE,
              conversion_date:DATE,
              transmission_date_time:BIGINT>,
            retrieval_reference_number:STRING>,
          card:STRUCT<
            id:STRING,
            expiry_date:STRING>,
          acquirer:STRUCT<
            id:STRING,
            country_code:STRING>,
          merchant:STRUCT<
            name:STRING,
            address:STRUCT<
              city_name:STRING,
              state_or_country_code:STRING>,
            bankcard_phone:STRUCT<
              phone_number_dialed:STRING,
              abbreviation:STRING,
              call_duration:STRING,
              call_origin_city:STRING,
              call_origin_state_or_country_code:STRING>,
            terminal_id:STRING,
            category_code:STRING,
            acceptor_id_code:STRING>,
          pos:STRUCT<
            condition_code:STRING,
            additional_pos_detail:STRING,
            additional_pos_detail_attributes:STRUCT<
              pos_terminal_attendance:INT,
              pos_terminal_location:INT,
              pos_cardholder_presence:STRING,
              pos_card_presence:INT,
              pos_card_capture_capabilities:INT,
              pos_transaction_status:INT,
              pos_transaction_security:INT,
              cardholder_activated_terminal_level:INT,
              pos_card_data_terminal_input_capability_indicator:INT,
              pos_authorisation_life_cycle:INT,
              pos_country_code:STRING,
              pos_postal_code:STRING>,
            pos_entry_mode:STRING,
            pos_entry_mode_attributes:STRUCT<
              pan_entry_mode:STRING,
              pin_entry_mode:STRING>,
            extended_data_condition_codes:STRING>,
          additional_data:STRUCT<
            money_send_ref:STRING,
            multi_purpose_merchant_indicator:STRUCT<
              low_risk_merchant_indicator:STRING>,
            payment_initiation_channel:STRING,
            wallet_program_data:STRING,
            pan_mapping_file_information:STRING,
            trace_id:STRING,
            e_commerce_indicator:STRING,
            on_behalf_of_services:STRING,
            avs_response:STRING>,
          fraud_score_data:STRUCT<
            raw_data:STRING,
            way_4_risk_score:STRING,
            fraud_score:STRING,
            fraud_score_reason_code:STRING,
            rules_score:STRING,
            rules_reason_code_1:STRING,
            rules_reason_code_2:STRING>,
          wallet:STRUCT<
            account_number_indicator:STRING,
            account_number:STRING,
            expiry_date:STRING,
            token_requestor_id:STRING,
            wallet_program_data:STRING>,
          replacement_amounts:STRUCT<
            transaction:DECIMAL(17,4),
            settlement:DECIMAL(17,4),
            billing:DECIMAL(17,4)>,
          authentication:STRUCT<
            threeDS:STRUCT<
              authentication_protocol:STRING,
              directory_server_transaction_id:STRING>,
            ucaf:STRING,
            validationResults:STRUCT<
              cvc2_validation_result:STRING,
              ucaf_validation_result:STRING>,
            integratedCircuitCardData:STRING,
            pinValidation:STRING>,
          decline_reasons:ARRAY<
            STRUCT<
              reason:STRING,
              additional_data:MAP<STRING,STRING>>>,
          auth_code:STRING,
          auth_response_code:STRING,
          original_data_elements:STRUCT<
            message_type:STRING,
            system_trace_number:STRING,
            transmission_date_time:BIGINT,
            acquiring_institution_id:STRING,
            forwarding_institution_id:STRING>,
          paymentDevice:STRUCT<
            fundingDeviceId:STRING>,
          scheme_message_to_reverse_lifecycle_id:STRING,
          stipProcessor:STRING,
          stipIndicator:BOOLEAN,
          metadata:STRUCT<
            received_at:BIGINT>>,
        processing_result:STRUCT<
          response_code:STRING,
          auth_code:STRING,
          approved_amount:STRUCT<
            amount:DECIMAL(17,4),
            currency:STRING>,
          available_balance:STRUCT<
            amount:DECIMAL(17,4),
            currency:STRING>>,
        state:STRING,
        has_impacted_ledger:BOOLEAN,
        payment_device_details:STRUCT<
          device_id:STRING,
          funding_device_id:STRING,
          logical_card_id:STRING,
          device_type:STRING,
          token_details:STRUCT<
            token_number:STRING>>>>,
    ledger_transactions:ARRAY<
      STRUCT<
        ledger_transaction_id:STRING,
        subscription_key:STRING,
        ledger_type:STRING,
        original_currency_amount:STRUCT<
          amount:DECIMAL(17,4),
          currency:STRING>,
        average_conversion_rate:DECIMAL(16,9),
        amount:STRUCT<
          amount:DECIMAL(17,4),
          currency:STRING>,
        sign:STRING,
        state:STRING,
        transaction_code:STRING,
        value_date:BIGINT,
        booking_date:BIGINT,
        correlation_id:STRING>>,
    clearing_message:STRUCT<
      clearing_message_id:STRING,
      cleared_original_currency_amount:STRUCT<
        amount:DECIMAL(17,4),
        currency:STRING>,
        conversion_rate:DECIMAL(16,9),
        cleared_amount:STRUCT<
          amount:DECIMAL(17,4),
          currency:STRING>,
        acquirer_reference_data:STRING,
        content:STRUCT<
          id:STRING,
          transaction_date:STRING,
          retrieval_reference_number:STRING,
          merchant:STRUCT<
            name:STRING,
            address:STRUCT<
              city_name:STRING,
              state_code:STRING,
              country_code:STRING,
              post_code:STRING>,
            terminal_id:STRING,
            category_code:STRING,
            acceptor_id_code:STRING>,
          card:STRUCT<
            id:STRING,
            expiry_date:STRING,
            card_sequence_number:INT,
            primary_account_number:STRING>,
          amounts:STRUCT<
            transaction:STRUCT<
              amount:DECIMAL(17,4),
              currency:STRING>,
            settlement:STRUCT<
              amount:DECIMAL(17,4),
              currency:STRING>,
            billing:STRUCT<
              amount:DECIMAL(17,4),
              currency:STRING>,
            transaction_sign:STRING,
            interchange_fee:STRUCT<
              amount:DECIMAL(17,4),
              currency:STRING>,
            interchange_fee_sign:STRING,
            additional_amounts:ARRAY<
              STRUCT<
                amount_type:STRING,
                amount:STRUCT<
                  amount:DECIMAL(17,4),
                  currency:STRING>>>,
            settlement_conversion_rate:DECIMAL(16,9),
            billing_conversion_rate:DECIMAL(16,9)>,
          authentication_code:STRING,
          mapped_authorisation_processing_code:STRING,
          processing_code:STRING,
          pos:STRUCT<
            message_reason_code:STRING,
            pos_entry_mode:STRING>,
          function_code:INT,
          transaction_lifecycle_id:STRING,
          icc_data:STRING,
          ecommerce_security_level_indicator:STRING,
          mapping_service_account_number:STRING,
          wallet_identifier:STRING,
          data_record:STRING,
          message_number:INT,
          matching_indicator:BOOLEAN,
          file_id:STRING,
          acquirer_reference_data:STRING,
          created_at:BIGINT,
          file_key:STRING,
          row_number:INT,
          paymentDevice:STRUCT<
            fundingDeviceId:STRING>,
            wallet:STRUCT<
              mapping_service_account_number:STRING,
              wallet_identifier:STRING,
              token_requestor_id:STRING>>>,
        version:INT>)
    PARTITIONED BY (dt DATE)
    WITH SERDEPROPERTIES ('avro.schema.url'='s3a://cerebrodata-test/chase/chase.cards.card-transaction-event-v001/dt=2022-01-13/chase.cards.card-transaction-event-v001 34 0000008419.avro')
    STORED AS AVRO
    LOCATION 's3a://cerebrodata-test/chase/chase.cards.card-transaction-event-v001'
    ''' % db)
            conn.execute_ddl('ALTER TABLE %s.event_1 RECOVER PARTITIONS' % db)

            conn.execute_ddl('''
              CREATE VIEW %s.view_event_1 AS
              SELECT ** FROM %s.event_1''' % (db, db))

            conn.execute_ddl('''
CREATE VIEW %s.ren_chase_fraud_card_screening_agent_decision AS
SELECT
  dt seriesDate,
  lifecycleId paymentIdentifier,
  decision cardScreeningAgentDecisionCode,
  amount paymentAmount,
  currency currencyCode,
  country countryCode,
  username cardScreeningAgentDecisionUserName,
  startedAt cardScreeningAgentDecisionCodeStartTimestamp,
  finishedAt cardScreeningAgentDecisionCodeFinishTimestamp
FROM
  %s.chase_fraud_cards_screening_agent_decision_v001''' % (db, db))

            """
            Repro:
            [build]ubuntu@ip-10-1-11-17:~/okera/client/pycerebro/okera/test_scans$ rs-cat "select count(*) from zd_1980.event_1 where dt = cast('2021-01-01' as date)"
            rs-cat: Task failed due to an internal error.
            detail: Failed to parse file schema: Cannot save fixed schema. Schema length: 24687. Filename: s3a://cerebrodata-test/chase/chase.cards.card-transaction-event-v001/dt=2021-01-01/part-00000-886acf8c-2869-4ee0-b608-879d7f24f1bf-c000.avro
            """

if __name__ == "__main__":
    unittest.main()

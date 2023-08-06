# Copyright 2021 Okera Inc. All Rights Reserved.
#
# Test cases, to be run by test_cte.py
#
from inspect import currentframe, getframeinfo

# (file, line, query, result)
V2_PRESTO_TESTS = [
#  (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
#      """
#      SELECT 1
#      """,
#      """
#      SELECT 1
#      """
#  ),
  (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
      """
      SELECT * FROM jdbc_test_snowflake.all_types
      """,
      """
WITH okera_rewrite_jdbc_test_snowflake__all_types AS
  (SELECT "VARCHAR" as "varchar",
          "STRING" as "string",
          "TEXT" as "text",
          "SMALLINT" as "smallint",
          "INT" as "int",
          "BIGINT" as "bigint",
          "INTEGER" as "integer",
          "DOUBLE" as "double",
          "NUMERIC" as "numeric",
          "NUMBER" as "number",
          "DECIMAL" as "decimal",
          "TIMESTAMP" as "timestamp",
          "CHAR" as "char",
          "BOOLEAN" as "boolean",
          "BINARY" as "binary",
          "VARBINARY" as "varbinary",
          "REAL" as "real"
   FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES")
SELECT *
FROM okera_rewrite_jdbc_test_snowflake__all_types "all_types"
      """
  ),
  (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
      """
      SELECT "Date Dim"."d_year" AS "d_year", "Item"."i_brand" AS "i_brand", "Item"."i_brand_id" AS "i_brand_id",
      sum("sf_tpcds_1gb"."store_sales"."ss_ext_sales_price") AS "sum" FROM "sf_tpcds_1gb"."store_sales"
      LEFT JOIN "sf_tpcds_1gb"."date_dim" "Date Dim" ON "sf_tpcds_1gb"."store_sales"."ss_sold_date_sk" = "Date Dim"."d_date_sk"
      LEFT JOIN "sf_tpcds_1gb"."item" "Item" ON "sf_tpcds_1gb"."store_sales"."ss_item_sk" = "Item"."i_item_sk"
      WHERE ("Item"."i_manufact_id" = 128 AND "Date Dim"."d_moy" = 11)
      GROUP BY "Date Dim"."d_year", "Item"."i_brand", "Item"."i_brand_id"
      ORDER BY "Date Dim"."d_year" ASC, "sum" ASC, "Item"."i_brand_id" ASC, "Item"."i_brand" ASC
      """,
      """
WITH okera_rewrite_sf_tpcds_1gb__store_sales AS
  (SELECT "SS_ITEM_SK" as "ss_item_sk",
          "SS_EXT_SALES_PRICE" as "ss_ext_sales_price",
          "SS_SOLD_DATE_SK" as "ss_sold_date_sk"
   FROM "TPCDS_UNPARTITIONED"."TPCDS_001GB"."STORE_SALES"),
     okera_rewrite_sf_tpcds_1gb__date_dim AS
  (SELECT "D_DATE_SK" as "d_date_sk",
          "D_YEAR" as "d_year",
          "D_MOY" as "d_moy"
   FROM "TPCDS_UNPARTITIONED"."TPCDS_001GB"."DATE_DIM"),
     okera_rewrite_sf_tpcds_1gb__item AS
  (SELECT "I_ITEM_SK" as "i_item_sk",
          "I_BRAND_ID" as "i_brand_id",
          "I_BRAND" as "i_brand",
          "I_MANUFACT_ID" as "i_manufact_id"
   FROM "TPCDS_UNPARTITIONED"."TPCDS_001GB"."ITEM")
SELECT "Date Dim"."d_year" "d_year",
       "Item"."i_brand" "i_brand",
       "Item"."i_brand_id" "i_brand_id",
       sum("store_sales"."ss_ext_sales_price") "sum"
FROM ((okera_rewrite_sf_tpcds_1gb__store_sales "store_sales"
       LEFT JOIN okera_rewrite_sf_tpcds_1gb__date_dim "Date Dim" ON ("store_sales"."ss_sold_date_sk" = "Date Dim"."d_date_sk"))
      LEFT JOIN okera_rewrite_sf_tpcds_1gb__item "Item" ON ("store_sales"."ss_item_sk" = "Item"."i_item_sk"))
WHERE (("Item"."i_manufact_id" = 128)
       AND ("Date Dim"."d_moy" = 11))
GROUP BY "Date Dim"."d_year",
         "Item"."i_brand",
         "Item"."i_brand_id"
ORDER BY "Date Dim"."d_year" ASC,
         "sum" ASC,
         "Item"."i_brand_id" ASC,
         "Item"."i_brand" ASC
      """
  ),
  (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
      """
      SELECT "jdbc_test_snowflake"."all_types"."string" AS "String",
      count(distinct "jdbc_test_snowflake"."all_types"."bigint") AS "count"
      FROM "jdbc_test_snowflake"."all_types"
      GROUP BY "jdbc_test_snowflake"."all_types"."string"
      ORDER BY "jdbc_test_snowflake"."all_types"."string" ASC
      """,
      """
      WITH okera_rewrite_jdbc_test_snowflake__all_types AS
        (SELECT "STRING" as "string",
                "BIGINT" as "bigint"
        FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES")
      SELECT "all_types"."string" "String",
            count(DISTINCT "all_types"."bigint") "count"
      FROM okera_rewrite_jdbc_test_snowflake__all_types "all_types"
      GROUP BY "all_types"."string"
      ORDER BY "all_types"."string" ASC
      """
  ),
  (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
      """
      SELECT 1 AS "number_of_records", "all_types"."bigint" AS "BigInt", "all_types"."binary" AS "Binary",
      "all_types"."boolean" AS "Boolean", "all_types"."char" AS "Char", "all_types"."decimal" AS "Decimal",
      "all_types"."double" AS "Double", "all_types"."int" AS "Int", "all_types"."integer" AS "Integer",
      "all_types"."number" AS "Number", "all_types"."numeric" AS "Numeric", "all_types"."real" AS "Real",
      "all_types"."smallint" AS "Smallint", "all_types"."string" AS "String", "all_types"."text" AS "Text",
      "all_types"."timestamp" AS "Timestamp", "all_types"."varbinary" AS "Varbinary", "all_types"."varchar" AS "Varchar"
      FROM "jdbc_test_snowflake"."all_types" "all_types" LIMIT 1000
      """,
      """
      WITH okera_rewrite_jdbc_test_snowflake__all_types AS
        (SELECT "VARCHAR" as "varchar",
                "STRING" as "string",
                "TEXT" as "text",
                "SMALLINT" as "smallint",
                "INT" as "int",
                "BIGINT" as "bigint",
                "INTEGER" as "integer",
                "DOUBLE" as "double",
                "NUMERIC" as "numeric",
                "NUMBER" as "number",
                "DECIMAL" as "decimal",
                "TIMESTAMP" as "timestamp",
                "CHAR" as "char",
                "BOOLEAN" as "boolean",
                "BINARY" as "binary",
                "VARBINARY" as "varbinary",
                "REAL" as "real"
        FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES")
      SELECT 1 "number_of_records",
            "all_types"."bigint" "BigInt",
            "all_types"."binary" "Binary",
            "all_types"."boolean" "Boolean",
            "all_types"."char" "Char",
            "all_types"."decimal" "Decimal",
            "all_types"."double" "Double",
            "all_types"."int" "Int",
            "all_types"."integer" "Integer",
            "all_types"."number" "Number",
            "all_types"."numeric" "Numeric",
            "all_types"."real" "Real",
            "all_types"."smallint" "Smallint",
            "all_types"."string" "String",
            "all_types"."text" "Text",
            "all_types"."timestamp" "Timestamp",
            "all_types"."varbinary" "Varbinary",
            "all_types"."varchar" "Varchar"
      FROM okera_rewrite_jdbc_test_snowflake__all_types "all_types"
      LIMIT 1000
      """
  ),
  #(getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
  #    """
  #    select * from "jdbc_test_snowflake"."all_types" a join "jdbc_test_snowflake"."all_types" b ON a.string = b.string
  #    """,
  #    """
  #    WITH okera_rewrite_jdbc_test_snowflake__all_types AS
  #      (SELECT "VARCHAR" as "varchar",
  #              "STRING" as "string",
  #              "TEXT" as "text",
  #              "SMALLINT" as "smallint",
  #              "INT" as "int",
  #              "BIGINT" as "bigint",
  #              "INTEGER" as "integer",
  #              "DOUBLE" as "double",
  #              "NUMERIC" as "numeric",
  #              "NUMBER" as "number",
  #              "DECIMAL" as "decimal",
  #              "TIMESTAMP" as "timestamp",
  #              "CHAR" as "char",
  #              "BOOLEAN" as "boolean",
  #              "BINARY" as "binary",
  #              "VARBINARY" as "varbinary",
  #              "REAL" as "real"
  #      FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES")
  #    SELECT *
  #    FROM (okera_rewrite_jdbc_test_snowflake__all_types a
  #          INNER JOIN okera_rewrite_jdbc_test_snowflake__all_types b ON (a."string" = b."string"))
  #    """
  #),
  #(getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
  #    """
  #    select * from jdbc_test_snowflake.all_types a join jdbc_test_snowflake.all_types b ON a.string = b.string
  #    """,
  #    """
  #    WITH okera_rewrite_jdbc_test_snowflake__all_types AS
  #      (SELECT "VARCHAR" as "varchar",
  #              "STRING" as "string",
  #              "TEXT" as "text",
  #              "SMALLINT" as "smallint",
  #              "INT" as "int",
  #              "BIGINT" as "bigint",
  #              "INTEGER" as "integer",
  #              "DOUBLE" as "double",
  #              "NUMERIC" as "numeric",
  #              "NUMBER" as "number",
  #              "DECIMAL" as "decimal",
  #              "TIMESTAMP" as "timestamp",
  #              "CHAR" as "char",
  #              "BOOLEAN" as "boolean",
  #              "BINARY" as "binary",
  #              "VARBINARY" as "varbinary",
  #              "REAL" as "real"
  #      FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES")
  #    SELECT *
  #    FROM (okera_rewrite_jdbc_test_snowflake__all_types a
  #          INNER JOIN okera_rewrite_jdbc_test_snowflake__all_types b ON (a."string" = b."string"))
  #    """
  #),
  (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
      """
      SELECT "sf_tpcds_1gb"."customer"."c_birth_year" AS "c_birth_year", count(distinct "sf_tpcds_1gb"."customer"."c_first_name") AS "count"
      FROM "sf_tpcds_1gb"."customer"
      GROUP BY "sf_tpcds_1gb"."customer"."c_birth_year"
      ORDER BY "sf_tpcds_1gb"."customer"."c_birth_year" ASC
      """,
      """
      WITH okera_rewrite_sf_tpcds_1gb__customer AS
        (SELECT "C_FIRST_NAME" as "c_first_name",
                "C_BIRTH_YEAR" as "c_birth_year"
        FROM "TPCDS_UNPARTITIONED"."TPCDS_001GB"."CUSTOMER")
      SELECT "customer"."c_birth_year" "c_birth_year",
            count(DISTINCT "customer"."c_first_name") "count"
      FROM okera_rewrite_sf_tpcds_1gb__customer "customer"
      GROUP BY "customer"."c_birth_year"
      ORDER BY "customer"."c_birth_year" ASC
      """
  ),
  (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
      """
      SELECT  "customer_address"."ca_address_id" "ca_address_id", "customer_address"."ca_address_sk" "ca_address_sk",
      "customer_address"."ca_city" "ca_city", "customer_address"."ca_country" "ca_country", "customer_address"."ca_county" "ca_county",
      "customer_address"."ca_gmt_offset" "ca_gmt_offset", "customer_address"."ca_location_type" "ca_location_type",
      "customer_address"."ca_state" "ca_state", "customer_address"."ca_street_name" "ca_street_name",
      "customer_address"."ca_street_number" "ca_street_number", "customer_address"."ca_street_type" "ca_street_type",
      "customer_address"."ca_suite_number" "ca_suite_number", "customer_address"."ca_zip" "ca_zip", "customer_address"."value" "value"
      FROM "sf_tpcds_1gb"."customer_address"
      """,
      """
      WITH okera_rewrite_sf_tpcds_1gb__customer_address AS
        (SELECT "VALUE" as "value",
                "CA_ADDRESS_SK" as "ca_address_sk",
                "CA_ADDRESS_ID" as "ca_address_id",
                "CA_STREET_NUMBER" as "ca_street_number",
                "CA_STREET_NAME" as "ca_street_name",
                "CA_STREET_TYPE" as "ca_street_type",
                "CA_SUITE_NUMBER" as "ca_suite_number",
                "CA_CITY" as "ca_city",
                "CA_COUNTY" as "ca_county",
                "CA_STATE" as "ca_state",
                "CA_ZIP" as "ca_zip",
                "CA_COUNTRY" as "ca_country",
                "CA_GMT_OFFSET" as "ca_gmt_offset",
                "CA_LOCATION_TYPE" as "ca_location_type"
        FROM "TPCDS_UNPARTITIONED"."TPCDS_001GB"."CUSTOMER_ADDRESS")
      SELECT "customer_address"."ca_address_id" "ca_address_id",
            "customer_address"."ca_address_sk" "ca_address_sk",
            "customer_address"."ca_city" "ca_city",
            "customer_address"."ca_country" "ca_country",
            "customer_address"."ca_county" "ca_county",
            "customer_address"."ca_gmt_offset" "ca_gmt_offset",
            "customer_address"."ca_location_type" "ca_location_type",
            "customer_address"."ca_state" "ca_state",
            "customer_address"."ca_street_name" "ca_street_name",
            "customer_address"."ca_street_number" "ca_street_number",
            "customer_address"."ca_street_type" "ca_street_type",
            "customer_address"."ca_suite_number" "ca_suite_number",
            "customer_address"."ca_zip" "ca_zip",
            "customer_address"."value" "value"
      FROM okera_rewrite_sf_tpcds_1gb__customer_address "customer_address"
      """
  ),
  (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
      """
      SELECT DateDim.d_year                                            AS
              d_year,
              Item.i_brand_id                                            AS
              i_brand_id,
              Item.i_brand                                               AS
              i_brand,
              Sum(store_sales.ss_ext_sales_price) AS sum
      FROM   sf_tpcds_1gb.store_sales
              LEFT JOIN sf_tpcds_1gb.date_dim AS DateDim
                    ON sf_tpcds_1gb.store_sales.ss_sold_date_sk =
                        DateDim.d_date_sk
              LEFT JOIN sf_tpcds_1gb.item Item
                    ON sf_tpcds_1gb.store_sales.ss_item_sk =
                        Item.i_item_sk
      WHERE  ( Item.i_manufact_id = 128
                AND DateDim.d_moy = 11 )
      GROUP  BY DateDim.d_year,
                Item.i_brand_id,
                Item.i_brand
      ORDER  BY DateDim.d_year ASC,
                sum DESC,
                Item.i_brand_id ASC,
                Item.i_brand ASC
      """,
      """
      WITH okera_rewrite_sf_tpcds_1gb__store_sales AS
        (SELECT "SS_ITEM_SK" as "ss_item_sk",
                "SS_EXT_SALES_PRICE" as "ss_ext_sales_price",
                "SS_SOLD_DATE_SK" as "ss_sold_date_sk"
        FROM "TPCDS_UNPARTITIONED"."TPCDS_001GB"."STORE_SALES"),
          okera_rewrite_sf_tpcds_1gb__date_dim AS
        (SELECT "D_DATE_SK" as "d_date_sk",
                "D_YEAR" as "d_year",
                "D_MOY" as "d_moy"
        FROM "TPCDS_UNPARTITIONED"."TPCDS_001GB"."DATE_DIM"),
          okera_rewrite_sf_tpcds_1gb__item AS
        (SELECT "I_ITEM_SK" as "i_item_sk",
                "I_BRAND_ID" as "i_brand_id",
                "I_BRAND" as "i_brand",
                "I_MANUFACT_ID" as "i_manufact_id"
        FROM "TPCDS_UNPARTITIONED"."TPCDS_001GB"."ITEM")
      SELECT DateDim.d_year d_year,
            Item.i_brand_id i_brand_id,
            Item.i_brand i_brand,
            Sum(store_sales.ss_ext_sales_price) sum
      FROM ((okera_rewrite_sf_tpcds_1gb__store_sales "store_sales"
            LEFT JOIN okera_rewrite_sf_tpcds_1gb__date_dim DateDim ON (store_sales.ss_sold_date_sk = DateDim.d_date_sk))
            LEFT JOIN okera_rewrite_sf_tpcds_1gb__item Item ON (store_sales.ss_item_sk = Item.i_item_sk))
      WHERE ((Item.i_manufact_id = 128)
            AND (DateDim.d_moy = 11))
      GROUP BY DateDim.d_year,
              Item.i_brand_id,
              Item.i_brand
      ORDER BY DateDim.d_year ASC,
              sum DESC, Item.i_brand_id ASC,
                        Item.i_brand ASC
      """
  ),
#  (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
#      """
#      select count(a.varchar), a.bigint from "jdbc_test_snowflake"."all_types" a join "jdbc_test_snowflake"."all_types" b ON a.string = b.string
#      group by b.bigint
#      """,
#      """
#      WITH okera_rewrite_jdbc_test_snowflake__all_types AS (SELECT
#      "VARCHAR" as "varchar",
#      "STRING" as "string",
#      "BIGINT" as "bigint"
#      FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES")
#      SELECT  "count"("a"."varchar"), "bigint"
#      FROM
#        (okera_rewrite_jdbc_test_snowflake__all_types "a"
#      INNER JOIN okera_rewrite_jdbc_test_snowflake__all_types "b" ON ("a"."string" = "b"."string"))
#      GROUP BY "b"."bigint"
#      """
#  ),
  (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
      """
      SELECT DATE_FORMAT(all_types2.date, '%Y-%m-%d') as "all_types2.date" FROM jdbc_test_snowflake.all_types2
      """,
      """
      WITH okera_rewrite_jdbc_test_snowflake__all_types2 AS
        (SELECT "DATE" as "date"
        FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES2")
      SELECT "TO_VARCHAR"(all_types2.date,
                          '%Y-%m-%d') "all_types2.date"
      FROM okera_rewrite_jdbc_test_snowflake__all_types2 "all_types2"
      """
  ),
  (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
      """
      with date_test as (
            select decimal, from_unixtime(1582985586) as x from jdbc_test_snowflake.all_types2
          )
          select
            current_date as c1, current_time  as c2, current_timestamp as c3,
            DATE(x) as c4,
            localtime as c5, now() as c6,
            to_unixtime(x) as c7, date_trunc('year', x) as c8, date_add('month', 2, x) as c9, date_diff('day', x, from_unixtime(1583995586)) as c10,
            date_format(x, 'YYYY-MM-DD') as c11, date_parse('2020-02-29 12:05:30', 'YYYY-MM-DD HH:mi:ss') as c12, extract(year FROM x) as c13,
            format_datetime(x, 'YYYY-MM-DD') as c14, parse_datetime('2020-02-29', 'YYYY-MM-DD') as c15, day(x) as c16, day_of_month(x) as c17,
            day_of_week(x) as c18, day_of_year(x) as c19, dow(x) as c20, doy(x) as c21, hour(x) as c22, minute(x) as c23, month(x) as c24,
            quarter(x) as c25, second(x) as c26, week(x) as c27, week_of_year(x) as c28, year(x) as c29, year_of_week(x) as c30, yow(x) as c31
          from date_test
          limit 1
      """,
      """
WITH okera_rewrite_jdbc_test_snowflake__all_types2 AS (SELECT "DECIMAL" as "decimal", "DATE" as "date" FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES2") , date_test AS ( SELECT decimal , "TO_TIMESTAMP"(1582985586) x FROM okera_rewrite_jdbc_test_snowflake__all_types2 "all_types2" ) SELECT current_date c1, current_time c2, current_timestamp c3, DATE(x) c4, localtime c5, "CURRENT_TIMESTAMP"() c6, "DATE_PART"('EPOCH_MILLISECOND', "TO_TIMESTAMP"(x)) c7, date_trunc('year', x) c8, "DATEADD"('month', 2, x) c9, "DATEDIFF"('day', x, "TO_TIMESTAMP"(1583995586)) c10, "TO_VARCHAR"(x, 'YYYY-MM-DD') c11, "TO_TIMESTAMP"('2020-02-29 12:05:30', 'YYYY-MM-DD HH:mi:ss') c12, EXTRACT(YEAR FROM x) c13, "TO_VARCHAR"(x, 'YYYY-MM-DD') c14, "TO_TIMESTAMP_TZ"('2020-02-29', 'YYYY-MM-DD') c15, day(x) c16, "DAYOFMONTH"(x) c17, "DAYOFWEEK"(x) c18, "DAYOFYEAR"(x) c19, "DAYOFWEEK"(x) c20, "DAYOFYEAR"(x) c21, hour(x) c22, minute(x) c23, month(x) c24, quarter(x) c25, second(x) c26, week(x) c27, "WEEKOFYEAR"(x) c28, year(x) c29, "YEAROFWEEK"(x) c30, "YEAROFWEEK"(x) c31 FROM date_test date_test LIMIT 1
      """
  ),
#  (getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno,
#      """
#      select count(a.*), bigint from "jdbc_test_snowflake"."all_types" a join "jdbc_test_snowflake"."all_types" b ON a.string = b.string
#      """,
#      """
#      WITH okera_rewrite_jdbc_test_snowflake__all_types AS (SELECT
#      "VARCHAR" as "varchar",
#      "STRING" as "string",
#      "BIGINT" as "bigint"
#      FROM "DEMO_DB"."JDBC_TEST"."ALL_TYPES")
#      SELECT  "count"("a"."varchar"), "bigint"
#      FROM
#        (okera_rewrite_jdbc_test_snowflake__all_types "a"
#      INNER JOIN okera_rewrite_jdbc_test_snowflake__all_types "b" ON ("a"."string" = "b"."string"))
#      GROUP BY "b"."bigint"
#      """
#  ),
]

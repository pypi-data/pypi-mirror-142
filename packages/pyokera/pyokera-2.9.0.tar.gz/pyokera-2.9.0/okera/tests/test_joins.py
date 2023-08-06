# Copyright Okera Inc. All Rights Reserved.

import unittest

import time
from okera.tests import pycerebro_test_common as common

class JoinsTest(common.TestBase):
    @unittest.skip("This test takes a really long time to run")
    def test_join_mem(self):
        ctx = common.get_test_context()
        DB = 'joins_mem_test_db'
        with common.get_planner(ctx) as conn:
            self._recreate_test_db(conn, DB)


            conn.execute_ddl(
            """
            CREATE EXTERNAL TABLE IF NOT EXISTS %s.chase_cards_card_transaction_event_v001 (
              event_id STRING,
              event_type STRING,
              event_name STRING,
              entity_key STRING,
              partition_key STRING,
              checksum STRING,
              created_at BIGINT,
              card_transaction STRUCT<transaction_lifecycle_id:STRING,card_id:STRING,payment_device_details:STRUCT<device_id:STRING,funding_device_id:STRING,logical_card_id:STRING,device_type:STRING,token_details:STRUCT<token_number:STRING>>,party_key:STRING,state:STRING,card_messages:ARRAY<STRUCT<card_message_id:STRING,subscription_key:STRING,sequence_number:INT,matched_message_id:STRING,synthetic_trace_id:STRING,message_type:STRING,processing_category:STRING,pos_entry_mode:STRING,processing_code:STRING,acquirer_id:STRING,retrieval_reference_number:STRING,original_currency_amount:STRUCT<amount:DECIMAL(17,4),currency:STRING>,conversion_rate:DECIMAL(14,7),amount:STRUCT<amount:DECIMAL(17,4),currency:STRING>,content:STRUCT<message_type:STRING,primary_account_number:STRING,processing_code:STRING,processing_code_attributes:STRUCT<transaction_type_code:STRING,from_account_type_code:STRING,to_account_type_code:STRING>,system_trace_number:STRING,transaction:STRUCT<amounts:STRUCT<transaction:STRUCT<amount:DECIMAL(17,4),currency:STRING>,settlement:STRUCT<amount:DECIMAL(17,4),currency:STRING>,billing:STRUCT<amount:DECIMAL(17,4),currency:STRING>,fee:STRUCT<amount:DECIMAL(17,4),currency:STRING>,additional_amounts:ARRAY<STRUCT<account_type:STRING,amount_type:STRING,transaction_sign:STRING,amount:STRUCT<amount:DECIMAL(17,4),currency:STRING>>>,conversion_rate:DECIMAL(14,7)>,network_code:STRING,banknet_reference_number:STRING,dates:STRUCT<transaction_date:DATE,transaction_time:STRING,settlement_date:DATE,conversion_date:DATE,transmission_date_time:BIGINT>,retrieval_reference_number:STRING>,card:STRUCT<id:STRING,expiry_date:STRING>,acquirer:STRUCT<id:STRING,country_code:STRING>,merchant:STRUCT<name:STRING,address:STRUCT<city_name:STRING,state_or_country_code:STRING>,bankcard_phone:STRUCT<phone_number_dialed:STRING,abbreviation:STRING,call_duration:STRING,call_origin_city:STRING,call_origin_state_or_country_code:STRING>,terminal_id:STRING,category_code:STRING,acceptor_id_code:STRING>,pos:STRUCT<condition_code:STRING,additional_pos_detail:STRING,additional_pos_detail_attributes:STRUCT<pos_terminal_attendance:INT,pos_terminal_location:INT,pos_cardholder_presence:STRING,pos_card_presence:INT,pos_card_capture_capabilities:INT,pos_transaction_status:INT,pos_transaction_security:INT,cardholder_activated_terminal_level:INT,pos_card_data_terminal_input_capability_indicator:INT,pos_authorisation_life_cycle:INT,pos_country_code:STRING,pos_postal_code:STRING>,pos_entry_mode:STRING,pos_entry_mode_attributes:STRUCT<pan_entry_mode:STRING,pin_entry_mode:STRING>,extended_data_condition_codes:STRING>,additional_data:STRUCT<money_send_ref:STRING,multi_purpose_merchant_indicator:STRUCT<low_risk_merchant_indicator:STRING>,payment_initiation_channel:STRING,wallet_program_data:STRING,pan_mapping_file_information:STRING,trace_id:STRING,e_commerce_indicator:STRING,on_behalf_of_services:STRING,avs_response:STRING>,fraud_score_data:STRUCT<raw_data:STRING,way_4_risk_score:STRING,fraud_score:STRING,fraud_score_reason_code:STRING,rules_score:STRING,rules_reason_code_1:STRING,rules_reason_code_2:STRING>,wallet:STRUCT<account_number_indicator:STRING,account_number:STRING,expiry_date:STRING,token_requestor_id:STRING,wallet_program_data:STRING>,replacement_amounts:STRUCT<transaction:DECIMAL(17,4),settlement:DECIMAL(17,4),billing:DECIMAL(17,4)>,authentication:STRUCT<threeDS:STRUCT<authentication_protocol:STRING,directory_server_transaction_id:STRING>,ucaf:STRING,validationResults:STRUCT<cvc2_validation_result:STRING,ucaf_validation_result:STRING>,integratedCircuitCardData:STRING,pinValidation:STRING>,decline_reasons:ARRAY<STRUCT<reason:STRING,additional_data:MAP<STRING,STRING>>>,auth_code:STRING,auth_response_code:STRING,original_data_elements:STRUCT<message_type:STRING,system_trace_number:STRING,transmission_date_time:BIGINT,acquiring_institution_id:STRING,forwarding_institution_id:STRING>,paymentDevice:STRUCT<fundingDeviceId:STRING>,scheme_message_to_reverse_lifecycle_id:STRING,stipProcessor:STRING,stipIndicator:BOOLEAN,metadata:STRUCT<received_at:BIGINT>>,processing_result:STRUCT<response_code:STRING,auth_code:STRING,approved_amount:STRUCT<amount:DECIMAL(17,4),currency:STRING>,available_balance:STRUCT<amount:DECIMAL(17,4),currency:STRING>>,state:STRING,has_impacted_ledger:BOOLEAN,payment_device_details:STRUCT<device_id:STRING,funding_device_id:STRING,logical_card_id:STRING,device_type:STRING,token_details:STRUCT<token_number:STRING>>>>,ledger_transactions:ARRAY<STRUCT<ledger_transaction_id:STRING,subscription_key:STRING,ledger_type:STRING,original_currency_amount:STRUCT<amount:DECIMAL(17,4),currency:STRING>,average_conversion_rate:DECIMAL(16,9),amount:STRUCT<amount:DECIMAL(17,4),currency:STRING>,sign:STRING,state:STRING,transaction_code:STRING,value_date:BIGINT,booking_date:BIGINT,correlation_id:STRING>>,clearing_message:STRUCT<clearing_message_id:STRING,cleared_original_currency_amount:STRUCT<amount:DECIMAL(17,4),currency:STRING>,conversion_rate:DECIMAL(16,9),cleared_amount:STRUCT<amount:DECIMAL(17,4),currency:STRING>,acquirer_reference_data:STRING,content:STRUCT<id:STRING,transaction_date:STRING,retrieval_reference_number:STRING,merchant:STRUCT<name:STRING,address:STRUCT<city_name:STRING,state_code:STRING,country_code:STRING,post_code:STRING>,terminal_id:STRING,category_code:STRING,acceptor_id_code:STRING>,card:STRUCT<id:STRING,expiry_date:STRING,card_sequence_number:INT,primary_account_number:STRING>,amounts:STRUCT<transaction:STRUCT<amount:DECIMAL(17,4),currency:STRING>,settlement:STRUCT<amount:DECIMAL(17,4),currency:STRING>,billing:STRUCT<amount:DECIMAL(17,4),currency:STRING>,transaction_sign:STRING,interchange_fee:STRUCT<amount:DECIMAL(17,4),currency:STRING>,interchange_fee_sign:STRING,additional_amounts:ARRAY<STRUCT<amount_type:STRING,amount:STRUCT<amount:DECIMAL(17,4),currency:STRING>>>,settlement_conversion_rate:DECIMAL(16,9),billing_conversion_rate:DECIMAL(16,9)>,authentication_code:STRING,mapped_authorisation_processing_code:STRING,processing_code:STRING,pos:STRUCT<message_reason_code:STRING,pos_entry_mode:STRING>,function_code:INT,transaction_lifecycle_id:STRING,icc_data:STRING,ecommerce_security_level_indicator:STRING,mapping_service_account_number:STRING,wallet_identifier:STRING,data_record:STRING,message_number:INT,matching_indicator:BOOLEAN,file_id:STRING,acquirer_reference_data:STRING,created_at:BIGINT,file_key:STRING,row_number:INT,paymentDevice:STRUCT<fundingDeviceId:STRING>,wallet:STRUCT<mapping_service_account_number:STRING,wallet_identifier:STRING,token_requestor_id:STRING>>>,version:INT>
                          )
            PARTITIONED BY (
              dt DATE
              )
            COMMENT 'Discovered by Okera crawler'
            WITH SERDEPROPERTIES ('avro.schema.url'='s3a://cerebrodata-test/chase/chase.cards.card-transaction-event-v001/dt=2022-01-13/chase.cards.card-transaction-event-v001 34 0000008419.avro')
            STORED AS AVRO
            LOCATION 's3a://cerebrodata-test/chase/chase.cards.card-transaction-event-v001'
            TBLPROPERTIES ('okera.view.children'='chase_payments_view.chase_cards_card_transaction_event_view')
            """ % DB)

            conn.execute_ddl("""
                ALTER TABLE %s.chase_cards_card_transaction_event_v001 RECOVER PARTITIONS
            """ % DB)

            result = conn.scan_as_json("""
              select * from %s.chase_cards_card_transaction_event_v001
                  t, t.card_transaction.card_messages m
              WHERE m.item.content.wallet.wallet_program_data = '103'""" % DB,
              max_task_count=1)
            print(result)

            result = conn.scan_as_json("""
              select * from %s.chase_cards_card_transaction_event_v001
                  t, t.card_transaction.card_messages m""" % DB, max_task_count=1)
            print(result)

    @unittest.skip("This test requires --fast-sasl-timeout to start the cluster")
    def test_client_sleep(self):
        ctx = common.get_test_context(auth_mech='TOKEN')
        DB = 'joins_mem_test_db'
        with common.get_planner(ctx) as conn:
            print('Creating db...')
            self._recreate_test_db(conn, DB)
            print('Sleeping...')
            time.sleep(30)
            print('Creating db...')
            self._recreate_test_db(conn, DB)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3

import os
import sys

import configargparse

from okera import context
from okera import policy_sync
from okera.tests import pycerebro_test_common as common
from okera._thrift_api import TAuthorizeQueryClient, TGetDatasetsParams

ROOT_TOKEN = os.environ['OKERA_HOME'] + '/integration/tokens/cerebro.token'
NIGHTLY_PLANNER = 'nightly.internal.okera.rocks'

parser = configargparse.ArgParser()
parser.add("--table", dest="table", default=None,
            help="[db].[table] to generate policy sync for")
parser.add("--users", dest="users", default=None,
            help="Comma separated list of users to generate policy sync for.")

parser.add("--single-role", dest="single_role", default=None,
            help="Name of the role that should be used for all users.")
parser.add("--per-user-role", dest="per_user_role_grants", default=False,
            help="Grant to a per user role.")

parser.add("--nightly", dest="nightly", default=False,
            help="If true, connect to nightly (vs local).")
options = parser.parse_args()

def error(msg):
  print("error: " + msg)
  sys.exit(1)

def get_conn():
    if bool(options.nightly):
        ctx = context()
        ctx.enable_token_auth(token_file=ROOT_TOKEN)
        return ctx.connect(NIGHTLY_PLANNER)
    else:
        ctx = common.get_test_context()
        return common.get_planner(ctx)

if __name__ == "__main__":
    if options.table is None:
        error("Must specify table.")
    if len(options.table.split('.')) != 2:
        error("Table must be [db].[table]")
    if options.users is None:
        error("Must specify users.")

    users = []
    for u in options.users.split(','):
        users.append(u.strip())
    db = options.table.split('.')[0]
    tbl = options.table.split('.')[1]

    with get_conn() as conn:
        request = TGetDatasetsParams()
        request.dataset_names = ['{}.{}'.format(db_name, tbl_name)]
        request.with_schema = True
        okera_tbl = planner_conn.service.client.GetDatasets(request).datasets[0]
        grants, pre_alters, row_filters, column_policies, post_alters, _ = \
            policy_sync.generate_policies(
            conn, users, db, tbl, okera_tbl,
            single_grant_role=options.single_role,
            per_user_role_grants=bool(options.per_user_role_grants))
        policy_sync.debug_print(grants, pre_alters, row_filters, column_policies, post_alters)

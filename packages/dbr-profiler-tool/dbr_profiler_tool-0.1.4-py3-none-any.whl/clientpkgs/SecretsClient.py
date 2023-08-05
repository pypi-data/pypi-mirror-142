import os
import time
from timeit import default_timer as timer
import base64
import logging
from core import logging_utils
from core import wmconstants
from core.dbclient import dbclient


class SecretsClient(dbclient):

    def get_secret_scopes_list(self):
        scopes_list = self.get('/secrets/scopes/list').get('scopes', [])
        return scopes_list

    def get_secrets(self, scope_name):
        secrets_list = self.get('/secrets/list', {'scope': scope_name}).get('secrets', [])
        return secrets_list

    def get_secret_value(self, scope_name, secret_key, cid):
        ec_id = self.get_execution_context(cid)
        cmd_set_value = f"value = dbutils.secrets.get(scope = '{scope_name}', key = '{secret_key}')"
        cmd_convert_b64 = "import base64; b64_value = base64.b64encode(value.encode('ascii'))"
        cmd_get_b64 = "print(str(b64_value.decode('ascii')))"   # b64_value.decode('ascii')
        results_set = self.submit_command(cid, ec_id, cmd_set_value)
        results_convert = self.submit_command(cid, ec_id, cmd_convert_b64)
        results_get = self.submit_command(cid, ec_id, cmd_get_b64)
        val = results_get.get('data')
        print(val)
        b64_value_decode = base64.b64decode(val).decode('ascii')
        return b64_value_decode

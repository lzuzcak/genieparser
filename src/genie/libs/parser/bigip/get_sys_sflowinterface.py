# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/sflow/data-source/interface' resources
# =============================================


class SysSflowInterfaceSchema(MetaParser):

    schema = {}


class SysSflowInterface(SysSflowInterfaceSchema):
    """ To F5 resource for /mgmt/tm/sys/sflow/data-source/interface
    """

    cli_command = "/mgmt/tm/sys/sflow/data-source/interface"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

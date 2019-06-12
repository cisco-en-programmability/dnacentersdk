# -*- coding: utf-8 -*-
"""DNA Center Start discovery data model.

Copyright (c) 2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
from dnacentersdk.exceptions import MalformedRequest

from builtins import *

class JSONSchemaValidator55B439Dc4239B140(object):
    """Start discovery request schema definition."""
    def __init__(self):
        # print("created 55b4-39dc-4239-b140")
        super(JSONSchemaValidator55B439Dc4239B140, self).__init__()
        self._validator = fastjsonschema.compile( {'type': 'object', 'properties': {'cdpLevel': {'type': 'number'}, 'discoveryType': {'type': 'string'}, 'enablePasswordList': {'type': 'array', 'items': {'type': 'string'}}, 'globalCredentialIdList': {'type': 'array', 'items': {'type': 'string'}}, 'httpReadCredential': {'type': 'object', 'properties': {'comments': {'type': 'string'}, 'credentialType': {'type': 'string', 'enum': ['GLOBAL', 'APP']}, 'description': {'type': 'string'}, 'id': {'type': 'string'}, 'instanceTenantId': {'type': 'string'}, 'instanceUuid': {'type': 'string'}, 'password': {'type': 'string'}, 'port': {'type': 'number'}, 'secure': {'type': 'boolean'}, 'username': {'type': 'string'}}}, 'httpWriteCredential': {'type': 'object', 'properties': {'comments': {'type': 'string'}, 'credentialType': {'type': 'string', 'enum': ['GLOBAL', 'APP']}, 'description': {'type': 'string'}, 'id': {'type': 'string'}, 'instanceTenantId': {'type': 'string'}, 'instanceUuid': {'type': 'string'}, 'password': {'type': 'string'}, 'port': {'type': 'number'}, 'secure': {'type': 'boolean'}, 'username': {'type': 'string'}}}, 'ipAddressList': {'type': 'string'}, 'ipFilterList': {'type': 'array', 'items': {'type': 'string'}}, 'lldpLevel': {'type': 'number'}, 'name': {'type': 'string'}, 'netconfPort': {'type': 'string'}, 'noAddNewDevice': {'type': 'boolean'}, 'parentDiscoveryId': {'type': 'string'}, 'passwordList': {'type': 'array', 'items': {'type': 'string'}}, 'preferredMgmtIPMethod': {'type': 'string'}, 'protocolOrder': {'type': 'string'}, 'reDiscovery': {'type': 'boolean'}, 'retry': {'type': 'number'}, 'snmpAuthPassphrase': {'type': 'string'}, 'snmpAuthProtocol': {'type': 'string'}, 'snmpMode': {'type': 'string'}, 'snmpPrivPassphrase': {'type': 'string'}, 'snmpPrivProtocol': {'type': 'string'}, 'snmpROCommunity': {'type': 'string'}, 'snmpROCommunityDesc': {'type': 'string'}, 'snmpRWCommunity': {'type': 'string'}, 'snmpRWCommunityDesc': {'type': 'string'}, 'snmpUserName': {'type': 'string'}, 'snmpVersion': {'type': 'string'}, 'timeout': {'type': 'number'}, 'updateMgmtIp': {'type': 'boolean'}, 'userNameList': {'type': 'array', 'items': {'type': 'string'}}}} )

    def validate(self, request):
        try:
            self._validator(request)
            return True
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(request, e.message))
            return False
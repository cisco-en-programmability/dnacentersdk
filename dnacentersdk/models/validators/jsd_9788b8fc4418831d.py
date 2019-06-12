# -*- coding: utf-8 -*-
"""DNA Center Updates an existing discovery by specified Id data model.

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

class JSONSchemaValidator9788B8Fc4418831D(object):
    """Updates an existing discovery by specified Id request schema definition."""
    def __init__(self):
        # print("created 9788-b8fc-4418-831d")
        super(JSONSchemaValidator9788B8Fc4418831D, self).__init__()
        self._validator = fastjsonschema.compile( {'type': 'object', 'properties': {'attributeInfo': {'type': 'object', 'properties': {}}, 'cdpLevel': {'type': 'number'}, 'deviceIds': {'type': 'string'}, 'discoveryCondition': {'type': 'string'}, 'discoveryStatus': {'type': 'string'}, 'discoveryType': {'type': 'string'}, 'enablePasswordList': {'type': 'string'}, 'globalCredentialIdList': {'type': 'array', 'items': {'type': 'string'}}, 'httpReadCredential': {'type': 'object', 'properties': {'comments': {'type': 'string'}, 'credentialType': {'type': 'string', 'enum': ['GLOBAL', 'APP']}, 'description': {'type': 'string'}, 'id': {'type': 'string'}, 'instanceTenantId': {'type': 'string'}, 'instanceUuid': {'type': 'string'}, 'password': {'type': 'string'}, 'port': {'type': 'number'}, 'secure': {'type': 'boolean'}, 'username': {'type': 'string'}}}, 'httpWriteCredential': {'type': 'object', 'properties': {'comments': {'type': 'string'}, 'credentialType': {'type': 'string', 'enum': ['GLOBAL', 'APP']}, 'description': {'type': 'string'}, 'id': {'type': 'string'}, 'instanceTenantId': {'type': 'string'}, 'instanceUuid': {'type': 'string'}, 'password': {'type': 'string'}, 'port': {'type': 'number'}, 'secure': {'type': 'boolean'}, 'username': {'type': 'string'}}}, 'id': {'type': 'string'}, 'ipAddressList': {'type': 'string'}, 'ipFilterList': {'type': 'string'}, 'isAutoCdp': {'type': 'boolean'}, 'lldpLevel': {'type': 'number'}, 'name': {'type': 'string'}, 'netconfPort': {'type': 'string'}, 'numDevices': {'type': 'number'}, 'parentDiscoveryId': {'type': 'string'}, 'passwordList': {'type': 'string'}, 'preferredMgmtIPMethod': {'type': 'string'}, 'protocolOrder': {'type': 'string'}, 'retryCount': {'type': 'number'}, 'snmpAuthPassphrase': {'type': 'string'}, 'snmpAuthProtocol': {'type': 'string'}, 'snmpMode': {'type': 'string'}, 'snmpPrivPassphrase': {'type': 'string'}, 'snmpPrivProtocol': {'type': 'string'}, 'snmpRoCommunity': {'type': 'string'}, 'snmpRoCommunityDesc': {'type': 'string'}, 'snmpRwCommunity': {'type': 'string'}, 'snmpRwCommunityDesc': {'type': 'string'}, 'snmpUserName': {'type': 'string'}, 'timeOut': {'type': 'number'}, 'updateMgmtIp': {'type': 'boolean'}, 'userNameList': {'type': 'string'}}} )

    def validate(self, request):
        try:
            self._validator(request)
            return True
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(request, e.message))
            return False
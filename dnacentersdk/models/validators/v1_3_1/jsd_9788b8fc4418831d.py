# -*- coding: utf-8 -*-
"""Cisco DNA Center Updates discovery by Id data model.

Copyright (c) 2019-2021 Cisco Systems.

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
import json
from dnacentersdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidator9788B8Fc4418831D(object):
    """Updates discovery by Id request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator9788B8Fc4418831D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "attributeInfo": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "cdpLevel": {
                "type": [
                "number",
                "null"
                ]
                },
                "deviceIds": {
                "type": [
                "string",
                "null"
                ]
                },
                "discoveryCondition": {
                "type": [
                "string",
                "null"
                ]
                },
                "discoveryStatus": {
                "type": [
                "string"
                ]
                },
                "discoveryType": {
                "type": [
                "string",
                "null"
                ]
                },
                "enablePasswordList": {
                "type": [
                "string",
                "null"
                ]
                },
                "globalCredentialIdList": {
                "items": {
                "type": [
                "string",
                "null",
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "httpReadCredential": {
                "properties": {
                "comments": {
                "type": [
                "string",
                "null"
                ]
                },
                "credentialType": {
                "enum": [
                "GLOBAL",
                "APP",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "description":
                 {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "type": [
                "string",
                "null"
                ]
                },
                "password": {
                "type": [
                "string",
                "null"
                ]
                },
                "port": {
                "type": [
                "number",
                "null"
                ]
                },
                "secure": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "username": {
                "type": [
                "string",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "httpWriteCredential": {
                "properties": {
                "comments": {
                "type": [
                "string",
                "null"
                ]
                },
                "credentialType": {
                "enum": [
                "GLOBAL",
                "APP",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "description":
                 {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "type": [
                "string",
                "null"
                ]
                },
                "password": {
                "type": [
                "string",
                "null"
                ]
                },
                "port": {
                "type": [
                "number",
                "null"
                ]
                },
                "secure": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "username": {
                "type": [
                "string",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "id": {
                "type": [
                "string"
                ]
                },
                "ipAddressList": {
                "type": [
                "string",
                "null"
                ]
                },
                "ipFilterList": {
                "type": [
                "string",
                "null"
                ]
                },
                "isAutoCdp": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "lldpLevel": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "netconfPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "numDevices": {
                "type": [
                "number",
                "null"
                ]
                },
                "parentDiscoveryId": {
                "type": [
                "string",
                "null"
                ]
                },
                "passwordList": {
                "type": [
                "string",
                "null"
                ]
                },
                "preferredMgmtIPMethod": {
                "type": [
                "string",
                "null"
                ]
                },
                "protocolOrder": {
                "type": [
                "string",
                "null"
                ]
                },
                "retryCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "snmpAuthPassphrase": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpAuthProtocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpMode": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpPrivPassphrase": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpPrivProtocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpRoCommunity": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpRoCommunityDesc": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpRwCommunity": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpRwCommunityDesc": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpUserName": {
                "type": [
                "string",
                "null"
                ]
                },
                "timeOut": {
                "type": [
                "number",
                "null"
                ]
                },
                "updateMgmtIp": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "userNameList": {
                "type": [
                "string",
                "null"
                ]
                }
                },
                "required": [
                "discoveryStatus",
                "id"
                ],
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )

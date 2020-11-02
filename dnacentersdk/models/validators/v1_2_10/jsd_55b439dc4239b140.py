# -*- coding: utf-8 -*-
"""DNA Center Start discovery data model.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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


class JSONSchemaValidator55B439Dc4239B140(object):
    """Start discovery request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator55B439Dc4239B140, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "cdpLevel": {
                "type": [
                "number",
                "null"
                ]
                },
                "discoveryType": {
                "description":
                 "",
                "type": [
                "string"
                ]
                },
                "enablePasswordList": {
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "credentialType": {
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "password": {
                "description":
                 "",
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
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "credentialType": {
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "password": {
                "description":
                 "",
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
                "description":
                 "",
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
                "ipAddressList": {
                "description":
                 "",
                "type": [
                "string"
                ]
                },
                "ipFilterList": {
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
                "lldpLevel": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string"
                ]
                },
                "netconfPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "noAddNewDevice": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "parentDiscoveryId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "passwordList": {
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
                "preferredMgmtIPMethod": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "protocolOrder": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "reDiscovery": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "retry": {
                "type": [
                "number",
                "null"
                ]
                },
                "snmpAuthPassphrase": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpAuthProtocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpMode": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpPrivPassphrase": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpPrivProtocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpROCommunity": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpROCommunityDesc": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpRWCommunity": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpRWCommunityDesc": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpUserName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpVersion": {
                "description":
                 "",
                "type": [
                "string"
                ]
                },
                "timeout": {
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
                }
                },
                "required": [
                "discoveryType",
                "ipAddressList",
                "name",
                "snmpVersion"
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

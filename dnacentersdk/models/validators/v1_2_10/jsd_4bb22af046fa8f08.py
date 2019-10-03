# -*- coding: utf-8 -*-
"""DNA Center Add Device data model.

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
import json
from dnacentersdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidator4Bb22Af046Fa8F08(object):
    """Add Device request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator4Bb22Af046Fa8F08, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "cliTransport": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "computeDevice": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "enablePassword": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "extendedDiscoveryInfo": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "httpPassword": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "httpPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "httpSecure": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "httpUserName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ipAddress": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "merakiOrgId": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
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
                "password": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "serialNumber": {
                "description":
                 "",
                "type": [
                "string",
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
                "snmpRWCommunity": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpRetry": {
                "type": [
                "number",
                "null"
                ]
                },
                "snmpTimeout": {
                "type": [
                "number",
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
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                 "",
                "enum": [
                "COMPUTE_DEVICE",
                "MERAKI_DASHBOARD",
                "NETWORK_DEVICE",
                "NODATACHANGE",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "updateMgmtIPaddressList": {
                "description":
                 "",
                "items": {
                "properties": {
                "existMgmtIpAddress": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "newMgmtIpAddress": {
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
                "type": [
                "array",
                "null"
                ]
                },
                "userName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                }
                },
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

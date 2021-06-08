# -*- coding: utf-8 -*-
"""Cisco DNA Center Add Device data model.

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


class JSONSchemaValidator4Bb22Af046Fa8F08(object):
    """Add Device request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator4Bb22Af046Fa8F08, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "cliTransport": {
                "type": [
                "string"
                ]
                },
                "computeDevice": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "enablePassword": {
                "type": [
                "string"
                ]
                },
                "extendedDiscoveryInfo": {
                "type": [
                "string",
                "null"
                ]
                },
                "httpPassword": {
                "type": [
                "string",
                "null"
                ]
                },
                "httpPort": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "ipAddress": {
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array"
                ]
                },
                "merakiOrgId": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "password": {
                "type": [
                "string"
                ]
                },
                "serialNumber": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpAuthPassphrase": {
                "type": [
                "string"
                ]
                },
                "snmpAuthProtocol": {
                "type": [
                "string"
                ]
                },
                "snmpMode": {
                "type": [
                "string"
                ]
                },
                "snmpPrivPassphrase": {
                "type": [
                "string"
                ]
                },
                "snmpPrivProtocol": {
                "type": [
                "string"
                ]
                },
                "snmpROCommunity": {
                "type": [
                "string"
                ]
                },
                "snmpRWCommunity": {
                "type": [
                "string"
                ]
                },
                "snmpRetry": {
                "type": [
                "number"
                ]
                },
                "snmpTimeout": {
                "type": [
                "number"
                ]
                },
                "snmpUserName": {
                "type": [
                "string"
                ]
                },
                "snmpVersion": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
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
                "items": {
                "properties": {
                "existMgmtIpAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "newMgmtIpAddress": {
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
                "type": [
                "string"
                ]
                }
                },
                "required": [
                "cliTransport",
                "enablePassword",
                "ipAddress",
                "password",
                "snmpAuthPassphrase",
                "snmpAuthProtocol",
                "snmpMode",
                "snmpPrivPassphrase",
                "snmpPrivProtocol",
                "snmpROCommunity",
                "snmpRWCommunity",
                "snmpRetry",
                "snmpTimeout",
                "snmpUserName",
                "userName"
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

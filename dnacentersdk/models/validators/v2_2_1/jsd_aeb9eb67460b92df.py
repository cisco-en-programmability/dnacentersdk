# -*- coding: utf-8 -*-
"""DNA Center Sync Devices data model.

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


class JSONSchemaValidatorAeb9Eb67460B92Df(object):
    """Sync Devices request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorAeb9Eb67460B92Df, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "cliTransport": {
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string"
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
                "string"
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
                "string"
                ]
                },
                "snmpAuthProtocol": {
                "description":
                 "",
                "type": [
                "string"
                ]
                },
                "snmpMode": {
                "description":
                 "",
                "type": [
                "string"
                ]
                },
                "snmpPrivPassphrase": {
                "description":
                 "",
                "type": [
                "string"
                ]
                },
                "snmpPrivProtocol": {
                "description":
                 "",
                "type": [
                "string"
                ]
                },
                "snmpROCommunity": {
                "description":
                 "",
                "type": [
                "string"
                ]
                },
                "snmpRWCommunity": {
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string"
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

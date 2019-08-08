# -*- coding: utf-8 -*-
"""DNA Center Sync Devices data model.

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
                "type": "string"
                },
                "computeDevice": {
                "type": "boolean"
                },
                "enablePassword": {
                "description":
                 "",
                "type": "string"
                },
                "extendedDiscoveryInfo": {
                "description":
                 "",
                "type": "string"
                },
                "httpPassword": {
                "description":
                 "",
                "type": "string"
                },
                "httpPort": {
                "description":
                 "",
                "type": "string"
                },
                "httpSecure": {
                "type": "boolean"
                },
                "httpUserName": {
                "description":
                 "",
                "type": "string"
                },
                "ipAddress": {
                "description":
                 "",
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "merakiOrgId": {
                "description":
                 "",
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "netconfPort": {
                "description":
                 "",
                "type": "string"
                },
                "password": {
                "description":
                 "",
                "type": "string"
                },
                "serialNumber": {
                "description":
                 "",
                "type": "string"
                },
                "snmpAuthPassphrase": {
                "description":
                 "",
                "type": "string"
                },
                "snmpAuthProtocol": {
                "description":
                 "",
                "type": "string"
                },
                "snmpMode": {
                "description":
                 "",
                "type": "string"
                },
                "snmpPrivPassphrase": {
                "description":
                 "",
                "type": "string"
                },
                "snmpPrivProtocol": {
                "description":
                 "",
                "type": "string"
                },
                "snmpROCommunity": {
                "description":
                 "",
                "type": "string"
                },
                "snmpRWCommunity": {
                "description":
                 "",
                "type": "string"
                },
                "snmpRetry": {
                "type": "number"
                },
                "snmpTimeout": {
                "type": "number"
                },
                "snmpUserName": {
                "description":
                 "",
                "type": "string"
                },
                "snmpVersion": {
                "description":
                 "",
                "type": "string"
                },
                "type": {
                "description":
                 "",
                "enum": [
                "COMPUTE_DEVICE",
                "MERAKI_DASHBOARD",
                "NETWORK_DEVICE",
                "NODATACHANGE"
                ],
                "type": "string"
                },
                "updateMgmtIPaddressList": {
                "description":
                 "",
                "items": {
                "properties": {
                "existMgmtIpAddress": {
                "description":
                 "",
                "type": "string"
                },
                "newMgmtIpAddress": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "userName": {
                "description":
                 "",
                "type": "string"
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

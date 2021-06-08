# -*- coding: utf-8 -*-
"""Cisco DNA Center Create and Provision SSID data model.

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


class JSONSchemaValidatorDb9F997F4E59Aec1(object):
    """Create and Provision SSID request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorDb9F997F4E59Aec1, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "enableFabric": {
                "type": [
                "boolean"
                ]
                },
                "flexConnect": {
                "properties": {
                "enableFlexConnect": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "localToVlan": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "managedAPLocations": {
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
                "ssidDetails": {
                "properties": {
                "enableBroadcastSSID": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "enableFastLane": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "enableMACFiltering": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "fastTransition": {
                "enum": [
                "Adaptive",
                "Enable",
                "Disable",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "passphrase": {
                "type": [
                "string",
                "null"
                ]
                },
                "radioPolicy": {
                "enum": [
                "Dual band operation (2.4GHz and 5GHz)",
                "Dual band operation with band select",
                "5GHz only",
                "2.4GHz only",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "securityLevel": {
                "enum": [
                "WPA2_ENTERPRISE",
                "WPA2_PERSONAL",
                "OPEN",
                "WEB_AUTH",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "trafficType": {
                "enum": [
                "data",
                "voicedata",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "webAuthURL": {
                "type": [
                "string",
                "null"
                ]
                }
                },
                "type": [
                "object"
                ]
                },
                "ssidType": {
                "enum": [
                "Guest",
                "Enterprise",
                null
                ],
                "type": [
                "string"
                ]
                },
                "vlanAndDynamicInterfaceDetails": {
                "properties": {
                "managedAPLocation": {
                "properties": {
                "interfaceGateway": {
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceIPAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceNetmaskInCIDR": {
                "type": [
                "number",
                "null"
                ]
                },
                "lagOrPortNumber": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "vlanId": {
                "type": [
                "number",
                "null"
                ]
                },
                "vlanName": {
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
                }
                },
                "required": [
                "managedAPLocations",
                "ssidDetails",
                "ssidType",
                "enableFabric"
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

# -*- coding: utf-8 -*-
"""DNA Center Create and Provision SSID data model.

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

class JSONSchemaValidatorDb9F997F4E59Aec1(object):
    """Create and Provision SSID request schema definition."""
    def __init__(self):
        # print("created db9f-997f-4e59-aec1")
        super(JSONSchemaValidatorDb9F997F4E59Aec1, self).__init__()
        self._validator = fastjsonschema.compile( {'type': 'object', 'properties': {'managedAPLocations': {'type': 'array', 'items': {'type': 'string'}}, 'ssidDetails': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'securityLevel': {'type': 'string', 'enum': ['WPA2_ENTERPRISE', 'WPA2_PERSONAL', 'OPEN', 'WEB_AUTH']}, 'enableFastLane': {'type': 'boolean'}, 'passphrase': {'type': 'string'}, 'trafficType': {'type': 'string', 'enum': ['data', 'voicedata']}, 'enableBroadcastSSID': {'type': 'boolean'}, 'radioPolicy': {'type': 'string', 'enum': ['Dual band operation (2.4GHz and 5GHz)', 'Dual band operation with band select', '5GHz only', '2.4GHz only']}, 'enableMACFiltering': {'type': 'boolean'}, 'fastTransition': {'type': 'string', 'enum': ['Adaptive', 'Enable', 'Disable']}, 'webAuthURL': {'type': 'string'}}}, 'ssidType': {'type': 'string', 'enum': ['Guest', 'Enterprise']}, 'enableFabric': {'type': 'boolean'}, 'flexConnect': {'type': 'object', 'properties': {'enableFlexConnect': {'type': 'boolean'}, 'localToVlan': {'type': 'number'}}}, 'vlanAndDynamicInterfaceDetails': {'type': 'object', 'properties': {'managedAPLocation': {'type': 'object', 'properties': {'interfaceIPAddress': {'type': 'string'}, 'interfaceNetmaskInCIDR': {'type': 'number'}, 'interfaceGateway': {'type': 'string'}, 'lagOrPortNumber': {'type': 'number'}}}, 'vlanId': {'type': 'number'}, 'vlanName': {'type': 'string'}}}}} )

    def validate(self, request):
        try:
            self._validator(request)
            return True
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(request, e.message))
            return False
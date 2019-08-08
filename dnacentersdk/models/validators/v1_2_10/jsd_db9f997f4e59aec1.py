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
                "type": "boolean"
                },
                "flexConnect": {
                "description":
                "Flex Connect - Applicable for non fabric profile",
                "properties": {
                "enableFlexConnect": {
                "type": "boolean"
                },
                "localToVlan": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "managedAPLocations": {
                "description":
                "Managed AP Locations (Enter entire Site(s)
                 hierarchy)",
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "ssidDetails": {
                "description":
                "SsidDetails",
                "properties": {
                "enableBroadcastSSID": {
                "type": "boolean"
                },
                "enableFastLane": {
                "type": "boolean"
                },
                "enableMACFiltering": {
                "type": "boolean"
                },
                "fastTransition": {
                "description":
                "Fast Transition",
                "enum": [
                "Adaptive",
                "Enable",
                "Disable"
                ],
                "type": "string"
                },
                "name": {
                "description":
                "Name",
                "type": "string"
                },
                "passphrase": {
                "description":
                "Pass Phrase ( Only applicable for SSID with
                 PERSONAL auth type )",
                "type": "string"
                },
                "radioPolicy": {
                "description":
                "Radio Policy",
                "enum": [
                "Dual band operation (2.4GHz and 5GHz)",
                "Dual band operation with band select",
                "5GHz only",
                "2.4GHz only"
                ],
                "type": "string"
                },
                "securityLevel": {
                "description":
                "Security Level(For guest SSID OPEN/WEB_AUTH, For
                 Enterprise SSID ENTERPRISE/PERSONAL/OPEN)",
                "enum": [
                "WPA2_ENTERPRISE",
                "WPA2_PERSONAL",
                "OPEN",
                "WEB_AUTH"
                ],
                "type": "string"
                },
                "trafficType": {
                "description":
                "Traffic Type",
                "enum": [
                "data",
                "voicedata"
                ],
                "type": "string"
                },
                "webAuthURL": {
                "description":
                "Web Auth URL",
                "type": "string"
                }
                },
                "type": "object"
                },
                "ssidType": {
                "description":
                "SSID Type",
                "enum": [
                "Guest",
                "Enterprise"
                ],
                "type": "string"
                },
                "vlanAndDynamicInterfaceDetails": {
                "description":
                "VLAN And Dynamic Interface Details",
                "properties": {
                "managedAPLocation": {
                "description":
                "Managed AP Location",
                "properties": {
                "interfaceGateway": {
                "description":
                "Interface Gateway",
                "type": "string"
                },
                "interfaceIPAddress": {
                "description":
                "Interface IP Address",
                "type": "string"
                },
                "interfaceNetmaskInCIDR": {
                "type": "number"
                },
                "lagOrPortNumber": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "vlanId": {
                "type": "number"
                },
                "vlanName": {
                "description":
                "VLAN Name",
                "type": "string"
                }
                },
                "type": "object"
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

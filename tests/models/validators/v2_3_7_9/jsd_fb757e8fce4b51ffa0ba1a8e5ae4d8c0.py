# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetEnterpriseSSIDV1 data model.

Copyright (c) 2024 Cisco Systems.

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



import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorFb757E8FCe4B51FfA0Ba1A8E5Ae4D8C0(object):
    """GetEnterpriseSSIDV1 request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorFb757E8FCe4B51FfA0Ba1A8E5Ae4D8C0, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "groupUuid": {
                "type": "string"
                },
                "inheritedGroupName": {
                "type": "string"
                },
                "inheritedGroupUuid": {
                "type": "string"
                },
                "instanceUuid": {
                "type": "string"
                },
                "ssidDetails": {
                "items": {
                "properties": {
                "aaaOverride": {
                "type": "boolean"
                },
                "authServer": {
                "type": "string"
                },
                "basicServiceSetClientIdleTimeout": {
                "type": "number"
                },
                "clientExclusionTimeout": {
                "type": "number"
                },
                "clientRateLimit": {
                "type": "number"
                },
                "coverageHoleDetectionEnable": {
                "type": "boolean"
                },
                "enableBasicServiceSetMaxIdle": {
                "type": "boolean"
                },
                "enableBroadcastSSID": {
                "type": "boolean"
                },
                "enableClientExclusion": {
                "type": "boolean"
                },
                "enableDirectedMulticastService": {
                "type": "boolean"
                },
                "enableFastLane": {
                "type": "boolean"
                },
                "enableMACFiltering": {
                "type": "boolean"
                },
                "enableNeighborList": {
                "type": "boolean"
                },
                "enableSessionTimeOut": {
                "type": "boolean"
                },
                "fastTransition": {
                "type": "string"
                },
                "isEnabled": {
                "type": "boolean"
                },
                "isFabric": {
                "type": "boolean"
                },
                "mfpClientProtection": {
                "type": "string"
                },
                "multiPSKSettings": {
                "items": {
                "properties": {
                "passphrase": {
                "type": "string"
                },
                "passphraseType": {
                "enum": [
                "ASCII",
                "HEX"
                ],
                "type": "string"
                },
                "priority": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "name": {
                "type": "string"
                },
                "nasOptions": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "passphrase": {
                "type": "string"
                },
                "protectedManagementFrame": {
                "enum": [
                "Optional",
                "Disabled",
                "Required"
                ],
                "type": "string"
                },
                "radioPolicy": {
                "type": "string"
                },
                "securityLevel": {
                "type": "string"
                },
                "sessionTimeOut": {
                "type": "number"
                },
                "trafficType": {
                "type": "string"
                },
                "wlanType": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "version": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )

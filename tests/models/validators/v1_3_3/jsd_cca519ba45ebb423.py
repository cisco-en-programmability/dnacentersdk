# -*- coding: utf-8 -*-
"""DNA Center Get Enterprise SSID data model.

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


class JSONSchemaValidatorCca519Ba45EbB423(object):
    """Get Enterprise SSID request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorCca519Ba45EbB423, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "items": {
                "properties": {
                "groupUuid": {
                "description":
                "Group Uuid",
                "type": [
                "string",
                "null"
                ]
                },
                "inheritedGroupName": {
                "description":
                "Inherited Group Name",
                "type": [
                "string",
                "null"
                ]
                },
                "inheritedGroupUuid": {
                "description":
                "Inherited Group Uuid",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "description":
                "Instance Uuid",
                "type": [
                "string",
                "null"
                ]
                },
                "ssidDetails": {
                "description":
                "SSID Details",
                "items": {
                "properties": {
                "authServer": {
                "description":
                "Auth Server",
                "type": [
                "string",
                "null"
                ]
                },
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
                "description":
                "Fast Transition",
                "type": [
                "string",
                "null"
                ]
                },
                "isEnabled": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "isFabric": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "passphrase": {
                "description":
                "Passphrase",
                "type": [
                "string",
                "null"
                ]
                },
                "radioPolicy": {
                "description":
                "Radio Policy",
                "type": [
                "string",
                "null"
                ]
                },
                "securityLevel": {
                "description":
                "Security Level",
                "type": [
                "string",
                "null"
                ]
                },
                "trafficType": {
                "description":
                "Traffic Type",
                "type": [
                "string",
                "null"
                ]
                },
                "wlanType": {
                "description":
                "Wlan Type",
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
                "version": {
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

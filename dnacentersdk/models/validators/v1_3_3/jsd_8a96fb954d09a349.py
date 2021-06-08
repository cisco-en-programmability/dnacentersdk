# -*- coding: utf-8 -*-
"""Cisco DNA Center Create Enterprise SSID data model.

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


class JSONSchemaValidator8A96Fb954D09A349(object):
    """Create Enterprise SSID request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator8A96Fb954D09A349, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
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
                "maxLength": 32,
                "type": [
                "string"
                ]
                },
                "passphrase": {
                "maxLength": 63,
                "minLength": 8,
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
                null
                ],
                "type": [
                "string"
                ]
                },
                "trafficType": {
                "enum": [
                "voicedata",
                "data",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                }
                },
                "required": [
                "name",
                "securityLevel"
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

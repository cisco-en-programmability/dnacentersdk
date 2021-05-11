# -*- coding: utf-8 -*-
"""DNA Center Create sensor test template data model.

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


class JSONSchemaValidator08Bd88834A68A2E6(object):
    """Create sensor test template request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator08Bd88834A68A2E6, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "apCoverage": {
                "description":
                "Ap Coverage",
                "items": {
                "properties": {
                "bands": {
                "description":
                "Bands",
                "type": [
                "string",
                "null"
                ]
                },
                "numberOfApsToTest": {
                "description":
                "Number Of Aps To Test",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "rssiThreshold": {
                "description":
                "Rssi Threshold",
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
                "connection": {
                "description":
                "Connection",
                "type": [
                "string",
                "null"
                ]
                },
                "modelVersion": {
                "type": [
                "number",
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
                "ssids": {
                "description":
                "Ssids",
                "items": {
                "properties": {
                "authType": {
                "description":
                "Auth Type",
                "type": [
                "string",
                "null"
                ]
                },
                "categories": {
                "description":
                "Categories",
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
                "profileName": {
                "description":
                "Profile Name",
                "type": [
                "string",
                "null"
                ]
                },
                "psk": {
                "description":
                "Psk",
                "type": [
                "string",
                "null"
                ]
                },
                "qosPolicy": {
                "description":
                "Qos Policy",
                "type": [
                "string",
                "null"
                ]
                },
                "ssid": {
                "description":
                "Ssid",
                "type": [
                "string",
                "null"
                ]
                },
                "tests": {
                "description":
                "Tests",
                "items": {
                "properties": {
                "config": {
                "description":
                "Config",
                "items": {},
                "type": [
                "array",
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
                "thirdParty": {
                "description":
                "Third Party",
                "properties": {
                "selected": {
                "type": [
                "boolean",
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
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
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

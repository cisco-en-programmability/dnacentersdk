# -*- coding: utf-8 -*-
"""Cisco DNA Center Create sensor test template data model.

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


class JSONSchemaValidator08Bd88834A68A2E6(object):
    """Create sensor test template request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator08Bd88834A68A2E6, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "apCoverage": {
                "items": {
                "properties": {
                "bands": {
                "type": [
                "string",
                "null"
                ]
                },
                "numberOfApsToTest": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "rssiThreshold": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "ssids": {
                "items": {
                "properties": {
                "authType": {
                "type": [
                "string",
                "null"
                ]
                },
                "categories": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "psk": {
                "type": [
                "string",
                "null"
                ]
                },
                "qosPolicy": {
                "type": [
                "string",
                "null"
                ]
                },
                "ssid": {
                "type": [
                "string",
                "null"
                ]
                },
                "tests": {
                "items": {
                "properties": {
                "config": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "name": {
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

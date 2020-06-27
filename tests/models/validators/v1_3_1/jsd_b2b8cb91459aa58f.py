# -*- coding: utf-8 -*-
"""DNA Center Get Physical Topology data model.

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


class JSONSchemaValidatorB2B8Cb91459AA58F(object):
    """Get Physical Topology request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorB2B8Cb91459AA58F, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "description":
                 "",
                "properties": {
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "links": {
                "description":
                 "",
                "items": {
                "properties": {
                "additionalInfo": {
                "description":
                 "",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "endPortID": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "endPortIpv4Address": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "endPortIpv4Mask": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "endPortName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "endPortSpeed": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "greyOut": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "linkStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "source": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "startPortID": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "startPortIpv4Address": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "startPortIpv4Mask": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "startPortName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "startPortSpeed": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "tag": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "target": {
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
                "nodes": {
                "description":
                 "",
                "items": {
                "properties": {
                "aclApplied": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "additionalInfo": {
                "description":
                 "",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "customParam": {
                "description":
                 "",
                "properties": {
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "label": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "parentNodeId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "x": {
                "type": [
                "number",
                "null"
                ]
                },
                "y": {
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
                "dataPathId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "deviceType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "family": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "fixed": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "greyOut": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ip": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "label": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "networkType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "nodeType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "order": {
                "type": [
                "number",
                "null"
                ]
                },
                "osType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "platformId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "role": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "roleSource": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "tags": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null",
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "upperNode": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "userId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vlanId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "x": {
                "type": [
                "number",
                "null"
                ]
                },
                "y": {
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
                "type": [
                "array",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "version": {
                "description":
                 "",
                "type": [
                "string",
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

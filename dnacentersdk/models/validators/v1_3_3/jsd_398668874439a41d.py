# -*- coding: utf-8 -*-
"""Cisco DNA Center Edit Application data model.

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


class JSONSchemaValidator398668874439A41D(object):
    """Edit Application request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator398668874439A41D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "items": {
                "properties": {
                "applicationSet": {
                "properties": {
                "idRef": {
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
                "id": {
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
                "networkApplications": {
                "items": {
                "properties": {
                "appProtocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "applicationSubType": {
                "type": [
                "string",
                "null"
                ]
                },
                "applicationType": {
                "type": [
                "string",
                "null"
                ]
                },
                "categoryId": {
                "type": [
                "string",
                "null"
                ]
                },
                "displayName": {
                "type": [
                "string",
                "null"
                ]
                },
                "dscp": {
                "type": [
                "string",
                "null"
                ]
                },
                "engineId": {
                "type": [
                "string",
                "null"
                ]
                },
                "helpString": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "ignoreConflict": {
                "type": [
                "string",
                "null"
                ]
                },
                "longDescription": {
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
                "popularity": {
                "type": [
                "string",
                "null"
                ]
                },
                "rank": {
                "type": [
                "string",
                "null"
                ]
                },
                "serverName": {
                "type": [
                "string",
                "null"
                ]
                },
                "trafficClass": {
                "type": [
                "string",
                "null"
                ]
                },
                "url": {
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
                "networkIdentity": {
                "items": {
                "properties": {
                "displayName": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "lowerPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "ports": {
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "upperPort": {
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

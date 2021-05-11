# -*- coding: utf-8 -*-
"""DNA Center Edit Application data model.

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


class JSONSchemaValidator398668874439A41D(object):
    """Edit Application request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator398668874439A41D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "items": {
                "properties": {
                "applicationSet": {
                "description":
                "Application Set",
                "properties": {
                "idRef": {
                "description":
                "Id Ref",
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
                "description":
                "Id",
                "type": [
                "string",
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
                "networkApplications": {
                "description":
                "Network Applications",
                "items": {
                "properties": {
                "appProtocol": {
                "description":
                "App Protocol",
                "type": [
                "string",
                "null"
                ]
                },
                "applicationSubType": {
                "description":
                "Application Sub Type",
                "type": [
                "string",
                "null"
                ]
                },
                "applicationType": {
                "description":
                "Application Type",
                "type": [
                "string",
                "null"
                ]
                },
                "categoryId": {
                "description":
                "Category Id",
                "type": [
                "string",
                "null"
                ]
                },
                "displayName": {
                "description":
                "Display Name",
                "type": [
                "string",
                "null"
                ]
                },
                "dscp": {
                "description":
                "Dscp",
                "type": [
                "string",
                "null"
                ]
                },
                "engineId": {
                "description":
                "Engine Id",
                "type": [
                "string",
                "null"
                ]
                },
                "helpString": {
                "description":
                "Help String",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "ignoreConflict": {
                "description":
                "Ignore Conflict",
                "type": [
                "string",
                "null"
                ]
                },
                "longDescription": {
                "description":
                "Long Description",
                "type": [
                "string",
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
                "popularity": {
                "description":
                "Popularity",
                "type": [
                "string",
                "null"
                ]
                },
                "rank": {
                "description":
                "Rank",
                "type": [
                "string",
                "null"
                ]
                },
                "serverName": {
                "description":
                "Server Name",
                "type": [
                "string",
                "null"
                ]
                },
                "trafficClass": {
                "description":
                "Traffic Class",
                "type": [
                "string",
                "null"
                ]
                },
                "url": {
                "description":
                "Url",
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
                "description":
                "Network Identity",
                "items": {
                "properties": {
                "displayName": {
                "description":
                "Display Name",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "lowerPort": {
                "description":
                "Lower Port",
                "type": [
                "string",
                "null"
                ]
                },
                "ports": {
                "description":
                "Ports",
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                "Protocol",
                "type": [
                "string",
                "null"
                ]
                },
                "upperPort": {
                "description":
                "Upper Port",
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

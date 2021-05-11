# -*- coding: utf-8 -*-
"""DNA Center Create or Schedule a report data model.

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


class JSONSchemaValidator8Abf291A42Aa8860(object):
    """Create or Schedule a report request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator8Abf291A42Aa8860, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "deliveries": {
                "description":
                "Array of available delivery channels",
                "items": {},
                "type": [
                "array"
                ]
                },
                "name": {
                "description":
                "report name",
                "type": [
                "string"
                ]
                },
                "schedule": {
                "description":
                 "",
                "type": [
                "string"
                ]
                },
                "tags": {
                "description":
                "array of tags for report",
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
                "view": {
                "properties": {
                "fieldGroups": {
                "description":
                "Fields selected for specific type of reports(CSV,
                 TDE, JSON)",
                "items": {
                "properties": {
                "fieldGroupDisplayName": {
                "description":
                "Field group label/displayname for user",
                "type": [
                "string",
                "null"
                ]
                },
                "fieldGroupName": {
                "description":
                "Field group name",
                "type": [
                "string",
                "null"
                ]
                },
                "fields": {
                "description":
                "fields selected in the fieldgroup",
                "items": {
                "properties": {
                "displayName": {
                "description":
                "field label/displayname",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "field name",
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
                "type": [
                "array",
                "null"
                ]
                },
                "filters": {
                "items": {
                "properties": {
                "displayName": {
                "description":
                "filter label/displayname",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "filter name",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                "filter type",
                "type": [
                "string",
                "null"
                ]
                },
                "value": {
                "type": [
                "number"
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
                "format": {
                "description":
                "Details of selected format for the report",
                "properties": {
                "formatType": {
                "description":
                "format type of report",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "format name of report",
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
                "name": {
                "description":
                "view name",
                "type": [
                "string",
                "null"
                ]
                },
                "viewId": {
                "description":
                "view Id",
                "type": [
                "string",
                "null"
                ]
                }
                },
                "type": [
                "object"
                ]
                },
                "viewGroupId": {
                "description":
                "viewGroupId of the viewgroup for the report",
                "type": [
                "string"
                ]
                },
                "viewGroupVersion": {
                "description":
                "version of viewgroup for the report",
                "type": [
                "string"
                ]
                }
                },
                "required": [
                "deliveries",
                "name",
                "schedule",
                "view",
                "viewGroupId",
                "viewGroupVersion"
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

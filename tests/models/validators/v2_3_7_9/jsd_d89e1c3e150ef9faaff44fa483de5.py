# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetListOfScheduledReportsV1 data model.

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


class JSONSchemaValidatorD89E1C3E150Ef9FaaFf44Fa483De5(object):
    """GetListOfScheduledReportsV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorD89E1C3E150Ef9FaaFf44Fa483De5, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "dataCategory": {
                "type": "string"
                },
                "deliveries": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "executionCount": {
                "type": "integer"
                },
                "executions": {
                "items": {
                "properties": {
                "endTime": {
                "type": "integer"
                },
                "errors": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "executionId": {
                "type": "string"
                },
                "processStatus": {
                "type": "string"
                },
                "requestStatus": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "warnings": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "name": {
                "type": "string"
                },
                "reportId": {
                "type": "string"
                },
                "reportWasExecuted": {
                "type": "boolean"
                },
                "schedule": {
                "type": "object"
                },
                "tags": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "view": {
                "properties": {
                "description":
                 {
                "type": "string"
                },
                "fieldGroups": {
                "items": {
                "properties": {
                "fieldGroupDisplayName": {
                "type": "string"
                },
                "fieldGroupName": {
                "type": "string"
                },
                "fields": {
                "items": {
                "properties": {
                "displayName": {
                "type": "string"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "filters": {
                "items": {
                "properties": {
                "displayName": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "value": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "format": {
                "properties": {
                "default": {
                "type": "boolean"
                },
                "formatType": {
                "type": "string"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "viewId": {
                "type": "string"
                },
                "viewInfo": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "viewGroupId": {
                "type": "string"
                },
                "viewGroupVersion": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }""".replace(
                    "\n" + " " * 16, ""
                )
            )
        )

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                "{} is invalid. Reason: {}".format(request, e.message)
            )

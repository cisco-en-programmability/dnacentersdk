# -*- coding: utf-8 -*-
"""Cisco DNA Center GetDeviceHistoryV1 data model.

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


class JSONSchemaValidatorF03966978A7F5Cd4B3228Dcae71373Fe(object):
    """GetDeviceHistoryV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorF03966978A7F5Cd4B3228Dcae71373Fe, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "details": {
                "type": "string"
                },
                "errorFlag": {
                "type": "boolean"
                },
                "historyTaskInfo": {
                "properties": {
                "addnDetails": {
                "items": {
                "properties": {
                "key": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "name": {
                "type": "string"
                },
                "timeTaken": {
                "type": "number"
                },
                "type": {
                "type": "string"
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "outputStr": {
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "type": "string"
                },
                "timeTaken": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "timestamp": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "statusCode": {
                "type": "number"
                }
                },
                "type": "object"
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

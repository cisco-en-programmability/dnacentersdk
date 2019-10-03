# -*- coding: utf-8 -*-
"""DNA Center Get Device details by IP data model.

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


class JSONSchemaValidator7Fbe4B804879Baa4(object):
    """Get Device details by IP request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator7Fbe4B804879Baa4, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "provisionDetails": {
                "description":
                "Provision Details",
                "properties": {
                "beginStep": {
                "description":
                "Begin Step",
                "type": [
                "string",
                "null"
                ]
                },
                "duration": {
                "description":
                "Duration",
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "description":
                "End Time",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "startTime": {
                "description":
                "Start Time",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "status": {
                "description":
                "Status",
                "type": [
                "string",
                "null"
                ]
                },
                "statusMessage": {
                "description":
                "Status Message",
                "type": [
                "string",
                "null"
                ]
                },
                "taskNodes": {
                "description":
                "Task Nodes",
                "items": {
                "properties": {
                "cliTemplateUserMessageDTO": {
                "description":
                "Cli Template User Message D T O",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "duration": {
                "description":
                "Duration",
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "description":
                "End Time",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "errorPayload": {
                "description":
                "Error Payload",
                "properties": {},
                "type": [
                "object",
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
                "nextTask": {
                "description":
                "Next Task",
                "type": [
                "string",
                "null"
                ]
                },
                "parentTask": {
                "description":
                "Parent Task",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "payload": {
                "description":
                "Payload",
                "type": [
                "string",
                "null"
                ]
                },
                "provisionedNames": {
                "description":
                "Provisioned Names",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "startTime": {
                "description":
                "Start Time",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "status": {
                "description":
                "Status",
                "type": [
                "string",
                "null"
                ]
                },
                "statusMessage": {
                "description":
                "Status Message",
                "type": [
                "string",
                "null"
                ]
                },
                "stepRan": {
                "description":
                "Step Ran",
                "type": [
                "string",
                "null"
                ]
                },
                "target": {
                "description":
                "Target",
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
                "topology": {
                "description":
                "Topology",
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

# -*- coding: utf-8 -*-
"""Cisco DNA Center GetDeviceDetailsByIP data model.

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


class JSONSchemaValidatorBfde206Eb445821A5722511F138814A(object):
    """GetDeviceDetailsByIP request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorBfde206Eb445821A5722511F138814A, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "provisionDetails": {
                "properties": {
                "beginStep": {
                "type": "string"
                },
                "duration": {
                "type": "string"
                },
                "endTime": {
                "type": "string"
                },
                "startTime": {
                "type": "string"
                },
                "status": {
                "type": "string"
                },
                "statusMessage": {
                "type": "string"
                },
                "taskNodes": {
                "items": {
                "properties": {
                "cliTemplateUserMessageDTO": {
                "type": "object"
                },
                "duration": {
                "type": "string"
                },
                "endTime": {
                "type": "string"
                },
                "errorPayload": {
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "nextTask": {
                "type": "string"
                },
                "parentTask": {
                "type": "object"
                },
                "payload": {
                "type": "string"
                },
                "provisionedNames": {
                "type": "object"
                },
                "startTime": {
                "type": "string"
                },
                "status": {
                "type": "string"
                },
                "statusMessage": {
                "type": "string"
                },
                "stepRan": {
                "type": "string"
                },
                "target": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "topology": {
                "type": "string"
                }
                },
                "type": "object"
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

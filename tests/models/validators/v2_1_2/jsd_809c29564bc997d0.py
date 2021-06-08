# -*- coding: utf-8 -*-
"""Cisco DNA Center Return replacement devices with details data model.

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


class JSONSchemaValidator809C29564Bc997D0(object):
    """Return replacement devices with details request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator809C29564Bc997D0, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "items": {
                "properties": {
                "creationTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "family": {
                "type": [
                "string",
                "null"
                ]
                },
                "faultyDeviceId": {
                "type": [
                "string",
                "null"
                ]
                },
                "faultyDeviceName": {
                "type": [
                "string",
                "null"
                ]
                },
                "faultyDevicePlatform": {
                "type": [
                "string",
                "null"
                ]
                },
                "faultyDeviceSerialNumber": {
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
                "neighbourDeviceId": {
                "type": [
                "string",
                "null"
                ]
                },
                "networkReadinessTaskId": {
                "type": [
                "string",
                "null"
                ]
                },
                "replacementDevicePlatform": {
                "type": [
                "string",
                "null"
                ]
                },
                "replacementDeviceSerialNumber": {
                "type": [
                "string",
                "null"
                ]
                },
                "replacementStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "replacementTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "workflowId": {
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
                "version": {
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
# -*- coding: utf-8 -*-
"""DNA Center Update Site data model.

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


class JSONSchemaValidator33AaB9B842388023(object):
    """Update Site request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator33AaB9B842388023, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "description":
                "Response",
                "properties": {
                "data": {
                "description":
                "Data",
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
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                "Instance Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "isError": {
                "description":
                "Is Error",
                "type": [
                "string",
                "null"
                ]
                },
                "operationIdList": {
                "description":
                "Operation Id List",
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
                "progress": {
                "description":
                "Progress",
                "type": [
                "string",
                "null"
                ]
                },
                "rootId": {
                "description":
                "Root Id",
                "type": [
                "string",
                "null"
                ]
                },
                "serviceType": {
                "description":
                "Service Type",
                "type": [
                "string",
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
                "version": {
                "description":
                "Version",
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
                "result": {
                "description":
                "Result",
                "type": [
                "string",
                "null"
                ]
                },
                "status": {
                "description":
                "Status",
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

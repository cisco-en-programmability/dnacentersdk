# -*- coding: utf-8 -*-
"""DNA Center Add a Workflow data model.

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


class JSONSchemaValidator848B5A7B4F9B8C12(object):
    """Add a Workflow request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator848B5A7B4F9B8C12, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "_id": {
                "description":
                 "",
                "type": "string"
                },
                "addToInventory": {
                "type": "boolean"
                },
                "addedOn": {
                "type": "number"
                },
                "configId": {
                "description":
                 "",
                "type": "string"
                },
                "currTaskIdx": {
                "type": "number"
                },
                "description":
                 {
                "description":
                 "",
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "execTime": {
                "type": "number"
                },
                "imageId": {
                "description":
                 "",
                "type": "string"
                },
                "instanceType": {
                "description":
                 "",
                "enum": [
                "SystemWorkflow",
                "UserWorkflow",
                "SystemResetWorkflow"
                ],
                "type": "string"
                },
                "lastupdateOn": {
                "type": "number"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "tasks": {
                "description":
                 "",
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": "number"
                },
                "endTime": {
                "type": "number"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "taskSeqNo": {
                "type": "number"
                },
                "timeTaken": {
                "type": "number"
                },
                "type": {
                "description":
                 "",
                "type": "string"
                },
                "workItemList": {
                "description":
                 "",
                "items": {
                "properties": {
                "command": {
                "description":
                 "",
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "outputStr": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
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
                "type": "array"
                },
                "tenantId": {
                "description":
                 "",
                "type": "string"
                },
                "type": {
                "description":
                 "",
                "type": "string"
                },
                "useState": {
                "description":
                 "",
                "type": "string"
                },
                "version": {
                "type": "number"
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

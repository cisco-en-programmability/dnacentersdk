# -*- coding: utf-8 -*-
"""DNA Center Update Workflow data model.

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


class JSONSchemaValidator3086C9624F498B85(object):
    """Update Workflow request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator3086C9624F498B85, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "_id": {
                "description":
                " Id",
                "type": [
                "string",
                "null"
                ]
                },
                "addToInventory": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "addedOn": {
                "type": [
                "number",
                "null"
                ]
                },
                "configId": {
                "description":
                "Config Id",
                "type": [
                "string",
                "null"
                ]
                },
                "currTaskIdx": {
                "type": [
                "number",
                "null"
                ]
                },
                "description":
                 {
                "description":
                "Description",
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "execTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "imageId": {
                "description":
                "Image Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceType": {
                "description":
                "Instance Type",
                "type": [
                "string",
                "null"
                ]
                },
                "lastupdateOn": {
                "type": [
                "number",
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
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "tasks": {
                "description":
                "Tasks",
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": [
                "number",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
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
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "taskSeqNo": {
                "type": [
                "number",
                "null"
                ]
                },
                "timeTaken": {
                "type": [
                "number",
                "null"
                ]
                },
                "type": {
                "description":
                "Type",
                "type": [
                "string",
                "null"
                ]
                },
                "workItemList": {
                "description":
                "Work Item List",
                "items": {
                "properties": {
                "command": {
                "description":
                "Command",
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputStr": {
                "description":
                "Output Str",
                "type": [
                "string",
                "null"
                ]
                },
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "timeTaken": {
                "type": [
                "number",
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
                "tenantId": {
                "description":
                "Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                "Type",
                "type": [
                "string",
                "null"
                ]
                },
                "useState": {
                "description":
                "Use State",
                "type": [
                "string",
                "null"
                ]
                },
                "version": {
                "type": [
                "number",
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

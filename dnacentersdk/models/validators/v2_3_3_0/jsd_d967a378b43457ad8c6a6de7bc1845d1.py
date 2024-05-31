# -*- coding: utf-8 -*-
"""Cisco DNA Center AddAWorkflow data model.

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


import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorD967A378B43457Ad8C6A6De7Bc1845D1(object):
    """AddAWorkflow request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD967A378B43457Ad8C6A6De7Bc1845D1, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "_id": {
                "type": "string"
                },
                "addToInventory": {
                "type": "boolean"
                },
                "addedOn": {
                "type": "integer"
                },
                "configId": {
                "type": "string"
                },
                "currTaskIdx": {
                "type": "integer"
                },
                "description":
                 {
                "type": "string"
                },
                "endTime": {
                "type": "integer"
                },
                "execTime": {
                "type": "integer"
                },
                "imageId": {
                "type": "string"
                },
                "instanceType": {
                "enum": [
                "SystemWorkflow",
                "UserWorkflow",
                "SystemResetWorkflow"
                ],
                "type": "string"
                },
                "lastupdateOn": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "tasks": {
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": "integer"
                },
                "endTime": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "taskSeqNo": {
                "type": "integer"
                },
                "timeTaken": {
                "type": "integer"
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
                "type": "integer"
                },
                "outputStr": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "timeTaken": {
                "type": "integer"
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
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "useState": {
                "type": "string"
                },
                "version": {
                "type": "integer"
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

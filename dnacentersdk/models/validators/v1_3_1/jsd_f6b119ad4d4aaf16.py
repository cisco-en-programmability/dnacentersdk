# -*- coding: utf-8 -*-
"""Cisco DNA Center Create Template data model.

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


class JSONSchemaValidatorF6B119Ad4D4AAf16(object):
    """Create Template request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF6B119Ad4D4AAf16, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "author": {
                "type": [
                "string",
                "null"
                ]
                },
                "composite": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "containingTemplates": {
                "items": {
                "properties": {
                "composite": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
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
                "createTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "description":
                 {
                "type": [
                "string",
                "null"
                ]
                },
                "deviceTypes": {
                "items": {
                "properties": {
                "productFamily": {
                "type": [
                "string",
                "null"
                ]
                },
                "productSeries": {
                "type": [
                "string",
                "null"
                ]
                },
                "productType": {
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
                "failurePolicy": {
                "enum": [
                "ABORT_ON_ERROR",
                "CONTINUE_ON_ERROR",
                "ROLLBACK_ON_ERROR",
                "ROLLBACK_TARGET_ON_ERROR",
                "ABORT_TARGET_ON_ERROR",
                null
                ],
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
                "lastUpdateTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "parentTemplateId": {
                "type": [
                "string",
                "null"
                ]
                },
                "projectId": {
                "type": [
                "string",
                "null"
                ]
                },
                "projectName": {
                "type": [
                "string",
                "null"
                ]
                },
                "rollbackTemplateContent": {
                "type": [
                "string",
                "null"
                ]
                },
                "rollbackTemplateParams": {
                "items": {
                "properties": {
                "binding": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataType": {
                "enum": [
                "STRING",
                "INTEGER",
                "IPADDRESS",
                "MACADDRESS",
                "SECTIONDIVIDER",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "defaultValue": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "description":
                 {
                "type": [
                "string",
                "null"
                ]
                },
                "displayName": {
                "type": [
                "string",
                "null"
                ]
                },
                "group": {
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
                "instructionText": {
                "type": [
                "string",
                "null"
                ]
                },
                "key": {
                "type": [
                "string",
                "null"
                ]
                },
                "notParam": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "order": {
                "type": [
                "number",
                "null"
                ]
                },
                "paramArray": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "parameterName": {
                "type": [
                "string",
                "null"
                ]
                },
                "provider": {
                "type": [
                "string",
                "null"
                ]
                },
                "range": {
                "items": {
                "properties": {
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "maxValue": {
                "type": [
                "number",
                "null"
                ]
                },
                "minValue": {
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
                },
                "required": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "selection": {
                "properties": {
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "selectionType": {
                "enum": [
                "SINGLE_SELECT",
                "MULTI_SELECT",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "selectionValues": {
                "properties": {},
                "type": [
                "object",
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
                "softwareType": {
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVariant": {
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "type": [
                "string",
                "null"
                ]
                },
                "tags": {
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
                "templateContent": {
                "type": [
                "string",
                "null"
                ]
                },
                "templateParams": {
                "items": {
                "properties": {
                "binding": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataType": {
                "enum": [
                "STRING",
                "INTEGER",
                "IPADDRESS",
                "MACADDRESS",
                "SECTIONDIVIDER",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "defaultValue": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "description":
                 {
                "type": [
                "string",
                "null"
                ]
                },
                "displayName": {
                "type": [
                "string",
                "null"
                ]
                },
                "group": {
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
                "instructionText": {
                "type": [
                "string",
                "null"
                ]
                },
                "key": {
                "type": [
                "string",
                "null"
                ]
                },
                "notParam": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "order": {
                "type": [
                "number",
                "null"
                ]
                },
                "paramArray": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "parameterName": {
                "type": [
                "string",
                "null"
                ]
                },
                "provider": {
                "type": [
                "string",
                "null"
                ]
                },
                "range": {
                "items": {
                "properties": {
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "maxValue": {
                "type": [
                "number",
                "null"
                ]
                },
                "minValue": {
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
                },
                "required": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "selection": {
                "properties": {
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "selectionType": {
                "enum": [
                "SINGLE_SELECT",
                "MULTI_SELECT",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "selectionValues": {
                "properties": {},
                "type": [
                "object",
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

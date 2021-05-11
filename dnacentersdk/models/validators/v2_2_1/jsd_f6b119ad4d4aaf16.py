# -*- coding: utf-8 -*-
"""DNA Center Create Template data model.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "version": {
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "deviceTypes": {
                "items": {
                "properties": {
                "productFamily": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "productSeries": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "productType": {
                "description":
                 "",
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
                "description":
                 "",
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
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "parentTemplateId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "projectId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "projectName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "rollbackTemplateContent": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "rollbackTemplateParams": {
                "items": {
                "properties": {
                "binding": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dataType": {
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "description":
                 {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "displayName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "group": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instructionText": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "key": {
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "provider": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "range": {
                "items": {
                "properties": {
                "id": {
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "selectionType": {
                "description":
                 "",
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
                "null",
                "number"
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVariant": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "templateParams": {
                "items": {
                "properties": {
                "binding": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dataType": {
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "description":
                 {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "displayName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "group": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instructionText": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "key": {
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "provider": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "range": {
                "items": {
                "properties": {
                "id": {
                "description":
                 "",
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
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "selectionType": {
                "description":
                 "",
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
                "null",
                "number"
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
                "description":
                 "",
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

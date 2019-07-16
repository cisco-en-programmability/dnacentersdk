# -*- coding: utf-8 -*-
"""DNA Center Update Template data model.

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


class JSONSchemaValidator7781Fa0548A98342(object):
    """Update Template request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator7781Fa0548A98342, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "author": {
                "description":
                 "",
                "type": "string"
                },
                "composite": {
                "type": "boolean"
                },
                "containingTemplates": {
                "description":
                 "",
                "items": {
                "properties": {
                "composite": {
                "type": "boolean"
                },
                "id": {
                "description":
                 "",
                "type": "string"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "version": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "createTime": {
                "type": "number"
                },
                "description":
                 {
                "description":
                 "",
                "type": "string"
                },
                "deviceTypes": {
                "description":
                 "",
                "items": {
                "properties": {
                "productFamily": {
                "description":
                 "",
                "type": "string"
                },
                "productSeries": {
                "description":
                 "",
                "type": "string"
                },
                "productType": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "failurePolicy": {
                "description":
                 "",
                "enum": [
                "ABORT_ON_ERROR",
                "CONTINUE_ON_ERROR",
                "ROLLBACK_ON_ERROR",
                "ROLLBACK_TARGET_ON_ERROR",
                "ABORT_TARGET_ON_ERROR"
                ],
                "type": "string"
                },
                "id": {
                "description":
                 "",
                "type": "string"
                },
                "lastUpdateTime": {
                "type": "number"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "parentTemplateId": {
                "description":
                 "",
                "type": "string"
                },
                "projectId": {
                "description":
                 "",
                "type": "string"
                },
                "projectName": {
                "description":
                 "",
                "type": "string"
                },
                "rollbackTemplateContent": {
                "description":
                 "",
                "type": "string"
                },
                "rollbackTemplateParams": {
                "description":
                 "",
                "items": {
                "properties": {
                "binding": {
                "description":
                 "",
                "type": "string"
                },
                "dataType": {
                "description":
                 "",
                "enum": [
                "STRING",
                "INTEGER",
                "IPADDRESS",
                "MACADDRESS",
                "SECTIONDIVIDER"
                ],
                "type": "string"
                },
                "defaultValue": {
                "description":
                 "",
                "type": "string"
                },
                "description":
                 {
                "description":
                 "",
                "type": "string"
                },
                "displayName": {
                "description":
                 "",
                "type": "string"
                },
                "group": {
                "description":
                 "",
                "type": "string"
                },
                "id": {
                "description":
                 "",
                "type": "string"
                },
                "instructionText": {
                "description":
                 "",
                "type": "string"
                },
                "key": {
                "description":
                 "",
                "type": "string"
                },
                "notParam": {
                "type": "boolean"
                },
                "order": {
                "type": "number"
                },
                "paramArray": {
                "type": "boolean"
                },
                "parameterName": {
                "description":
                 "",
                "type": "string"
                },
                "provider": {
                "description":
                 "",
                "type": "string"
                },
                "range": {
                "description":
                 "",
                "items": {
                "properties": {
                "id": {
                "description":
                 "",
                "type": "string"
                },
                "maxValue": {
                "type": "number"
                },
                "minValue": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "required": {
                "type": "boolean"
                },
                "selection": {
                "description":
                 "",
                "properties": {
                "id": {
                "description":
                 "",
                "type": "string"
                },
                "selectionType": {
                "description":
                 "",
                "enum": [
                "SINGLE_SELECT",
                "MULTI_SELECT"
                ],
                "type": "string"
                },
                "selectionValues": {
                "description":
                 "",
                "properties": {},
                "type": "object"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "softwareType": {
                "description":
                 "",
                "type": "string"
                },
                "softwareVariant": {
                "description":
                 "",
                "type": "string"
                },
                "softwareVersion": {
                "description":
                 "",
                "type": "string"
                },
                "tags": {
                "description":
                 "",
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "templateContent": {
                "description":
                 "",
                "type": "string"
                },
                "templateParams": {
                "description":
                 "",
                "items": {
                "properties": {
                "binding": {
                "description":
                 "",
                "type": "string"
                },
                "dataType": {
                "description":
                 "",
                "enum": [
                "STRING",
                "INTEGER",
                "IPADDRESS",
                "MACADDRESS",
                "SECTIONDIVIDER"
                ],
                "type": "string"
                },
                "defaultValue": {
                "description":
                 "",
                "type": "string"
                },
                "description":
                 {
                "description":
                 "",
                "type": "string"
                },
                "displayName": {
                "description":
                 "",
                "type": "string"
                },
                "group": {
                "description":
                 "",
                "type": "string"
                },
                "id": {
                "description":
                 "",
                "type": "string"
                },
                "instructionText": {
                "description":
                 "",
                "type": "string"
                },
                "key": {
                "description":
                 "",
                "type": "string"
                },
                "notParam": {
                "type": "boolean"
                },
                "order": {
                "type": "number"
                },
                "paramArray": {
                "type": "boolean"
                },
                "parameterName": {
                "description":
                 "",
                "type": "string"
                },
                "provider": {
                "description":
                 "",
                "type": "string"
                },
                "range": {
                "description":
                 "",
                "items": {
                "properties": {
                "id": {
                "description":
                 "",
                "type": "string"
                },
                "maxValue": {
                "type": "number"
                },
                "minValue": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "required": {
                "type": "boolean"
                },
                "selection": {
                "description":
                 "",
                "properties": {
                "id": {
                "description":
                 "",
                "type": "string"
                },
                "selectionType": {
                "description":
                 "",
                "enum": [
                "SINGLE_SELECT",
                "MULTI_SELECT"
                ],
                "type": "string"
                },
                "selectionValues": {
                "description":
                 "",
                "properties": {},
                "type": "object"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "version": {
                "description":
                 "",
                "type": "string"
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

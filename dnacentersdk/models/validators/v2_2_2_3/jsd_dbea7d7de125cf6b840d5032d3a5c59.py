# -*- coding: utf-8 -*-
"""Cisco DNA Center UpdateTemplate data model.

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


class JSONSchemaValidatorDbea7D7De125Cf6B840D5032D3A5C59(object):
    """UpdateTemplate request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorDbea7D7De125Cf6B840D5032D3A5C59, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "author": {
                "type": "string"
                },
                "composite": {
                "type": "boolean"
                },
                "containingTemplates": {
                "items": {
                "properties": {
                "composite": {
                "type": "boolean"
                },
                "description":
                 {
                "type": "string"
                },
                "deviceTypes": {
                "items": {
                "properties": {
                "productFamily": {
                "type": "string"
                },
                "productSeries": {
                "type": "string"
                },
                "productType": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "id": {
                "type": "string"
                },
                "language": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "projectName": {
                "type": "string"
                },
                "rollbackTemplateParams": {
                "items": {
                "properties": {
                "binding": {
                "type": "string"
                },
                "customOrder": {
                "type": "integer"
                },
                "dataType": {
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
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "displayName": {
                "type": "string"
                },
                "group": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instructionText": {
                "type": "string"
                },
                "key": {
                "type": "string"
                },
                "notParam": {
                "type": "boolean"
                },
                "order": {
                "type": "integer"
                },
                "paramArray": {
                "type": "boolean"
                },
                "parameterName": {
                "type": "string"
                },
                "provider": {
                "type": "string"
                },
                "range": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "maxValue": {
                "type": "integer"
                },
                "minValue": {
                "type": "integer"
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
                "properties": {
                "defaultSelectedValues": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "id": {
                "type": "string"
                },
                "selectionType": {
                "enum": [
                "SINGLE_SELECT",
                "MULTI_SELECT"
                ],
                "type": "string"
                },
                "selectionValues": {
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
                "tags": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "templateContent": {
                "type": "string"
                },
                "templateParams": {
                "items": {
                "properties": {
                "binding": {
                "type": "string"
                },
                "customOrder": {
                "type": "integer"
                },
                "dataType": {
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
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "displayName": {
                "type": "string"
                },
                "group": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instructionText": {
                "type": "string"
                },
                "key": {
                "type": "string"
                },
                "notParam": {
                "type": "boolean"
                },
                "order": {
                "type": "integer"
                },
                "paramArray": {
                "type": "boolean"
                },
                "parameterName": {
                "type": "string"
                },
                "provider": {
                "type": "string"
                },
                "range": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "maxValue": {
                "type": "integer"
                },
                "minValue": {
                "type": "integer"
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
                "properties": {
                "defaultSelectedValues": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "id": {
                "type": "string"
                },
                "selectionType": {
                "enum": [
                "SINGLE_SELECT",
                "MULTI_SELECT"
                ],
                "type": "string"
                },
                "selectionValues": {
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
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "createTime": {
                "type": "integer"
                },
                "customParamsOrder": {
                "type": "boolean"
                },
                "description":
                 {
                "type": "string"
                },
                "deviceTypes": {
                "items": {
                "properties": {
                "productFamily": {
                "type": "string"
                },
                "productSeries": {
                "type": "string"
                },
                "productType": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "failurePolicy": {
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
                "type": "string"
                },
                "language": {
                "type": "string"
                },
                "lastUpdateTime": {
                "type": "integer"
                },
                "latestVersionTime": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "parentTemplateId": {
                "type": "string"
                },
                "projectId": {
                "type": "string"
                },
                "projectName": {
                "type": "string"
                },
                "rollbackTemplateContent": {
                "type": "string"
                },
                "rollbackTemplateParams": {
                "items": {
                "properties": {
                "binding": {
                "type": "string"
                },
                "customOrder": {
                "type": "integer"
                },
                "dataType": {
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
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "displayName": {
                "type": "string"
                },
                "group": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instructionText": {
                "type": "string"
                },
                "key": {
                "type": "string"
                },
                "notParam": {
                "type": "boolean"
                },
                "order": {
                "type": "integer"
                },
                "paramArray": {
                "type": "boolean"
                },
                "parameterName": {
                "type": "string"
                },
                "provider": {
                "type": "string"
                },
                "range": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "maxValue": {
                "type": "integer"
                },
                "minValue": {
                "type": "integer"
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
                "properties": {
                "defaultSelectedValues": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "id": {
                "type": "string"
                },
                "selectionType": {
                "enum": [
                "SINGLE_SELECT",
                "MULTI_SELECT"
                ],
                "type": "string"
                },
                "selectionValues": {
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
                "type": "string"
                },
                "softwareVariant": {
                "type": "string"
                },
                "softwareVersion": {
                "type": "string"
                },
                "tags": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "templateContent": {
                "type": "string"
                },
                "templateParams": {
                "items": {
                "properties": {
                "binding": {
                "type": "string"
                },
                "customOrder": {
                "type": "integer"
                },
                "dataType": {
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
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "displayName": {
                "type": "string"
                },
                "group": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instructionText": {
                "type": "string"
                },
                "key": {
                "type": "string"
                },
                "notParam": {
                "type": "boolean"
                },
                "order": {
                "type": "integer"
                },
                "paramArray": {
                "type": "boolean"
                },
                "parameterName": {
                "type": "string"
                },
                "provider": {
                "type": "string"
                },
                "range": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "maxValue": {
                "type": "integer"
                },
                "minValue": {
                "type": "integer"
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
                "properties": {
                "defaultSelectedValues": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "id": {
                "type": "string"
                },
                "selectionType": {
                "enum": [
                "SINGLE_SELECT",
                "MULTI_SELECT"
                ],
                "type": "string"
                },
                "selectionValues": {
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
                "validationErrors": {
                "properties": {
                "rollbackTemplateErrors": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "templateErrors": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "templateId": {
                "type": "string"
                },
                "templateVersion": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "version": {
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

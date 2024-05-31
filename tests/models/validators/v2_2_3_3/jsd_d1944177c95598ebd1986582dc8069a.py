# -*- coding: utf-8 -*-
"""Cisco DNA Center GetViewDetailsForAGivenViewGroupAndView data model.

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


class JSONSchemaValidatorD1944177C95598EBd1986582Dc8069A(object):
    """GetViewDetailsForAGivenViewGroupAndView request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD1944177C95598EBd1986582Dc8069A, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "deliveries": {
                "items": {
                "properties": {
                "default": {
                "type": "boolean"
                },
                "type": {
                "enum": [
                "EMAIL",
                "WEBHOOK",
                "DOWNLOAD"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "description":
                 {
                "type": "string"
                },
                "fieldGroups": {
                "items": {
                "properties": {
                "fieldGroupDisplayName": {
                "type": "string"
                },
                "fieldGroupName": {
                "type": "string"
                },
                "fields": {
                "items": {
                "properties": {
                "displayName": {
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
                "tableId": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "filters": {
                "items": {
                "properties": {
                "additionalInfo": {
                "type": "object"
                },
                "cacheFilter": {
                "type": "boolean"
                },
                "dataType": {
                "type": "string"
                },
                "displayName": {
                "type": "string"
                },
                "filterSource": {
                "properties": {
                "dataSource": {
                "type": "object"
                },
                "displayValuePath": {
                "type": "string"
                },
                "rootPath": {
                "type": "string"
                },
                "valuePath": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "required": {
                "type": "boolean"
                },
                "timeOptions": {
                "items": {
                "properties": {
                "info": {
                "type": "string"
                },
                "maxValue": {
                "type": "integer"
                },
                "minValue": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "formats": {
                "items": {
                "properties": {
                "default": {
                "type": "boolean"
                },
                "format": {
                "enum": [
                "CSV",
                "TDE",
                "JSON",
                "PDF"
                ],
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "template": {
                "properties": {
                "jsTemplateId": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "schedules": {
                "items": {
                "properties": {
                "default": {
                "type": "boolean"
                },
                "type": {
                "enum": [
                "SCHEDULE_NOW",
                "SCHEDULE_LATER",
                "SCHEDULE_RECURRENCE"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "viewId": {
                "type": "string"
                },
                "viewInfo": {
                "type": "string"
                },
                "viewName": {
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

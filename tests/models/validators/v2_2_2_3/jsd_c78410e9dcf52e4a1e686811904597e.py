# -*- coding: utf-8 -*-
"""Cisco DNA Center GetFloormaps data model.

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


class JSONSchemaValidatorC78410E9Dcf52E4A1E686811904597E(object):
    """GetFloormaps request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC78410E9Dcf52E4A1E686811904597E, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "items": {
                "items": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingName": {
                "type": "string"
                },
                "contact": {
                "type": "object"
                },
                "criticalRadioCount": {
                "type": "string"
                },
                "floorIndex": {
                "type": "number"
                },
                "geometry": {
                "properties": {
                "height": {
                "type": "number"
                },
                "length": {
                "type": "number"
                },
                "offsetX": {
                "type": "number"
                },
                "offsetY": {
                "type": "number"
                },
                "type": {
                "type": "object"
                },
                "width": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "groupInstanceUuid": {
                "type": "string"
                },
                "id": {
                "type": "integer"
                },
                "imageInfo": {
                "properties": {
                "categories": {
                "type": "object"
                },
                "enteredImageName": {
                "type": "object"
                },
                "features": {
                "type": "object"
                },
                "generatedRasterImage": {
                "type": "object"
                },
                "image": {
                "type": "object"
                },
                "isCadFile": {
                "type": "boolean"
                },
                "shapes": {
                "type": "object"
                },
                "thumbnail": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "instanceUuid": {
                "type": "string"
                },
                "items": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "location": {
                "properties": {
                "address": {
                "type": "string"
                },
                "country": {
                "type": "string"
                },
                "height": {
                "type": "number"
                },
                "lat": {
                "type": "number"
                },
                "lon": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "maintainAspectRatio": {
                "type": "boolean"
                },
                "metrics": {
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "parentGroupUuid": {
                "type": "string"
                },
                "siteName": {
                "type": "string"
                },
                "type": {
                "type": "integer"
                },
                "wirelessClientsCount": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "total": {
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

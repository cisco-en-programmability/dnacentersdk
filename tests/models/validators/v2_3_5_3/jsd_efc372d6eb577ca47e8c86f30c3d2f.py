# -*- coding: utf-8 -*-
"""Cisco DNA Center GetPlannedAccessPointsForBuilding data model.

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

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorEfc372D6Eb577CA47E8C86F30C3D2F(object):
    """GetPlannedAccessPointsForBuilding request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorEfc372D6Eb577CA47E8C86F30C3D2F, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "attributes": {
                "properties": {
                "createDate": {
                "type": "integer"
                },
                "domain": {
                "type": "string"
                },
                "heirarchyName": {
                "type": "string"
                },
                "id": {
                "type": "integer"
                },
                "instanceUuid": {
                "type": "string"
                },
                "macaddress": {
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "source": {
                "type": "string"
                },
                "typeString": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "isSensor": {
                "type": "boolean"
                },
                "location": {
                "type": "object"
                },
                "position": {
                "properties": {
                "x": {
                "type": "number"
                },
                "y": {
                "type": "number"
                },
                "z": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "radioCount": {
                "type": "integer"
                },
                "radios": {
                "items": {
                "properties": {
                "antenna": {
                "properties": {
                "azimuthAngle": {
                "type": "number"
                },
                "elevationAngle": {
                "type": "number"
                },
                "gain": {
                "type": "number"
                },
                "mode": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "attributes": {
                "properties": {
                "channel": {
                "type": "object"
                },
                "channelString": {
                "type": "object"
                },
                "id": {
                "type": "integer"
                },
                "ifMode": {
                "type": "string"
                },
                "ifTypeString": {
                "type": "string"
                },
                "ifTypeSubband": {
                "type": "string"
                },
                "instanceUuid": {
                "type": "string"
                },
                "slotId": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "isSensor": {
                "type": "boolean"
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
                "total": {
                "type": "integer"
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

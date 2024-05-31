# -*- coding: utf-8 -*-
"""Cisco DNA Center CreatePlannedAccessPointForFloor data model.

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


class JSONSchemaValidatorCa2Fe989A227585086452D24D32867A6(object):
    """CreatePlannedAccessPointForFloor request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorCa2Fe989A227585086452D24D32867A6, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
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
                "type": "number"
                },
                "instanceUuid": {
                "type": "string"
                },
                "macaddress": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "source": {
                "enum": [
                "EKAHAU",
                "MANUAL",
                "UNKNOWN"
                ],
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
                "properties": {
                "altitude": {
                "type": "number"
                },
                "lattitude": {
                "type": "number"
                },
                "longtitude": {
                "type": "number"
                }
                },
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
                "enum": [
                "sector_a",
                "sector_b",
                "omni",
                "unknown"
                ],
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "type": {
                "enum": [
                "internal",
                "external",
                "circular",
                "linear",
                "unknown"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "attributes": {
                "properties": {
                "channel": {
                "type": "number"
                },
                "channelString": {
                "type": "string"
                },
                "id": {
                "type": "number"
                },
                "ifMode": {
                "enum": [
                "A",
                "B",
                "ABGN",
                "Monitor",
                "Sniffer",
                "XorMonitor",
                "Xor24",
                "Xor5",
                "Xor6",
                "XorUnknown",
                "_6GHZ",
                "XOR56GHZ",
                "Unknown"
                ],
                "type": "string"
                },
                "ifTypeString": {
                "type": "string"
                },
                "ifTypeSubband": {
                "enum": [
                "A",
                "B",
                "ABGN",
                "_6GHZ",
                "_XOR_5_6GHZ",
                "Unknown"
                ],
                "type": "string"
                },
                "instanceUuid": {
                "type": "string"
                },
                "slotId": {
                "type": "number"
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
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )

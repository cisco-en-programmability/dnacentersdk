# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetPhysicalTopologyV1 data model.

Copyright (c) 2025 Cisco Systems.

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


class JSONSchemaValidatorEB4Ab5A978Fe8785516C8Af42(object):
    """GetPhysicalTopologyV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorEB4Ab5A978Fe8785516C8Af42, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "id": {
                "type": "string"
                },
                "links": {
                "items": {
                "properties": {
                "additionalInfo": {
                "type": "object"
                },
                "endPortID": {
                "type": "string"
                },
                "endPortIpv4Address": {
                "type": "string"
                },
                "endPortIpv4Mask": {
                "type": "string"
                },
                "endPortName": {
                "type": "string"
                },
                "endPortSpeed": {
                "type": "string"
                },
                "greyOut": {
                "type": "boolean"
                },
                "id": {
                "type": "string"
                },
                "linkStatus": {
                "type": "string"
                },
                "source": {
                "type": "string"
                },
                "startPortID": {
                "type": "string"
                },
                "startPortIpv4Address": {
                "type": "string"
                },
                "startPortIpv4Mask": {
                "type": "string"
                },
                "startPortName": {
                "type": "string"
                },
                "startPortSpeed": {
                "type": "string"
                },
                "tag": {
                "type": "string"
                },
                "target": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "nodes": {
                "items": {
                "properties": {
                "aclApplied": {
                "type": "boolean"
                },
                "additionalInfo": {
                "type": "object"
                },
                "connectedDeviceId": {
                "type": "string"
                },
                "customParam": {
                "properties": {
                "id": {
                "type": "string"
                },
                "label": {
                "type": "string"
                },
                "parentNodeId": {
                "type": "string"
                },
                "x": {
                "type": "integer"
                },
                "y": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "dataPathId": {
                "type": "string"
                },
                "deviceSeries": {
                "type": "string"
                },
                "deviceType": {
                "type": "string"
                },
                "family": {
                "type": "string"
                },
                "fixed": {
                "type": "boolean"
                },
                "greyOut": {
                "type": "boolean"
                },
                "id": {
                "type": "string"
                },
                "ip": {
                "type": "string"
                },
                "label": {
                "type": "string"
                },
                "networkType": {
                "type": "string"
                },
                "nodeType": {
                "type": "string"
                },
                "order": {
                "type": "integer"
                },
                "osType": {
                "type": "string"
                },
                "platformId": {
                "type": "string"
                },
                "role": {
                "type": "string"
                },
                "roleSource": {
                "type": "string"
                },
                "softwareVersion": {
                "type": "string"
                },
                "tags": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "upperNode": {
                "type": "string"
                },
                "userId": {
                "type": "string"
                },
                "vlanId": {
                "type": "string"
                },
                "x": {
                "type": "integer"
                },
                "y": {
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
                "version": {
                "type": "string"
                }
                },
                "type": "object"
                }""".replace(
                    "\n" + " " * 16, ""
                )
            )
        )

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                "{} is invalid. Reason: {}".format(request, e.message)
            )

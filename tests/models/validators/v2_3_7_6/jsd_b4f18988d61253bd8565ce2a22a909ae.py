# -*- coding: utf-8 -*-
"""Cisco DNA Center QueryTheEndpointsV1 data model.

Copyright (c) 2024 Cisco Systems.

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


class JSONSchemaValidatorB4F18988D61253Bd8565Ce2A22A909Ae(object):
    """QueryTheEndpointsV1 request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorB4F18988D61253Bd8565Ce2A22A909Ae, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "hasMoreResults": {
                "type": "boolean"
                },
                "items": {
                "items": {
                "properties": {
                "ancPolicy": {
                "type": "string"
                },
                "attributes": {
                "type": "object"
                },
                "deviceType": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "duid": {
                "type": "string"
                },
                "granularAncPolicy": {
                "items": {
                "properties": {
                "name": {
                "type": "string"
                },
                "nasIpAddress": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "hardwareManufacturer": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "hardwareModel": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "id": {
                "type": "string"
                },
                "lastProbeCollectionTimestamp": {
                "type": "integer"
                },
                "macAddress": {
                "type": "string"
                },
                "operatingSystem": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "randomMac": {
                "type": "boolean"
                },
                "registered": {
                "type": "boolean"
                },
                "trustData": {
                "properties": {
                "aiSpoofingTrustLevel": {
                "enum": [
                "low",
                "medium",
                "high"
                ],
                "type": "string"
                },
                "authMethod": {
                "type": "string"
                },
                "changedProfileTrustLevel": {
                "enum": [
                "low",
                "medium",
                "high"
                ],
                "type": "string"
                },
                "concurrentMacTrustLevel": {
                "enum": [
                "low",
                "medium",
                "high"
                ],
                "type": "string"
                },
                "ipBlocklistDetected": {
                "type": "boolean"
                },
                "natTrustLevel": {
                "enum": [
                "low",
                "medium",
                "high"
                ],
                "type": "string"
                },
                "postureStatus": {
                "enum": [
                "Compliant",
                "Non-Compliant",
                "Grace Compliant",
                "Pending",
                "Unknown"
                ],
                "type": "string"
                },
                "trustScore": {
                "type": "integer"
                },
                "unauthPortDetected": {
                "type": "boolean"
                },
                "weakCredDetected": {
                "type": "boolean"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "totalResults": {
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

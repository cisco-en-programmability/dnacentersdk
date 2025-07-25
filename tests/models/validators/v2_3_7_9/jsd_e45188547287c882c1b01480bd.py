# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetAnchorGroupByIDV1 data model.

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


class JSONSchemaValidatorE45188547287C882C1B01480Bd(object):
    """GetAnchorGroupByIDV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorE45188547287C882C1B01480Bd, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "anchorGroupName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "mobilityAnchors": {
                "items": {
                "properties": {
                "anchorPriority": {
                "enum": [
                "PRIMARY",
                "SECONDARY",
                "TERTIARY"
                ],
                "type": "string"
                },
                "deviceName": {
                "type": "string"
                },
                "ipAddress": {
                "type": "string"
                },
                "macAddress": {
                "type": "string"
                },
                "managedAnchorWlc": {
                "type": "boolean"
                },
                "mobilityGroupName": {
                "type": "string"
                },
                "peerDeviceType": {
                "enum": [
                "IOS-XE",
                "AIREOS"
                ],
                "type": "string"
                },
                "privateIp": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
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

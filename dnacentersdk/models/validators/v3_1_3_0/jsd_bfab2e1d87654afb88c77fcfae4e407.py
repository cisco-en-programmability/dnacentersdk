# -*- coding: utf-8 -*-
"""Cisco DNA Center UpdateDot11axConfigurationFeatureTemplate data model.

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


class JSONSchemaValidatorBfab2E1D87654AfB88C77Fcfae4E407(object):
    """UpdateDot11axConfigurationFeatureTemplate request schema
    definition."""

    def __init__(self):
        super(JSONSchemaValidatorBfab2E1D87654AfB88C77Fcfae4E407, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "designName": {
                "type": "string"
                },
                "featureAttributes": {
                "properties": {
                "bssColor": {
                "type": "boolean"
                },
                "multipleBssid": {
                "type": "boolean"
                },
                "nonSRGObssPdMaxThreshold": {
                "type": "integer"
                },
                "obssPd": {
                "type": "boolean"
                },
                "radioBand": {
                "enum": [
                "2_4GHZ",
                "5GHZ",
                "6GHZ"
                ],
                "type": "string"
                },
                "targetWakeUpTime11ax": {
                "type": "boolean"
                },
                "targetWaketimeBroadcast": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "unlockedAttributes": {
                "items": {
                "type": "string"
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

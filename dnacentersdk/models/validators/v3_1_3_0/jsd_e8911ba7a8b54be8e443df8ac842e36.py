# -*- coding: utf-8 -*-
"""Cisco DNA Center CreateCleanAirConfigurationFeatureTemplate data model.

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


class JSONSchemaValidatorE8911Ba7A8B54Be8E443Df8Ac842E36(object):
    """CreateCleanAirConfigurationFeatureTemplate request schema
    definition."""

    def __init__(self):
        super(JSONSchemaValidatorE8911Ba7A8B54Be8E443Df8Ac842E36, self).__init__()
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
                "cleanAir": {
                "type": "boolean"
                },
                "cleanAirDeviceReporting": {
                "type": "boolean"
                },
                "description":
                 {
                "type": "string"
                },
                "interferersFeatures": {
                "properties": {
                "bleBeacon": {
                "type": "boolean"
                },
                "bluetoothPagingInquiry": {
                "type": "boolean"
                },
                "bluetoothScoAcl": {
                "type": "boolean"
                },
                "continuousTransmitter": {
                "type": "boolean"
                },
                "genericDect": {
                "type": "boolean"
                },
                "genericTdd": {
                "type": "boolean"
                },
                "jammer": {
                "type": "boolean"
                },
                "microwaveOven": {
                "type": "boolean"
                },
                "motorolaCanopy": {
                "type": "boolean"
                },
                "siFhss": {
                "type": "boolean"
                },
                "spectrum80211Fh": {
                "type": "boolean"
                },
                "spectrum80211NonStandardChannel": {
                "type": "boolean"
                },
                "spectrum802154": {
                "type": "boolean"
                },
                "spectrumInverted": {
                "type": "boolean"
                },
                "superAg": {
                "type": "boolean"
                },
                "videoCamera": {
                "type": "boolean"
                },
                "wimaxFixed": {
                "type": "boolean"
                },
                "wimaxMobile": {
                "type": "boolean"
                },
                "xbox": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "persistentDevicePropagation": {
                "type": "boolean"
                },
                "radioBand": {
                "enum": [
                "2_4GHZ",
                "5GHZ",
                "6GHZ"
                ],
                "type": "string"
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

# -*- coding: utf-8 -*-
"""Cisco DNA Center UpdateRFProfileV1 data model.

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


class JSONSchemaValidatorDa455F4BE5B75126Ba9970C7Cc54C7Db(object):
    """UpdateRFProfileV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorDa455F4BE5B75126Ba9970C7Cc54C7Db, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "defaultRfProfile": {
                "type": "boolean"
                },
                "enableRadioType6GHz": {
                "type": "boolean"
                },
                "enableRadioTypeA": {
                "type": "boolean"
                },
                "enableRadioTypeB": {
                "type": "boolean"
                },
                "radioType6GHzProperties": {
                "properties": {
                "dataRates": {
                "type": "string"
                },
                "enableStandardPowerService": {
                "type": "boolean"
                },
                "mandatoryDataRates": {
                "type": "string"
                },
                "maxDbsWidth": {
                "type": "integer"
                },
                "maxPowerLevel": {
                "type": "integer"
                },
                "minDbsWidth": {
                "type": "integer"
                },
                "minPowerLevel": {
                "type": "integer"
                },
                "multiBssidProperties": {
                "properties": {
                "dot11axParameters": {
                "properties": {
                "muMimoDownLink": {
                "type": "boolean"
                },
                "muMimoUpLink": {
                "type": "boolean"
                },
                "ofdmaDownLink": {
                "type": "boolean"
                },
                "ofdmaUpLink": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "dot11beParameters": {
                "properties": {
                "muMimoDownLink": {
                "type": "boolean"
                },
                "muMimoUpLink": {
                "type": "boolean"
                },
                "ofdmaDownLink": {
                "type": "boolean"
                },
                "ofdmaMultiRu": {
                "type": "boolean"
                },
                "ofdmaUpLink": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "targetWakeTime": {
                "type": "boolean"
                },
                "twtBroadcastSupport": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "parentProfile": {
                "enum": [
                "CUSTOM"
                ],
                "type": "string"
                },
                "powerThresholdV1": {
                "type": "integer"
                },
                "preamblePuncture": {
                "type": "boolean"
                },
                "radioChannels": {
                "type": "string"
                },
                "rxSopThreshold": {
                "enum": [
                "HIGH",
                "MEDIUM",
                "LOW",
                "AUTO"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "radioTypeAProperties": {
                "properties": {
                "channelWidth": {
                "enum": [
                "20",
                "40",
                "80",
                "160",
                "best"
                ],
                "type": "string"
                },
                "dataRates": {
                "type": "string"
                },
                "mandatoryDataRates": {
                "type": "string"
                },
                "maxPowerLevel": {
                "type": "integer"
                },
                "minPowerLevel": {
                "type": "integer"
                },
                "parentProfile": {
                "enum": [
                "HIGH",
                "TYPICAL",
                "LOW",
                "CUSTOM",
                "GLOBAL"
                ],
                "type": "string"
                },
                "powerThresholdV1": {
                "type": "integer"
                },
                "preamblePuncture": {
                "type": "boolean"
                },
                "radioChannels": {
                "type": "string"
                },
                "rxSopThreshold": {
                "enum": [
                "HIGH",
                "MEDIUM",
                "LOW",
                "AUTO"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "radioTypeBProperties": {
                "properties": {
                "dataRates": {
                "type": "string"
                },
                "mandatoryDataRates": {
                "type": "string"
                },
                "maxPowerLevel": {
                "type": "integer"
                },
                "minPowerLevel": {
                "type": "integer"
                },
                "parentProfile": {
                "enum": [
                "HIGH",
                "TYPICAL",
                "LOW",
                "CUSTOM",
                "GLOBAL"
                ],
                "type": "string"
                },
                "powerThresholdV1": {
                "type": "integer"
                },
                "radioChannels": {
                "type": "string"
                },
                "rxSopThreshold": {
                "enum": [
                "HIGH",
                "MEDIUM",
                "LOW",
                "AUTO"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "rfProfileName": {
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

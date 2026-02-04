# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetRFProfiles data model.

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


class JSONSchemaValidatorE11599Ca71552E960DC2Cdd182Abb9(object):
    """GetRFProfiles request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE11599Ca71552E960DC2Cdd182Abb9, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "defaultRfProfile": {
                "type": "boolean"
                },
                "enableCustom": {
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
                "id": {
                "type": "string"
                },
                "radioType6GHzProperties": {
                "properties": {
                "broadcastProbeResponseInterval": {
                "type": "integer"
                },
                "coverageHoleDetectionProperties": {
                "properties": {
                "chdClientLevel": {
                "type": "integer"
                },
                "chdDataRssiThreshold": {
                "type": "integer"
                },
                "chdExceptionLevel": {
                "type": "integer"
                },
                "chdVoiceRssiThreshold": {
                "type": "integer"
                }
                },
                "required": [
                "chdClientLevel",
                "chdDataRssiThreshold",
                "chdVoiceRssiThreshold",
                "chdExceptionLevel"
                ],
                "type": "object"
                },
                "customRxSopThreshold": {
                "type": "integer"
                },
                "dataRates": {
                "type": "string"
                },
                "discoveryFrames6GHz": {
                "enum": [
                "None",
                "Broadcast Probe Response",
                "FILS Discovery"
                ],
                "type": "string"
                },
                "enableStandardPowerService": {
                "type": "boolean"
                },
                "fraPropertiesC": {
                "properties": {
                "clientResetCount": {
                "type": "integer"
                },
                "clientUtilizationThreshold": {
                "type": "integer"
                }
                },
                "required": [
                "clientResetCount",
                "clientUtilizationThreshold"
                ],
                "type": "object"
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
                "maxRadioClients": {
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
                "required": [
                "ofdmaDownLink",
                "ofdmaUpLink",
                "muMimoUpLink",
                "muMimoDownLink"
                ],
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
                "required": [
                "ofdmaDownLink",
                "ofdmaUpLink",
                "muMimoUpLink",
                "muMimoDownLink",
                "ofdmaMultiRu"
                ],
                "type": "object"
                },
                "targetWakeTime": {
                "type": "boolean"
                },
                "twtBroadcastSupport": {
                "type": "boolean"
                }
                },
                "required": [
                "dot11axParameters",
                "dot11beParameters",
                "targetWakeTime",
                "twtBroadcastSupport"
                ],
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
                "pscEnforcingEnabled": {
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
                "AUTO",
                "CUSTOM"
                ],
                "type": "string"
                },
                "spatialReuseProperties": {
                "properties": {
                "dot11axNonSrgObssPacketDetect": {
                "type": "boolean"
                },
                "dot11axNonSrgObssPacketDetectMaxThreshold": {
                "type": "integer"
                },
                "dot11axSrgObssPacketDetect": {
                "type": "boolean"
                },
                "dot11axSrgObssPacketDetectMaxThreshold": {
                "type": "integer"
                },
                "dot11axSrgObssPacketDetectMinThreshold": {
                "type": "integer"
                }
                },
                "required": [
                "dot11axNonSrgObssPacketDetect",
                "dot11axNonSrgObssPacketDetectMaxThreshold",
                "dot11axSrgObssPacketDetect",
                "dot11axSrgObssPacketDetectMinThreshold",
                "dot11axSrgObssPacketDetectMaxThreshold"
                ],
                "type": "object"
                }
                },
                "required": [
                "parentProfile",
                "radioChannels",
                "dataRates",
                "mandatoryDataRates",
                "powerThresholdV1",
                "rxSopThreshold",
                "minPowerLevel",
                "maxPowerLevel",
                "enableStandardPowerService",
                "multiBssidProperties",
                "preamblePuncture",
                "minDbsWidth",
                "maxDbsWidth",
                "maxRadioClients",
                "pscEnforcingEnabled",
                "discoveryFrames6GHz",
                "broadcastProbeResponseInterval",
                "fraPropertiesC",
                "coverageHoleDetectionProperties",
                "spatialReuseProperties"
                ],
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
                "coverageHoleDetectionProperties": {
                "properties": {
                "chdClientLevel": {
                "type": "integer"
                },
                "chdDataRssiThreshold": {
                "type": "integer"
                },
                "chdExceptionLevel": {
                "type": "integer"
                },
                "chdVoiceRssiThreshold": {
                "type": "integer"
                }
                },
                "required": [
                "chdClientLevel",
                "chdDataRssiThreshold",
                "chdVoiceRssiThreshold",
                "chdExceptionLevel"
                ],
                "type": "object"
                },
                "customRxSopThreshold": {
                "type": "integer"
                },
                "dataRates": {
                "type": "string"
                },
                "fraPropertiesA": {
                "properties": {
                "clientAware": {
                "type": "boolean"
                },
                "clientReset": {
                "type": "integer"
                },
                "clientSelect": {
                "type": "integer"
                }
                },
                "required": [
                "clientAware",
                "clientSelect",
                "clientReset"
                ],
                "type": "object"
                },
                "mandatoryDataRates": {
                "type": "string"
                },
                "maxPowerLevel": {
                "type": "integer"
                },
                "maxRadioClients": {
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
                "AUTO",
                "CUSTOM"
                ],
                "type": "string"
                },
                "spatialReuseProperties": {
                "properties": {
                "dot11axNonSrgObssPacketDetect": {
                "type": "boolean"
                },
                "dot11axNonSrgObssPacketDetectMaxThreshold": {
                "type": "integer"
                },
                "dot11axSrgObssPacketDetect": {
                "type": "boolean"
                },
                "dot11axSrgObssPacketDetectMaxThreshold": {
                "type": "integer"
                },
                "dot11axSrgObssPacketDetectMinThreshold": {
                "type": "integer"
                }
                },
                "required": [
                "dot11axNonSrgObssPacketDetect",
                "dot11axNonSrgObssPacketDetectMaxThreshold",
                "dot11axSrgObssPacketDetect",
                "dot11axSrgObssPacketDetectMinThreshold",
                "dot11axSrgObssPacketDetectMaxThreshold"
                ],
                "type": "object"
                },
                "zeroWaitDfsEnable": {
                "type": "boolean"
                }
                },
                "required": [
                "parentProfile",
                "radioChannels",
                "dataRates",
                "mandatoryDataRates",
                "powerThresholdV1",
                "rxSopThreshold",
                "minPowerLevel",
                "maxPowerLevel",
                "channelWidth",
                "preamblePuncture",
                "zeroWaitDfsEnable",
                "maxRadioClients",
                "fraPropertiesA",
                "coverageHoleDetectionProperties",
                "spatialReuseProperties"
                ],
                "type": "object"
                },
                "radioTypeBProperties": {
                "properties": {
                "coverageHoleDetectionProperties": {
                "properties": {
                "chdClientLevel": {
                "type": "integer"
                },
                "chdDataRssiThreshold": {
                "type": "integer"
                },
                "chdExceptionLevel": {
                "type": "integer"
                },
                "chdVoiceRssiThreshold": {
                "type": "integer"
                }
                },
                "required": [
                "chdClientLevel",
                "chdDataRssiThreshold",
                "chdVoiceRssiThreshold",
                "chdExceptionLevel"
                ],
                "type": "object"
                },
                "customRxSopThreshold": {
                "type": "integer"
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
                "maxRadioClients": {
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
                "AUTO",
                "CUSTOM"
                ],
                "type": "string"
                },
                "spatialReuseProperties": {
                "properties": {
                "dot11axNonSrgObssPacketDetect": {
                "type": "boolean"
                },
                "dot11axNonSrgObssPacketDetectMaxThreshold": {
                "type": "integer"
                },
                "dot11axSrgObssPacketDetect": {
                "type": "boolean"
                },
                "dot11axSrgObssPacketDetectMaxThreshold": {
                "type": "integer"
                },
                "dot11axSrgObssPacketDetectMinThreshold": {
                "type": "integer"
                }
                },
                "required": [
                "dot11axNonSrgObssPacketDetect",
                "dot11axNonSrgObssPacketDetectMaxThreshold",
                "dot11axSrgObssPacketDetect",
                "dot11axSrgObssPacketDetectMinThreshold",
                "dot11axSrgObssPacketDetectMaxThreshold"
                ],
                "type": "object"
                }
                },
                "required": [
                "parentProfile",
                "radioChannels",
                "dataRates",
                "mandatoryDataRates",
                "powerThresholdV1",
                "rxSopThreshold",
                "minPowerLevel",
                "maxPowerLevel",
                "maxRadioClients",
                "coverageHoleDetectionProperties",
                "spatialReuseProperties"
                ],
                "type": "object"
                },
                "rfProfileName": {
                "type": "string"
                }
                },
                "required": [
                "rfProfileName",
                "defaultRfProfile",
                "enableRadioTypeA",
                "enableRadioTypeB",
                "enableRadioType6GHz",
                "enableCustom",
                "radioTypeAProperties",
                "radioTypeBProperties",
                "radioType6GHzProperties",
                "id"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "version": {
                "type": "string"
                }
                },
                "required": [
                "response",
                "version"
                ],
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

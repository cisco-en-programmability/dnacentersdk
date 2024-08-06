# -*- coding: utf-8 -*-
"""Cisco DNA Center ConfigureAccessPointsV1 data model.

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


class JSONSchemaValidatorE0Bd567C1395531A7F18Ab4E14110Bd(object):
    """ConfigureAccessPointsV1 request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE0Bd567C1395531A7F18Ab4E14110Bd, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "adminStatus": {
                "type": "boolean"
                },
                "apList": {
                "items": {
                "properties": {
                "apName": {
                "type": "string"
                },
                "apNameNew": {
                "type": "string"
                },
                "macAddress": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "apMode": {
                "type": "integer"
                },
                "configureAdminStatus": {
                "type": "boolean"
                },
                "configureApMode": {
                "type": "boolean"
                },
                "configureFailoverPriority": {
                "type": "boolean"
                },
                "configureHAController": {
                "type": "boolean"
                },
                "configureLedBrightnessLevel": {
                "type": "boolean"
                },
                "configureLedStatus": {
                "type": "boolean"
                },
                "configureLocation": {
                "type": "boolean"
                },
                "failoverPriority": {
                "type": "integer"
                },
                "isAssignedSiteAsLocation": {
                "type": "boolean"
                },
                "ledBrightnessLevel": {
                "type": "integer"
                },
                "ledStatus": {
                "type": "boolean"
                },
                "location": {
                "type": "string"
                },
                "primaryControllerName": {
                "type": "string"
                },
                "primaryIpAddress": {
                "properties": {
                "address": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "radioConfigurations": {
                "items": {
                "properties": {
                "adminStatus": {
                "type": "boolean"
                },
                "antennaCableName": {
                "type": "string"
                },
                "antennaGain": {
                "type": "integer"
                },
                "antennaPatternName": {
                "type": "string"
                },
                "cableLoss": {
                "type": "number"
                },
                "channelAssignmentMode": {
                "type": "integer"
                },
                "channelNumber": {
                "type": "integer"
                },
                "channelWidth": {
                "type": "integer"
                },
                "cleanAirSI": {
                "type": "integer"
                },
                "configureAdminStatus": {
                "type": "boolean"
                },
                "configureAntennaCable": {
                "type": "boolean"
                },
                "configureAntennaPatternName": {
                "type": "boolean"
                },
                "configureChannel": {
                "type": "boolean"
                },
                "configureChannelWidth": {
                "type": "boolean"
                },
                "configureCleanAirSI": {
                "type": "boolean"
                },
                "configurePower": {
                "type": "boolean"
                },
                "configureRadioRoleAssignment": {
                "type": "boolean"
                },
                "powerAssignmentMode": {
                "type": "integer"
                },
                "powerlevel": {
                "type": "integer"
                },
                "radioBand": {
                "enum": [
                "RADIO24",
                "RADIO5"
                ],
                "type": "string"
                },
                "radioRoleAssignment": {
                "enum": [
                "auto",
                "serving",
                "monitor"
                ],
                "type": "string"
                },
                "radioType": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "secondaryControllerName": {
                "type": "string"
                },
                "secondaryIpAddress": {
                "properties": {
                "address": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "tertiaryControllerName": {
                "type": "string"
                },
                "tertiaryIpAddress": {
                "properties": {
                "address": {
                "type": "string"
                }
                },
                "type": "object"
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

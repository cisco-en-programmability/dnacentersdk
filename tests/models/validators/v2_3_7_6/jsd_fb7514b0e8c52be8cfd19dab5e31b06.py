# -*- coding: utf-8 -*-
"""Cisco DNA Center GetAccessPointConfigurationV1 data model.

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


class JSONSchemaValidatorFb7514B0E8C52Be8Cfd19Dab5E31B06(object):
    """GetAccessPointConfigurationV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorFb7514B0E8C52Be8Cfd19Dab5E31B06, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "_creationOrderIndex": {
                "type": "number"
                },
                "_isBeingChanged": {
                "type": "boolean"
                },
                "_orderedListOEAssocName": {
                "type": "object"
                },
                "_orderedListOEIndex": {
                "type": "number"
                },
                "adminStatus": {
                "type": "string"
                },
                "apHeight": {
                "type": "number"
                },
                "apMode": {
                "type": "string"
                },
                "apName": {
                "type": "string"
                },
                "authEntityClass": {
                "type": "object"
                },
                "authEntityId": {
                "type": "object"
                },
                "changeLogList": {
                "type": "object"
                },
                "deployPending": {
                "type": "string"
                },
                "displayName": {
                "type": "string"
                },
                "ethMac": {
                "type": "string"
                },
                "failoverPriority": {
                "type": "string"
                },
                "instanceCreatedOn": {
                "type": "object"
                },
                "instanceId": {
                "type": "number"
                },
                "instanceOrigin": {
                "type": "object"
                },
                "instanceTenantId": {
                "type": "string"
                },
                "instanceUpdatedOn": {
                "type": "object"
                },
                "instanceUuid": {
                "type": "object"
                },
                "instanceVersion": {
                "type": "number"
                },
                "internalKey": {
                "properties": {
                "id": {
                "type": "number"
                },
                "longType": {
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "url": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "lazyLoadedEntities": {
                "type": "object"
                },
                "ledBrightnessLevel": {
                "type": "integer"
                },
                "ledStatus": {
                "type": "string"
                },
                "location": {
                "type": "string"
                },
                "macAddress": {
                "type": "string"
                },
                "meshDTOs": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "primaryControllerName": {
                "type": "string"
                },
                "primaryIpAddress": {
                "type": "string"
                },
                "radioDTOs": {
                "items": {
                "properties": {
                "_creationOrderIndex": {
                "type": "number"
                },
                "_isBeingChanged": {
                "type": "boolean"
                },
                "_orderedListOEAssocName": {
                "type": "object"
                },
                "_orderedListOEIndex": {
                "type": "number"
                },
                "adminStatus": {
                "type": "string"
                },
                "antennaAngle": {
                "type": "number"
                },
                "antennaElevAngle": {
                "type": "number"
                },
                "antennaGain": {
                "type": "integer"
                },
                "antennaPatternName": {
                "type": "string"
                },
                "authEntityClass": {
                "type": "object"
                },
                "authEntityId": {
                "type": "object"
                },
                "changeLogList": {
                "type": "object"
                },
                "channelAssignmentMode": {
                "type": "string"
                },
                "channelNumber": {
                "type": "integer"
                },
                "channelWidth": {
                "type": "string"
                },
                "cleanAirSI": {
                "type": "string"
                },
                "deployPending": {
                "type": "string"
                },
                "displayName": {
                "type": "string"
                },
                "ifType": {
                "type": "integer"
                },
                "ifTypeValue": {
                "type": "string"
                },
                "instanceCreatedOn": {
                "type": "object"
                },
                "instanceId": {
                "type": "number"
                },
                "instanceOrigin": {
                "type": "object"
                },
                "instanceTenantId": {
                "type": "string"
                },
                "instanceUpdatedOn": {
                "type": "object"
                },
                "instanceUuid": {
                "type": "object"
                },
                "instanceVersion": {
                "type": "number"
                },
                "internalKey": {
                "properties": {
                "id": {
                "type": "number"
                },
                "longType": {
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "url": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "lazyLoadedEntities": {
                "type": "object"
                },
                "macAddress": {
                "type": "string"
                },
                "powerAssignmentMode": {
                "type": "string"
                },
                "powerlevel": {
                "type": "integer"
                },
                "radioBand": {
                "type": "object"
                },
                "radioRoleAssignment": {
                "type": "object"
                },
                "slotId": {
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
                "type": "string"
                },
                "tertiaryControllerName": {
                "type": "string"
                },
                "tertiaryIpAddress": {
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

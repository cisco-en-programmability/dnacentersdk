# -*- coding: utf-8 -*-
"""Cisco DNA Center GetDiscoveredNetworkDevicesByDiscoveryIdV1 data model.

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


class JSONSchemaValidatorF478B876B38A5Cf094D80Eced531B1A0(object):
    """GetDiscoveredNetworkDevicesByDiscoveryIdV1 request schema
    definition."""

    def __init__(self):
        super(JSONSchemaValidatorF478B876B38A5Cf094D80Eced531B1A0, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "anchorWlcForAp": {
                "type": "string"
                },
                "authModelId": {
                "type": "string"
                },
                "avgUpdateFrequency": {
                "type": "integer"
                },
                "bootDateTime": {
                "type": "string"
                },
                "cliStatus": {
                "type": "string"
                },
                "duplicateDeviceId": {
                "type": "string"
                },
                "errorCode": {
                "type": "string"
                },
                "errorDescription": {
                "type": "string"
                },
                "family": {
                "type": "string"
                },
                "hostname": {
                "type": "string"
                },
                "httpStatus": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "imageName": {
                "type": "string"
                },
                "ingressQueueConfig": {
                "type": "string"
                },
                "interfaceCount": {
                "type": "string"
                },
                "inventoryCollectionStatus": {
                "type": "string"
                },
                "inventoryReachabilityStatus": {
                "type": "string"
                },
                "lastUpdated": {
                "type": "string"
                },
                "lineCardCount": {
                "type": "string"
                },
                "lineCardId": {
                "type": "string"
                },
                "location": {
                "type": "string"
                },
                "locationName": {
                "type": "string"
                },
                "macAddress": {
                "type": "string"
                },
                "managementIpAddress": {
                "type": "string"
                },
                "memorySize": {
                "type": "string"
                },
                "netconfStatus": {
                "type": "string"
                },
                "numUpdates": {
                "type": "integer"
                },
                "pingStatus": {
                "type": "string"
                },
                "platformId": {
                "type": "string"
                },
                "portRange": {
                "type": "string"
                },
                "qosStatus": {
                "type": "string"
                },
                "reachabilityFailureReason": {
                "type": "string"
                },
                "reachabilityStatus": {
                "type": "string"
                },
                "role": {
                "type": "string"
                },
                "roleSource": {
                "type": "string"
                },
                "serialNumber": {
                "type": "string"
                },
                "snmpContact": {
                "type": "string"
                },
                "snmpLocation": {
                "type": "string"
                },
                "snmpStatus": {
                "type": "string"
                },
                "softwareVersion": {
                "type": "string"
                },
                "tag": {
                "type": "string"
                },
                "tagCount": {
                "type": "integer"
                },
                "type": {
                "type": "string"
                },
                "upTime": {
                "type": "string"
                },
                "vendor": {
                "type": "string"
                },
                "wlcApDeviceStatus": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
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

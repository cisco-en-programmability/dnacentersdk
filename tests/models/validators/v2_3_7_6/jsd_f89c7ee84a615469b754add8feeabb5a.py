# -*- coding: utf-8 -*-
"""Cisco DNA Center GetTheDeviceDataForTheGivenDeviceIdUuid data model.

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

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorF89C7Ee84A615469B754Add8Feeabb5A(object):
    """GetTheDeviceDataForTheGivenDeviceIdUuid request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF89C7Ee84A615469B754Add8Feeabb5A, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "aggregateAttributes": {
                "items": {
                "properties": {
                "function": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "value": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "apDetails": {
                "properties": {
                "adminState": {
                "type": "string"
                },
                "apGroup": {
                "type": "string"
                },
                "apOperationalState": {
                "type": "string"
                },
                "apType": {
                "type": "string"
                },
                "connectedTime": {
                "type": "integer"
                },
                "connectedWlcName": {
                "type": "string"
                },
                "ethernetMac": {
                "type": "string"
                },
                "flexGroup": {
                "type": "string"
                },
                "homeApEnabled": {
                "type": "boolean"
                },
                "icapCapability": {
                "type": "string"
                },
                "ledFlashEnabled": {
                "type": "boolean"
                },
                "ledFlashSeconds": {
                "type": "integer"
                },
                "operationalMode": {
                "type": "string"
                },
                "policyTagName": {
                "type": "string"
                },
                "powerCalendarProfile": {
                "type": "string"
                },
                "powerMode": {
                "type": "string"
                },
                "powerProfile": {
                "type": "string"
                },
                "powerSaveMode": {
                "type": "string"
                },
                "powerSaveModeCapable": {
                "type": "string"
                },
                "powerType": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "radios": {
                "items": {
                "properties": {
                "airQuality": {
                "type": "number"
                },
                "band": {
                "type": "string"
                },
                "clientCount": {
                "type": "integer"
                },
                "id": {
                "type": "string"
                },
                "interference": {
                "type": "number"
                },
                "noise": {
                "type": "integer"
                },
                "trafficUtil": {
                "type": "integer"
                },
                "utilization": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "regulatoryDomain": {
                "type": "string"
                },
                "resetReason": {
                "type": "string"
                },
                "rfTagName": {
                "type": "string"
                },
                "siteTagName": {
                "type": "string"
                },
                "subMode": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "clientCount": {
                "type": "integer"
                },
                "collectionStatus": {
                "type": "string"
                },
                "communicationState": {
                "type": "string"
                },
                "deviceFamily": {
                "type": "string"
                },
                "deviceGroupHierarchyId": {
                "type": "string"
                },
                "deviceRole": {
                "type": "string"
                },
                "deviceSeries": {
                "type": "string"
                },
                "deviceType": {
                "type": "string"
                },
                "fabricDetails": {
                "properties": {
                "fabricRole": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "fabricSiteName": {
                "type": "string"
                },
                "transitFabrics": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "featureFlagList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "haLastResetReason": {
                "type": "string"
                },
                "haStatus": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "ipv4Address": {
                "type": "string"
                },
                "ipv6Address": {
                "type": "string"
                },
                "lastBootTime": {
                "type": "integer"
                },
                "macAddress": {
                "type": "string"
                },
                "maintenanceModeEnabled": {
                "type": "boolean"
                },
                "managementIpAddress": {
                "type": "string"
                },
                "metricsDetails": {
                "properties": {
                "airQualityScore": {
                "type": "integer"
                },
                "apCount": {
                "type": "integer"
                },
                "avgTemperature": {
                "type": "number"
                },
                "cpuScore": {
                "type": "integer"
                },
                "cpuUtilization": {
                "type": "number"
                },
                "discardInterfaces": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "discardScore": {
                "type": "integer"
                },
                "errorInterfaces": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "errorScore": {
                "type": "integer"
                },
                "freeMemoryBuffer": {
                "type": "number"
                },
                "freeMemoryBufferScore": {
                "type": "integer"
                },
                "freeTimer": {
                "type": "number"
                },
                "freeTimerScore": {
                "type": "integer"
                },
                "highLinkUtilizationInterfaces": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "interDeviceConnectedDownInterfaces": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "interDeviceLinkScore": {
                "type": "integer"
                },
                "interferenceScore": {
                "type": "integer"
                },
                "linkUtilizationScore": {
                "type": "integer"
                },
                "maxTemperature": {
                "type": "number"
                },
                "memoryScore": {
                "type": "integer"
                },
                "memoryUtilization": {
                "type": "number"
                },
                "noiseScore": {
                "type": "integer"
                },
                "overallFabricScore": {
                "type": "integer"
                },
                "overallHealthScore": {
                "type": "integer"
                },
                "packetPool": {
                "type": "integer"
                },
                "packetPoolScore": {
                "type": "integer"
                },
                "utilizationScore": {
                "type": "integer"
                },
                "wqePool": {
                "type": "integer"
                },
                "wqePoolScore": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "osType": {
                "type": "string"
                },
                "platformId": {
                "type": "string"
                },
                "portCount": {
                "type": "integer"
                },
                "productVendor": {
                "type": "string"
                },
                "redundancyMode": {
                "type": "string"
                },
                "redundancyPeerState": {
                "type": "string"
                },
                "redundancyPeerStateDerived": {
                "type": "string"
                },
                "redundancyState": {
                "type": "string"
                },
                "redundancyStateDerived": {
                "type": "string"
                },
                "ringStatus": {
                "type": "boolean"
                },
                "serialNumber": {
                "type": "string"
                },
                "siteHierarchy": {
                "type": "string"
                },
                "siteHierarchyId": {
                "type": "string"
                },
                "siteId": {
                "type": "string"
                },
                "softwareVersion": {
                "type": "string"
                },
                "stackType": {
                "type": "string"
                },
                "tagNames": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "upTime": {
                "type": "integer"
                },
                "wiredClientCount": {
                "type": "integer"
                },
                "wirelessClientCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "version": {
                "type": "string"
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

# -*- coding: utf-8 -*-
"""Cisco DNA Center GetDeviceDetail data model.

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


class JSONSchemaValidatorC9Ee787Eb5A0391309F45Ddf392Ca(object):
    """GetDeviceDetail request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC9Ee787Eb5A0391309F45Ddf392Ca, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "HALastResetReason": {
                "type": "string"
                },
                "adminState": {
                "type": "string"
                },
                "airQuality": {
                "type": "string"
                },
                "airQualityScore": {
                "type": "integer"
                },
                "apGroup": {
                "type": "string"
                },
                "apType": {
                "type": "string"
                },
                "avgTemperature": {
                "type": "number"
                },
                "collectionStatus": {
                "type": "string"
                },
                "communicationState": {
                "type": "string"
                },
                "connectedTime": {
                "type": "string"
                },
                "connectivityStatus": {
                "type": "integer"
                },
                "cpu": {
                "type": "string"
                },
                "cpuScore": {
                "type": "integer"
                },
                "deviceGroupHierarchyId": {
                "type": "string"
                },
                "deviceSeries": {
                "type": "string"
                },
                "ethernetMac": {
                "type": "string"
                },
                "featureFlagList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "flexGroup": {
                "type": "string"
                },
                "freeMbuf": {
                "type": "number"
                },
                "freeMbufScore": {
                "type": "integer"
                },
                "freeTimer": {
                "type": "number"
                },
                "freeTimerScore": {
                "type": "integer"
                },
                "haStatus": {
                "type": "string"
                },
                "homeApEnabled": {
                "type": "string"
                },
                "icapCapability": {
                "type": "string"
                },
                "interference": {
                "type": "string"
                },
                "interferenceScore": {
                "type": "integer"
                },
                "ipV4Addr": {
                "type": "string"
                },
                "ipV6Addr": {
                "type": "string"
                },
                "ip_addr_managementIpAddr": {
                "type": "string"
                },
                "lastBootTime": {
                "type": "number"
                },
                "ledFlashEnabled": {
                "type": "string"
                },
                "ledFlashSeconds": {
                "type": "string"
                },
                "location": {
                "type": "string"
                },
                "macAddress": {
                "type": "string"
                },
                "maintenanceMode": {
                "type": "boolean"
                },
                "managementIpAddr": {
                "type": "string"
                },
                "maxTemperature": {
                "type": "number"
                },
                "memory": {
                "type": "string"
                },
                "memoryScore": {
                "type": "integer"
                },
                "mode": {
                "type": "string"
                },
                "noise": {
                "type": "string"
                },
                "noiseScore": {
                "type": "integer"
                },
                "nwDeviceFamily": {
                "type": "string"
                },
                "nwDeviceId": {
                "type": "string"
                },
                "nwDeviceName": {
                "type": "string"
                },
                "nwDeviceRole": {
                "type": "string"
                },
                "nwDeviceType": {
                "type": "string"
                },
                "opState": {
                "type": "string"
                },
                "osType": {
                "type": "string"
                },
                "overallHealth": {
                "type": "integer"
                },
                "packetPool": {
                "type": "number"
                },
                "packetPoolScore": {
                "type": "integer"
                },
                "platformId": {
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
                "regulatoryDomain": {
                "type": "string"
                },
                "resetReason": {
                "type": "string"
                },
                "rfTagName": {
                "type": "string"
                },
                "ringStatus": {
                "type": "boolean"
                },
                "serialNumber": {
                "type": "string"
                },
                "siteHierarchyGraphId": {
                "type": "string"
                },
                "siteTagName": {
                "type": "string"
                },
                "softwareVersion": {
                "type": "string"
                },
                "stackType": {
                "type": "string"
                },
                "subMode": {
                "type": "string"
                },
                "tagIdList": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "timestamp": {
                "type": "integer"
                },
                "upTime": {
                "type": "string"
                },
                "utilization": {
                "type": "string"
                },
                "utilizationScore": {
                "type": "integer"
                },
                "version": {
                "type": "string"
                },
                "wqe": {
                "type": "number"
                },
                "wqeScore": {
                "type": "integer"
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

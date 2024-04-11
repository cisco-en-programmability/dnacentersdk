# -*- coding: utf-8 -*-
"""Cisco DNA Center getUserEnrichmentDetails data model.

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


class JSONSchemaValidatorF9C1D861A051B4A4928F2E6D84B2E3(object):
    """getUserEnrichmentDetails request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF9C1D861A051B4A4928F2E6D84B2E3, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "connectedDevice": {
                "items": {
                "properties": {
                "deviceDetails": {
                "properties": {
                "apManagerInterfaceIp": {
                "type": "string"
                },
                "associatedWlcIp": {
                "type": "string"
                },
                "bootDateTime": {
                "type": "string"
                },
                "collectionInterval": {
                "type": "string"
                },
                "collectionStatus": {
                "type": "string"
                },
                "errorCode": {
                "type": "object"
                },
                "errorDescription": {
                "type": "object"
                },
                "family": {
                "type": "string"
                },
                "hostname": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instanceUuid": {
                "type": "string"
                },
                "interfaceCount": {
                "type": "string"
                },
                "inventoryStatusDetail": {
                "type": "string"
                },
                "lastUpdateTime": {
                "type": "integer"
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
                "type": "object"
                },
                "locationName": {
                "type": "object"
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
                "neighborTopology": {
                "items": {
                "properties": {
                "detail": {
                "type": "string"
                },
                "errorCode": {
                "type": "integer"
                },
                "message": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "platformId": {
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
                "series": {
                "type": "string"
                },
                "snmpContact": {
                "type": "string"
                },
                "snmpLocation": {
                "type": "string"
                },
                "softwareVersion": {
                "type": "string"
                },
                "tagCount": {
                "type": "string"
                },
                "tunnelUdpPort": {
                "type": "object"
                },
                "type": {
                "type": "string"
                },
                "upTime": {
                "type": "string"
                },
                "waasDeviceMode": {
                "type": "object"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "userDetails": {
                "properties": {
                "apGroup": {
                "type": "object"
                },
                "authType": {
                "type": "object"
                },
                "avgRssi": {
                "type": "object"
                },
                "avgSnr": {
                "type": "object"
                },
                "channel": {
                "type": "object"
                },
                "clientConnection": {
                "type": "string"
                },
                "connectedDevice": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "connectionStatus": {
                "type": "string"
                },
                "dataRate": {
                "type": "object"
                },
                "dnsFailure": {
                "type": "object"
                },
                "dnsSuccess": {
                "type": "object"
                },
                "frequency": {
                "type": "object"
                },
                "healthScore": {
                "items": {
                "properties": {
                "healthType": {
                "type": "string"
                },
                "reason": {
                "type": "string"
                },
                "score": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "hostIpV4": {
                "type": "string"
                },
                "hostIpV6": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "hostMac": {
                "type": "string"
                },
                "hostName": {
                "type": "object"
                },
                "hostOs": {
                "type": "object"
                },
                "hostType": {
                "type": "string"
                },
                "hostVersion": {
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "issueCount": {
                "type": "number"
                },
                "lastUpdated": {
                "type": "integer"
                },
                "location": {
                "type": "object"
                },
                "onboarding": {
                "properties": {
                "aaaServerIp": {
                "type": "object"
                },
                "averageAssocDuration": {
                "type": "object"
                },
                "averageAuthDuration": {
                "type": "object"
                },
                "averageDhcpDuration": {
                "type": "object"
                },
                "averageRunDuration": {
                "type": "object"
                },
                "dhcpServerIp": {
                "type": "object"
                },
                "maxAssocDuration": {
                "type": "object"
                },
                "maxAuthDuration": {
                "type": "object"
                },
                "maxDhcpDuration": {
                "type": "object"
                },
                "maxRunDuration": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "onboardingTime": {
                "type": "object"
                },
                "port": {
                "type": "object"
                },
                "rssi": {
                "type": "object"
                },
                "rxBytes": {
                "type": "object"
                },
                "snr": {
                "type": "object"
                },
                "ssid": {
                "type": "object"
                },
                "subType": {
                "type": "string"
                },
                "txBytes": {
                "type": "object"
                },
                "userId": {
                "type": "object"
                },
                "vlanId": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )

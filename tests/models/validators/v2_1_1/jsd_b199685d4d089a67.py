# -*- coding: utf-8 -*-
"""Cisco DNA Center Get Client Enrichment Details data model.

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


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
import json
from dnacentersdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidatorB199685D4D089A67(object):
    """Get Client Enrichment Details request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorB199685D4D089A67, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "items": {
                "properties": {
                "connectedDevice": {
                "items": {
                "properties": {
                "deviceDetails": {
                "properties": {
                "apManagerInterfaceIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "associatedWlcIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "bootDateTime": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "cisco360view": {
                "type": [
                "string",
                "null"
                ]
                },
                "collectionInterval": {
                "type": [
                "string",
                "null"
                ]
                },
                "collectionStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "errorCode": {
                "type": [
                "string",
                "null"
                ]
                },
                "errorDescription": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "family": {
                "type": [
                "string",
                "null"
                ]
                },
                "hostname": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceCount": {
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "inventoryStatusDetail": {
                "type": [
                "string",
                "null"
                ]
                },
                "lastUpdateTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "lastUpdated": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "lineCardCount": {
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "lineCardId": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "location": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "locationName": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "macAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "managementIpAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "memorySize": {
                "type": [
                "string",
                "null"
                ]
                },
                "neighborTopology": {
                "items": {
                "properties": {
                "links": {
                "items": {
                "properties": {
                "id": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "label": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "linkStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "portUtilization": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "source": {
                "type": [
                "string",
                "null"
                ]
                },
                "target": {
                "type": [
                "string",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "nodes": {
                "items": {
                "properties": {
                "clients": {
                "type": [
                "number",
                "null"
                ]
                },
                "count": {
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "description":
                 {
                "type": [
                "string",
                "null"
                ]
                },
                "deviceType": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "fabricGroup": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "family": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "healthScore": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "ip": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "level": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "nodeType": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "platformId": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "radioFrequency": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "role": {
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "userId": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "platformId": {
                "type": [
                "string",
                "null"
                ]
                },
                "reachabilityFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "reachabilityStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "role": {
                "type": [
                "string",
                "null"
                ]
                },
                "roleSource": {
                "type": [
                "string",
                "null"
                ]
                },
                "serialNumber": {
                "type": [
                "string",
                "null"
                ]
                },
                "series": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpContact": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpLocation": {
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "type": [
                "string",
                "null"
                ]
                },
                "tagCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "tunnelUdpPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "type": [
                "string",
                "null"
                ]
                },
                "upTime": {
                "type": [
                "string",
                "null"
                ]
                },
                "waasDeviceMode": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "issueDetails": {
                "properties": {
                "issue": {
                "items": {
                "properties": {
                "impactedHosts": {
                "items": {
                "properties": {
                "connectedInterface": {
                "type": [
                "string",
                "null"
                ]
                },
                "failedAttempts": {
                "type": [
                "number",
                "null"
                ]
                },
                "hostName": {
                "type": [
                "string",
                "null"
                ]
                },
                "hostOs": {
                "type": [
                "string",
                "null"
                ]
                },
                "hostType": {
                "type": [
                "string",
                "null"
                ]
                },
                "location": {
                "properties": {
                "apsImpacted": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "area": {
                "type": [
                "string",
                "null"
                ]
                },
                "building": {
                "type": [
                "string",
                "null"
                ]
                },
                "floor": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "siteId": {
                "type": [
                "string",
                "null"
                ]
                },
                "siteType": {
                "type": [
                "string",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "macAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "ssid": {
                "type": [
                "string",
                "null"
                ]
                },
                "timestamp": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "issueCategory": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueDescription": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueEntity": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueEntityValue": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "issueId": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueName": {
                "type": [
                "string",
                "null"
                ]
                },
                "issuePriority": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueSeverity": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueSource": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueSummary": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueTimestamp": {
                "type": [
                "number",
                "null"
                ]
                },
                "suggestedActions": {
                "items": {
                "properties": {
                "message": {
                "type": [
                "string",
                "null"
                ]
                },
                "steps": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "userDetails": {
                "properties": {
                "authType": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "clientConnection": {
                "type": [
                "string",
                "null"
                ]
                },
                "connectedDevice": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "connectionStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataRate": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "healthScore": {
                "items": {
                "properties": {
                "healthType": {
                "type": [
                "string",
                "null"
                ]
                },
                "reason": {
                "type": [
                "string",
                "null"
                ]
                },
                "score": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "hostIpV4": {
                "type": [
                "string",
                "null"
                ]
                },
                "hostIpV6": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "hostMac": {
                "type": [
                "string",
                "null"
                ]
                },
                "hostName": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "hostOs": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "hostType": {
                "type": [
                "string",
                "null"
                ]
                },
                "hostVersion": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "lastUpdated": {
                "type": [
                "number",
                "null"
                ]
                },
                "location": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "port": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "rssi": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "snr": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "ssid": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "subType": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "userId": {
                "type": [
                "string",
                "null"
                ]
                },
                "vlanId": {
                "type": [
                "string",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
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

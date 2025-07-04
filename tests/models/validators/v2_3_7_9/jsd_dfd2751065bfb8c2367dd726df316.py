# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetClientEnrichmentDetailsV1 data model.

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


class JSONSchemaValidatorDfd2751065Bfb8C2367Dd726Df316(object):
    """GetClientEnrichmentDetailsV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorDfd2751065Bfb8C2367Dd726Df316, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
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
                "type": "object"
                },
                "cisco360view": {
                "type": "string"
                },
                "collectionInterval": {
                "type": "string"
                },
                "collectionStatus": {
                "type": "string"
                },
                "errorCode": {
                "type": "string"
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
                "type": "object"
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
                "type": "object"
                },
                "lineCardId": {
                "type": "object"
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
                "links": {
                "items": {
                "properties": {
                "id": {
                "type": "object"
                },
                "label": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "linkStatus": {
                "type": "string"
                },
                "portUtilization": {
                "type": "object"
                },
                "source": {
                "type": "string"
                },
                "target": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "nodes": {
                "items": {
                "properties": {
                "clients": {
                "type": "number"
                },
                "count": {
                "type": "object"
                },
                "description":
                 {
                "type": "string"
                },
                "deviceType": {
                "type": "object"
                },
                "fabricGroup": {
                "type": "object"
                },
                "family": {
                "type": "object"
                },
                "healthScore": {
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "ip": {
                "type": "object"
                },
                "level": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "nodeType": {
                "type": "object"
                },
                "platformId": {
                "type": "object"
                },
                "radioFrequency": {
                "type": "object"
                },
                "role": {
                "type": "string"
                },
                "softwareVersion": {
                "type": "object"
                },
                "userId": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "type": "string"
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
                "issueDetails": {
                "properties": {
                "issue": {
                "items": {
                "properties": {
                "impactedHosts": {
                "items": {
                "properties": {
                "connectedInterface": {
                "type": "string"
                },
                "failedAttempts": {
                "type": "integer"
                },
                "hostName": {
                "type": "string"
                },
                "hostOs": {
                "type": "string"
                },
                "hostType": {
                "type": "string"
                },
                "location": {
                "properties": {
                "apsImpacted": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "area": {
                "type": "string"
                },
                "building": {
                "type": "string"
                },
                "floor": {
                "type": "object"
                },
                "siteId": {
                "type": "string"
                },
                "siteType": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "macAddress": {
                "type": "string"
                },
                "ssid": {
                "type": "string"
                },
                "timestamp": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "issueCategory": {
                "type": "string"
                },
                "issueDescription": {
                "type": "string"
                },
                "issueEntity": {
                "type": "string"
                },
                "issueEntityValue": {
                "type": "string"
                },
                "issueId": {
                "type": "string"
                },
                "issueName": {
                "type": "string"
                },
                "issuePriority": {
                "type": "string"
                },
                "issueSeverity": {
                "type": "string"
                },
                "issueSource": {
                "type": "string"
                },
                "issueSummary": {
                "type": "string"
                },
                "issueTimestamp": {
                "type": "integer"
                },
                "suggestedActions": {
                "items": {
                "properties": {
                "message": {
                "type": "string"
                },
                "steps": {
                "items": {
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "userDetails": {
                "properties": {
                "authType": {
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
                "port": {
                "type": "object"
                },
                "rssi": {
                "type": "object"
                },
                "snr": {
                "type": "object"
                },
                "ssid": {
                "type": "object"
                },
                "subType": {
                "type": "object"
                },
                "userId": {
                "type": "string"
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

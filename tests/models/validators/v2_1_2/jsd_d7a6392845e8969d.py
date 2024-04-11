# -*- coding: utf-8 -*-
"""Cisco DNA Center Get User Enrichment Details data model.

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


class JSONSchemaValidatorD7A6392845E8969D(object):
    """Get User Enrichment Details request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD7A6392845E8969D, self).__init__()
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
                "properties": {},
                "type": [
                "object",
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
                "type": [
                "string",
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
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "lineCardId": {
                "type": [
                "string",
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
                "detail": {
                "type": [
                "string",
                "null"
                ]
                },
                "errorCode": {
                "type": [
                "number",
                "null"
                ]
                },
                "message": {
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
                "properties": {},
                "type": [
                "object",
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
                "userDetails": {
                "properties": {
                "apGroup": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "authType": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "avgRssi": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "avgSnr": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "channel": {
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
                "dnsFailure": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "dnsSuccess": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "frequency": {
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
                "onboarding": {
                "properties": {
                "aaaServerIp": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "averageAssocDuration": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "averageAuthDuration": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "averageDhcpDuration": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "averageRunDuration": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "dhcpServerIp": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "maxAssocDuration": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "maxAuthDuration": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "maxDhcpDuration": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "maxRunDuration": {
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
                "onboardingTime": {
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
                "rxBytes": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "txBytes": {
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

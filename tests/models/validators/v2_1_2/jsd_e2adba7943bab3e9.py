# -*- coding: utf-8 -*-
"""Cisco DNA Center Get Client Detail data model.

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


class JSONSchemaValidatorE2AdBa7943BaB3E9(object):
    """Get Client Detail request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE2AdBa7943BaB3E9, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "connectionInfo": {
                "properties": {
                "band": {
                "type": [
                "string",
                "null"
                ]
                },
                "channel": {
                "type": [
                "string",
                "null"
                ]
                },
                "channelWidth": {
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
                "nwDeviceMac": {
                "type": [
                "string",
                "null"
                ]
                },
                "nwDeviceName": {
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "spatialStream": {
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
                },
                "uapsd": {
                "type": [
                "string",
                "null"
                ]
                },
                "wmm": {
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
                "detail": {
                "properties": {
                "apGroup": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "authType": {
                "type": [
                "string",
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
                "type": [
                "string",
                "null"
                ]
                },
                "clientConnection": {
                "type": [
                "string",
                "null"
                ]
                },
                "clientType": {
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
                "type": [
                "string",
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
                "type": [
                "string",
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
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
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
                "type": [
                "string",
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
                "iosCapable": {
                "type": [
                "boolean",
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
                "aaaRootcauseList": {
                "items": {
                "type": [
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "aaaServerIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "assocDoneTime": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "assocRootcauseList": {
                "items": {
                "type": [
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "authDoneTime": {
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
                "dhcpDoneTime": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "dhcpRootcauseList": {
                "items": {
                "type": [
                "object"
                ]
                },
                "type": [
                "array",
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
                },
                "otherRootcauseList": {
                "items": {
                "type": [
                "object"
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
                "type": [
                "string",
                "null"
                ]
                },
                "rxBytes": {
                "type": [
                "string",
                "null"
                ]
                },
                "snr": {
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
                "subType": {
                "type": [
                "string",
                "null"
                ]
                },
                "txBytes": {
                "type": [
                "string",
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
                },
                "vnid": {
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
                "topology": {
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
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
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
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "connectedDevice": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "count": {
                "properties": {},
                "type": [
                "object",
                "null"
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
                "type": [
                "string",
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
                "type": [
                "number",
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
                "type": [
                "string",
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
                "type": [
                "string",
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

# -*- coding: utf-8 -*-
"""DNA Center Get Client Detail data model.

Copyright (c) 2019 Cisco and/or its affiliates.

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


class JSONSchemaValidatorE2AdBa7943BaB3E9(object):
    """Get Client Detail request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE2AdBa7943BaB3E9, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "connectionInfo": {
                "description":
                "Connection Info",
                "properties": {
                "band": {
                "description":
                "Band",
                "type": [
                "string",
                "null"
                ]
                },
                "channel": {
                "description":
                "Channel",
                "type": [
                "string",
                "null"
                ]
                },
                "channelWidth": {
                "description":
                "Channel Width",
                "type": [
                "string",
                "null"
                ]
                },
                "hostType": {
                "description":
                "Host Type",
                "type": [
                "string",
                "null"
                ]
                },
                "nwDeviceMac": {
                "description":
                "Nw Device Mac",
                "type": [
                "string",
                "null"
                ]
                },
                "nwDeviceName": {
                "description":
                "Nw Device Name",
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                "Protocol",
                "type": [
                "string",
                "null"
                ]
                },
                "spatialStream": {
                "description":
                "Spatial Stream",
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
                "description":
                "Uapsd",
                "type": [
                "string",
                "null"
                ]
                },
                "wmm": {
                "description":
                "Wmm",
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
                "description":
                "Detail",
                "properties": {
                "apGroup": {
                "description":
                "Ap Group",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "authType": {
                "description":
                "Auth Type",
                "type": [
                "string",
                "null"
                ]
                },
                "avgRssi": {
                "description":
                "Avg Rssi",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "avgSnr": {
                "description":
                "Avg Snr",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "channel": {
                "description":
                "Channel",
                "type": [
                "string",
                "null"
                ]
                },
                "clientConnection": {
                "description":
                "Client Connection",
                "type": [
                "string",
                "null"
                ]
                },
                "clientType": {
                "description":
                "Client Type",
                "type": [
                "string",
                "null"
                ]
                },
                "connectedDevice": {
                "description":
                "Connected Device",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "connectionStatus": {
                "description":
                "Connection Status",
                "type": [
                "string",
                "null"
                ]
                },
                "dataRate": {
                "description":
                "Data Rate",
                "type": [
                "string",
                "null"
                ]
                },
                "dnsFailure": {
                "description":
                "Dns Failure",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "dnsSuccess": {
                "description":
                "Dns Success",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "frequency": {
                "description":
                "Frequency",
                "type": [
                "string",
                "null"
                ]
                },
                "healthScore": {
                "description":
                "Health Score",
                "items": {
                "properties": {
                "healthType": {
                "description":
                "Health Type",
                "type": [
                "string",
                "null"
                ]
                },
                "reason": {
                "description":
                "Reason",
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
                "description":
                "Host Ip V4",
                "type": [
                "string",
                "null"
                ]
                },
                "hostIpV6": {
                "description":
                "Host Ip V6",
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
                "description":
                "Host Mac",
                "type": [
                "string",
                "null"
                ]
                },
                "hostName": {
                "description":
                "Host Name",
                "type": [
                "string",
                "null"
                ]
                },
                "hostOs": {
                "description":
                "Host Os",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "hostType": {
                "description":
                "Host Type",
                "type": [
                "string",
                "null"
                ]
                },
                "hostVersion": {
                "description":
                "Host Version",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "id": {
                "description":
                "Id",
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
                "description":
                "Location",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "onboarding": {
                "description":
                "Onboarding",
                "properties": {
                "aaaRootcauseList": {
                "description":
                "Aaa Rootcause List",
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
                "description":
                "Aaa Server Ip",
                "type": [
                "string",
                "null"
                ]
                },
                "assocDoneTime": {
                "description":
                "Assoc Done Time",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "assocRootcauseList": {
                "description":
                "Assoc Rootcause List",
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
                "description":
                "Auth Done Time",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "averageAssocDuration": {
                "description":
                "Average Assoc Duration",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "averageAuthDuration": {
                "description":
                "Average Auth Duration",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "averageDhcpDuration": {
                "description":
                "Average Dhcp Duration",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "averageRunDuration": {
                "description":
                "Average Run Duration",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "dhcpDoneTime": {
                "description":
                "Dhcp Done Time",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "dhcpRootcauseList": {
                "description":
                "Dhcp Rootcause List",
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
                "description":
                "Dhcp Server Ip",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "maxAssocDuration": {
                "description":
                "Max Assoc Duration",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "maxAuthDuration": {
                "description":
                "Max Auth Duration",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "maxDhcpDuration": {
                "description":
                "Max Dhcp Duration",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "maxRunDuration": {
                "description":
                "Max Run Duration",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "otherRootcauseList": {
                "description":
                "Other Rootcause List",
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
                "description":
                "Onboarding Time",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "port": {
                "description":
                "Port",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "rssi": {
                "description":
                "Rssi",
                "type": [
                "string",
                "null"
                ]
                },
                "rxBytes": {
                "description":
                "Rx Bytes",
                "type": [
                "string",
                "null"
                ]
                },
                "snr": {
                "description":
                "Snr",
                "type": [
                "string",
                "null"
                ]
                },
                "ssid": {
                "description":
                "Ssid",
                "type": [
                "string",
                "null"
                ]
                },
                "subType": {
                "description":
                "Sub Type",
                "type": [
                "string",
                "null"
                ]
                },
                "txBytes": {
                "description":
                "Tx Bytes",
                "type": [
                "string",
                "null"
                ]
                },
                "userId": {
                "description":
                "User Id",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "vlanId": {
                "description":
                "Vlan Id",
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
                "description":
                "Vnid",
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
                "description":
                "Topology",
                "properties": {
                "links": {
                "description":
                "Links",
                "items": {
                "properties": {
                "id": {
                "description":
                "Id",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "label": {
                "description":
                "Label",
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
                "description":
                "Link Status",
                "type": [
                "string",
                "null"
                ]
                },
                "portUtilization": {
                "description":
                "Port Utilization",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "source": {
                "description":
                "Source",
                "type": [
                "string",
                "null"
                ]
                },
                "target": {
                "description":
                "Target",
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
                "description":
                "Nodes",
                "items": {
                "properties": {
                "clients": {
                "description":
                "Clients",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "connectedDevice": {
                "description":
                "Connected Device",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "count": {
                "description":
                "Count",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "description":
                 {
                "description":
                "Description",
                "type": [
                "string",
                "null"
                ]
                },
                "deviceType": {
                "description":
                "Device Type",
                "type": [
                "string",
                "null"
                ]
                },
                "fabricGroup": {
                "description":
                "Fabric Group",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "family": {
                "description":
                "Family",
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
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "ip": {
                "description":
                "Ip",
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
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "nodeType": {
                "description":
                "Node Type",
                "type": [
                "string",
                "null"
                ]
                },
                "platformId": {
                "description":
                "Platform Id",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "radioFrequency": {
                "description":
                "Radio Frequency",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "role": {
                "description":
                "Role",
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "description":
                "Software Version",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "userId": {
                "description":
                "User Id",
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

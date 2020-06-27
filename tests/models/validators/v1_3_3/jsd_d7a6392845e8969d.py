# -*- coding: utf-8 -*-
"""DNA Center Get User Enrichment Details data model.

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


class JSONSchemaValidatorD7A6392845E8969D(object):
    """Get User Enrichment Details request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD7A6392845E8969D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "items": {
                "properties": {
                "connectedDevice": {
                "description":
                "Connected Device",
                "items": {
                "properties": {
                "deviceDetails": {
                "description":
                "Device Details",
                "properties": {
                "apManagerInterfaceIp": {
                "description":
                "Ap Manager Interface Ip",
                "type": [
                "string",
                "null"
                ]
                },
                "associatedWlcIp": {
                "description":
                "Associated Wlc Ip",
                "type": [
                "string",
                "null"
                ]
                },
                "bootDateTime": {
                "description":
                "Boot Date Time",
                "type": [
                "string",
                "null"
                ]
                },
                "collectionInterval": {
                "description":
                "Collection Interval",
                "type": [
                "string",
                "null"
                ]
                },
                "collectionStatus": {
                "description":
                "Collection Status",
                "type": [
                "string",
                "null"
                ]
                },
                "errorCode": {
                "description":
                "Error Code",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "errorDescription": {
                "description":
                "Error Description",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "family": {
                "description":
                "Family",
                "type": [
                "string",
                "null"
                ]
                },
                "hostname": {
                "description":
                "Hostname",
                "type": [
                "string",
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
                "instanceUuid": {
                "description":
                "Instance Uuid",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceCount": {
                "description":
                "Interface Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "inventoryStatusDetail": {
                "description":
                "Inventory Status Detail",
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
                "description":
                "Last Updated",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "lineCardCount": {
                "description":
                "Line Card Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "lineCardId": {
                "description":
                "Line Card Id",
                "type": [
                "string",
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
                "locationName": {
                "description":
                "Location Name",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "macAddress": {
                "description":
                "Mac Address",
                "type": [
                "string",
                "null"
                ]
                },
                "managementIpAddress": {
                "description":
                "Management Ip Address",
                "type": [
                "string",
                "null"
                ]
                },
                "memorySize": {
                "description":
                "Memory Size",
                "type": [
                "string",
                "null"
                ]
                },
                "neighborTopology": {
                "description":
                "Neighbor Topology",
                "items": {
                "properties": {
                "detail": {
                "description":
                "Detail",
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
                "description":
                "Message",
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
                "description":
                "Platform Id",
                "type": [
                "string",
                "null"
                ]
                },
                "reachabilityFailureReason": {
                "description":
                "Reachability Failure Reason",
                "type": [
                "string",
                "null"
                ]
                },
                "reachabilityStatus": {
                "description":
                "Reachability Status",
                "type": [
                "string",
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
                "roleSource": {
                "description":
                "Role Source",
                "type": [
                "string",
                "null"
                ]
                },
                "serialNumber": {
                "description":
                "Serial Number",
                "type": [
                "string",
                "null"
                ]
                },
                "series": {
                "description":
                "Series",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpContact": {
                "description":
                "Snmp Contact",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpLocation": {
                "description":
                "Snmp Location",
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "description":
                "Software Version",
                "type": [
                "string",
                "null"
                ]
                },
                "tagCount": {
                "description":
                "Tag Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "tunnelUdpPort": {
                "description":
                "Tunnel Udp Port",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "type": {
                "description":
                "Type",
                "type": [
                "string",
                "null"
                ]
                },
                "upTime": {
                "description":
                "Up Time",
                "type": [
                "string",
                "null"
                ]
                },
                "waasDeviceMode": {
                "description":
                "Waas Device Mode",
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
                "description":
                "User Details",
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
                "properties": {},
                "type": [
                "object",
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
                "properties": {},
                "type": [
                "object",
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
                "properties": {},
                "type": [
                "object",
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
                "properties": {},
                "type": [
                "object",
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
                "items": {},
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
                "properties": {},
                "type": [
                "object",
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
                "aaaServerIp": {
                "description":
                "Aaa Server Ip",
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
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "rxBytes": {
                "description":
                "Rx Bytes",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "snr": {
                "description":
                "Snr",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "ssid": {
                "description":
                "Ssid",
                "properties": {},
                "type": [
                "object",
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
                },
                "vlanId": {
                "description":
                "Vlan Id",
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

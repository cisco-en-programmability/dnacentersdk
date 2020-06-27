# -*- coding: utf-8 -*-
"""DNA Center Get Device Enrichment Details data model.

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


class JSONSchemaValidatorE0B5599B4F2997B7(object):
    """Get Device Enrichment Details request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE0B5599B4F2997B7, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
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
                "type": [
                "string",
                "null"
                ]
                },
                "errorDescription": {
                "description":
                "Error Description",
                "type": [
                "string",
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
                "items": {},
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
                "type": [
                "string",
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
                "type": [
                "string",
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

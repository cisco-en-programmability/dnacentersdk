# -*- coding: utf-8 -*-
"""Cisco DNA Center Get Device Enrichment Details data model.

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


class JSONSchemaValidatorE0B5599B4F2997B7(object):
    """Get Device Enrichment Details request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE0B5599B4F2997B7, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
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
                "type": [
                "string",
                "null"
                ]
                },
                "errorDescription": {
                "type": [
                "string",
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
                "type": [
                "string",
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

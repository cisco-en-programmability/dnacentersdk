# -*- coding: utf-8 -*-
"""Cisco DNA Center Get Device by ID data model.

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


class JSONSchemaValidator8Fa8Eb404A4A8D96(object):
    """Get Device by ID request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator8Fa8Eb404A4A8D96, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
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
                "instanceTenantId": {
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
                "string",
                "null",
                "number"
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
                "type": [
                "string",
                "null"
                ]
                },
                "locationName": {
                "type": [
                "string",
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
                "softwareType": {
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
                "version": {
                "type": [
                "string",
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

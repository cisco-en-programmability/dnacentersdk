# -*- coding: utf-8 -*-
"""DNA Center Get Network Device by pagination range data model.

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


class JSONSchemaValidatorF49548C54Be8A3E2(object):
    """Get Network Device by pagination range request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF49548C54Be8A3E2, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "description":
                 "",
                "items": {
                "properties": {
                "apManagerInterfaceIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "associatedWlcIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "bootDateTime": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "collectionInterval": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "collectionStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "errorCode": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "errorDescription": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "family": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "hostname": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceCount": {
                "description":
                 "",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "inventoryStatusDetail": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "lastUpdateTime": {
                "description":
                 "",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "lastUpdated": {
                "description":
                 "",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "lineCardCount": {
                "description":
                 "",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "lineCardId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "location": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "locationName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "macAddress": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "managementIpAddress": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "memorySize": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "platformId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "reachabilityFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "reachabilityStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "role": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "roleSource": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "serialNumber": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "series": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpContact": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpLocation": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "softwareType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "tagCount": {
                "description":
                 "",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "tunnelUdpPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "upTime": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "waasDeviceMode": {
                "description":
                 "",
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
                "null",
                "object"
                ]
                },
                "version": {
                "description":
                 "",
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

# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetDeviceByID data model.

Copyright (c) 2025 Cisco Systems.

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

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorD86F657F8592F97014D2Ebf8D37Ac(object):
    """GetDeviceByID request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD86F657F8592F97014D2Ebf8D37Ac, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "apEthernetMacAddress": {
                "type": "string"
                },
                "apManagerInterfaceIp": {
                "type": "string"
                },
                "associatedWlcIp": {
                "type": "string"
                },
                "bootDateTime": {
                "type": "string"
                },
                "collectionInterval": {
                "type": "string"
                },
                "collectionStatus": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "deviceSupportLevel": {
                "type": "string"
                },
                "dnsResolvedManagementAddress": {
                "type": "string"
                },
                "errorCode": {
                "type": "string"
                },
                "errorDescription": {
                "type": "string"
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
                "instanceTenantId": {
                "type": "string"
                },
                "instanceUuid": {
                "type": "string"
                },
                "interfaceCount": {
                "type": "string"
                },
                "inventoryStatusDetail": {
                "type": "string"
                },
                "lastDeviceResyncStartTime": {
                "type": "string"
                },
                "lastUpdateTime": {
                "type": "number"
                },
                "lastUpdated": {
                "type": "string"
                },
                "lineCardCount": {
                "type": "string"
                },
                "lineCardId": {
                "type": "string"
                },
                "location": {
                "type": "string"
                },
                "locationName": {
                "type": "string"
                },
                "macAddress": {
                "type": "string"
                },
                "managedAtleastOnce": {
                "type": "boolean"
                },
                "managementIpAddress": {
                "type": "string"
                },
                "managementState": {
                "type": "string"
                },
                "memorySize": {
                "type": "string"
                },
                "pendingSyncRequestsCount": {
                "type": "string"
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
                "reasonsForDeviceResync": {
                "type": "string"
                },
                "reasonsForPendingSyncRequests": {
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
                "softwareType": {
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
                "uptimeSeconds": {
                "type": "number"
                },
                "vendor": {
                "type": "string"
                },
                "waasDeviceMode": {
                "type": "string"
                }
                },
                "required": [
                "collectionStatus",
                "family",
                "hostname",
                "id",
                "instanceTenantId",
                "instanceUuid",
                "interfaceCount",
                "inventoryStatusDetail",
                "lastUpdateTime",
                "lastUpdated",
                "lineCardCount",
                "lineCardId",
                "macAddress",
                "managementIpAddress",
                "memorySize",
                "platformId",
                "reachabilityStatus",
                "role",
                "serialNumber",
                "series",
                "softwareType",
                "softwareVersion",
                "tagCount",
                "type",
                "upTime",
                "waasDeviceMode",
                "dnsResolvedManagementAddress",
                "apEthernetMacAddress",
                "vendor",
                "reasonsForPendingSyncRequests",
                "pendingSyncRequestsCount",
                "reasonsForDeviceResync",
                "lastDeviceResyncStartTime",
                "uptimeSeconds",
                "managementState"
                ],
                "type": "object"
                },
                "version": {
                "type": "string"
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

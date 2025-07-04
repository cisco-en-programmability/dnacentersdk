# -*- coding: utf-8 -*-
"""Cisco Catalyst Center QueryNetworkDevicesWithFiltersV1 data model.

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


class JSONSchemaValidatorFff3662537E538F82BfB5809E30B3Df(object):
    """QueryNetworkDevicesWithFiltersV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorFff3662537E538F82BfB5809E30B3Df, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "apEthernetMacAddress": {
                "type": "string"
                },
                "apManagerInterfaceIpAddress": {
                "type": "string"
                },
                "apWlcIpAddress": {
                "type": "string"
                },
                "bootTime": {
                "type": "number"
                },
                "deviceSupportLevel": {
                "enum": [
                "SUPPORTED",
                "LIMITED",
                "THIRD_PARTY",
                "UNSUPPORTED"
                ],
                "type": "string"
                },
                "dnsResolvedManagementIpAddress": {
                "type": "string"
                },
                "errorCode": {
                "enum": [
                "UNREACHABLE",
                "ONLY_PING_REACHABLE",
                "CREDENTIAL_MISSING",
                "SNMP_TIMEOUT",
                "SNMP_AUTH_ERROR",
                "SNMP_UNSUPPORTED_AUTH",
                "SNMP_UNSUPPORTED_PRIV",
                "SNMP_DES_DEPRECATED",
                "SNMP_UNSUPPORTED_SECURITY_LEVEL",
                "SNMP_SPARSE_ERROR",
                "SNMP_FAILED",
                "CLI_TIMEOUT",
                "CLI_CONNECTION_CLOSED",
                "CLI_CONNECTION_ERROR",
                "CLI_AUTH_ERROR",
                "CLI_MISSING_ENABLE_PASSWORD",
                "CLI_INCORRECT_ENABLE_PASSWORD",
                "NETCONF_CONNECTION_ERROR",
                "NETCONF_AUTH_ERROR",
                "NETCONF_PORT_MISSING",
                "NETCONF_ACCESS_DENIED",
                "NETCONF_RPC_ERROR",
                "HTTP_FAILED",
                "QUARANTINED",
                "SYNC_DELAYED",
                "SYNC_CANCELLED",
                "SYNC_DISABLED",
                "WLAN_CONTROLLER_MISSING",
                "SERIAL_NUMBER_CONFLICT",
                "UNSUPPORTED_MANAGEMENT_IP",
                "INCORRECT_THIRD_PARTY_CATEGORY",
                "INCORRECT_NETWORK_DEVICE_CATEGORY",
                "UNKNOWN"
                ],
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
                "lastSuccessfulResyncReasons": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "macAddress": {
                "type": "string"
                },
                "managementAddress": {
                "type": "string"
                },
                "managementState": {
                "enum": [
                "MANAGED",
                "UNDER_MAINTENANCE",
                "NEVER_MANAGED"
                ],
                "type": "string"
                },
                "pendingResyncRequestCount": {
                "type": "integer"
                },
                "pendingResyncRequestReasons": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "platformIds": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "reachabilityFailureReason": {
                "type": "string"
                },
                "reachabilityStatus": {
                "enum": [
                "REACHABLE",
                "ONLY_PING_REACHABLE",
                "UNREACHABLE",
                "UNKNOWN"
                ],
                "type": "string"
                },
                "resyncEndTime": {
                "type": "number"
                },
                "resyncIntervalMinutes": {
                "type": "integer"
                },
                "resyncIntervalSource": {
                "enum": [
                "GLOBAL",
                "CUSTOM",
                "NA"
                ],
                "type": "string"
                },
                "resyncReasons": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "resyncRequestedByApps": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "resyncStartTime": {
                "type": "number"
                },
                "role": {
                "enum": [
                "BORDER_ROUTER",
                "CORE",
                "DISTRIBUTION",
                "ACCESS",
                "UNKNOWN"
                ],
                "type": "string"
                },
                "roleSource": {
                "enum": [
                "AUTO",
                "MANUAL"
                ],
                "type": "string"
                },
                "serialNumbers": {
                "items": {
                "type": "string"
                },
                "type": "array"
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
                "stackDevice": {
                "type": "boolean"
                },
                "status": {
                "enum": [
                "MANAGED",
                "SYNC_NOT_STARTED",
                "SYNC_INIT_FAILED",
                "SYNC_PRECHECK_FAILED",
                "SYNC_IN_PROGRESS",
                "SYNC_INTERNAL_ERROR",
                "SYNC_DISABLED",
                "DELETING_DEVICE",
                "UNDER_MAINTENANCE",
                "QUARANTINED",
                "UNASSOCIATED",
                "UNREACHABLE",
                "UNKNOWN"
                ],
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "userDefinedFields": {
                "type": "object"
                },
                "vendor": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "version": {
                "type": "string"
                }
                },
                "type": "object"
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

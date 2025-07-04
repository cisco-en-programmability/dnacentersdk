# -*- coding: utf-8 -*-
"""Cisco DNA Center QueryNetworkDevicesWithFilters data model.

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
    """QueryNetworkDevicesWithFilters request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorFff3662537E538F82BfB5809E30B3Df, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "filter": {
                "properties": {
                "filters": {
                "items": {
                "properties": {
                "key": {
                "type": "string"
                },
                "operator": {
                "enum": [
                "eq",
                "lt",
                "gt",
                "lte",
                "gte",
                "contains",
                "in"
                ],
                "type": "string"
                },
                "value": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "logicalOperator": {
                "enum": [
                "AND",
                "OR"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "page": {
                "properties": {
                "limit": {
                "type": "integer"
                },
                "offset": {
                "type": "integer"
                },
                "sortBy": {
                "properties": {
                "name": {
                "enum": [
                "id",
                "managementAddress",
                "dnsResolvedManagementIpAddress",
                "hostname",
                "macAddress",
                "type",
                "platformids",
                "softwareType",
                "softwareVersion",
                "vendor",
                "bootTime",
                "role",
                "roleSource",
                "apEthernetMacAddress",
                "apManagerInterfaceIpAddress",
                "apWlcIpAddress",
                "deviceSupportLevel",
                "reachabilityFailureReason",
                "resyncStartTime",
                "resyncEndTime",
                "resyncReasons",
                "pendingResyncRequestCount",
                "pendingResyncRequestReasons",
                "resyncIntervalSource",
                "resyncIntervalMinutes"
                ],
                "type": "string"
                },
                "order": {
                "enum": [
                "asc",
                "des"
                ],
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "views": {
                "items": {
                "type": "string"
                },
                "type": "array"
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

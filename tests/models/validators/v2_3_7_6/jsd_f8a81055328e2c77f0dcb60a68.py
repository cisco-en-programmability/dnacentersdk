# -*- coding: utf-8 -*-
"""Cisco DNA Center GetApplicationsV2 data model.

Copyright (c) 2024 Cisco Systems.

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


class JSONSchemaValidatorF8A81055328E2C77F0Dcb60A68(object):
    """GetApplicationsV2 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorF8A81055328E2C77F0Dcb60A68, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "displayName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "identitySource": {
                "properties": {
                "id": {
                "type": "string"
                },
                "type": {
                "enum": [
                "NBAR",
                "APIC_EM"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "indicativeNetworkIdentity": {
                "items": {
                "properties": {
                "displayName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "lowerPort": {
                "type": "number"
                },
                "ports": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "upperPort": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "instanceId": {
                "type": "integer"
                },
                "instanceVersion": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "namespace": {
                "type": "string"
                },
                "networkApplications": {
                "items": {
                "properties": {
                "appProtocol": {
                "enum": [
                "TCP",
                "UDP",
                "TCP/UDP",
                "IP"
                ],
                "type": "string"
                },
                "applicationSubType": {
                "enum": [
                "NONE",
                "LEARNED"
                ],
                "type": "string"
                },
                "applicationType": {
                "enum": [
                "DEFAULT",
                "DEFAULT_MODIFIED",
                "CUSTOM"
                ],
                "type": "string"
                },
                "categoryId": {
                "type": "string"
                },
                "displayName": {
                "type": "string"
                },
                "dscp": {
                "type": "string"
                },
                "engineId": {
                "type": "string"
                },
                "helpString": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "longDescription": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "popularity": {
                "type": "number"
                },
                "rank": {
                "type": "integer"
                },
                "selectorId": {
                "type": "string"
                },
                "serverName": {
                "type": "string"
                },
                "trafficClass": {
                "enum": [
                "BROADCAST_VIDEO",
                "BULK_DATA",
                "MULTIMEDIA_CONFERENCING",
                "MULTIMEDIA_STREAMING",
                "NETWORK_CONTROL",
                "OPS_ADMIN_MGMT",
                "REAL_TIME_INTERACTIVE",
                "SIGNALING",
                "TRANSACTIONAL_DATA",
                "VOIP_TELEPHONY",
                "BEST_EFFORT",
                "SCAVENGER"
                ],
                "type": "string"
                },
                "url": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "networkIdentity": {
                "items": {
                "properties": {
                "displayName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "ipv4Subnet": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "ipv6Subnet": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "lowerPort": {
                "type": "number"
                },
                "ports": {
                "type": "string"
                },
                "protocol": {
                "enum": [
                "TCP_OR_UDP",
                "TCP",
                "UDP",
                "IP"
                ],
                "type": "string"
                },
                "upperPort": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "parentScalableGroup": {
                "properties": {
                "id": {
                "type": "string"
                },
                "idRef": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "qualifier": {
                "type": "string"
                },
                "scalableGroupExternalHandle": {
                "type": "string"
                },
                "scalableGroupType": {
                "type": "string"
                },
                "type": {
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

# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetAnycastGatewaysV1 data model.

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


class JSONSchemaValidatorC634A503551E885C053Fd1Ed9D3Fd(object):
    """GetAnycastGatewaysV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorC634A503551E885C053Fd1Ed9D3Fd, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "fabricId": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "ipPoolName": {
                "type": "string"
                },
                "isCriticalPool": {
                "type": "boolean"
                },
                "isGroupBasedPolicyEnforcementEnabled": {
                "type": "boolean"
                },
                "isIntraSubnetRoutingEnabled": {
                "type": "boolean"
                },
                "isIpDirectedBroadcast": {
                "type": "boolean"
                },
                "isLayer2FloodingEnabled": {
                "type": "boolean"
                },
                "isMultipleIpToMacAddresses": {
                "type": "boolean"
                },
                "isResourceGuardEnabled": {
                "type": "boolean"
                },
                "isSupplicantBasedExtendedNodeOnboarding": {
                "type": "boolean"
                },
                "isWirelessFloodingEnabled": {
                "type": "boolean"
                },
                "isWirelessPool": {
                "type": "boolean"
                },
                "layer2FloodingAddress": {
                "type": "string"
                },
                "layer2FloodingAddressAssignment": {
                "enum": [
                "SHARED",
                "CUSTOM"
                ],
                "type": "string"
                },
                "poolType": {
                "type": "string"
                },
                "securityGroupName": {
                "type": "string"
                },
                "tcpMssAdjustment": {
                "type": "integer"
                },
                "trafficType": {
                "enum": [
                "DATA",
                "VOICE"
                ],
                "type": "string"
                },
                "virtualNetworkName": {
                "type": "string"
                },
                "vlanId": {
                "type": "integer"
                },
                "vlanName": {
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

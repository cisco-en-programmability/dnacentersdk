# -*- coding: utf-8 -*-
"""Cisco Catalyst Center ReadListOfVirtualNetworksWithTheirHealthSummaryV1 data model.

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


class JSONSchemaValidatorA89A96Bc132D58D5Abc0Bdf4D3868B42(object):
    """ReadListOfVirtualNetworksWithTheirHealthSummaryV1 request schema
    definition."""

    def __init__(self):
        super(JSONSchemaValidatorA89A96Bc132D58D5Abc0Bdf4D3868B42, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "page": {
                "properties": {
                "count": {
                "type": "integer"
                },
                "limit": {
                "type": "integer"
                },
                "offset": {
                "type": "integer"
                },
                "sortBy": {
                "items": {
                "properties": {
                "name": {
                "type": "string"
                },
                "order": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "response": {
                "items": {
                "properties": {
                "associatedL3Vn": {
                "type": "string"
                },
                "bgpPeerFairHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPeerGoodHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPeerGoodHealthPercentage": {
                "type": "number"
                },
                "bgpPeerNoHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPeerPoorHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPeerTotalDeviceCount": {
                "type": "integer"
                },
                "fairHealthDeviceCount": {
                "type": "integer"
                },
                "goodHealthDeviceCount": {
                "type": "integer"
                },
                "goodHealthPercentage": {
                "type": "number"
                },
                "id": {
                "type": "string"
                },
                "internetAvailFairHealthDeviceCount": {
                "type": "integer"
                },
                "internetAvailGoodHealthDeviceCount": {
                "type": "integer"
                },
                "internetAvailGoodHealthPercentage": {
                "type": "number"
                },
                "internetAvailNoHealthDeviceCount": {
                "type": "integer"
                },
                "internetAvailPoorHealthDeviceCount": {
                "type": "integer"
                },
                "internetAvailTotalDeviceCount": {
                "type": "integer"
                },
                "layer": {
                "type": "string"
                },
                "multiCastFairHealthDeviceCount": {
                "type": "integer"
                },
                "multiCastGoodHealthDeviceCount": {
                "type": "integer"
                },
                "multiCastGoodHealthPercentage": {
                "type": "number"
                },
                "multiCastPoorHealthDeviceCount": {
                "type": "integer"
                },
                "multiCastTotalDeviceCount": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "networkProtocol": {
                "type": "string"
                },
                "noHealthDeviceCount": {
                "type": "integer"
                },
                "poorHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubSessionFairHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubSessionGoodHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubSessionGoodHealthPercentage": {
                "type": "number"
                },
                "pubsubSessionNoHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubSessionPoorHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubSessionTotalDeviceCount": {
                "type": "integer"
                },
                "totalEndpoints": {
                "type": "integer"
                },
                "totalFabricSites": {
                "type": "integer"
                },
                "totalHealthDeviceCount": {
                "type": "integer"
                },
                "vlan": {
                "type": "string"
                },
                "vnExitFairHealthDeviceCount": {
                "type": "integer"
                },
                "vnExitGoodHealthDeviceCount": {
                "type": "integer"
                },
                "vnExitHealthPercentage": {
                "type": "number"
                },
                "vnExitNoHealthDeviceCount": {
                "type": "integer"
                },
                "vnExitPoorHealthDeviceCount": {
                "type": "integer"
                },
                "vnExitTotalDeviceCount": {
                "type": "integer"
                },
                "vnFabricControlPlaneFairHealthDeviceCount": {
                "type": "integer"
                },
                "vnFabricControlPlaneGoodHealthDeviceCount": {
                "type": "integer"
                },
                "vnFabricControlPlaneGoodHealthPercentage": {
                "type": "number"
                },
                "vnFabricControlPlaneNoHealthDeviceCount": {
                "type": "integer"
                },
                "vnFabricControlPlanePoorHealthDeviceCount": {
                "type": "integer"
                },
                "vnFabricControlPlaneTotalDeviceCount": {
                "type": "integer"
                },
                "vnServicesFairHealthDeviceCount": {
                "type": "integer"
                },
                "vnServicesGoodHealthDeviceCount": {
                "type": "integer"
                },
                "vnServicesHealthPercentage": {
                "type": "number"
                },
                "vnServicesNoHealthDeviceCount": {
                "type": "integer"
                },
                "vnServicesPoorHealthDeviceCount": {
                "type": "integer"
                },
                "vnServicesTotalDeviceCount": {
                "type": "integer"
                },
                "vnStatusFairHealthDeviceCount": {
                "type": "integer"
                },
                "vnStatusGoodHealthDeviceCount": {
                "type": "integer"
                },
                "vnStatusHealthPercentage": {
                "type": "number"
                },
                "vnStatusNoHealthDeviceCount": {
                "type": "integer"
                },
                "vnStatusPoorHealthDeviceCount": {
                "type": "integer"
                },
                "vnStatusTotalDeviceCount": {
                "type": "integer"
                },
                "vniFairHealthDeviceCount": {
                "type": "integer"
                },
                "vniGoodHealthDeviceCount": {
                "type": "integer"
                },
                "vniGoodHealthPercentage": {
                "type": "number"
                },
                "vniNoHealthDeviceCount": {
                "type": "integer"
                },
                "vniPoorHealthDeviceCount": {
                "type": "integer"
                },
                "vniTotalDeviceCount": {
                "type": "integer"
                },
                "vnid": {
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

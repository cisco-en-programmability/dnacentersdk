# -*- coding: utf-8 -*-
"""Cisco Catalyst Center ReadListOfVirtualNetworksWithTheirHealthSummaryV1 data model.

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
                "response": {
                "items": {
                "properties": {
                "associatedL3Vn": {
                "type": "object"
                },
                "bgpPeerFairHealthDeviceCount": {
                "type": "number"
                },
                "bgpPeerGoodHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPeerGoodHealthPercentage": {
                "type": "integer"
                },
                "bgpPeerNoHealthDeviceCount": {
                "type": "number"
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
                "type": "integer"
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
                "type": "integer"
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
                "type": "object"
                },
                "multiCastFairHealthDeviceCount": {
                "type": "number"
                },
                "multiCastGoodHealthDeviceCount": {
                "type": "number"
                },
                "multiCastGoodHealthPercentage": {
                "type": "object"
                },
                "multiCastNoHealthDeviceCount": {
                "type": "number"
                },
                "multiCastPoorHealthDeviceCount": {
                "type": "number"
                },
                "multiCastTotalDeviceCount": {
                "type": "number"
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
                "type": "number"
                },
                "pubsubSessionGoodHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubSessionGoodHealthPercentage": {
                "type": "integer"
                },
                "pubsubSessionNoHealthDeviceCount": {
                "type": "number"
                },
                "pubsubSessionPoorHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubSessionTotalDeviceCount": {
                "type": "integer"
                },
                "totalDeviceCount": {
                "type": "integer"
                },
                "totalEndpoints": {
                "type": "number"
                },
                "totalFabricSites": {
                "type": "integer"
                },
                "vlan": {
                "type": "object"
                },
                "vnExitFairHealthDeviceCount": {
                "type": "number"
                },
                "vnExitGoodHealthDeviceCount": {
                "type": "integer"
                },
                "vnExitHealthPercentage": {
                "type": "integer"
                },
                "vnExitNoHealthDeviceCount": {
                "type": "number"
                },
                "vnExitPoorHealthDeviceCount": {
                "type": "integer"
                },
                "vnExitTotalDeviceCount": {
                "type": "integer"
                },
                "vnFabricControlPlaneFairHealthDeviceCount": {
                "type": "number"
                },
                "vnFabricControlPlaneGoodHealthDeviceCount": {
                "type": "integer"
                },
                "vnFabricControlPlaneGoodHealthPercentage": {
                "type": "integer"
                },
                "vnFabricControlPlaneNoHealthDeviceCount": {
                "type": "number"
                },
                "vnFabricControlPlanePoorHealthDeviceCount": {
                "type": "integer"
                },
                "vnFabricControlPlaneTotalDeviceCount": {
                "type": "integer"
                },
                "vnServicesFairHealthDeviceCount": {
                "type": "number"
                },
                "vnServicesGoodHealthDeviceCount": {
                "type": "integer"
                },
                "vnServicesHealthPercentage": {
                "type": "integer"
                },
                "vnServicesNoHealthDeviceCount": {
                "type": "number"
                },
                "vnServicesPoorHealthDeviceCount": {
                "type": "integer"
                },
                "vnServicesTotalDeviceCount": {
                "type": "integer"
                },
                "vnStatusFairHealthDeviceCount": {
                "type": "number"
                },
                "vnStatusGoodHealthDeviceCount": {
                "type": "number"
                },
                "vnStatusHealthPercentage": {
                "type": "object"
                },
                "vnStatusNoHealthDeviceCount": {
                "type": "number"
                },
                "vnStatusPoorHealthDeviceCount": {
                "type": "number"
                },
                "vnStatusTotalDeviceCount": {
                "type": "number"
                },
                "vniFairHealthDeviceCount": {
                "type": "number"
                },
                "vniGoodHealthDeviceCount": {
                "type": "number"
                },
                "vniGoodHealthPercentage": {
                "type": "object"
                },
                "vniNoHealthDeviceCount": {
                "type": "number"
                },
                "vniPoorHealthDeviceCount": {
                "type": "number"
                },
                "vniTotalDeviceCount": {
                "type": "number"
                },
                "vnid": {
                "type": "integer"
                }
                },
                "type": "object"
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

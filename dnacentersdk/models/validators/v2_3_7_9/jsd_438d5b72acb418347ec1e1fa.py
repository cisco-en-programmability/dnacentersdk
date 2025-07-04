# -*- coding: utf-8 -*-
"""Cisco DNA Center UpdateAdvancedSSIDConfigurationFeatureTemplate data model.

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


class JSONSchemaValidator438D5B72Acb418347Ec1E1Fa(object):
    """UpdateAdvancedSSIDConfigurationFeatureTemplate request schema
    definition."""

    def __init__(self):
        super(JSONSchemaValidator438D5B72Acb418347Ec1E1Fa, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "designName": {
                "type": "string"
                },
                "featureAttributes": {
                "properties": {
                "advertisePCAnalyticsSupport": {
                "type": "boolean"
                },
                "advertiseSupport": {
                "type": "boolean"
                },
                "aironetIESupport": {
                "type": "boolean"
                },
                "callSnooping": {
                "type": "boolean"
                },
                "deferPriority0": {
                "type": "boolean"
                },
                "deferPriority1": {
                "type": "boolean"
                },
                "deferPriority2": {
                "type": "boolean"
                },
                "deferPriority3": {
                "type": "boolean"
                },
                "deferPriority4": {
                "type": "boolean"
                },
                "deferPriority5": {
                "type": "boolean"
                },
                "deferPriority6": {
                "type": "boolean"
                },
                "deferPriority7": {
                "type": "boolean"
                },
                "dhcpOpt82RemoteIDSubOption": {
                "type": "boolean"
                },
                "dhcpRequired": {
                "type": "boolean"
                },
                "dhcpServer": {
                "type": "string"
                },
                "dot11ax": {
                "type": "boolean"
                },
                "dot11vBSSMaxIdleProtected": {
                "type": "boolean"
                },
                "downlinkMuMimo": {
                "type": "boolean"
                },
                "downlinkOfdma": {
                "type": "boolean"
                },
                "dtimPeriod24GHz": {
                "type": "integer"
                },
                "dtimPeriod5GHz": {
                "type": "integer"
                },
                "dualBandNeighborList": {
                "type": "boolean"
                },
                "fastTransitionReassociationTimeout": {
                "type": "integer"
                },
                "fastlaneASR": {
                "type": "boolean"
                },
                "flexLocalAuth": {
                "type": "boolean"
                },
                "idleThreshold": {
                "type": "integer"
                },
                "ipMacBinding": {
                "type": "boolean"
                },
                "ipSourceGuard": {
                "type": "boolean"
                },
                "loadBalancing": {
                "type": "boolean"
                },
                "mDNSMode": {
                "enum": [
                "MDNS_SD_BRIDGING",
                "MDNS_SD_DROP",
                "MDNS_SD_GATEWAY"
                ],
                "type": "string"
                },
                "maxClients": {
                "type": "integer"
                },
                "maxClientsPerAp": {
                "type": "integer"
                },
                "maxClientsPerRadio": {
                "type": "integer"
                },
                "mediaStreamMulticastDirect": {
                "type": "boolean"
                },
                "muMimo11ac": {
                "type": "boolean"
                },
                "multicastBuffer": {
                "type": "boolean"
                },
                "multicastBufferValue": {
                "type": "integer"
                },
                "opportunisticKeyCaching": {
                "type": "boolean"
                },
                "passiveClient": {
                "type": "boolean"
                },
                "peer2peerblocking": {
                "enum": [
                "DISABLE",
                "DROP",
                "FORWARD_UP",
                "ALLOW_PVT_GROUP"
                ],
                "type": "string"
                },
                "predictionOptimization": {
                "type": "boolean"
                },
                "radiusNacState": {
                "type": "boolean"
                },
                "scanDeferTime": {
                "type": "integer"
                },
                "sendBeaconOnAssociation": {
                "type": "boolean"
                },
                "sendBeaconOnRoam": {
                "type": "boolean"
                },
                "sendDisassociate": {
                "type": "boolean"
                },
                "sent486Busy": {
                "type": "boolean"
                },
                "shareDataWithClient": {
                "type": "boolean"
                },
                "targetWakeupTime": {
                "type": "boolean"
                },
                "universalAPAdmin": {
                "type": "boolean"
                },
                "uplinkMuMimo": {
                "type": "boolean"
                },
                "uplinkOfdma": {
                "type": "boolean"
                },
                "vlanCentralSwitching": {
                "type": "boolean"
                },
                "wifiAllianceAgileMultiband": {
                "type": "boolean"
                },
                "wifiToCellularSteering": {
                "type": "boolean"
                },
                "wmmPolicy": {
                "enum": [
                "DISABLED",
                "ALLOWED",
                "REQUIRED"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "unlockedAttributes": {
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

# -*- coding: utf-8 -*-
"""DNA Center Retrieves previous Pathtrace data model.

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


class JSONSchemaValidator7Ab9A8Bd4F3B86A4(object):
    """Retrieves previous Pathtrace request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator7Ab9A8Bd4F3B86A4, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "description":
                 "",
                "properties": {
                "detailedStatus": {
                "description":
                 "",
                "properties": {
                "aclTraceCalculation": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "aclTraceCalculationFailureReason": {
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
                "lastUpdate": {
                "description":
                 "",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "networkElements": {
                "description":
                 "",
                "items": {
                "properties": {
                "accuracyList": {
                "description":
                 "",
                "items": {
                "properties": {
                "percent": {
                "type": [
                "number",
                "null"
                ]
                },
                "reason": {
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
                "null"
                ]
                },
                "detailedStatus": {
                "description":
                 "",
                "properties": {
                "aclTraceCalculation": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "aclTraceCalculationFailureReason": {
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
                "deviceStatistics": {
                "description":
                 "",
                "properties": {
                "cpuStatistics": {
                "description":
                 "",
                "properties": {
                "fiveMinUsageInPercentage": {
                "type": [
                "number",
                "null"
                ]
                },
                "fiveSecsUsageInPercentage": {
                "type": [
                "number",
                "null"
                ]
                },
                "oneMinUsageInPercentage": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "memoryStatistics": {
                "description":
                 "",
                "properties": {
                "memoryUsage": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                },
                "totalMemory": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "deviceStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "deviceStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "egressPhysicalInterface": {
                "description":
                 "",
                "properties": {
                "aclAnalysis": {
                "description":
                 "",
                "properties": {
                "aclName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ace": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "description":
                 "",
                "items": {
                "properties": {
                "ports": {
                "description":
                 "",
                "items": {
                "properties": {
                "destPorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sourcePorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "null"
                ]
                },
                "protocol": {
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
                "null"
                ]
                },
                "result": {
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
                "null"
                ]
                },
                "result": {
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
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "description":
                 "",
                "properties": {
                "adminStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "inputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueFlushes": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueMaxDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "operationalStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "outputDrop": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "interfaceStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "description":
                 "",
                "items": {
                "properties": {
                "controlPlane": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "description":
                 "",
                "properties": {
                "dscp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "qosStatistics": {
                "description":
                 "",
                "items": {
                "properties": {
                "classMapName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dropRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "numBytes": {
                "type": [
                "number",
                "null"
                ]
                },
                "numPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "offeredRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueBandwidthbps": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "queueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueNoBufferDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueTotalDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
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
                "null"
                ]
                },
                "qosStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "egressVirtualInterface": {
                "description":
                 "",
                "properties": {
                "aclAnalysis": {
                "description":
                 "",
                "properties": {
                "aclName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ace": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "description":
                 "",
                "items": {
                "properties": {
                "ports": {
                "description":
                 "",
                "items": {
                "properties": {
                "destPorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sourcePorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "null"
                ]
                },
                "protocol": {
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
                "null"
                ]
                },
                "result": {
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
                "null"
                ]
                },
                "result": {
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
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "description":
                 "",
                "properties": {
                "adminStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "inputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueFlushes": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueMaxDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "operationalStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "outputDrop": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "interfaceStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "description":
                 "",
                "items": {
                "properties": {
                "controlPlane": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "description":
                 "",
                "properties": {
                "dscp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "qosStatistics": {
                "description":
                 "",
                "items": {
                "properties": {
                "classMapName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dropRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "numBytes": {
                "type": [
                "number",
                "null"
                ]
                },
                "numPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "offeredRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueBandwidthbps": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "queueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueNoBufferDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueTotalDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
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
                "null"
                ]
                },
                "qosStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "flexConnect": {
                "description":
                 "",
                "properties": {
                "authentication": {
                "description":
                 "",
                "enum": [
                "LOCAL",
                "CENTRAL",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "dataSwitching": {
                "description":
                 "",
                "enum": [
                "LOCAL",
                "CENTRAL",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "egressAclAnalysis": {
                "description":
                 "",
                "properties": {
                "aclName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ace": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "description":
                 "",
                "items": {
                "properties": {
                "ports": {
                "description":
                 "",
                "items": {
                "properties": {
                "destPorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sourcePorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "null"
                ]
                },
                "protocol": {
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
                "null"
                ]
                },
                "result": {
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
                "null"
                ]
                },
                "result": {
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
                "ingressAclAnalysis": {
                "description":
                 "",
                "properties": {
                "aclName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ace": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "description":
                 "",
                "items": {
                "properties": {
                "ports": {
                "description":
                 "",
                "items": {
                "properties": {
                "destPorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sourcePorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "null"
                ]
                },
                "protocol": {
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
                "null"
                ]
                },
                "result": {
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
                "null"
                ]
                },
                "result": {
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
                "wirelessLanControllerId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "wirelessLanControllerName": {
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
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ingressPhysicalInterface": {
                "description":
                 "",
                "properties": {
                "aclAnalysis": {
                "description":
                 "",
                "properties": {
                "aclName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ace": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "description":
                 "",
                "items": {
                "properties": {
                "ports": {
                "description":
                 "",
                "items": {
                "properties": {
                "destPorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sourcePorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "null"
                ]
                },
                "protocol": {
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
                "null"
                ]
                },
                "result": {
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
                "null"
                ]
                },
                "result": {
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
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "description":
                 "",
                "properties": {
                "adminStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "inputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueFlushes": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueMaxDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "operationalStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "outputDrop": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "interfaceStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "description":
                 "",
                "items": {
                "properties": {
                "controlPlane": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "description":
                 "",
                "properties": {
                "dscp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "qosStatistics": {
                "description":
                 "",
                "items": {
                "properties": {
                "classMapName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dropRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "numBytes": {
                "type": [
                "number",
                "null"
                ]
                },
                "numPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "offeredRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueBandwidthbps": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "queueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueNoBufferDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueTotalDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
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
                "null"
                ]
                },
                "qosStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "ingressVirtualInterface": {
                "description":
                 "",
                "properties": {
                "aclAnalysis": {
                "description":
                 "",
                "properties": {
                "aclName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ace": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "description":
                 "",
                "items": {
                "properties": {
                "ports": {
                "description":
                 "",
                "items": {
                "properties": {
                "destPorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sourcePorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "null"
                ]
                },
                "protocol": {
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
                "null"
                ]
                },
                "result": {
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
                "null"
                ]
                },
                "result": {
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
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "description":
                 "",
                "properties": {
                "adminStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "inputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueFlushes": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueMaxDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "operationalStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "outputDrop": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "interfaceStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "description":
                 "",
                "items": {
                "properties": {
                "controlPlane": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "description":
                 "",
                "properties": {
                "dscp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "qosStatistics": {
                "description":
                 "",
                "items": {
                "properties": {
                "classMapName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dropRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "numBytes": {
                "type": [
                "number",
                "null"
                ]
                },
                "numPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "offeredRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueBandwidthbps": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "queueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueNoBufferDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueTotalDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
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
                "null"
                ]
                },
                "qosStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "ip": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "linkInformationSource": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "perfMonCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "perfMonCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "perfMonStatistics": {
                "description":
                 "",
                "items": {
                "properties": {
                "byteRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "destIpAddress": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "inputInterface": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4DSCP": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4TTL": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputInterface": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "packetBytes": {
                "type": [
                "number",
                "null"
                ]
                },
                "packetCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "packetLoss": {
                "type": [
                "number",
                "null"
                ]
                },
                "packetLossPercentage": {
                "type": [
                "number",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                },
                "rtpJitterMax": {
                "type": [
                "number",
                "null"
                ]
                },
                "rtpJitterMean": {
                "type": [
                "number",
                "null"
                ]
                },
                "rtpJitterMin": {
                "type": [
                "number",
                "null"
                ]
                },
                "sourceIpAddress": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
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
                "ssid": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "tunnels": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "wlanId": {
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
                "null"
                ]
                },
                "networkElementsInfo": {
                "description":
                 "",
                "items": {
                "properties": {
                "accuracyList": {
                "description":
                 "",
                "items": {
                "properties": {
                "percent": {
                "type": [
                "number",
                "null"
                ]
                },
                "reason": {
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
                "null"
                ]
                },
                "detailedStatus": {
                "description":
                 "",
                "properties": {
                "aclTraceCalculation": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "aclTraceCalculationFailureReason": {
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
                "deviceStatistics": {
                "description":
                 "",
                "properties": {
                "cpuStatistics": {
                "description":
                 "",
                "properties": {
                "fiveMinUsageInPercentage": {
                "type": [
                "number",
                "null"
                ]
                },
                "fiveSecsUsageInPercentage": {
                "type": [
                "number",
                "null"
                ]
                },
                "oneMinUsageInPercentage": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "memoryStatistics": {
                "description":
                 "",
                "properties": {
                "memoryUsage": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                },
                "totalMemory": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "deviceStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "deviceStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "egressInterface": {
                "description":
                 "",
                "properties": {
                "physicalInterface": {
                "description":
                 "",
                "properties": {
                "aclAnalysis": {
                "description":
                 "",
                "properties": {
                "aclName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ace": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "description":
                 "",
                "items": {
                "properties": {
                "ports": {
                "description":
                 "",
                "items": {
                "properties": {
                "destPorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sourcePorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "null"
                ]
                },
                "protocol": {
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
                "null"
                ]
                },
                "result": {
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
                "null"
                ]
                },
                "result": {
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
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "description":
                 "",
                "properties": {
                "adminStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "inputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueFlushes": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueMaxDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "operationalStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "outputDrop": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "interfaceStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "description":
                 "",
                "items": {
                "properties": {
                "controlPlane": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "description":
                 "",
                "properties": {
                "dscp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "qosStatistics": {
                "description":
                 "",
                "items": {
                "properties": {
                "classMapName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dropRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "numBytes": {
                "type": [
                "number",
                "null"
                ]
                },
                "numPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "offeredRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueBandwidthbps": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "queueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueNoBufferDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueTotalDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
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
                "null"
                ]
                },
                "qosStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "virtualInterface": {
                "description":
                 "",
                "items": {
                "properties": {
                "aclAnalysis": {
                "description":
                 "",
                "properties": {
                "aclName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ace": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "description":
                 "",
                "items": {
                "properties": {
                "ports": {
                "description":
                 "",
                "items": {
                "properties": {
                "destPorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sourcePorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "null"
                ]
                },
                "protocol": {
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
                "null"
                ]
                },
                "result": {
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
                "null"
                ]
                },
                "result": {
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
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "description":
                 "",
                "properties": {
                "adminStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "inputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueFlushes": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueMaxDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "operationalStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "outputDrop": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "interfaceStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "description":
                 "",
                "items": {
                "properties": {
                "controlPlane": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "description":
                 "",
                "properties": {
                "dscp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "qosStatistics": {
                "description":
                 "",
                "items": {
                "properties": {
                "classMapName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dropRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "numBytes": {
                "type": [
                "number",
                "null"
                ]
                },
                "numPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "offeredRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueBandwidthbps": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "queueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueNoBufferDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueTotalDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
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
                "null"
                ]
                },
                "qosStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "flexConnect": {
                "description":
                 "",
                "properties": {
                "authentication": {
                "description":
                 "",
                "enum": [
                "LOCAL",
                "CENTRAL",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "dataSwitching": {
                "description":
                 "",
                "enum": [
                "LOCAL",
                "CENTRAL",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "egressAclAnalysis": {
                "description":
                 "",
                "properties": {
                "aclName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ace": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "description":
                 "",
                "items": {
                "properties": {
                "ports": {
                "description":
                 "",
                "items": {
                "properties": {
                "destPorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sourcePorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "null"
                ]
                },
                "protocol": {
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
                "null"
                ]
                },
                "result": {
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
                "null"
                ]
                },
                "result": {
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
                "ingressAclAnalysis": {
                "description":
                 "",
                "properties": {
                "aclName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ace": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "description":
                 "",
                "items": {
                "properties": {
                "ports": {
                "description":
                 "",
                "items": {
                "properties": {
                "destPorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sourcePorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "null"
                ]
                },
                "protocol": {
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
                "null"
                ]
                },
                "result": {
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
                "null"
                ]
                },
                "result": {
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
                "wirelessLanControllerId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "wirelessLanControllerName": {
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
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ingressInterface": {
                "description":
                 "",
                "properties": {
                "physicalInterface": {
                "description":
                 "",
                "properties": {
                "aclAnalysis": {
                "description":
                 "",
                "properties": {
                "aclName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ace": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "description":
                 "",
                "items": {
                "properties": {
                "ports": {
                "description":
                 "",
                "items": {
                "properties": {
                "destPorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sourcePorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "null"
                ]
                },
                "protocol": {
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
                "null"
                ]
                },
                "result": {
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
                "null"
                ]
                },
                "result": {
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
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "description":
                 "",
                "properties": {
                "adminStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "inputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueFlushes": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueMaxDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "operationalStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "outputDrop": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "interfaceStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "description":
                 "",
                "items": {
                "properties": {
                "controlPlane": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "description":
                 "",
                "properties": {
                "dscp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "qosStatistics": {
                "description":
                 "",
                "items": {
                "properties": {
                "classMapName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dropRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "numBytes": {
                "type": [
                "number",
                "null"
                ]
                },
                "numPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "offeredRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueBandwidthbps": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "queueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueNoBufferDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueTotalDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
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
                "null"
                ]
                },
                "qosStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "virtualInterface": {
                "description":
                 "",
                "items": {
                "properties": {
                "aclAnalysis": {
                "description":
                 "",
                "properties": {
                "aclName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ace": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "description":
                 "",
                "items": {
                "properties": {
                "ports": {
                "description":
                 "",
                "items": {
                "properties": {
                "destPorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sourcePorts": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "null"
                ]
                },
                "protocol": {
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
                "null"
                ]
                },
                "result": {
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
                "null"
                ]
                },
                "result": {
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
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "description":
                 "",
                "properties": {
                "adminStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "inputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueFlushes": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputQueueMaxDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "inputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "operationalStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "outputDrop": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputQueueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputRatebps": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "interfaceStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "description":
                 "",
                "items": {
                "properties": {
                "controlPlane": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "description":
                 "",
                "properties": {
                "dscp": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "qosStatistics": {
                "description":
                 "",
                "items": {
                "properties": {
                "classMapName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "dropRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "numBytes": {
                "type": [
                "number",
                "null"
                ]
                },
                "numPackets": {
                "type": [
                "number",
                "null"
                ]
                },
                "offeredRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueBandwidthbps": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "queueDepth": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueNoBufferDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "queueTotalDrops": {
                "type": [
                "number",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
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
                "null"
                ]
                },
                "qosStatsCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "ip": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "linkInformationSource": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "perfMonCollection": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "perfMonCollectionFailureReason": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "perfMonitorStatistics": {
                "description":
                 "",
                "items": {
                "properties": {
                "byteRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "destIpAddress": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "inputInterface": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4DSCP": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4TTL": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputInterface": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "packetBytes": {
                "type": [
                "number",
                "null"
                ]
                },
                "packetCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "packetLoss": {
                "type": [
                "number",
                "null"
                ]
                },
                "packetLossPercentage": {
                "type": [
                "number",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "refreshedAt": {
                "type": [
                "number",
                "null"
                ]
                },
                "rtpJitterMax": {
                "type": [
                "number",
                "null"
                ]
                },
                "rtpJitterMean": {
                "type": [
                "number",
                "null"
                ]
                },
                "rtpJitterMin": {
                "type": [
                "number",
                "null"
                ]
                },
                "sourceIpAddress": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
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
                "ssid": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "tunnels": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
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
                "wlanId": {
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
                "null"
                ]
                },
                "properties": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "request": {
                "description":
                 "",
                "properties": {
                "controlPath": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "createTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "destIP": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "failureReason": {
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
                "inclusions": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "lastUpdateTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "periodicRefresh": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIP": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "status": {
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
                }
                },
                "type": [
                "object",
                "null"
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

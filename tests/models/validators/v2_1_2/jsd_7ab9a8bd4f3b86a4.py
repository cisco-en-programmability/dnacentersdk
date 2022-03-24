# -*- coding: utf-8 -*-
"""Cisco DNA Center Retrieves previous Pathtrace data model.

Copyright (c) 2019-2021 Cisco Systems.

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


class JSONSchemaValidator7Ab9A8Bd4F3B86A4(object):
    """Retrieves previous Pathtrace request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator7Ab9A8Bd4F3B86A4, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "properties": {
                "detailedStatus": {
                "properties": {
                "aclTraceCalculation": {
                "type": [
                "string",
                "null"
                ]
                },
                "aclTraceCalculationFailureReason": {
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
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "networkElements": {
                "items": {
                "properties": {
                "accuracyList": {
                "items": {
                "properties": {
                "percent": {
                "type": [
                "number",
                "null"
                ]
                },
                "reason": {
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
                "properties": {
                "aclTraceCalculation": {
                "type": [
                "string",
                "null"
                ]
                },
                "aclTraceCalculationFailureReason": {
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
                "properties": {
                "cpuStatistics": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "deviceStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "egressPhysicalInterface": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                "items": {
                "properties": {
                "classMapName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                "items": {
                "properties": {
                "classMapName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "properties": {
                "authentication": {
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
                "properties": {
                "aclName": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
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
                "properties": {
                "aclName": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "wirelessLanControllerName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "ingressPhysicalInterface": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                "items": {
                "properties": {
                "classMapName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                "items": {
                "properties": {
                "classMapName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "linkInformationSource": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "perfMonCollection": {
                "type": [
                "string",
                "null"
                ]
                },
                "perfMonCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "perfMonStatistics": {
                "items": {
                "properties": {
                "byteRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "destIpAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "inputInterface": {
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4DSCP": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "ssid": {
                "type": [
                "string",
                "null"
                ]
                },
                "tunnels": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "wlanId": {
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
                "items": {
                "properties": {
                "accuracyList": {
                "items": {
                "properties": {
                "percent": {
                "type": [
                "number",
                "null"
                ]
                },
                "reason": {
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
                "properties": {
                "aclTraceCalculation": {
                "type": [
                "string",
                "null"
                ]
                },
                "aclTraceCalculationFailureReason": {
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
                "properties": {
                "cpuStatistics": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "deviceStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "egressInterface": {
                "properties": {
                "physicalInterface": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                "items": {
                "properties": {
                "classMapName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "items": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                "items": {
                "properties": {
                "classMapName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "properties": {
                "authentication": {
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
                "properties": {
                "aclName": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
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
                "properties": {
                "aclName": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "wirelessLanControllerName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "ingressInterface": {
                "properties": {
                "physicalInterface": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                "items": {
                "properties": {
                "classMapName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "items": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": [
                "string",
                "null"
                ]
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataPacketEncapsulation": {
                "type": [
                "string",
                "null"
                ]
                },
                "destIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "type": [
                "string",
                "null"
                ]
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": [
                "string",
                "null"
                ]
                },
                "vnid": {
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
                "items": {
                "properties": {
                "classMapName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatsCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "usedVlan": {
                "type": [
                "string",
                "null"
                ]
                },
                "vrfName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "linkInformationSource": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "perfMonCollection": {
                "type": [
                "string",
                "null"
                ]
                },
                "perfMonCollectionFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "perfMonitorStatistics": {
                "items": {
                "properties": {
                "byteRate": {
                "type": [
                "number",
                "null"
                ]
                },
                "destIpAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "inputInterface": {
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4DSCP": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "ssid": {
                "type": [
                "string",
                "null"
                ]
                },
                "tunnels": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "wlanId": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "destPort": {
                "type": [
                "string",
                "null"
                ]
                },
                "failureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "inclusions": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "sourceIP": {
                "type": [
                "string",
                "null"
                ]
                },
                "sourcePort": {
                "type": [
                "string",
                "null"
                ]
                },
                "status": {
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

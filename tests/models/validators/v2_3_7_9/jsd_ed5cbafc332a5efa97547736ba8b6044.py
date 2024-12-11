# -*- coding: utf-8 -*-
"""Cisco Catalyst Center RetrievesPreviousPathtraceV1 data model.

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


class JSONSchemaValidatorEd5Cbafc332A5Efa97547736Ba8B6044(object):
    """RetrievesPreviousPathtraceV1 request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorEd5Cbafc332A5Efa97547736Ba8B6044, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "detailedStatus": {
                "properties": {
                "aclTraceCalculation": {
                "type": "string"
                },
                "aclTraceCalculationFailureReason": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "lastUpdate": {
                "type": "string"
                },
                "networkElements": {
                "items": {
                "properties": {
                "accuracyList": {
                "items": {
                "properties": {
                "percent": {
                "type": "integer"
                },
                "reason": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "detailedStatus": {
                "properties": {
                "aclTraceCalculation": {
                "type": "string"
                },
                "aclTraceCalculationFailureReason": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "deviceStatistics": {
                "properties": {
                "cpuStatistics": {
                "properties": {
                "fiveMinUsageInPercentage": {
                "type": "number"
                },
                "fiveSecsUsageInPercentage": {
                "type": "number"
                },
                "oneMinUsageInPercentage": {
                "type": "number"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "memoryStatistics": {
                "properties": {
                "memoryUsage": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                },
                "totalMemory": {
                "type": "integer"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "deviceStatsCollection": {
                "type": "string"
                },
                "deviceStatsCollectionFailureReason": {
                "type": "string"
                },
                "egressPhysicalInterface": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": "string"
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": "string"
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sourcePorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
                "type": "string"
                },
                "inputPackets": {
                "type": "integer"
                },
                "inputQueueCount": {
                "type": "integer"
                },
                "inputQueueDrops": {
                "type": "integer"
                },
                "inputQueueFlushes": {
                "type": "integer"
                },
                "inputQueueMaxDepth": {
                "type": "integer"
                },
                "inputRatebps": {
                "type": "integer"
                },
                "operationalStatus": {
                "type": "string"
                },
                "outputDrop": {
                "type": "integer"
                },
                "outputPackets": {
                "type": "integer"
                },
                "outputQueueCount": {
                "type": "integer"
                },
                "outputQueueDepth": {
                "type": "integer"
                },
                "outputRatebps": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "interfaceStatsCollection": {
                "type": "string"
                },
                "interfaceStatsCollectionFailureReason": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": "string"
                },
                "dataPacketEncapsulation": {
                "type": "string"
                },
                "destIp": {
                "type": "string"
                },
                "destPort": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "sourceIp": {
                "type": "string"
                },
                "sourcePort": {
                "type": "string"
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": "string"
                },
                "vnid": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatistics": {
                "items": {
                "properties": {
                "classMapName": {
                "type": "string"
                },
                "dropRate": {
                "type": "integer"
                },
                "numBytes": {
                "type": "integer"
                },
                "numPackets": {
                "type": "integer"
                },
                "offeredRate": {
                "type": "integer"
                },
                "queueBandwidthbps": {
                "type": "string"
                },
                "queueDepth": {
                "type": "integer"
                },
                "queueNoBufferDrops": {
                "type": "integer"
                },
                "queueTotalDrops": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatsCollection": {
                "type": "string"
                },
                "qosStatsCollectionFailureReason": {
                "type": "string"
                },
                "usedVlan": {
                "type": "string"
                },
                "vrfName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "egressVirtualInterface": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": "string"
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": "string"
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sourcePorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
                "type": "string"
                },
                "inputPackets": {
                "type": "integer"
                },
                "inputQueueCount": {
                "type": "integer"
                },
                "inputQueueDrops": {
                "type": "integer"
                },
                "inputQueueFlushes": {
                "type": "integer"
                },
                "inputQueueMaxDepth": {
                "type": "integer"
                },
                "inputRatebps": {
                "type": "integer"
                },
                "operationalStatus": {
                "type": "string"
                },
                "outputDrop": {
                "type": "integer"
                },
                "outputPackets": {
                "type": "integer"
                },
                "outputQueueCount": {
                "type": "integer"
                },
                "outputQueueDepth": {
                "type": "integer"
                },
                "outputRatebps": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "interfaceStatsCollection": {
                "type": "string"
                },
                "interfaceStatsCollectionFailureReason": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": "string"
                },
                "dataPacketEncapsulation": {
                "type": "string"
                },
                "destIp": {
                "type": "string"
                },
                "destPort": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "sourceIp": {
                "type": "string"
                },
                "sourcePort": {
                "type": "string"
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": "string"
                },
                "vnid": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatistics": {
                "items": {
                "properties": {
                "classMapName": {
                "type": "string"
                },
                "dropRate": {
                "type": "integer"
                },
                "numBytes": {
                "type": "integer"
                },
                "numPackets": {
                "type": "integer"
                },
                "offeredRate": {
                "type": "integer"
                },
                "queueBandwidthbps": {
                "type": "string"
                },
                "queueDepth": {
                "type": "integer"
                },
                "queueNoBufferDrops": {
                "type": "integer"
                },
                "queueTotalDrops": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatsCollection": {
                "type": "string"
                },
                "qosStatsCollectionFailureReason": {
                "type": "string"
                },
                "usedVlan": {
                "type": "string"
                },
                "vrfName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "flexConnect": {
                "properties": {
                "authentication": {
                "enum": [
                "LOCAL",
                "CENTRAL"
                ],
                "type": "string"
                },
                "dataSwitching": {
                "enum": [
                "LOCAL",
                "CENTRAL"
                ],
                "type": "string"
                },
                "egressAclAnalysis": {
                "properties": {
                "aclName": {
                "type": "string"
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": "string"
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sourcePorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "ingressAclAnalysis": {
                "properties": {
                "aclName": {
                "type": "string"
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": "string"
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sourcePorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "wirelessLanControllerId": {
                "type": "string"
                },
                "wirelessLanControllerName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "ingressPhysicalInterface": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": "string"
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": "string"
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sourcePorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
                "type": "string"
                },
                "inputPackets": {
                "type": "integer"
                },
                "inputQueueCount": {
                "type": "integer"
                },
                "inputQueueDrops": {
                "type": "integer"
                },
                "inputQueueFlushes": {
                "type": "integer"
                },
                "inputQueueMaxDepth": {
                "type": "integer"
                },
                "inputRatebps": {
                "type": "integer"
                },
                "operationalStatus": {
                "type": "string"
                },
                "outputDrop": {
                "type": "integer"
                },
                "outputPackets": {
                "type": "integer"
                },
                "outputQueueCount": {
                "type": "integer"
                },
                "outputQueueDepth": {
                "type": "integer"
                },
                "outputRatebps": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "interfaceStatsCollection": {
                "type": "string"
                },
                "interfaceStatsCollectionFailureReason": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": "string"
                },
                "dataPacketEncapsulation": {
                "type": "string"
                },
                "destIp": {
                "type": "string"
                },
                "destPort": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "sourceIp": {
                "type": "string"
                },
                "sourcePort": {
                "type": "string"
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": "string"
                },
                "vnid": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatistics": {
                "items": {
                "properties": {
                "classMapName": {
                "type": "string"
                },
                "dropRate": {
                "type": "integer"
                },
                "numBytes": {
                "type": "integer"
                },
                "numPackets": {
                "type": "integer"
                },
                "offeredRate": {
                "type": "integer"
                },
                "queueBandwidthbps": {
                "type": "string"
                },
                "queueDepth": {
                "type": "integer"
                },
                "queueNoBufferDrops": {
                "type": "integer"
                },
                "queueTotalDrops": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatsCollection": {
                "type": "string"
                },
                "qosStatsCollectionFailureReason": {
                "type": "string"
                },
                "usedVlan": {
                "type": "string"
                },
                "vrfName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "ingressVirtualInterface": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": "string"
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": "string"
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sourcePorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
                "type": "string"
                },
                "inputPackets": {
                "type": "integer"
                },
                "inputQueueCount": {
                "type": "integer"
                },
                "inputQueueDrops": {
                "type": "integer"
                },
                "inputQueueFlushes": {
                "type": "integer"
                },
                "inputQueueMaxDepth": {
                "type": "integer"
                },
                "inputRatebps": {
                "type": "integer"
                },
                "operationalStatus": {
                "type": "string"
                },
                "outputDrop": {
                "type": "integer"
                },
                "outputPackets": {
                "type": "integer"
                },
                "outputQueueCount": {
                "type": "integer"
                },
                "outputQueueDepth": {
                "type": "integer"
                },
                "outputRatebps": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "interfaceStatsCollection": {
                "type": "string"
                },
                "interfaceStatsCollectionFailureReason": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": "string"
                },
                "dataPacketEncapsulation": {
                "type": "string"
                },
                "destIp": {
                "type": "string"
                },
                "destPort": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "sourceIp": {
                "type": "string"
                },
                "sourcePort": {
                "type": "string"
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": "string"
                },
                "vnid": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatistics": {
                "items": {
                "properties": {
                "classMapName": {
                "type": "string"
                },
                "dropRate": {
                "type": "integer"
                },
                "numBytes": {
                "type": "integer"
                },
                "numPackets": {
                "type": "integer"
                },
                "offeredRate": {
                "type": "integer"
                },
                "queueBandwidthbps": {
                "type": "string"
                },
                "queueDepth": {
                "type": "integer"
                },
                "queueNoBufferDrops": {
                "type": "integer"
                },
                "queueTotalDrops": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatsCollection": {
                "type": "string"
                },
                "qosStatsCollectionFailureReason": {
                "type": "string"
                },
                "usedVlan": {
                "type": "string"
                },
                "vrfName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "ip": {
                "type": "string"
                },
                "linkInformationSource": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "perfMonCollection": {
                "type": "string"
                },
                "perfMonCollectionFailureReason": {
                "type": "string"
                },
                "perfMonStatistics": {
                "items": {
                "properties": {
                "byteRate": {
                "type": "integer"
                },
                "destIpAddress": {
                "type": "string"
                },
                "destPort": {
                "type": "string"
                },
                "inputInterface": {
                "type": "string"
                },
                "ipv4DSCP": {
                "type": "string"
                },
                "ipv4TTL": {
                "type": "integer"
                },
                "outputInterface": {
                "type": "string"
                },
                "packetBytes": {
                "type": "integer"
                },
                "packetCount": {
                "type": "integer"
                },
                "packetLoss": {
                "type": "integer"
                },
                "packetLossPercentage": {
                "type": "number"
                },
                "protocol": {
                "type": "string"
                },
                "refreshedAt": {
                "type": "integer"
                },
                "rtpJitterMax": {
                "type": "integer"
                },
                "rtpJitterMean": {
                "type": "integer"
                },
                "rtpJitterMin": {
                "type": "integer"
                },
                "sourceIpAddress": {
                "type": "string"
                },
                "sourcePort": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "role": {
                "type": "string"
                },
                "ssid": {
                "type": "string"
                },
                "tunnels": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "type": {
                "type": "string"
                },
                "wlanId": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "networkElementsInfo": {
                "items": {
                "properties": {
                "accuracyList": {
                "items": {
                "properties": {
                "percent": {
                "type": "integer"
                },
                "reason": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "detailedStatus": {
                "properties": {
                "aclTraceCalculation": {
                "type": "string"
                },
                "aclTraceCalculationFailureReason": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "deviceStatistics": {
                "properties": {
                "cpuStatistics": {
                "properties": {
                "fiveMinUsageInPercentage": {
                "type": "number"
                },
                "fiveSecsUsageInPercentage": {
                "type": "number"
                },
                "oneMinUsageInPercentage": {
                "type": "number"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "memoryStatistics": {
                "properties": {
                "memoryUsage": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                },
                "totalMemory": {
                "type": "integer"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "deviceStatsCollection": {
                "type": "string"
                },
                "deviceStatsCollectionFailureReason": {
                "type": "string"
                },
                "egressInterface": {
                "properties": {
                "physicalInterface": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": "string"
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": "string"
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sourcePorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
                "type": "string"
                },
                "inputPackets": {
                "type": "integer"
                },
                "inputQueueCount": {
                "type": "integer"
                },
                "inputQueueDrops": {
                "type": "integer"
                },
                "inputQueueFlushes": {
                "type": "integer"
                },
                "inputQueueMaxDepth": {
                "type": "integer"
                },
                "inputRatebps": {
                "type": "integer"
                },
                "operationalStatus": {
                "type": "string"
                },
                "outputDrop": {
                "type": "integer"
                },
                "outputPackets": {
                "type": "integer"
                },
                "outputQueueCount": {
                "type": "integer"
                },
                "outputQueueDepth": {
                "type": "integer"
                },
                "outputRatebps": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "interfaceStatsCollection": {
                "type": "string"
                },
                "interfaceStatsCollectionFailureReason": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": "string"
                },
                "dataPacketEncapsulation": {
                "type": "string"
                },
                "destIp": {
                "type": "string"
                },
                "destPort": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "sourceIp": {
                "type": "string"
                },
                "sourcePort": {
                "type": "string"
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": "string"
                },
                "vnid": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatistics": {
                "items": {
                "properties": {
                "classMapName": {
                "type": "string"
                },
                "dropRate": {
                "type": "integer"
                },
                "numBytes": {
                "type": "integer"
                },
                "numPackets": {
                "type": "integer"
                },
                "offeredRate": {
                "type": "integer"
                },
                "queueBandwidthbps": {
                "type": "string"
                },
                "queueDepth": {
                "type": "integer"
                },
                "queueNoBufferDrops": {
                "type": "integer"
                },
                "queueTotalDrops": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatsCollection": {
                "type": "string"
                },
                "qosStatsCollectionFailureReason": {
                "type": "string"
                },
                "usedVlan": {
                "type": "string"
                },
                "vrfName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "virtualInterface": {
                "items": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": "string"
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": "string"
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sourcePorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
                "type": "string"
                },
                "inputPackets": {
                "type": "integer"
                },
                "inputQueueCount": {
                "type": "integer"
                },
                "inputQueueDrops": {
                "type": "integer"
                },
                "inputQueueFlushes": {
                "type": "integer"
                },
                "inputQueueMaxDepth": {
                "type": "integer"
                },
                "inputRatebps": {
                "type": "integer"
                },
                "operationalStatus": {
                "type": "string"
                },
                "outputDrop": {
                "type": "integer"
                },
                "outputPackets": {
                "type": "integer"
                },
                "outputQueueCount": {
                "type": "integer"
                },
                "outputQueueDepth": {
                "type": "integer"
                },
                "outputRatebps": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "interfaceStatsCollection": {
                "type": "string"
                },
                "interfaceStatsCollectionFailureReason": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": "string"
                },
                "dataPacketEncapsulation": {
                "type": "string"
                },
                "destIp": {
                "type": "string"
                },
                "destPort": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "sourceIp": {
                "type": "string"
                },
                "sourcePort": {
                "type": "string"
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": "string"
                },
                "vnid": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatistics": {
                "items": {
                "properties": {
                "classMapName": {
                "type": "string"
                },
                "dropRate": {
                "type": "integer"
                },
                "numBytes": {
                "type": "integer"
                },
                "numPackets": {
                "type": "integer"
                },
                "offeredRate": {
                "type": "integer"
                },
                "queueBandwidthbps": {
                "type": "string"
                },
                "queueDepth": {
                "type": "integer"
                },
                "queueNoBufferDrops": {
                "type": "integer"
                },
                "queueTotalDrops": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatsCollection": {
                "type": "string"
                },
                "qosStatsCollectionFailureReason": {
                "type": "string"
                },
                "usedVlan": {
                "type": "string"
                },
                "vrfName": {
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
                "flexConnect": {
                "properties": {
                "authentication": {
                "enum": [
                "LOCAL",
                "CENTRAL"
                ],
                "type": "string"
                },
                "dataSwitching": {
                "enum": [
                "LOCAL",
                "CENTRAL"
                ],
                "type": "string"
                },
                "egressAclAnalysis": {
                "properties": {
                "aclName": {
                "type": "string"
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": "string"
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sourcePorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "ingressAclAnalysis": {
                "properties": {
                "aclName": {
                "type": "string"
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": "string"
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sourcePorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "wirelessLanControllerId": {
                "type": "string"
                },
                "wirelessLanControllerName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "ingressInterface": {
                "properties": {
                "physicalInterface": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": "string"
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": "string"
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sourcePorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
                "type": "string"
                },
                "inputPackets": {
                "type": "integer"
                },
                "inputQueueCount": {
                "type": "integer"
                },
                "inputQueueDrops": {
                "type": "integer"
                },
                "inputQueueFlushes": {
                "type": "integer"
                },
                "inputQueueMaxDepth": {
                "type": "integer"
                },
                "inputRatebps": {
                "type": "integer"
                },
                "operationalStatus": {
                "type": "string"
                },
                "outputDrop": {
                "type": "integer"
                },
                "outputPackets": {
                "type": "integer"
                },
                "outputQueueCount": {
                "type": "integer"
                },
                "outputQueueDepth": {
                "type": "integer"
                },
                "outputRatebps": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "interfaceStatsCollection": {
                "type": "string"
                },
                "interfaceStatsCollectionFailureReason": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": "string"
                },
                "dataPacketEncapsulation": {
                "type": "string"
                },
                "destIp": {
                "type": "string"
                },
                "destPort": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "sourceIp": {
                "type": "string"
                },
                "sourcePort": {
                "type": "string"
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": "string"
                },
                "vnid": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatistics": {
                "items": {
                "properties": {
                "classMapName": {
                "type": "string"
                },
                "dropRate": {
                "type": "integer"
                },
                "numBytes": {
                "type": "integer"
                },
                "numPackets": {
                "type": "integer"
                },
                "offeredRate": {
                "type": "integer"
                },
                "queueBandwidthbps": {
                "type": "string"
                },
                "queueDepth": {
                "type": "integer"
                },
                "queueNoBufferDrops": {
                "type": "integer"
                },
                "queueTotalDrops": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatsCollection": {
                "type": "string"
                },
                "qosStatsCollectionFailureReason": {
                "type": "string"
                },
                "usedVlan": {
                "type": "string"
                },
                "vrfName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "virtualInterface": {
                "items": {
                "properties": {
                "aclAnalysis": {
                "properties": {
                "aclName": {
                "type": "string"
                },
                "matchingAces": {
                "items": {
                "properties": {
                "ace": {
                "type": "string"
                },
                "matchingPorts": {
                "items": {
                "properties": {
                "ports": {
                "items": {
                "properties": {
                "destPorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sourcePorts": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "result": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "interfaceStatistics": {
                "properties": {
                "adminStatus": {
                "type": "string"
                },
                "inputPackets": {
                "type": "integer"
                },
                "inputQueueCount": {
                "type": "integer"
                },
                "inputQueueDrops": {
                "type": "integer"
                },
                "inputQueueFlushes": {
                "type": "integer"
                },
                "inputQueueMaxDepth": {
                "type": "integer"
                },
                "inputRatebps": {
                "type": "integer"
                },
                "operationalStatus": {
                "type": "string"
                },
                "outputDrop": {
                "type": "integer"
                },
                "outputPackets": {
                "type": "integer"
                },
                "outputQueueCount": {
                "type": "integer"
                },
                "outputQueueDepth": {
                "type": "integer"
                },
                "outputRatebps": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "interfaceStatsCollection": {
                "type": "string"
                },
                "interfaceStatsCollectionFailureReason": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "pathOverlayInfo": {
                "items": {
                "properties": {
                "controlPlane": {
                "type": "string"
                },
                "dataPacketEncapsulation": {
                "type": "string"
                },
                "destIp": {
                "type": "string"
                },
                "destPort": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "sourceIp": {
                "type": "string"
                },
                "sourcePort": {
                "type": "string"
                },
                "vxlanInfo": {
                "properties": {
                "dscp": {
                "type": "string"
                },
                "vnid": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatistics": {
                "items": {
                "properties": {
                "classMapName": {
                "type": "string"
                },
                "dropRate": {
                "type": "integer"
                },
                "numBytes": {
                "type": "integer"
                },
                "numPackets": {
                "type": "integer"
                },
                "offeredRate": {
                "type": "integer"
                },
                "queueBandwidthbps": {
                "type": "string"
                },
                "queueDepth": {
                "type": "integer"
                },
                "queueNoBufferDrops": {
                "type": "integer"
                },
                "queueTotalDrops": {
                "type": "integer"
                },
                "refreshedAt": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qosStatsCollection": {
                "type": "string"
                },
                "qosStatsCollectionFailureReason": {
                "type": "string"
                },
                "usedVlan": {
                "type": "string"
                },
                "vrfName": {
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
                "ip": {
                "type": "string"
                },
                "linkInformationSource": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "perfMonCollection": {
                "type": "string"
                },
                "perfMonCollectionFailureReason": {
                "type": "string"
                },
                "perfMonitorStatistics": {
                "items": {
                "properties": {
                "byteRate": {
                "type": "integer"
                },
                "destIpAddress": {
                "type": "string"
                },
                "destPort": {
                "type": "string"
                },
                "inputInterface": {
                "type": "string"
                },
                "ipv4DSCP": {
                "type": "string"
                },
                "ipv4TTL": {
                "type": "integer"
                },
                "outputInterface": {
                "type": "string"
                },
                "packetBytes": {
                "type": "integer"
                },
                "packetCount": {
                "type": "integer"
                },
                "packetLoss": {
                "type": "integer"
                },
                "packetLossPercentage": {
                "type": "number"
                },
                "protocol": {
                "type": "string"
                },
                "refreshedAt": {
                "type": "integer"
                },
                "rtpJitterMax": {
                "type": "integer"
                },
                "rtpJitterMean": {
                "type": "integer"
                },
                "rtpJitterMin": {
                "type": "integer"
                },
                "sourceIpAddress": {
                "type": "string"
                },
                "sourcePort": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "role": {
                "type": "string"
                },
                "ssid": {
                "type": "string"
                },
                "tunnels": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "type": {
                "type": "string"
                },
                "wlanId": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "properties": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "request": {
                "properties": {
                "controlPath": {
                "type": "boolean"
                },
                "createTime": {
                "type": "integer"
                },
                "destIP": {
                "type": "string"
                },
                "destPort": {
                "type": "string"
                },
                "failureReason": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "inclusions": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "lastUpdateTime": {
                "type": "integer"
                },
                "periodicRefresh": {
                "type": "boolean"
                },
                "previousFlowAnalysisId": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "sourceIP": {
                "type": "string"
                },
                "sourcePort": {
                "type": "string"
                },
                "status": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
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

# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetsTheListOfNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFun
ctionsV1 data model.

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


class JSONSchemaValidatorBd1C59E9Be75Ac4A40DEcaa95Ee9Efd(object):
    """GetsTheListOfNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggr
    egationFunctionsV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorBd1C59E9Be75Ac4A40DEcaa95Ee9Efd, self).__init__()
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
                "order": {
                "type": "string"
                },
                "sortBy": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "response": {
                "items": {
                "properties": {
                "aggregateAttributes": {
                "items": {
                "properties": {
                "function": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "value": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "apDetails": {
                "properties": {
                "adminState": {
                "type": "string"
                },
                "apGroup": {
                "type": "string"
                },
                "apOperationalState": {
                "type": "string"
                },
                "apType": {
                "type": "string"
                },
                "connectedTime": {
                "type": "integer"
                },
                "connectedWlcName": {
                "type": "string"
                },
                "ethernetMac": {
                "type": "string"
                },
                "flexGroup": {
                "type": "string"
                },
                "homeApEnabled": {
                "type": "boolean"
                },
                "icapCapability": {
                "type": "string"
                },
                "ledFlashEnabled": {
                "type": "boolean"
                },
                "ledFlashSeconds": {
                "type": "integer"
                },
                "operationalMode": {
                "type": "string"
                },
                "policyTagName": {
                "type": "string"
                },
                "powerCalendarProfile": {
                "type": "string"
                },
                "powerMode": {
                "type": "string"
                },
                "powerProfile": {
                "type": "string"
                },
                "powerSaveMode": {
                "type": "string"
                },
                "powerSaveModeCapable": {
                "type": "string"
                },
                "powerType": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "radios": {
                "items": {
                "properties": {
                "airQuality": {
                "type": "number"
                },
                "band": {
                "type": "string"
                },
                "clientCount": {
                "type": "integer"
                },
                "id": {
                "type": "string"
                },
                "interference": {
                "type": "number"
                },
                "noise": {
                "type": "integer"
                },
                "trafficUtil": {
                "type": "integer"
                },
                "utilization": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "regulatoryDomain": {
                "type": "string"
                },
                "resetReason": {
                "type": "string"
                },
                "rfTagName": {
                "type": "string"
                },
                "siteTagName": {
                "type": "string"
                },
                "subMode": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "clientCount": {
                "type": "integer"
                },
                "collectionStatus": {
                "type": "string"
                },
                "communicationState": {
                "type": "string"
                },
                "deviceFamily": {
                "type": "string"
                },
                "deviceGroupHierarchyId": {
                "type": "string"
                },
                "deviceRole": {
                "type": "string"
                },
                "deviceSeries": {
                "type": "string"
                },
                "deviceType": {
                "type": "string"
                },
                "fabricDetails": {
                "properties": {
                "fabricRole": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "fabricSiteId": {
                "type": "string"
                },
                "fabricSiteName": {
                "type": "string"
                },
                "l2Vns": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "l3Vns": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "networkProtocol": {
                "type": "string"
                },
                "transitFabrics": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "fabricMetricsDetails": {
                "properties": {
                "aaaStatusScore": {
                "type": "integer"
                },
                "bgpBgpSiteScore": {
                "type": "integer"
                },
                "bgpEvpnScore": {
                "type": "integer"
                },
                "bgpPeerInfraVnScore": {
                "type": "integer"
                },
                "bgpPeerScore": {
                "type": "integer"
                },
                "bgpPubsubSiteScore": {
                "type": "integer"
                },
                "bgpTcpScore": {
                "type": "integer"
                },
                "ctsEnvDataDownloadScore": {
                "type": "integer"
                },
                "fabricSiteScore": {
                "type": "integer"
                },
                "fabricTransitScore": {
                "type": "integer"
                },
                "fabricVnScore": {
                "type": "integer"
                },
                "fabsiteFcpScore": {
                "type": "integer"
                },
                "fabsiteFsconnScore": {
                "type": "integer"
                },
                "fabsiteInfraScore": {
                "type": "integer"
                },
                "internetAvailScore": {
                "type": "integer"
                },
                "lispCpConnScore": {
                "type": "integer"
                },
                "lispTransitConnScore": {
                "type": "integer"
                },
                "mcastScore": {
                "type": "integer"
                },
                "overallFabricScore": {
                "type": "integer"
                },
                "peerScore": {
                "type": "integer"
                },
                "portChannelScore": {
                "type": "integer"
                },
                "pubsubInfraVnScore": {
                "type": "integer"
                },
                "pubsubSessionScore": {
                "type": "integer"
                },
                "pubsubTransitConnScore": {
                "type": "integer"
                },
                "remoteInternetAvailScore": {
                "type": "integer"
                },
                "tcpConnScore": {
                "type": "integer"
                },
                "transitControlPlaneScore": {
                "type": "integer"
                },
                "transitServicesScore": {
                "type": "integer"
                },
                "vnExitScore": {
                "type": "integer"
                },
                "vnFcpScore": {
                "type": "integer"
                },
                "vnServiceScore": {
                "type": "integer"
                },
                "vnStatusScore": {
                "type": "integer"
                },
                "vniStatusScore": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "featureFlagList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "haLastResetReason": {
                "type": "string"
                },
                "haStatus": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "ipv4Address": {
                "type": "string"
                },
                "ipv6Address": {
                "type": "string"
                },
                "lastBootTime": {
                "type": "integer"
                },
                "macAddress": {
                "type": "string"
                },
                "maintenanceModeEnabled": {
                "type": "boolean"
                },
                "managementIpAddress": {
                "type": "string"
                },
                "metricsDetails": {
                "properties": {
                "airQualityScore": {
                "type": "integer"
                },
                "apCount": {
                "type": "integer"
                },
                "avgTemperature": {
                "type": "number"
                },
                "cpuScore": {
                "type": "integer"
                },
                "cpuUtilization": {
                "type": "number"
                },
                "discardInterfaces": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "discardScore": {
                "type": "integer"
                },
                "errorInterfaces": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "errorScore": {
                "type": "integer"
                },
                "freeMemoryBuffer": {
                "type": "number"
                },
                "freeMemoryBufferScore": {
                "type": "integer"
                },
                "freeTimer": {
                "type": "number"
                },
                "freeTimerScore": {
                "type": "integer"
                },
                "highLinkUtilizationInterfaces": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "interDeviceConnectedDownInterfaces": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "interDeviceLinkScore": {
                "type": "integer"
                },
                "interferenceScore": {
                "type": "integer"
                },
                "linkUtilizationScore": {
                "type": "integer"
                },
                "maxTemperature": {
                "type": "number"
                },
                "memoryScore": {
                "type": "integer"
                },
                "memoryUtilization": {
                "type": "number"
                },
                "noiseScore": {
                "type": "integer"
                },
                "overallHealthScore": {
                "type": "integer"
                },
                "packetPool": {
                "type": "integer"
                },
                "packetPoolScore": {
                "type": "integer"
                },
                "utilizationScore": {
                "type": "integer"
                },
                "wqePool": {
                "type": "integer"
                },
                "wqePoolScore": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "osType": {
                "type": "string"
                },
                "physicalPortCount": {
                "type": "integer"
                },
                "platformId": {
                "type": "string"
                },
                "portCount": {
                "type": "integer"
                },
                "productVendor": {
                "type": "string"
                },
                "redundancyMode": {
                "type": "string"
                },
                "redundancyPeerState": {
                "type": "string"
                },
                "redundancyPeerStateDerived": {
                "type": "string"
                },
                "redundancyState": {
                "type": "string"
                },
                "redundancyStateDerived": {
                "type": "string"
                },
                "ringStatus": {
                "type": "boolean"
                },
                "serialNumber": {
                "type": "string"
                },
                "siteHierarchy": {
                "type": "string"
                },
                "siteHierarchyId": {
                "type": "string"
                },
                "siteId": {
                "type": "string"
                },
                "softwareVersion": {
                "type": "string"
                },
                "stackType": {
                "type": "string"
                },
                "switchPoeDetails": {
                "properties": {
                "chassisCount": {
                "type": "integer"
                },
                "freePortCount": {
                "type": "integer"
                },
                "moduleCount": {
                "type": "integer"
                },
                "moduleDetails": {
                "items": {
                "properties": {
                "chassisId": {
                "type": "string"
                },
                "interfacePowerMax": {
                "type": "integer"
                },
                "moduleFreePortCount": {
                "type": "integer"
                },
                "moduleId": {
                "type": "string"
                },
                "modulePoePowerAllocated": {
                "type": "number"
                },
                "modulePoePowerConsumed": {
                "type": "integer"
                },
                "modulePortCount": {
                "type": "integer"
                },
                "modulePowerBudget": {
                "type": "integer"
                },
                "modulePowerConsumed": {
                "type": "number"
                },
                "modulePowerRemaining": {
                "type": "number"
                },
                "moduleSystemPowerAllocated": {
                "type": "integer"
                },
                "moduleSystemPowerConsumed": {
                "type": "number"
                },
                "moduleUsedPortCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "poePowerAllocated": {
                "type": "number"
                },
                "poePowerConsumed": {
                "type": "integer"
                },
                "poeVersion": {
                "type": "string"
                },
                "portCount": {
                "type": "integer"
                },
                "powerBudget": {
                "type": "integer"
                },
                "powerConsumed": {
                "type": "number"
                },
                "powerRemaining": {
                "type": "number"
                },
                "systemPowerAllocated": {
                "type": "integer"
                },
                "systemPowerConsumed": {
                "type": "number"
                },
                "usedPortCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "tagNames": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "upTime": {
                "type": "integer"
                },
                "virtualPortCount": {
                "type": "integer"
                },
                "wiredClientCount": {
                "type": "integer"
                },
                "wirelessClientCount": {
                "type": "integer"
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

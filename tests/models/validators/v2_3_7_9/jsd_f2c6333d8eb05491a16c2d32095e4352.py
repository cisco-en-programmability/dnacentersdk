# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetClientDetailV1 data model.

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


class JSONSchemaValidatorF2C6333D8Eb05491A16C2D32095E4352(object):
    """GetClientDetailV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorF2C6333D8Eb05491A16C2D32095E4352, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "connectionInfo": {
                "properties": {
                "band": {
                "type": "string"
                },
                "channel": {
                "type": "string"
                },
                "channelWidth": {
                "type": "string"
                },
                "hostType": {
                "type": "string"
                },
                "nwDeviceMac": {
                "type": "string"
                },
                "nwDeviceName": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "spatialStream": {
                "type": "string"
                },
                "timestamp": {
                "type": "integer"
                },
                "uapsd": {
                "type": "string"
                },
                "wmm": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "detail": {
                "properties": {
                "aaaServerEAPLatency": {
                "type": "number"
                },
                "aaaServerFailedTransaction": {
                "type": "integer"
                },
                "aaaServerIp": {
                "type": "string"
                },
                "aaaServerLatency": {
                "type": "number"
                },
                "aaaServerMABLatency": {
                "type": "number"
                },
                "aaaServerSuccessTransaction": {
                "type": "integer"
                },
                "aaaServerTransaction": {
                "type": "integer"
                },
                "apGroup": {
                "type": "string"
                },
                "authType": {
                "type": "string"
                },
                "avgRssi": {
                "type": "string"
                },
                "avgSnr": {
                "type": "string"
                },
                "bridgeVMMode": {
                "type": "string"
                },
                "channel": {
                "type": "string"
                },
                "clientConnection": {
                "type": "string"
                },
                "clientType": {
                "type": "string"
                },
                "connectedDevice": {
                "items": {
                "properties": {
                "band": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "ip address": {
                "type": "string"
                },
                "mac": {
                "type": "string"
                },
                "mgmtIp": {
                "type": "string"
                },
                "mode": {
                "type": "string"
                },
                "name": {
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
                "connectedUpn": {
                "type": "string"
                },
                "connectedUpnId": {
                "type": "string"
                },
                "connectedUpnOwner": {
                "type": "string"
                },
                "connectionStatus": {
                "type": "string"
                },
                "countryCode": {
                "type": "string"
                },
                "dataRate": {
                "type": "string"
                },
                "deviceForm": {
                "type": "string"
                },
                "deviceVendor": {
                "type": "string"
                },
                "dhcpDeclineIp": {
                "type": "string"
                },
                "dhcpNakIp": {
                "type": "string"
                },
                "dhcpServerDOLatency": {
                "type": "number"
                },
                "dhcpServerFailedTransaction": {
                "type": "integer"
                },
                "dhcpServerIp": {
                "type": "string"
                },
                "dhcpServerLatency": {
                "type": "number"
                },
                "dhcpServerRALatency": {
                "type": "number"
                },
                "dhcpServerSuccessTransaction": {
                "type": "integer"
                },
                "dhcpServerTransaction": {
                "type": "integer"
                },
                "dnsRequest": {
                "type": "string"
                },
                "dnsResponse": {
                "type": "string"
                },
                "dot11Protocol": {
                "type": "string"
                },
                "dot11ProtocolCapability": {
                "type": "string"
                },
                "duid": {
                "type": "string"
                },
                "firmwareVersion": {
                "type": "string"
                },
                "frequency": {
                "type": "string"
                },
                "healthScore": {
                "items": {
                "properties": {
                "healthType": {
                "type": "string"
                },
                "reason": {
                "type": "string"
                },
                "score": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "hostIpV4": {
                "type": "string"
                },
                "hostIpV6": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "hostMac": {
                "type": "string"
                },
                "hostName": {
                "type": "string"
                },
                "hostOs": {
                "type": "string"
                },
                "hostType": {
                "enum": [
                "wired",
                "wireless"
                ],
                "type": "string"
                },
                "hostVersion": {
                "type": "string"
                },
                "hwModel": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "identifier": {
                "type": "string"
                },
                "intelCapable": {
                "type": "boolean"
                },
                "iosCapable": {
                "type": "boolean"
                },
                "isGuestUPNEndpoint": {
                "type": "boolean"
                },
                "issueCount": {
                "type": "integer"
                },
                "l2VirtualNetwork": {
                "type": "string"
                },
                "l3VirtualNetwork": {
                "type": "string"
                },
                "lastUpdated": {
                "type": "integer"
                },
                "latencyBe": {
                "type": "number"
                },
                "latencyBg": {
                "type": "number"
                },
                "latencyVideo": {
                "type": "number"
                },
                "latencyVoice": {
                "type": "number"
                },
                "linkSpeed": {
                "type": "number"
                },
                "linkThreshold": {
                "type": "string"
                },
                "location": {
                "type": "string"
                },
                "maxRoamingDuration": {
                "type": "string"
                },
                "modelName": {
                "type": "string"
                },
                "onboarding": {
                "properties": {
                "aaaRootcauseList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "aaaServerIp": {
                "type": "string"
                },
                "assocDoneTime": {
                "type": "integer"
                },
                "assocRootcauseList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "authDoneTime": {
                "type": "integer"
                },
                "averageAssocDuration": {
                "type": "string"
                },
                "averageAuthDuration": {
                "type": "string"
                },
                "averageDhcpDuration": {
                "type": "string"
                },
                "averageRunDuration": {
                "type": "string"
                },
                "dhcpDoneTime": {
                "type": "integer"
                },
                "dhcpRootcauseList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "dhcpServerIp": {
                "type": "string"
                },
                "latestRootCauseList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "maxAssocDuration": {
                "type": "string"
                },
                "maxAuthDuration": {
                "type": "string"
                },
                "maxDhcpDuration": {
                "type": "string"
                },
                "maxRunDuration": {
                "type": "string"
                },
                "otherRootcauseList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "onboardingTime": {
                "type": "integer"
                },
                "port": {
                "type": "string"
                },
                "portDescription": {
                "type": "string"
                },
                "powerType": {
                "type": "string"
                },
                "privateMac": {
                "type": "boolean"
                },
                "remoteEndDuplexMode": {
                "type": "string"
                },
                "rssi": {
                "type": "string"
                },
                "rssiIsInclude": {
                "type": "string"
                },
                "rssiThreshold": {
                "type": "string"
                },
                "rxBytes": {
                "type": "string"
                },
                "rxLinkError": {
                "type": "number"
                },
                "rxRate": {
                "type": "number"
                },
                "rxRetryPct": {
                "type": "string"
                },
                "salesCode": {
                "type": "string"
                },
                "sessionDuration": {
                "type": "string"
                },
                "sgt": {
                "type": "string"
                },
                "slotId": {
                "type": "integer"
                },
                "snr": {
                "type": "string"
                },
                "snrIsInclude": {
                "type": "string"
                },
                "snrThreshold": {
                "type": "string"
                },
                "ssid": {
                "type": "string"
                },
                "subType": {
                "type": "string"
                },
                "tracked": {
                "type": "string"
                },
                "trustDetails": {
                "type": "string"
                },
                "trustScore": {
                "type": "string"
                },
                "txBytes": {
                "type": "string"
                },
                "txLinkError": {
                "type": "number"
                },
                "txRate": {
                "type": "number"
                },
                "upnId": {
                "type": "string"
                },
                "upnName": {
                "type": "string"
                },
                "upnOwner": {
                "type": "string"
                },
                "usage": {
                "type": "number"
                },
                "userId": {
                "type": "string"
                },
                "versionTime": {
                "type": "integer"
                },
                "vlanId": {
                "type": "integer"
                },
                "vnid": {
                "type": "integer"
                },
                "wlcName": {
                "type": "string"
                },
                "wlcUuid": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "topology": {
                "properties": {
                "links": {
                "items": {
                "properties": {
                "apRadioAdminStatus": {
                "type": "string"
                },
                "apRadioOperStatus": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "interfaceDetails": {
                "items": {
                "properties": {
                "adminStatus": {
                "type": "string"
                },
                "clientMacAddress": {
                "type": "string"
                },
                "connectedDeviceIntName": {
                "type": "string"
                },
                "duplex": {
                "type": "string"
                },
                "portMode": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "label": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "linkStatus": {
                "type": "string"
                },
                "portUtilization": {
                "type": "number"
                },
                "source": {
                "type": "string"
                },
                "sourceAdminStatus": {
                "type": "string"
                },
                "sourceDuplexInfo": {
                "type": "string"
                },
                "sourceInterfaceName": {
                "type": "string"
                },
                "sourceLinkStatus": {
                "type": "string"
                },
                "sourcePortMode": {
                "type": "string"
                },
                "sourcePortVLANInfo": {
                "type": "string"
                },
                "target": {
                "type": "string"
                },
                "targetAdminStatus": {
                "type": "string"
                },
                "targetDuplexInfo": {
                "type": "string"
                },
                "targetInterfaceName": {
                "type": "string"
                },
                "targetLinkStatus": {
                "type": "string"
                },
                "targetPortMode": {
                "type": "string"
                },
                "targetPortVLANInfo": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "nodes": {
                "items": {
                "properties": {
                "clients": {
                "type": "number"
                },
                "connectedDevice": {
                "type": "string"
                },
                "count": {
                "type": "integer"
                },
                "description":
                 {
                "type": "string"
                },
                "deviceType": {
                "type": "string"
                },
                "fabricGroup": {
                "type": "string"
                },
                "fabricRole": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "family": {
                "type": "string"
                },
                "healthScore": {
                "type": "number"
                },
                "id": {
                "type": "string"
                },
                "ip": {
                "type": "string"
                },
                "ipv6": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "level": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "nodeType": {
                "type": "string"
                },
                "platformId": {
                "type": "string"
                },
                "radioFrequency": {
                "type": "string"
                },
                "role": {
                "type": "string"
                },
                "softwareVersion": {
                "type": "string"
                },
                "stackType": {
                "type": "string"
                },
                "userId": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
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

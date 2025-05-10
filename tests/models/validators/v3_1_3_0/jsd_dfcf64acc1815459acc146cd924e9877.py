# -*- coding: utf-8 -*-
"""Cisco Catalyst Center RetrievesTheListOfClientsWhileAlsoOfferingBasicFilteringAndSortingCapabiliti
esV1 data model.

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


class JSONSchemaValidatorDfcf64AcC1815459Acc146Cd924E9877(object):
    """RetrievesTheListOfClientsWhileAlsoOfferingBasicFilteringAndSorting
    CapabilitiesV1 request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorDfcf64AcC1815459Acc146Cd924E9877, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
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
                "connectedNetworkDevice": {
                "properties": {
                "connectedNetworkDeviceId": {
                "type": "string"
                },
                "connectedNetworkDeviceMac": {
                "type": "string"
                },
                "connectedNetworkDeviceManagementIp": {
                "type": "string"
                },
                "connectedNetworkDeviceName": {
                "type": "string"
                },
                "connectedNetworkDeviceType": {
                "type": "string"
                },
                "duplexMode": {
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "interfaceSpeed": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "connection": {
                "properties": {
                "apEthernetMac": {
                "type": "string"
                },
                "apMac": {
                "type": "string"
                },
                "apMode": {
                "type": "string"
                },
                "authType": {
                "type": "string"
                },
                "band": {
                "type": "string"
                },
                "bridgeVMMode": {
                "type": "string"
                },
                "channel": {
                "type": "string"
                },
                "channelWidth": {
                "type": "string"
                },
                "dataRate": {
                "type": "integer"
                },
                "isIosAnalyticsCapable": {
                "type": "boolean"
                },
                "l2Vn": {
                "type": "string"
                },
                "l3Vn": {
                "type": "string"
                },
                "linkSpeed": {
                "type": "integer"
                },
                "protocol": {
                "type": "string"
                },
                "protocolCapability": {
                "type": "string"
                },
                "radioId": {
                "type": "integer"
                },
                "rssi": {
                "type": "integer"
                },
                "securityGroupTag": {
                "type": "string"
                },
                "sessionDuration": {
                "type": "integer"
                },
                "snr": {
                "type": "integer"
                },
                "ssid": {
                "type": "string"
                },
                "upnDuid": {
                "type": "string"
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
                "vlanId": {
                "type": "string"
                },
                "vnId": {
                "type": "string"
                },
                "wlcId": {
                "type": "string"
                },
                "wlcName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "connectionStatus": {
                "type": "string"
                },
                "formFactor": {
                "type": "string"
                },
                "health": {
                "properties": {
                "connectedScore": {
                "type": "integer"
                },
                "isLinkErrorIncluded": {
                "type": "boolean"
                },
                "isRssiIncluded": {
                "type": "boolean"
                },
                "isSnrIncluded": {
                "type": "boolean"
                },
                "linkErrorPercentageThreshold": {
                "type": "integer"
                },
                "onboardingScore": {
                "type": "integer"
                },
                "overallScore": {
                "type": "integer"
                },
                "rssiThreshold": {
                "type": "integer"
                },
                "snrThreshold": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "ipv4Address": {
                "type": "string"
                },
                "ipv6Addresses": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "isPrivateMacAddress": {
                "type": "boolean"
                },
                "lastUpdatedTime": {
                "type": "integer"
                },
                "latency": {
                "properties": {
                "background": {
                "type": "integer"
                },
                "bestEffort": {
                "type": "integer"
                },
                "video": {
                "type": "integer"
                },
                "voice": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "macAddress": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "onboarding": {
                "properties": {
                "aaaFailureReason": {
                "type": "string"
                },
                "aaaServerIp": {
                "type": "string"
                },
                "assocDoneTime": {
                "type": "integer"
                },
                "assocFailureReason": {
                "type": "string"
                },
                "authDoneTime": {
                "type": "integer"
                },
                "avgAssocDuration": {
                "type": "integer"
                },
                "avgAuthDuration": {
                "type": "integer"
                },
                "avgDhcpDuration": {
                "type": "integer"
                },
                "avgRunDuration": {
                "type": "integer"
                },
                "dhcpDoneTime": {
                "type": "integer"
                },
                "dhcpFailureReason": {
                "type": "string"
                },
                "dhcpServerIp": {
                "type": "string"
                },
                "failedRoamingCount": {
                "type": "integer"
                },
                "latestFailureReason": {
                "type": "string"
                },
                "maxAssocDuration": {
                "type": "integer"
                },
                "maxAuthDuration": {
                "type": "integer"
                },
                "maxDhcpDuration": {
                "type": "integer"
                },
                "maxRoamingDuration": {
                "type": "integer"
                },
                "maxRunDuration": {
                "type": "integer"
                },
                "onboardingTime": {
                "type": "integer"
                },
                "otherFailureReason": {
                "type": "string"
                },
                "roamingTime": {
                "type": "integer"
                },
                "successfulRoamingCount": {
                "type": "integer"
                },
                "totalRoamingAttempts": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "osType": {
                "type": "string"
                },
                "osVersion": {
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
                "tracked": {
                "type": "string"
                },
                "traffic": {
                "properties": {
                "dnsRequestCount": {
                "type": "integer"
                },
                "dnsResponseCount": {
                "type": "integer"
                },
                "rxBytes": {
                "type": "integer"
                },
                "rxLinkErrorPercentage": {
                "type": "number"
                },
                "rxPackets": {
                "type": "integer"
                },
                "rxRate": {
                "type": "number"
                },
                "rxRetries": {
                "type": "integer"
                },
                "rxRetryPercentage": {
                "type": "number"
                },
                "txBytes": {
                "type": "integer"
                },
                "txDropPercentage": {
                "type": "integer"
                },
                "txDrops": {
                "type": "integer"
                },
                "txLinkErrorPercentage": {
                "type": "number"
                },
                "txPackets": {
                "type": "integer"
                },
                "txRate": {
                "type": "integer"
                },
                "usage": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": {
                "type": "string"
                },
                "userId": {
                "type": "string"
                },
                "username": {
                "type": "string"
                },
                "vendor": {
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
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )

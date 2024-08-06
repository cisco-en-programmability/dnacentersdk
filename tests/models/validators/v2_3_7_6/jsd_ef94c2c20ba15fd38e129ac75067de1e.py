# -*- coding: utf-8 -*-
"""Cisco DNA Center QueryAssuranceEventsWithFilters data model.

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


class JSONSchemaValidatorEf94C2C20Ba15Fd38E129Ac75067De1E(object):
    """QueryAssuranceEventsWithFilters request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorEf94C2C20Ba15Fd38E129Ac75067De1E, self).__init__()
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
                "affectedClients": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "apMac": {
                "type": "string"
                },
                "apRadioOperationState": {
                "type": "string"
                },
                "apRole": {
                "type": "string"
                },
                "apSwitchId": {
                "type": "string"
                },
                "apSwitchName": {
                "type": "string"
                },
                "assocRssi": {
                "type": "integer"
                },
                "assocSnr": {
                "type": "integer"
                },
                "auditSessionId": {
                "type": "string"
                },
                "authServerIp": {
                "type": "string"
                },
                "candidateAPs": {
                "items": {
                "properties": {
                "apId": {
                "type": "string"
                },
                "apMac": {
                "type": "string"
                },
                "apName": {
                "type": "string"
                },
                "bssid": {
                "type": "string"
                },
                "rssi": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "childEvents": {
                "items": {
                "properties": {
                "details": {
                "type": "string"
                },
                "failureCategory": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "reasonCode": {
                "type": "string"
                },
                "reasonDescription": {
                "type": "string"
                },
                "resultStatus": {
                "type": "string"
                },
                "subReasonCode": {
                "type": "string"
                },
                "subReasonDescription": {
                "type": "string"
                },
                "timestamp": {
                "type": "integer"
                },
                "wirelessEventType": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "clientMac": {
                "type": "string"
                },
                "connectedInterfaceName": {
                "type": "string"
                },
                "currentRadioPowerLevel": {
                "type": "integer"
                },
                "details": {
                "type": "string"
                },
                "deviceFamily": {
                "type": "string"
                },
                "dhcpServerIp": {
                "type": "string"
                },
                "duid": {
                "type": "string"
                },
                "eventStatus": {
                "type": "string"
                },
                "facility": {
                "type": "string"
                },
                "failureCategory": {
                "type": "string"
                },
                "failureIpAddress": {
                "type": "string"
                },
                "frequency": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "identifier": {
                "type": "string"
                },
                "invalidIeAPs": {
                "items": {
                "properties": {
                "apId": {
                "type": "string"
                },
                "apMac": {
                "type": "string"
                },
                "apName": {
                "type": "string"
                },
                "bssid": {
                "type": "string"
                },
                "frameType": {
                "type": "string"
                },
                "ies": {
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
                "ipv4": {
                "type": "string"
                },
                "ipv6": {
                "type": "string"
                },
                "isPrivateMac": {
                "type": "boolean"
                },
                "lastApDisconnectReason": {
                "type": "string"
                },
                "lastApResetType": {
                "type": "string"
                },
                "managementIpAddress": {
                "type": "string"
                },
                "messageType": {
                "type": "string"
                },
                "missingResponseAPs": {
                "items": {
                "properties": {
                "apId": {
                "type": "string"
                },
                "apMac": {
                "type": "string"
                },
                "apName": {
                "type": "string"
                },
                "bssid": {
                "type": "string"
                },
                "frameType": {
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
                "mnemonic": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "networkDeviceId": {
                "type": "string"
                },
                "networkDeviceName": {
                "type": "string"
                },
                "newRadioChannelList": {
                "type": "string"
                },
                "newRadioChannelWidth": {
                "type": "string"
                },
                "oldRadioChannelList": {
                "type": "string"
                },
                "oldRadioChannelWidth": {
                "type": "string"
                },
                "previousRadioPowerLevel": {
                "type": "integer"
                },
                "radioChannelSlot": {
                "type": "integer"
                },
                "radioChannelUtilization": {
                "type": "string"
                },
                "radioInterference": {
                "type": "string"
                },
                "radioNoise": {
                "type": "string"
                },
                "reasonDescription": {
                "type": "string"
                },
                "replacedDeviceSerialNumber": {
                "type": "string"
                },
                "replacingDeviceSerialNumber": {
                "type": "string"
                },
                "resultStatus": {
                "type": "string"
                },
                "roamType": {
                "type": "string"
                },
                "severity": {
                "type": "integer"
                },
                "siteHierarchy": {
                "type": "string"
                },
                "siteHierarchyId": {
                "type": "string"
                },
                "ssid": {
                "type": "string"
                },
                "subReasonDescription": {
                "type": "string"
                },
                "switchNumber": {
                "type": "string"
                },
                "timestamp": {
                "type": "integer"
                },
                "udnId": {
                "type": "string"
                },
                "udnName": {
                "type": "string"
                },
                "username": {
                "type": "string"
                },
                "vlanId": {
                "type": "string"
                },
                "wirelessClientEventEndTime": {
                "type": "integer"
                },
                "wirelessClientEventStartTime": {
                "type": "integer"
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

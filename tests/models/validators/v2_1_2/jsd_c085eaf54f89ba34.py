# -*- coding: utf-8 -*-
"""DNA Center Edit sensor test template data model.

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


class JSONSchemaValidatorC085Eaf54F89Ba34(object):
    """Edit sensor test template request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC085Eaf54F89Ba34, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "description":
                "Response",
                "properties": {
                "_id": {
                "description":
                " Id",
                "type": [
                "string",
                "null"
                ]
                },
                "apCoverage": {
                "description":
                "Ap Coverage",
                "items": {
                "properties": {
                "bands": {
                "description":
                "Bands",
                "type": [
                "string",
                "null"
                ]
                },
                "numberOfApsToTest": {
                "type": [
                "number",
                "null"
                ]
                },
                "rssiThreshold": {
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
                "connection": {
                "description":
                "Connection",
                "type": [
                "string",
                "null"
                ]
                },
                "encryptionMode": {
                "description":
                "Encryption Mode",
                "type": [
                "string",
                "null"
                ]
                },
                "frequency": {
                "description":
                "Frequency",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "lastModifiedTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "legacyTestSuite": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "location": {
                "description":
                "Location",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "locationInfoList": {
                "description":
                "Location Info List",
                "items": {
                "properties": {
                "allSensors": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "locationId": {
                "description":
                "Location Id",
                "type": [
                "string",
                "null"
                ]
                },
                "locationType": {
                "description":
                "Location Type",
                "type": [
                "string",
                "null"
                ]
                },
                "macAddressList": {
                "description":
                "Mac Address List",
                "items": {
                "type": [
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "siteHierarchy": {
                "description":
                "Site Hierarchy",
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
                "modelVersion": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "numAssociatedSensor": {
                "type": [
                "number",
                "null"
                ]
                },
                "numNeighborAPThreshold": {
                "type": [
                "number",
                "null"
                ]
                },
                "radioAsSensorRemoved": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "rssiThreshold": {
                "type": [
                "number",
                "null"
                ]
                },
                "runNow": {
                "description":
                "Run Now",
                "type": [
                "string",
                "null"
                ]
                },
                "schedule": {
                "description":
                "Schedule",
                "properties": {
                "frequency": {
                "description":
                "Frequency",
                "properties": {
                "unit": {
                "description":
                "Unit",
                "type": [
                "string",
                "null"
                ]
                },
                "value": {
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
                "scheduleRange": {
                "description":
                "Schedule Range",
                "items": {
                "properties": {
                "day": {
                "description":
                "Day",
                "type": [
                "string",
                "null"
                ]
                },
                "timeRange": {
                "description":
                "Time Range",
                "items": {
                "properties": {
                "frequency": {
                "description":
                "Frequency",
                "properties": {
                "unit": {
                "description":
                "Unit",
                "type": [
                "string",
                "null"
                ]
                },
                "value": {
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
                "from": {
                "description":
                "From",
                "type": [
                "string",
                "null"
                ]
                },
                "to": {
                "description":
                "To",
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
                "type": [
                "array",
                "null"
                ]
                },
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "testScheduleMode": {
                "description":
                "Test Schedule Mode",
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
                "scheduleInDays": {
                "type": [
                "number",
                "null"
                ]
                },
                "sensors": {
                "description":
                "Sensors",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "showWlcUpgradeBanner": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "siteHierarchy": {
                "description":
                "Site Hierarchy",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "ssids": {
                "description":
                "Ssids",
                "items": {
                "properties": {
                "authProtocol": {
                "description":
                "Auth Protocol",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "authType": {
                "description":
                "Auth Type",
                "type": [
                "string",
                "null"
                ]
                },
                "authTypeRcvd": {
                "description":
                "Auth Type Rcvd",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "bands": {
                "description":
                "Bands",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "certdownloadurl": {
                "description":
                "Certdownloadurl",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "certfilename": {
                "description":
                "Certfilename",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "certpassphrase": {
                "description":
                "Certpassphrase",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "certstatus": {
                "description":
                "Certstatus",
                "type": [
                "string",
                "null"
                ]
                },
                "certxferprotocol": {
                "description":
                "Certxferprotocol",
                "type": [
                "string",
                "null"
                ]
                },
                "eapMethod": {
                "description":
                "Eap Method",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "extWebAuth": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "extWebAuthAccessUrl": {
                "description":
                "Ext Web Auth Access Url",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "extWebAuthHtmlTag": {
                "description":
                "Ext Web Auth Html Tag",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "extWebAuthPortal": {
                "description":
                "Ext Web Auth Portal",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "extWebAuthVirtualIp": {
                "description":
                "Ext Web Auth Virtual Ip",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "id": {
                "type": [
                "number",
                "null"
                ]
                },
                "layer3webAuthEmailAddress": {
                "description":
                "Layer3web Auth Email Address",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "layer3webAuthpassword": {
                "description":
                "Layer3web Authpassword",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "layer3webAuthsecurity": {
                "description":
                "Layer3web Authsecurity",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "layer3webAuthuserName": {
                "description":
                "Layer3web Authuser Name",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "numAps": {
                "type": [
                "number",
                "null"
                ]
                },
                "numSensors": {
                "type": [
                "number",
                "null"
                ]
                },
                "password": {
                "description":
                "Password",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "profileName": {
                "description":
                "Profile Name",
                "type": [
                "string",
                "null"
                ]
                },
                "psk": {
                "description":
                "Psk",
                "type": [
                "string",
                "null"
                ]
                },
                "qosPolicy": {
                "description":
                "Qos Policy",
                "type": [
                "string",
                "null"
                ]
                },
                "scep": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "ssid": {
                "description":
                "Ssid",
                "type": [
                "string",
                "null"
                ]
                },
                "status": {
                "description":
                "Status",
                "type": [
                "string",
                "null"
                ]
                },
                "tests": {
                "description":
                "Tests",
                "items": {
                "properties": {
                "config": {
                "description":
                "Config",
                "items": {
                "properties": {},
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
                "name": {
                "description":
                "Name",
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
                "thirdParty": {
                "description":
                "Third Party",
                "properties": {
                "selected": {
                "type": [
                "boolean",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "username": {
                "description":
                "Username",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "validFrom": {
                "type": [
                "number",
                "null"
                ]
                },
                "validTo": {
                "type": [
                "number",
                "null"
                ]
                },
                "whiteList": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "wlanId": {
                "type": [
                "number",
                "null"
                ]
                },
                "wlc": {
                "description":
                "Wlc",
                "properties": {},
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
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "status": {
                "description":
                "Status",
                "type": [
                "string",
                "null"
                ]
                },
                "tenantId": {
                "description":
                "Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "testDurationEstimate": {
                "type": [
                "number",
                "null"
                ]
                },
                "testScheduleMode": {
                "description":
                "Test Schedule Mode",
                "type": [
                "string",
                "null"
                ]
                },
                "testTemplate": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "tests": {
                "description":
                "Tests",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "version": {
                "type": [
                "number",
                "null"
                ]
                },
                "wlans": {
                "description":
                "Wlans",
                "items": {},
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
                "version": {
                "description":
                "Version",
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

# -*- coding: utf-8 -*-
"""Cisco DNA Center Create sensor test template data model.

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


class JSONSchemaValidator08Bd88834A68A2E6(object):
    """Create sensor test template request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator08Bd88834A68A2E6, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "properties": {
                "_id": {
                "type": [
                "string",
                "null"
                ]
                },
                "apCoverage": {
                "items": {
                "properties": {
                "bands": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "encryptionMode": {
                "type": [
                "string",
                "null"
                ]
                },
                "frequency": {
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
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "locationInfoList": {
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
                "modelVersion": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "schedule": {
                "properties": {},
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
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "ssids": {
                "items": {
                "properties": {
                "authProtocol": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "authType": {
                "type": [
                "string",
                "null"
                ]
                },
                "authTypeRcvd": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "bands": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "certdownloadurl": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "certfilename": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "certpassphrase": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "certstatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "certxferprotocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "eapMethod": {
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
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "extWebAuthHtmlTag": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "extWebAuthPortal": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "extWebAuthVirtualIp": {
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
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "layer3webAuthpassword": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "layer3webAuthsecurity": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "layer3webAuthuserName": {
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
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "profileName": {
                "type": [
                "string",
                "null"
                ]
                },
                "psk": {
                "type": [
                "string",
                "null"
                ]
                },
                "qosPolicy": {
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
                },
                "tests": {
                "items": {
                "properties": {
                "config": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "tenantId": {
                "properties": {},
                "type": [
                "object",
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

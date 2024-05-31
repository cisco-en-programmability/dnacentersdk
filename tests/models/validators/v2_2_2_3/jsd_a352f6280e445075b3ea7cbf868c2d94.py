# -*- coding: utf-8 -*-
"""Cisco DNA Center DuplicateSensorTestTemplate data model.

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


import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorA352F6280E445075B3Ea7Cbf868C2D94(object):
    """DuplicateSensorTestTemplate request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorA352F6280E445075B3Ea7Cbf868C2D94, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "_id": {
                "type": "string"
                },
                "apCoverage": {
                "items": {
                "properties": {
                "bands": {
                "type": "string"
                },
                "numberOfApsToTest": {
                "type": "integer"
                },
                "rssiThreshold": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "connection": {
                "type": "string"
                },
                "encryptionMode": {
                "type": "string"
                },
                "frequency": {
                "type": "object"
                },
                "lastModifiedTime": {
                "type": "number"
                },
                "legacyTestSuite": {
                "type": "boolean"
                },
                "location": {
                "type": "object"
                },
                "locationInfoList": {
                "items": {
                "properties": {
                "allSensors": {
                "type": "boolean"
                },
                "locationId": {
                "type": "string"
                },
                "locationType": {
                "type": "string"
                },
                "macAddressList": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "siteHierarchy": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "modelVersion": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "numAssociatedSensor": {
                "type": "number"
                },
                "numNeighborAPThreshold": {
                "type": "integer"
                },
                "radioAsSensorRemoved": {
                "type": "boolean"
                },
                "rssiThreshold": {
                "type": "integer"
                },
                "runNow": {
                "type": "string"
                },
                "schedule": {
                "properties": {
                "frequency": {
                "properties": {
                "unit": {
                "type": "string"
                },
                "value": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "scheduleRange": {
                "items": {
                "properties": {
                "day": {
                "type": "string"
                },
                "timeRange": {
                "items": {
                "properties": {
                "frequency": {
                "properties": {
                "unit": {
                "type": "string"
                },
                "value": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "from": {
                "type": "string"
                },
                "to": {
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
                "type": "array"
                },
                "startTime": {
                "type": "number"
                },
                "testScheduleMode": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "scheduleInDays": {
                "type": "number"
                },
                "sensors": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "showWlcUpgradeBanner": {
                "type": "boolean"
                },
                "siteHierarchy": {
                "type": "object"
                },
                "ssids": {
                "items": {
                "properties": {
                "authProtocol": {
                "type": "object"
                },
                "authType": {
                "type": "string"
                },
                "authTypeRcvd": {
                "type": "object"
                },
                "bands": {
                "type": "object"
                },
                "certdownloadurl": {
                "type": "object"
                },
                "certfilename": {
                "type": "object"
                },
                "certpassphrase": {
                "type": "object"
                },
                "certstatus": {
                "type": "string"
                },
                "certxferprotocol": {
                "type": "string"
                },
                "eapMethod": {
                "type": "object"
                },
                "extWebAuth": {
                "type": "boolean"
                },
                "extWebAuthAccessUrl": {
                "type": "object"
                },
                "extWebAuthHtmlTag": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "extWebAuthPortal": {
                "type": "object"
                },
                "extWebAuthVirtualIp": {
                "type": "object"
                },
                "id": {
                "type": "number"
                },
                "layer3webAuthEmailAddress": {
                "type": "object"
                },
                "layer3webAuthpassword": {
                "type": "object"
                },
                "layer3webAuthsecurity": {
                "type": "object"
                },
                "layer3webAuthuserName": {
                "type": "object"
                },
                "numAps": {
                "type": "number"
                },
                "numSensors": {
                "type": "number"
                },
                "password": {
                "type": "object"
                },
                "profileName": {
                "type": "string"
                },
                "psk": {
                "type": "string"
                },
                "qosPolicy": {
                "type": "string"
                },
                "scep": {
                "type": "boolean"
                },
                "ssid": {
                "type": "string"
                },
                "status": {
                "type": "string"
                },
                "tests": {
                "items": {
                "properties": {
                "config": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "thirdParty": {
                "properties": {
                "selected": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "username": {
                "type": "object"
                },
                "validFrom": {
                "type": "number"
                },
                "validTo": {
                "type": "number"
                },
                "whiteList": {
                "type": "boolean"
                },
                "wlanId": {
                "type": "number"
                },
                "wlc": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "startTime": {
                "type": "number"
                },
                "status": {
                "type": "string"
                },
                "tenantId": {
                "type": "object"
                },
                "testDurationEstimate": {
                "type": "integer"
                },
                "testScheduleMode": {
                "type": "string"
                },
                "testTemplate": {
                "type": "boolean"
                },
                "tests": {
                "type": "object"
                },
                "version": {
                "type": "number"
                },
                "wlans": {
                "items": {
                "type": "object"
                },
                "type": "array"
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

# -*- coding: utf-8 -*-
"""Cisco DNA Center GetSiteHealthV1 data model.

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


class JSONSchemaValidatorAe4B592F66035F24B55028F79C1B7290(object):
    """GetSiteHealthV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorAe4B592F66035F24B55028F79C1B7290, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "accessGoodCount": {
                "type": "integer"
                },
                "accessTotalCount": {
                "type": "integer"
                },
                "apDeviceGoodCount": {
                "type": "integer"
                },
                "apDeviceTotalCount": {
                "type": "integer"
                },
                "applicationBytesTotalCount": {
                "type": "number"
                },
                "applicationGoodCount": {
                "type": "integer"
                },
                "applicationHealth": {
                "type": "integer"
                },
                "applicationHealthInfo": {
                "items": {
                "properties": {
                "bytesCount": {
                "type": "number"
                },
                "healthScore": {
                "type": "integer"
                },
                "trafficClass": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "applicationHealthStats": {
                "properties": {
                "appTotalCount": {
                "type": "number"
                },
                "businessIrrelevantAppCount": {
                "properties": {
                "fair": {
                "type": "number"
                },
                "good": {
                "type": "number"
                },
                "poor": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "businessRelevantAppCount": {
                "properties": {
                "fair": {
                "type": "number"
                },
                "good": {
                "type": "number"
                },
                "poor": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "defaultHealthAppCount": {
                "properties": {
                "fair": {
                "type": "number"
                },
                "good": {
                "type": "number"
                },
                "poor": {
                "type": "number"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "applicationTotalCount": {
                "type": "integer"
                },
                "clientHealthWired": {
                "type": "integer"
                },
                "clientHealthWireless": {
                "type": "integer"
                },
                "coreGoodCount": {
                "type": "integer"
                },
                "coreTotalCount": {
                "type": "integer"
                },
                "distributionGoodCount": {
                "type": "integer"
                },
                "distributionTotalCount": {
                "type": "integer"
                },
                "dnacInfo": {
                "properties": {
                "ip": {
                "type": "string"
                },
                "status": {
                "type": "string"
                },
                "uuid": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "healthyClientsPercentage": {
                "type": "integer"
                },
                "healthyNetworkDevicePercentage": {
                "type": "integer"
                },
                "latitude": {
                "type": "number"
                },
                "longitude": {
                "type": "number"
                },
                "networkHealthAP": {
                "type": "integer"
                },
                "networkHealthAccess": {
                "type": "integer"
                },
                "networkHealthAverage": {
                "type": "integer"
                },
                "networkHealthCore": {
                "type": "integer"
                },
                "networkHealthDistribution": {
                "type": "integer"
                },
                "networkHealthOthers": {
                "type": "integer"
                },
                "networkHealthRouter": {
                "type": "integer"
                },
                "networkHealthSwitch": {
                "type": "integer"
                },
                "networkHealthWLC": {
                "type": "integer"
                },
                "networkHealthWireless": {
                "type": "integer"
                },
                "numberOfClients": {
                "type": "integer"
                },
                "numberOfNetworkDevice": {
                "type": "integer"
                },
                "numberOfWiredClients": {
                "type": "integer"
                },
                "numberOfWirelessClients": {
                "type": "integer"
                },
                "overallGoodDevices": {
                "type": "integer"
                },
                "parentSiteId": {
                "type": "string"
                },
                "parentSiteName": {
                "type": "string"
                },
                "routerGoodCount": {
                "type": "integer"
                },
                "routerTotalCount": {
                "type": "integer"
                },
                "siteId": {
                "type": "string"
                },
                "siteName": {
                "type": "string"
                },
                "siteType": {
                "type": "string"
                },
                "switchDeviceGoodCount": {
                "type": "integer"
                },
                "switchDeviceTotalCount": {
                "type": "integer"
                },
                "totalNumberOfActiveWirelessClients": {
                "type": "integer"
                },
                "totalNumberOfConnectedWiredClients": {
                "type": "integer"
                },
                "usage": {
                "type": "number"
                },
                "wiredGoodClients": {
                "type": "integer"
                },
                "wirelessDeviceGoodCount": {
                "type": "integer"
                },
                "wirelessDeviceTotalCount": {
                "type": "integer"
                },
                "wirelessGoodClients": {
                "type": "integer"
                },
                "wlcDeviceGoodCount": {
                "type": "integer"
                },
                "wlcDeviceTotalCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
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

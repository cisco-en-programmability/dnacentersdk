# -*- coding: utf-8 -*-
"""Cisco DNA Center Get Site Health data model.

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


class JSONSchemaValidator15B7Aa0C4Dda8E85(object):
    """Get Site Health request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator15B7Aa0C4Dda8E85, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "items": {
                "properties": {
                "accessGoodCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "accessTotalCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "applicationBytesTotalCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "applicationGoodCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "applicationHealth": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "applicationHealthStats": {
                "properties": {
                "appTotalCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "businessIrrelevantAppCount": {
                "properties": {
                "fair": {
                "type": [
                "number",
                "null"
                ]
                },
                "good": {
                "type": [
                "number",
                "null"
                ]
                },
                "poor": {
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
                "businessRelevantAppCount": {
                "properties": {
                "fair": {
                "type": [
                "number",
                "null"
                ]
                },
                "good": {
                "type": [
                "number",
                "null"
                ]
                },
                "poor": {
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
                "defaultHealthAppCount": {
                "properties": {
                "fair": {
                "type": [
                "number",
                "null"
                ]
                },
                "good": {
                "type": [
                "number",
                "null"
                ]
                },
                "poor": {
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
                "applicationTotalCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "clientHealthWired": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "clientHealthWireless": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "coreGoodCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "coreTotalCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "distributionGoodCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "distributionTotalCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "dnacInfo": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "healthyClientsPercentage": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "healthyNetworkDevicePercentage": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "latitude": {
                "type": [
                "number",
                "null"
                ]
                },
                "longitude": {
                "type": [
                "number",
                "null"
                ]
                },
                "networkHealthAccess": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "networkHealthAverage": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "networkHealthCore": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "networkHealthDistribution": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "networkHealthOthers": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "networkHealthRouter": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "networkHealthWireless": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "numberOfClients": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "numberOfNetworkDevice": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "numberOfWiredClients": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "numberOfWirelessClients": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "overallGoodDevices": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "parentSiteId": {
                "type": [
                "string",
                "null"
                ]
                },
                "parentSiteName": {
                "type": [
                "string",
                "null"
                ]
                },
                "routerGoodCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "routerTotalCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "siteId": {
                "type": [
                "string",
                "null"
                ]
                },
                "siteName": {
                "type": [
                "string",
                "null"
                ]
                },
                "siteType": {
                "type": [
                "string",
                "null"
                ]
                },
                "totalNumberOfActiveWirelessClients": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "totalNumberOfConnectedWiredClients": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "wiredGoodClients": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "wirelessDeviceGoodCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "wirelessDeviceTotalCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "wirelessGoodClients": {
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

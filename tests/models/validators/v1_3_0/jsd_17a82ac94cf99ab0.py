# -*- coding: utf-8 -*-
"""DNA Center Get Site Health data model.

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


class JSONSchemaValidator17A82Ac94Cf99Ab0(object):
    """Get Site Health request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator17A82Ac94Cf99Ab0, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "description":
                "Response",
                "items": {
                "properties": {
                "accessGoodCount": {
                "description":
                "Access Good Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "accessTotalCount": {
                "description":
                "Access Total Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "applicationBytesTotalCount": {
                "description":
                "Application Bytes Total Count",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "applicationGoodCount": {
                "description":
                "Application Good Count",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "applicationHealth": {
                "description":
                "Application Health",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "applicationTotalCount": {
                "description":
                "Application Total Count",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "clientHealthWired": {
                "description":
                "Client Health Wired",
                "type": [
                "string",
                "null"
                ]
                },
                "clientHealthWireless": {
                "description":
                "Client Health Wireless",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "clientIssueCount": {
                "description":
                "Client Issue Count",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "clientNumberOfIssues": {
                "description":
                "Client Number Of Issues",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "coreGoodCount": {
                "description":
                "Core Good Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "coreTotalCount": {
                "description":
                "Core Total Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "distributionGoodCount": {
                "description":
                "Distribution Good Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "distributionTotalCount": {
                "description":
                "Distribution Total Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "healthyClientsPercentage": {
                "description":
                "Healthy Clients Percentage",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "healthyNetworkDevicePercentage": {
                "description":
                "Healthy Network Device Percentage",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "latitude": {
                "description":
                "Latitude",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "longitude": {
                "description":
                "Longitude",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "networkHealthAccess": {
                "description":
                "Network Health Access",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "networkHealthAverage": {
                "description":
                "Network Health Average",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "networkHealthCore": {
                "description":
                "Network Health Core",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "networkHealthDistribution": {
                "description":
                "Network Health Distribution",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "networkHealthOthers": {
                "description":
                "Network Health Others",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "networkHealthRouter": {
                "description":
                "Network Health Router",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "networkHealthWireless": {
                "description":
                "Network Health Wireless",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "networkNumberOfIssues": {
                "description":
                "Network Number Of Issues",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "numberOfClients": {
                "description":
                "Number Of Clients",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "numberOfNetworkDevice": {
                "description":
                "Number Of Network Device",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "numberOfWiredClients": {
                "description":
                "Number Of Wired Clients",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "numberOfWirelessClients": {
                "description":
                "Number Of Wireless Clients",
                "properties": {},
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "overallGoodDevices": {
                "description":
                "Overall Good Devices",
                "type": [
                "string",
                "null"
                ]
                },
                "parentSiteId": {
                "description":
                "Parent Site Id",
                "type": [
                "string",
                "null"
                ]
                },
                "parentSiteName": {
                "description":
                "Parent Site Name",
                "type": [
                "string",
                "null"
                ]
                },
                "routerGoodCount": {
                "description":
                "Router Good Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "routerTotalCount": {
                "description":
                "Router Total Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "siteId": {
                "description":
                "Site Id",
                "type": [
                "string",
                "null"
                ]
                },
                "siteName": {
                "description":
                "Site Name",
                "type": [
                "string",
                "null"
                ]
                },
                "siteType": {
                "description":
                "Site Type",
                "type": [
                "string",
                "null"
                ]
                },
                "wiredGoodClients": {
                "description":
                "Wired Good Clients",
                "type": [
                "string",
                "null"
                ]
                },
                "wirelessDeviceGoodCount": {
                "description":
                "Wireless Device Good Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "wirelessDeviceTotalCount": {
                "description":
                "Wireless Device Total Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "wirelessGoodClients": {
                "description":
                "Wireless Good Clients",
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
                "null",
                "object"
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

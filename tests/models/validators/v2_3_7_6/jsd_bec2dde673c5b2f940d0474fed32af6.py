# -*- coding: utf-8 -*-
"""Cisco DNA Center QueryAnAggregatedSummaryOfSiteHealthData data model.

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


class JSONSchemaValidatorBec2Dde673C5B2F940D0474Fed32Af6(object):
    """QueryAnAggregatedSummaryOfSiteHealthData request schema
    definition."""
    def __init__(self):
        super(JSONSchemaValidatorBec2Dde673C5B2F940D0474Fed32Af6, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "accessDeviceCount": {
                "type": "integer"
                },
                "accessDeviceGoodHealthCount": {
                "type": "integer"
                },
                "accessDeviceGoodHealthPercentage": {
                "type": "integer"
                },
                "apDeviceCount": {
                "type": "integer"
                },
                "apDeviceGoodHealthCount": {
                "type": "integer"
                },
                "apDeviceGoodHealthPercentage": {
                "type": "integer"
                },
                "clientCount": {
                "type": "integer"
                },
                "clientDataUsage": {
                "type": "number"
                },
                "clientGoodHealthCount": {
                "type": "integer"
                },
                "clientGoodHealthPercentage": {
                "type": "integer"
                },
                "coreDeviceCount": {
                "type": "integer"
                },
                "coreDeviceGoodHealthCount": {
                "type": "integer"
                },
                "coreDeviceGoodHealthPercentage": {
                "type": "integer"
                },
                "distributionDeviceCount": {
                "type": "integer"
                },
                "distributionDeviceGoodHealthCount": {
                "type": "integer"
                },
                "distributionDeviceGoodHealthPercentage": {
                "type": "integer"
                },
                "id": {
                "type": "string"
                },
                "issueCount": {
                "type": "integer"
                },
                "latitude": {
                "type": "number"
                },
                "longitude": {
                "type": "number"
                },
                "networkDeviceCount": {
                "type": "integer"
                },
                "networkDeviceGoodHealthCount": {
                "type": "integer"
                },
                "networkDeviceGoodHealthPercentage": {
                "type": "integer"
                },
                "p1IssueCount": {
                "type": "integer"
                },
                "p2IssueCount": {
                "type": "integer"
                },
                "p3IssueCount": {
                "type": "integer"
                },
                "p4IssueCount": {
                "type": "integer"
                },
                "routerDeviceCount": {
                "type": "integer"
                },
                "routerDeviceGoodHealthCount": {
                "type": "integer"
                },
                "routerDeviceGoodHealthPercentage": {
                "type": "integer"
                },
                "siteHierarchy": {
                "type": "string"
                },
                "siteHierarchyId": {
                "type": "string"
                },
                "siteType": {
                "type": "string"
                },
                "switchDeviceCount": {
                "type": "integer"
                },
                "switchDeviceGoodHealthCount": {
                "type": "integer"
                },
                "switchDeviceGoodHealthPercentage": {
                "type": "integer"
                },
                "wiredClientCount": {
                "type": "integer"
                },
                "wiredClientGoodHealthCount": {
                "type": "integer"
                },
                "wiredClientGoodHealthPercentage": {
                "type": "integer"
                },
                "wirelessClientCount": {
                "type": "integer"
                },
                "wirelessClientGoodHealthCount": {
                "type": "integer"
                },
                "wirelessClientGoodHealthPercentage": {
                "type": "integer"
                },
                "wirelessDeviceCount": {
                "type": "integer"
                },
                "wirelessDeviceGoodHealthCount": {
                "type": "integer"
                },
                "wirelessDeviceGoodHealthPercentage": {
                "type": "integer"
                },
                "wlcDeviceCount": {
                "type": "integer"
                },
                "wlcDeviceGoodHealthCount": {
                "type": "integer"
                },
                "wlcDeviceGoodHealthPercentage": {
                "type": "integer"
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

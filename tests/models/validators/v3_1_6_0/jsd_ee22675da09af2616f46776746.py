# -*- coding: utf-8 -*-
"""Cisco Catalyst Center ReadFabricEntitySummary data model.

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


class JSONSchemaValidatorEe22675Da09Af2616F46776746(object):
    """ReadFabricEntitySummary request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorEe22675Da09Af2616F46776746, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "protocolSummaries": {
                "items": {
                "properties": {
                "fabricDeviceCount": {
                "type": "integer"
                },
                "fabricSiteCount": {
                "type": "integer"
                },
                "fabricSiteFairHealthCount": {
                "type": "integer"
                },
                "fabricSiteGoodHealthCount": {
                "type": "integer"
                },
                "fabricSiteGoodHealthPercentage": {
                "type": "number"
                },
                "fabricSiteNoHealthCount": {
                "type": "integer"
                },
                "fabricSitePoorHealthCount": {
                "type": "integer"
                },
                "ipTransitNetworkCount": {
                "type": "integer"
                },
                "l2VnCount": {
                "type": "integer"
                },
                "l2VnFairHealthCount": {
                "type": "integer"
                },
                "l2VnGoodHealthCount": {
                "type": "integer"
                },
                "l2VnGoodHealthPercentage": {
                "type": "number"
                },
                "l2VnNoHealthCount": {
                "type": "integer"
                },
                "l2VnPoorHealthCount": {
                "type": "integer"
                },
                "l3VnCount": {
                "type": "integer"
                },
                "l3VnFairHealthCount": {
                "type": "integer"
                },
                "l3VnGoodHealthCount": {
                "type": "integer"
                },
                "l3VnGoodHealthPercentage": {
                "type": "number"
                },
                "l3VnNoHealthCount": {
                "type": "integer"
                },
                "l3VnPoorHealthCount": {
                "type": "integer"
                },
                "networkSegmentProtocol": {
                "type": "string"
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
                "transitNetworkCount": {
                "type": "integer"
                },
                "transitNetworkFairHealthCount": {
                "type": "integer"
                },
                "transitNetworkGoodHealthCount": {
                "type": "integer"
                },
                "transitNetworkGoodHealthPercentage": {
                "type": "number"
                },
                "transitNetworkNoHealthCount": {
                "type": "integer"
                },
                "transitNetworkPoorHealthCount": {
                "type": "integer"
                }
                },
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

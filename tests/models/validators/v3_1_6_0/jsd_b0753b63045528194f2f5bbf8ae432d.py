# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetOverallNetworkHealth data model.

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


class JSONSchemaValidatorB0753B63045528194F2F5Bbf8Ae432D(object):
    """GetOverallNetworkHealth request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorB0753B63045528194F2F5Bbf8Ae432D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "healthContributingDevices": {
                "type": "integer"
                },
                "healthDistirubution": {
                "items": {
                "properties": {
                "badCount": {
                "type": "number"
                },
                "badPercentage": {
                "type": "number"
                },
                "category": {
                "type": "string"
                },
                "fairCount": {
                "type": "number"
                },
                "fairPercentage": {
                "type": "number"
                },
                "goodCount": {
                "type": "number"
                },
                "goodPercentage": {
                "type": "number"
                },
                "healthScore": {
                "type": "integer"
                },
                "kpiMetrics": {
                "items": {
                "properties": {
                "key": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "noHealthCount": {
                "type": "number"
                },
                "noHealthPercentage": {
                "type": "number"
                },
                "thirdPartyDeviceCount": {
                "type": "number"
                },
                "totalCount": {
                "type": "integer"
                },
                "unmonCount": {
                "type": "number"
                },
                "unmonPercentage": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "latestHealthScore": {
                "type": "integer"
                },
                "latestMeasuredByEntity": {
                "type": "string"
                },
                "measuredBy": {
                "type": "string"
                },
                "monitoredDevices": {
                "type": "integer"
                },
                "monitoredFairHealthDevices": {
                "type": "integer"
                },
                "monitoredHealthyDevices": {
                "type": "integer"
                },
                "monitoredPoorHealthDevices": {
                "type": "integer"
                },
                "monitoredUnHealthyDevices": {
                "type": "integer"
                },
                "noHealthDevices": {
                "type": "integer"
                },
                "response": {
                "items": {
                "properties": {
                "badCount": {
                "type": "integer"
                },
                "entity": {
                "type": "string"
                },
                "fairCount": {
                "type": "integer"
                },
                "goodCount": {
                "type": "integer"
                },
                "healthScore": {
                "type": "integer"
                },
                "maintenanceModeCount": {
                "type": "integer"
                },
                "noHealthCount": {
                "type": "integer"
                },
                "time": {
                "type": "string"
                },
                "timeinMillis": {
                "type": "integer"
                },
                "totalCount": {
                "type": "integer"
                },
                "unmonCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "totalDevices": {
                "type": "integer"
                },
                "unMonitoredDevices": {
                "type": "integer"
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

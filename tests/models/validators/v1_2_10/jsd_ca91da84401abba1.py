# -*- coding: utf-8 -*-
"""DNA Center Get Overall Network Health data model.

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


class JSONSchemaValidatorCa91Da84401ABba1(object):
    """Get Overall Network Health request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorCa91Da84401ABba1, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "healthDistirubution": {
                "description":
                "Health Distirubution",
                "items": {
                "properties": {
                "badCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "badPercentage": {
                "type": [
                "number",
                "null"
                ]
                },
                "category": {
                "description":
                "Category",
                "type": [
                "string",
                "null"
                ]
                },
                "fairCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "fairPercentage": {
                "type": [
                "number",
                "null"
                ]
                },
                "goodCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "goodPercentage": {
                "type": [
                "number",
                "null"
                ]
                },
                "healthScore": {
                "type": [
                "number",
                "null"
                ]
                },
                "kpiMetrics": {
                "description":
                "Kpi Metrics",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "totalCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "unmonCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "unmonPercentage": {
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
                "latestHealthScore": {
                "type": [
                "number",
                "null"
                ]
                },
                "latestMeasuredByEntity": {
                "description":
                "Latest Measured By Entity",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "measuredBy": {
                "description":
                "Measured By",
                "type": [
                "string",
                "null"
                ]
                },
                "monitoredDevices": {
                "type": [
                "number",
                "null"
                ]
                },
                "monitoredHealthyDevices": {
                "type": [
                "number",
                "null"
                ]
                },
                "monitoredUnHealthyDevices": {
                "type": [
                "number",
                "null"
                ]
                },
                "response": {
                "description":
                "Response",
                "items": {
                "properties": {
                "badCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "entity": {
                "description":
                "Entity",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "fairCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "goodCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "healthScore": {
                "type": [
                "number",
                "null"
                ]
                },
                "time": {
                "description":
                "Time",
                "type": [
                "string",
                "null"
                ]
                },
                "timeinMillis": {
                "type": [
                "number",
                "null"
                ]
                },
                "totalCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "unmonCount": {
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
                "null",
                "object"
                ]
                },
                "unMonitoredDevices": {
                "type": [
                "number",
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

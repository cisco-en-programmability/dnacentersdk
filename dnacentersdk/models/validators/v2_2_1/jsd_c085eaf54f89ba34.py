# -*- coding: utf-8 -*-
"""DNA Center Edit sensor test template data model.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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
                "templateName": {
                "description":
                "Template Name",
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

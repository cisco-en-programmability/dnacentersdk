# -*- coding: utf-8 -*-
"""Cisco DNA Center Devices data model.

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


class JSONSchemaValidatorA2B479A045298Dca(object):
    """Devices request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorA2B479A045298Dca, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "items": {
                "properties": {
                "airQualityHealth": {
                "properties": {
                "Ghz24": {
                "type": [
                "number",
                "null"
                ]
                },
                "Ghz50": {
                "type": [
                "number",
                "null"
                ]
                },
                "radio0": {
                "type": [
                "number",
                "null"
                ]
                },
                "radio1": {
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
                "clientCount": {
                "properties": {
                "Ghz24": {
                "type": [
                "number",
                "null"
                ]
                },
                "Ghz50": {
                "type": [
                "number",
                "null"
                ]
                },
                "radio0": {
                "type": [
                "number",
                "null"
                ]
                },
                "radio1": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null",
                "number"
                ]
                },
                "cpuHealth": {
                "type": [
                "number",
                "null"
                ]
                },
                "cpuUlitilization": {
                "type": [
                "number",
                "null"
                ]
                },
                "deviceFamily": {
                "type": [
                "string",
                "null"
                ]
                },
                "deviceType": {
                "type": [
                "string",
                "null"
                ]
                },
                "interDeviceLinkAvailHealth": {
                "type": [
                "number",
                "null"
                ]
                },
                "interfaceLinkErrHealth": {
                "type": [
                "number",
                "null"
                ]
                },
                "interferenceHealth": {
                "properties": {
                "Ghz24": {
                "type": [
                "number",
                "null"
                ]
                },
                "Ghz50": {
                "type": [
                "number",
                "null"
                ]
                },
                "radio0": {
                "type": [
                "number",
                "null"
                ]
                },
                "radio1": {
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
                "ipAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "location": {
                "type": [
                "string",
                "null"
                ]
                },
                "macAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "memoryUtilization": {
                "type": [
                "number",
                "null"
                ]
                },
                "memoryUtilizationHealth": {
                "type": [
                "number",
                "null"
                ]
                },
                "model": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "noiseHealth": {
                "properties": {
                "Ghz50": {
                "type": [
                "number",
                "null"
                ]
                },
                "radio1": {
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
                "osVersion": {
                "type": [
                "string",
                "null"
                ]
                },
                "overallHealth": {
                "type": [
                "number",
                "null"
                ]
                },
                "reachabilityHealth": {
                "type": [
                "string",
                "null"
                ]
                },
                "utilizationHealth": {
                "properties": {
                "Ghz24": {
                "type": [
                "number",
                "null"
                ]
                },
                "Ghz50": {
                "type": [
                "number",
                "null"
                ]
                },
                "radio0": {
                "type": [
                "number",
                "null"
                ]
                },
                "radio1": {
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
                "type": [
                "array",
                "null",
                "object"
                ]
                },
                "totalCount": {
                "type": [
                "number",
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

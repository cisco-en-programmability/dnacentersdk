# -*- coding: utf-8 -*-
"""Cisco DNA Center Get Device Detail data model.

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


class JSONSchemaValidator89B2Fb144F5BB09B(object):
    """Get Device Detail request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator89B2Fb144F5BB09B, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "properties": {
                "HALastResetReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "HAPrimaryPowerStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "HASecondaryPowerStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "airQuality": {
                "type": [
                "string",
                "null"
                ]
                },
                "airQualityScore": {
                "type": [
                "number",
                "null"
                ]
                },
                "clientCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "collectionStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "communicationState": {
                "type": [
                "string",
                "null"
                ]
                },
                "cpu": {
                "type": [
                "string",
                "null"
                ]
                },
                "cpuScore": {
                "type": [
                "number",
                "null"
                ]
                },
                "deviceSeries": {
                "type": [
                "string",
                "null"
                ]
                },
                "freeMbuf": {
                "type": [
                "string",
                "null"
                ]
                },
                "freeMbufScore": {
                "type": [
                "number",
                "null"
                ]
                },
                "freeTimer": {
                "type": [
                "string",
                "null"
                ]
                },
                "freeTimerScore": {
                "type": [
                "number",
                "null"
                ]
                },
                "interference": {
                "type": [
                "string",
                "null"
                ]
                },
                "interferenceScore": {
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
                "managementIpAddr": {
                "type": [
                "string",
                "null"
                ]
                },
                "memory": {
                "type": [
                "string",
                "null"
                ]
                },
                "memoryScore": {
                "type": [
                "number",
                "null"
                ]
                },
                "noise": {
                "type": [
                "string",
                "null"
                ]
                },
                "noiseScore": {
                "type": [
                "number",
                "null"
                ]
                },
                "nwDeviceFamily": {
                "type": [
                "string",
                "null"
                ]
                },
                "nwDeviceId": {
                "type": [
                "string",
                "null"
                ]
                },
                "nwDeviceName": {
                "type": [
                "string",
                "null"
                ]
                },
                "nwDeviceRole": {
                "type": [
                "string",
                "null"
                ]
                },
                "nwDeviceType": {
                "type": [
                "string",
                "null"
                ]
                },
                "osType": {
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
                "packetPool": {
                "type": [
                "string",
                "null"
                ]
                },
                "packetPoolScore": {
                "type": [
                "number",
                "null"
                ]
                },
                "platformId": {
                "type": [
                "string",
                "null"
                ]
                },
                "redundancyMode": {
                "type": [
                "string",
                "null"
                ]
                },
                "redundancyPeerState": {
                "type": [
                "string",
                "null"
                ]
                },
                "redundancyState": {
                "type": [
                "string",
                "null"
                ]
                },
                "redundancyUnit": {
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "type": [
                "string",
                "null"
                ]
                },
                "timestamp": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "utilization": {
                "type": [
                "string",
                "null"
                ]
                },
                "utilizationScore": {
                "type": [
                "number",
                "null"
                ]
                },
                "wqe": {
                "type": [
                "string",
                "null"
                ]
                },
                "wqeScore": {
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

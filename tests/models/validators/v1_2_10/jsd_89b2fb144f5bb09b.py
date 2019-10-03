# -*- coding: utf-8 -*-
"""DNA Center Get Device Detail data model.

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


class JSONSchemaValidator89B2Fb144F5BB09B(object):
    """Get Device Detail request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator89B2Fb144F5BB09B, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "description":
                "Response",
                "properties": {
                "HALastResetReason": {
                "description":
                " H A Last Reset Reason",
                "type": [
                "string",
                "null"
                ]
                },
                "HAPrimaryPowerStatus": {
                "description":
                " H A Primary Power Status",
                "type": [
                "string",
                "null"
                ]
                },
                "HASecondaryPowerStatus": {
                "description":
                " H A Secondary Power Status",
                "type": [
                "string",
                "null"
                ]
                },
                "airQuality": {
                "description":
                "Air Quality",
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
                "description":
                "Client Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "collectionStatus": {
                "description":
                "Collection Status",
                "type": [
                "string",
                "null"
                ]
                },
                "communicationState": {
                "description":
                "Communication State",
                "type": [
                "string",
                "null"
                ]
                },
                "cpu": {
                "description":
                "Cpu",
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
                "description":
                "Device Series",
                "type": [
                "string",
                "null"
                ]
                },
                "freeMbuf": {
                "description":
                "Free Mbuf",
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
                "description":
                "Free Timer",
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
                "description":
                "Interference",
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
                "description":
                "Location",
                "type": [
                "string",
                "null"
                ]
                },
                "macAddress": {
                "description":
                "Mac Address",
                "type": [
                "string",
                "null"
                ]
                },
                "managementIpAddr": {
                "description":
                "Management Ip Addr",
                "type": [
                "string",
                "null"
                ]
                },
                "memory": {
                "description":
                "Memory",
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
                "description":
                "Noise",
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
                "description":
                "Nw Device Family",
                "type": [
                "string",
                "null"
                ]
                },
                "nwDeviceId": {
                "description":
                "Nw Device Id",
                "type": [
                "string",
                "null"
                ]
                },
                "nwDeviceName": {
                "description":
                "Nw Device Name",
                "type": [
                "string",
                "null"
                ]
                },
                "nwDeviceRole": {
                "description":
                "Nw Device Role",
                "type": [
                "string",
                "null"
                ]
                },
                "nwDeviceType": {
                "description":
                "Nw Device Type",
                "type": [
                "string",
                "null"
                ]
                },
                "osType": {
                "description":
                "Os Type",
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
                "description":
                "Packet Pool",
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
                "description":
                "Platform Id",
                "type": [
                "string",
                "null"
                ]
                },
                "redundancyMode": {
                "description":
                "Redundancy Mode",
                "type": [
                "string",
                "null"
                ]
                },
                "redundancyPeerState": {
                "description":
                "Redundancy Peer State",
                "type": [
                "string",
                "null"
                ]
                },
                "redundancyState": {
                "description":
                "Redundancy State",
                "type": [
                "string",
                "null"
                ]
                },
                "redundancyUnit": {
                "description":
                "Redundancy Unit",
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "description":
                "Software Version",
                "type": [
                "string",
                "null"
                ]
                },
                "timestamp": {
                "description":
                "Timestamp",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "utilization": {
                "description":
                "Utilization",
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
                "description":
                "Wqe",
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

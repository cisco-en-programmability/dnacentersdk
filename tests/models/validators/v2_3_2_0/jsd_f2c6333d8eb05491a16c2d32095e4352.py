# -*- coding: utf-8 -*-
"""Cisco DNA Center GetClientDetail data model.

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


class JSONSchemaValidatorF2C6333D8Eb05491A16C2D32095E4352(object):
    """GetClientDetail request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF2C6333D8Eb05491A16C2D32095E4352, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "connectionInfo": {
                "properties": {
                "band": {
                "type": "string"
                },
                "channel": {
                "type": "string"
                },
                "channelWidth": {
                "type": "string"
                },
                "hostType": {
                "type": "string"
                },
                "nwDeviceMac": {
                "type": "string"
                },
                "nwDeviceName": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "spatialStream": {
                "type": "string"
                },
                "timestamp": {
                "type": "integer"
                },
                "uapsd": {
                "type": "string"
                },
                "wmm": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "detail": {
                "properties": {
                "apGroup": {
                "type": "object"
                },
                "authType": {
                "type": "string"
                },
                "avgRssi": {
                "type": "object"
                },
                "avgSnr": {
                "type": "object"
                },
                "channel": {
                "type": "string"
                },
                "clientConnection": {
                "type": "string"
                },
                "clientType": {
                "type": "string"
                },
                "connectedDevice": {
                "items": {
                "type": "object"
                }
                },
                "connectionStatus": {
                "type": "string"
                },
                "dataRate": {
                "type": "string"
                },
                "dnsFailure": {
                "type": "object"
                },
                "dnsSuccess": {
                "type": "object"
                },
                "frequency": {
                "type": "string"
                },
                "healthScore": {
                "items": {
                "properties": {
                "healthType": {
                "type": "string"
                },
                "reason": {
                "type": "string"
                },
                "score": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "hostIpV4": {
                "type": "string"
                },
                "hostIpV6": {
                "items": {
                "type": "string"
                }
                },
                "hostMac": {
                "type": "string"
                },
                "hostName": {
                "type": "string"
                },
                "hostOs": {
                "type": "object"
                },
                "hostType": {
                "type": "string"
                },
                "hostVersion": {
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "iosCapable": {
                "type": "boolean"
                },
                "issueCount": {
                "type": "number"
                },
                "lastUpdated": {
                "type": "integer"
                },
                "location": {
                "type": "object"
                },
                "onboarding": {
                "properties": {
                "aaaRootcauseList": {
                "items": {
                "type": "object"
                }
                },
                "aaaServerIp": {
                "type": "string"
                },
                "assocDoneTime": {
                "type": "object"
                },
                "assocRootcauseList": {
                "items": {
                "type": "object"
                }
                },
                "authDoneTime": {
                "type": "object"
                },
                "averageAssocDuration": {
                "type": "object"
                },
                "averageAuthDuration": {
                "type": "object"
                },
                "averageDhcpDuration": {
                "type": "object"
                },
                "averageRunDuration": {
                "type": "object"
                },
                "dhcpDoneTime": {
                "type": "object"
                },
                "dhcpRootcauseList": {
                "items": {
                "type": "object"
                }
                },
                "dhcpServerIp": {
                "type": "object"
                },
                "maxAssocDuration": {
                "type": "object"
                },
                "maxAuthDuration": {
                "type": "object"
                },
                "maxDhcpDuration": {
                "type": "object"
                },
                "maxRunDuration": {
                "type": "object"
                },
                "otherRootcauseList": {
                "items": {
                "type": "object"
                }
                }
                },
                "type": "object"
                },
                "onboardingTime": {
                "type": "object"
                },
                "port": {
                "type": "object"
                },
                "rssi": {
                "type": "string"
                },
                "rxBytes": {
                "type": "string"
                },
                "snr": {
                "type": "string"
                },
                "ssid": {
                "type": "string"
                },
                "subType": {
                "type": "string"
                },
                "txBytes": {
                "type": "string"
                },
                "userId": {
                "type": "object"
                },
                "vlanId": {
                "type": "string"
                },
                "vnid": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "topology": {
                "properties": {
                "links": {
                "items": {
                "properties": {
                "id": {
                "type": "object"
                },
                "label": {
                "items": {
                "type": "string"
                }
                },
                "linkStatus": {
                "type": "string"
                },
                "portUtilization": {
                "type": "object"
                },
                "source": {
                "type": "string"
                },
                "target": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "nodes": {
                "items": {
                "properties": {
                "clients": {
                "type": "object"
                },
                "connectedDevice": {
                "type": "object"
                },
                "count": {
                "type": "object"
                },
                "description":
                 {
                "type": "string"
                },
                "deviceType": {
                "type": "string"
                },
                "fabricGroup": {
                "type": "object"
                },
                "family": {
                "type": "object"
                },
                "healthScore": {
                "type": "integer"
                },
                "id": {
                "type": "string"
                },
                "ip": {
                "type": "string"
                },
                "level": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "nodeType": {
                "type": "string"
                },
                "platformId": {
                "type": "object"
                },
                "radioFrequency": {
                "type": "object"
                },
                "role": {
                "type": "string"
                },
                "softwareVersion": {
                "type": "object"
                },
                "userId": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
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

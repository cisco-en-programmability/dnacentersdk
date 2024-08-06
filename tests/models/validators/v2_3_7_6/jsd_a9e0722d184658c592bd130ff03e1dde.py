# -*- coding: utf-8 -*-
"""Cisco DNA Center GetDeviceInterfaceStatsInfo data model.

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

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorA9E0722D184658C592Bd130Ff03E1Dde(object):
    """GetDeviceInterfaceStatsInfo request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorA9E0722D184658C592Bd130Ff03E1Dde, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "page": {
                "properties": {
                "count": {
                "type": "integer"
                },
                "limit": {
                "type": "integer"
                },
                "offset": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "response": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "values": {
                "properties": {
                "adminStatus": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "deviceId": {
                "type": "string"
                },
                "duplexConfig": {
                "type": "string"
                },
                "duplexOper": {
                "type": "string"
                },
                "instanceId": {
                "type": "string"
                },
                "interfaceId": {
                "type": "string"
                },
                "interfaceType": {
                "type": "string"
                },
                "ipv4Address": {
                "type": "string"
                },
                "ipv6AddressList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "isL3Interface": {
                "type": "string"
                },
                "isWan": {
                "type": "string"
                },
                "macAddr": {
                "type": "string"
                },
                "mediaType": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "operStatus": {
                "type": "string"
                },
                "peerStackMember": {
                "type": "string"
                },
                "peerStackPort": {
                "type": "string"
                },
                "portChannelId": {
                "type": "string"
                },
                "portMode": {
                "type": "string"
                },
                "portType": {
                "type": "string"
                },
                "rxDiscards": {
                "type": "string"
                },
                "rxError": {
                "type": "string"
                },
                "rxRate": {
                "type": "string"
                },
                "rxUtilization": {
                "type": "string"
                },
                "speed": {
                "type": "string"
                },
                "stackPortType": {
                "type": "string"
                },
                "timestamp": {
                "type": "string"
                },
                "txDiscards": {
                "type": "string"
                },
                "txError": {
                "type": "string"
                },
                "txRate": {
                "type": "string"
                },
                "txUtilization": {
                "type": "string"
                },
                "vlanId": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "totalCount": {
                "type": "number"
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

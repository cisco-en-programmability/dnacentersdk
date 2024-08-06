# -*- coding: utf-8 -*-
"""Cisco DNA Center InventoryInsightDeviceLinkMismatch data model.

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


class JSONSchemaValidatorEed1595442B757Bf94938C858A257Ced(object):
    """InventoryInsightDeviceLinkMismatch request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorEed1595442B757Bf94938C858A257Ced, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "avgUpdateFrequency": {
                "type": "number"
                },
                "endDeviceHostName": {
                "type": "string"
                },
                "endDeviceId": {
                "type": "string"
                },
                "endDeviceIpAddress": {
                "type": "string"
                },
                "endPortAddress": {
                "type": "string"
                },
                "endPortAllowedVlanIds": {
                "type": "string"
                },
                "endPortDuplex": {
                "type": "string"
                },
                "endPortId": {
                "type": "string"
                },
                "endPortMask": {
                "type": "string"
                },
                "endPortName": {
                "type": "string"
                },
                "endPortNativeVlanId": {
                "type": "string"
                },
                "endPortPepId": {
                "type": "string"
                },
                "endPortSpeed": {
                "type": "string"
                },
                "instanceTenantId": {
                "type": "string"
                },
                "instanceUuid": {
                "type": "string"
                },
                "lastUpdated": {
                "type": "string"
                },
                "linkStatus": {
                "type": "string"
                },
                "numUpdates": {
                "type": "number"
                },
                "startDeviceHostName": {
                "type": "string"
                },
                "startDeviceId": {
                "type": "string"
                },
                "startDeviceIpAddress": {
                "type": "string"
                },
                "startPortAddress": {
                "type": "string"
                },
                "startPortAllowedVlanIds": {
                "type": "string"
                },
                "startPortDuplex": {
                "type": "string"
                },
                "startPortId": {
                "type": "string"
                },
                "startPortMask": {
                "type": "string"
                },
                "startPortName": {
                "type": "string"
                },
                "startPortNativeVlanId": {
                "type": "string"
                },
                "startPortPepId": {
                "type": "string"
                },
                "startPortSpeed": {
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
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

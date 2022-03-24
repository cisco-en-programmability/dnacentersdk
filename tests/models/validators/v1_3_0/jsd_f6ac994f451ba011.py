# -*- coding: utf-8 -*-
"""Cisco DNA Center Get Discovered network devices by discovery Id data model.

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


class JSONSchemaValidatorF6Ac994F451BA011(object):
    """Get Discovered network devices by discovery Id request schema
    definition."""
    def __init__(self):
        super(JSONSchemaValidatorF6Ac994F451BA011, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "items": {
                "properties": {
                "anchorWlcForAp": {
                "type": [
                "string",
                "null"
                ]
                },
                "authModelId": {
                "type": [
                "string",
                "null"
                ]
                },
                "avgUpdateFrequency": {
                "type": [
                "number",
                "null"
                ]
                },
                "bootDateTime": {
                "type": [
                "string",
                "null"
                ]
                },
                "cliStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "duplicateDeviceId": {
                "type": [
                "string",
                "null"
                ]
                },
                "errorCode": {
                "type": [
                "string",
                "null"
                ]
                },
                "errorDescription": {
                "type": [
                "string",
                "null"
                ]
                },
                "family": {
                "type": [
                "string",
                "null"
                ]
                },
                "hostname": {
                "type": [
                "string",
                "null"
                ]
                },
                "httpStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "imageName": {
                "type": [
                "string",
                "null"
                ]
                },
                "ingressQueueConfig": {
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "inventoryCollectionStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "inventoryReachabilityStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "lastUpdated": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "lineCardCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "lineCardId": {
                "type": [
                "string",
                "null"
                ]
                },
                "location": {
                "type": [
                "string",
                "null"
                ]
                },
                "locationName": {
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
                "managementIpAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "memorySize": {
                "type": [
                "string",
                "null"
                ]
                },
                "netconfStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "numUpdates": {
                "type": [
                "number",
                "null"
                ]
                },
                "pingStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "platformId": {
                "type": [
                "string",
                "null"
                ]
                },
                "portRange": {
                "type": [
                "string",
                "null"
                ]
                },
                "qosStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "reachabilityFailureReason": {
                "type": [
                "string",
                "null"
                ]
                },
                "reachabilityStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "role": {
                "type": [
                "string",
                "null"
                ]
                },
                "roleSource": {
                "type": [
                "string",
                "null"
                ]
                },
                "serialNumber": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpContact": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpLocation": {
                "type": [
                "string",
                "null"
                ]
                },
                "snmpStatus": {
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
                "tag": {
                "type": [
                "string",
                "null"
                ]
                },
                "tagCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "type": {
                "type": [
                "string",
                "null"
                ]
                },
                "upTime": {
                "type": [
                "string",
                "null"
                ]
                },
                "vendor": {
                "type": [
                "string",
                "null"
                ]
                },
                "wlcApDeviceStatus": {
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

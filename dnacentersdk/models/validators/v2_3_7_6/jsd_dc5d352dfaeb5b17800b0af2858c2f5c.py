# -*- coding: utf-8 -*-
"""Cisco DNA Center LANAutomationStartV2 data model.

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


class JSONSchemaValidatorDc5D352DFaeb5B17800B0Af2858C2F5C(object):
    """LANAutomationStartV2 request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorDc5D352DFaeb5B17800B0Af2858C2F5C, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "discoveredDeviceSiteNameHierarchy": {
                "type": "string"
                },
                "discoveryDevices": {
                "items": {
                "properties": {
                "deviceHostName": {
                "type": "string"
                },
                "deviceManagementIPAddress": {
                "type": "string"
                },
                "deviceSerialNumber": {
                "type": "string"
                },
                "deviceSiteNameHierarchy": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "discoveryLevel": {
                "type": "integer"
                },
                "discoveryTimeout": {
                "type": "integer"
                },
                "hostNameFileId": {
                "type": "string"
                },
                "hostNamePrefix": {
                "type": "string"
                },
                "ipPools": {
                "items": {
                "properties": {
                "ipPoolName": {
                "type": "string"
                },
                "ipPoolRole": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "isisDomainPwd": {
                "type": "string"
                },
                "multicastEnabled": {
                "type": "boolean"
                },
                "peerDeviceManagmentIPAddress": {
                "type": "string"
                },
                "primaryDeviceInterfaceNames": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "primaryDeviceManagmentIPAddress": {
                "type": "string"
                },
                "redistributeIsisToBgp": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )

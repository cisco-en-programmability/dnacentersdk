# -*- coding: utf-8 -*-
"""Cisco DNA Center Get NFV Profile data model.

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


class JSONSchemaValidator1Eb19887457B9616(object):
    """Get NFV Profile request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator1Eb19887457B9616, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "items": {
                "properties": {
                "device": {
                "items": {
                "properties": {
                "customNetworks": {
                "items": {
                "properties": {
                "connectionType": {
                "type": [
                "string",
                "null"
                ]
                },
                "networkName": {
                "type": [
                "string",
                "null"
                ]
                },
                "servicesToConnect": {
                "items": {
                "properties": {
                "serviceName": {
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
                "vlanId": {
                "type": [
                "string",
                "null"
                ]
                },
                "vlanMode": {
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
                "customTemplate": {
                "items": {
                "properties": {
                "deviceType": {
                "type": [
                "string",
                "null"
                ]
                },
                "template": {
                "type": [
                "string",
                "null"
                ]
                },
                "templateType": {
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
                "deviceTag": {
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
                "directInternetAccessForFirewall": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "serviceProviderProfile": {
                "items": {
                "properties": {
                "connect": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "connectDefaultGatewayOnWan": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "linkType": {
                "type": [
                "string",
                "null"
                ]
                },
                "serviceProvider": {
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
                "services": {
                "items": {
                "properties": {
                "firewallMode": {
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
                "profileType": {
                "type": [
                "string",
                "null"
                ]
                },
                "serviceName": {
                "type": [
                "string",
                "null"
                ]
                },
                "serviceType": {
                "type": [
                "string",
                "null"
                ]
                },
                "vNicMapping": {
                "items": {
                "properties": {
                "assignIpAddressToNetwork": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "networkType": {
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
                "vlanForL2": {
                "items": {
                "properties": {
                "vlanDescription": {
                "type": [
                "string",
                "null"
                ]
                },
                "vlanId": {
                "type": [
                "string",
                "null"
                ]
                },
                "vlanType": {
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
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "profileName": {
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
                "null",
                "object"
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

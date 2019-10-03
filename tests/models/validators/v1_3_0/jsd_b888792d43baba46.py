# -*- coding: utf-8 -*-
"""DNA Center Get Interface by Id data model.

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


class JSONSchemaValidatorB888792D43BaBa46(object):
    """Get Interface by Id request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorB888792D43BaBa46, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "description":
                 "",
                "properties": {
                "adminStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "className": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "description":
                 {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "deviceId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "duplex": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ifIndex": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4Address": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4Mask": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "isisSupport": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "lastUpdated": {
                "description":
                 "",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "macAddress": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "mappedPhysicalInterfaceId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "mappedPhysicalInterfaceName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "mediaType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "nativeVlanId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ospfSupport": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "pid": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "portMode": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "portName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "portType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "serialNo": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "series": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "speed": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "status": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vlanId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "voiceVlan": {
                "description":
                 "",
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
                "version": {
                "description":
                 "",
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

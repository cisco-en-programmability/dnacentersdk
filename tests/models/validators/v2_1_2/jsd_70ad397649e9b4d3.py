# -*- coding: utf-8 -*-
"""Cisco DNA Center Get OSPF interfaces data model.

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


class JSONSchemaValidator70Ad397649E9B4D3(object):
    """Get OSPF interfaces request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator70Ad397649E9B4D3, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "items": {
                "properties": {
                "adminStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "className": {
                "type": [
                "string",
                "null"
                ]
                },
                "description":
                 {
                "type": [
                "string",
                "null"
                ]
                },
                "deviceId": {
                "type": [
                "string",
                "null"
                ]
                },
                "duplex": {
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
                "ifIndex": {
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceType": {
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4Address": {
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4Mask": {
                "type": [
                "string",
                "null"
                ]
                },
                "isisSupport": {
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
                "macAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "mappedPhysicalInterfaceId": {
                "type": [
                "string",
                "null"
                ]
                },
                "mappedPhysicalInterfaceName": {
                "type": [
                "string",
                "null"
                ]
                },
                "mediaType": {
                "type": [
                "string",
                "null"
                ]
                },
                "nativeVlanId": {
                "type": [
                "string",
                "null"
                ]
                },
                "ospfSupport": {
                "type": [
                "string",
                "null"
                ]
                },
                "pid": {
                "type": [
                "string",
                "null"
                ]
                },
                "portMode": {
                "type": [
                "string",
                "null"
                ]
                },
                "portName": {
                "type": [
                "string",
                "null"
                ]
                },
                "portType": {
                "type": [
                "string",
                "null"
                ]
                },
                "serialNo": {
                "type": [
                "string",
                "null"
                ]
                },
                "series": {
                "type": [
                "string",
                "null"
                ]
                },
                "speed": {
                "type": [
                "string",
                "null"
                ]
                },
                "status": {
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
                "voiceVlan": {
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

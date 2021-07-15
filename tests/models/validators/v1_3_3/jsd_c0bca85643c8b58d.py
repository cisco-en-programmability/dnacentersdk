# -*- coding: utf-8 -*-
"""Cisco DNA Center Get Global Pool data model.

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


class JSONSchemaValidatorC0BcA85643C8B58D(object):
    """Get Global Pool request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC0BcA85643C8B58D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "items": {
                "properties": {
                "clientOptions": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "configureExternalDhcp": {
                "type": [
                "string",
                "null"
                ]
                },
                "context": {
                "items": {
                "properties": {
                "contextKey": {
                "type": [
                "string",
                "null"
                ]
                },
                "contextValue": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "owner": {
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
                "createTime": {
                "type": [
                "string",
                "null"
                ]
                },
                "dhcpServerIps": {
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "dnsServerIps": {
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "gateways": {
                "items": {
                "type": [
                "string",
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
                "ipPoolCidr": {
                "type": [
                "string",
                "null"
                ]
                },
                "ipPoolName": {
                "type": [
                "string",
                "null"
                ]
                },
                "ipv6": {
                "type": [
                "string",
                "null"
                ]
                },
                "lastUpdateTime": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "overlapping": {
                "type": [
                "string",
                "null"
                ]
                },
                "owner": {
                "type": [
                "string",
                "null"
                ]
                },
                "parentUuid": {
                "type": [
                "string",
                "null"
                ]
                },
                "shared": {
                "type": [
                "string",
                "null"
                ]
                },
                "totalIpAddressCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "usedIpAddressCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "usedPercentage": {
                "type": [
                "string",
                "null",
                "number"
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

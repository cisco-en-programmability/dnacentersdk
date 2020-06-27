# -*- coding: utf-8 -*-
"""DNA Center Get Global Pool data model.

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


class JSONSchemaValidatorC0BcA85643C8B58D(object):
    """Get Global Pool request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC0BcA85643C8B58D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "description":
                "Response",
                "items": {
                "properties": {
                "clientOptions": {
                "description":
                "Client Options",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "configureExternalDhcp": {
                "description":
                "Configure External Dhcp",
                "type": [
                "string",
                "null"
                ]
                },
                "context": {
                "description":
                "Context",
                "items": {
                "properties": {
                "contextKey": {
                "description":
                "Context Key",
                "type": [
                "string",
                "null"
                ]
                },
                "contextValue": {
                "description":
                "Context Value",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "owner": {
                "description":
                "Owner",
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
                "description":
                "Create Time",
                "type": [
                "string",
                "null"
                ]
                },
                "dhcpServerIps": {
                "description":
                "Dhcp Server Ips",
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
                "description":
                "Dns Server Ips",
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
                "description":
                "Gateways",
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
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "ipPoolCidr": {
                "description":
                "Ip Pool Cidr",
                "type": [
                "string",
                "null"
                ]
                },
                "ipPoolName": {
                "description":
                "Ip Pool Name",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv6": {
                "description":
                "Ipv6",
                "type": [
                "string",
                "null"
                ]
                },
                "lastUpdateTime": {
                "description":
                "Last Update Time",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "overlapping": {
                "description":
                "Overlapping",
                "type": [
                "string",
                "null"
                ]
                },
                "owner": {
                "description":
                "Owner",
                "type": [
                "string",
                "null"
                ]
                },
                "parentUuid": {
                "description":
                "Parent Uuid",
                "type": [
                "string",
                "null"
                ]
                },
                "shared": {
                "description":
                "Shared",
                "type": [
                "string",
                "null"
                ]
                },
                "totalIpAddressCount": {
                "description":
                "Total Ip Address Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "usedIpAddressCount": {
                "description":
                "Used Ip Address Count",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "usedPercentage": {
                "description":
                "Used Percentage",
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
                "description":
                "Version",
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

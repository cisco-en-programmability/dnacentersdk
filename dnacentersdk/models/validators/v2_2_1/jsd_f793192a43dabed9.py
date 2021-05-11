# -*- coding: utf-8 -*-
"""DNA Center Create Global Pool data model.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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


class JSONSchemaValidatorF793192A43DaBed9(object):
    """Create Global Pool request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF793192A43DaBed9, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "settings": {
                "description":
                "Settings",
                "properties": {
                "ippool": {
                "description":
                "Ippool",
                "items": {
                "properties": {
                "IpAddressSpace": {
                "description":
                "Ip Address Space",
                "enum": [
                "IPv6 or IPv4",
                null
                ],
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
                "gateway": {
                "description":
                "Gateway",
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
                "type": {
                "description":
                "Type",
                "enum": [
                "Generic",
                "Tunnel",
                null
                ],
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
                "object"
                ]
                }
                },
                "required": [
                "settings"
                ],
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

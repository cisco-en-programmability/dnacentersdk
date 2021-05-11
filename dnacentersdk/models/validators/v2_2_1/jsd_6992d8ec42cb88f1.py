# -*- coding: utf-8 -*-
"""DNA Center Update Reserve IP Subpool data model.

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


class JSONSchemaValidator6992D8Ec42Cb88F1(object):
    """Update Reserve IP Subpool request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator6992D8Ec42Cb88F1, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "ipv4DhcpServers": {
                "description":
                "IPv4 input for dhcp server ip example: 1.1.1.1",
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
                "ipv4DnsServers": {
                "description":
                "IPv4 input for dns server ip  example: 4.4.4.4",
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
                "ipv6AddressSpace": {
                "type": [
                "boolean"
                ]
                },
                "ipv6DhcpServers": {
                "description":
                "IPv6 format dhcp server as input example :
                 2001:db8::1234",
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
                "ipv6DnsServers": {
                "description":
                "IPv6 format dns server input example:
                 2001:db8::1234",
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
                "ipv6GateWay": {
                "description":
                "Gateway ip address details, example:
                 2001:db8:85a3:0:100::1",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv6GlobalPool": {
                "description":
                "IP v6 Global pool address with cidr this is
                 required when Ipv6AddressSpace value is true,
                 example: 2001:db8:85a3::/64",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv6Prefix": {
                "type": [
                "boolean"
                ]
                },
                "ipv6PrefixLength": {
                "type": [
                "number",
                "null"
                ]
                },
                "ipv6Subnet": {
                "description":
                "IPv6 Subnet address, example
                 :2001:db8:85a3:0:100::",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv6TotalHost": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "description":
                "Name of the reserve ip sub pool",
                "type": [
                "string"
                ]
                },
                "slaacSupport": {
                "type": [
                "boolean",
                "null"
                ]
                }
                },
                "required": [
                "name",
                "ipv6AddressSpace",
                "ipv6Prefix"
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

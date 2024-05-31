# -*- coding: utf-8 -*-
"""Cisco DNA Center UpdateReserveIPSubpool data model.

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


class JSONSchemaValidatorFd6083B0C65D03B2D53F10B3Ece59D(object):
    """UpdateReserveIPSubpool request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorFd6083B0C65D03B2D53F10B3Ece59D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "ipv4DhcpServers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "ipv4DnsServers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "ipv6AddressSpace": {
                "type": "boolean"
                },
                "ipv6DhcpServers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "ipv6DnsServers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "ipv6GateWay": {
                "type": "string"
                },
                "ipv6GlobalPool": {
                "type": "string"
                },
                "ipv6Prefix": {
                "type": "boolean"
                },
                "ipv6PrefixLength": {
                "type": "integer"
                },
                "ipv6Subnet": {
                "type": "string"
                },
                "ipv6TotalHost": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "slaacSupport": {
                "type": "boolean"
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

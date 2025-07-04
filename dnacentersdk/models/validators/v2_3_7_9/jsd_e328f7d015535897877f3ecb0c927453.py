# -*- coding: utf-8 -*-
"""Cisco DNA Center UpdatesAnIPAddressSubpool data model.

Copyright (c) 2025 Cisco Systems.

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


class JSONSchemaValidatorE328F7D015535897877F3Ecb0C927453(object):
    """UpdatesAnIPAddressSubpool request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorE328F7D015535897877F3Ecb0C927453, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "ipV4AddressSpace": {
                "properties": {
                "dhcpServers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "dnsServers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "gatewayIpAddress": {
                "type": "string"
                },
                "globalPoolId": {
                "type": "string"
                },
                "prefixLength": {
                "type": "number"
                },
                "slaacSupport": {
                "type": "boolean"
                },
                "subnet": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "ipV6AddressSpace": {
                "properties": {
                "dhcpServers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "dnsServers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "gatewayIpAddress": {
                "type": "string"
                },
                "globalPoolId": {
                "type": "string"
                },
                "prefixLength": {
                "type": "number"
                },
                "slaacSupport": {
                "type": "boolean"
                },
                "subnet": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "poolType": {
                "enum": [
                "Generic",
                "LAN",
                "Management",
                "Service",
                "WAN"
                ],
                "type": "string"
                },
                "siteId": {
                "type": "string"
                }
                },
                "type": "object"
                }""".replace(
                    "\n" + " " * 16, ""
                )
            )
        )

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                "{} is invalid. Reason: {}".format(request, e.message)
            )

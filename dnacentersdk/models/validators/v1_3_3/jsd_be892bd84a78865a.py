# -*- coding: utf-8 -*-
"""DNA Center Create Network data model.

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


class JSONSchemaValidatorBe892Bd84A78865A(object):
    """Create Network request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorBe892Bd84A78865A, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "settings": {
                "description":
                "Settings",
                "properties": {
                "clientAndEndpoint_aaa": {
                "description":
                "Client And Endpoint Aaa",
                "properties": {
                "ipAddress": {
                "description":
                "Ip Address",
                "enum": [
                "Mandatory for ISE servers.",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "network": {
                "description":
                "Network",
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                "Protocol",
                "type": [
                "string",
                "null"
                ]
                },
                "servers": {
                "description":
                "Servers",
                "type": [
                "string",
                "null"
                ]
                },
                "sharedSecret": {
                "description":
                "Shared Secret",
                "enum": [
                "Supported only by ISE servers",
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
                "dhcpServer": {
                "description":
                "Dhcp Server",
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
                "dnsServer": {
                "description":
                "Dns Server",
                "properties": {
                "domainName": {
                "description":
                "Domain Name",
                "enum": [
                "can only contain alphanumeric characters or hyphen",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "primaryIpAddress": {
                "description":
                "Primary Ip Address",
                "enum": [
                "valid range : 1.0.0.0 - 223.255.255.255",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "secondaryIpAddress": {
                "description":
                "Secondary Ipaddress",
                "enum": [
                "valid range : 1.0.0.0 - 223.255.255.255",
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
                "messageOfTheday": {
                "description":
                "Message Of Theday",
                "properties": {
                "bannerMessage": {
                "description":
                "Banner Message",
                "type": [
                "string",
                "null"
                ]
                },
                "retainExistingBanner": {
                "type": [
                "boolean",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "netflowcollector": {
                "description":
                "Netflowcollector",
                "properties": {
                "ipAddress": {
                "description":
                "Ip Address",
                "type": [
                "string",
                "null"
                ]
                },
                "port": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "network_aaa": {
                "description":
                "Network Aaa",
                "properties": {
                "ipAddress": {
                "description":
                "Ip Address",
                "enum": [
                "Mandatory for ISE servers and for AAA consider this as additional Ip.",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "network": {
                "description":
                "Network",
                "enum": [
                "For AAA server consider it as primary IP and For ISE consider as Network",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                "Protocol",
                "type": [
                "string",
                "null"
                ]
                },
                "servers": {
                "description":
                "Servers",
                "enum": [
                "Server type supported by ISE and AAA",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "sharedSecret": {
                "description":
                "Shared Secret",
                "enum": [
                "Supported only by ISE servers",
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
                "ntpServer": {
                "description":
                "Ntp Server",
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
                "snmpServer": {
                "description":
                "Snmp Server",
                "properties": {
                "configureDnacIP": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "ipAddresses": {
                "description":
                "Ip Addresses",
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "syslogServer": {
                "description":
                "Syslog Server",
                "properties": {
                "configureDnacIP": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "ipAddresses": {
                "description":
                "Ip Addresses",
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "timezone": {
                "description":
                "Timezone",
                "type": [
                "string",
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

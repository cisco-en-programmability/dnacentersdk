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
                "additionalIp": {
                "description":
                "Additional IP for ISE server which is not
                 supported by AAA server.",
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
                "ipAddress": {
                "description":
                "IP address for ISE serve (eg: 1.1.1.4)",
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
                "IP address for AAA or ISE server (eg: 2.2.2.1)",
                "type": [
                "string",
                "null"
                ]
                },
                "protocol": {
                "description":
                "Protocol for AAA or ISE serve (eg: RADIUS)",
                "type": [
                "string",
                "null"
                ]
                },
                "servers": {
                "description":
                "Server type AAA or ISE server (eg: AAA)",
                "type": [
                "string",
                "null"
                ]
                },
                "sharedSecret": {
                "description":
                "Shared secret for ISE server",
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
                "Dhcp serve Ip (eg: 1.1.1.1)",
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
                "Dns server detail",
                "properties": {
                "domainName": {
                "description":
                "Domain name of DHCP (eg; cisco)",
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
                "Primary ip address for DHCP (eg: 2.2.2.2)",
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
                "Secondary ip address for DHCP (eg: 3.3.3.3)",
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
                "Message of the detail",
                "properties": {
                "bannerMessage": {
                "description":
                "Massage for banner message (eg; Good day)",
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
                "Net flow collector details",
                "properties": {
                "ipAddress": {
                "description":
                "IP address for netflow collector (eg: 3.3.3.1)",
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
                "AAA network settings detail",
                "properties": {
                "additionalIp": {
                "description":
                "Additional IP for ISE server which is not
                 supported by AAA server.",
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
                "ipAddress": {
                "description":
                "IP address for AAA and ISE server (eg: 1.1.1.1)",
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
                "IP address for AAA or ISE server (eg: 2.2.2.2)",
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
                "Protocol for AAA or ISE serve (eg: RADIUS)",
                "type": [
                "string",
                "null"
                ]
                },
                "servers": {
                "description":
                "Server type for AAA network (eg: AAA)",
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
                "Shared secret for ISE server",
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
                "IP address for NTP server (eg: 1.1.1.2)",
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
                "Snmp serve details",
                "properties": {
                "configureDnacIP": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "ipAddresses": {
                "description":
                "IP address for snmp server (eg: 4.4.4.1)",
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
                "Syslog server detail",
                "properties": {
                "configureDnacIP": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "ipAddresses": {
                "description":
                "IP address for syslog server (eg: 4.4.4.4)",
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
                "Input for time zone (eg: Africa/Abidjan (GMT))",
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

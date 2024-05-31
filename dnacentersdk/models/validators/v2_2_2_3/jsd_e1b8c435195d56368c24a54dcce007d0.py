# -*- coding: utf-8 -*-
"""Cisco DNA Center UpdateNetwork data model.

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


class JSONSchemaValidatorE1B8C435195D56368C24A54Dcce007D0(object):
    """UpdateNetwork request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE1B8C435195D56368C24A54Dcce007D0, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "settings": {
                "properties": {
                "clientAndEndpoint_aaa": {
                "properties": {
                "additionalIp": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "ipAddress": {
                "type": "string"
                },
                "network": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "servers": {
                "type": "string"
                },
                "sharedSecret": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "dhcpServer": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "dnsServer": {
                "properties": {
                "domainName": {
                "type": "string"
                },
                "primaryIpAddress": {
                "type": "string"
                },
                "secondaryIpAddress": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "messageOfTheday": {
                "properties": {
                "bannerMessage": {
                "type": "string"
                },
                "retainExistingBanner": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "netflowcollector": {
                "properties": {
                "ipAddress": {
                "type": "string"
                },
                "port": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "network_aaa": {
                "properties": {
                "additionalIp": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "ipAddress": {
                "type": "string"
                },
                "network": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "servers": {
                "type": "string"
                },
                "sharedSecret": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "ntpServer": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "snmpServer": {
                "properties": {
                "configureDnacIP": {
                "type": "boolean"
                },
                "ipAddresses": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "syslogServer": {
                "properties": {
                "configureDnacIP": {
                "type": "boolean"
                },
                "ipAddresses": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "timezone": {
                "type": "string"
                }
                },
                "type": "object"
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

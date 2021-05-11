# -*- coding: utf-8 -*-
"""DNA Center Create Device Credentials data model.

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


class JSONSchemaValidatorFbb95B37484A9Fce(object):
    """Create Device Credentials request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorFbb95B37484A9Fce, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "settings": {
                "description":
                "Settings",
                "properties": {
                "cliCredential": {
                "description":
                "Credential detail for CLI",
                "items": {
                "properties": {
                "description":
                 {
                "description":
                "Name or description for CLI credential",
                "type": [
                "string",
                "null"
                ]
                },
                "enablePassword": {
                "description":
                "Enable password for CLI credential",
                "type": [
                "string",
                "null"
                ]
                },
                "password": {
                "description":
                "Password for CLI credential",
                "type": [
                "string",
                "null"
                ]
                },
                "username": {
                "description":
                "User name for CLI credential",
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
                "httpsRead": {
                "description":
                "Http ready credential detail",
                "items": {
                "properties": {
                "name": {
                "description":
                "Name or description of http read credential",
                "type": [
                "string",
                "null"
                ]
                },
                "password": {
                "description":
                "Password for http read credential",
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
                },
                "username": {
                "description":
                "User name of the http read credential",
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
                "httpsWrite": {
                "description":
                "Http write credential detail",
                "items": {
                "properties": {
                "name": {
                "description":
                "Name or description of http write credential",
                "type": [
                "string",
                "null"
                ]
                },
                "password": {
                "description":
                "Password for http write credential",
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
                },
                "username": {
                "description":
                "User name of the http write credential",
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
                "snmpV2cRead": {
                "description":
                "Snmp v2 read credential detail",
                "items": {
                "properties": {
                "description":
                 {
                "description":
                "Description for snmp v2 read",
                "type": [
                "string",
                "null"
                ]
                },
                "readCommunity": {
                "description":
                "Ready community for snmp v2 read credential",
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
                "snmpV2cWrite": {
                "description":
                "Snmp v2 write credential detail",
                "items": {
                "properties": {
                "description":
                 {
                "description":
                "Description for snmp v2 write",
                "type": [
                "string",
                "null"
                ]
                },
                "writeCommunity": {
                "description":
                "Write community for snmp v2 write credential",
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
                "snmpV3": {
                "description":
                "Credential for SNMPv3",
                "items": {
                "properties": {
                "authPassword": {
                "description":
                "Authentication password for snmpv3 credential",
                "type": [
                "string",
                "null"
                ]
                },
                "authType": {
                "description":
                "Authentication type for snmpv3 credential",
                "enum": [
                "SHA",
                "MD5",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "description":
                 {
                "description":
                "Name or description for SNMPV3 credential",
                "type": [
                "string",
                "null"
                ]
                },
                "privacyPassword": {
                "description":
                "Privacy password for snmpv3 credential",
                "type": [
                "string",
                "null"
                ]
                },
                "privacyType": {
                "description":
                "Privacy type for snmpv3 credential",
                "enum": [
                "AES128",
                "DES",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "snmpMode": {
                "description":
                "Mode for snmpv3 credential",
                "enum": [
                "AUTHPRIV",
                "AUTHNOPRIV",
                "NOAUTHNOPRIV",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "username": {
                "description":
                "User name for SNMPv3 credential",
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

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
                "Cli Credential",
                "items": {
                "properties": {
                "description":
                 {
                "description":
                "Description",
                "type": [
                "string",
                "null"
                ]
                },
                "enablePassword": {
                "description":
                "Enable Password",
                "type": [
                "string",
                "null"
                ]
                },
                "password": {
                "description":
                "Password",
                "type": [
                "string",
                "null"
                ]
                },
                "username": {
                "description":
                "Username",
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
                "Https Read",
                "items": {
                "properties": {
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "password": {
                "description":
                "Password",
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
                "Username",
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
                "Https Write",
                "items": {
                "properties": {
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "password": {
                "description":
                "Password",
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
                "Username",
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
                "Snmp V2c Read",
                "items": {
                "properties": {
                "description":
                 {
                "description":
                "Description",
                "type": [
                "string",
                "null"
                ]
                },
                "readCommunity": {
                "description":
                "Read Community",
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
                "Snmp V2c Write",
                "items": {
                "properties": {
                "description":
                 {
                "description":
                "Description",
                "type": [
                "string",
                "null"
                ]
                },
                "writeCommunity": {
                "description":
                "Write Community",
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
                "Snmp V3",
                "items": {
                "properties": {
                "authPassword": {
                "description":
                "Auth Password",
                "type": [
                "string",
                "null"
                ]
                },
                "authType": {
                "description":
                "Auth Type",
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
                "Description",
                "type": [
                "string",
                "null"
                ]
                },
                "privacyPassword": {
                "description":
                "Privacy Password",
                "type": [
                "string",
                "null"
                ]
                },
                "privacyType": {
                "description":
                "Privacy Type",
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
                "Snmp Mode",
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
                "Username",
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

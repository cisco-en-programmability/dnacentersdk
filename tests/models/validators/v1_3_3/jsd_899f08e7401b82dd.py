# -*- coding: utf-8 -*-
"""DNA Center Get Device Credential Details data model.

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


class JSONSchemaValidator899F08E7401B82Dd(object):
    """Get Device Credential Details request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator899F08E7401B82Dd, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "cli": {
                "description":
                "Cli",
                "items": {
                "properties": {
                "comments": {
                "description":
                "Comments",
                "type": [
                "string",
                "null"
                ]
                },
                "credentialType": {
                "description":
                "Credential Type",
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
                "enablePassword": {
                "description":
                "Enable Password",
                "type": [
                "string",
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
                "instanceTenantId": {
                "description":
                "Instance Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "description":
                "Instance Uuid",
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
                "http_read": {
                "description":
                "Http Read",
                "items": {
                "properties": {
                "comments": {
                "description":
                "Comments",
                "type": [
                "string",
                "null"
                ]
                },
                "credentialType": {
                "description":
                "Credential Type",
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
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                "Instance Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "description":
                "Instance Uuid",
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
                "description":
                "Port",
                "type": [
                "string",
                "null"
                ]
                },
                "secure": {
                "description":
                "Secure",
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
                "http_write": {
                "description":
                "Http Write",
                "items": {
                "properties": {
                "comments": {
                "description":
                "Comments",
                "type": [
                "string",
                "null"
                ]
                },
                "credentialType": {
                "description":
                "Credential Type",
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
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                "Instance Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "description":
                "Instance Uuid",
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
                "description":
                "Port",
                "type": [
                "string",
                "null"
                ]
                },
                "secure": {
                "description":
                "Secure",
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
                "snmp_v2_read": {
                "description":
                "Snmp V2 Read",
                "items": {
                "properties": {
                "comments": {
                "description":
                "Comments",
                "type": [
                "string",
                "null"
                ]
                },
                "credentialType": {
                "description":
                "Credential Type",
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
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                "Instance Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "description":
                "Instance Uuid",
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
                "snmp_v2_write": {
                "description":
                "Snmp V2 Write",
                "items": {
                "properties": {
                "comments": {
                "description":
                "Comments",
                "type": [
                "string",
                "null"
                ]
                },
                "credentialType": {
                "description":
                "Credential Type",
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
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                "Instance Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "description":
                "Instance Uuid",
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
                "snmp_v3": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "comments": {
                "description":
                "Comments",
                "type": [
                "string",
                "null"
                ]
                },
                "credentialType": {
                "description":
                "Credential Type",
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
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                "Instance Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceUuid": {
                "description":
                "Instance Uuid",
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
                "type": [
                "string",
                "null"
                ]
                },
                "snmpMode": {
                "description":
                "Snmp Mode",
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

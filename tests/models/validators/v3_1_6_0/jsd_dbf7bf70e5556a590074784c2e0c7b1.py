# -*- coding: utf-8 -*-
"""Cisco Catalyst Center FetchesTheDiscoveryJobDetailsForTheGivenJobId data model.

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


class JSONSchemaValidatorDbf7Bf70E5556A590074784C2E0C7B1(object):
    """FetchesTheDiscoveryJobDetailsForTheGivenJobId request schema
    definition."""
    def __init__(self):
        super(JSONSchemaValidatorDbf7Bf70E5556A590074784C2E0C7B1, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "credentials": {
                "properties": {
                "cli": {
                "properties": {
                "description":
                 {
                "type": "string"
                },
                "globalCredentialIdList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "protocolOrder": {
                "enum": [
                "SSH,TELNET"
                ],
                "type": "string"
                },
                "username": {
                "type": "string"
                }
                },
                "required": [
                "description",
                "username"
                ],
                "type": "object"
                },
                "httpRead": {
                "properties": {
                "description":
                 {
                "type": "string"
                },
                "globalCredentialIdList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "port": {
                "type": "integer"
                },
                "protocol": {
                "type": "string"
                },
                "username": {
                "type": "string"
                }
                },
                "required": [
                "description",
                "username"
                ],
                "type": "object"
                },
                "httpWrite": {
                "properties": {
                "description":
                 {
                "type": "string"
                },
                "globalCredentialIdList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "port": {
                "type": "integer"
                },
                "protocol": {
                "type": "string"
                },
                "username": {
                "type": "string"
                }
                },
                "required": [
                "description",
                "username",
                "port"
                ],
                "type": "object"
                },
                "netconf": {
                "properties": {
                "description":
                 {
                "type": "string"
                },
                "globalCredentialIdList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "port": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "snmp": {
                "properties": {
                "retries": {
                "type": "integer"
                },
                "snmpV2Read": {
                "properties": {
                "description":
                 {
                "type": "string"
                },
                "globalCredentialIdList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "required": [
                "description"
                ],
                "type": "object"
                },
                "snmpV2Write": {
                "properties": {
                "description":
                 {
                "type": "string"
                },
                "globalCredentialIdList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "required": [
                "description"
                ],
                "type": "object"
                },
                "snmpV3": {
                "properties": {
                "authType": {
                "enum": [
                "SHA,MD5, SHA256"
                ],
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "globalCredentialIdList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "mode": {
                "enum": [
                "AUTHPRIV, AUTHNOPRIV, NOAUTHNOPRIV"
                ],
                "type": "string"
                },
                "privacyType": {
                "enum": [
                "AES128, AES192, AES256, CISCOAES192, CISCOAES256"
                ],
                "type": "string"
                },
                "username": {
                "type": "string"
                }
                },
                "required": [
                "description",
                "mode",
                "username"
                ],
                "type": "object"
                },
                "timeout": {
                "type": "integer"
                }
                },
                "required": [
                "snmpV2Read",
                "snmpV2Write",
                "snmpV3"
                ],
                "type": "object"
                }
                },
                "required": [
                "cli",
                "snmp"
                ],
                "type": "object"
                },
                "discoveryTypeDetails": {
                "properties": {
                "cidrAddress": {
                "properties": {
                "cidrPrefix": {
                "type": "string"
                },
                "cidrSuffix": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "hopCount": {
                "type": "integer"
                },
                "ipAddress": {
                "type": "string"
                },
                "range": {
                "items": {
                "properties": {
                "ipAddressEnd": {
                "type": "string"
                },
                "ipAddressStart": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "subnetFilter": {
                "properties": {
                "cidrAddress": {
                "properties": {
                "cidrPrefix": {
                "type": "string"
                },
                "cidrSuffix": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "ipAddress": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": {
                "enum": [
                "SINGLE,RANGE,CIDR,CDP,LLDP"
                ],
                "type": "string"
                }
                },
                "required": [
                "type"
                ],
                "type": "object"
                },
                "managementIpSelectionMethod": {
                "enum": [
                "DEFAULT, LOOPBACK"
                ],
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "onlyNewDevice": {
                "type": "boolean"
                },
                "updateManagementIp": {
                "type": "boolean"
                }
                },
                "required": [
                "name",
                "discoveryTypeDetails",
                "credentials"
                ],
                "type": "object"
                },
                "version": {
                "type": "string"
                }
                },
                "required": [
                "response",
                "version"
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

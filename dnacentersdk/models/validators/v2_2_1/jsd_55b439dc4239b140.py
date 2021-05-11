# -*- coding: utf-8 -*-
"""DNA Center Start discovery data model.

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


class JSONSchemaValidator55B439Dc4239B140(object):
    """Start discovery request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator55B439Dc4239B140, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "cdpLevel": {
                "type": [
                "number",
                "null"
                ]
                },
                "discoveryType": {
                "description":
                "Type of Discovery. 'SINGLE', 'RANGE', 'MULTI
                 RANGE', 'CDP', 'LLDP'",
                "type": [
                "string"
                ]
                },
                "enablePasswordList": {
                "description":
                "Enable Password of the devices to be discovered",
                "items": {
                "type": [
                "string",
                "null",
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "globalCredentialIdList": {
                "description":
                "Global Credential Ids to be used for discovery",
                "items": {
                "type": [
                "string",
                "null",
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "httpReadCredential": {
                "description":
                "HTTP Read Credential of the devices to be
                 discovered",
                "properties": {
                "password": {
                "description":
                "HTTP(S) password",
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
                "secure": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "username": {
                "description":
                "HTTP(S) username",
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
                "httpWriteCredential": {
                "description":
                "HTTP Write Credential of the devices to be
                 discovered",
                "properties": {
                "password": {
                "description":
                "HTTP(S) password",
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
                "secure": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "username": {
                "description":
                "HTTP(S) username",
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
                "ipAddressList": {
                "description":
                "IP Address of devices to be discovered. Ex:
                 '172.30.0.1' for SINGLE, CDP and LLDP;
                 '72.30.0.1-172.30.0.4' for RANGE;
                 '72.30.0.1-172.30.0.4,172.31.0.1-172.31.0.4' for
                 MULTI RANGE",
                "type": [
                "string"
                ]
                },
                "ipFilterList": {
                "description":
                "IP Addresses of the devices to be filtered out
                 during discovery",
                "items": {
                "type": [
                "string",
                "null",
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "lldpLevel": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "description":
                "Name of the discovery",
                "type": [
                "string"
                ]
                },
                "netconfPort": {
                "description":
                "Netconf Port. It will need valid SSH credentials
                 to work",
                "type": [
                "string",
                "null"
                ]
                },
                "passwordList": {
                "description":
                "Password of the devices to be discovered",
                "items": {
                "type": [
                "string",
                "null",
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "preferredMgmtIPMethod": {
                "description":
                "Preferred Management IP Method.'None' or
                 'UseLoopBack'. Default is 'None'",
                "type": [
                "string",
                "null"
                ]
                },
                "protocolOrder": {
                "description":
                "Order of protocol (ssh/telnet) in which device
                 connection will be tried. Ex: 'telnet': only
                 telnet; 'ssh,telnet': ssh with higher order than
                 telnet",
                "type": [
                "string",
                "null"
                ]
                },
                "retry": {
                "type": [
                "number",
                "null"
                ]
                },
                "snmpAuthPassphrase": {
                "description":
                "Auth Pass phrase for SNMP",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpAuthProtocol": {
                "description":
                "SNMP auth protocol. SHA' or 'MD5'",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpMode": {
                "description":
                "Mode of SNMP. 'AUTHPRIV' or 'AUTHNOPRIV' or
                 'NOAUTHNOPRIV'",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpPrivPassphrase": {
                "description":
                "Pass phrase for SNMP privacy",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpPrivProtocol": {
                "description":
                "SNMP privacy protocol. 'DES' or 'AES128'",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpROCommunity": {
                "description":
                "Snmp RO community of the devices to be discovered",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpROCommunityDesc": {
                "description":
                "Description for Snmp RO community",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpRWCommunity": {
                "description":
                "Snmp RW community of the devices to be discovered",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpRWCommunityDesc": {
                "description":
                "Description for Snmp RW community",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpUserName": {
                "description":
                "SNMP username of the device",
                "type": [
                "string",
                "null"
                ]
                },
                "snmpVersion": {
                "description":
                "Version of SNMP. v2 or v3",
                "type": [
                "string"
                ]
                },
                "timeout": {
                "type": [
                "number",
                "null"
                ]
                },
                "userNameList": {
                "description":
                "Username of the devices to be discovered",
                "items": {
                "type": [
                "string",
                "null",
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                }
                },
                "required": [
                "discoveryType",
                "ipAddressList",
                "name",
                "snmpVersion"
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

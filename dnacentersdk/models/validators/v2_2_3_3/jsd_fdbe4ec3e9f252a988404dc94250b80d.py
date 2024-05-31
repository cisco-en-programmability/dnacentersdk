# -*- coding: utf-8 -*-
"""Cisco DNA Center StartDiscovery data model.

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


class JSONSchemaValidatorFdbe4Ec3E9F252A988404Dc94250B80D(object):
    """StartDiscovery request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorFdbe4Ec3E9F252A988404Dc94250B80D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "cdpLevel": {
                "type": "integer"
                },
                "discoveryType": {
                "type": "string"
                },
                "enablePasswordList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "globalCredentialIdList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "httpReadCredential": {
                "properties": {
                "password": {
                "type": "string"
                },
                "port": {
                "type": "integer"
                },
                "secure": {
                "type": "boolean"
                },
                "username": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "httpWriteCredential": {
                "properties": {
                "password": {
                "type": "string"
                },
                "port": {
                "type": "integer"
                },
                "secure": {
                "type": "boolean"
                },
                "username": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "ipAddressList": {
                "type": "string"
                },
                "ipFilterList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "lldpLevel": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "netconfPort": {
                "type": "string"
                },
                "passwordList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "preferredMgmtIPMethod": {
                "type": "string"
                },
                "protocolOrder": {
                "type": "string"
                },
                "retry": {
                "type": "integer"
                },
                "snmpAuthPassphrase": {
                "type": "string"
                },
                "snmpAuthProtocol": {
                "type": "string"
                },
                "snmpMode": {
                "type": "string"
                },
                "snmpPrivPassphrase": {
                "type": "string"
                },
                "snmpPrivProtocol": {
                "type": "string"
                },
                "snmpROCommunity": {
                "type": "string"
                },
                "snmpROCommunityDesc": {
                "type": "string"
                },
                "snmpRWCommunity": {
                "type": "string"
                },
                "snmpRWCommunityDesc": {
                "type": "string"
                },
                "snmpUserName": {
                "type": "string"
                },
                "snmpVersion": {
                "type": "string"
                },
                "timeout": {
                "type": "integer"
                },
                "userNameList": {
                "items": {
                "type": "string"
                },
                "type": "array"
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

# -*- coding: utf-8 -*-
"""Cisco DNA Center AddAuthenticationAndPolicyServerAccessConfiguration data model.

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


class JSONSchemaValidatorFa3975Be5Af25501Abb40339D96917Eb(object):
    """AddAuthenticationAndPolicyServerAccessConfiguration request schema
    definition."""
    def __init__(self):
        super(JSONSchemaValidatorFa3975Be5Af25501Abb40339D96917Eb, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "accountingPort": {
                "type": "integer"
                },
                "authenticationPort": {
                "type": "integer"
                },
                "ciscoIseDtos": {
                "items": {
                "properties": {
                "description":
                 {
                "type": "string"
                },
                "fqdn": {
                "type": "string"
                },
                "ipAddress": {
                "type": "string"
                },
                "password": {
                "type": "string"
                },
                "sshkey": {
                "type": "string"
                },
                "subscriberName": {
                "type": "string"
                },
                "userName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "encryptionKey": {
                "type": "string"
                },
                "encryptionScheme": {
                "enum": [
                "KEYWRAP",
                "RADSEC"
                ],
                "type": "string"
                },
                "externalCiscoIseIpAddrDtos": {
                "items": {
                "properties": {
                "externalCiscoIseIpAddresses": {
                "items": {
                "properties": {
                "externalIpAddress": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "ipAddress": {
                "type": "string"
                },
                "isIseEnabled": {
                "type": "boolean"
                },
                "messageKey": {
                "type": "string"
                },
                "port": {
                "type": "integer"
                },
                "protocol": {
                "enum": [
                "TACACS",
                "RADIUS",
                "RADIUS_TACACS"
                ],
                "type": "string"
                },
                "pxgridEnabled": {
                "type": "boolean"
                },
                "retries": {
                "type": "string"
                },
                "role": {
                "type": "string"
                },
                "sharedSecret": {
                "type": "string"
                },
                "timeoutSeconds": {
                "type": "string"
                },
                "useDnacCertForPxgrid": {
                "type": "boolean"
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

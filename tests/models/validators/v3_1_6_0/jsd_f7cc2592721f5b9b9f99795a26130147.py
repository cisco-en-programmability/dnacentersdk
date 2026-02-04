# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetAuthenticationAndPolicyServers data model.

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


class JSONSchemaValidatorF7Cc2592721F5B9B9F99795A26130147(object):
    """GetAuthenticationAndPolicyServers request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF7Cc2592721F5B9B9F99795A26130147, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
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
                "externalCiscoIseIpAddrDtos": {
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
                "failureReason": {
                "type": "string"
                },
                "fqdn": {
                "type": "string"
                },
                "instanceUuid": {
                "type": "string"
                },
                "ipAddress": {
                "type": "string"
                },
                "password": {
                "type": "string"
                },
                "role": {
                "enum": [
                "PRIMARY",
                "SECONDARY",
                "PXGRID"
                ],
                "type": "string"
                },
                "sshkey": {
                "type": "string"
                },
                "subscriberName": {
                "type": "string"
                },
                "trustState": {
                "enum": [
                "TRUSTED",
                "UNTRUSTED",
                "INIT"
                ],
                "type": "string"
                },
                "type": {
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
                "instanceUuid": {
                "type": "string"
                },
                "ipAddress": {
                "type": "string"
                },
                "isIseEnabled": {
                "type": "boolean"
                },
                "iseEnabled": {
                "type": "boolean"
                },
                "messageKey": {
                "type": "string"
                },
                "multiDnacEnabled": {
                "type": "boolean"
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
                "rbacUuid": {
                "type": "string"
                },
                "retries": {
                "type": "integer"
                },
                "role": {
                "type": "string"
                },
                "sharedSecret": {
                "type": "string"
                },
                "state": {
                "enum": [
                "ACTIVE",
                "INACTIVE",
                "RBAC_SUCCESS",
                "RBAC_FAILURE",
                "DELETED",
                "FAILED",
                "INPROGRESS"
                ],
                "type": "string"
                },
                "timeoutSeconds": {
                "type": "integer"
                },
                "useDnacCertForPxgrid": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "version": {
                "type": "string"
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

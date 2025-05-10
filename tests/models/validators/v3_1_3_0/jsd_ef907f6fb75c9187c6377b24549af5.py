# -*- coding: utf-8 -*-
"""Cisco Catalyst Center RetrievesTheListOfMRPRingsV1 data model.

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


class JSONSchemaValidatorEf907F6Fb75C9187C6377B24549Af5(object):
    """RetrievesTheListOfMRPRingsV1 request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorEf907F6Fb75C9187C6377B24549Af5, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "response": {
                "items": {
                "properties": {
                "deviceDetails": {
                "items": {
                "properties": {
                "bestManagerHostName": {
                "type": "string"
                },
                "bestManagerMacAddress": {
                "type": "string"
                },
                "bestManagerPrority": {
                "type": "integer"
                },
                "configurationMode": {
                "enum": [
                "CLIENT",
                "MANAGER",
                "AUTOMANAGER"
                ],
                "type": "string"
                },
                "configuredFrom": {
                "type": "string"
                },
                "domainId": {
                "type": "string"
                },
                "domainName": {
                "type": "string"
                },
                "mrpLicense": {
                "type": "string"
                },
                "networkStatus": {
                "enum": [
                "OPEN",
                "CLOSED",
                "UNKNOWN"
                ],
                "type": "string"
                },
                "operationMode": {
                "enum": [
                "CLIENT",
                "MANAGER"
                ],
                "type": "string"
                },
                "ports": {
                "items": {
                "properties": {
                "interfaceName": {
                "type": "string"
                },
                "portMacAddress": {
                "type": "string"
                },
                "portNumber": {
                "enum": [
                "PORT1",
                "PORT2"
                ],
                "type": "integer"
                },
                "portStatus": {
                "enum": [
                "DISABLED",
                "FORWARDING",
                "BLOCKED",
                "NOTCONNECTED"
                ],
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "priority": {
                "type": "integer"
                },
                "recoveryTimeProfileMilliseconds": {
                "type": "string"
                },
                "topologyChangeRequestIntervalMilliseconds": {
                "type": "string"
                },
                "vlanId": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "id": {
                "type": "integer"
                },
                "networkDeviceId": {
                "type": "string"
                },
                "ringSize": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "version": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )

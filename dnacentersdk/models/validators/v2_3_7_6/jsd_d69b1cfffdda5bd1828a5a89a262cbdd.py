# -*- coding: utf-8 -*-
"""Cisco DNA Center CreateSNMPDestination data model.

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


class JSONSchemaValidatorD69B1CffFdda5Bd1828A5A89A262Cbdd(object):
    """CreateSNMPDestination request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD69B1CffFdda5Bd1828A5A89A262Cbdd, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "authPassword": {
                "type": "string"
                },
                "community": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "ipAddress": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "port": {
                "type": "string"
                },
                "privacyPassword": {
                "type": "string"
                },
                "snmpAuthType": {
                "enum": [
                "SHA",
                "MD5",
                "NONE"
                ],
                "type": "string"
                },
                "snmpMode": {
                "enum": [
                "AUTH_PRIVACY",
                "AUTH_NO_PRIVACY",
                "NO_AUTH_NO_PRIVACY",
                "NONE"
                ],
                "type": "string"
                },
                "snmpPrivacyType": {
                "enum": [
                "AES128",
                "DES",
                "NONE"
                ],
                "type": "string"
                },
                "snmpVersion": {
                "enum": [
                "V2C",
                "V3"
                ],
                "type": "string"
                },
                "userName": {
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

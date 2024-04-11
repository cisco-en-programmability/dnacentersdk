# -*- coding: utf-8 -*-
"""Cisco DNA Center Sensor Test Results data model.

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


class JSONSchemaValidator87Ae7B214F0BA838(object):
    """Sensor Test Results request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator87Ae7B214F0BA838, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "failureStats": {
                "items": {
                "properties": {
                "errorCode": {
                "type": [
                "number",
                "null"
                ]
                },
                "errorTitle": {
                "type": [
                "string",
                "null"
                ]
                },
                "testCategory": {
                "type": [
                "string",
                "null"
                ]
                },
                "testType": {
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
                "summary": {
                "properties": {
                "APP_CONNECTIVITY": {
                "properties": {
                "FILETRANSFER": {
                "properties": {
                "failCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "passCount": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "HOST_REACHABILITY": {
                "properties": {
                "failCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "passCount": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "WEBSERVER": {
                "properties": {
                "failCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "passCount": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "EMAIL": {
                "properties": {
                "MAILSERVER": {
                "properties": {
                "failCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "passCount": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "NETWORK_SERVICES": {
                "properties": {
                "DNS": {
                "properties": {
                "failCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "passCount": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "ONBOARDING": {
                "properties": {
                "ASSOC": {
                "properties": {
                "failCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "passCount": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "AUTH": {
                "properties": {
                "failCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "passCount": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "DHCP": {
                "properties": {
                "failCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "passCount": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "PERFORMANCE": {
                "properties": {
                "IPSLASENDER": {
                "properties": {
                "failCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "passCount": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "RF_ASSESSMENT": {
                "properties": {
                "DATA_RATE": {
                "properties": {
                "failCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "passCount": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "SNR": {
                "properties": {
                "failCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "passCount": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "totalTestCount": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
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

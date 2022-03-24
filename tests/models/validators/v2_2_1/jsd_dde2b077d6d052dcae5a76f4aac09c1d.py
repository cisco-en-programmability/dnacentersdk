# -*- coding: utf-8 -*-
"""Cisco DNA Center sensorTestResults data model.

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

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorDde2B077D6D052DcAe5A76F4Aac09C1D(object):
    """sensorTestResults request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorDde2B077D6D052DcAe5A76F4Aac09C1D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "failureStats": {
                "items": {
                "properties": {
                "errorCode": {
                "type": "integer"
                },
                "errorTitle": {
                "type": "string"
                },
                "testCategory": {
                "type": "string"
                },
                "testType": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "summary": {
                "properties": {
                "APP_CONNECTIVITY": {
                "properties": {
                "FILETRANSFER": {
                "properties": {
                "failCount": {
                "type": "integer"
                },
                "passCount": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "HOST_REACHABILITY": {
                "properties": {
                "failCount": {
                "type": "number"
                },
                "passCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "WEBSERVER": {
                "properties": {
                "failCount": {
                "type": "integer"
                },
                "passCount": {
                "type": "integer"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "EMAIL": {
                "properties": {
                "MAILSERVER": {
                "properties": {
                "failCount": {
                "type": "integer"
                },
                "passCount": {
                "type": "number"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "NETWORK_SERVICES": {
                "properties": {
                "DNS": {
                "properties": {
                "failCount": {
                "type": "number"
                },
                "passCount": {
                "type": "integer"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "ONBOARDING": {
                "properties": {
                "ASSOC": {
                "properties": {
                "failCount": {
                "type": "integer"
                },
                "passCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "AUTH": {
                "properties": {
                "failCount": {
                "type": "integer"
                },
                "passCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "DHCP": {
                "properties": {
                "failCount": {
                "type": "number"
                },
                "passCount": {
                "type": "integer"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "PERFORMANCE": {
                "properties": {
                "IPSLASENDER": {
                "properties": {
                "failCount": {
                "type": "integer"
                },
                "passCount": {
                "type": "integer"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "RF_ASSESSMENT": {
                "properties": {
                "DATA_RATE": {
                "properties": {
                "failCount": {
                "type": "integer"
                },
                "passCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "SNR": {
                "properties": {
                "failCount": {
                "type": "number"
                },
                "passCount": {
                "type": "integer"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "totalTestCount": {
                "type": "integer"
                }
                },
                "type": "object"
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

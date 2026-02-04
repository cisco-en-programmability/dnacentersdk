# -*- coding: utf-8 -*-
"""Cisco Catalyst Center CreateLSCCertificateRenewalProfile data model.

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


class JSONSchemaValidatorDa35060D4A15Da8B4C7D9176408Ca1E(object):
    """CreateLSCCertificateRenewalProfile request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorDa35060D4A15Da8B4C7D9176408Ca1E, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "CalendarProfileSetting": {
                "properties": {
                "duration": {
                "properties": {
                "schedulerDate": {
                "type": "string"
                },
                "schedulerDay": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "schedulerEndTime": {
                "type": "string"
                },
                "schedulerStartTime": {
                "type": "string"
                }
                },
                "required": [
                "schedulerStartTime"
                ],
                "type": "object"
                },
                "schedulerType": {
                "enum": [
                "DAILY, WEEKLY, MONTHLY"
                ],
                "type": "string"
                }
                },
                "required": [
                "schedulerType",
                "duration"
                ],
                "type": "object"
                },
                "lscProfileName": {
                "type": "string"
                },
                "renewalDueInDays": {
                "type": "integer"
                },
                "renewalType": {
                "enum": [
                "ONESHOT, STAGGERED"
                ],
                "type": "string"
                }
                },
                "required": [
                "renewalType",
                "renewalDueInDays"
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

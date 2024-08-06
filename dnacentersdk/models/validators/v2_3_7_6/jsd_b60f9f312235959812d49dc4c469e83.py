# -*- coding: utf-8 -*-
"""Cisco DNA Center UnMarkDeviceForReplacement data model.

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


class JSONSchemaValidatorB60F9F312235959812D49Dc4C469E83(object):
    """UnMarkDeviceForReplacement request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorB60F9F312235959812D49Dc4C469E83, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "creationTime": {
                "type": "integer"
                },
                "family": {
                "type": "string"
                },
                "faultyDeviceId": {
                "type": "string"
                },
                "faultyDeviceName": {
                "type": "string"
                },
                "faultyDevicePlatform": {
                "type": "string"
                },
                "faultyDeviceSerialNumber": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "neighbourDeviceId": {
                "type": "string"
                },
                "networkReadinessTaskId": {
                "type": "string"
                },
                "replacementDevicePlatform": {
                "type": "string"
                },
                "replacementDeviceSerialNumber": {
                "type": "string"
                },
                "replacementStatus": {
                "type": "string"
                },
                "replacementTime": {
                "type": "integer"
                },
                "workflowId": {
                "type": "string"
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

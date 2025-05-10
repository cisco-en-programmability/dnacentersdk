# -*- coding: utf-8 -*-
"""Cisco Catalyst Center RetrieveTheStatusOfAllTheDeviceReplacementWorkflowsV1 data model.

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


class JSONSchemaValidatorBaf2F1FbBb9456C79497Cb324764A3D0(object):
    """RetrieveTheStatusOfAllTheDeviceReplacementWorkflowsV1 request
    schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorBaf2F1FbBb9456C79497Cb324764A3D0, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
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
                "neighborDeviceId": {
                "type": "string"
                },
                "replacementDevicePlatform": {
                "type": "string"
                },
                "replacementDeviceSerialNumber": {
                "type": "string"
                },
                "replacementStatus": {
                "enum": [
                "MARKED_FOR_REPLACEMENT",
                "NETWORK_READINESS_REQUESTED",
                "NETWORK_READINESS_FAILED",
                "READY_FOR_REPLACEMENT",
                "REPLACEMENT_SCHEDULED",
                "REPLACEMENT_IN_PROGRESS",
                "REPLACED",
                "ERROR"
                ],
                "type": "string"
                },
                "replacementTime": {
                "type": "integer"
                },
                "workflow": {
                "properties": {
                "endTime": {
                "type": "integer"
                },
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "steps": {
                "items": {
                "properties": {
                "endTime": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "status": {
                "enum": [
                "INIT",
                "RUNNING",
                "SUCCESS",
                "FAILED",
                "ABORTED",
                "TIMEOUT"
                ],
                "type": "string"
                },
                "statusMessage": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "workflowStatus": {
                "enum": [
                "RUNNING",
                "SUCCESS",
                "FAILED"
                ],
                "type": "string"
                }
                },
                "type": "object"
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

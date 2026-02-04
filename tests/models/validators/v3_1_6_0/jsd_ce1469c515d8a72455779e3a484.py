# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetTheREPRingBasedOnTheRingId data model.

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


class JSONSchemaValidatorCe1469C515D8A72455779E3A484(object):
    """GetTheREPRingBasedOnTheRingId request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorCe1469C515D8A72455779E3A484, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "response": {
                "items": {
                "properties": {
                "deploymentMode": {
                "enum": [
                "FABRIC",
                "NON_FABRIC"
                ],
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "repSegmentId": {
                "type": "integer"
                },
                "ringMembers": {
                "items": {
                "properties": {
                "networkDeviceId": {
                "type": "string"
                },
                "nodeName": {
                "type": "string"
                },
                "portName1": {
                "type": "string"
                },
                "portName2": {
                "type": "string"
                },
                "ringOrder": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "ringName": {
                "type": "string"
                },
                "rootNeighbourNetworkDeviceIds": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "rootNetworkDeviceId": {
                "type": "string"
                },
                "status": {
                "enum": [
                "DISCOVERY_REQUEST_RECEIVED",
                "DISCOVERY_REQUEST_ACCEPTED",
                "REMAINING_PORT_CHANNEL_IN_PROGRESS",
                "REP_CONVERSION_IN_PROGRESS",
                "REP_CONVERSION_COMPLETED",
                "REP_CONVERSION_FAILED",
                "REP_RING_DELETE_REQUEST_RECEIVED",
                "REP_RING_DELETION_INPROGRESS",
                "REP_RING_DELETION_ABORTED",
                "REP_RING_DELETED",
                "REP_RING_DELETION_FAILED",
                "REP_RING_DELETED_WITH_ERRS",
                "DISCOVERY_REQUEST_COMPLETED"
                ],
                "type": "string"
                }
                },
                "required": [
                "id",
                "rootNetworkDeviceId",
                "rootNeighbourNetworkDeviceIds"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "version": {
                "type": "integer"
                }
                },
                "required": [
                "response",
                "version"
                ],
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

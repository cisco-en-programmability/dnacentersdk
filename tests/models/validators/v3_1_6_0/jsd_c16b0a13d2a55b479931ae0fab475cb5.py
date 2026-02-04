# -*- coding: utf-8 -*-
"""Cisco Catalyst Center FetchesTheDetailsOfAllTheDevicesDiscoveredByTheGivenJobIdAndDiscoveryId data
model.

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


class JSONSchemaValidatorC16B0A13D2A55B479931Ae0Fab475Cb5(object):
    """FetchesTheDetailsOfAllTheDevicesDiscoveredByTheGivenJobIdAndDiscov
    eryId request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC16B0A13D2A55B479931Ae0Fab475Cb5, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "discoveryStatus": {
                "enum": [
                "SUCCESS, UNREACHABLE\t, DISCARDED"
                ],
                "type": "string"
                },
                "hostname": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "managementIpAddress": {
                "type": "string"
                },
                "reachabilityFailureReason": {
                "type": "string"
                },
                "reachabilityStatus": {
                "enum": [
                "REACHABLE, ONLY_PING_REACHABLE, UNREACHABLE, UNKNOWN"
                ],
                "type": "string"
                },
                "status": {
                "enum": [
                "MANAGED, SYNC_NOT_STARTED, SYNC_INIT_FAILED, SYNC_PRECHECK_FAILED, SYNC_IN_PROGRESS, SYNC_INTERNAL_ERROR, SYNC_DISABLED, DELETING_DEVICE, UNDER_MAINTENANCE, QUARANTINED, UNASSOCIATED, UNREACHABLE, UNKNOWN "
                ],
                "type": "string"
                },
                "validationStatuses": {
                "properties": {
                "cli": {
                "enum": [
                "SUCCESS, FAILURE, NOT_PROVIDED, NOT_VALIDATED"
                ],
                "type": "string"
                },
                "http": {
                "enum": [
                "SUCCESS, FAILURE, NOT_PROVIDED, NOT_VALIDATED"
                ],
                "type": "string"
                },
                "netconf": {
                "enum": [
                "SUCCESS, FAILURE, NOT_PROVIDED, NOT_VALIDATED"
                ],
                "type": "string"
                },
                "ping": {
                "enum": [
                "SUCCESS, FAILURE, NOT_PROVIDED, NOT_VALIDATED"
                ],
                "type": "string"
                },
                "snmp": {
                "enum": [
                "SUCCESS, FAILURE, NOT_PROVIDED, NOT_VALIDATED"
                ],
                "type": "string"
                }
                },
                "required": [
                "ping",
                "cli",
                "snmp",
                "http",
                "netconf"
                ],
                "type": "object"
                }
                },
                "required": [
                "id",
                "managementIpAddress",
                "hostname",
                "discoveryStatus",
                "status",
                "reachabilityStatus",
                "validationStatuses"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "version": {
                "type": "string"
                }
                },
                "required": [
                "response",
                "version"
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

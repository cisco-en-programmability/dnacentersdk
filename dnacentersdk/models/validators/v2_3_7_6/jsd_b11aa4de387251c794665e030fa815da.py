# -*- coding: utf-8 -*-
"""Cisco DNA Center UpdateApplicationPolicyQueuingProfile data model.

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


class JSONSchemaValidatorB11Aa4De387251C794665E030Fa815Da(object):
    """UpdateApplicationPolicyQueuingProfile request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorB11Aa4De387251C794665E030Fa815Da, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "clause": {
                "items": {
                "properties": {
                "instanceId": {
                "type": "integer"
                },
                "interfaceSpeedBandwidthClauses": {
                "items": {
                "properties": {
                "instanceId": {
                "type": "integer"
                },
                "interfaceSpeed": {
                "enum": [
                "ALL",
                "HUNDRED_GBPS",
                "TEN_GBPS",
                "ONE_GBPS",
                "HUNDRED_MBPS",
                "TEN_MBPS",
                "ONE_MBPS"
                ],
                "type": "string"
                },
                "tcBandwidthSettings": {
                "items": {
                "properties": {
                "bandwidthPercentage": {
                "type": "integer"
                },
                "instanceId": {
                "type": "integer"
                },
                "trafficClass": {
                "enum": [
                "BROADCAST_VIDEO",
                "REAL_TIME_INTERACTIVE",
                "VOIP_TELEPHONY",
                "SCAVENGER",
                "TRANSACTIONAL_DATA",
                "MULTIMEDIA_CONFERENCING",
                "NETWORK_CONTROL",
                "MULTIMEDIA_STREAMING",
                "BEST_EFFORT",
                "SIGNALING",
                "BULK_DATA",
                "OPS_ADMIN_MGMT"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "isCommonBetweenAllInterfaceSpeeds": {
                "type": "boolean"
                },
                "tcDscpSettings": {
                "items": {
                "properties": {
                "dscp": {
                "type": "string"
                },
                "instanceId": {
                "type": "integer"
                },
                "trafficClass": {
                "enum": [
                "BROADCAST_VIDEO",
                "REAL_TIME_INTERACTIVE",
                "VOIP_TELEPHONY",
                "SCAVENGER",
                "TRANSACTIONAL_DATA",
                "MULTIMEDIA_CONFERENCING",
                "NETWORK_CONTROL",
                "MULTIMEDIA_STREAMING",
                "BEST_EFFORT",
                "SIGNALING",
                "BULK_DATA",
                "OPS_ADMIN_MGMT"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "type": {
                "enum": [
                "BANDWIDTH",
                "DSCP_CUSTOMIZATION"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "description":
                 {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "name": {
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

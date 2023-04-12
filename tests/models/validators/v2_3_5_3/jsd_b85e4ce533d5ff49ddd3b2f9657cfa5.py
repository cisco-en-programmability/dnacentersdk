# -*- coding: utf-8 -*-
"""Cisco DNA Center Applications data model.

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


class JSONSchemaValidatorB85E4Ce533D5Ff49Ddd3B2F9657Cfa5(object):
    """Applications request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorB85E4Ce533D5Ff49Ddd3B2F9657Cfa5, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "application": {
                "type": "string"
                },
                "applicationServerLatency": {
                "type": "object"
                },
                "averageThroughput": {
                "type": "number"
                },
                "businessRelevance": {
                "enum": [
                "business-irrelevant",
                "business-relevant",
                "default"
                ],
                "type": "string"
                },
                "clientIp": {
                "type": "string"
                },
                "clientMacAddress": {
                "type": "string"
                },
                "clientName": {
                "type": "string"
                },
                "clientNetworkLatency": {
                "type": "object"
                },
                "deviceType": {
                "enum": [
                "Wired",
                "Wireless"
                ],
                "type": "string"
                },
                "exporterFamily": {
                "type": "string"
                },
                "exporterIpAddress": {
                "type": "string"
                },
                "exporterName": {
                "type": "string"
                },
                "exporterUUID": {
                "type": "string"
                },
                "health": {
                "type": "integer"
                },
                "issueId": {
                "type": "string"
                },
                "issueName": {
                "type": "string"
                },
                "jitter": {
                "type": "object"
                },
                "location": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "networkLatency": {
                "type": "object"
                },
                "occurrences": {
                "type": "integer"
                },
                "operatingSystem": {
                "type": "string"
                },
                "packetLossPercent": {
                "type": "object"
                },
                "priority": {
                "type": "string"
                },
                "rootCause": {
                "type": "string"
                },
                "serverNetworkLatency": {
                "type": "object"
                },
                "severity": {
                "type": "string"
                },
                "summary": {
                "type": "string"
                },
                "timestamp": {
                "type": "integer"
                },
                "trafficClass": {
                "type": "string"
                },
                "usageBytes": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "totalCount": {
                "type": "integer"
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

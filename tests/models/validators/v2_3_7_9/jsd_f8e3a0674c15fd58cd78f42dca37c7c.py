# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetAuditlogParentRecords data model.

Copyright (c) 2024 Cisco Systems.

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


class JSONSchemaValidatorF8E3A0674C15Fd58Cd78F42Dca37C7C(object):
    """GetAuditlogParentRecords request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF8E3A0674C15Fd58Cd78F42Dca37C7C, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "additionalDetails": {
                "type": "object"
                },
                "category": {
                "type": "string"
                },
                "childCount": {
                "type": "number"
                },
                "ciscoDnaEventLink": {
                "type": "string"
                },
                "context": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "details": {
                "type": "object"
                },
                "domain": {
                "type": "string"
                },
                "eventHierarchy": {
                "type": "string"
                },
                "eventId": {
                "type": "string"
                },
                "i18n": {
                "type": "string"
                },
                "instanceId": {
                "type": "string"
                },
                "message": {
                "type": "string"
                },
                "messageParams": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "namespace": {
                "type": "string"
                },
                "network": {
                "type": "string"
                },
                "note": {
                "type": "string"
                },
                "parentInstanceId": {
                "type": "string"
                },
                "severity": {
                "type": "integer"
                },
                "source": {
                "type": "string"
                },
                "subDomain": {
                "type": "string"
                },
                "tags": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "tenantId": {
                "type": "string"
                },
                "timestamp": {
                "type": "integer"
                },
                "tntId": {
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "userId": {
                "type": "string"
                },
                "version": {
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

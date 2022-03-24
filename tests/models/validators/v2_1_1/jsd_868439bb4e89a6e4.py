# -*- coding: utf-8 -*-
"""Cisco DNA Center Get Issue Enrichment Details data model.

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


class JSONSchemaValidator868439Bb4E89A6E4(object):
    """Get Issue Enrichment Details request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator868439Bb4E89A6E4, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "issueDetails": {
                "properties": {
                "issue": {
                "items": {
                "properties": {
                "impactedHosts": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "issueCategory": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueDescription": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueEntity": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueEntityValue": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "issueId": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueName": {
                "type": [
                "string",
                "null"
                ]
                },
                "issuePriority": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueSeverity": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueSource": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueSummary": {
                "type": [
                "string",
                "null"
                ]
                },
                "issueTimestamp": {
                "type": [
                "number",
                "null"
                ]
                },
                "suggestedActions": {
                "items": {
                "properties": {
                "message": {
                "type": [
                "string",
                "null"
                ]
                },
                "steps": {
                "items": {},
                "type": [
                "array",
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

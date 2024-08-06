# -*- coding: utf-8 -*-
"""Cisco DNA Center Issues data model.

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


import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorAaEf3B519BA8B9Fb2Cbf43B985(object):
    """Issues request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorAaEf3B519BA8B9Fb2Cbf43B985, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "aiDriven": {
                "type": "string"
                },
                "category": {
                "type": "string"
                },
                "clientMac": {
                "type": "string"
                },
                "deviceId": {
                "type": "string"
                },
                "deviceRole": {
                "type": "string"
                },
                "issueId": {
                "type": "string"
                },
                "issue_occurence_count": {
                "type": "integer"
                },
                "last_occurence_time": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "priority": {
                "type": "string"
                },
                "siteId": {
                "type": "string"
                },
                "status": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "totalCount": {
                "type": "string"
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

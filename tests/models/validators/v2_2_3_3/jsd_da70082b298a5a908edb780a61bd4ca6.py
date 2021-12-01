# -*- coding: utf-8 -*-
"""Cisco DNA Center GetFailedITSMEvents data model.

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


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
import json
from dnacentersdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidatorDa70082B298A5A908Edb780A61Bd4Ca6(object):
    """GetFailedITSMEvents request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorDa70082B298A5A908Edb780A61Bd4Ca6, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "category": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "domain": {
                "type": "string"
                },
                "enrichmentInfo": {
                "properties": {
                "errorCode": {
                "type": "string"
                },
                "errorDescription": {
                "type": "string"
                },
                "eventStatus": {
                "type": "string"
                },
                "responseReceivedFromITSMSystem": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "eventId": {
                "type": "string"
                },
                "instanceId": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "severity": {
                "type": "string"
                },
                "source": {
                "type": "string"
                },
                "subDomain": {
                "type": "string"
                },
                "timestamp": {
                "type": "integer"
                },
                "type": {
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

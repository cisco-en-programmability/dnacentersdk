# -*- coding: utf-8 -*-
"""Cisco Catalyst Center UpdateAnExistingCondition data model.

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


class JSONSchemaValidatorC024BB00458248144753C93Dd8215(object):
    """UpdateAnExistingCondition request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC024BB00458248144753C93Dd8215, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "action": {
                "properties": {
                "doesNotMatchAction": {
                "enum": [
                "DO_NOT_RAISE_VIOLATION_AND_CONTINUE, DO_NOT_RAISE_VIOLATION_AND_STOP, RAISE_VIOLATION_AND_CONTINUE, RAISE_VIOLATION_AND_STOP"
                ],
                "type": "string"
                },
                "doesNotMatchViolationMessage": {
                "type": "string"
                },
                "doesNotMatchViolationMessageType": {
                "enum": [
                "DEFAULT_MESSAGE, CUSTOM_MESSAGE"
                ],
                "type": "string"
                },
                "doesNotMatchViolationSeverity": {
                "enum": [
                "CRITICAL, MAJOR, MINOR, WARNING, INFO"
                ],
                "type": "string"
                },
                "matchAction": {
                "enum": [
                "DO_NOT_RAISE_VIOLATION_AND_CONTINUE, DO_NOT_RAISE_VIOLATION_AND_STOP, RAISE_VIOLATION_AND_CONTINUE, RAISE_VIOLATION_AND_STOP"
                ],
                "type": "string"
                },
                "matchViolationMessage": {
                "type": "string"
                },
                "matchViolationMessageType": {
                "enum": [
                "DEFAULT_MESSAGE, CUSTOM_MESSAGE"
                ],
                "type": "string"
                },
                "matchViolationSeverity": {
                "enum": [
                "CRITICAL, MAJOR, MINOR, WARNING, INFO"
                ],
                "type": "string"
                }
                },
                "required": [
                "matchAction",
                "doesNotMatchAction"
                ],
                "type": "object"
                },
                "blockEndExpression": {
                "type": "string"
                },
                "blockStartExpression": {
                "type": "string"
                },
                "blockViolationCriteria": {
                "enum": [
                "RAISE_FOR_EACH_VIOLATION, RAISE_SINGLE_FOR_ANY_VIOLATION, RAISE_IF_ALL_VIOLATED"
                ],
                "type": "string"
                },
                "deviceProperty": {
                "enum": [
                "DEVICE_NAME, IP_ADDRESS, OS_NAME, OS_VERSION"
                ],
                "type": "string"
                },
                "operator": {
                "enum": [
                "CONTAINS_STRING, DOES_NOT_CONTAIN_STRING, MATCHES_EXPRESSION, DOES_NOT_MATCH_EXPRESSION, EVALUATE_EXPRESSION"
                ],
                "type": "string"
                },
                "parseAsBlocks": {
                "type": "boolean"
                },
                "regexViolationCriteria": {
                "enum": [
                "RAISE_FOR_EACH_VIOLATION, RAISE_SINGLE_FOR_ANY_VIOLATION, RAISE_IF_ALL_VIOLATED"
                ],
                "type": "string"
                },
                "scope": {
                "enum": [
                "CONFIGURATION, DEVICE_PROPERTIES, DEVICE_COMMAND_OUTPUT, PREVIOUSLY_MATCHED_BLOCKS"
                ],
                "type": "string"
                },
                "showCommand": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "required": [
                "scope",
                "operator",
                "value",
                "action"
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

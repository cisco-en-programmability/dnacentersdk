# -*- coding: utf-8 -*-
"""Cisco Catalyst Center SecurityServiceInsertionReadinessV1 data model.

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


class JSONSchemaValidatorC763EB5C55E9A9F3460F27Ba14821(object):
    """SecurityServiceInsertionReadinessV1 request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC763EB5C55E9A9F3460F27Ba14821, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "accessControlDetails": {
                "properties": {
                "accessControlAppPkgStatus": {
                "enum": [
                "INSTALLED, NOT_INSTALLED"
                ],
                "type": "string"
                },
                "fabricSitesCount": {
                "type": "integer"
                },
                "readiness": {
                "enum": [
                "READY, NOT_READy"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "ise": {
                "properties": {
                "integrationStatus": {
                "enum": [
                "INTEGRATED, NOT_INTEGRATED"
                ],
                "type": "string"
                },
                "readiness": {
                "enum": [
                "READY, NOT_READY"
                ],
                "type": "string"
                },
                "syncStatus": {
                "enum": [
                "SYNCHRONIZED, NOT_SYNCHRONIZED"
                ],
                "type": "string"
                },
                "version": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "readiness": {
                "enum": [
                "READY, NOT_READY"
                ],
                "type": "string"
                },
                "securityGroup": {
                "properties": {
                "readiness": {
                "enum": [
                "READY, NOT_READY"
                ],
                "type": "string"
                },
                "securityGroupsCount": {
                "type": "integer"
                },
                "sgtManagedBy": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
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

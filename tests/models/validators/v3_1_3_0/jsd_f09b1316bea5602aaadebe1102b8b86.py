# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetAllBackupV1 data model.

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


class JSONSchemaValidatorF09B1316Bea5602AaadEbe1102B8B86(object):
    """GetAllBackupV1 request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF09B1316Bea5602AaadEbe1102B8B86, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "filter": {
                "type": "object"
                },
                "page": {
                "type": "object"
                },
                "response": {
                "items": {
                "properties": {
                "compatibilityError": {
                "items": {
                "properties": {
                "endDate": {
                "type": "string"
                },
                "namespace": {
                "type": "string"
                },
                "response": {
                "type": "object"
                },
                "serviceName": {
                "type": "string"
                },
                "startDate": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "context": {
                "type": "object"
                },
                "createdBy": {
                "type": "string"
                },
                "createdDate": {
                "type": "string"
                },
                "duration": {
                "type": "integer"
                },
                "endDate": {
                "type": "string"
                },
                "fipsEnabled": {
                "type": "boolean"
                },
                "id": {
                "type": "string"
                },
                "installedPackages": {
                "items": {
                "properties": {
                "displayName": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "version": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "internetProtocolVersion": {
                "enum": [
                "ipv4",
                "ipv6"
                ],
                "type": "string"
                },
                "isBackupAvailable": {
                "type": "boolean"
                },
                "isCompatible": {
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "numberOfNodes": {
                "type": "integer"
                },
                "productType": {
                "type": "string"
                },
                "productVersion": {
                "type": "string"
                },
                "releaseDisplayName": {
                "type": "string"
                },
                "releaseDisplayVersion": {
                "type": "string"
                },
                "releaseName": {
                "type": "string"
                },
                "releaseVersion": {
                "type": "string"
                },
                "scope": {
                "enum": [
                "CISCO_DNA_DATA_WITH_ASSURANCE",
                "CISCO_DNA_DATA_WITHOUT_ASSURANCE"
                ],
                "type": "string"
                },
                "size": {
                "type": "integer"
                },
                "status": {
                "type": "string"
                },
                "storage": {
                "type": "object"
                },
                "versions": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
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

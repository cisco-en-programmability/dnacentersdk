# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetTemplateVersionsV1 data model.

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


class JSONSchemaValidatorB2B1616094B5091812B0E412B8982E7(object):
    """GetTemplateVersionsV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorB2B1616094B5091812B0E412B8982E7, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "CompositeTemplate": {
                "properties": {
                "author": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "failurePolicy": {
                "enum": [
                "CONTINUE_ON_ERROR",
                "ABORT_TARGET_ON_ERROR"
                ],
                "type": "string"
                },
                "lastUpdateTime": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "products": {
                "items": {
                "properties": {
                "productFamily": {
                "type": "string"
                },
                "productName": {
                "type": "string"
                },
                "productSeries": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "projectId": {
                "type": "string"
                },
                "softwareFamily": {
                "enum": [
                "IOS",
                "IOS_XE",
                "IOS_XR",
                "NX_OS",
                "CISCO_CONTROLLER",
                "WIDE_AREA_APPLICATION_SERVICES",
                "NFV_OS",
                "OTHER"
                ],
                "type": "string"
                },
                "templateId": {
                "type": "string"
                },
                "type": {
                "enum": [
                "COMPOSITE"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "RegularTemplate": {
                "properties": {
                "author": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "language": {
                "enum": [
                "JINJA",
                "VELOCITY"
                ],
                "type": "string"
                },
                "lastUpdateTime": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "products": {
                "items": {
                "properties": {
                "productFamily": {
                "type": "string"
                },
                "productName": {
                "type": "string"
                },
                "productSeries": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "projectId": {
                "type": "string"
                },
                "softwareFamily": {
                "enum": [
                "IOS",
                "IOS_XE",
                "IOS_XR",
                "NX_OS",
                "CISCO_CONTROLLER",
                "WIDE_AREA_APPLICATION_SERVICES",
                "NFV_OS",
                "OTHER"
                ],
                "type": "string"
                },
                "templateContent": {
                "type": "string"
                },
                "templateId": {
                "type": "string"
                },
                "type": {
                "enum": [
                "REGULAR"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "version": {
                "type": "integer"
                },
                "versionId": {
                "type": "string"
                },
                "versionTime": {
                "type": "number"
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
                }""".replace(
                    "\n" + " " * 16, ""
                )
            )
        )

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                "{} is invalid. Reason: {}".format(request, e.message)
            )

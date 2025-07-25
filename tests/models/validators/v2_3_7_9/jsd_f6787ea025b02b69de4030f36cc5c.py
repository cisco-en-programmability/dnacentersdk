# -*- coding: utf-8 -*-
"""Cisco Catalyst Center RetrieveApplicableAddOnImagesForTheGivenSoftwareImageV1 data model.

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


class JSONSchemaValidatorF6787Ea025B02B69DE4030F36Cc5C(object):
    """RetrieveApplicableAddOnImagesForTheGivenSoftwareImageV1 request
    schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorF6787Ea025B02B69DE4030F36Cc5C, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "ciscoLatest": {
                "type": "boolean"
                },
                "goldenTaggingDetails": {
                "items": {
                "properties": {
                "deviceRoles": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "deviceTags": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "inheritedSiteId": {
                "type": "string"
                },
                "inheritedSiteName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "hasAddonImages": {
                "type": "boolean"
                },
                "id": {
                "type": "string"
                },
                "imageType": {
                "enum": [
                "SYSTEM",
                "SMU",
                "SUBPACKAGE",
                "PSIRT_SMU",
                "APSP",
                "APDP",
                "ROMMON_SW"
                ],
                "type": "string"
                },
                "imported": {
                "type": "boolean"
                },
                "integrityStatus": {
                "enum": [
                "VERIFIED",
                "UNKNOWN"
                ],
                "type": "string"
                },
                "isAddonImage": {
                "type": "boolean"
                },
                "isGoldenTagged": {
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "productNames": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "productName": {
                "type": "string"
                },
                "productNameOrdinal": {
                "type": "number"
                },
                "supervisorProductName": {
                "type": "string"
                },
                "supervisorProductNameOrdinal": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "recommended": {
                "enum": [
                "CISCO",
                "UNKNOWN"
                ],
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

# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetTheListOfNetworkDevicesWithImageDetailsV1 data model.

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


class JSONSchemaValidatorE39B6621058569039Ee9A6E935145(object):
    """GetTheListOfNetworkDevicesWithImageDetailsV1 request schema
    definition."""

    def __init__(self):
        super(JSONSchemaValidatorE39B6621058569039Ee9A6E935145, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "compatibleFeatures": {
                "items": {
                "properties": {
                "key": {
                "type": "string"
                },
                "value": {
                "enum": [
                "ENABLE",
                "DISABLE"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "goldenImages": {
                "items": {
                "properties": {
                "goldenTaggingDetails": {
                "properties": {
                "deviceRoles": {
                "enum": [
                "CORE",
                "DISTRIBUTION",
                "UNKNOWN",
                "ACCESS",
                "BORDER_ROUTER"
                ],
                "type": "string"
                },
                "deviceTags": {
                "type": "string"
                },
                "isInherited": {
                "type": "boolean"
                },
                "siteId": {
                "type": "string"
                },
                "siteName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "imageType": {
                "enum": [
                "SYSTEM",
                "SMU",
                "PSIRT_SMU",
                "SUBPACKAGE",
                "ROMMON_SW",
                "APDP",
                "APSP"
                ],
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
                "id": {
                "type": "string"
                },
                "installedImages": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "imageType": {
                "enum": [
                "SYSTEM",
                "SMU",
                "PSIRT_SMU",
                "SUBPACKAGE",
                "ROMMON_SW",
                "APDP",
                "APSP"
                ],
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
                "managementAddress": {
                "type": "string"
                },
                "networkDevice": {
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
                "networkDeviceImageStatus": {
                "enum": [
                "OUTDATED",
                "UP_TO_DATE",
                "UNKNOWN",
                "CONFLICTED",
                "UNSUPPORTED"
                ],
                "type": "string"
                },
                "networkDeviceUpdateStatus": {
                "enum": [
                "DISTRIBUTION_PENDING",
                "DISTRIBUTION_IN_PROGRESS",
                "DISTRIBUTION_FAILED",
                "ACTIVATION_PENDING",
                "ACTIVATION_IN_PROGRESS",
                "ACTIVATION_FAILED",
                "DEVICE_UP_TO_DATE",
                "UNKNOWN"
                ],
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

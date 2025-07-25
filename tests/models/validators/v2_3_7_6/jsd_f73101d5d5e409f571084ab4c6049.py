# -*- coding: utf-8 -*-
"""Cisco DNA Center GetSoftwareImageDetailsV1 data model.

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


class JSONSchemaValidatorF73101D5D5E409F571084Ab4C6049(object):
    """GetSoftwareImageDetailsV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorF73101D5D5E409F571084Ab4C6049, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "applicableDevicesForImage": {
                "items": {
                "properties": {
                "mdfId": {
                "type": "string"
                },
                "productId": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "productName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "applicationType": {
                "type": "string"
                },
                "createdTime": {
                "type": "string"
                },
                "extendedAttributes": {
                "type": "object"
                },
                "family": {
                "type": "string"
                },
                "feature": {
                "type": "string"
                },
                "fileServiceId": {
                "type": "string"
                },
                "fileSize": {
                "type": "string"
                },
                "imageIntegrityStatus": {
                "type": "string"
                },
                "imageName": {
                "type": "string"
                },
                "imageSeries": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "imageSource": {
                "type": "string"
                },
                "imageType": {
                "type": "string"
                },
                "imageUuid": {
                "type": "string"
                },
                "importSourceType": {
                "enum": [
                "DEVICE",
                "REMOTEURL",
                "CCO",
                "FILESYSTEM"
                ],
                "type": "string"
                },
                "isTaggedGolden": {
                "type": "boolean"
                },
                "md5Checksum": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "profileInfo": {
                "items": {
                "properties": {
                "description":
                 {
                "type": "string"
                },
                "extendedAttributes": {
                "type": "object"
                },
                "memory": {
                "type": "integer"
                },
                "productType": {
                "type": "string"
                },
                "profileName": {
                "type": "string"
                },
                "shares": {
                "type": "integer"
                },
                "vCpu": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "shaCheckSum": {
                "type": "string"
                },
                "vendor": {
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

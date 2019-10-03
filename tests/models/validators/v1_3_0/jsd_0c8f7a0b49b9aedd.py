# -*- coding: utf-8 -*-
"""DNA Center Get software image details data model.

Copyright (c) 2019 Cisco and/or its affiliates.

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


class JSONSchemaValidator0C8F7A0B49B9Aedd(object):
    """Get software image details request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator0C8F7A0B49B9Aedd, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "description":
                 "",
                "items": {
                "properties": {
                "applicableDevicesForImage": {
                "description":
                 "",
                "items": {
                "properties": {
                "mdfId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "productId": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "productName": {
                "description":
                 "",
                "type": [
                "string",
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
                },
                "applicationType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "createdTime": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "extendedAttributes": {
                "description":
                 "",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "family": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "feature": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "fileServiceId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "fileSize": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "imageIntegrityStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "imageName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "imageSeries": {
                "description":
                 "",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "imageSource": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "imageType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "imageUuid": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "importSourceType": {
                "description":
                 "",
                "enum": [
                "DEVICE",
                "REMOTEURL",
                "CCO",
                "FILESYSTEM",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "isTaggedGolden": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "md5Checksum": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "profileInfo": {
                "description":
                 "",
                "items": {
                "properties": {
                "description":
                 {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "extendedAttributes": {
                "description":
                 "",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "memory": {
                "type": [
                "number",
                "null"
                ]
                },
                "productType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "profileName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "shares": {
                "type": [
                "number",
                "null"
                ]
                },
                "vCpu": {
                "type": [
                "number",
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
                },
                "shaCheckSum": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "vendor": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "version": {
                "description":
                 "",
                "type": [
                "string",
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
                "null",
                "object"
                ]
                },
                "version": {
                "description":
                 "",
                "type": [
                "string",
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

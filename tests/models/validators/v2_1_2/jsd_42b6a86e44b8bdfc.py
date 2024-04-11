# -*- coding: utf-8 -*-
"""Cisco DNA Center Get list of files data model.

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


class JSONSchemaValidator42B6A86E44B8Bdfc(object):
    """Get list of files request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator42B6A86E44B8Bdfc, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "items": {
                "properties": {
                "attributeInfo": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "downloadPath": {
                "type": [
                "string",
                "null"
                ]
                },
                "encrypted": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "fileFormat": {
                "type": [
                "string",
                "null"
                ]
                },
                "fileSize": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "md5Checksum": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "nameSpace": {
                "type": [
                "string",
                "null"
                ]
                },
                "sftpServerList": {
                "items": {
                "type": [
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "sha1Checksum": {
                "type": [
                "string",
                "null"
                ]
                },
                "taskId": {}
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
                "version": {
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

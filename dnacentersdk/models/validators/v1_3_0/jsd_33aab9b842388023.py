# -*- coding: utf-8 -*-
"""DNA Center Update Site data model.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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


class JSONSchemaValidator33AaB9B842388023(object):
    """Update Site request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator33AaB9B842388023, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "site": {
                "description":
                "Site",
                "properties": {
                "area": {
                "description":
                "Area",
                "properties": {
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "parentName": {
                "description":
                "Parent Name",
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
                "building": {
                "description":
                "Building",
                "properties": {
                "address": {
                "description":
                "Address",
                "type": [
                "string",
                "null"
                ]
                },
                "latitude": {
                "type": [
                "number",
                "null"
                ]
                },
                "longitude": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "parentName": {
                "description":
                "Parent Name",
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
                "floor": {
                "description":
                "Floor",
                "properties": {
                "height": {
                "type": [
                "number",
                "null"
                ]
                },
                "length": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "rfModel": {
                "description":
                "Rf Model",
                "enum": [
                "Cubes And Walled Offices",
                "Drywall Office Only",
                "Indoor High Ceiling",
                "Outdoor Open Space",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "width": {
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
                }
                },
                "type": [
                "object"
                ]
                },
                "type": {
                "description":
                "Type",
                "enum": [
                "area",
                "building",
                "floor",
                null
                ],
                "type": [
                "string"
                ]
                }
                },
                "required": [
                "type",
                "site"
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

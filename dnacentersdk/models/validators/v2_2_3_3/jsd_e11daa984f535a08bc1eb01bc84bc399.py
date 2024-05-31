# -*- coding: utf-8 -*-
"""Cisco DNA Center ClaimADeviceToASite data model.

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


import fastjsonschema
import json
from dnacentersdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidatorE11Daa984F535A08Bc1EB01Bc84Bc399(object):
    """ClaimADeviceToASite request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE11Daa984F535A08Bc1EB01Bc84Bc399, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "configInfo": {
                "properties": {
                "configId": {
                "type": "string"
                },
                "configParameters": {
                "items": {
                "properties": {
                "key": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "deviceId": {
                "type": "string"
                },
                "gateway": {
                "type": "string"
                },
                "hostname": {
                "type": "string"
                },
                "imageId": {
                "type": "string"
                },
                "imageInfo": {
                "properties": {
                "imageId": {
                "type": "string"
                },
                "removeInactive": {
                "type": "boolean"
                },
                "skip": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "ipInterfaceName": {
                "type": "string"
                },
                "rfProfile": {
                "type": "string"
                },
                "siteId": {
                "type": "string"
                },
                "staticIP": {
                "type": "string"
                },
                "subnetMask": {
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "vlanId": {
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

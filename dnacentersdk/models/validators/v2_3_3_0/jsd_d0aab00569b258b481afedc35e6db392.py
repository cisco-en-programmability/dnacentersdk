# -*- coding: utf-8 -*-
"""Cisco DNA Center ProvisionUpdate data model.

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


class JSONSchemaValidatorD0Aab00569B258B481AfEdc35E6Db392(object):
    """ProvisionUpdate request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD0Aab00569B258B481AfEdc35E6Db392, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "deviceName": {
                "type": "string"
                },
                "dynamicInterfaces": {
                "items": {
                "properties": {
                "interfaceGateway": {
                "type": "string"
                },
                "interfaceIPAddress": {
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "interfaceNetmaskInCIDR": {
                "type": "integer"
                },
                "lagOrPortNumber": {
                "type": "integer"
                },
                "vlanId": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "managedAPLocations": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )

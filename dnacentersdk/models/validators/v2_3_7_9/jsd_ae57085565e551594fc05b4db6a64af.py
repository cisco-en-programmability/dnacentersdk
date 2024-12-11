# -*- coding: utf-8 -*-
"""Cisco Catalyst Center AddTransitNetworksV1 data model.

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


class JSONSchemaValidatorAe57085565E551594Fc05B4Db6A64Af(object):
    """AddTransitNetworksV1 request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorAe57085565E551594Fc05B4Db6A64Af, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "ipTransitSettings": {
                "properties": {
                "autonomousSystemNumber": {
                "type": "string"
                },
                "routingProtocolName": {
                "enum": [
                "BGP"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "sdaTransitSettings": {
                "properties": {
                "controlPlaneNetworkDeviceIds": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "isMulticastOverTransitEnabled": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": {
                "enum": [
                "IP_BASED_TRANSIT",
                "SDA_LISP_PUB_SUB_TRANSIT",
                "SDA_LISP_BGP_TRANSIT"
                ],
                "type": "string"
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

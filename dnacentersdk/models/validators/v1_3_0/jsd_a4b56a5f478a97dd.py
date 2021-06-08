# -*- coding: utf-8 -*-
"""Cisco DNA Center Adds border device in SDA Fabric data model.

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


class JSONSchemaValidatorA4B56A5F478A97Dd(object):
    """Adds border device in SDA Fabric request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorA4B56A5F478A97Dd, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "items": {
                "properties": {
                "borderSessionType": {
                "type": [
                "string",
                "null"
                ]
                },
                "connectedToInternet": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "deviceManagementIpAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "externalConnectivityIpPoolName": {
                "type": [
                "string",
                "null"
                ]
                },
                "externalConnectivitySettings": {
                "items": {
                "properties": {
                "externalAutonomouSystemNumber": {
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceName": {
                "type": [
                "string",
                "null"
                ]
                },
                "l3Handoff": {
                "items": {
                "properties": {
                "virtualNetwork": {
                "properties": {
                "virtualNetworkName": {
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
                "externalDomainRoutingProtocolName": {
                "type": [
                "string",
                "null"
                ]
                },
                "internalAutonomouSystemNumber": {
                "type": [
                "string",
                "null"
                ]
                },
                "siteHierarchy": {
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

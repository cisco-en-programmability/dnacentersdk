# -*- coding: utf-8 -*-
"""Cisco DNA Center GetWirelessLanControllerDetailsById data model.

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


class JSONSchemaValidatorC01Ee650Fcf858789Ca00C8Deda969B9(object):
    """GetWirelessLanControllerDetailsById request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC01Ee650Fcf858789Ca00C8Deda969B9, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "adminEnabledPorts": {
                "items": {
                "type": "integer"
                },
                "type": "array"
                },
                "apGroupName": {
                "type": "string"
                },
                "deviceId": {
                "type": "string"
                },
                "ethMacAddress": {
                "type": "string"
                },
                "flexGroupName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instanceTenantId": {
                "type": "string"
                },
                "instanceUuid": {
                "type": "string"
                },
                "lagModeEnabled": {
                "type": "boolean"
                },
                "netconfEnabled": {
                "type": "boolean"
                },
                "wirelessLicenseInfo": {
                "enum": [
                "ADVANTAGE",
                "ESSENTIALS"
                ],
                "type": "string"
                },
                "wirelessPackageInstalled": {
                "type": "boolean"
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

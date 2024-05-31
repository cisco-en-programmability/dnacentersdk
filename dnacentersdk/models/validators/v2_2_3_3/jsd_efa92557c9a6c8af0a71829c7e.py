# -*- coding: utf-8 -*-
"""Cisco DNA Center DeployTemplate data model.

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


class JSONSchemaValidatorEfA92557C9A6C8Af0A71829C7E(object):
    """DeployTemplate request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorEfA92557C9A6C8Af0A71829C7E, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "forcePushTemplate": {
                "type": "boolean"
                },
                "isComposite": {
                "type": "boolean"
                },
                "mainTemplateId": {
                "type": "string"
                },
                "memberTemplateDeploymentInfo": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "targetInfo": {
                "items": {
                "properties": {
                "hostName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "params": {
                "type": "object"
                },
                "resourceParams": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "type": {
                "enum": [
                "MANAGED_DEVICE_IP",
                "MANAGED_DEVICE_UUID",
                "PRE_PROVISIONED_SERIAL",
                "PRE_PROVISIONED_MAC",
                "DEFAULT",
                "MANAGED_DEVICE_HOSTNAME"
                ],
                "type": "string"
                },
                "versionedTemplateId": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "templateId": {
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

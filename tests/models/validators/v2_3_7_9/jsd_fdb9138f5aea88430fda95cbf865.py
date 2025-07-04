# -*- coding: utf-8 -*-
"""Cisco Catalyst Center RetrievesDeployedICAPConfigurationsWhileSupportingBasicFilteringV1 data
model.

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


class JSONSchemaValidatorFdb9138F5Aea88430Fda95Cbf865(object):
    """RetrievesDeployedICAPConfigurationsWhileSupportingBasicFilteringV1
    request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorFdb9138F5Aea88430Fda95Cbf865, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "activityId": {
                "type": "string"
                },
                "apId": {
                "type": "string"
                },
                "captureType": {
                "type": "string"
                },
                "clientMac": {
                "type": "string"
                },
                "createTime": {
                "type": "integer"
                },
                "deployedId": {
                "type": "string"
                },
                "disableActivityId": {
                "type": "string"
                },
                "durationInMins": {
                "type": "integer"
                },
                "endTime": {
                "type": "integer"
                },
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "otaBand": {
                "type": "string"
                },
                "otaChannel": {
                "type": "integer"
                },
                "otaChannelWidth": {
                "type": "integer"
                },
                "slots": {
                "items": {
                "type": "number"
                },
                "type": "array"
                },
                "status": {
                "type": "string"
                },
                "wlcId": {
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

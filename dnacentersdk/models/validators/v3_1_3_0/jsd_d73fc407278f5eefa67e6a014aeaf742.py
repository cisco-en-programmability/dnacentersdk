# -*- coding: utf-8 -*-
"""Cisco Catalyst Center UpdateRRMGeneralConfigurationFeatureTemplateV1 data model.

Copyright (c) 2025 Cisco Systems.

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


class JSONSchemaValidatorD73Fc407278F5EefA67E6A014Aeaf742(object):
    """UpdateRRMGeneralConfigurationFeatureTemplateV1 request schema
    definition."""
    def __init__(self):
        super(JSONSchemaValidatorD73Fc407278F5EefA67E6A014Aeaf742, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "designName": {
                "type": "string"
                },
                "featureAttributes": {
                "properties": {
                "coverageHoleDetection": {
                "type": "boolean"
                },
                "monitoringChannels": {
                "enum": [
                "MONITORING_CHANNELS_ALL",
                "MONITORING_CHANNELS_COUNTRY",
                "MONITORING_CHANNELS_DCA"
                ],
                "type": "string"
                },
                "neighborDiscoverType": {
                "enum": [
                "NEIGHBOR_DISCOVER_TYPE_TRANSPARENT",
                "NEIGHBOR_DISCOVER_TYPE_PROTECTED"
                ],
                "type": "string"
                },
                "radioBand": {
                "enum": [
                "2_4GHZ",
                "5GHZ",
                "6GHZ"
                ],
                "type": "string"
                },
                "throughputThreshold": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "unlockedAttributes": {
                "items": {
                "type": "string"
                },
                "type": "array"
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

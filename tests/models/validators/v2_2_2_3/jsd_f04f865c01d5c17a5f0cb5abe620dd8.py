# -*- coding: utf-8 -*-
"""Cisco DNA Center DeviceLicenseDetails data model.

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


class JSONSchemaValidatorF04F865C01D5C17A5F0Cb5Abe620Dd8(object):
    """DeviceLicenseDetails request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF04F865C01D5C17A5F0Cb5Abe620Dd8, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "access_points": {
                "items": {
                "items": {
                "properties": {
                "ap_type": {
                "type": "string"
                },
                "count": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "type": "array"
                },
                "chassis_details": {
                "properties": {
                "board_serial_number": {
                "type": "string"
                },
                "modules": {
                "items": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "module_name": {
                "type": "string"
                },
                "module_type": {
                "type": "string"
                },
                "serial_number": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "type": "array"
                },
                "port": {
                "type": "integer"
                },
                "supervisor_cards": {
                "items": {
                "items": {
                "properties": {
                "serial_number": {
                "type": "string"
                },
                "status": {
                "type": "string"
                },
                "supervisor_card_type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "device_name": {
                "type": "string"
                },
                "device_type": {
                "type": "string"
                },
                "device_uuid": {
                "type": "string"
                },
                "dna_level": {
                "type": "string"
                },
                "evaluation_license_expiry": {
                "type": "string"
                },
                "feature_license": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "has_sup_cards": {
                "type": "boolean"
                },
                "ip_address": {
                "type": "string"
                },
                "is_license_expired": {
                "type": "boolean"
                },
                "is_stacked_device": {
                "type": "boolean"
                },
                "license_mode": {
                "type": "string"
                },
                "mac_address": {
                "type": "string"
                },
                "model": {
                "type": "string"
                },
                "network_license": {
                "type": "string"
                },
                "site": {
                "type": "string"
                },
                "sntc_status": {
                "type": "string"
                },
                "software_version": {
                "type": "string"
                },
                "stacked_devices": {
                "items": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "mac_address": {
                "type": "string"
                },
                "role": {
                "type": "string"
                },
                "serial_number": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "type": "array"
                },
                "udi": {
                "type": "string"
                },
                "virtual_account_name": {
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

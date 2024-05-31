# -*- coding: utf-8 -*-
"""Cisco DNA Center DeviceLicenseSummary data model.

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


class JSONSchemaValidatorF4Ba64EeF4085D518A612835E128Fe3C(object):
    """DeviceLicenseSummary request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF4Ba64EeF4085D518A612835E128Fe3C, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "authorization_status": {
                "type": "string"
                },
                "customer_tag1": {
                "type": "string"
                },
                "customer_tag2": {
                "type": "string"
                },
                "customer_tag3": {
                "type": "string"
                },
                "customer_tag4": {
                "type": "string"
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
                "hsec_status": {
                "type": "string"
                },
                "ip_address": {
                "type": "string"
                },
                "is_license_expired": {
                "type": "boolean"
                },
                "is_performance_allowed": {
                "type": "boolean"
                },
                "is_wireless": {
                "type": "boolean"
                },
                "is_wireless_capable": {
                "type": "boolean"
                },
                "last_successful_rum_usage_upload_time": {
                "type": "string"
                },
                "last_updated_time": {
                "type": "string"
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
                "performance_license": {
                "type": "string"
                },
                "registration_status": {
                "type": "string"
                },
                "reservation_status": {
                "type": "string"
                },
                "site": {
                "type": "string"
                },
                "sle_auth_code": {
                "type": "string"
                },
                "sle_state": {
                "type": "string"
                },
                "smart_account_name": {
                "type": "string"
                },
                "software_version": {
                "type": "string"
                },
                "throughput_level": {
                "type": "string"
                },
                "total_access_point_count": {
                "type": "integer"
                },
                "virtual_account_name": {
                "type": "string"
                },
                "wireless_capable_dna_license": {
                "type": "string"
                },
                "wireless_capable_network_license": {
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
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )

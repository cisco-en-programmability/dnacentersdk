# -*- coding: utf-8 -*-
"""Cisco DNA Center GetEoXDetailsPerDevice data model.

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


class JSONSchemaValidatorEc048832853F8A63F34415D0E6Fce(object):
    """GetEoXDetailsPerDevice request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorEc048832853F8A63F34415D0E6Fce, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "alertCount": {
                "type": "integer"
                },
                "comments": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "deviceId": {
                "type": "string"
                },
                "eoxDetails": {
                "items": {
                "properties": {
                "bulletinHeadline": {
                "type": "string"
                },
                "bulletinName": {
                "type": "string"
                },
                "bulletinNumber": {
                "type": "string"
                },
                "bulletinPID": {
                "type": "string"
                },
                "bulletinURL": {
                "type": "string"
                },
                "endOfHardwareNewServiceAttachmentDate": {
                "type": "string"
                },
                "endOfHardwareServiceContractRenewalDate": {
                "type": "string"
                },
                "endOfLastHardwareShipDate": {
                "type": "string"
                },
                "endOfLifeDate": {
                "type": "string"
                },
                "endOfLifeExternalAnnouncementDate": {
                "type": "string"
                },
                "endOfSaleDate": {
                "type": "string"
                },
                "endOfSignatureReleasesDate": {
                "type": "string"
                },
                "endOfSoftwareMaintenanceReleasesDate": {
                "type": "string"
                },
                "endOfSoftwareVulnerabilityOrSecuritySupportDate": {
                "type": "string"
                },
                "endOfSoftwareVulnerabilityOrSecuritySupportDateHw": {
                "type": "string"
                },
                "eoXPhysicalType": {
                "type": "string"
                },
                "eoxAlertType": {
                "enum": [
                "HARDWARE",
                "SOFTWARE",
                "MODULE",
                "NONE"
                ],
                "type": "string"
                },
                "lastDateOfSupport": {
                "type": "string"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "lastScanTime": {
                "type": "integer"
                },
                "scanStatus": {
                "enum": [
                "NOT_SCANNED",
                "SUCCESS",
                "FAILED",
                "IN_PROGRESS",
                "UNKNOWN"
                ],
                "type": "string"
                }
                },
                "type": "object"
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

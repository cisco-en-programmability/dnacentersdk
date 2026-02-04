# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetSoftwareManagementExecutionDetails data model.

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

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorFc20A7Cd31655Bf1Ae775E4Bf645A9E1(object):
    """GetSoftwareManagementExecutionDetails request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorFc20A7Cd31655Bf1Ae775E4Bf645A9E1, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "completedPercentage": {
                "type": "number"
                },
                "createdBy": {
                "type": "string"
                },
                "duration": {
                "type": "integer"
                },
                "endDate": {
                "type": "string"
                },
                "errorCode": {
                "type": "string"
                },
                "errorMessage": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "isForceUpdate": {
                "type": "boolean"
                },
                "jobType": {
                "enum": [
                "DOWNLOAD_RELEASE",
                "UPGRADE_RELEASE",
                "UPDATE_DOWNLOADED_RELEASE",
                "DELETE_RELEASE",
                "INSTALL_OPTIONAL_PACKAGE",
                "UNINSTALL_OPTIONAL_PACKAGE"
                ],
                "type": "string"
                },
                "localReleaseId": {
                "type": "string"
                },
                "optionalPackages": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "releaseDisplayName": {
                "type": "string"
                },
                "releaseDisplayVersion": {
                "type": "string"
                },
                "releaseName": {
                "type": "string"
                },
                "releaseVersion": {
                "type": "string"
                },
                "startDate": {
                "type": "string"
                },
                "status": {
                "enum": [
                "INPROGRESS",
                "SUCCESS",
                "FAILED",
                "CANCELLED"
                ],
                "type": "string"
                },
                "systemErrorMessage": {
                "type": "string"
                },
                "tasks": {
                "items": {
                "properties": {
                "endDate": {
                "type": "string"
                },
                "errorCode": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "message": {
                "type": "string"
                },
                "startDate": {
                "type": "string"
                },
                "status": {
                "enum": [
                "INPROGRESS",
                "SUCCESS",
                "FAILED",
                "CANCELLED"
                ],
                "type": "string"
                },
                "systemErrorMessage": {
                "type": "string"
                },
                "taskName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "updateMessage": {
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

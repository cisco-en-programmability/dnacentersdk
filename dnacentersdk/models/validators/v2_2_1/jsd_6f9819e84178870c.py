# -*- coding: utf-8 -*-
"""DNA Center Update PnP Server Profile data model.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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


class JSONSchemaValidator6F9819E84178870C(object):
    """Update PnP Server Profile request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator6F9819E84178870C, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "autoSyncPeriod": {
                "type": [
                "number",
                "null"
                ]
                },
                "ccoUser": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "expiry": {
                "type": [
                "number",
                "null"
                ]
                },
                "lastSync": {
                "type": [
                "number",
                "null"
                ]
                },
                "profile": {
                "properties": {
                "addressFqdn": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "addressIpV4": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "cert": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "makeDefault": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "port": {
                "type": [
                "number",
                "null"
                ]
                },
                "profileId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "proxy": {
                "type": [
                "boolean",
                "null"
                ]
                }
                },
                "type": [
                "object"
                ]
                },
                "smartAccountId": {
                "description":
                 "",
                "type": [
                "string"
                ]
                },
                "syncResult": {
                "properties": {
                "syncList": {
                "items": {
                "properties": {
                "deviceSnList": {
                "items": {
                "type": [
                "string",
                "null",
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "syncType": {
                "description":
                 "",
                "enum": [
                "Add",
                "Update",
                "Delete",
                "MismatchError",
                null
                ],
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
                "type": [
                "array",
                "null"
                ]
                },
                "syncMsg": {
                "description":
                 "",
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
                "syncResultStr": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "syncStartTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "syncStatus": {
                "description":
                 "",
                "enum": [
                "NOT_SYNCED",
                "SYNCING",
                "SUCCESS",
                "FAILURE",
                null
                ],
                "type": [
                "string"
                ]
                },
                "tenantId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "token": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "virtualAccountId": {
                "description":
                 "",
                "type": [
                "string"
                ]
                }
                },
                "required": [
                "profile",
                "smartAccountId",
                "syncStatus",
                "virtualAccountId"
                ],
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

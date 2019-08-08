# -*- coding: utf-8 -*-
"""DNA Center Sync Virtual Account Devices data model.

Copyright (c) 2019 Cisco and/or its affiliates.

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


class JSONSchemaValidatorA4B6C87A4Ffb9Efa(object):
    """Sync Virtual Account Devices request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorA4B6C87A4Ffb9Efa, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "autoSyncPeriod": {
                "type": "number"
                },
                "ccoUser": {
                "description":
                 "",
                "type": "string"
                },
                "expiry": {
                "type": "number"
                },
                "lastSync": {
                "type": "number"
                },
                "profile": {
                "description":
                 "",
                "properties": {
                "addressFqdn": {
                "description":
                 "",
                "type": "string"
                },
                "addressIpV4": {
                "description":
                 "",
                "type": "string"
                },
                "cert": {
                "description":
                 "",
                "type": "string"
                },
                "makeDefault": {
                "type": "boolean"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "port": {
                "type": "number"
                },
                "profileId": {
                "description":
                 "",
                "type": "string"
                },
                "proxy": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "smartAccountId": {
                "description":
                 "",
                "type": "string"
                },
                "syncResult": {
                "description":
                 "",
                "properties": {
                "syncList": {
                "description":
                 "",
                "items": {
                "properties": {
                "deviceSnList": {
                "description":
                 "",
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "syncType": {
                "description":
                 "",
                "enum": [
                "Add",
                "Update",
                "Delete",
                "MismatchError"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "syncMsg": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "syncResultStr": {
                "description":
                 "",
                "type": "string"
                },
                "syncStartTime": {
                "type": "number"
                },
                "syncStatus": {
                "description":
                 "",
                "enum": [
                "NOT_SYNCED",
                "SYNCING",
                "SUCCESS",
                "FAILURE"
                ],
                "type": "string"
                },
                "tenantId": {
                "description":
                 "",
                "type": "string"
                },
                "token": {
                "description":
                 "",
                "type": "string"
                },
                "virtualAccountId": {
                "description":
                 "",
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

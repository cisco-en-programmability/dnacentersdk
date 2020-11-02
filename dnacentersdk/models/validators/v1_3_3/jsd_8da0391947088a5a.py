# -*- coding: utf-8 -*-
"""DNA Center Update PnP global settings data model.

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


class JSONSchemaValidator8Da0391947088A5A(object):
    """Update PnP global settings request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator8Da0391947088A5A, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "_id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "aaaCredentials": {
                "properties": {
                "password": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "username": {
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
                "acceptEula": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "defaultProfile": {
                "properties": {
                "cert": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "fqdnAddresses": {
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "ipAddresses": {
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "port": {
                "type": [
                "number",
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
                "object",
                "null"
                ]
                },
                "savaMappingList": {
                "items": {
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
                "object",
                "null"
                ]
                },
                "smartAccountId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
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
                "string",
                "null"
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
                "taskTimeOuts": {
                "properties": {
                "configTimeOut": {
                "type": [
                "number",
                "null"
                ]
                },
                "generalTimeOut": {
                "type": [
                "number",
                "null"
                ]
                },
                "imageDownloadTimeOut": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
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
                "version": {
                "type": [
                "number",
                "null"
                ]
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

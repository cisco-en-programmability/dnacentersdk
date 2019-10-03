# -*- coding: utf-8 -*-
"""DNA Center Get PnP global settings data model.

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


class JSONSchemaValidator7E92F9Eb46Db8320(object):
    """Get PnP global settings request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator7E92F9Eb46Db8320, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "_id": {
                "description":
                " Id",
                "type": [
                "string",
                "null"
                ]
                },
                "aaaCredentials": {
                "description":
                "Aaa Credentials",
                "properties": {
                "password": {
                "description":
                "Password",
                "type": [
                "string",
                "null"
                ]
                },
                "username": {
                "description":
                "Username",
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
                "description":
                "Default Profile",
                "properties": {
                "cert": {
                "description":
                "Cert",
                "type": [
                "string",
                "null"
                ]
                },
                "fqdnAddresses": {
                "description":
                "Fqdn Addresses",
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
                "description":
                "Ip Addresses",
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
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "savaMappingList": {
                "description":
                "Sava Mapping List",
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
                "Cco User",
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
                "description":
                "Profile",
                "properties": {
                "addressFqdn": {
                "description":
                "Address Fqdn",
                "type": [
                "string",
                "null"
                ]
                },
                "addressIpV4": {
                "description":
                "Address Ip V4",
                "type": [
                "string",
                "null"
                ]
                },
                "cert": {
                "description":
                "Cert",
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
                "Name",
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
                "Profile Id",
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
                "Smart Account Id",
                "type": [
                "string",
                "null"
                ]
                },
                "syncResult": {
                "description":
                "Sync Result",
                "properties": {
                "syncList": {
                "description":
                "Sync List",
                "items": {
                "properties": {
                "deviceSnList": {
                "description":
                "Device Sn List",
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
                "Sync Type",
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
                "Sync Msg",
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
                "Sync Result Str",
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
                "Sync Status",
                "type": [
                "string",
                "null"
                ]
                },
                "tenantId": {
                "description":
                "Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "token": {
                "description":
                "Token",
                "type": [
                "string",
                "null"
                ]
                },
                "virtualAccountId": {
                "description":
                "Virtual Account Id",
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
                "description":
                "Task Time Outs",
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
                "Tenant Id",
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

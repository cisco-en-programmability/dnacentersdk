# -*- coding: utf-8 -*-
"""Cisco DNA Center GetPnPGlobalSettings data model.

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


class JSONSchemaValidatorB37Eb826A4Ad5283Ae85Dc4628045B40(object):
    """GetPnPGlobalSettings request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorB37Eb826A4Ad5283Ae85Dc4628045B40, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "_id": {
                "type": "string"
                },
                "aaaCredentials": {
                "properties": {
                "password": {
                "type": "string"
                },
                "username": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "acceptEula": {
                "type": "boolean"
                },
                "defaultProfile": {
                "properties": {
                "cert": {
                "type": "string"
                },
                "fqdnAddresses": {
                "items": {
                "type": "string"
                }
                },
                "ipAddresses": {
                "items": {
                "type": "string"
                }
                },
                "port": {
                "type": "number"
                },
                "proxy": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "savaMappingList": {
                "items": {
                "properties": {
                "autoSyncPeriod": {
                "type": "number"
                },
                "ccoUser": {
                "type": "string"
                },
                "expiry": {
                "type": "number"
                },
                "lastSync": {
                "type": "number"
                },
                "profile": {
                "properties": {
                "addressFqdn": {
                "type": "string"
                },
                "addressIpV4": {
                "type": "string"
                },
                "cert": {
                "type": "string"
                },
                "makeDefault": {
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "port": {
                "type": "number"
                },
                "profileId": {
                "type": "string"
                },
                "proxy": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "smartAccountId": {
                "type": "string"
                },
                "syncResult": {
                "properties": {
                "syncList": {
                "items": {
                "properties": {
                "deviceSnList": {
                "items": {
                "type": "string"
                }
                },
                "syncType": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "syncMsg": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "syncResultStr": {
                "type": "string"
                },
                "syncStartTime": {
                "type": "number"
                },
                "syncStatus": {
                "type": "string"
                },
                "tenantId": {
                "type": "string"
                },
                "token": {
                "type": "string"
                },
                "virtualAccountId": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "taskTimeOuts": {
                "properties": {
                "configTimeOut": {
                "type": "number"
                },
                "generalTimeOut": {
                "type": "number"
                },
                "imageDownloadTimeOut": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "tenantId": {
                "type": "string"
                },
                "version": {
                "type": "number"
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

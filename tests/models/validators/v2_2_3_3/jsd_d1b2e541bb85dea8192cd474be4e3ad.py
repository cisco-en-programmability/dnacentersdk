# -*- coding: utf-8 -*-
"""Cisco DNA Center GetApplicationPolicyDefault data model.

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


class JSONSchemaValidatorD1B2E541Bb85Dea8192Cd474Be4E3Ad(object):
    """GetApplicationPolicyDefault request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD1B2E541Bb85Dea8192Cd474Be4E3Ad, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "cfsChangeInfo": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "contractList": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "createTime": {
                "type": "integer"
                },
                "customProvisions": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "deletePolicyStatus": {
                "enum": [
                "NONE",
                "DELETED",
                "RESTORED"
                ],
                "type": "string"
                },
                "deployed": {
                "type": "boolean"
                },
                "displayName": {
                "type": "string"
                },
                "exclusiveContract": {
                "properties": {
                "clause": {
                "items": {
                "properties": {
                "displayName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instanceCreatedOn": {
                "type": "integer"
                },
                "instanceId": {
                "type": "integer"
                },
                "instanceUpdatedOn": {
                "type": "integer"
                },
                "instanceVersion": {
                "type": "number"
                },
                "priority": {
                "type": "integer"
                },
                "relevanceLevel": {
                "enum": [
                "BUSINESS_RELEVANT",
                "BUSINESS_IRRELEVANT",
                "DEFAULT"
                ],
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "displayName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instanceCreatedOn": {
                "type": "integer"
                },
                "instanceId": {
                "type": "integer"
                },
                "instanceUpdatedOn": {
                "type": "integer"
                },
                "instanceVersion": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "identitySource": {
                "properties": {
                "displayName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instanceCreatedOn": {
                "type": "integer"
                },
                "instanceId": {
                "type": "integer"
                },
                "instanceUpdatedOn": {
                "type": "integer"
                },
                "instanceVersion": {
                "type": "number"
                },
                "state": {
                "enum": [
                "INACTIVE",
                "ACTIVE",
                "DELETED"
                ],
                "type": "string"
                },
                "type": {
                "enum": [
                "APIC_EM",
                "NBAR"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "instanceCreatedOn": {
                "type": "integer"
                },
                "instanceId": {
                "type": "integer"
                },
                "instanceUpdatedOn": {
                "type": "integer"
                },
                "instanceVersion": {
                "type": "number"
                },
                "internal": {
                "type": "boolean"
                },
                "isDeleted": {
                "type": "boolean"
                },
                "isEnabled": {
                "type": "boolean"
                },
                "isScopeStale": {
                "type": "boolean"
                },
                "isSeeded": {
                "type": "boolean"
                },
                "isStale": {
                "type": "boolean"
                },
                "iseReserved": {
                "type": "boolean"
                },
                "lastUpdateTime": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "namespace": {
                "type": "string"
                },
                "policyStatus": {
                "enum": [
                "ENABLED",
                "DISABLED",
                "MONITOR"
                ],
                "type": "string"
                },
                "priority": {
                "type": "integer"
                },
                "producer": {
                "properties": {
                "displayName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instanceCreatedOn": {
                "type": "integer"
                },
                "instanceId": {
                "type": "integer"
                },
                "instanceUpdatedOn": {
                "type": "integer"
                },
                "instanceVersion": {
                "type": "number"
                },
                "scalableGroup": {
                "items": {
                "properties": {
                "idRef": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "provisioningState": {
                "enum": [
                "UNKNOWN",
                "DEFINED",
                "DEPLOYED",
                "FAILED",
                "VERIFIED",
                "DEPLOYING",
                "SUBMITTED",
                "PREPROCESSED",
                "VALIDATED"
                ],
                "type": "string"
                },
                "pushed": {
                "type": "boolean"
                },
                "qualifier": {
                "type": "string"
                },
                "resourceVersion": {
                "type": "number"
                },
                "targetIdList": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "type": {
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

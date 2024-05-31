# -*- coding: utf-8 -*-
"""Cisco DNA Center ApplicationPolicyIntent data model.

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


class JSONSchemaValidatorFa27CcBaf55711849381A707E1Edfa(object):
    """ApplicationPolicyIntent request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorFa27CcBaf55711849381A707E1Edfa, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "createList": {
                "items": {
                "properties": {
                "advancedPolicyScope": {
                "properties": {
                "advancedPolicyScopeElement": {
                "items": {
                "properties": {
                "groupId": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "ssid": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "consumer": {
                "properties": {
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
                "contract": {
                "properties": {
                "idRef": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "deletePolicyStatus": {
                "enum": [
                "NONE",
                "DELETED",
                "RESTORED"
                ],
                "type": "string"
                },
                "exclusiveContract": {
                "properties": {
                "clause": {
                "items": {
                "properties": {
                "deviceRemovalBehavior": {
                "enum": [
                "DELETE",
                "RESTORE",
                "IGNORE"
                ],
                "type": "string"
                },
                "hostTrackingEnabled": {
                "type": "boolean"
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
                "enum": [
                "BUSINESS_RELEVANCE",
                "APPLICATION_POLICY_KNOBS"
                ],
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
                "name": {
                "type": "string"
                },
                "policyScope": {
                "type": "string"
                },
                "priority": {
                "type": "string"
                },
                "producer": {
                "properties": {
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
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "deleteList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "updateList": {
                "items": {
                "properties": {
                "advancedPolicyScope": {
                "properties": {
                "advancedPolicyScopeElement": {
                "items": {
                "properties": {
                "groupId": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "id": {
                "type": "string"
                },
                "ssid": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "consumer": {
                "properties": {
                "id": {
                "type": "string"
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
                "contract": {
                "properties": {
                "idRef": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "deletePolicyStatus": {
                "enum": [
                "NONE",
                "DELETED",
                "RESTORED"
                ],
                "type": "string"
                },
                "exclusiveContract": {
                "properties": {
                "clause": {
                "items": {
                "properties": {
                "deviceRemovalBehavior": {
                "enum": [
                "DELETE",
                "RESTORE",
                "IGNORE"
                ],
                "type": "string"
                },
                "hostTrackingEnabled": {
                "type": "boolean"
                },
                "id": {
                "type": "string"
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
                "enum": [
                "BUSINESS_RELEVANCE",
                "APPLICATION_POLICY_KNOBS"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "id": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "policyScope": {
                "type": "string"
                },
                "priority": {
                "type": "string"
                },
                "producer": {
                "properties": {
                "id": {
                "type": "string"
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
                }
                },
                "type": "object"
                },
                "type": "array"
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

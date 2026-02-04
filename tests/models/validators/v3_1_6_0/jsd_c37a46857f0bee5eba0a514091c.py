# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetQosDeviceInterfaceInfo data model.

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


class JSONSchemaValidatorC37A46857F0Bee5Eba0A514091C(object):
    """GetQosDeviceInterfaceInfo request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC37A46857F0Bee5Eba0A514091C, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "cfsChangeInfo": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "createTime": {
                "type": "integer"
                },
                "customProvisions": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "deployed": {
                "type": "boolean"
                },
                "displayName": {
                "type": "string"
                },
                "excludedInterfaces": {
                "items": {
                "type": "string"
                },
                "type": "array"
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
                "type": "integer"
                },
                "isExcluded": {
                "type": "boolean"
                },
                "isSeeded": {
                "type": "boolean"
                },
                "isStale": {
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
                "networkDeviceId": {
                "type": "string"
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
                "qosDeviceInterfaceInfo": {
                "items": {
                "properties": {
                "displayName": {
                "type": "string"
                },
                "dmvpnRemoteSitesBw": {
                "items": {
                "type": "integer"
                },
                "type": "array"
                },
                "downloadBW": {
                "type": "number"
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
                "interfaceId": {
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "label": {
                "type": "string"
                },
                "role": {
                "enum": [
                "WAN",
                "DMVPN_HUB",
                "DMVPN_SPOKE"
                ],
                "type": "string"
                },
                "uploadBW": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "qualifier": {
                "type": "string"
                },
                "resourceVersion": {
                "type": "integer"
                },
                "targetIdList": {
                "items": {
                "type": "string"
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

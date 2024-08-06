# -*- coding: utf-8 -*-
"""Cisco DNA Center GetStackDetailsForDevice data model.

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

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorC07Eaefa1Fa45Faa801764D9094336Ae(object):
    """GetStackDetailsForDevice request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC07Eaefa1Fa45Faa801764D9094336Ae, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "deviceId": {
                "type": "string"
                },
                "stackPortInfo": {
                "items": {
                "properties": {
                "isSynchOk": {
                "type": "string"
                },
                "linkActive": {
                "type": "boolean"
                },
                "linkOk": {
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "neighborPort": {
                "type": "string"
                },
                "nrLinkOkChanges": {
                "type": "integer"
                },
                "stackCableLengthInfo": {
                "enum": [
                "NO_CABLE",
                "_50_CM",
                "_1_M",
                "_3_M",
                "UNKNOWN"
                ],
                "type": "string"
                },
                "stackPortOperStatusInfo": {
                "enum": [
                "OK",
                "UP",
                "DOWN",
                "FORCEDDOWN",
                "ABSENT",
                "UNKNOWN"
                ],
                "type": "string"
                },
                "switchPort": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "stackSwitchInfo": {
                "items": {
                "properties": {
                "entPhysicalIndex": {
                "type": "string"
                },
                "hwPriority": {
                "type": "integer"
                },
                "macAddress": {
                "type": "string"
                },
                "numNextReload": {
                "type": "integer"
                },
                "platformId": {
                "type": "string"
                },
                "role": {
                "enum": [
                "MASTER",
                "MEMBER",
                "NOTMEMBER",
                "STANDBY",
                "UNKNOWN"
                ],
                "type": "string"
                },
                "serialNumber": {
                "type": "string"
                },
                "softwareImage": {
                "type": "string"
                },
                "stackMemberNumber": {
                "type": "integer"
                },
                "state": {
                "enum": [
                "WAITING",
                "PROGRESSING",
                "ADDED",
                "READY",
                "SDMMISMATCH",
                "VERMISMATCH",
                "FEATUREMISMATCH",
                "NEWMASTERINIT",
                "PROVISIONED",
                "INVALID",
                "UNKNOWN"
                ],
                "type": "string"
                },
                "switchPriority": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "svlSwitchInfo": {
                "items": {
                "properties": {
                "dadProtocol": {
                "enum": [
                "NONE",
                "PAGP",
                "UNKNOWN"
                ],
                "type": "string"
                },
                "dadRecoveryReloadEnabled": {
                "type": "boolean"
                },
                "domainNumber": {
                "type": "integer"
                },
                "inDadRecoveryMode": {
                "type": "boolean"
                },
                "swVirtualStatus": {
                "type": "string"
                },
                "switchMembers": {
                "items": {
                "properties": {
                "bandwidth": {
                "type": "string"
                },
                "svlMemberEndPoints": {
                "items": {
                "properties": {
                "svlMemberEndPointPorts": {
                "items": {
                "properties": {
                "svlProtocolStatus": {
                "enum": [
                "SUSPENDED",
                "PENDING",
                "ERROR",
                "TIMEOUT",
                "READY",
                "UNKNOWN"
                ],
                "type": "string"
                },
                "swLocalInterface": {
                "type": "string"
                },
                "swRemoteInterface": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "svlNumber": {
                "type": "integer"
                },
                "svlStatus": {
                "enum": [
                "UP",
                "DOWN",
                "UNKNOWN"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "svlMemberNumber": {
                "type": "integer"
                },
                "svlMemberPepSettings": {
                "items": {
                "properties": {
                "dadEnabled": {
                "type": "boolean"
                },
                "dadInterfaceName": {
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
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
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

# -*- coding: utf-8 -*-
"""Cisco Catalyst Center DisasterRecoveryStatusV1 data model.

Copyright (c) 2024 Cisco Systems.

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


class JSONSchemaValidatorB27CcD369519D8820De238483B865(object):
    """DisasterRecoveryStatusV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorB27CcD369519D8820De238483B865, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "ipconfig": {
                "items": {
                "properties": {
                "interface": {
                "enum": [
                "enterprise",
                "management"
                ],
                "type": "string"
                },
                "ip": {
                "type": "string"
                },
                "vip": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "ipsec-tunnel": {
                "items": {
                "properties": {
                "side_a": {
                "type": "string"
                },
                "side_b": {
                "type": "string"
                },
                "status": {
                "enum": [
                "up",
                "down"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "main": {
                "properties": {
                "ipconfig": {
                "items": {
                "properties": {
                "interface": {
                "enum": [
                "enterprise",
                "management"
                ],
                "type": "string"
                },
                "ip": {
                "type": "string"
                },
                "vip": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "nodes": {
                "items": {
                "properties": {
                "hostname": {
                "type": "string"
                },
                "ipaddresses": {
                "items": {
                "properties": {
                "interface": {
                "enum": [
                "enterprise",
                "management"
                ],
                "type": "string"
                },
                "ip": {
                "type": "string"
                },
                "vip": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "state": {
                "enum": [
                "up",
                "down",
                "unknown"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "state": {
                "enum": [
                "Unregistered",
                "Registering",
                "Registered",
                "RegisterFailed",
                "Configuring",
                "Active",
                "ConfigureFailed",
                "FailingOver",
                "StandbyReady",
                "FailoverFailed",
                "Standby",
                "Isolating",
                "Isolated",
                "IsolateFailed",
                "Pausing",
                "Paused",
                "PauseFailed",
                "ActiveStandAlone",
                "StandbyStandAlone",
                "Partitioned",
                "Deregistering",
                "DeregisterFailed",
                "Up",
                "Down"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "recovery": {
                "properties": {
                "ipconfig": {
                "items": {
                "properties": {
                "interface": {
                "enum": [
                "enterprise",
                "management"
                ],
                "type": "string"
                },
                "ip": {
                "type": "string"
                },
                "vip": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "nodes": {
                "items": {
                "properties": {
                "hostname": {
                "type": "string"
                },
                "ipconfig": {
                "items": {
                "properties": {
                "interface": {
                "enum": [
                "enterprise",
                "management"
                ],
                "type": "string"
                },
                "ip": {
                "type": "string"
                },
                "vip": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "state": {
                "enum": [
                "up",
                "down",
                "unknown"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "state": {
                "enum": [
                "Unregistered",
                "Registering",
                "Registered",
                "RegisterFailed",
                "Configuring",
                "Active",
                "ConfigureFailed",
                "FailingOver",
                "StandbyReady",
                "FailoverFailed",
                "Standby",
                "Isolating",
                "Isolated",
                "IsolateFailed",
                "Pausing",
                "Paused",
                "PauseFailed",
                "ActiveStandAlone",
                "StandbyStandAlone",
                "Partitioned",
                "Deregistering",
                "DeregisterFailed",
                "Up",
                "Down"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "site": {
                "enum": [
                "main",
                "recovery"
                ],
                "type": "string"
                },
                "state": {
                "enum": [
                "Unconfigured",
                "Registering",
                "Registered",
                "Deregistering",
                "Deregistered",
                "Configuring",
                "ConfigureFailed",
                "Up",
                "FailingOver",
                "FailoverFailed",
                "Pausing",
                "Paused",
                "PauseFailed",
                "Down"
                ],
                "type": "string"
                },
                "witness": {
                "properties": {
                "ipconfig": {
                "items": {
                "properties": {
                "interface": {
                "type": "string"
                },
                "ip": {
                "type": "string"
                },
                "vip": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "nodes": {
                "items": {
                "properties": {
                "hostname": {
                "type": "string"
                },
                "ipconfig": {
                "items": {
                "properties": {
                "interface": {
                "type": "string"
                },
                "ip": {
                "type": "string"
                },
                "vip": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "state": {
                "enum": [
                "up",
                "down",
                "unknown"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "state": {
                "enum": [
                "Unregistered",
                "Registering",
                "Registered",
                "RegisterFailed",
                "Up",
                "Down",
                "Pausing",
                "PauseFailed",
                "Paused",
                "Deregistering",
                "DeregisterFailed"
                ],
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                }""".replace(
                    "\n" + " " * 16, ""
                )
            )
        )

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                "{} is invalid. Reason: {}".format(request, e.message)
            )

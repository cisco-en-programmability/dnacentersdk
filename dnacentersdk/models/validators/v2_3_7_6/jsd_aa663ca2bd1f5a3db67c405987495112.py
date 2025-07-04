# -*- coding: utf-8 -*-
"""Cisco DNA Center CreateSSIDV1 data model.

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


class JSONSchemaValidatorAa663Ca2Bd1F5A3DB67C405987495112(object):
    """CreateSSIDV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorAa663Ca2Bd1F5A3DB67C405987495112, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "aaaOverride": {
                "type": "boolean"
                },
                "acctServers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "aclName": {
                "type": "string"
                },
                "authServer": {
                "enum": [
                "auth_ise",
                "auth_external",
                "auth_internal"
                ],
                "type": "string"
                },
                "authServers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "authType": {
                "enum": [
                "WPA2_ENTERPRISE",
                "WPA2_PERSONAL",
                "OPEN",
                "WPA3_ENTERPRISE",
                "WPA3_PERSONAL",
                "WPA2_WPA3_PERSONAL",
                "WPA2_WPA3_ENTERPRISE",
                "OPEN-SECURED"
                ],
                "type": "string"
                },
                "basicServiceSetClientIdleTimeout": {
                "type": "integer"
                },
                "basicServiceSetMaxIdleEnable": {
                "type": "boolean"
                },
                "cckmTsfTolerance": {
                "type": "integer"
                },
                "clientExclusionEnable": {
                "type": "boolean"
                },
                "clientExclusionTimeout": {
                "type": "integer"
                },
                "clientRateLimit": {
                "type": "integer"
                },
                "coverageHoleDetectionEnable": {
                "type": "boolean"
                },
                "directedMulticastServiceEnable": {
                "type": "boolean"
                },
                "egressQos": {
                "enum": [
                "PLATINUM",
                "SILVER",
                "GOLD",
                "BRONZE"
                ],
                "type": "string"
                },
                "externalAuthIpAddress": {
                "type": "string"
                },
                "fastTransition": {
                "enum": [
                "ADAPTIVE",
                "ENABLE",
                "DISABLE"
                ],
                "type": "string"
                },
                "fastTransitionOverTheDistributedSystemEnable": {
                "type": "boolean"
                },
                "ghz24Policy": {
                "enum": [
                "dot11-bg-only",
                "dot11-g-only"
                ],
                "type": "string"
                },
                "ghz6PolicyClientSteering": {
                "type": "boolean"
                },
                "ingressQos": {
                "enum": [
                "PLATINUM-UP",
                "SILVER-UP",
                "GOLD-UP",
                "BRONZE-UP"
                ],
                "type": "string"
                },
                "isApBeaconProtectionEnabled": {
                "type": "boolean"
                },
                "isAuthKey8021x": {
                "type": "boolean"
                },
                "isAuthKey8021xPlusFT": {
                "type": "boolean"
                },
                "isAuthKey8021x_SHA256": {
                "type": "boolean"
                },
                "isAuthKeyEasyPSK": {
                "type": "boolean"
                },
                "isAuthKeyOWE": {
                "type": "boolean"
                },
                "isAuthKeyPSK": {
                "type": "boolean"
                },
                "isAuthKeyPSKPlusFT": {
                "type": "boolean"
                },
                "isAuthKeyPSKSHA256": {
                "type": "boolean"
                },
                "isAuthKeySae": {
                "type": "boolean"
                },
                "isAuthKeySaeExt": {
                "type": "boolean"
                },
                "isAuthKeySaeExtPlusFT": {
                "type": "boolean"
                },
                "isAuthKeySaePlusFT": {
                "type": "boolean"
                },
                "isAuthKeySuiteB1921x": {
                "type": "boolean"
                },
                "isAuthKeySuiteB1x": {
                "type": "boolean"
                },
                "isBroadcastSSID": {
                "type": "boolean"
                },
                "isCckmEnabled": {
                "type": "boolean"
                },
                "isEnabled": {
                "type": "boolean"
                },
                "isFastLaneEnabled": {
                "type": "boolean"
                },
                "isHex": {
                "type": "boolean"
                },
                "isMacFilteringEnabled": {
                "type": "boolean"
                },
                "isPosturingEnabled": {
                "type": "boolean"
                },
                "isRandomMacFilterEnabled": {
                "type": "boolean"
                },
                "l3AuthType": {
                "enum": [
                "open",
                "web_auth"
                ],
                "type": "string"
                },
                "managementFrameProtectionClientprotection": {
                "enum": [
                "OPTIONAL",
                "DISABLED",
                "REQUIRED"
                ],
                "type": "string"
                },
                "multiPSKSettings": {
                "items": {
                "properties": {
                "passphrase": {
                "type": "string"
                },
                "passphraseType": {
                "enum": [
                "ASCII",
                "HEX"
                ],
                "type": "string"
                },
                "priority": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "nasOptions": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "neighborListEnable": {
                "type": "boolean"
                },
                "openSsid": {
                "type": "string"
                },
                "passphrase": {
                "type": "string"
                },
                "profileName": {
                "type": "string"
                },
                "protectedManagementFrame": {
                "enum": [
                "OPTIONAL",
                "DISABLED",
                "REQUIRED"
                ],
                "type": "string"
                },
                "rsnCipherSuiteCcmp128": {
                "type": "boolean"
                },
                "rsnCipherSuiteCcmp256": {
                "type": "boolean"
                },
                "rsnCipherSuiteGcmp128": {
                "type": "boolean"
                },
                "rsnCipherSuiteGcmp256": {
                "type": "boolean"
                },
                "sessionTimeOut": {
                "type": "integer"
                },
                "sessionTimeOutEnable": {
                "type": "boolean"
                },
                "sleepingClientEnable": {
                "type": "boolean"
                },
                "sleepingClientTimeout": {
                "type": "integer"
                },
                "ssid": {
                "type": "string"
                },
                "ssidRadioType": {
                "enum": [
                "Triple band operation(2.4GHz, 5GHz and 6GHz)",
                "5GHz only",
                "2.4GHz only",
                "6GHz only",
                "2.4 and 5 GHz",
                "2.4 and 6 GHz",
                "5 and 6 GHz"
                ],
                "type": "string"
                },
                "webPassthrough": {
                "type": "boolean"
                },
                "wlanBandSelectEnable": {
                "type": "boolean"
                },
                "wlanType": {
                "enum": [
                "Enterprise",
                "Guest"
                ],
                "type": "string"
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

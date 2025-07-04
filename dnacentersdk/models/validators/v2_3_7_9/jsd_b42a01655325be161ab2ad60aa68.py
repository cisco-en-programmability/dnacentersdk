# -*- coding: utf-8 -*-
"""Cisco DNA Center UpdateAPProfileByID data model.

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


class JSONSchemaValidatorB42A01655325Be161Ab2Ad60Aa68(object):
    """UpdateAPProfileByID request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorB42A01655325Be161Ab2Ad60Aa68, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "apPowerProfileName": {
                "type": "string"
                },
                "apProfileName": {
                "type": "string"
                },
                "awipsEnabled": {
                "type": "boolean"
                },
                "awipsForensicEnabled": {
                "type": "boolean"
                },
                "calendarPowerProfiles": {
                "properties": {
                "duration": {
                "properties": {
                "schedulerDate": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "schedulerDay": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "schedulerEndTime": {
                "type": "string"
                },
                "schedulerStartTime": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "powerProfileName": {
                "type": "string"
                },
                "schedulerType": {
                "enum": [
                "DAILY",
                "WEEKLY",
                "MONTHLY"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "clientLimit": {
                "type": "integer"
                },
                "countryCode": {
                "enum": [
                "(AF|AE|AL|AR|AT|AO|AU|BD|BA|BB|BE|BG|BH|BM|BN|BO|BR|BT|BY|CA|CD|CH|CI|CL|CM|CN|CO|CR|CU|CY|CZ|DE|DK|DO|DZ|EC|EE|EG|EL|ES|ET|FI|FJ|FR|GB|GH|GI|GE|GR|GT|HK|HN|HR|HU|ID|IE|IL|IN|IQ|IS|IT|J2|J4|JM|JO|KE|KH|KN|KW|KZ|LA|LB|LI|LK|LT|LU|LV|LY|MA|MC|MD|ME|MK|MN|MM|MO|MT|MX|MY|NG|NI|NL|NO|NP|NZ|OM|PA|PE|PH|PK|PL|PR|PT|PY|QA|RO|RS|RU|SA|SD|SE|SG|SI|SK|SM|TH|TI|TN|TR|TW|TZ|UA|US|UY|VA|VE|VN|XK|YE|ZA|ZW|MU|ZM|BI|NA|BW|GA|UG|UZ)"
                ],
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "managementSetting": {
                "properties": {
                "authType": {
                "enum": [
                "NO-AUTH",
                "EAP-TLS",
                "EAP-PEAP",
                "EAP-FAST"
                ],
                "type": "string"
                },
                "cdpState": {
                "type": "boolean"
                },
                "dot1xPassword": {
                "type": "string"
                },
                "dot1xUsername": {
                "type": "string"
                },
                "managementEnablePassword": {
                "type": "string"
                },
                "managementPassword": {
                "type": "string"
                },
                "managementUserName": {
                "type": "string"
                },
                "sshEnabled": {
                "type": "boolean"
                },
                "telnetEnabled": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "meshEnabled": {
                "type": "boolean"
                },
                "meshSetting": {
                "properties": {
                "backhaulClientAccess": {
                "type": "boolean"
                },
                "bridgeGroupName": {
                "type": "string"
                },
                "ghz24BackhaulDataRates": {
                "enum": [
                "auto",
                "802.11abg",
                "802.11ax",
                "802.11n"
                ],
                "type": "string"
                },
                "ghz5BackhaulDataRates": {
                "enum": [
                "auto",
                "802.11abg",
                "802.12ac",
                "802.11ax",
                "802.11n"
                ],
                "type": "string"
                },
                "range": {
                "type": "integer"
                },
                "rapDownlinkBackhaul": {
                "enum": [
                "5 GHz",
                "2.4 GHz"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "pmfDenialEnabled": {
                "type": "boolean"
                },
                "remoteWorkerEnabled": {
                "type": "boolean"
                },
                "rogueDetectionSetting": {
                "properties": {
                "rogueDetection": {
                "type": "boolean"
                },
                "rogueDetectionMinRssi": {
                "type": "integer"
                },
                "rogueDetectionReportInterval": {
                "type": "integer"
                },
                "rogueDetectionTransientInterval": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "timeZone": {
                "enum": [
                "Not Configured",
                "Controller",
                "Delta from Controller"
                ],
                "type": "string"
                },
                "timeZoneOffsetHour": {
                "type": "integer"
                },
                "timeZoneOffsetMinutes": {
                "type": "integer"
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

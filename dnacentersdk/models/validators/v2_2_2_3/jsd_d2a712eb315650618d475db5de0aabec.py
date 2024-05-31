# -*- coding: utf-8 -*-
"""Cisco DNA Center CreateNFVProfile data model.

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


class JSONSchemaValidatorD2A712Eb315650618D475Db5De0Aabec(object):
    """CreateNFVProfile request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD2A712Eb315650618D475Db5De0Aabec, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "device": {
                "items": {
                "properties": {
                "customNetworks": {
                "items": {
                "properties": {
                "connectionType": {
                "enum": [
                "wan-net",
                "wan2-net",
                "lan-net",
                "mgmt-net",
                "service-net",
                "GEO-2-1",
                "GEO-2-2",
                "GEO-3-1",
                "GEO-3-2",
                "SRIOV-1",
                "SRIOV-2",
                "SRIOV-3",
                "SRIOV-4",
                "SRIOV-5",
                "SRIOV-6"
                ],
                "type": "string"
                },
                "networkName": {
                "type": "string"
                },
                "servicesToConnect": {
                "items": {
                "properties": {
                "serviceName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "vlanId": {
                "type": "number"
                },
                "vlanMode": {
                "enum": [
                "trunk",
                "Access"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "customTemplate": {
                "items": {
                "properties": {
                "deviceType": {
                "enum": [
                "Cisco 5400 Enterprise Network Compute System",
                "Cisco Integrated Services Virtual Router",
                "Cisco Adaptive Security Virtual Appliance (ASAv)",
                "NFVIS",
                "ASAV"
                ],
                "type": "string"
                },
                "template": {
                "type": "string"
                },
                "templateType": {
                "enum": [
                "Onboarding Template(s)",
                "Day-N-Template(s)"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "deviceTag": {
                "type": "string"
                },
                "deviceType": {
                "enum": [
                "Cisco 5400 Enterprise Network Compute System",
                "Cisco 5100 Enterprise Network Compute System"
                ],
                "type": "string"
                },
                "directInternetAccessForFirewall": {
                "type": "boolean"
                },
                "serviceProviderProfile": {
                "items": {
                "properties": {
                "connect": {
                "type": "boolean"
                },
                "connectDefaultGatewayOnWan": {
                "type": "boolean"
                },
                "linkType": {
                "enum": [
                "GigabitEthernet",
                "Cellular"
                ],
                "type": "string"
                },
                "serviceProvider": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "services": {
                "items": {
                "properties": {
                "firewallMode": {
                "enum": [
                "routed",
                "transparent"
                ],
                "type": "string"
                },
                "imageName": {
                "type": "string"
                },
                "profileType": {
                "enum": [
                "ASAv5",
                "ASAv30",
                "ASAv30",
                "ISRv-mini",
                "ISRv-medium",
                "ISRv-small",
                "riverbed-small",
                "sp-small",
                "rehel7-medium",
                "vEdge-samll",
                "vwaas-200-original",
                "vwaas-150-original",
                "vWASS-6000R-Resized",
                "vWASS-1300-Original",
                "vWASS-50000-Original",
                "vCM-100",
                "vWASS-6000R-Original",
                "vWASS-750-Original",
                "vWASS-1300-Resized",
                "vWASS-2500-Original",
                "vCM-500",
                "vCM-2000",
                "vWASS-6000-Resized",
                "vWASS-6000-Original",
                "vCM-1000",
                "vWASS-750-Resized",
                "vWASS-200-Resized",
                "vWASS-12000-Original",
                "vWASS-150-Resized",
                "vWASS-12000-Resized",
                "vWASS-2500-Resized",
                "vWASS-50000-Resized"
                ],
                "type": "string"
                },
                "serviceName": {
                "type": "string"
                },
                "serviceType": {
                "enum": [
                "isr",
                "vedge",
                "waas",
                "asa",
                "ngfw",
                "paloalto",
                "fortinet",
                "checkpoint",
                "riverbed",
                "silverpeak",
                "linux"
                ],
                "type": "string"
                },
                "vNicMapping": {
                "items": {
                "properties": {
                "assignIpAddressToNetwork": {
                "type": "string"
                },
                "networkType": {
                "enum": [
                "wan-net",
                "wan2-net",
                "lan-net",
                "mgmt-net",
                "service-net",
                "GEO-0",
                "GEO-1",
                "GEO-2-1",
                "GEO-2-2",
                "GEO-3-1",
                "GEO-3-2",
                "SRIOV-1",
                "SRIOV-2",
                "SRIOV-3",
                "SRIOV-4",
                "SRIOV-5",
                "SRIOV-6"
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
                "type": "array"
                },
                "vlanForL2": {
                "items": {
                "properties": {
                "vlanDescription": {
                "type": "string"
                },
                "vlanId": {
                "type": "number"
                },
                "vlanType": {
                "enum": [
                "access",
                "trunk"
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
                "type": "array"
                },
                "profileName": {
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

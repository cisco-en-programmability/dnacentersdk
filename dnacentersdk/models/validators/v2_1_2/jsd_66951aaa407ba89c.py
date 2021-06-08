# -*- coding: utf-8 -*-
"""Cisco DNA Center Create NFV Profile data model.

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


class JSONSchemaValidator66951Aaa407BA89C(object):
    """Create NFV Profile request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator66951Aaa407BA89C, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
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
                "SRIOV-6",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "networkName": {
                "type": [
                "string",
                "null"
                ]
                },
                "servicesToConnect": {
                "items": {
                "properties": {
                "serviceName": {
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
                "vlanId": {
                "type": [
                "number",
                "null"
                ]
                },
                "vlanMode": {
                "enum": [
                "trunk",
                "Access",
                null
                ],
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
                "customTemplate": {
                "items": {
                "properties": {
                "deviceType": {
                "enum": [
                "Cisco 5400 Enterprise Network Compute System",
                "Cisco Integrated Services Virtual Router",
                "Cisco Adaptive Security Virtual Appliance (ASAv)",
                "NFVIS",
                "ASAV",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "template": {
                "type": [
                "string",
                "null"
                ]
                },
                "templateType": {
                "enum": [
                "Onboarding Template(s)",
                "Day-N-Template(s)",
                null
                ],
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
                "deviceTag": {
                "type": [
                "string",
                "null"
                ]
                },
                "deviceType": {
                "enum": [
                "Cisco 5400 Enterprise Network Compute System",
                "Cisco 5100 Enterprise Network Compute System",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "directInternetAccessForFirewall": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "serviceProviderProfile": {
                "items": {
                "properties": {
                "connect": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "connectDefaultGatewayOnWan": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "linkType": {
                "enum": [
                "GigabitEthernet",
                "Cellular",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "serviceProvider": {
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
                "services": {
                "items": {
                "properties": {
                "firewallMode": {
                "enum": [
                "routed",
                "transparent",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "imageName": {
                "type": [
                "string",
                "null"
                ]
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
                "vWASS-50000-Resized",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "serviceName": {
                "type": [
                "string",
                "null"
                ]
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
                "linux",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "vNicMapping": {
                "items": {
                "properties": {
                "assignIpAddressToNetwork": {
                "type": [
                "string",
                "null"
                ]
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
                "SRIOV-6",
                null
                ],
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
                "vlanForL2": {
                "items": {
                "properties": {
                "vlanDescription": {
                "type": [
                "string",
                "null"
                ]
                },
                "vlanId": {
                "type": [
                "number",
                "null"
                ]
                },
                "vlanType": {
                "enum": [
                "access",
                "trunk",
                null
                ],
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array"
                ]
                },
                "profileName": {
                "type": [
                "string"
                ]
                }
                },
                "required": [
                "profileName",
                "device"
                ],
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

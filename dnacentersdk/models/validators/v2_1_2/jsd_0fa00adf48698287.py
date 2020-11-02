# -*- coding: utf-8 -*-
"""DNA Center Update NFV Profile data model.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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


class JSONSchemaValidator0Fa00Adf48698287(object):
    """Update NFV Profile request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator0Fa00Adf48698287, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "device": {
                "description":
                "Device",
                "items": {
                "properties": {
                "currentDeviceTag": {
                "description":
                "Old Device Tag",
                "type": [
                "string",
                "null"
                ]
                },
                "customNetworks": {
                "description":
                "Custom Networks",
                "items": {
                "properties": {
                "connectionType": {
                "description":
                "Connection Type",
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
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "servicesToConnect": {
                "description":
                "Services To Connect",
                "items": {
                "properties": {
                "serviceName": {
                "description":
                "Service",
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
                "description":
                "Network Mode",
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
                "description":
                "Custom Template",
                "items": {
                "properties": {
                "deviceType": {
                "description":
                "Device Type",
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
                "description":
                "Template",
                "type": [
                "string",
                "null"
                ]
                },
                "templateType": {
                "description":
                "Project Name",
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
                "description":
                "Device Tag",
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
                "services": {
                "description":
                "Services",
                "items": {
                "properties": {
                "firewallMode": {
                "description":
                "Mode",
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
                "description":
                "Image Name",
                "type": [
                "string",
                "null"
                ]
                },
                "profileType": {
                "description":
                "Profile",
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
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "serviceType": {
                "description":
                "Type",
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
                "description":
                "Topology",
                "items": {
                "properties": {
                "assignIpAddressToNetwork": {
                "description":
                "Assign Ip",
                "type": [
                "string",
                "null"
                ]
                },
                "networkType": {
                "description":
                "Type",
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
                "description":
                "Vlan",
                "items": {
                "properties": {
                "vlanDescription": {
                "description":
                "Description",
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
                "description":
                "Type",
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
                }
                },
                "required": [
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

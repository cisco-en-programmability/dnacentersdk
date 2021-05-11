# -*- coding: utf-8 -*-
"""DNA Center Create NFV Profile data model.

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


class JSONSchemaValidator66951Aaa407BA89C(object):
    """Create NFV Profile request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator66951Aaa407BA89C, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "device": {
                "description":
                "Device",
                "items": {
                "properties": {
                "customNetworks": {
                "description":
                "Custom network details array",
                "items": {
                "properties": {
                "connectionType": {
                "description":
                "Type of network connection from custom network
                 (eg: lan)",
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
                "Name of custom network (eg: cust-1)",
                "type": [
                "string",
                "null"
                ]
                },
                "servicesToConnect": {
                "description":
                "Custom network connection to services list",
                "items": {
                "properties": {
                "serviceName": {
                "description":
                "Name of service to be connected to the custom
                 network (eg: router-1)",
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
                "Network mode (eg Access or Trunk)",
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
                "Details of custom template to be pushed to the
                 device",
                "items": {
                "properties": {
                "deviceType": {
                "description":
                "Type of the device(eg: Cisco 5400 Enterprise
                 Network Compute System)",
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
                "Name of the template(eg NFVIS template)",
                "type": [
                "string",
                "null"
                ]
                },
                "templateType": {
                "description":
                "Name of the template type to which template is
                 associated (eg: Cloud DayN Templates)",
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
                "Device Tag name(eg: dev1)",
                "type": [
                "string",
                "null"
                ]
                },
                "deviceType": {
                "description":
                "Name of the device used in creating nfv profile",
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
                "description":
                "Service Providers",
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
                "description":
                "Name of connection type(eg: GigabitEthernet)",
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
                "description":
                "Name of the service provider(eg: Airtel)",
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
                "description":
                "service details array",
                "items": {
                "properties": {
                "firewallMode": {
                "description":
                "Firewall mode details example (routed,
                 transparent)",
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
                "Service image name (eg: isrv-
                 universalk9.16.12.01a.tar.gz)",
                "type": [
                "string",
                "null"
                ]
                },
                "profileType": {
                "description":
                "Profile type of service (eg: ISRv-mini)",
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
                "Name of the service (eg: Router-1)",
                "type": [
                "string",
                "null"
                ]
                },
                "serviceType": {
                "description":
                "Service type (eg: ISRV)",
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
                "Service connection array",
                "items": {
                "properties": {
                "assignIpAddressToNetwork": {
                "description":
                "Assign ip address to network (eg: true or false)",
                "type": [
                "string",
                "null"
                ]
                },
                "networkType": {
                "description":
                "Type of connection (eg:  wan, lan or internal)",
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
                "Vlan description(eg: Access 4018)",
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
                "Vlan type(eg: Access or Trunk)",
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
                "description":
                "Name of the profile to create NFV profile",
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

# -*- coding: utf-8 -*-
"""DNA Center Provision NFV data model.

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


class JSONSchemaValidator828828F44F28Bd0D(object):
    """Provision NFV request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator828828F44F28Bd0D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "provisioning": {
                "description":
                "Provisioning",
                "items": {
                "properties": {
                "device": {
                "description":
                "Device",
                "items": {
                "properties": {
                "customNetworks": {
                "description":
                "Custom Networks",
                "items": {
                "properties": {
                "ipAddressPool": {
                "description":
                "Ip Address Pool",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "port": {
                "description":
                "Port",
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
                "deviceSerialNumber": {
                "description":
                "Device Serial Number",
                "type": [
                "string",
                "null"
                ]
                },
                "ip": {
                "description":
                "Ip",
                "type": [
                "string",
                "null"
                ]
                },
                "serviceProviders": {
                "description":
                "Service Providers",
                "items": {
                "properties": {
                "serviceProvider": {
                "description":
                "Service Provider",
                "type": [
                "string",
                "null"
                ]
                },
                "wanInterface": {
                "description":
                "Wan Interface",
                "properties": {
                "bandwidth": {
                "description":
                "Bandwidth",
                "type": [
                "string",
                "null"
                ]
                },
                "gateway": {
                "description":
                "Gateway",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceName": {
                "description":
                "Interface Name",
                "type": [
                "string",
                "null"
                ]
                },
                "ipAddress": {
                "description":
                "Ip Address",
                "type": [
                "string",
                "null"
                ]
                },
                "subnetmask": {
                "description":
                "Subnetmask",
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
                "Services",
                "items": {
                "properties": {
                "adminPasswordHash": {
                "description":
                "Admin Password Hash",
                "type": [
                "string",
                "null"
                ]
                },
                "centralManagerIP": {
                "description":
                "Central Manager IP",
                "type": [
                "string",
                "null"
                ]
                },
                "centralRegistrationKey": {
                "description":
                "Central Registration Key",
                "type": [
                "string",
                "null"
                ]
                },
                "commonKey": {
                "description":
                "Common Key",
                "type": [
                "string",
                "null"
                ]
                },
                "mode": {
                "description":
                "Mode",
                "type": [
                "string",
                "null"
                ]
                },
                "systemIp": {
                "description":
                "System Ip",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                "Type",
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
                "subPools": {
                "description":
                "Sub Pools",
                "items": {
                "properties": {
                "gateway": {
                "description":
                "Gateway",
                "type": [
                "string",
                "null"
                ]
                },
                "ipSubnet": {
                "description":
                "Ip Subnet",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "parentPoolName": {
                "description":
                "Parent Pool Name",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                "Type",
                "enum": [
                "Lan",
                "Management",
                "Service",
                "Wan",
                "Generic",
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
                "tagName": {
                "description":
                "Tag Name",
                "type": [
                "string",
                "null"
                ]
                },
                "templateParam": {
                "description":
                "Template Param",
                "properties": {
                "asav": {
                "description":
                "Asav",
                "properties": {
                "var1": {
                "description":
                "Var1",
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
                "nfvis": {
                "description":
                "Nfvis",
                "properties": {
                "var1": {
                "description":
                "Var1",
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "vlan": {
                "description":
                "Vlan",
                "items": {
                "properties": {
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaces": {
                "description":
                "Interfaces",
                "type": [
                "string",
                "null"
                ]
                },
                "network": {
                "description":
                "Network",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                "Type",
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
                "site": {
                "description":
                "Site",
                "properties": {
                "area": {
                "description":
                "Area",
                "properties": {
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "parentName": {
                "description":
                "Parent Name",
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
                "building": {
                "description":
                "Building",
                "properties": {
                "address": {
                "description":
                "Address",
                "type": [
                "string",
                "null"
                ]
                },
                "latitude": {
                "type": [
                "number",
                "null"
                ]
                },
                "longitude": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "parentName": {
                "description":
                "Parent Name",
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
                "floor": {
                "description":
                "Floor",
                "properties": {
                "height": {
                "type": [
                "number",
                "null"
                ]
                },
                "length": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "parentName": {
                "description":
                "Parent Name",
                "type": [
                "string",
                "null"
                ]
                },
                "rfModel": {
                "description":
                "Rf Model",
                "type": [
                "string",
                "null"
                ]
                },
                "width": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "siteProfileName": {
                "description":
                "Site Profile Name",
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
                "siteProfile": {
                "description":
                "Site Profile",
                "items": {
                "properties": {
                "device": {
                "description":
                "Device",
                "items": {
                "properties": {
                "customNetworks": {
                "description":
                "Custom Networks",
                "items": {
                "properties": {
                "connectionType": {
                "description":
                "Connection Type",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "networkMode": {
                "description":
                "Network Mode",
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
                "service": {
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
                "vlan": {
                "description":
                "Vlan",
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
                "customServices": {
                "description":
                "Custom Services",
                "items": {
                "properties": {
                "applicationType": {
                "description":
                "Application Type",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "profile": {
                "description":
                "Profile",
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
                "NFVIS",
                "ASAv",
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
                "deviceType": {
                "description":
                "Device Type",
                "enum": [
                "ENCS5100",
                "ENCS5400",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "dia": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "serviceProviders": {
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
                "defaultGateway": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "linkType": {
                "description":
                "Link Type",
                "enum": [
                "GigabitEthernet",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "serviceProvider": {
                "description":
                "Service Provider",
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
                "Services",
                "items": {
                "properties": {
                "mode": {
                "description":
                "Mode",
                "type": [
                "string",
                "null"
                ]
                },
                "profile": {
                "description":
                "Profile",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
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
                "tagName": {
                "description":
                "Tag Name",
                "type": [
                "string",
                "null"
                ]
                },
                "vlan": {
                "description":
                "Vlan",
                "items": {
                "properties": {
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                "Type",
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
                "siteProfileName": {
                "description":
                "Site Profile Name",
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
                "array"
                ]
                }
                },
                "required": [
                "siteProfile",
                "provisioning"
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

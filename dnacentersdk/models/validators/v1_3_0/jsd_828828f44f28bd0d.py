# -*- coding: utf-8 -*-
"""DNA Center Provision NFV data model.

Copyright (c) 2019 Cisco and/or its affiliates.

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
                "type": "string"
                },
                "name": {
                "description":
                "Name",
                "type": "string"
                },
                "port": {
                "description":
                "Port",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "deviceSerialNumber": {
                "description":
                "Device Serial Number",
                "type": "string"
                },
                "ip": {
                "description":
                "Ip",
                "type": "string"
                },
                "serviceProviders": {
                "description":
                "Service Providers",
                "items": {
                "properties": {
                "serviceProvider": {
                "description":
                "Service Provider",
                "type": "string"
                },
                "wanInterface": {
                "description":
                "Wan Interface",
                "properties": {
                "bandwidth": {
                "description":
                "Bandwidth",
                "type": "string"
                },
                "gateway": {
                "description":
                "Gateway",
                "type": "string"
                },
                "interfaceName": {
                "description":
                "Interface Name",
                "type": "string"
                },
                "ipAddress": {
                "description":
                "Ip Address",
                "type": "string"
                },
                "subnetmask": {
                "description":
                "Subnetmask",
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "services": {
                "description":
                "Services",
                "items": {
                "properties": {
                "adminPasswordHash": {
                "description":
                "Admin Password Hash",
                "type": "string"
                },
                "centralManagerIP": {
                "description":
                "Central Manager IP",
                "type": "string"
                },
                "centralRegistrationKey": {
                "description":
                "Central Registration Key",
                "type": "string"
                },
                "commonKey": {
                "description":
                "Common Key",
                "type": "string"
                },
                "mode": {
                "description":
                "Mode",
                "type": "string"
                },
                "systemIp": {
                "description":
                "System Ip",
                "type": "string"
                },
                "type": {
                "description":
                "Type",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "subPools": {
                "description":
                "Sub Pools",
                "items": {
                "properties": {
                "gateway": {
                "description":
                "Gateway",
                "type": "string"
                },
                "ipSubnet": {
                "description":
                "Ip Subnet",
                "type": "string"
                },
                "name": {
                "description":
                "Name",
                "type": "string"
                },
                "parentPoolName": {
                "description":
                "Parent Pool Name",
                "type": "string"
                },
                "type": {
                "description":
                "Type",
                "enum": [
                "Lan",
                "Management",
                "Service",
                "Wan",
                "Generic"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "tagName": {
                "description":
                "Tag Name",
                "type": "string"
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
                "type": "string"
                }
                },
                "type": "object"
                },
                "nfvis": {
                "description":
                "Nfvis",
                "properties": {
                "var1": {
                "description":
                "Var1",
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "vlan": {
                "description":
                "Vlan",
                "items": {
                "properties": {
                "id": {
                "description":
                "Id",
                "type": "string"
                },
                "interfaces": {
                "description":
                "Interfaces",
                "type": "string"
                },
                "network": {
                "description":
                "Network",
                "type": "string"
                },
                "type": {
                "description":
                "Type",
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
                "type": "string"
                },
                "parentName": {
                "description":
                "Parent Name",
                "type": "string"
                }
                },
                "type": "object"
                },
                "building": {
                "description":
                "Building",
                "properties": {
                "address": {
                "description":
                "Address",
                "type": "string"
                },
                "latitude": {
                "type": "number"
                },
                "longitude": {
                "type": "number"
                },
                "name": {
                "description":
                "Name",
                "type": "string"
                },
                "parentName": {
                "description":
                "Parent Name",
                "type": "string"
                }
                },
                "type": "object"
                },
                "floor": {
                "description":
                "Floor",
                "properties": {
                "height": {
                "type": "number"
                },
                "length": {
                "type": "number"
                },
                "name": {
                "description":
                "Name",
                "type": "string"
                },
                "parentName": {
                "description":
                "Parent Name",
                "type": "string"
                },
                "rfModel": {
                "description":
                "Rf Model",
                "type": "string"
                },
                "width": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "siteProfileName": {
                "description":
                "Site Profile Name",
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "type": "string"
                },
                "name": {
                "description":
                "Name",
                "type": "string"
                },
                "networkMode": {
                "description":
                "Network Mode",
                "type": "string"
                },
                "servicesToConnect": {
                "description":
                "Services To Connect",
                "items": {
                "properties": {
                "service": {
                "description":
                "Service",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "vlan": {
                "description":
                "Vlan",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "customServices": {
                "description":
                "Custom Services",
                "items": {
                "properties": {
                "applicationType": {
                "description":
                "Application Type",
                "type": "string"
                },
                "name": {
                "description":
                "Name",
                "type": "string"
                },
                "profile": {
                "description":
                "Profile",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "ASAv"
                ],
                "type": "string"
                },
                "template": {
                "description":
                "Template",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "deviceType": {
                "description":
                "Device Type",
                "enum": [
                "ENCS5100",
                "ENCS5400"
                ],
                "type": "string"
                },
                "dia": {
                "type": "boolean"
                },
                "serviceProviders": {
                "description":
                "Service Providers",
                "items": {
                "properties": {
                "connect": {
                "type": "boolean"
                },
                "defaultGateway": {
                "type": "boolean"
                },
                "linkType": {
                "description":
                "Link Type",
                "enum": [
                "GigabitEthernet"
                ],
                "type": "string"
                },
                "serviceProvider": {
                "description":
                "Service Provider",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "services": {
                "description":
                "Services",
                "items": {
                "properties": {
                "mode": {
                "description":
                "Mode",
                "type": "string"
                },
                "profile": {
                "description":
                "Profile",
                "type": "string"
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
                "silverpeak"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "tagName": {
                "description":
                "Tag Name",
                "type": "string"
                },
                "vlan": {
                "description":
                "Vlan",
                "items": {
                "properties": {
                "id": {
                "description":
                "Id",
                "type": "string"
                },
                "type": {
                "description":
                "Type",
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
                "siteProfileName": {
                "description":
                "Site Profile Name",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
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

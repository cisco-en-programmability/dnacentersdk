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


class JSONSchemaValidator6F9CDa9A465884B4(object):
    """Provision NFV request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator6F9CDa9A465884B4, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "provisioning": {
                "description":
                "Provisioning details array",
                "items": {
                "properties": {
                "device": {
                "description":
                "Device details array",
                "items": {
                "properties": {
                "customNetworks": {
                "description":
                "Custom network details",
                "items": {
                "properties": {
                "ipAddressPool": {
                "description":
                "IP address pool of sub pool (eg: 175.175.140.1)",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "Name of custom network (eg: cust-1)",
                "type": [
                "string",
                "null"
                ]
                },
                "port": {
                "description":
                "Port for custom network (eg: 443)",
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
                "Serial number of device (eg: FGL210710QY)",
                "type": [
                "string",
                "null"
                ]
                },
                "ip": {
                "description":
                "IP address of the device (eg: 172.20.126.90)",
                "type": [
                "string",
                "null"
                ]
                },
                "serviceProviders": {
                "description":
                "Service provider details",
                "items": {
                "properties": {
                "serviceProvider": {
                "description":
                "Name of the service provider (eg: Airtel)",
                "type": [
                "string",
                "null"
                ]
                },
                "wanInterface": {
                "description":
                "Wan interface details",
                "properties": {
                "bandwidth": {
                "description":
                "Bandwidth limit (eg: 100)",
                "type": [
                "string",
                "null"
                ]
                },
                "gateway": {
                "description":
                "Gateway (eg: 175.175.190.1)",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceName": {
                "description":
                "Name of the interface (eg: GE0-0)",
                "type": [
                "string",
                "null"
                ]
                },
                "ipAddress": {
                "description":
                "IP address (eg: 175.175.190.205)",
                "type": [
                "string",
                "null"
                ]
                },
                "subnetmask": {
                "description":
                "Subnet mask (eg: 255.255.255.0)",
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
                "Service details",
                "items": {
                "properties": {
                "adminPasswordHash": {
                "description":
                "Admin password hash",
                "type": [
                "string",
                "null"
                ]
                },
                "centralManagerIP": {
                "description":
                "WAAS Package needs to be installed to populate
                 Central Manager IP automatically.",
                "type": [
                "string",
                "null"
                ]
                },
                "centralRegistrationKey": {
                "description":
                "Central registration key",
                "type": [
                "string",
                "null"
                ]
                },
                "commonKey": {
                "description":
                "Common key",
                "type": [
                "string",
                "null"
                ]
                },
                "disk": {
                "description":
                "Name of disk type (eg: internal)",
                "type": [
                "string",
                "null"
                ]
                },
                "mode": {
                "description":
                "Mode of firewall (eg: transparent)",
                "type": [
                "string",
                "null"
                ]
                },
                "systemIp": {
                "description":
                "System IP",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                "Type of service (eg: ISR)",
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
                "IP sub pool detail",
                "items": {
                "properties": {
                "gateway": {
                "description":
                "IP address for gate way (eg: 175.175.140.1)",
                "type": [
                "string",
                "null"
                ]
                },
                "ipSubnet": {
                "description":
                "IP pool cidir (eg: 175.175.140.0)",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "Name of the ip sub pool (eg; Lan-65)",
                "type": [
                "string",
                "null"
                ]
                },
                "parentPoolName": {
                "description":
                "Name of parent pool (global pool name)",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                "Tyep of ip sub pool (eg: Lan)",
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
                "Name of device tag (eg: dev1)",
                "type": [
                "string",
                "null"
                ]
                },
                "templateParam": {
                "description":
                "Template detail",
                "properties": {
                "asav": {
                "description":
                "Asav template details",
                "properties": {
                "var1": {
                "description":
                "Variable for asav template (eg: \"test\":\"Hello
                 asav\")",
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
                "Nfvis template details",
                "properties": {
                "var1": {
                "description":
                "Variable for nfvis template (eg: \"test\":\"Hello
                 nfvis\")",
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
                "Vlan details",
                "items": {
                "properties": {
                "id": {
                "description":
                "Vlan id(e: .4018)",
                "type": [
                "string",
                "null"
                ]
                },
                "interfaces": {
                "description":
                "Interface (eg: GigabitEathernet1/0)",
                "type": [
                "string",
                "null"
                ]
                },
                "network": {
                "description":
                "Network name to connect (eg: lan-net)",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                "Vlan type(eg. Access or Trunk)",
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
                "Site details",
                "properties": {
                "area": {
                "description":
                "Area details",
                "properties": {
                "name": {
                "description":
                "Name of the area (eg: Area1)",
                "type": [
                "string",
                "null"
                ]
                },
                "parentName": {
                "description":
                "Parent name of the area to be created",
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
                "Building details",
                "properties": {
                "address": {
                "description":
                "Address of the building to be created",
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
                "Name of the building (eg: building1)",
                "type": [
                "string",
                "null"
                ]
                },
                "parentName": {
                "description":
                "Address of the building to be created",
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
                "Name of the floor (eg:floor-1)",
                "type": [
                "string",
                "null"
                ]
                },
                "parentName": {
                "description":
                "Parent name of the floor to be created",
                "type": [
                "string",
                "null"
                ]
                },
                "rfModel": {
                "description":
                "Type of floor (eg: Cubes And Walled Offices)",
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
                "Name of site profile to be provision with device",
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
                "Site profile details array",
                "items": {
                "properties": {
                "device": {
                "description":
                "Device details array",
                "items": {
                "properties": {
                "customNetworks": {
                "description":
                "Custom network details",
                "items": {
                "properties": {
                "connectionType": {
                "description":
                "Type of network connection from custom network
                 (eg: lan)",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "Name of custom network (eg: cust-1)",
                "type": [
                "string",
                "null"
                ]
                },
                "networkMode": {
                "description":
                "Network mode (eg Access or Trunk)",
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
                "service": {
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
                "vlan": {
                "description":
                "Vlan id for the custom network(eg: 4000)",
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
                "Custom services array",
                "items": {
                "properties": {
                "applicationType": {
                "description":
                "Application type of custom service (eg: LINUX)",
                "type": [
                "string",
                "null"
                ]
                },
                "imageName": {
                "description":
                "Image name of custom service (eg:
                 redhat7.tar.gz.tar.gz)",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "Name of custom service (eg: LINUX-1)",
                "type": [
                "string",
                "null"
                ]
                },
                "profile": {
                "description":
                "Profile type of service (eg: rhel7-medium)",
                "type": [
                "string",
                "null"
                ]
                },
                "topology": {
                "description":
                "Custom service connection array",
                "properties": {
                "assignIp": {
                "description":
                "Assign ip to network (eg: true)",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "Name of connection from custom service(eg: wan-
                 net)",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                "Type of connection from custom service (eg:  wan,
                 lan or internal)",
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
                "customTemplate": {
                "description":
                "Details of custom template to be pushed to the
                 device",
                "items": {
                "properties": {
                "deviceType": {
                "description":
                "Type of the device(eg: NFVIS)",
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
                "Name of the template(eg NFVIS template)",
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
                "Name of the device used in creating nfv
                 profile(eg: ENCS5400)",
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
                "Service provider details array",
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
                "Name of connection type(eg: GigabitEthernet)",
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
                "Service details array",
                "items": {
                "properties": {
                "imageName": {
                "description":
                "Name of image (eg: isrv-
                 universalk9.16.06.02.tar.gz)",
                "type": [
                "string",
                "null"
                ]
                },
                "mode": {
                "description":
                "Mode of firewall (eg: routed, transparent)",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "Name of the service (eg: isrv)",
                "type": [
                "string",
                "null"
                ]
                },
                "profile": {
                "description":
                "Profile type of service (eg: ISRv-mini)",
                "type": [
                "string",
                "null"
                ]
                },
                "topology": {
                "description":
                "Service connection array",
                "properties": {
                "assignIp": {
                "description":
                "Assign ip address to network (eg: true)",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "Name of connection (eg: wan-net)",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                "Type of connection (eg:  wan, lan or internal)",
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
                "type": {
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
                "Device Tag name(eg: dev1)",
                "type": [
                "string",
                "null"
                ]
                },
                "vlan": {
                "description":
                "Vlan details",
                "items": {
                "properties": {
                "id": {
                "description":
                "Vlan id(eg.4018)",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                "Vlan type(eg. Access or Trunk)",
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
                "Name of the profile to create site profile
                 profile( eg: profile-1)",
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

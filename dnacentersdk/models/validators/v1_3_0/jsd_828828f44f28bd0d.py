# -*- coding: utf-8 -*-
"""Cisco DNA Center Provision NFV data model.

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


class JSONSchemaValidator828828F44F28Bd0D(object):
    """Provision NFV request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator828828F44F28Bd0D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "provisioning": {
                "items": {
                "properties": {
                "device": {
                "items": {
                "properties": {
                "customNetworks": {
                "items": {
                "properties": {
                "ipAddressPool": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "port": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "ip": {
                "type": [
                "string",
                "null"
                ]
                },
                "serviceProviders": {
                "items": {
                "properties": {
                "serviceProvider": {
                "type": [
                "string",
                "null"
                ]
                },
                "wanInterface": {
                "properties": {
                "bandwidth": {
                "type": [
                "string",
                "null"
                ]
                },
                "gateway": {
                "type": [
                "string",
                "null"
                ]
                },
                "interfaceName": {
                "type": [
                "string",
                "null"
                ]
                },
                "ipAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "subnetmask": {
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
                "items": {
                "properties": {
                "adminPasswordHash": {
                "type": [
                "string",
                "null"
                ]
                },
                "centralManagerIP": {
                "type": [
                "string",
                "null"
                ]
                },
                "centralRegistrationKey": {
                "type": [
                "string",
                "null"
                ]
                },
                "commonKey": {
                "type": [
                "string",
                "null"
                ]
                },
                "mode": {
                "type": [
                "string",
                "null"
                ]
                },
                "systemIp": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
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
                "items": {
                "properties": {
                "gateway": {
                "type": [
                "string",
                "null"
                ]
                },
                "ipSubnet": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "parentPoolName": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "templateParam": {
                "properties": {
                "asav": {
                "properties": {
                "var1": {
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
                "properties": {
                "var1": {
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
                "items": {
                "properties": {
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "interfaces": {
                "type": [
                "string",
                "null"
                ]
                },
                "network": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
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
                "properties": {
                "area": {
                "properties": {
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "parentName": {
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
                "properties": {
                "address": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "parentName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "parentName": {
                "type": [
                "string",
                "null"
                ]
                },
                "rfModel": {
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
                "items": {
                "properties": {
                "device": {
                "items": {
                "properties": {
                "customNetworks": {
                "items": {
                "properties": {
                "connectionType": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "networkMode": {
                "type": [
                "string",
                "null"
                ]
                },
                "servicesToConnect": {
                "items": {
                "properties": {
                "service": {
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
                "items": {
                "properties": {
                "applicationType": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "profile": {
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
                "mode": {
                "type": [
                "string",
                "null"
                ]
                },
                "profile": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "vlan": {
                "items": {
                "properties": {
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
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

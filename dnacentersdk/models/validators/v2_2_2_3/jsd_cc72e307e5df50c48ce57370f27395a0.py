# -*- coding: utf-8 -*-
"""Cisco DNA Center ProvisionNFV data model.

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


class JSONSchemaValidatorCc72E307E5Df50C48Ce57370F27395A0(object):
    """ProvisionNFV request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorCc72E307E5Df50C48Ce57370F27395A0, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
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
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "port": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "deviceSerialNumber": {
                "type": "string"
                },
                "ip": {
                "type": "string"
                },
                "serviceProviders": {
                "items": {
                "properties": {
                "serviceProvider": {
                "type": "string"
                },
                "wanInterface": {
                "properties": {
                "bandwidth": {
                "type": "string"
                },
                "gateway": {
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "ipAddress": {
                "type": "string"
                },
                "subnetmask": {
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
                "items": {
                "properties": {
                "adminPasswordHash": {
                "type": "string"
                },
                "centralManagerIP": {
                "type": "string"
                },
                "centralRegistrationKey": {
                "type": "string"
                },
                "commonKey": {
                "type": "string"
                },
                "disk": {
                "type": "string"
                },
                "mode": {
                "type": "string"
                },
                "systemIp": {
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "subPools": {
                "items": {
                "properties": {
                "gateway": {
                "type": "string"
                },
                "ipSubnet": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "parentPoolName": {
                "type": "string"
                },
                "type": {
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
                "type": "string"
                },
                "templateParam": {
                "properties": {
                "asav": {
                "properties": {
                "var1": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "nfvis": {
                "properties": {
                "var1": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "vlan": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "interfaces": {
                "type": "string"
                },
                "network": {
                "type": "string"
                },
                "type": {
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
                "properties": {
                "area": {
                "properties": {
                "name": {
                "type": "string"
                },
                "parentName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "building": {
                "properties": {
                "address": {
                "type": "string"
                },
                "latitude": {
                "type": "number"
                },
                "longitude": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "parentName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "floor": {
                "properties": {
                "height": {
                "type": "number"
                },
                "length": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "parentName": {
                "type": "string"
                },
                "rfModel": {
                "type": "string"
                },
                "width": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "siteProfileName": {
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
                "items": {
                "properties": {
                "device": {
                "items": {
                "properties": {
                "customNetworks": {
                "items": {
                "properties": {
                "connectionType": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "networkMode": {
                "type": "string"
                },
                "servicesToConnect": {
                "items": {
                "properties": {
                "service": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "vlan": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "customServices": {
                "items": {
                "properties": {
                "applicationType": {
                "type": "string"
                },
                "imageName": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "profile": {
                "type": "string"
                },
                "topology": {
                "properties": {
                "assignIp": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "type": {
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
                "customTemplate": {
                "items": {
                "properties": {
                "deviceType": {
                "enum": [
                "NFVIS",
                "ASAv"
                ],
                "type": "string"
                },
                "template": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "deviceType": {
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
                "items": {
                "properties": {
                "connect": {
                "type": "boolean"
                },
                "defaultGateway": {
                "type": "boolean"
                },
                "linkType": {
                
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
                "imageName": {
                "type": "string"
                },
                "mode": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "profile": {
                "type": "string"
                },
                "topology": {
                "properties": {
                "assignIp": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
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
                "type": "string"
                },
                "vlan": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "type": {
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

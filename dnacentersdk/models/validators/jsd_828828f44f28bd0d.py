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
from dnacentersdk.exceptions import MalformedRequest

from builtins import *

class JSONSchemaValidator828828F44F28Bd0D(object):
    """Provision NFV request schema definition."""
    def __init__(self):
        # print("created 8288-28f4-4f28-bd0d")
        super(JSONSchemaValidator828828F44F28Bd0D, self).__init__()
        self._validator = fastjsonschema.compile( {'type': 'object', 'properties': {'siteProfile': {'type': 'array', 'items': {'type': 'object', 'properties': {'siteProfileName': {'type': 'string'}, 'device': {'type': 'array', 'items': {'type': 'object', 'properties': {'deviceType': {'type': 'string', 'enum': ['ENCS5100', 'ENCS5400']}, 'tagName': {'type': 'string'}, 'serviceProviders': {'type': 'array', 'items': {'type': 'object', 'properties': {'serviceProvider': {'type': 'string'}, 'linkType': {'type': 'string', 'enum': ['GigabitEthernet']}, 'connect': {'type': 'boolean'}, 'defaultGateway': {'type': 'boolean'}}}}, 'dia': {'type': 'boolean'}, 'services': {'type': 'array', 'items': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['isr', 'vedge', 'waas', 'asa', 'ngfw', 'paloalto', 'fortinet', 'checkpoint', 'riverbed', 'silverpeak']}, 'profile': {'type': 'string'}, 'mode': {'type': 'string'}}}}, 'customServices': {'type': 'array', 'items': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'applicationType': {'type': 'string'}, 'profile': {'type': 'string'}}}}, 'customNetworks': {'type': 'array', 'items': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'servicesToConnect': {'type': 'array', 'items': {'type': 'object', 'properties': {'service': {'type': 'string'}}}}, 'connectionType': {'type': 'string'}, 'networkMode': {'type': 'string'}, 'vlan': {'type': 'string'}}}}, 'vlan': {'type': 'array', 'items': {'type': 'object', 'properties': {'type': {'type': 'string'}, 'id': {'type': 'string'}}}}}}}, 'customTemplate': {'type': 'array', 'items': {'type': 'object', 'properties': {'deviceType': {'type': 'string', 'enum': ['NFVIS', 'ASAv']}, 'template': {'type': 'string'}}}}}}}, 'provisioning': {'type': 'array', 'items': {'type': 'object', 'properties': {'site': {'type': 'object', 'properties': {'siteProfileName': {'type': 'string'}, 'area': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'parentName': {'type': 'string'}}}, 'building': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'address': {'type': 'string'}}}, 'floor': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'parentName': {'type': 'string'}}}}}, 'templateParam': {'type': 'object', 'properties': {'nfvis': {'type': 'object', 'properties': {'var1': {'type': 'string'}}}, 'asav': {'type': 'object', 'properties': {'var1': {'type': 'string'}}}}}, 'networksettings': {'type': 'object', 'properties': {'ipPool': {'type': 'object', 'properties': {'globalPool': {'type': 'object', 'properties': {'name': {'type': 'string'}}}}}}}, 'device': {'type': 'array', 'items': {'type': 'object', 'properties': {'ip': {'type': 'string'}, 'deviceSerialNumber': {'type': 'string'}, 'tagName': {'type': 'string'}, 'serviceProviders': {'type': 'array', 'items': {'type': 'object', 'properties': {'serviceProvider': {'type': 'string'}, 'wanInterface': {'type': 'object', 'properties': {'ipAddress': {'type': 'string'}, 'interfaceName': {'type': 'string'}, 'subnetmask': {'type': 'string'}, 'bandwidth': {'type': 'string'}, 'gateway': {'type': 'string'}}}}}}, 'services': {'type': 'array', 'items': {'type': 'object', 'properties': {'type': {'type': 'string'}, 'mode': {'type': 'string'}, 'systemIp': {'type': 'string'}, 'centralManagerIP': {'type': 'string'}, 'centralRegistrationKey': {'type': 'string'}, 'commonKey': {'type': 'string'}, 'adminPasswordHash': {'type': 'string'}}}}, 'vlan': {'type': 'array', 'items': {'type': 'object', 'properties': {'type': {'type': 'string'}, 'id': {'type': 'string'}, 'interfaces': {'type': 'string'}, 'network': {'type': 'string'}}}}, 'subPools': {'type': 'array', 'items': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['Lan', 'Management', 'Service', 'Wan', 'Generic']}, 'name': {'type': 'string'}, 'ipSubnet': {'type': 'string'}, 'gateway': {'type': 'string'}}}}, 'customNetworks': {'type': 'array', 'items': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'port': {'type': 'string'}, 'ipAddressPool': {'type': 'string'}}}}}}}}}}, 'callbackUrl': {'type': 'string'}}} )

    def validate(self, request):
        try:
            self._validator(request)
            return True
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(request, e.message))
            return False
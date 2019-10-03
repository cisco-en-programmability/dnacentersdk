# -*- coding: utf-8 -*-
"""DNA Center Gets border device details from SDA Fabric data model.

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


class JSONSchemaValidatorD0B3593C4A7AAf22(object):
    """Gets border device details from SDA Fabric request schema
    definition."""
    def __init__(self):
        super(JSONSchemaValidatorD0B3593C4A7AAf22, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "description":
                 {
                "description":
                "Description",
                "type": [
                "string",
                "null"
                ]
                },
                "payload": {
                "description":
                "Payload",
                "properties": {
                "akcSettingsCfs": {
                "description":
                "Akc Settings Cfs",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "authEntityClass": {
                "type": [
                "number",
                "null"
                ]
                },
                "authEntityId": {
                "type": [
                "number",
                "null"
                ]
                },
                "cfsChangeInfo": {
                "description":
                "Cfs Change Info",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "configs": {
                "description":
                "Configs",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "createTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "customProvisions": {
                "description":
                "Custom Provisions",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "deployPending": {
                "description":
                "Deploy Pending",
                "type": [
                "string",
                "null"
                ]
                },
                "deployed": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "deviceInterfaceInfo": {
                "description":
                "Device Interface Info",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "deviceSettings": {
                "description":
                "Device Settings",
                "properties": {
                "connectedTo": {
                "description":
                "Connected To",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "cpu": {
                "type": [
                "number",
                "null"
                ]
                },
                "deployPending": {
                "description":
                "Deploy Pending",
                "type": [
                "string",
                "null"
                ]
                },
                "dhcpEnabled": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "displayName": {
                "description":
                "Display Name",
                "type": [
                "string",
                "null"
                ]
                },
                "extConnectivitySettings": {
                "description":
                "Ext Connectivity Settings",
                "items": {
                "properties": {
                "deployPending": {
                "description":
                "Deploy Pending",
                "type": [
                "string",
                "null"
                ]
                },
                "displayName": {
                "description":
                "Display Name",
                "type": [
                "string",
                "null"
                ]
                },
                "externalDomainProtocolNumber": {
                "description":
                "External Domain Protocol Number",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceId": {
                "type": [
                "number",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                "Instance Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceVersion": {
                "type": [
                "number",
                "null"
                ]
                },
                "interfaceUuid": {
                "description":
                "Interface Uuid",
                "type": [
                "string",
                "null"
                ]
                },
                "l2Handoff": {
                "description":
                "L2 Handoff",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "l3Handoff": {
                "description":
                "L3 Handoff",
                "items": {
                "properties": {
                "deployPending": {
                "description":
                "Deploy Pending",
                "type": [
                "string",
                "null"
                ]
                },
                "displayName": {
                "description":
                "Display Name",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceId": {
                "type": [
                "number",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                "Instance Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceVersion": {
                "type": [
                "number",
                "null"
                ]
                },
                "localIpAddress": {
                "description":
                "Local Ip Address",
                "type": [
                "string",
                "null"
                ]
                },
                "remoteIpAddress": {
                "description":
                "Remote Ip Address",
                "type": [
                "string",
                "null"
                ]
                },
                "virtualNetwork": {
                "description":
                "Virtual Network",
                "properties": {
                "idRef": {
                "description":
                "Id Ref",
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
                "vlanId": {
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
                "type": [
                "array",
                "null"
                ]
                },
                "policyPropagationEnabled": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "policySgtTag": {
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
                "type": [
                "array",
                "null"
                ]
                },
                "externalConnectivityIpPool": {
                "description":
                "External Connectivity Ip Pool",
                "type": [
                "string",
                "null"
                ]
                },
                "externalDomainRoutingProtocol": {
                "description":
                "External Domain Routing Protocol",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceId": {
                "type": [
                "number",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                "Instance Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceVersion": {
                "type": [
                "number",
                "null"
                ]
                },
                "internalDomainProtocolNumber": {
                "description":
                "Internal Domain Protocol Number",
                "type": [
                "string",
                "null"
                ]
                },
                "memory": {
                "type": [
                "number",
                "null"
                ]
                },
                "nodeType": {
                "description":
                "Node Type",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "storage": {
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
                "displayName": {
                "description":
                "Display Name",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceId": {
                "type": [
                "number",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                "Instance Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceVersion": {
                "type": [
                "number",
                "null"
                ]
                },
                "isSeeded": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "isStale": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "lastUpdateTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "managedSites": {
                "description":
                "Managed Sites",
                "items": {},
                "type": [
                "array",
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
                "namespace": {
                "description":
                "Namespace",
                "type": [
                "string",
                "null"
                ]
                },
                "networkDeviceId": {
                "description":
                "Network Device Id",
                "type": [
                "string",
                "null"
                ]
                },
                "networkWideSettings": {
                "description":
                "Network Wide Settings",
                "properties": {
                "aaa": {
                "description":
                "Aaa",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "cmx": {
                "description":
                "Cmx",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "deployPending": {
                "description":
                "Deploy Pending",
                "type": [
                "string",
                "null"
                ]
                },
                "dhcp": {
                "description":
                "Dhcp",
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
                "ipAddress": {
                "description":
                "Ip Address",
                "properties": {
                "address": {
                "description":
                "Address",
                "type": [
                "string",
                "null"
                ]
                },
                "addressType": {
                "description":
                "Address Type",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "paddedAddress": {
                "description":
                "Padded Address",
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
                "displayName": {
                "description":
                "Display Name",
                "type": [
                "string",
                "null"
                ]
                },
                "dns": {
                "description":
                "Dns",
                "items": {
                "properties": {
                "domainName": {
                "description":
                "Domain Name",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "ip": {
                "description":
                "Ip",
                "properties": {
                "address": {
                "description":
                "Address",
                "type": [
                "string",
                "null"
                ]
                },
                "addressType": {
                "description":
                "Address Type",
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "paddedAddress": {
                "description":
                "Padded Address",
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
                "id": {
                "description":
                "Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceId": {
                "type": [
                "number",
                "null"
                ]
                },
                "instanceTenantId": {
                "description":
                "Instance Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceVersion": {
                "type": [
                "number",
                "null"
                ]
                },
                "ldap": {
                "description":
                "Ldap",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "nativeVlan": {
                "description":
                "Native Vlan",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "netflow": {
                "description":
                "Netflow",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "ntp": {
                "description":
                "Ntp",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "snmp": {
                "description":
                "Snmp",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "syslogs": {
                "description":
                "Syslogs",
                "items": {},
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
                "otherDevice": {
                "description":
                "Other Device",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "provisioningState": {
                "description":
                "Provisioning State",
                "type": [
                "string",
                "null"
                ]
                },
                "resourceVersion": {
                "type": [
                "number",
                "null"
                ]
                },
                "roles": {
                "description":
                "Roles",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "saveWanConnectivityDetailsOnly": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "siteId": {
                "description":
                "Site Id",
                "type": [
                "string",
                "null"
                ]
                },
                "targetIdList": {
                "description":
                "Target Id List",
                "items": {
                "type": [
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "transitNetworks": {
                "description":
                "Transit Networks",
                "items": {
                "properties": {
                "idRef": {
                "description":
                "Id Ref",
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
                "type": {
                "description":
                "Type",
                "type": [
                "string",
                "null"
                ]
                },
                "virtualNetwork": {
                "description":
                "Virtual Network",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "wlan": {
                "description":
                "Wlan",
                "items": {},
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
                "status": {
                "description":
                "Status",
                "type": [
                "string",
                "null"
                ]
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

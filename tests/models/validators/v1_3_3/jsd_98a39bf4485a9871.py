# -*- coding: utf-8 -*-
"""Cisco DNA Center Gets border device detail data model.

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

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidator98A39Bf4485A9871(object):
    """Gets border device detail request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator98A39Bf4485A9871, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "description":
                 {
                "type": [
                "string",
                "null"
                ]
                },
                "payload": {
                "properties": {
                "akcSettingsCfs": {
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
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "configs": {
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
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "deployPending": {
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
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "deviceSettings": {
                "properties": {
                "connectedTo": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "extConnectivitySettings": {
                "items": {
                "properties": {
                "deployPending": {
                "type": [
                "string",
                "null"
                ]
                },
                "displayName": {
                "type": [
                "string",
                "null"
                ]
                },
                "externalDomainProtocolNumber": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "l2Handoff": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "l3Handoff": {
                "items": {
                "properties": {
                "deployPending": {
                "type": [
                "string",
                "null"
                ]
                },
                "displayName": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "remoteIpAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "virtualNetwork": {
                "properties": {
                "idRef": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "externalDomainRoutingProtocol": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
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
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "namespace": {
                "type": [
                "string",
                "null"
                ]
                },
                "networkDeviceId": {
                "type": [
                "string",
                "null"
                ]
                },
                "networkWideSettings": {
                "properties": {
                "aaa": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "cmx": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "deployPending": {
                "type": [
                "string",
                "null"
                ]
                },
                "dhcp": {
                "items": {
                "properties": {
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "ipAddress": {
                "properties": {
                "address": {
                "type": [
                "string",
                "null"
                ]
                },
                "addressType": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "paddedAddress": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "dns": {
                "items": {
                "properties": {
                "domainName": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "ip": {
                "properties": {
                "address": {
                "type": [
                "string",
                "null"
                ]
                },
                "addressType": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "paddedAddress": {
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
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "nativeVlan": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "netflow": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "ntp": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "snmp": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "syslogs": {
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
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "provisioningState": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "targetIdList": {
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
                "items": {
                "properties": {
                "idRef": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "virtualNetwork": {
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "wlan": {
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

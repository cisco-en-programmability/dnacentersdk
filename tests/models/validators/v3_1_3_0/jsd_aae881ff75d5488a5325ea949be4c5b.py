# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetsBorderDeviceDetail data model.

Copyright (c) 2025 Cisco Systems.

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


class JSONSchemaValidatorAae881FF75D5488A5325Ea949Be4C5B(object):
    """GetsBorderDeviceDetail request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorAae881FF75D5488A5325Ea949Be4C5B, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "description":
                 {
                "type": "string"
                },
                "payload": {
                "properties": {
                "akcSettingsCfs": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "authEntityClass": {
                "type": "integer"
                },
                "authEntityId": {
                "type": "integer"
                },
                "cfsChangeInfo": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "configs": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "createTime": {
                "type": "integer"
                },
                "customProvisions": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "deployPending": {
                "type": "string"
                },
                "deployed": {
                "type": "boolean"
                },
                "deviceInterfaceInfo": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "deviceSettings": {
                "properties": {
                "connectedTo": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "cpu": {
                "type": "number"
                },
                "deployPending": {
                "type": "string"
                },
                "dhcpEnabled": {
                "type": "boolean"
                },
                "displayName": {
                "type": "string"
                },
                "extConnectivitySettings": {
                "items": {
                "properties": {
                "deployPending": {
                "type": "string"
                },
                "displayName": {
                "type": "string"
                },
                "externalDomainProtocolNumber": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instanceId": {
                "type": "integer"
                },
                "instanceTenantId": {
                "type": "string"
                },
                "instanceVersion": {
                "type": "integer"
                },
                "interfaceUuid": {
                "type": "string"
                },
                "l2Handoff": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "l3Handoff": {
                "items": {
                "properties": {
                "deployPending": {
                "type": "string"
                },
                "displayName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instanceId": {
                "type": "integer"
                },
                "instanceTenantId": {
                "type": "string"
                },
                "instanceVersion": {
                "type": "number"
                },
                "localIpAddress": {
                "type": "string"
                },
                "remoteIpAddress": {
                "type": "string"
                },
                "virtualNetwork": {
                "properties": {
                "idRef": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "vlanId": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "policyPropagationEnabled": {
                "type": "boolean"
                },
                "policySgtTag": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "externalConnectivityIpPool": {
                "type": "string"
                },
                "externalDomainRoutingProtocol": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instanceId": {
                "type": "integer"
                },
                "instanceTenantId": {
                "type": "string"
                },
                "instanceVersion": {
                "type": "integer"
                },
                "internalDomainProtocolNumber": {
                "type": "string"
                },
                "memory": {
                "type": "number"
                },
                "nodeType": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "storage": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "displayName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "instanceId": {
                "type": "integer"
                },
                "instanceTenantId": {
                "type": "string"
                },
                "instanceVersion": {
                "type": "integer"
                },
                "isSeeded": {
                "type": "boolean"
                },
                "isStale": {
                "type": "boolean"
                },
                "lastUpdateTime": {
                "type": "integer"
                },
                "managedSites": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "name": {
                "type": "string"
                },
                "namespace": {
                "type": "string"
                },
                "networkDeviceId": {
                "type": "string"
                },
                "networkWideSettings": {
                "properties": {
                "aaa": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "cmx": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "deployPending": {
                "type": "string"
                },
                "dhcp": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "ipAddress": {
                "properties": {
                "address": {
                "type": "string"
                },
                "addressType": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "paddedAddress": {
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
                "displayName": {
                "type": "string"
                },
                "dns": {
                "items": {
                "properties": {
                "domainName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "ip": {
                "properties": {
                "address": {
                "type": "string"
                },
                "addressType": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "paddedAddress": {
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
                "id": {
                "type": "string"
                },
                "instanceId": {
                "type": "integer"
                },
                "instanceTenantId": {
                "type": "string"
                },
                "instanceVersion": {
                "type": "integer"
                },
                "ldap": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "nativeVlan": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "netflow": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "ntp": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "snmp": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "syslogs": {
                "items": {
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "otherDevice": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "provisioningState": {
                "type": "string"
                },
                "resourceVersion": {
                "type": "integer"
                },
                "roles": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "saveWanConnectivityDetailsOnly": {
                "type": "boolean"
                },
                "siteId": {
                "type": "string"
                },
                "targetIdList": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "transitNetworks": {
                "items": {
                "properties": {
                "idRef": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "type": {
                "type": "string"
                },
                "virtualNetwork": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "wlan": {
                "items": {
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "status": {
                "type": "string"
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

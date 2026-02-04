# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetConfigurationsForIntendedLayer2FeaturesOnAWiredDevice data model.

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


class JSONSchemaValidatorD96B49E8C1A0594CB4E1946731F06411(object):
    """GetConfigurationsForIntendedLayer2FeaturesOnAWiredDevice request
    schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD96B49E8C1A0594CB4E1946731F06411, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "features": {
                "properties": {
                "cdpGlobalConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "holdTime": {
                "type": "integer"
                },
                "isAdvertiseV2Enabled": {
                "type": "boolean"
                },
                "isCdpEnabled": {
                "type": "boolean"
                },
                "isLogDuplexMismatchEnabled": {
                "type": "boolean"
                },
                "timer": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "cdpInterfaceConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "isCdpEnabled": {
                "type": "boolean"
                },
                "isLogDuplexMismatchEnabled": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "dhcpSnoopingGlobalConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "databaseAgent": {
                "properties": {
                "agentUrl": {
                "type": "string"
                },
                "timeout": {
                "type": "integer"
                },
                "writeDelay": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "isDhcpSnoopingEnabled": {
                "type": "boolean"
                },
                "isGleaningEnabled": {
                "type": "boolean"
                },
                "proxyBridgeVlans": {
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
                "dhcpSnoopingInterfaceConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "isTrustedInterface": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "dot1xGlobalConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "authenticationConfigMode": {
                "type": "string"
                },
                "configType": {
                "type": "string"
                },
                "isDot1xEnabled": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "dot1xInterfaceConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "authenticationMode": {
                "type": "string"
                },
                "authenticationOrder": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "items": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "configType": {
                "type": "string"
                },
                "inactivityTimer": {
                "type": "number"
                },
                "interfaceName": {
                "type": "string"
                },
                "isInactivityTimerFromServerEnabled": {
                "type": "boolean"
                },
                "isReauthEnabled": {
                "type": "boolean"
                },
                "isReauthTimerFromServerEnabled": {
                "type": "boolean"
                },
                "maxReauthRequests": {
                "type": "number"
                },
                "priority": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "items": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "reauthTimer": {
                "type": "number"
                },
                "txPeriod": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "igmpSnoopingGlobalConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "igmpSnoopingVlanSettings": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "igmpSnoopingVlanMrouters": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "interfaceName": {
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
                "isIgmpSnoopingEnabled": {
                "type": "boolean"
                },
                "isImmediateLeaveEnabled": {
                "type": "boolean"
                },
                "isQuerierEnabled": {
                "type": "boolean"
                },
                "querierQueryInterval": {
                "type": "number"
                },
                "vlanId": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "isIgmpSnoopingEnabled": {
                "type": "boolean"
                },
                "isQuerierEnabled": {
                "type": "boolean"
                },
                "querierQueryInterval": {
                "type": "number"
                },
                "querierVersion": {
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
                "lldpGlobalConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "holdTime": {
                "type": "integer"
                },
                "isLldpEnabled": {
                "type": "boolean"
                },
                "reinitializationDelay": {
                "type": "integer"
                },
                "timer": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "lldpInterfaceConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "adminStatus": {
                "type": "string"
                },
                "configType": {
                "type": "string"
                },
                "interfaceName": {
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
                "mabInterfaceConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "isMabEnabled": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "mldSnoopingGlobalConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "isMldSnoopingEnabled": {
                "type": "boolean"
                },
                "isQuerierEnabled": {
                "type": "boolean"
                },
                "mldSnoopingVlanSettings": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "isImmediateLeaveEnabled": {
                "type": "boolean"
                },
                "isMldSnoopingEnabled": {
                "type": "boolean"
                },
                "isQuerierEnabled": {
                "type": "boolean"
                },
                "mldSnoopingVlanMrouters": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "items": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "querierQueryInterval": {
                "type": "number"
                },
                "vlanId": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "querierQueryInterval": {
                "type": "number"
                },
                "querierVersion": {
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
                "portchannelConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "isAutoEnabled": {
                "type": "boolean"
                },
                "lacpSystemPriority": {
                "type": "integer"
                },
                "loadBalancingMethod": {
                "type": "string"
                },
                "portchannels": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "isLayer2": {
                "type": "boolean"
                },
                "memberPorts": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "items": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "stpGlobalConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "isBackboneFastEnabled": {
                "type": "boolean"
                },
                "isBpduFilterEnabled": {
                "type": "boolean"
                },
                "isBpduGuardEnabled": {
                "type": "boolean"
                },
                "isEtherChannelGuardEnabled": {
                "type": "boolean"
                },
                "isExtendedSystemIdEnabled": {
                "type": "boolean"
                },
                "isLoggingEnabled": {
                "type": "boolean"
                },
                "isLoopGuardEnabled": {
                "type": "boolean"
                },
                "isUplinkFastEnabled": {
                "type": "boolean"
                },
                "portFastMode": {
                "type": "string"
                },
                "stpInstances": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "isStpEnabled": {
                "type": "boolean"
                },
                "priority": {
                "type": "integer"
                },
                "vlanId": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "stpMode": {
                "type": "string"
                },
                "transmitHoldCount": {
                "type": "number"
                },
                "uplinkFastMaxUpdateRate": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "stpInterfaceConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "bpduFilter": {
                "type": "string"
                },
                "bpduGuard": {
                "type": "string"
                },
                "configType": {
                "type": "string"
                },
                "guardMode": {
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "pathCost": {
                "type": "number"
                },
                "portVlanCostSettings": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "cost": {
                "type": "integer"
                },
                "vlans": {
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
                "portVlanPrioritySettings": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "priority": {
                "type": "integer"
                },
                "vlans": {
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
                "priority": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "switchportInterfaceConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "accessVlan": {
                "type": "integer"
                },
                "adminStatus": {
                "type": "string"
                },
                "configType": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "mode": {
                "type": "string"
                },
                "nativeVlan": {
                "type": "integer"
                },
                "trunkAllowedVlans": {
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
                "trunkInterfaceConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "isDtpNegotiationEnabled": {
                "type": "boolean"
                },
                "isProtected": {
                "type": "boolean"
                },
                "pruneEligibleVlans": {
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
                "vlanConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "isVlanEnabled": {
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "vlanId": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "vtpGlobalConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "configurationFileName": {
                "type": "string"
                },
                "isPruningEnabled": {
                "type": "boolean"
                },
                "mode": {
                "type": "string"
                },
                "sourceInterface": {
                "type": "string"
                },
                "version": {
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
                "vtpInterfaceConfig": {
                "properties": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "isVtpEnabled": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "version": {
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

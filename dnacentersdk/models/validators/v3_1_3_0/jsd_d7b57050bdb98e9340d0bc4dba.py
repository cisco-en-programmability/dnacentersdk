# -*- coding: utf-8 -*-
"""Cisco DNA Center CreateConfigurationsForAnIntendedLayer2FeatureOnAWiredDevice data model.

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


class JSONSchemaValidatorD7B57050BdB98E9340D0Bc4Dba(object):
    """CreateConfigurationsForAnIntendedLayer2FeatureOnAWiredDevice
    request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorD7B57050BdB98E9340D0Bc4Dba, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "cdpGlobalConfig": {
                "properties": {
                "items": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "CDP_GLOBAL"
                ],
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
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "CDP_INTERFACE"
                ],
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
                "items": {
                "properties": {
                "configType": {
                "enum": [
                ""
                ],
                "type": "string"
                },
                "databaseAgent": {
                "properties": {
                "agentUrl": {
                "type": "string"
                },
                "configType": {
                "enum": [
                "DHCP_SNOOPING_DATABASE_AGENT"
                ],
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
                "dhcpSnoopingVlans": {
                "type": "string"
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
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "DHCP_SNOOPING_INTERFACE"
                ],
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "isTrustedInterface": {
                "type": "boolean"
                },
                "messageRateLimit": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "items": {
                "properties": {
                "authenticationConfigMode": {
                "enum": [
                "LEGACY",
                "NEW_STYLE"
                ],
                "type": "string"
                },
                "configType": {
                "enum": [
                "DOT1X_GLOBAL"
                ],
                "type": "string"
                },
                "isDot1xEnabled": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "items": {
                "properties": {
                "authenticationOrder": {
                "properties": {
                "configType": {
                "enum": [
                "ORDERED_SET"
                ],
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
                "enum": [
                "DOT1X_INTERFACE"
                ],
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "IGMP_SNOOPING_GLOBAL"
                ],
                "type": "string"
                },
                "igmpSnoopingVlanSettings": {
                "properties": {
                "configType": {
                "enum": [
                "SET"
                ],
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "IGMP_SNOOPING_VLAN"
                ],
                "type": "string"
                },
                "igmpSnoopingVlanMrouters": {
                "properties": {
                "configType": {
                "enum": [
                "SET"
                ],
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "IGMP_SNOOPING_VLAN_MROUTER"
                ],
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
                "querierAddress": {
                "type": "string"
                },
                "querierQueryInterval": {
                "type": "integer"
                },
                "querierVersion": {
                "enum": [
                "VERSION_1",
                "VERSION_2",
                "VERSION_3"
                ],
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
                "isIgmpSnoopingEnabled": {
                "type": "boolean"
                },
                "isQuerierEnabled": {
                "type": "boolean"
                },
                "querierAddress": {
                "type": "string"
                },
                "querierQueryInterval": {
                "type": "integer"
                },
                "querierVersion": {
                "enum": [
                "VERSION_1",
                "VERSION_2",
                "VERSION_3"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "LLDP_GLOBAL"
                ],
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
                "items": {
                "properties": {
                "adminStatus": {
                "enum": [
                "TRANSMIT_ONLY",
                "RECEIVE_ONLY",
                "TRANSMIT_AND_RECEIVE",
                "DISABLED"
                ],
                "type": "string"
                },
                "configType": {
                "enum": [
                "LLDP_INTERFACE"
                ],
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "MAB_INTERFACE"
                ],
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
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "MLD_SNOOPING_GLOBAL"
                ],
                "type": "string"
                },
                "isMldSnoopingEnabled": {
                "type": "boolean"
                },
                "isQuerierEnabled": {
                "type": "boolean"
                },
                "isSuppressListenerMessagesEnabled": {
                "type": "boolean"
                },
                "mldSnoopingVlanSettings": {
                "properties": {
                "configType": {
                "enum": [
                "SET"
                ],
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "MLD_SNOOPING_VLAN"
                ],
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
                "enum": [
                "SET"
                ],
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "MLD_SNOOPING_VLAN_MROUTER"
                ],
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
                "querierAddress": {
                "type": "string"
                },
                "querierQueryInterval": {
                "type": "integer"
                },
                "querierVersion": {
                "enum": [
                "VERSION_1",
                "VERSION_2"
                ],
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
                "querierAddress": {
                "type": "string"
                },
                "querierQueryInterval": {
                "type": "integer"
                },
                "querierVersion": {
                "enum": [
                "VERSION_1",
                "VERSION_2"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "portChannelConfig": {
                "properties": {
                "items": {
                "items": {
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "PORTCHANNEL"
                ],
                "type": "string"
                },
                "isAutoEnabled": {
                "type": "boolean"
                },
                "lacpSystemPriority": {
                "type": "integer"
                },
                "loadBalancingMethod": {
                "enum": [
                "SRC_MAC",
                "DST_MAC",
                "SRC_DST_MAC",
                "SRC_IP",
                "DST_IP",
                "SRC_DST_IP",
                "SRC_PORT",
                "DST_PORT",
                "SRC_DST_PORT",
                "SRC_DST_MIXED_IP_PORT",
                "SRC_MIXED_IP_PORT",
                "DST_MIXED_IP_PORT",
                "VLAN_SRC_IP",
                "VLAN_DST_IP",
                "VLAN_SRC_DST_IP",
                "VLAN_SRC_MIXED_IP_PORT",
                "VLAN_DST_MIXED_IP_PORT",
                "VLAN_SRC_DST_MIXED_IP_PORT"
                ],
                "type": "string"
                },
                "portchannels": {
                "properties": {
                "configType": {
                "enum": [
                "SET"
                ],
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "AnyOf": {
                "properties": {
                "EtherchannelConfig": {
                "properties": {
                "configType": {
                "enum": [
                "ETHERCHANNEL_CONFIG"
                ],
                "type": "string"
                },
                "memberPorts": {
                "properties": {
                "configType": {
                "enum": [
                "SET"
                ],
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "ETHERCHANNEL_MEMBER_PORT_CONFIG"
                ],
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "mode": {
                "enum": [
                "ON"
                ],
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
                "minLinks": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "LacpPortchannelConfig": {
                "properties": {
                "configType": {
                "enum": [
                "LACP_PORTCHANNEL_CONFIG"
                ],
                "type": "string"
                },
                "memberPorts": {
                "properties": {
                "configType": {
                "enum": [
                "SET"
                ],
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "LACP_PORTCHANNEL_MEMBER_PORT_CONFIG"
                ],
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "mode": {
                "enum": [
                "ACTIVE",
                "PASSIVE"
                ],
                "type": "string"
                },
                "portPriority": {
                "type": "integer"
                },
                "rate": {
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
                "minLinks": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "PagpPortchannelConfig": {
                "properties": {
                "configType": {
                "enum": [
                "PAGP_PORTCHANNEL_CONFIG"
                ],
                "type": "string"
                },
                "memberPorts": {
                "properties": {
                "configType": {
                "enum": [
                "SET"
                ],
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "PAGP_PORTCHANNEL_MEMBER_PORT_CONFIG"
                ],
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "learnMethod": {
                "enum": [
                "AGGREGATION_PORT",
                "PHYSICAL_PORT"
                ],
                "type": "string"
                },
                "mode": {
                "enum": [
                "AUTO",
                "AUTO_NON_SILENT",
                "DESIRABLE",
                "DESIRABLE_NON_SILENT"
                ],
                "type": "string"
                },
                "portPriority": {
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
                "minLinks": {
                "type": "integer"
                },
                "name": {
                "type": "string"
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
                "type": "array"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "STP_GLOBAL"
                ],
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
                "enum": [
                "ENABLE",
                "DISABLE",
                "EDGE",
                "NETWORK"
                ],
                "type": "string"
                },
                "stpInstances": {
                "properties": {
                "configType": {
                "enum": [
                "LIST"
                ],
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "STP_VLAN"
                ],
                "type": "string"
                },
                "priority": {
                "type": "integer"
                },
                "timers": {
                "properties": {
                "configType": {
                "enum": [
                "STP_TIMERS"
                ],
                "type": "string"
                },
                "forwardDelay": {
                "type": "integer"
                },
                "helloInterval": {
                "type": "integer"
                },
                "isStpEnabled": {
                "type": "boolean"
                },
                "maxAge": {
                "type": "integer"
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
                }
                },
                "type": "object"
                },
                "stpMode": {
                "enum": [
                "PVST",
                "RSTP",
                "MST"
                ],
                "type": "string"
                },
                "transmitHoldCount": {
                "type": "integer"
                },
                "uplinkFastMaxUpdateRate": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "enum": [
                "ENABLE",
                "DISABLE",
                "NONE"
                ],
                "type": "string"
                },
                "bpduGuard": {
                "enum": [
                "ENABLE",
                "DISABLE",
                "NONE"
                ],
                "type": "string"
                },
                "configType": {
                "enum": [
                "STP_INTERFACE"
                ],
                "type": "string"
                },
                "guardMode": {
                "enum": [
                "LOOP",
                "ROOT",
                "NONE"
                ],
                "type": "string"
                },
                "interfaceName": {
                "type": "string"
                },
                "pathCost": {
                "type": "integer"
                },
                "portFastMode": {
                "enum": [
                "NONE",
                "DISABLE",
                "EDGE",
                "EDGE_TRUNK",
                "NETWORK",
                "TRUNK"
                ],
                "type": "string"
                },
                "portVlanCostSettings": {
                "properties": {
                "configType": {
                "enum": [
                "LIST"
                ],
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "STP_INTERFACE_VLAN_COST"
                ],
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
                "enum": [
                "LIST"
                ],
                "type": "string"
                },
                "items": {
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "STP_INTERFACE_VLAN_PRIORITY"
                ],
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
                "items": {
                "properties": {
                "accessVlan": {
                "type": "integer"
                },
                "adminStatus": {
                "enum": [
                "UP",
                "DOWN"
                ],
                "type": "string"
                },
                "configType": {
                "enum": [
                "SWITCHPORT_INTERFACE"
                ],
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
                "enum": [
                "ACCESS",
                "TRUNK",
                "DYNAMIC_AUTO",
                "DYNAMIC_DESIRABLE",
                "DOT1Q_TUNNEL"
                ],
                "type": "string"
                },
                "nativeVlan": {
                "type": "integer"
                },
                "trunkAllowedVlans": {
                "type": "string"
                },
                "voiceVlan": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "TRUNK_INTERFACE"
                ],
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
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "VLAN"
                ],
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
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "VTP_GLOBAL"
                ],
                "type": "string"
                },
                "configurationFileName": {
                "type": "string"
                },
                "domainName": {
                "type": "string"
                },
                "isPruningEnabled": {
                "type": "boolean"
                },
                "mode": {
                "enum": [
                "SERVER",
                "CLIENT",
                "TRANSPARENT",
                "OFF"
                ],
                "type": "string"
                },
                "sourceInterface": {
                "type": "string"
                },
                "version": {
                "enum": [
                "VERSION_1",
                "VERSION_2",
                "VERSION_3"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "items": {
                "properties": {
                "configType": {
                "enum": [
                "VTP_INTERFACE"
                ],
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
                },
                "type": "array"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                }""".replace(
                    "\n" + " " * 16, ""
                )
            )
        )

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                "{} is invalid. Reason: {}".format(request, e.message)
            )

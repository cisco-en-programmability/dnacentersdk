# -*- coding: utf-8 -*-
"""DNA Center Update Device data model.

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


class JSONSchemaValidator09B0F9Ce4239Ae10(object):
    """Update Device request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator09B0F9Ce4239Ae10, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "_id": {
                "description":
                " Id",
                "type": [
                "string",
                "null"
                ]
                },
                "dayZeroConfig": {
                "description":
                "Day Zero Config",
                "properties": {
                "config": {
                "description":
                "Config",
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
                "dayZeroConfigPreview": {
                "description":
                "Day Zero Config Preview",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "deviceInfo": {
                "description":
                "Device Info",
                "properties": {
                "aaaCredentials": {
                "description":
                "Aaa Credentials",
                "properties": {
                "password": {
                "description":
                "Password",
                "type": [
                "string",
                "null"
                ]
                },
                "username": {
                "description":
                "Username",
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
                "addedOn": {
                "type": [
                "number",
                "null"
                ]
                },
                "addnMacAddrs": {
                "description":
                "Addn Mac Addrs",
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
                "agentType": {
                "description":
                "Agent Type",
                "type": [
                "string",
                "null"
                ]
                },
                "authStatus": {
                "description":
                "Auth Status",
                "type": [
                "string",
                "null"
                ]
                },
                "authenticatedMicNumber": {
                "description":
                "Authenticated Mic Number",
                "type": [
                "string",
                "null"
                ]
                },
                "authenticatedSudiSerialNo": {
                "description":
                "Authenticated Sudi Serial No",
                "type": [
                "string",
                "null"
                ]
                },
                "capabilitiesSupported": {
                "description":
                "Capabilities Supported",
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
                "cmState": {
                "description":
                "Cm State",
                "type": [
                "string",
                "null"
                ]
                },
                "description":
                 {
                "description":
                "Description",
                "type": [
                "string",
                "null"
                ]
                },
                "deviceSudiSerialNos": {
                "description":
                "Device Sudi Serial Nos",
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
                "deviceType": {
                "description":
                "Device Type",
                "type": [
                "string",
                "null"
                ]
                },
                "featuresSupported": {
                "description":
                "Features Supported",
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
                "fileSystemList": {
                "description":
                "File System List",
                "items": {
                "properties": {
                "freespace": {
                "type": [
                "number",
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
                "readable": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "size": {
                "type": [
                "number",
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
                "writeable": {
                "type": [
                "boolean",
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
                "firstContact": {
                "type": [
                "number",
                "null"
                ]
                },
                "hostname": {
                "description":
                "Hostname",
                "type": [
                "string",
                "null"
                ]
                },
                "httpHeaders": {
                "description":
                "Http Headers",
                "items": {
                "properties": {
                "key": {
                "description":
                "Key",
                "type": [
                "string",
                "null"
                ]
                },
                "value": {
                "description":
                "Value",
                "type": [
                "string",
                "null",
                "number"
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
                "imageFile": {
                "description":
                "Image File",
                "type": [
                "string",
                "null"
                ]
                },
                "imageVersion": {
                "description":
                "Image Version",
                "type": [
                "string",
                "null"
                ]
                },
                "ipInterfaces": {
                "description":
                "Ip Interfaces",
                "items": {
                "properties": {
                "ipv4Address": {
                "description":
                "Ipv4 Address",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "ipv6AddressList": {
                "description":
                "Ipv6 Address List",
                "items": {
                "properties": {},
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
                "macAddress": {
                "description":
                "Mac Address",
                "type": [
                "string",
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
                "status": {
                "description":
                "Status",
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
                "lastContact": {
                "type": [
                "number",
                "null"
                ]
                },
                "lastSyncTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "lastUpdateOn": {
                "type": [
                "number",
                "null"
                ]
                },
                "location": {
                "description":
                "Location",
                "properties": {
                "address": {
                "description":
                "Address",
                "type": [
                "string",
                "null"
                ]
                },
                "altitude": {
                "description":
                "Altitude",
                "type": [
                "string",
                "null"
                ]
                },
                "latitude": {
                "description":
                "Latitude",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "longitude": {
                "description":
                "Longitude",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "siteId": {
                "description":
                "Site Id",
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
                "macAddress": {
                "description":
                "Mac Address",
                "type": [
                "string",
                "null"
                ]
                },
                "mode": {
                "description":
                "Mode",
                "type": [
                "string",
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
                "neighborLinks": {
                "description":
                "Neighbor Links",
                "items": {
                "properties": {
                "localInterfaceName": {
                "description":
                "Local Interface Name",
                "type": [
                "string",
                "null"
                ]
                },
                "localMacAddress": {
                "description":
                "Local Mac Address",
                "type": [
                "string",
                "null"
                ]
                },
                "localShortInterfaceName": {
                "description":
                "Local Short Interface Name",
                "type": [
                "string",
                "null"
                ]
                },
                "remoteDeviceName": {
                "description":
                "Remote Device Name",
                "type": [
                "string",
                "null"
                ]
                },
                "remoteInterfaceName": {
                "description":
                "Remote Interface Name",
                "type": [
                "string",
                "null"
                ]
                },
                "remoteMacAddress": {
                "description":
                "Remote Mac Address",
                "type": [
                "string",
                "null"
                ]
                },
                "remotePlatform": {
                "description":
                "Remote Platform",
                "type": [
                "string",
                "null"
                ]
                },
                "remoteShortInterfaceName": {
                "description":
                "Remote Short Interface Name",
                "type": [
                "string",
                "null"
                ]
                },
                "remoteVersion": {
                "description":
                "Remote Version",
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
                "onbState": {
                "description":
                "Onb State",
                "type": [
                "string",
                "null"
                ]
                },
                "pid": {
                "description":
                "Pid",
                "type": [
                "string",
                "null"
                ]
                },
                "pnpProfileList": {
                "description":
                "Pnp Profile List",
                "items": {
                "properties": {
                "createdBy": {
                "description":
                "Created By",
                "type": [
                "string",
                "null"
                ]
                },
                "discoveryCreated": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "primaryEndpoint": {
                "description":
                "Primary Endpoint",
                "properties": {
                "certificate": {
                "description":
                "Certificate",
                "type": [
                "string",
                "null"
                ]
                },
                "fqdn": {
                "description":
                "Fqdn",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4Address": {
                "description":
                "Ipv4 Address",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "ipv6Address": {
                "description":
                "Ipv6 Address",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "port": {
                "type": [
                "number",
                "null"
                ]
                },
                "protocol": {
                "description":
                "Protocol",
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
                "profileName": {
                "description":
                "Profile Name",
                "type": [
                "string",
                "null"
                ]
                },
                "secondaryEndpoint": {
                "description":
                "Secondary Endpoint",
                "properties": {
                "certificate": {
                "description":
                "Certificate",
                "type": [
                "string",
                "null"
                ]
                },
                "fqdn": {
                "description":
                "Fqdn",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4Address": {
                "description":
                "Ipv4 Address",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "ipv6Address": {
                "description":
                "Ipv6 Address",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "port": {
                "type": [
                "number",
                "null"
                ]
                },
                "protocol": {
                "description":
                "Protocol",
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
                "populateInventory": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "preWorkflowCliOuputs": {
                "description":
                "Pre Workflow Cli Ouputs",
                "items": {
                "properties": {
                "cli": {
                "description":
                "Cli",
                "type": [
                "string",
                "null"
                ]
                },
                "cliOutput": {
                "description":
                "Cli Output",
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
                "projectId": {
                "description":
                "Project Id",
                "type": [
                "string",
                "null"
                ]
                },
                "projectName": {
                "description":
                "Project Name",
                "type": [
                "string",
                "null"
                ]
                },
                "reloadRequested": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "serialNumber": {
                "description":
                "Serial Number",
                "type": [
                "string",
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
                "siteName": {
                "description":
                "Site Name",
                "type": [
                "string",
                "null"
                ]
                },
                "smartAccountId": {
                "description":
                "Smart Account Id",
                "type": [
                "string",
                "null"
                ]
                },
                "source": {
                "description":
                "Source",
                "type": [
                "string",
                "null"
                ]
                },
                "stack": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "stackInfo": {
                "description":
                "Stack Info",
                "properties": {
                "isFullRing": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "stackMemberList": {
                "description":
                "Stack Member List",
                "items": {
                "properties": {
                "hardwareVersion": {
                "description":
                "Hardware Version",
                "type": [
                "string",
                "null"
                ]
                },
                "licenseLevel": {
                "description":
                "License Level",
                "type": [
                "string",
                "null"
                ]
                },
                "licenseType": {
                "description":
                "License Type",
                "type": [
                "string",
                "null"
                ]
                },
                "macAddress": {
                "description":
                "Mac Address",
                "type": [
                "string",
                "null"
                ]
                },
                "pid": {
                "description":
                "Pid",
                "type": [
                "string",
                "null"
                ]
                },
                "priority": {
                "type": [
                "number",
                "null"
                ]
                },
                "role": {
                "description":
                "Role",
                "type": [
                "string",
                "null"
                ]
                },
                "serialNumber": {
                "description":
                "Serial Number",
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "description":
                "Software Version",
                "type": [
                "string",
                "null"
                ]
                },
                "stackNumber": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "sudiSerialNumber": {
                "description":
                "Sudi Serial Number",
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
                "stackRingProtocol": {
                "description":
                "Stack Ring Protocol",
                "type": [
                "string",
                "null"
                ]
                },
                "supportsStackWorkflows": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "totalMemberCount": {
                "type": [
                "number",
                "null"
                ]
                },
                "validLicenseLevels": {
                "description":
                "Valid License Levels",
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "sudiRequired": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "tags": {
                "description":
                "Tags",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "userMicNumbers": {
                "description":
                "User Mic Numbers",
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
                "userSudiSerialNos": {
                "description":
                "User Sudi Serial Nos",
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
                "virtualAccountId": {
                "description":
                "Virtual Account Id",
                "type": [
                "string",
                "null"
                ]
                },
                "workflowId": {
                "description":
                "Workflow Id",
                "type": [
                "string",
                "null"
                ]
                },
                "workflowName": {
                "description":
                "Workflow Name",
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
                "runSummaryList": {
                "description":
                "Run Summary List",
                "items": {
                "properties": {
                "details": {
                "description":
                "Details",
                "type": [
                "string",
                "null"
                ]
                },
                "errorFlag": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "historyTaskInfo": {
                "description":
                "History Task Info",
                "properties": {
                "addnDetails": {
                "description":
                "Addn Details",
                "items": {
                "properties": {
                "key": {
                "description":
                "Key",
                "type": [
                "string",
                "null"
                ]
                },
                "value": {
                "description":
                "Value",
                "type": [
                "string",
                "null",
                "number"
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
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "timeTaken": {
                "type": [
                "number",
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
                "workItemList": {
                "description":
                "Work Item List",
                "items": {
                "properties": {
                "command": {
                "description":
                "Command",
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputStr": {
                "description":
                "Output Str",
                "type": [
                "string",
                "null"
                ]
                },
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "timeTaken": {
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
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "timestamp": {
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
                "systemResetWorkflow": {
                "description":
                "System Reset Workflow",
                "properties": {
                "_id": {
                "description":
                " Id",
                "type": [
                "string",
                "null"
                ]
                },
                "addToInventory": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "addedOn": {
                "type": [
                "number",
                "null"
                ]
                },
                "configId": {
                "description":
                "Config Id",
                "type": [
                "string",
                "null"
                ]
                },
                "currTaskIdx": {
                "type": [
                "number",
                "null"
                ]
                },
                "description":
                 {
                "description":
                "Description",
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "execTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "imageId": {
                "description":
                "Image Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceType": {
                "description":
                "Instance Type",
                "type": [
                "string",
                "null"
                ]
                },
                "lastupdateOn": {
                "type": [
                "number",
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
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "tasks": {
                "description":
                "Tasks",
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": [
                "number",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
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
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "taskSeqNo": {
                "type": [
                "number",
                "null"
                ]
                },
                "timeTaken": {
                "type": [
                "number",
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
                "workItemList": {
                "description":
                "Work Item List",
                "items": {
                "properties": {
                "command": {
                "description":
                "Command",
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputStr": {
                "description":
                "Output Str",
                "type": [
                "string",
                "null"
                ]
                },
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "timeTaken": {
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
                "tenantId": {
                "description":
                "Tenant Id",
                "type": [
                "string",
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
                "useState": {
                "description":
                "Use State",
                "type": [
                "string",
                "null"
                ]
                },
                "version": {
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
                "systemWorkflow": {
                "description":
                "System Workflow",
                "properties": {
                "_id": {
                "description":
                " Id",
                "type": [
                "string",
                "null"
                ]
                },
                "addToInventory": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "addedOn": {
                "type": [
                "number",
                "null"
                ]
                },
                "configId": {
                "description":
                "Config Id",
                "type": [
                "string",
                "null"
                ]
                },
                "currTaskIdx": {
                "type": [
                "number",
                "null"
                ]
                },
                "description":
                 {
                "description":
                "Description",
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "execTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "imageId": {
                "description":
                "Image Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceType": {
                "description":
                "Instance Type",
                "type": [
                "string",
                "null"
                ]
                },
                "lastupdateOn": {
                "type": [
                "number",
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
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "tasks": {
                "description":
                "Tasks",
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": [
                "number",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
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
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "taskSeqNo": {
                "type": [
                "number",
                "null"
                ]
                },
                "timeTaken": {
                "type": [
                "number",
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
                "workItemList": {
                "description":
                "Work Item List",
                "items": {
                "properties": {
                "command": {
                "description":
                "Command",
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputStr": {
                "description":
                "Output Str",
                "type": [
                "string",
                "null"
                ]
                },
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "timeTaken": {
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
                "tenantId": {
                "description":
                "Tenant Id",
                "type": [
                "string",
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
                "useState": {
                "description":
                "Use State",
                "type": [
                "string",
                "null"
                ]
                },
                "version": {
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
                "tenantId": {
                "description":
                "Tenant Id",
                "type": [
                "string",
                "null"
                ]
                },
                "version": {
                "type": [
                "number",
                "null"
                ]
                },
                "workflow": {
                "description":
                "Workflow",
                "properties": {
                "_id": {
                "description":
                " Id",
                "type": [
                "string",
                "null"
                ]
                },
                "addToInventory": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "addedOn": {
                "type": [
                "number",
                "null"
                ]
                },
                "configId": {
                "description":
                "Config Id",
                "type": [
                "string",
                "null"
                ]
                },
                "currTaskIdx": {
                "type": [
                "number",
                "null"
                ]
                },
                "description":
                 {
                "description":
                "Description",
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "execTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "imageId": {
                "description":
                "Image Id",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceType": {
                "description":
                "Instance Type",
                "type": [
                "string",
                "null"
                ]
                },
                "lastupdateOn": {
                "type": [
                "number",
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
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "tasks": {
                "description":
                "Tasks",
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": [
                "number",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
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
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "taskSeqNo": {
                "type": [
                "number",
                "null"
                ]
                },
                "timeTaken": {
                "type": [
                "number",
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
                "workItemList": {
                "description":
                "Work Item List",
                "items": {
                "properties": {
                "command": {
                "description":
                "Command",
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputStr": {
                "description":
                "Output Str",
                "type": [
                "string",
                "null"
                ]
                },
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "description":
                "State",
                "type": [
                "string",
                "null"
                ]
                },
                "timeTaken": {
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
                "tenantId": {
                "description":
                "Tenant Id",
                "type": [
                "string",
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
                "useState": {
                "description":
                "Use State",
                "type": [
                "string",
                "null"
                ]
                },
                "version": {
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
                "workflowParameters": {
                "description":
                "Workflow Parameters",
                "properties": {
                "configList": {
                "description":
                "Config List",
                "items": {
                "properties": {
                "configId": {
                "description":
                "Config Id",
                "type": [
                "string",
                "null"
                ]
                },
                "configParameters": {
                "description":
                "Config Parameters",
                "items": {
                "properties": {
                "key": {
                "description":
                "Key",
                "type": [
                "string",
                "null"
                ]
                },
                "value": {
                "description":
                "Value",
                "type": [
                "string",
                "null",
                "number"
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
                "licenseLevel": {
                "description":
                "License Level",
                "type": [
                "string",
                "null"
                ]
                },
                "licenseType": {
                "description":
                "License Type",
                "type": [
                "string",
                "null"
                ]
                },
                "topOfStackSerialNumber": {
                "description":
                "Top Of Stack Serial Number",
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

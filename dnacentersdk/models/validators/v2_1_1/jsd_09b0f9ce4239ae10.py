# -*- coding: utf-8 -*-
"""DNA Center Update Device data model.

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


class JSONSchemaValidator09B0F9Ce4239Ae10(object):
    """Update Device request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator09B0F9Ce4239Ae10, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "_id": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "deviceInfo": {
                "properties": {
                "aaaCredentials": {
                "properties": {
                "password": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "username": {
                "description":
                 "",
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
                 "",
                "enum": [
                "POSIX",
                "IOS",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "authStatus": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "authenticatedSudiSerialNo": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "capabilitiesSupported": {
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
                 "",
                "enum": [
                "NotContacted",
                "Contacted",
                "Disconnected",
                "SecuringConnection",
                "SecuredConnection",
                "Authenticated",
                "ErrorSecuringConnection",
                "ErrorAuthenticating",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "description":
                 {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "deviceSudiSerialNos": {
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "featuresSupported": {
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
                 "",
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "httpHeaders": {
                "items": {
                "properties": {
                "key": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "value": {
                "description":
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "imageVersion": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ipInterfaces": {
                "items": {
                "properties": {
                "ipv4Address": {},
                "ipv6AddressList": {
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
                "macAddress": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "status": {
                "description":
                 "",
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
                "properties": {
                "address": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "altitude": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "latitude": {
                "description":
                 "",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "longitude": {
                "description":
                 "",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "siteId": {
                "description":
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "mode": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "neighborLinks": {
                "items": {
                "properties": {
                "localInterfaceName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "localMacAddress": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "localShortInterfaceName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "remoteDeviceName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "remoteInterfaceName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "remoteMacAddress": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "remotePlatform": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "remoteShortInterfaceName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "remoteVersion": {
                "description":
                 "",
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
                 "",
                "enum": [
                "NotContacted",
                "Connecting",
                "ErrorSecuringConnection",
                "ErrorAuthenticating",
                "Initializing",
                "Initialized",
                "ErrorInitializing",
                "SudiAuthorizing",
                "ErrorSudiAuthorizing",
                "ExecutingWorkflow",
                "ExecutedWorkflow",
                "ErrorExecutingWorkflow",
                "ExecutingReset",
                "ErrorExecutingReset",
                "Provisioned",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "pid": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "pnpProfileList": {
                "items": {
                "properties": {
                "createdBy": {
                "description":
                 "",
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
                "properties": {
                "certificate": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "fqdn": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4Address": {},
                "ipv6Address": {},
                "port": {
                "type": [
                "number",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "secondaryEndpoint": {
                "properties": {
                "certificate": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "fqdn": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "ipv4Address": {},
                "ipv6Address": {},
                "port": {
                "type": [
                "number",
                "null"
                ]
                },
                "protocol": {
                "description":
                 "",
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
                "items": {
                "properties": {
                "cli": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "cliOutput": {
                "description":
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "projectName": {
                "description":
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "smartAccountId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "source": {
                "description":
                 "",
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
                "properties": {
                "isFullRing": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "stackMemberList": {
                "items": {
                "properties": {
                "hardwareVersion": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "licenseLevel": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "licenseType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "macAddress": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "pid": {
                "description":
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "serialNumber": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "description":
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "sudiSerialNumber": {
                "description":
                 "",
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
                 "",
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
                 "",
                "enum": [
                "Unclaimed",
                "Planned",
                "Onboarding",
                "Provisioned",
                "Error",
                "Deleted",
                null
                ],
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
                "tags": {},
                "userSudiSerialNos": {
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "workflowId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "workflowName": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                }
                },
                "type": [
                "object"
                ]
                },
                "runSummaryList": {
                "items": {
                "properties": {
                "details": {
                "description":
                 "",
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
                "properties": {
                "addnDetails": {
                "items": {
                "properties": {
                "key": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "value": {
                "description":
                 "",
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
                "description":
                 "",
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
                 "",
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
                 "",
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
                "properties": {
                "_id": {
                "description":
                 "",
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
                 "",
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceType": {
                "description":
                 "",
                "enum": [
                "SystemWorkflow",
                "UserWorkflow",
                "SystemResetWorkflow",
                null
                ],
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "tasks": {
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
                 "",
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
                "description":
                 "",
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
                 "",
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "useState": {
                "description":
                 "",
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
                "properties": {
                "_id": {
                "description":
                 "",
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
                 "",
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceType": {
                "description":
                 "",
                "enum": [
                "SystemWorkflow",
                "UserWorkflow",
                "SystemResetWorkflow",
                null
                ],
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "tasks": {
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
                 "",
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
                "description":
                 "",
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
                 "",
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "useState": {
                "description":
                 "",
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
                 "",
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
                "properties": {
                "_id": {
                "description":
                 "",
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
                 "",
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "instanceType": {
                "description":
                 "",
                "enum": [
                "SystemWorkflow",
                "UserWorkflow",
                "SystemResetWorkflow",
                null
                ],
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "tasks": {
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
                 "",
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
                "description":
                 "",
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
                 "",
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
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "useState": {
                "description":
                 "",
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
                "properties": {
                "configList": {
                "items": {
                "properties": {
                "configId": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "configParameters": {
                "items": {
                "properties": {
                "key": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "value": {
                "description":
                 "",
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
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "licenseType": {
                "description":
                 "",
                "type": [
                "string",
                "null"
                ]
                },
                "topOfStackSerialNumber": {
                "description":
                 "",
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
                "required": [
                "deviceInfo"
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

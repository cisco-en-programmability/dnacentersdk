# -*- coding: utf-8 -*-
"""Cisco DNA Center Update Device data model.

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


class JSONSchemaValidator09B0F9Ce4239Ae10(object):
    """Update Device request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator09B0F9Ce4239Ae10, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "_id": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "username": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "authenticatedSudiSerialNo": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "httpHeaders": {
                "items": {
                "properties": {
                "key": {
                "type": [
                "string",
                "null"
                ]
                },
                "value": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "imageVersion": {
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
                "status": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "altitude": {
                "type": [
                "string",
                "null"
                ]
                },
                "latitude": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "longitude": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "siteId": {
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
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "neighborLinks": {
                "items": {
                "properties": {
                "localInterfaceName": {
                "type": [
                "string",
                "null"
                ]
                },
                "localMacAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "localShortInterfaceName": {
                "type": [
                "string",
                "null"
                ]
                },
                "remoteDeviceName": {
                "type": [
                "string",
                "null"
                ]
                },
                "remoteInterfaceName": {
                "type": [
                "string",
                "null"
                ]
                },
                "remoteMacAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "remotePlatform": {
                "type": [
                "string",
                "null"
                ]
                },
                "remoteShortInterfaceName": {
                "type": [
                "string",
                "null"
                ]
                },
                "remoteVersion": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "pnpProfileList": {
                "items": {
                "properties": {
                "createdBy": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "fqdn": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "secondaryEndpoint": {
                "properties": {
                "certificate": {
                "type": [
                "string",
                "null"
                ]
                },
                "fqdn": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "cliOutput": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "projectName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "smartAccountId": {
                "type": [
                "string",
                "null"
                ]
                },
                "source": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "licenseLevel": {
                "type": [
                "string",
                "null"
                ]
                },
                "licenseType": {
                "type": [
                "string",
                "null"
                ]
                },
                "macAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "pid": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "serialNumber": {
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "sudiSerialNumber": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "workflowId": {
                "type": [
                "string",
                "null"
                ]
                },
                "workflowName": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "value": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "instanceType": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
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
                },
                "useState": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "instanceType": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
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
                },
                "useState": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "instanceType": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
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
                },
                "useState": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "configParameters": {
                "items": {
                "properties": {
                "key": {
                "type": [
                "string",
                "null"
                ]
                },
                "value": {
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
                "type": [
                "string",
                "null"
                ]
                },
                "licenseType": {
                "type": [
                "string",
                "null"
                ]
                },
                "topOfStackSerialNumber": {
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

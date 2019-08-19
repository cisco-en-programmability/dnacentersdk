# -*- coding: utf-8 -*-
"""DNA Center Add Device data model.

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


class JSONSchemaValidatorF3B26B5544CaBab9(object):
    """Add Device request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF3B26B5544CaBab9, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "_id": {
                "description":
                 "",
                "type": "string"
                },
                "deviceInfo": {
                "description":
                 "",
                "properties": {
                "aaaCredentials": {
                "description":
                 "",
                "properties": {
                "password": {
                "description":
                 "",
                "type": "string"
                },
                "username": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "addedOn": {
                "type": "number"
                },
                "addnMacAddrs": {
                "description":
                 "",
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "agentType": {
                "description":
                 "",
                "enum": [
                "POSIX",
                "IOS"
                ],
                "type": "string"
                },
                "authStatus": {
                "description":
                 "",
                "type": "string"
                },
                "authenticatedSudiSerialNo": {
                "description":
                 "",
                "type": "string"
                },
                "capabilitiesSupported": {
                "description":
                 "",
                "items": {
                "type": "string"
                },
                "type": "array"
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
                "ErrorAuthenticating"
                ],
                "type": "string"
                },
                "description":
                 {
                "description":
                 "",
                "type": "string"
                },
                "deviceSudiSerialNos": {
                "description":
                 "",
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "deviceType": {
                "description":
                 "",
                "type": "string"
                },
                "featuresSupported": {
                "description":
                 "",
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "fileSystemList": {
                "description":
                 "",
                "items": {
                "properties": {
                "freespace": {
                "type": "number"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "readable": {
                "type": "boolean"
                },
                "size": {
                "type": "number"
                },
                "type": {
                "description":
                 "",
                "type": "string"
                },
                "writeable": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "firstContact": {
                "type": "number"
                },
                "hostname": {
                "description":
                 "",
                "type": "string"
                },
                "httpHeaders": {
                "description":
                 "",
                "items": {
                "properties": {
                "key": {
                "description":
                 "",
                "type": "string"
                },
                "value": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "imageFile": {
                "description":
                 "",
                "type": "string"
                },
                "imageVersion": {
                "description":
                 "",
                "type": "string"
                },
                "ipInterfaces": {
                "description":
                 "",
                "items": {
                "properties": {
                "ipv4Address": {},
                "ipv6AddressList": {
                "description":
                 "",
                "items": {},
                "type": "array"
                },
                "macAddress": {
                "description":
                 "",
                "type": "string"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "status": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "lastContact": {
                "type": "number"
                },
                "lastSyncTime": {
                "type": "number"
                },
                "lastUpdateOn": {
                "type": "number"
                },
                "location": {
                "description":
                 "",
                "properties": {
                "address": {
                "description":
                 "",
                "type": "string"
                },
                "altitude": {
                "description":
                 "",
                "type": "string"
                },
                "latitude": {
                "description":
                 "",
                "type": "string"
                },
                "longitude": {
                "description":
                 "",
                "type": "string"
                },
                "siteId": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "macAddress": {
                "description":
                 "",
                "type": "string"
                },
                "mode": {
                "description":
                 "",
                "type": "string"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "neighborLinks": {
                "description":
                 "",
                "items": {
                "properties": {
                "localInterfaceName": {
                "description":
                 "",
                "type": "string"
                },
                "localMacAddress": {
                "description":
                 "",
                "type": "string"
                },
                "localShortInterfaceName": {
                "description":
                 "",
                "type": "string"
                },
                "remoteDeviceName": {
                "description":
                 "",
                "type": "string"
                },
                "remoteInterfaceName": {
                "description":
                 "",
                "type": "string"
                },
                "remoteMacAddress": {
                "description":
                 "",
                "type": "string"
                },
                "remotePlatform": {
                "description":
                 "",
                "type": "string"
                },
                "remoteShortInterfaceName": {
                "description":
                 "",
                "type": "string"
                },
                "remoteVersion": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "Provisioned"
                ],
                "type": "string"
                },
                "pid": {
                "description":
                 "",
                "type": "string"
                },
                "pnpProfileList": {
                "description":
                 "",
                "items": {
                "properties": {
                "createdBy": {
                "description":
                 "",
                "type": "string"
                },
                "discoveryCreated": {
                "type": "boolean"
                },
                "primaryEndpoint": {
                "description":
                 "",
                "properties": {
                "certificate": {
                "description":
                 "",
                "type": "string"
                },
                "fqdn": {
                "description":
                 "",
                "type": "string"
                },
                "ipv4Address": {},
                "ipv6Address": {},
                "port": {
                "type": "number"
                },
                "protocol": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "profileName": {
                "description":
                 "",
                "type": "string"
                },
                "secondaryEndpoint": {
                "description":
                 "",
                "properties": {
                "certificate": {
                "description":
                 "",
                "type": "string"
                },
                "fqdn": {
                "description":
                 "",
                "type": "string"
                },
                "ipv4Address": {},
                "ipv6Address": {},
                "port": {
                "type": "number"
                },
                "protocol": {
                "description":
                 "",
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
                "populateInventory": {
                "type": "boolean"
                },
                "preWorkflowCliOuputs": {
                "description":
                 "",
                "items": {
                "properties": {
                "cli": {
                "description":
                 "",
                "type": "string"
                },
                "cliOutput": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "projectId": {
                "description":
                 "",
                "type": "string"
                },
                "projectName": {
                "description":
                 "",
                "type": "string"
                },
                "reloadRequested": {
                "type": "boolean"
                },
                "serialNumber": {
                "description":
                 "",
                "type": "string"
                },
                "smartAccountId": {
                "description":
                 "",
                "type": "string"
                },
                "source": {
                "description":
                 "",
                "type": "string"
                },
                "stack": {
                "type": "boolean"
                },
                "stackInfo": {
                "description":
                 "",
                "properties": {
                "isFullRing": {
                "type": "boolean"
                },
                "stackMemberList": {
                "description":
                 "",
                "items": {
                "properties": {
                "hardwareVersion": {
                "description":
                 "",
                "type": "string"
                },
                "licenseLevel": {
                "description":
                 "",
                "type": "string"
                },
                "licenseType": {
                "description":
                 "",
                "type": "string"
                },
                "macAddress": {
                "description":
                 "",
                "type": "string"
                },
                "pid": {
                "description":
                 "",
                "type": "string"
                },
                "priority": {
                "type": "number"
                },
                "role": {
                "description":
                 "",
                "type": "string"
                },
                "serialNumber": {
                "description":
                 "",
                "type": "string"
                },
                "softwareVersion": {
                "description":
                 "",
                "type": "string"
                },
                "stackNumber": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "sudiSerialNumber": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "stackRingProtocol": {
                "description":
                 "",
                "type": "string"
                },
                "supportsStackWorkflows": {
                "type": "boolean"
                },
                "totalMemberCount": {
                "type": "number"
                },
                "validLicenseLevels": {
                "description":
                 "",
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
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
                "Deleted"
                ],
                "type": "string"
                },
                "sudiRequired": {
                "type": "boolean"
                },
                "tags": {},
                "userSudiSerialNos": {
                "description":
                 "",
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "virtualAccountId": {
                "description":
                 "",
                "type": "string"
                },
                "workflowId": {
                "description":
                 "",
                "type": "string"
                },
                "workflowName": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "runSummaryList": {
                "description":
                 "",
                "items": {
                "properties": {
                "details": {
                "description":
                 "",
                "type": "string"
                },
                "errorFlag": {
                "type": "boolean"
                },
                "historyTaskInfo": {
                "description":
                 "",
                "properties": {
                "addnDetails": {
                "description":
                 "",
                "items": {
                "properties": {
                "key": {
                "description":
                 "",
                "type": "string"
                },
                "value": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "timeTaken": {
                "type": "number"
                },
                "type": {
                "description":
                 "",
                "type": "string"
                },
                "workItemList": {
                "description":
                 "",
                "items": {
                "properties": {
                "command": {
                "description":
                 "",
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "outputStr": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "timeTaken": {
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
                "timestamp": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "systemResetWorkflow": {
                "description":
                 "",
                "properties": {
                "_id": {
                "description":
                 "",
                "type": "string"
                },
                "addToInventory": {
                "type": "boolean"
                },
                "addedOn": {
                "type": "number"
                },
                "configId": {
                "description":
                 "",
                "type": "string"
                },
                "currTaskIdx": {
                "type": "number"
                },
                "description":
                 {
                "description":
                 "",
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "execTime": {
                "type": "number"
                },
                "imageId": {
                "description":
                 "",
                "type": "string"
                },
                "instanceType": {
                "description":
                 "",
                "enum": [
                "SystemWorkflow",
                "UserWorkflow",
                "SystemResetWorkflow"
                ],
                "type": "string"
                },
                "lastupdateOn": {
                "type": "number"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "tasks": {
                "description":
                 "",
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": "number"
                },
                "endTime": {
                "type": "number"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "taskSeqNo": {
                "type": "number"
                },
                "timeTaken": {
                "type": "number"
                },
                "type": {
                "description":
                 "",
                "type": "string"
                },
                "workItemList": {
                "description":
                 "",
                "items": {
                "properties": {
                "command": {
                "description":
                 "",
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "outputStr": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "timeTaken": {
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
                "type": "array"
                },
                "tenantId": {
                "description":
                 "",
                "type": "string"
                },
                "type": {
                "description":
                 "",
                "type": "string"
                },
                "useState": {
                "description":
                 "",
                "type": "string"
                },
                "version": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "systemWorkflow": {
                "description":
                 "",
                "properties": {
                "_id": {
                "description":
                 "",
                "type": "string"
                },
                "addToInventory": {
                "type": "boolean"
                },
                "addedOn": {
                "type": "number"
                },
                "configId": {
                "description":
                 "",
                "type": "string"
                },
                "currTaskIdx": {
                "type": "number"
                },
                "description":
                 {
                "description":
                 "",
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "execTime": {
                "type": "number"
                },
                "imageId": {
                "description":
                 "",
                "type": "string"
                },
                "instanceType": {
                "description":
                 "",
                "enum": [
                "SystemWorkflow",
                "UserWorkflow",
                "SystemResetWorkflow"
                ],
                "type": "string"
                },
                "lastupdateOn": {
                "type": "number"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "tasks": {
                "description":
                 "",
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": "number"
                },
                "endTime": {
                "type": "number"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "taskSeqNo": {
                "type": "number"
                },
                "timeTaken": {
                "type": "number"
                },
                "type": {
                "description":
                 "",
                "type": "string"
                },
                "workItemList": {
                "description":
                 "",
                "items": {
                "properties": {
                "command": {
                "description":
                 "",
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "outputStr": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "timeTaken": {
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
                "type": "array"
                },
                "tenantId": {
                "description":
                 "",
                "type": "string"
                },
                "type": {
                "description":
                 "",
                "type": "string"
                },
                "useState": {
                "description":
                 "",
                "type": "string"
                },
                "version": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "tenantId": {
                "description":
                 "",
                "type": "string"
                },
                "version": {
                "type": "number"
                },
                "workflow": {
                "description":
                 "",
                "properties": {
                "_id": {
                "description":
                 "",
                "type": "string"
                },
                "addToInventory": {
                "type": "boolean"
                },
                "addedOn": {
                "type": "number"
                },
                "configId": {
                "description":
                 "",
                "type": "string"
                },
                "currTaskIdx": {
                "type": "number"
                },
                "description":
                 {
                "description":
                 "",
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "execTime": {
                "type": "number"
                },
                "imageId": {
                "description":
                 "",
                "type": "string"
                },
                "instanceType": {
                "description":
                 "",
                "enum": [
                "SystemWorkflow",
                "UserWorkflow",
                "SystemResetWorkflow"
                ],
                "type": "string"
                },
                "lastupdateOn": {
                "type": "number"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "tasks": {
                "description":
                 "",
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": "number"
                },
                "endTime": {
                "type": "number"
                },
                "name": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "taskSeqNo": {
                "type": "number"
                },
                "timeTaken": {
                "type": "number"
                },
                "type": {
                "description":
                 "",
                "type": "string"
                },
                "workItemList": {
                "description":
                 "",
                "items": {
                "properties": {
                "command": {
                "description":
                 "",
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "outputStr": {
                "description":
                 "",
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "description":
                 "",
                "type": "string"
                },
                "timeTaken": {
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
                "type": "array"
                },
                "tenantId": {
                "description":
                 "",
                "type": "string"
                },
                "type": {
                "description":
                 "",
                "type": "string"
                },
                "useState": {
                "description":
                 "",
                "type": "string"
                },
                "version": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "workflowParameters": {
                "description":
                 "",
                "properties": {
                "configList": {
                "description":
                 "",
                "items": {
                "properties": {
                "configId": {
                "description":
                 "",
                "type": "string"
                },
                "configParameters": {
                "description":
                 "",
                "items": {
                "properties": {
                "key": {
                "description":
                 "",
                "type": "string"
                },
                "value": {
                "description":
                 "",
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
                "licenseLevel": {
                "description":
                 "",
                "type": "string"
                },
                "licenseType": {
                "description":
                 "",
                "type": "string"
                },
                "topOfStackSerialNumber": {
                "description":
                 "",
                "type": "string"
                }
                },
                "type": "object"
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

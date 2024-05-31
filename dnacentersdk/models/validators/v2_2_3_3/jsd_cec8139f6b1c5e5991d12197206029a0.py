# -*- coding: utf-8 -*-
"""Cisco DNA Center UpdateDevice data model.

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


import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorCec8139F6B1C5E5991D12197206029A0(object):
    """UpdateDevice request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorCec8139F6B1C5E5991D12197206029A0, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "_id": {
                "type": "string"
                },
                "deviceInfo": {
                "properties": {
                "aaaCredentials": {
                "properties": {
                "password": {
                "type": "string"
                },
                "username": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "addedOn": {
                "type": "integer"
                },
                "addnMacAddrs": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "agentType": {
                "enum": [
                "POSIX",
                "IOS"
                ],
                "type": "string"
                },
                "authStatus": {
                "type": "string"
                },
                "authenticatedSudiSerialNo": {
                "type": "string"
                },
                "capabilitiesSupported": {
                "items": {
                "type": "string"
                },
                "type": "array"
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
                "ErrorAuthenticating"
                ],
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "deviceSudiSerialNos": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "deviceType": {
                "type": "string"
                },
                "featuresSupported": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "fileSystemList": {
                "items": {
                "properties": {
                "freespace": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "readable": {
                "type": "boolean"
                },
                "size": {
                "type": "integer"
                },
                "type": {
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
                "type": "integer"
                },
                "hostname": {
                "type": "string"
                },
                "httpHeaders": {
                "items": {
                "properties": {
                "key": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "imageFile": {
                "type": "string"
                },
                "imageVersion": {
                "type": "string"
                },
                "ipInterfaces": {
                "items": {
                "properties": {
                "ipv4Address": {
                "type": "object"
                },
                "ipv6AddressList": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "macAddress": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "status": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "lastContact": {
                "type": "integer"
                },
                "lastSyncTime": {
                "type": "integer"
                },
                "lastUpdateOn": {
                "type": "integer"
                },
                "location": {
                "properties": {
                "address": {
                "type": "string"
                },
                "altitude": {
                "type": "string"
                },
                "latitude": {
                "type": "string"
                },
                "longitude": {
                "type": "string"
                },
                "siteId": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "macAddress": {
                "type": "string"
                },
                "mode": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "neighborLinks": {
                "items": {
                "properties": {
                "localInterfaceName": {
                "type": "string"
                },
                "localMacAddress": {
                "type": "string"
                },
                "localShortInterfaceName": {
                "type": "string"
                },
                "remoteDeviceName": {
                "type": "string"
                },
                "remoteInterfaceName": {
                "type": "string"
                },
                "remoteMacAddress": {
                "type": "string"
                },
                "remotePlatform": {
                "type": "string"
                },
                "remoteShortInterfaceName": {
                "type": "string"
                },
                "remoteVersion": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
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
                "Provisioned"
                ],
                "type": "string"
                },
                "pid": {
                "type": "string"
                },
                "pnpProfileList": {
                "items": {
                "properties": {
                "createdBy": {
                "type": "string"
                },
                "discoveryCreated": {
                "type": "boolean"
                },
                "primaryEndpoint": {
                "properties": {
                "certificate": {
                "type": "string"
                },
                "fqdn": {
                "type": "string"
                },
                "ipv4Address": {
                "type": "object"
                },
                "ipv6Address": {
                "type": "object"
                },
                "port": {
                "type": "integer"
                },
                "protocol": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "profileName": {
                "type": "string"
                },
                "secondaryEndpoint": {
                "properties": {
                "certificate": {
                "type": "string"
                },
                "fqdn": {
                "type": "string"
                },
                "ipv4Address": {
                "type": "object"
                },
                "ipv6Address": {
                "type": "object"
                },
                "port": {
                "type": "integer"
                },
                "protocol": {
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
                "items": {
                "properties": {
                "cli": {
                "type": "string"
                },
                "cliOutput": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "projectId": {
                "type": "string"
                },
                "projectName": {
                "type": "string"
                },
                "reloadRequested": {
                "type": "boolean"
                },
                "serialNumber": {
                "type": "string"
                },
                "smartAccountId": {
                "type": "string"
                },
                "source": {
                "type": "string"
                },
                "stack": {
                "type": "boolean"
                },
                "stackInfo": {
                "properties": {
                "isFullRing": {
                "type": "boolean"
                },
                "stackMemberList": {
                "items": {
                "properties": {
                "hardwareVersion": {
                "type": "string"
                },
                "licenseLevel": {
                "type": "string"
                },
                "licenseType": {
                "type": "string"
                },
                "macAddress": {
                "type": "string"
                },
                "pid": {
                "type": "string"
                },
                "priority": {
                "type": "integer"
                },
                "role": {
                "type": "string"
                },
                "serialNumber": {
                "type": "string"
                },
                "softwareVersion": {
                "type": "string"
                },
                "stackNumber": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "sudiSerialNumber": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "stackRingProtocol": {
                "type": "string"
                },
                "supportsStackWorkflows": {
                "type": "boolean"
                },
                "totalMemberCount": {
                "type": "integer"
                },
                "validLicenseLevels": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "state": {
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
                "tags": {
                "type": "object"
                },
                "userSudiSerialNos": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "virtualAccountId": {
                "type": "string"
                },
                "workflowId": {
                "type": "string"
                },
                "workflowName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "runSummaryList": {
                "items": {
                "properties": {
                "details": {
                "type": "string"
                },
                "errorFlag": {
                "type": "boolean"
                },
                "historyTaskInfo": {
                "properties": {
                "addnDetails": {
                "items": {
                "properties": {
                "key": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "name": {
                "type": "string"
                },
                "timeTaken": {
                "type": "integer"
                },
                "type": {
                "type": "string"
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
                "type": "string"
                },
                "endTime": {
                "type": "integer"
                },
                "outputStr": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "timeTaken": {
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
                "timestamp": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "systemResetWorkflow": {
                "properties": {
                "_id": {
                "type": "string"
                },
                "addToInventory": {
                "type": "boolean"
                },
                "addedOn": {
                "type": "integer"
                },
                "configId": {
                "type": "string"
                },
                "currTaskIdx": {
                "type": "integer"
                },
                "description":
                 {
                "type": "string"
                },
                "endTime": {
                "type": "integer"
                },
                "execTime": {
                "type": "integer"
                },
                "imageId": {
                "type": "string"
                },
                "instanceType": {
                "enum": [
                "SystemWorkflow",
                "UserWorkflow",
                "SystemResetWorkflow"
                ],
                "type": "string"
                },
                "lastupdateOn": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "tasks": {
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": "integer"
                },
                "endTime": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "taskSeqNo": {
                "type": "integer"
                },
                "timeTaken": {
                "type": "integer"
                },
                "type": {
                "type": "string"
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
                "type": "string"
                },
                "endTime": {
                "type": "integer"
                },
                "outputStr": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "timeTaken": {
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
                "type": "array"
                },
                "tenantId": {
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "useState": {
                "type": "string"
                },
                "version": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "systemWorkflow": {
                "properties": {
                "_id": {
                "type": "string"
                },
                "addToInventory": {
                "type": "boolean"
                },
                "addedOn": {
                "type": "integer"
                },
                "configId": {
                "type": "string"
                },
                "currTaskIdx": {
                "type": "integer"
                },
                "description":
                 {
                "type": "string"
                },
                "endTime": {
                "type": "integer"
                },
                "execTime": {
                "type": "integer"
                },
                "imageId": {
                "type": "string"
                },
                "instanceType": {
                "enum": [
                "SystemWorkflow",
                "UserWorkflow",
                "SystemResetWorkflow"
                ],
                "type": "string"
                },
                "lastupdateOn": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "tasks": {
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": "integer"
                },
                "endTime": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "taskSeqNo": {
                "type": "integer"
                },
                "timeTaken": {
                "type": "integer"
                },
                "type": {
                "type": "string"
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
                "type": "string"
                },
                "endTime": {
                "type": "integer"
                },
                "outputStr": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "timeTaken": {
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
                "type": "array"
                },
                "tenantId": {
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "useState": {
                "type": "string"
                },
                "version": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "tenantId": {
                "type": "string"
                },
                "version": {
                "type": "integer"
                },
                "workflow": {
                "properties": {
                "_id": {
                "type": "string"
                },
                "addToInventory": {
                "type": "boolean"
                },
                "addedOn": {
                "type": "integer"
                },
                "configId": {
                "type": "string"
                },
                "currTaskIdx": {
                "type": "integer"
                },
                "description":
                 {
                "type": "string"
                },
                "endTime": {
                "type": "integer"
                },
                "execTime": {
                "type": "integer"
                },
                "imageId": {
                "type": "string"
                },
                "instanceType": {
                "enum": [
                "SystemWorkflow",
                "UserWorkflow",
                "SystemResetWorkflow"
                ],
                "type": "string"
                },
                "lastupdateOn": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "tasks": {
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": "integer"
                },
                "endTime": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "taskSeqNo": {
                "type": "integer"
                },
                "timeTaken": {
                "type": "integer"
                },
                "type": {
                "type": "string"
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
                "type": "string"
                },
                "endTime": {
                "type": "integer"
                },
                "outputStr": {
                "type": "string"
                },
                "startTime": {
                "type": "integer"
                },
                "state": {
                "type": "string"
                },
                "timeTaken": {
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
                "type": "array"
                },
                "tenantId": {
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "useState": {
                "type": "string"
                },
                "version": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "workflowParameters": {
                "properties": {
                "configList": {
                "items": {
                "properties": {
                "configId": {
                "type": "string"
                },
                "configParameters": {
                "items": {
                "properties": {
                "key": {
                "type": "string"
                },
                "value": {
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
                "type": "string"
                },
                "licenseType": {
                "type": "string"
                },
                "topOfStackSerialNumber": {
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

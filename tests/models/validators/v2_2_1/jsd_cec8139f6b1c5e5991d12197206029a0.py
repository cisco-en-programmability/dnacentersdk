# -*- coding: utf-8 -*-
"""Cisco DNA Center updateDevice data model.

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


class JSONSchemaValidatorCec8139F6B1C5E5991D12197206029A0(object):
    """updateDevice request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorCec8139F6B1C5E5991D12197206029A0, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "_id": {
                "type": "string"
                },
                "dayZeroConfig": {
                "properties": {
                "config": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "dayZeroConfigPreview": {
                "type": "object"
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
                "type": "number"
                },
                "addnMacAddrs": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "agentType": {
                "type": "string"
                },
                "authStatus": {
                "type": "string"
                },
                "authenticatedMicNumber": {
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
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "readable": {
                "type": "boolean"
                },
                "size": {
                "type": "number"
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
                "type": "number"
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
                "type": "number"
                },
                "lastSyncTime": {
                "type": "number"
                },
                "lastUpdateOn": {
                "type": "number"
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
                "type": "number"
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
                "type": "number"
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
                "siteId": {
                "type": "string"
                },
                "siteName": {
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
                "type": "number"
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
                "type": "number"
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
                "type": "number"
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
                "type": "string"
                },
                "sudiRequired": {
                "type": "boolean"
                },
                "tags": {
                "type": "object"
                },
                "userMicNumbers": {
                "items": {
                "type": "string"
                },
                "type": "array"
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
                "type": "number"
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
                "type": "number"
                },
                "outputStr": {
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
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
                "properties": {
                "_id": {
                "type": "string"
                },
                "addToInventory": {
                "type": "boolean"
                },
                "addedOn": {
                "type": "number"
                },
                "configId": {
                "type": "string"
                },
                "currTaskIdx": {
                "type": "number"
                },
                "description":
                 {
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "execTime": {
                "type": "number"
                },
                "imageId": {
                "type": "string"
                },
                "instanceType": {
                "type": "string"
                },
                "lastupdateOn": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "type": "string"
                },
                "tasks": {
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": "number"
                },
                "endTime": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "type": "string"
                },
                "taskSeqNo": {
                "type": "number"
                },
                "timeTaken": {
                "type": "number"
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
                "type": "number"
                },
                "outputStr": {
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
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
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "useState": {
                "type": "string"
                },
                "version": {
                "type": "number"
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
                "type": "number"
                },
                "configId": {
                "type": "string"
                },
                "currTaskIdx": {
                "type": "number"
                },
                "description":
                 {
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "execTime": {
                "type": "number"
                },
                "imageId": {
                "type": "string"
                },
                "instanceType": {
                "type": "string"
                },
                "lastupdateOn": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "type": "string"
                },
                "tasks": {
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": "number"
                },
                "endTime": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "type": "string"
                },
                "taskSeqNo": {
                "type": "number"
                },
                "timeTaken": {
                "type": "number"
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
                "type": "number"
                },
                "outputStr": {
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
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
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "useState": {
                "type": "string"
                },
                "version": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "tenantId": {
                "type": "string"
                },
                "version": {
                "type": "number"
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
                "type": "number"
                },
                "configId": {
                "type": "string"
                },
                "currTaskIdx": {
                "type": "number"
                },
                "description":
                 {
                "type": "string"
                },
                "endTime": {
                "type": "number"
                },
                "execTime": {
                "type": "number"
                },
                "imageId": {
                "type": "string"
                },
                "instanceType": {
                "type": "string"
                },
                "lastupdateOn": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "type": "string"
                },
                "tasks": {
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": "number"
                },
                "endTime": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
                "type": "string"
                },
                "taskSeqNo": {
                "type": "number"
                },
                "timeTaken": {
                "type": "number"
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
                "type": "number"
                },
                "outputStr": {
                "type": "string"
                },
                "startTime": {
                "type": "number"
                },
                "state": {
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
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "useState": {
                "type": "string"
                },
                "version": {
                "type": "number"
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

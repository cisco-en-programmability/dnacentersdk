# -*- coding: utf-8 -*-
"""Cisco DNA Center EditSensorTestTemplate data model.

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


class JSONSchemaValidatorE2F9718DE3D050819Cdc6355A3A43200(object):
    """EditSensorTestTemplate request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE2F9718DE3D050819Cdc6355A3A43200, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "_id": {
                "type": "string"
                },
                "actionInProgress": {
                "type": "string"
                },
                "apCoverage": {
                "items": {
                "properties": {
                "bands": {
                "type": "string"
                },
                "numberOfApsToTest": {
                "type": "integer"
                },
                "rssiThreshold": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "connection": {
                "type": "string"
                },
                "encryptionMode": {
                "type": "string"
                },
                "frequency": {
                "properties": {
                "unit": {
                "type": "string"
                },
                "value": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "lastModifiedTime": {
                "type": "integer"
                },
                "location": {
                "type": "string"
                },
                "locationInfoList": {
                "items": {
                "properties": {
                "allSensors": {
                "type": "boolean"
                },
                "customManagementVlan": {
                "type": "boolean"
                },
                "locationId": {
                "type": "string"
                },
                "locationType": {
                "type": "string"
                },
                "macAddressList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "managementVlan": {
                "type": "string"
                },
                "siteHierarchy": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "modelVersion": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "numAssociatedSensor": {
                "type": "integer"
                },
                "numNeighborAPThreshold": {
                "type": "integer"
                },
                "profiles": {
                "items": {
                "properties": {
                "authProtocol": {
                "type": "string"
                },
                "authType": {
                "type": "string"
                },
                "certdownloadurl": {
                "type": "string"
                },
                "certfilename": {
                "type": "string"
                },
                "certpassphrase": {
                "type": "string"
                },
                "certstatus": {
                "type": "string"
                },
                "certxferprotocol": {
                "type": "string"
                },
                "deviceType": {
                "type": "string"
                },
                "eapMethod": {
                "type": "string"
                },
                "extWebAuth": {
                "type": "boolean"
                },
                "extWebAuthAccessUrl": {
                "type": "string"
                },
                "extWebAuthHtmlTag": {
                "items": {
                "properties": {
                "label": {
                "type": "string"
                },
                "tag": {
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
                "extWebAuthPortal": {
                "type": "string"
                },
                "extWebAuthVirtualIp": {
                "type": "string"
                },
                "locationVlanList": {
                "items": {
                "properties": {
                "locationId": {
                "type": "string"
                },
                "vlans": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "password": {
                "type": "string"
                },
                "passwordType": {
                "type": "string"
                },
                "profileName": {
                "type": "string"
                },
                "psk": {
                "type": "string"
                },
                "qosPolicy": {
                "type": "string"
                },
                "scep": {
                "type": "boolean"
                },
                "tests": {
                "items": {
                "properties": {
                "config": {
                "items": {
                "properties": {
                "direction": {
                "type": "string"
                },
                "domains": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "downlinkTest": {
                "type": "boolean"
                },
                "endPort": {
                "type": "integer"
                },
                "exitCommand": {
                "type": "string"
                },
                "finalPrompt": {
                "type": "string"
                },
                "ndtServer": {
                "type": "string"
                },
                "ndtServerPath": {
                "type": "string"
                },
                "ndtServerPort": {
                "type": "string"
                },
                "numPackets": {
                "type": "integer"
                },
                "password": {
                "type": "string"
                },
                "passwordPrompt": {
                "type": "string"
                },
                "pathToDownload": {
                "type": "string"
                },
                "port": {
                "type": "integer"
                },
                "probeType": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "proxyPassword": {
                "type": "string"
                },
                "proxyPort": {
                "type": "string"
                },
                "proxyServer": {
                "type": "string"
                },
                "proxyUserName": {
                "type": "string"
                },
                "server": {
                "type": "string"
                },
                "servers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sharedSecret": {
                "type": "string"
                },
                "startPort": {
                "type": "integer"
                },
                "transferType": {
                "type": "string"
                },
                "udpBandwidth": {
                "type": "integer"
                },
                "uplinkTest": {
                "type": "boolean"
                },
                "url": {
                "type": "string"
                },
                "userName": {
                "type": "string"
                },
                "userNamePrompt": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "username": {
                "type": "string"
                },
                "vlan": {
                "type": "string"
                },
                "whiteList": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "radioAsSensorRemoved": {
                "type": "boolean"
                },
                "rssiThreshold": {
                "type": "integer"
                },
                "runNow": {
                "type": "string"
                },
                "scheduleInDays": {
                "type": "integer"
                },
                "sensors": {
                "items": {
                "properties": {
                "allSensorAddition": {
                "type": "boolean"
                },
                "assigned": {
                "type": "boolean"
                },
                "configUpdated": {
                "type": "string"
                },
                "hostName": {
                "type": "string"
                },
                "iPerfInfo": {
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "ipAddress": {
                "type": "string"
                },
                "locationId": {
                "type": "string"
                },
                "macAddress": {
                "type": "string"
                },
                "markedForUninstall": {
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "runNow": {
                "type": "string"
                },
                "sensorType": {
                "type": "string"
                },
                "servicePolicy": {
                "type": "string"
                },
                "status": {
                "type": "string"
                },
                "switchMac": {
                "type": "string"
                },
                "switchSerialNumber": {
                "type": "string"
                },
                "switchUuid": {
                "type": "string"
                },
                "targetAPs": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "testMacAddresses": {
                "type": "object"
                },
                "wiredApplicationMessage": {
                "type": "string"
                },
                "wiredApplicationStatus": {
                "type": "string"
                },
                "xorSensor": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "showWlcUpgradeBanner": {
                "type": "boolean"
                },
                "siteHierarchy": {
                "type": "string"
                },
                "ssids": {
                "items": {
                "properties": {
                "authProtocol": {
                "type": "string"
                },
                "authType": {
                "type": "string"
                },
                "bands": {
                "type": "string"
                },
                "certdownloadurl": {
                "type": "string"
                },
                "certfilename": {
                "type": "string"
                },
                "certpassphrase": {
                "type": "string"
                },
                "certstatus": {
                "type": "string"
                },
                "certxferprotocol": {
                "type": "string"
                },
                "eapMethod": {
                "type": "string"
                },
                "extWebAuth": {
                "type": "boolean"
                },
                "extWebAuthAccessUrl": {
                "type": "string"
                },
                "extWebAuthHtmlTag": {
                "items": {
                "properties": {
                "label": {
                "type": "string"
                },
                "tag": {
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
                "extWebAuthPortal": {
                "type": "string"
                },
                "extWebAuthVirtualIp": {
                "type": "string"
                },
                "id": {
                "type": "integer"
                },
                "layer3webAuthEmailAddress": {
                "type": "string"
                },
                "layer3webAuthpassword": {
                "type": "string"
                },
                "layer3webAuthsecurity": {
                "type": "string"
                },
                "layer3webAuthuserName": {
                "type": "string"
                },
                "numAps": {
                "type": "integer"
                },
                "numSensors": {
                "type": "integer"
                },
                "password": {
                "type": "string"
                },
                "passwordType": {
                "type": "string"
                },
                "profileName": {
                "type": "string"
                },
                "proxyPassword": {
                "type": "string"
                },
                "proxyPort": {
                "type": "string"
                },
                "proxyServer": {
                "type": "string"
                },
                "proxyUserName": {
                "type": "string"
                },
                "psk": {
                "type": "string"
                },
                "qosPolicy": {
                "type": "string"
                },
                "scep": {
                "type": "boolean"
                },
                "ssid": {
                "type": "string"
                },
                "status": {
                "type": "string"
                },
                "tests": {
                "items": {
                "properties": {
                "config": {
                "items": {
                "properties": {
                "direction": {
                "type": "string"
                },
                "domains": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "downlinkTest": {
                "type": "boolean"
                },
                "endPort": {
                "type": "integer"
                },
                "exitCommand": {
                "type": "string"
                },
                "finalPrompt": {
                "type": "string"
                },
                "ndtServer": {
                "type": "string"
                },
                "ndtServerPath": {
                "type": "string"
                },
                "ndtServerPort": {
                "type": "string"
                },
                "numPackets": {
                "type": "integer"
                },
                "password": {
                "type": "string"
                },
                "passwordPrompt": {
                "type": "string"
                },
                "pathToDownload": {
                "type": "string"
                },
                "port": {
                "type": "integer"
                },
                "probeType": {
                "type": "string"
                },
                "protocol": {
                "type": "string"
                },
                "proxyPassword": {
                "type": "string"
                },
                "proxyPort": {
                "type": "string"
                },
                "proxyServer": {
                "type": "string"
                },
                "proxyUserName": {
                "type": "string"
                },
                "server": {
                "type": "string"
                },
                "servers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sharedSecret": {
                "type": "string"
                },
                "startPort": {
                "type": "integer"
                },
                "transferType": {
                "type": "string"
                },
                "udpBandwidth": {
                "type": "integer"
                },
                "uplinkTest": {
                "type": "boolean"
                },
                "url": {
                "type": "string"
                },
                "userName": {
                "type": "string"
                },
                "userNamePrompt": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "thirdParty": {
                "properties": {
                "selected": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "username": {
                "type": "string"
                },
                "validFrom": {
                "type": "integer"
                },
                "validTo": {
                "type": "integer"
                },
                "whiteList": {
                "type": "boolean"
                },
                "wlanId": {
                "type": "integer"
                },
                "wlc": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "startTime": {
                "type": "integer"
                },
                "status": {
                "type": "string"
                },
                "templateName": {
                "type": "string"
                },
                "testScheduleMode": {
                "type": "string"
                },
                "version": {
                "type": "integer"
                },
                "wlans": {
                "items": {
                "type": "string"
                },
                "type": "array"
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

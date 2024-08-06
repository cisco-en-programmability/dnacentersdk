# -*- coding: utf-8 -*-
"""Cisco DNA Center GetInterfaceDetails data model.

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


class JSONSchemaValidatorBef9E9B306085D879B877598Fad71B51(object):
    """GetInterfaceDetails request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorBef9E9B306085D879B877598Fad71B51, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "addresses": {
                "items": {
                "properties": {
                "address": {
                "properties": {
                "ipAddress": {
                "properties": {
                "address": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "ipMask": {
                "properties": {
                "address": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "isInverseMask": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "adminStatus": {
                "type": "string"
                },
                "className": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "deviceId": {
                "type": "string"
                },
                "duplex": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "ifIndex": {
                "type": "string"
                },
                "instanceTenantId": {
                "type": "string"
                },
                "instanceUuid": {
                "type": "string"
                },
                "interfaceType": {
                "type": "string"
                },
                "ipv4Address": {
                "type": "string"
                },
                "ipv4Mask": {
                "type": "string"
                },
                "isisSupport": {
                "type": "string"
                },
                "lastIncomingPacketTime": {
                "type": "number"
                },
                "lastOutgoingPacketTime": {
                "type": "number"
                },
                "lastUpdated": {
                "type": "string"
                },
                "macAddress": {
                "type": "string"
                },
                "managedComputeElement": {
                "type": "string"
                },
                "managedComputeElementUrl": {
                "type": "string"
                },
                "managedNetworkElement": {
                "type": "string"
                },
                "managedNetworkElementUrl": {
                "type": "string"
                },
                "mappedPhysicalInterfaceId": {
                "type": "string"
                },
                "mappedPhysicalInterfaceName": {
                "type": "string"
                },
                "mediaType": {
                "type": "string"
                },
                "mtu": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "nativeVlanId": {
                "type": "string"
                },
                "networkdevice_id": {
                "type": "string"
                },
                "ospfSupport": {
                "type": "string"
                },
                "pid": {
                "type": "string"
                },
                "portMode": {
                "type": "string"
                },
                "portName": {
                "type": "string"
                },
                "portType": {
                "type": "string"
                },
                "poweroverethernet": {
                "type": "string"
                },
                "serialNo": {
                "type": "string"
                },
                "series": {
                "type": "string"
                },
                "speed": {
                "type": "string"
                },
                "status": {
                "type": "string"
                },
                "vlanId": {
                "type": "string"
                },
                "voiceVlan": {
                "type": "string"
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

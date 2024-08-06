# -*- coding: utf-8 -*-
"""Cisco DNA Center GetsTheListOfInterfacesAcrossTheNetworkDevicesBasedOnTheProvidedComplexFilte
rsAndAggregationFunctions data model.

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


class JSONSchemaValidatorF667322836D5527482Ad2100Bec7Feb4(object):
    """GetsTheListOfInterfacesAcrossTheNetworkDevicesBasedOnTheProvidedCo
    mplexFiltersAndAggregationFunctions request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF667322836D5527482Ad2100Bec7Feb4, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "page": {
                "properties": {
                "count": {
                "type": "integer"
                },
                "limit": {
                "type": "integer"
                },
                "offset": {
                "type": "integer"
                },
                "sortBy": {
                "items": {
                "properties": {
                "name": {
                "type": "string"
                },
                "order": {
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
                "response": {
                "items": {
                "properties": {
                "adminStatus": {
                "type": "string"
                },
                "aggregateAttributes": {
                "items": {
                "properties": {
                "name": {
                "type": "string"
                },
                "values": {
                "items": {
                "properties": {
                "key": {
                "type": "string"
                },
                "value": {
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
                "description":
                 {
                "type": "string"
                },
                "duplexConfig": {
                "type": "string"
                },
                "duplexOper": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "interfaceIfIndex": {
                "type": "integer"
                },
                "interfaceType": {
                "type": "string"
                },
                "ipv4Address": {
                "type": "string"
                },
                "ipv6AddressList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "isL3Interface": {
                "type": "boolean"
                },
                "isWan": {
                "type": "boolean"
                },
                "macAddr": {
                "type": "string"
                },
                "mediaType": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "networkDeviceId": {
                "type": "string"
                },
                "networkDeviceIpAddress": {
                "type": "string"
                },
                "networkDeviceMacAddress": {
                "type": "string"
                },
                "operStatus": {
                "type": "string"
                },
                "peerStackMember": {
                "type": "integer"
                },
                "peerStackPort": {
                "type": "string"
                },
                "portChannelId": {
                "type": "string"
                },
                "portMode": {
                "type": "string"
                },
                "portType": {
                "type": "string"
                },
                "rxDiscards": {
                "type": "number"
                },
                "rxError": {
                "type": "integer"
                },
                "rxRate": {
                "type": "number"
                },
                "rxUtilization": {
                "type": "number"
                },
                "siteHierarchy": {
                "type": "string"
                },
                "siteHierarchyId": {
                "type": "string"
                },
                "siteName": {
                "type": "string"
                },
                "speed": {
                "type": "string"
                },
                "stackPortType": {
                "type": "string"
                },
                "timestamp": {
                "type": "integer"
                },
                "txDiscards": {
                "type": "number"
                },
                "txError": {
                "type": "integer"
                },
                "txRate": {
                "type": "number"
                },
                "txUtilization": {
                "type": "number"
                },
                "vlanId": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
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

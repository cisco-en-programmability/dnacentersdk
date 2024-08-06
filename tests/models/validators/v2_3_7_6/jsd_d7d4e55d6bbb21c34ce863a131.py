# -*- coding: utf-8 -*-
"""Cisco DNA Center GetEventSubscriptions data model.

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

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorD7D4E55D6BBb21C34Ce863A131(object):
    """GetEventSubscriptions request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD7D4E55D6BBb21C34Ce863A131, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "description":
                 {
                "type": "string"
                },
                "filter": {
                "properties": {
                "categories": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "domainsSubdomains": {
                "items": {
                "properties": {
                "domain": {
                "type": "string"
                },
                "subDomains": {
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
                "eventIds": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "others": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "severities": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "siteIds": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sources": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "types": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "isPrivate": {
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "subscriptionEndpoints": {
                "items": {
                "properties": {
                "connectorType": {
                "type": "string"
                },
                "instanceId": {
                "type": "string"
                },
                "subscriptionDetails": {
                "properties": {
                "basePath": {
                "type": "string"
                },
                "body": {
                "type": "string"
                },
                "connectTimeout": {
                "type": "integer"
                },
                "connectorType": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "headers": {
                "items": {
                "properties": {
                "string": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "instanceId": {
                "type": "string"
                },
                "method": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "pathParams": {
                "items": {
                "properties": {
                "string": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "queryParams": {
                "items": {
                "properties": {
                "string": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "readTimeout": {
                "type": "integer"
                },
                "resource": {
                "type": "string"
                },
                "trustCert": {
                "type": "boolean"
                },
                "url": {
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
                "subscriptionId": {
                "type": "string"
                },
                "tenantId": {
                "type": "string"
                },
                "version": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )

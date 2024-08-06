# -*- coding: utf-8 -*-
"""Cisco DNA Center GetRestWebhookSubscriptionDetails data model.

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


class JSONSchemaValidatorF278C72555E9A56F554B2A21C85(object):
    """GetRestWebhookSubscriptionDetails request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF278C72555E9A56F554B2A21C85, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
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
                "name": {
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
                "instanceId": {
                "type": "string"
                },
                "method": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "namespace": {
                "type": "string"
                },
                "pathParams": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "proxyRoute": {
                "type": "boolean"
                },
                "queryParams": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "readTimeout": {
                "type": "integer"
                },
                "serviceName": {
                "type": "string"
                },
                "servicePort": {
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

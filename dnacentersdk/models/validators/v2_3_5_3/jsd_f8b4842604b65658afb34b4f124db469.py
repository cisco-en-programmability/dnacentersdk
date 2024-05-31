# -*- coding: utf-8 -*-
"""Cisco DNA Center UpdateEmailEventSubscription data model.

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


class JSONSchemaValidatorF8B4842604B65658Afb34B4F124Db469(object):
    """UpdateEmailEventSubscription request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF8B4842604B65658Afb34B4F124Db469, self).__init__()
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
                "severities": {
                "items": {
                "type": "integer"
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
                "name": {
                "type": "string"
                },
                "subscriptionEndpoints": {
                "items": {
                "properties": {
                "instanceId": {
                "type": "string"
                },
                "subscriptionDetails": {
                "properties": {
                "connectorType": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "fromEmailAddress": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "subject": {
                "type": "string"
                },
                "toEmailAddresses": {
                "items": {
                "type": "string"
                },
                "type": "array"
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

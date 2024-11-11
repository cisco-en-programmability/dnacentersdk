# -*- coding: utf-8 -*-
"""Cisco DNA Center NodesConfigurationSummary data model.

Copyright (c) 2024 Cisco Systems.

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


class JSONSchemaValidatorF0C26C266E552D6B0F1F68Da8E60E16(object):
    """NodesConfigurationSummary request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF0C26C266E552D6B0F1F68Da8E60E16, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "nodes": {
                "items": {
                "properties": {
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "network": {
                "items": {
                "properties": {
                "inet": {
                "properties": {
                "dns_servers": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "gateway": {
                "type": "string"
                },
                "host_ip": {
                "type": "string"
                },
                "netmask": {
                "type": "string"
                },
                "routes": {
                "items": {
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "inet6": {
                "properties": {
                "host_ip": {
                "type": "string"
                },
                "netmask": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "interface": {
                "type": "string"
                },
                "intra_cluster_link": {
                "type": "boolean"
                },
                "lacp_mode": {
                "type": "boolean"
                },
                "lacp_supported": {
                "type": "boolean"
                },
                "slave": {
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
                "ntp": {
                "properties": {
                "servers": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "platform": {
                "properties": {
                "product": {
                "type": "string"
                },
                "serial": {
                "type": "string"
                },
                "vendor": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "proxy": {
                "properties": {
                "http_proxy": {
                "type": "string"
                },
                "https_proxy": {
                "type": "string"
                },
                "https_proxy_password": {
                "type": "string"
                },
                "https_proxy_username": {
                "type": "string"
                },
                "no_proxy": {
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

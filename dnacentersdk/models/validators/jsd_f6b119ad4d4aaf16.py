# -*- coding: utf-8 -*-
"""DNA Center Create Template data model.

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
from dnacentersdk.exceptions import MalformedRequest

from builtins import *

class JSONSchemaValidatorF6B119Ad4D4AAf16(object):
    """Create Template request schema definition."""
    def __init__(self):
        # print("created f6b1-19ad-4d4a-af16")
        super(JSONSchemaValidatorF6B119Ad4D4AAf16, self).__init__()
        self._validator = fastjsonschema.compile( {'type': 'object', 'properties': {'author': {'type': 'string'}, 'composite': {'type': 'boolean'}, 'containingTemplates': {'type': 'array', 'items': {'type': 'object', 'properties': {'composite': {'type': 'boolean'}, 'id': {'type': 'string'}, 'name': {'type': 'string'}, 'version': {'type': 'string'}}}}, 'createTime': {'type': 'number'}, 'description': {'type': 'string'}, 'deviceTypes': {'type': 'array', 'items': {'type': 'object', 'properties': {'productFamily': {'type': 'string'}, 'productSeries': {'type': 'string'}, 'productType': {'type': 'string'}}}}, 'failurePolicy': {'type': 'string', 'enum': ['ABORT_ON_ERROR', 'CONTINUE_ON_ERROR', 'ROLLBACK_ON_ERROR', 'ROLLBACK_TARGET_ON_ERROR', 'ABORT_TARGET_ON_ERROR']}, 'id': {'type': 'string'}, 'lastUpdateTime': {'type': 'number'}, 'name': {'type': 'string'}, 'parentTemplateId': {'type': 'string'}, 'projectId': {'type': 'string'}, 'projectName': {'type': 'string'}, 'rollbackTemplateContent': {'type': 'string'}, 'rollbackTemplateParams': {'type': 'array', 'items': {'type': 'object', 'properties': {'binding': {'type': 'string'}, 'dataType': {'type': 'string', 'enum': ['STRING', 'INTEGER', 'IPADDRESS', 'MACADDRESS', 'SECTIONDIVIDER']}, 'defaultValue': {'type': 'string'}, 'description': {'type': 'string'}, 'displayName': {'type': 'string'}, 'group': {'type': 'string'}, 'id': {'type': 'string'}, 'instructionText': {'type': 'string'}, 'key': {'type': 'string'}, 'notParam': {'type': 'boolean'}, 'order': {'type': 'number'}, 'paramArray': {'type': 'boolean'}, 'parameterName': {'type': 'string'}, 'provider': {'type': 'string'}, 'range': {'type': 'array', 'items': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'maxValue': {'type': 'number'}, 'minValue': {'type': 'number'}}}}, 'required': {'type': 'boolean'}, 'selection': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'selectionType': {'type': 'string', 'enum': ['SINGLE_SELECT', 'MULTI_SELECT']}, 'selectionValues': {'type': 'object', 'properties': {}}}}}}}, 'softwareType': {'type': 'string'}, 'softwareVariant': {'type': 'string'}, 'softwareVersion': {'type': 'string'}, 'tags': {'type': 'array', 'items': {'type': 'string'}}, 'templateContent': {'type': 'string'}, 'templateParams': {'type': 'array', 'items': {'type': 'object', 'properties': {'binding': {'type': 'string'}, 'dataType': {'type': 'string', 'enum': ['STRING', 'INTEGER', 'IPADDRESS', 'MACADDRESS', 'SECTIONDIVIDER']}, 'defaultValue': {'type': 'string'}, 'description': {'type': 'string'}, 'displayName': {'type': 'string'}, 'group': {'type': 'string'}, 'id': {'type': 'string'}, 'instructionText': {'type': 'string'}, 'key': {'type': 'string'}, 'notParam': {'type': 'boolean'}, 'order': {'type': 'number'}, 'paramArray': {'type': 'boolean'}, 'parameterName': {'type': 'string'}, 'provider': {'type': 'string'}, 'range': {'type': 'array', 'items': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'maxValue': {'type': 'number'}, 'minValue': {'type': 'number'}}}}, 'required': {'type': 'boolean'}, 'selection': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'selectionType': {'type': 'string', 'enum': ['SINGLE_SELECT', 'MULTI_SELECT']}, 'selectionValues': {'type': 'object', 'properties': {}}}}}}}, 'version': {'type': 'string'}}} )

    def validate(self, request):
        try:
            self._validator(request)
            return True
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(request, e.message))
            return False
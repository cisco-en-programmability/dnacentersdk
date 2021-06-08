# -*- coding: utf-8 -*-
"""DNACenterAPI clients API fixtures and tests.

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
import pytest
from fastjsonschema.exceptions import JsonSchemaException
from dnacentersdk.exceptions import MalformedRequest
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.0', reason='version does not match')


def is_valid_get_overall_client_health(json_schema_validate, obj):
    json_schema_validate('jsd_149aa93b4ddb80dd_v1_3_0').validate(obj)
    return True


def get_overall_client_health(api):
    endpoint_result = api.clients.get_overall_client_health(
        timestamp=0
    )
    return endpoint_result


@pytest.mark.clients
def test_get_overall_client_health(api, validator):
    assert is_valid_get_overall_client_health(
        validator,
        get_overall_client_health(api)
    )


def get_overall_client_health_default(api):
    endpoint_result = api.clients.get_overall_client_health(
        timestamp=None
    )
    return endpoint_result


@pytest.mark.clients
def test_get_overall_client_health_default(api, validator):
    try:
        assert is_valid_get_overall_client_health(
            validator,
            get_overall_client_health_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_client_detail(json_schema_validate, obj):
    json_schema_validate('jsd_e2adba7943bab3e9_v1_3_0').validate(obj)
    return True


def get_client_detail(api):
    endpoint_result = api.clients.get_client_detail(
        mac_address='string',
        timestamp=0
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_detail(api, validator):
    assert is_valid_get_client_detail(
        validator,
        get_client_detail(api)
    )


def get_client_detail_default(api):
    endpoint_result = api.clients.get_client_detail(
        mac_address=None,
        timestamp=None
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_detail_default(api, validator):
    try:
        assert is_valid_get_client_detail(
            validator,
            get_client_detail_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

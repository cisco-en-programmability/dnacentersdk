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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.5', reason='version does not match')


def is_valid_get_client_detail(json_schema_validate, obj):
    json_schema_validate('jsd_f2c6333d8eb05491a16c2d32095e4352_v2_3_7_5').validate(obj)
    return True


def get_client_detail(api):
    endpoint_result = api.clients.get_client_detail(
        mac_address='string',
        timestamp=0
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_detail(api, validator):
    try:
        assert is_valid_get_client_detail(
            validator,
            get_client_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_client_detail_default_val(api):
    endpoint_result = api.clients.get_client_detail(
        mac_address=None,
        timestamp=None
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_detail_default_val(api, validator):
    try:
        assert is_valid_get_client_detail(
            validator,
            get_client_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_client_enrichment_details(json_schema_validate, obj):
    json_schema_validate('jsd_991dfd2751065bfb8c2367dd726df316_v2_3_7_5').validate(obj)
    return True


def get_client_enrichment_details(api):
    endpoint_result = api.clients.get_client_enrichment_details(

    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_enrichment_details(api, validator):
    try:
        assert is_valid_get_client_enrichment_details(
            validator,
            get_client_enrichment_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_client_enrichment_details_default_val(api):
    endpoint_result = api.clients.get_client_enrichment_details(

    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_enrichment_details_default_val(api, validator):
    try:
        assert is_valid_get_client_enrichment_details(
            validator,
            get_client_enrichment_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_overall_client_health(json_schema_validate, obj):
    json_schema_validate('jsd_f58ddf5cee095688aed79a9bb26e21e8_v2_3_7_5').validate(obj)
    return True


def get_overall_client_health(api):
    endpoint_result = api.clients.get_overall_client_health(
        timestamp=0
    )
    return endpoint_result


@pytest.mark.clients
def test_get_overall_client_health(api, validator):
    try:
        assert is_valid_get_overall_client_health(
            validator,
            get_overall_client_health(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_overall_client_health_default_val(api):
    endpoint_result = api.clients.get_overall_client_health(
        timestamp=None
    )
    return endpoint_result


@pytest.mark.clients
def test_get_overall_client_health_default_val(api, validator):
    try:
        assert is_valid_get_overall_client_health(
            validator,
            get_overall_client_health_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_client_proximity(json_schema_validate, obj):
    json_schema_validate('jsd_23c141467ea25ec0aa91cbcaff070354_v2_3_7_5').validate(obj)
    return True


def client_proximity(api):
    endpoint_result = api.clients.client_proximity(
        number_days=0,
        time_resolution=0,
        username='string'
    )
    return endpoint_result


@pytest.mark.clients
def test_client_proximity(api, validator):
    try:
        assert is_valid_client_proximity(
            validator,
            client_proximity(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def client_proximity_default_val(api):
    endpoint_result = api.clients.client_proximity(
        number_days=None,
        time_resolution=None,
        username=None
    )
    return endpoint_result


@pytest.mark.clients
def test_client_proximity_default_val(api, validator):
    try:
        assert is_valid_client_proximity(
            validator,
            client_proximity_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

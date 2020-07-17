# -*- coding: utf-8 -*-
"""DNACenterAPI clients API fixtures and tests.

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
import pytest
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.1.1', reason='version does not match')


def is_valid_get_overall_client_health(obj):
    json_schema_validate('jsd_149aa93b4ddb80dd_v2_1_1').validate(obj)
    return True


def get_overall_client_health(api):
    endpoint_result = api.clients.get_overall_client_health(
        timestamp=0
    )
    return endpoint_result


@pytest.mark.clients
def test_get_overall_client_health(api):
    assert is_valid_get_overall_client_health(
        get_overall_client_health(api)
    )


def get_overall_client_health_default(api):
    endpoint_result = api.clients.get_overall_client_health(
        timestamp=None
    )
    return endpoint_result


@pytest.mark.clients
def test_get_overall_client_health_default(api):
    try:
        assert is_valid_get_overall_client_health(
            get_overall_client_health_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_client_enrichment_details(obj):
    json_schema_validate('jsd_b199685d4d089a67_v2_1_1').validate(obj)
    return True


def get_client_enrichment_details(api):
    endpoint_result = api.clients.get_client_enrichment_details(

    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_enrichment_details(api):
    assert is_valid_get_client_enrichment_details(
        get_client_enrichment_details(api)
    )


def get_client_enrichment_details_default(api):
    endpoint_result = api.clients.get_client_enrichment_details(

    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_enrichment_details_default(api):
    try:
        assert is_valid_get_client_enrichment_details(
            get_client_enrichment_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_client_detail(obj):
    json_schema_validate('jsd_e2adba7943bab3e9_v2_1_1').validate(obj)
    return True


def get_client_detail(api):
    endpoint_result = api.clients.get_client_detail(
        mac_address='string',
        timestamp=0
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_detail(api):
    assert is_valid_get_client_detail(
        get_client_detail(api)
    )


def get_client_detail_default(api):
    endpoint_result = api.clients.get_client_detail(
        mac_address=None,
        timestamp=None
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_detail_default(api):
    try:
        assert is_valid_get_client_detail(
            get_client_detail_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

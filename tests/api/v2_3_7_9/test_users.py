# -*- coding: utf-8 -*-
"""CatalystCenterAPI users API fixtures and tests.

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
import pytest
from fastjsonschema.exceptions import JsonSchemaException
from dnacentersdk.exceptions import MalformedRequest
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.9', reason='version does not match')


def is_valid_get_user_enrichment_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_70f9c1d861a051b4a4928f2e6d84b2e3_v2_3_7_9').validate(obj)
    return True


def get_user_enrichment_details_v1(api):
    endpoint_result = api.users.get_user_enrichment_details_v1(

    )
    return endpoint_result


@pytest.mark.users
def test_get_user_enrichment_details_v1(api, validator):
    try:
        assert is_valid_get_user_enrichment_details_v1(
            validator,
            get_user_enrichment_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_user_enrichment_details_v1_default_val(api):
    endpoint_result = api.users.get_user_enrichment_details_v1(

    )
    return endpoint_result


@pytest.mark.users
def test_get_user_enrichment_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_user_enrichment_details_v1(
            validator,
            get_user_enrichment_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

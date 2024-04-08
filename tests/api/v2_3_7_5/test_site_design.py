# -*- coding: utf-8 -*-
"""DNACenterAPI site_design API fixtures and tests.

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


def is_valid_associate(json_schema_validate, obj):
    json_schema_validate('jsd_378a1800508058e4b82a08ea5637b794_v2_3_7_5').validate(obj)
    return True


def associate(api):
    endpoint_result = api.site_design.associate(
        active_validation=True,
        network_profile_id='string',
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_associate(api, validator):
    try:
        assert is_valid_associate(
            validator,
            associate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def associate_default_val(api):
    endpoint_result = api.site_design.associate(
        active_validation=True,
        network_profile_id='string',
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_associate_default_val(api, validator):
    try:
        assert is_valid_associate(
            validator,
            associate_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_disassociate(json_schema_validate, obj):
    json_schema_validate('jsd_21c8936d6a0c54e89b471fe36bf28de8_v2_3_7_5').validate(obj)
    return True


def disassociate(api):
    endpoint_result = api.site_design.disassociate(
        network_profile_id='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_disassociate(api, validator):
    try:
        assert is_valid_disassociate(
            validator,
            disassociate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def disassociate_default_val(api):
    endpoint_result = api.site_design.disassociate(
        network_profile_id='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_disassociate_default_val(api, validator):
    try:
        assert is_valid_disassociate(
            validator,
            disassociate_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

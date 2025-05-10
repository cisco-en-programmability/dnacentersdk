# -*- coding: utf-8 -*-
"""CatalystCenterAPI disaster_recovery API fixtures and tests.

Copyright (c) 2025 Cisco Systems.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '3.1.3.0', reason='version does not match')


def is_valid_disaster_recovery_operational_status_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b20622545922503da0c01b57c144f75b_v3_1_3_0').validate(obj)
    return True


def disaster_recovery_operational_status_v1(api):
    endpoint_result = api.disaster_recovery.disaster_recovery_operational_status_v1(

    )
    return endpoint_result


@pytest.mark.disaster_recovery
def test_disaster_recovery_operational_status_v1(api, validator):
    try:
        assert is_valid_disaster_recovery_operational_status_v1(
            validator,
            disaster_recovery_operational_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def disaster_recovery_operational_status_v1_default_val(api):
    endpoint_result = api.disaster_recovery.disaster_recovery_operational_status_v1(

    )
    return endpoint_result


@pytest.mark.disaster_recovery
def test_disaster_recovery_operational_status_v1_default_val(api, validator):
    try:
        assert is_valid_disaster_recovery_operational_status_v1(
            validator,
            disaster_recovery_operational_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_disaster_recovery_status_v1(json_schema_validate, obj):
    json_schema_validate('jsd_181b27ccd369519d8820de238483b865_v3_1_3_0').validate(obj)
    return True


def disaster_recovery_status_v1(api):
    endpoint_result = api.disaster_recovery.disaster_recovery_status_v1(

    )
    return endpoint_result


@pytest.mark.disaster_recovery
def test_disaster_recovery_status_v1(api, validator):
    try:
        assert is_valid_disaster_recovery_status_v1(
            validator,
            disaster_recovery_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def disaster_recovery_status_v1_default_val(api):
    endpoint_result = api.disaster_recovery.disaster_recovery_status_v1(

    )
    return endpoint_result


@pytest.mark.disaster_recovery
def test_disaster_recovery_status_v1_default_val(api, validator):
    try:
        assert is_valid_disaster_recovery_status_v1(
            validator,
            disaster_recovery_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

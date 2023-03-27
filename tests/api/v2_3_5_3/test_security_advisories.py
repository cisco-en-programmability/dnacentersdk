# -*- coding: utf-8 -*-
"""DNACenterAPI security_advisories API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.5.3', reason='version does not match')


def is_valid_get_advisories_list(json_schema_validate, obj):
    json_schema_validate('jsd_4e6317a46c835f0881f08071959bb026_v2_3_5_3').validate(obj)
    return True


def get_advisories_list(api):
    endpoint_result = api.security_advisories.get_advisories_list(

    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisories_list(api, validator):
    try:
        assert is_valid_get_advisories_list(
            validator,
            get_advisories_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_advisories_list_default_val(api):
    endpoint_result = api.security_advisories.get_advisories_list(

    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisories_list_default_val(api, validator):
    try:
        assert is_valid_get_advisories_list(
            validator,
            get_advisories_list_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_advisories_summary(json_schema_validate, obj):
    json_schema_validate('jsd_8947b24a5127510a8070b0f893494543_v2_3_5_3').validate(obj)
    return True


def get_advisories_summary(api):
    endpoint_result = api.security_advisories.get_advisories_summary(

    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisories_summary(api, validator):
    try:
        assert is_valid_get_advisories_summary(
            validator,
            get_advisories_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_advisories_summary_default_val(api):
    endpoint_result = api.security_advisories.get_advisories_summary(

    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisories_summary_default_val(api, validator):
    try:
        assert is_valid_get_advisories_summary(
            validator,
            get_advisories_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_devices_per_advisory(json_schema_validate, obj):
    json_schema_validate('jsd_cbdf8887b29b5f0ea87113d2ae17d6df_v2_3_5_3').validate(obj)
    return True


def get_devices_per_advisory(api):
    endpoint_result = api.security_advisories.get_devices_per_advisory(
        advisory_id='string'
    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_devices_per_advisory(api, validator):
    try:
        assert is_valid_get_devices_per_advisory(
            validator,
            get_devices_per_advisory(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_devices_per_advisory_default_val(api):
    endpoint_result = api.security_advisories.get_devices_per_advisory(
        advisory_id='string'
    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_devices_per_advisory_default_val(api, validator):
    try:
        assert is_valid_get_devices_per_advisory(
            validator,
            get_devices_per_advisory_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_advisory_ids_per_device(json_schema_validate, obj):
    json_schema_validate('jsd_34b1c03688485b44b1547c428a887c5d_v2_3_5_3').validate(obj)
    return True


def get_advisory_ids_per_device(api):
    endpoint_result = api.security_advisories.get_advisory_ids_per_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisory_ids_per_device(api, validator):
    try:
        assert is_valid_get_advisory_ids_per_device(
            validator,
            get_advisory_ids_per_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_advisory_ids_per_device_default_val(api):
    endpoint_result = api.security_advisories.get_advisory_ids_per_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisory_ids_per_device_default_val(api, validator):
    try:
        assert is_valid_get_advisory_ids_per_device(
            validator,
            get_advisory_ids_per_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_advisories_per_device(json_schema_validate, obj):
    json_schema_validate('jsd_7cf75923b0c6575ead874f9d404d7355_v2_3_5_3').validate(obj)
    return True


def get_advisories_per_device(api):
    endpoint_result = api.security_advisories.get_advisories_per_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisories_per_device(api, validator):
    try:
        assert is_valid_get_advisories_per_device(
            validator,
            get_advisories_per_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_advisories_per_device_default_val(api):
    endpoint_result = api.security_advisories.get_advisories_per_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisories_per_device_default_val(api, validator):
    try:
        assert is_valid_get_advisories_per_device(
            validator,
            get_advisories_per_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI eox API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.6', reason='version does not match')


def is_valid_get_eox_status_for_all_devices(json_schema_validate, obj):
    json_schema_validate('jsd_64d5d27a53ac53258fa2183b7e93a7d5_v2_3_7_6').validate(obj)
    return True


def get_eox_status_for_all_devices(api):
    endpoint_result = api.eox.get_eox_status_for_all_devices(

    )
    return endpoint_result


@pytest.mark.eox
def test_get_eox_status_for_all_devices(api, validator):
    try:
        assert is_valid_get_eox_status_for_all_devices(
            validator,
            get_eox_status_for_all_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_eox_status_for_all_devices_default_val(api):
    endpoint_result = api.eox.get_eox_status_for_all_devices(

    )
    return endpoint_result


@pytest.mark.eox
def test_get_eox_status_for_all_devices_default_val(api, validator):
    try:
        assert is_valid_get_eox_status_for_all_devices(
            validator,
            get_eox_status_for_all_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_eox_details_per_device(json_schema_validate, obj):
    json_schema_validate('jsd_816ec048832853f8a63f34415d0e6fce_v2_3_7_6').validate(obj)
    return True


def get_eox_details_per_device(api):
    endpoint_result = api.eox.get_eox_details_per_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.eox
def test_get_eox_details_per_device(api, validator):
    try:
        assert is_valid_get_eox_details_per_device(
            validator,
            get_eox_details_per_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_eox_details_per_device_default_val(api):
    endpoint_result = api.eox.get_eox_details_per_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.eox
def test_get_eox_details_per_device_default_val(api, validator):
    try:
        assert is_valid_get_eox_details_per_device(
            validator,
            get_eox_details_per_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_eox_summary(json_schema_validate, obj):
    json_schema_validate('jsd_f0a0dfdaca465bdc91fc290d87476b89_v2_3_7_6').validate(obj)
    return True


def get_eox_summary(api):
    endpoint_result = api.eox.get_eox_summary(

    )
    return endpoint_result


@pytest.mark.eox
def test_get_eox_summary(api, validator):
    try:
        assert is_valid_get_eox_summary(
            validator,
            get_eox_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_eox_summary_default_val(api):
    endpoint_result = api.eox.get_eox_summary(

    )
    return endpoint_result


@pytest.mark.eox
def test_get_eox_summary_default_val(api, validator):
    try:
        assert is_valid_get_eox_summary(
            validator,
            get_eox_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

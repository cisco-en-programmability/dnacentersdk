# -*- coding: utf-8 -*-
"""DNACenterAPI device_replacement API fixtures and tests.

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


def is_valid_return_replacement_devices_with_details(json_schema_validate, obj):
    json_schema_validate('jsd_e89f8ba4965853b3a075c7401c564477_v2_3_7_6').validate(obj)
    return True


def return_replacement_devices_with_details(api):
    endpoint_result = api.device_replacement.return_replacement_devices_with_details(
        family='value1,value2',
        faulty_device_name='string',
        faulty_device_platform='string',
        faulty_device_serial_number='string',
        limit=0,
        offset=0,
        replacement_device_platform='string',
        replacement_device_serial_number='string',
        replacement_status='value1,value2',
        sort_by='string',
        sort_order='string'
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_return_replacement_devices_with_details(api, validator):
    try:
        assert is_valid_return_replacement_devices_with_details(
            validator,
            return_replacement_devices_with_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def return_replacement_devices_with_details_default_val(api):
    endpoint_result = api.device_replacement.return_replacement_devices_with_details(
        family=None,
        faulty_device_name=None,
        faulty_device_platform=None,
        faulty_device_serial_number=None,
        limit=None,
        offset=None,
        replacement_device_platform=None,
        replacement_device_serial_number=None,
        replacement_status=None,
        sort_by=None,
        sort_order=None
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_return_replacement_devices_with_details_default_val(api, validator):
    try:
        assert is_valid_return_replacement_devices_with_details(
            validator,
            return_replacement_devices_with_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_unmark_device_for_replacement(json_schema_validate, obj):
    json_schema_validate('jsd_2b60f9f312235959812d49dc4c469e83_v2_3_7_6').validate(obj)
    return True


def unmark_device_for_replacement(api):
    endpoint_result = api.device_replacement.unmark_device_for_replacement(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_unmark_device_for_replacement(api, validator):
    try:
        assert is_valid_unmark_device_for_replacement(
            validator,
            unmark_device_for_replacement(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def unmark_device_for_replacement_default_val(api):
    endpoint_result = api.device_replacement.unmark_device_for_replacement(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_unmark_device_for_replacement_default_val(api, validator):
    try:
        assert is_valid_unmark_device_for_replacement(
            validator,
            unmark_device_for_replacement_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_mark_device_for_replacement(json_schema_validate, obj):
    json_schema_validate('jsd_ac6e63199fb05bcf89106a22502c2197_v2_3_7_6').validate(obj)
    return True


def mark_device_for_replacement(api):
    endpoint_result = api.device_replacement.mark_device_for_replacement(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_mark_device_for_replacement(api, validator):
    try:
        assert is_valid_mark_device_for_replacement(
            validator,
            mark_device_for_replacement(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def mark_device_for_replacement_default_val(api):
    endpoint_result = api.device_replacement.mark_device_for_replacement(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_mark_device_for_replacement_default_val(api, validator):
    try:
        assert is_valid_mark_device_for_replacement(
            validator,
            mark_device_for_replacement_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_return_replacement_devices_count(json_schema_validate, obj):
    json_schema_validate('jsd_c2b2882c8fb65284bfc9d781e9ddd07f_v2_3_7_6').validate(obj)
    return True


def return_replacement_devices_count(api):
    endpoint_result = api.device_replacement.return_replacement_devices_count(
        replacement_status='value1,value2'
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_return_replacement_devices_count(api, validator):
    try:
        assert is_valid_return_replacement_devices_count(
            validator,
            return_replacement_devices_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def return_replacement_devices_count_default_val(api):
    endpoint_result = api.device_replacement.return_replacement_devices_count(
        replacement_status=None
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_return_replacement_devices_count_default_val(api, validator):
    try:
        assert is_valid_return_replacement_devices_count(
            validator,
            return_replacement_devices_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_device_replacement_workflow(json_schema_validate, obj):
    json_schema_validate('jsd_19f256e33af7501a8bdae2742ca9f6d6_v2_3_7_6').validate(obj)
    return True


def deploy_device_replacement_workflow(api):
    endpoint_result = api.device_replacement.deploy_device_replacement_workflow(
        active_validation=True,
        faultyDeviceSerialNumber='string',
        payload=None,
        replacementDeviceSerialNumber='string'
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_deploy_device_replacement_workflow(api, validator):
    try:
        assert is_valid_deploy_device_replacement_workflow(
            validator,
            deploy_device_replacement_workflow(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_device_replacement_workflow_default_val(api):
    endpoint_result = api.device_replacement.deploy_device_replacement_workflow(
        active_validation=True,
        faultyDeviceSerialNumber=None,
        payload=None,
        replacementDeviceSerialNumber=None
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_deploy_device_replacement_workflow_default_val(api, validator):
    try:
        assert is_valid_deploy_device_replacement_workflow(
            validator,
            deploy_device_replacement_workflow_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

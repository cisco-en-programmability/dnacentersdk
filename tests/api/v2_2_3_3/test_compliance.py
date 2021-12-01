# -*- coding: utf-8 -*-
"""DNACenterAPI compliance API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.3.3', reason='version does not match')


def is_valid_get_compliance_status(json_schema_validate, obj):
    json_schema_validate('jsd_4a1de7ff46fa5da09c5051c06ad07f2c_v2_2_3_3').validate(obj)
    return True


def get_compliance_status(api):
    endpoint_result = api.compliance.get_compliance_status(
        compliance_status='string',
        device_uuid='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status(api, validator):
    try:
        assert is_valid_get_compliance_status(
            validator,
            get_compliance_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_compliance_status_default_val(api):
    endpoint_result = api.compliance.get_compliance_status(
        compliance_status=None,
        device_uuid=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status_default_val(api, validator):
    try:
        assert is_valid_get_compliance_status(
            validator,
            get_compliance_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_run_compliance(json_schema_validate, obj):
    json_schema_validate('jsd_0802306a0a8d545698d1d59a9be90e51_v2_2_3_3').validate(obj)
    return True


def run_compliance(api):
    endpoint_result = api.compliance.run_compliance(
        active_validation=True,
        categories=['string'],
        deviceUuids=['string'],
        payload=None,
        triggerFull=True
    )
    return endpoint_result


@pytest.mark.compliance
def test_run_compliance(api, validator):
    try:
        assert is_valid_run_compliance(
            validator,
            run_compliance(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def run_compliance_default_val(api):
    endpoint_result = api.compliance.run_compliance(
        active_validation=True,
        categories=None,
        deviceUuids=None,
        payload=None,
        triggerFull=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_run_compliance_default_val(api, validator):
    try:
        assert is_valid_run_compliance(
            validator,
            run_compliance_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_compliance_status_count(json_schema_validate, obj):
    json_schema_validate('jsd_079c37ce8136584f9e2ed471fc896ef9_v2_2_3_3').validate(obj)
    return True


def get_compliance_status_count(api):
    endpoint_result = api.compliance.get_compliance_status_count(
        compliance_status='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status_count(api, validator):
    try:
        assert is_valid_get_compliance_status_count(
            validator,
            get_compliance_status_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_compliance_status_count_default_val(api):
    endpoint_result = api.compliance.get_compliance_status_count(
        compliance_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status_count_default_val(api, validator):
    try:
        assert is_valid_get_compliance_status_count(
            validator,
            get_compliance_status_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_compliance_detail(json_schema_validate, obj):
    json_schema_validate('jsd_6395adeaeb8157da972efb7b91e1e2cb_v2_2_3_3').validate(obj)
    return True


def get_compliance_detail(api):
    endpoint_result = api.compliance.get_compliance_detail(
        compliance_status='string',
        compliance_type='string',
        device_uuid='string',
        limit='string',
        offset='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_detail(api, validator):
    try:
        assert is_valid_get_compliance_detail(
            validator,
            get_compliance_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_compliance_detail_default_val(api):
    endpoint_result = api.compliance.get_compliance_detail(
        compliance_status=None,
        compliance_type=None,
        device_uuid=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_detail_default_val(api, validator):
    try:
        assert is_valid_get_compliance_detail(
            validator,
            get_compliance_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_compliance_detail_count(json_schema_validate, obj):
    json_schema_validate('jsd_d3d38fed534f5aeaa80f5a8c63694708_v2_2_3_3').validate(obj)
    return True


def get_compliance_detail_count(api):
    endpoint_result = api.compliance.get_compliance_detail_count(
        compliance_status='string',
        compliance_type='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_detail_count(api, validator):
    try:
        assert is_valid_get_compliance_detail_count(
            validator,
            get_compliance_detail_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_compliance_detail_count_default_val(api):
    endpoint_result = api.compliance.get_compliance_detail_count(
        compliance_status=None,
        compliance_type=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_detail_count_default_val(api, validator):
    try:
        assert is_valid_get_compliance_detail_count(
            validator,
            get_compliance_detail_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_device_compliance_status(json_schema_validate, obj):
    json_schema_validate('jsd_41da8e5cdd435db0b1da1684be8f15b8_v2_2_3_3').validate(obj)
    return True


def device_compliance_status(api):
    endpoint_result = api.compliance.device_compliance_status(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_device_compliance_status(api, validator):
    try:
        assert is_valid_device_compliance_status(
            validator,
            device_compliance_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_compliance_status_default_val(api):
    endpoint_result = api.compliance.device_compliance_status(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_device_compliance_status_default_val(api, validator):
    try:
        assert is_valid_device_compliance_status(
            validator,
            device_compliance_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_compliance_details_of_device(json_schema_validate, obj):
    json_schema_validate('jsd_90b70e1b6a2f51a59690669a4b2fd3f0_v2_2_3_3').validate(obj)
    return True


def compliance_details_of_device(api):
    endpoint_result = api.compliance.compliance_details_of_device(
        category='string',
        compliance_type='string',
        device_uuid='string',
        diff_list=True,
        key='string',
        value='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_compliance_details_of_device(api, validator):
    try:
        assert is_valid_compliance_details_of_device(
            validator,
            compliance_details_of_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def compliance_details_of_device_default_val(api):
    endpoint_result = api.compliance.compliance_details_of_device(
        category=None,
        compliance_type=None,
        device_uuid='string',
        diff_list=None,
        key=None,
        value=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_compliance_details_of_device_default_val(api, validator):
    try:
        assert is_valid_compliance_details_of_device(
            validator,
            compliance_details_of_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI compliance API fixtures and tests.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.1', reason='version does not match')


def is_valid_compliance_details_of_device(json_schema_validate, obj):
    json_schema_validate('jsd_52bfe90445aab017_v2_2_1').validate(obj)
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
    assert is_valid_compliance_details_of_device(
        validator,
        compliance_details_of_device(api)
    )


def compliance_details_of_device_default(api):
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
def test_compliance_details_of_device_default(api, validator):
    try:
        assert is_valid_compliance_details_of_device(
            validator,
            compliance_details_of_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_device_compliance_status(json_schema_validate, obj):
    json_schema_validate('jsd_7aa85ad548ea94a7_v2_2_1').validate(obj)
    return True


def device_compliance_status(api):
    endpoint_result = api.compliance.device_compliance_status(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_device_compliance_status(api, validator):
    assert is_valid_device_compliance_status(
        validator,
        device_compliance_status(api)
    )


def device_compliance_status_default(api):
    endpoint_result = api.compliance.device_compliance_status(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_device_compliance_status_default(api, validator):
    try:
        assert is_valid_device_compliance_status(
            validator,
            device_compliance_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_compliance_status_(json_schema_validate, obj):
    json_schema_validate('jsd_dda5cb9a49aaaef6_v2_2_1').validate(obj)
    return True


def get_compliance_status_(api):
    endpoint_result = api.compliance.get_compliance_status_(
        compliance_status='string',
        device_uuid='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status_(api, validator):
    assert is_valid_get_compliance_status_(
        validator,
        get_compliance_status_(api)
    )


def get_compliance_status__default(api):
    endpoint_result = api.compliance.get_compliance_status_(
        compliance_status=None,
        device_uuid=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status__default(api, validator):
    try:
        assert is_valid_get_compliance_status_(
            validator,
            get_compliance_status__default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_run_compliance(json_schema_validate, obj):
    json_schema_validate('jsd_f6aec8a74428a9ff_v2_2_1').validate(obj)
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
    assert is_valid_run_compliance(
        validator,
        run_compliance(api)
    )


def run_compliance_default(api):
    endpoint_result = api.compliance.run_compliance(
        active_validation=True,
        categories=None,
        deviceUuids=None,
        payload=None,
        triggerFull=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_run_compliance_default(api, validator):
    try:
        assert is_valid_run_compliance(
            validator,
            run_compliance_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

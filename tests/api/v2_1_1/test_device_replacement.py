# -*- coding: utf-8 -*-
"""DNACenterAPI device_replacement API fixtures and tests.

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


def is_valid_deploy_device_replacement_workflow(obj):
    json_schema_validate('jsd_3faaa9944b49bc9f_v2_1_1').validate(obj)
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
def test_deploy_device_replacement_workflow(api):
    assert is_valid_deploy_device_replacement_workflow(
        deploy_device_replacement_workflow(api)
    )


def deploy_device_replacement_workflow_default(api):
    endpoint_result = api.device_replacement.deploy_device_replacement_workflow(
        active_validation=True,
        faultyDeviceSerialNumber=None,
        payload=None,
        replacementDeviceSerialNumber=None
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_deploy_device_replacement_workflow_default(api):
    try:
        assert is_valid_deploy_device_replacement_workflow(
            deploy_device_replacement_workflow_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_unmark_device_for_replacement(obj):
    json_schema_validate('jsd_4ababa75489ab24b_v2_1_1').validate(obj)
    return True


def unmark_device_for_replacement(api):
    endpoint_result = api.device_replacement.unmark_device_for_replacement(
        active_validation=True,
        payload=[{'creationTime': 0, 'family': 'string', 'faultyDeviceId': 'string', 'faultyDeviceName': 'string', 'faultyDevicePlatform': 'string', 'faultyDeviceSerialNumber': 'string', 'id': 'string', 'neighbourDeviceId': 'string', 'networkReadinessTaskId': 'string', 'replacementDevicePlatform': 'string', 'replacementDeviceSerialNumber': 'string', 'replacementStatus': 'string', 'replacementTime': 0, 'workflowId': 'string'}]
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_unmark_device_for_replacement(api):
    assert is_valid_unmark_device_for_replacement(
        unmark_device_for_replacement(api)
    )


def unmark_device_for_replacement_default(api):
    endpoint_result = api.device_replacement.unmark_device_for_replacement(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_unmark_device_for_replacement_default(api):
    try:
        assert is_valid_unmark_device_for_replacement(
            unmark_device_for_replacement_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_mark_device_for_replacement(obj):
    json_schema_validate('jsd_64b9dad0403aaca1_v2_1_1').validate(obj)
    return True


def mark_device_for_replacement(api):
    endpoint_result = api.device_replacement.mark_device_for_replacement(
        active_validation=True,
        payload=[{'creationTime': 0, 'family': 'string', 'faultyDeviceId': 'string', 'faultyDeviceName': 'string', 'faultyDevicePlatform': 'string', 'faultyDeviceSerialNumber': 'string', 'id': 'string', 'neighbourDeviceId': 'string', 'networkReadinessTaskId': 'string', 'replacementDevicePlatform': 'string', 'replacementDeviceSerialNumber': 'string', 'replacementStatus': 'string', 'replacementTime': 0, 'workflowId': 'string'}]
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_mark_device_for_replacement(api):
    assert is_valid_mark_device_for_replacement(
        mark_device_for_replacement(api)
    )


def mark_device_for_replacement_default(api):
    endpoint_result = api.device_replacement.mark_device_for_replacement(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_mark_device_for_replacement_default(api):
    try:
        assert is_valid_mark_device_for_replacement(
            mark_device_for_replacement_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_return_replacement_devices_with_details(obj):
    json_schema_validate('jsd_809c29564bc997d0_v2_1_1').validate(obj)
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
def test_return_replacement_devices_with_details(api):
    assert is_valid_return_replacement_devices_with_details(
        return_replacement_devices_with_details(api)
    )


def return_replacement_devices_with_details_default(api):
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
def test_return_replacement_devices_with_details_default(api):
    try:
        assert is_valid_return_replacement_devices_with_details(
            return_replacement_devices_with_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_return_replacement_devices_count(obj):
    json_schema_validate('jsd_9eb84ba54929a2a2_v2_1_1').validate(obj)
    return True


def return_replacement_devices_count(api):
    endpoint_result = api.device_replacement.return_replacement_devices_count(
        replacement_status='value1,value2'
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_return_replacement_devices_count(api):
    assert is_valid_return_replacement_devices_count(
        return_replacement_devices_count(api)
    )


def return_replacement_devices_count_default(api):
    endpoint_result = api.device_replacement.return_replacement_devices_count(
        replacement_status=None
    )
    return endpoint_result


@pytest.mark.device_replacement
def test_return_replacement_devices_count_default(api):
    try:
        assert is_valid_return_replacement_devices_count(
            return_replacement_devices_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

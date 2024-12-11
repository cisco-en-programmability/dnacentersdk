# -*- coding: utf-8 -*-
"""CatalystCenterAPI path_trace API fixtures and tests.

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


def is_valid_retrieves_all_previous_pathtraces_summary_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a75e4b27171c5c6782e84f902da9e5be_v2_3_7_9').validate(obj)
    return True


def retrieves_all_previous_pathtraces_summary_v1(api):
    endpoint_result = api.path_trace.retrieves_all_previous_pathtraces_summary_v1(
        dest_ip='string',
        dest_port=0,
        gt_create_time=0,
        last_update_time=0,
        limit=0,
        lt_create_time=0,
        offset=0,
        order='string',
        periodic_refresh=True,
        protocol='string',
        sort_by='string',
        source_ip='string',
        source_port=0,
        status='string',
        task_id='string'
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_all_previous_pathtraces_summary_v1(api, validator):
    try:
        assert is_valid_retrieves_all_previous_pathtraces_summary_v1(
            validator,
            retrieves_all_previous_pathtraces_summary_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_all_previous_pathtraces_summary_v1_default_val(api):
    endpoint_result = api.path_trace.retrieves_all_previous_pathtraces_summary_v1(
        dest_ip=None,
        dest_port=None,
        gt_create_time=None,
        last_update_time=None,
        limit=None,
        lt_create_time=None,
        offset=None,
        order=None,
        periodic_refresh=None,
        protocol=None,
        sort_by=None,
        source_ip=None,
        source_port=None,
        status=None,
        task_id=None
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_all_previous_pathtraces_summary_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_all_previous_pathtraces_summary_v1(
            validator,
            retrieves_all_previous_pathtraces_summary_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_initiate_a_new_pathtrace_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a54fce1a0c305bdabfe91a8a6161e539_v2_3_7_9').validate(obj)
    return True


def initiate_a_new_pathtrace_v1(api):
    endpoint_result = api.path_trace.initiate_a_new_pathtrace_v1(
        active_validation=True,
        controlPath=True,
        destIP='string',
        destPort='string',
        inclusions=['string'],
        payload=None,
        periodicRefresh=True,
        protocol='string',
        sourceIP='string',
        sourcePort='string'
    )
    return endpoint_result


@pytest.mark.path_trace
def test_initiate_a_new_pathtrace_v1(api, validator):
    try:
        assert is_valid_initiate_a_new_pathtrace_v1(
            validator,
            initiate_a_new_pathtrace_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def initiate_a_new_pathtrace_v1_default_val(api):
    endpoint_result = api.path_trace.initiate_a_new_pathtrace_v1(
        active_validation=True,
        controlPath=None,
        destIP=None,
        destPort=None,
        inclusions=None,
        payload=None,
        periodicRefresh=None,
        protocol=None,
        sourceIP=None,
        sourcePort=None
    )
    return endpoint_result


@pytest.mark.path_trace
def test_initiate_a_new_pathtrace_v1_default_val(api, validator):
    try:
        assert is_valid_initiate_a_new_pathtrace_v1(
            validator,
            initiate_a_new_pathtrace_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_previous_pathtrace_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ed5cbafc332a5efa97547736ba8b6044_v2_3_7_9').validate(obj)
    return True


def retrieves_previous_pathtrace_v1(api):
    endpoint_result = api.path_trace.retrieves_previous_pathtrace_v1(
        flow_analysis_id='string'
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_previous_pathtrace_v1(api, validator):
    try:
        assert is_valid_retrieves_previous_pathtrace_v1(
            validator,
            retrieves_previous_pathtrace_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_previous_pathtrace_v1_default_val(api):
    endpoint_result = api.path_trace.retrieves_previous_pathtrace_v1(
        flow_analysis_id='string'
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_previous_pathtrace_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_previous_pathtrace_v1(
            validator,
            retrieves_previous_pathtrace_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_pathtrace_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8a7ae984f943507ba621abe155e6e744_v2_3_7_9').validate(obj)
    return True


def deletes_pathtrace_by_id_v1(api):
    endpoint_result = api.path_trace.deletes_pathtrace_by_id_v1(
        flow_analysis_id='string'
    )
    return endpoint_result


@pytest.mark.path_trace
def test_deletes_pathtrace_by_id_v1(api, validator):
    try:
        assert is_valid_deletes_pathtrace_by_id_v1(
            validator,
            deletes_pathtrace_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_pathtrace_by_id_v1_default_val(api):
    endpoint_result = api.path_trace.deletes_pathtrace_by_id_v1(
        flow_analysis_id='string'
    )
    return endpoint_result


@pytest.mark.path_trace
def test_deletes_pathtrace_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_deletes_pathtrace_by_id_v1(
            validator,
            deletes_pathtrace_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

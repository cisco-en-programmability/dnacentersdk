# -*- coding: utf-8 -*-
"""DNACenterAPI path_trace API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.1', reason='version does not match')


def is_valid_deletes_pathtrace_by_id(obj):
    json_schema_validate('jsd_8a9d2b76443b914e_v1_3_1').validate(obj)
    return True


def deletes_pathtrace_by_id(api):
    endpoint_result = api.path_trace.deletes_pathtrace_by_id(
        flow_analysis_id='string'
    )
    return endpoint_result


@pytest.mark.path_trace
def test_deletes_pathtrace_by_id(api):
    assert is_valid_deletes_pathtrace_by_id(
        deletes_pathtrace_by_id(api)
    )


def deletes_pathtrace_by_id_default(api):
    endpoint_result = api.path_trace.deletes_pathtrace_by_id(
        flow_analysis_id='string'
    )
    return endpoint_result


@pytest.mark.path_trace
def test_deletes_pathtrace_by_id_default(api):
    try:
        assert is_valid_deletes_pathtrace_by_id(
            deletes_pathtrace_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_retrieves_previous_pathtrace(obj):
    json_schema_validate('jsd_7ab9a8bd4f3b86a4_v1_3_1').validate(obj)
    return True


def retrieves_previous_pathtrace(api):
    endpoint_result = api.path_trace.retrieves_previous_pathtrace(
        flow_analysis_id='string'
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_previous_pathtrace(api):
    assert is_valid_retrieves_previous_pathtrace(
        retrieves_previous_pathtrace(api)
    )


def retrieves_previous_pathtrace_default(api):
    endpoint_result = api.path_trace.retrieves_previous_pathtrace(
        flow_analysis_id='string'
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_previous_pathtrace_default(api):
    try:
        assert is_valid_retrieves_previous_pathtrace(
            retrieves_previous_pathtrace_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_retrives_all_previous_pathtraces_summary(obj):
    json_schema_validate('jsd_55bc3bf94e38b6ff_v1_3_1').validate(obj)
    return True


def retrives_all_previous_pathtraces_summary(api):
    endpoint_result = api.path_trace.retrives_all_previous_pathtraces_summary(
        dest_ip='string',
        dest_port='string',
        gt_create_time='string',
        last_update_time='string',
        limit='string',
        lt_create_time='string',
        offset='string',
        order='string',
        periodic_refresh=True,
        protocol='string',
        sort_by='string',
        source_ip='string',
        source_port='string',
        status='string',
        task_id='string'
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrives_all_previous_pathtraces_summary(api):
    assert is_valid_retrives_all_previous_pathtraces_summary(
        retrives_all_previous_pathtraces_summary(api)
    )


def retrives_all_previous_pathtraces_summary_default(api):
    endpoint_result = api.path_trace.retrives_all_previous_pathtraces_summary(
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
def test_retrives_all_previous_pathtraces_summary_default(api):
    try:
        assert is_valid_retrives_all_previous_pathtraces_summary(
            retrives_all_previous_pathtraces_summary_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_initiate_a_new_pathtrace(obj):
    json_schema_validate('jsd_a395fae644ca899c_v1_3_1').validate(obj)
    return True


def initiate_a_new_pathtrace(api):
    endpoint_result = api.path_trace.initiate_a_new_pathtrace(
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
def test_initiate_a_new_pathtrace(api):
    assert is_valid_initiate_a_new_pathtrace(
        initiate_a_new_pathtrace(api)
    )


def initiate_a_new_pathtrace_default(api):
    endpoint_result = api.path_trace.initiate_a_new_pathtrace(
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
def test_initiate_a_new_pathtrace_default(api):
    try:
        assert is_valid_initiate_a_new_pathtrace(
            initiate_a_new_pathtrace_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

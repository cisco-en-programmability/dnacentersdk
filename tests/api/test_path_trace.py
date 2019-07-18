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
import dnacentersdk
import calendar
import time
from tests.config import PATH_TRACE_SOURCE_IP, PATH_TRACE_DEST_IP


def is_valid_initiate_a_new_pathtrace(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def initiate_a_new_pathtrace(api):
    endpoint_result = api.path_trace.initiate_a_new_pathtrace(
        controlPath=None,
        destIP=PATH_TRACE_DEST_IP,
        destPort=None,
        inclusions=None,
        periodicRefresh=None,
        protocol=None,
        sourceIP=PATH_TRACE_SOURCE_IP,
        sourcePort=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([PATH_TRACE_SOURCE_IP, PATH_TRACE_DEST_IP]) is True,
                    reason="tests.config values required not present")
def test_initiate_a_new_pathtrace(api):
    assert is_valid_initiate_a_new_pathtrace(
        initiate_a_new_pathtrace(api)
    )


def is_valid_deletes_pathtrace_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def deletes_pathtrace_by_id(api):
    endpoint_result = api.path_trace.deletes_pathtrace_by_id(
        flow_analysis_id=retrives_all_previous_pathtraces_summary(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_deletes_pathtrace_by_id(api):
    assert is_valid_deletes_pathtrace_by_id(
        deletes_pathtrace_by_id(api)
    )


def is_valid_retrieves_previous_pathtrace(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def retrieves_previous_pathtrace(api):
    endpoint_result = api.path_trace.retrieves_previous_pathtrace(
        flow_analysis_id=initiate_a_new_pathtrace(api).response.flowAnalysisId,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_retrieves_previous_pathtrace(api):
    assert is_valid_retrieves_previous_pathtrace(
        retrieves_previous_pathtrace(api)
    )


def is_valid_retrives_all_previous_pathtraces_summary(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def retrives_all_previous_pathtraces_summary(api):
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
        source_ip=PATH_TRACE_SOURCE_IP,
        source_port=None,
        status=None,
        task_id=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([PATH_TRACE_SOURCE_IP]) is True,
                    reason="tests.config values required not present")
def test_retrives_all_previous_pathtraces_summary(api):
    assert is_valid_retrives_all_previous_pathtraces_summary(
        retrives_all_previous_pathtraces_summary(api)
    )

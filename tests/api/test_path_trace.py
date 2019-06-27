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




# a395-fae6-44ca-899c
def is_valid_initiate_a_new_pathtrace(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def initiate_a_new_pathtrace(api):
    endpoint_result = api.path_trace.initiate_a_new_pathtrace( rq_controlPath = None, rq_destIP = '10.10.22.114', rq_destPort = None, rq_inclusions = None, rq_periodicRefresh = None, rq_protocol = None, rq_sourceIP = '10.10.22.98', rq_sourcePort = None, payload = '' )
    return endpoint_result


def test_initiate_a_new_pathtrace(api):
    assert is_valid_initiate_a_new_pathtrace(initiate_a_new_pathtrace(api))


# 8a9d-2b76-443b-914e
def is_valid_deletes_pathtrace_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def deletes_pathtrace_by_id(api):
    endpoint_result = api.path_trace.deletes_pathtrace_by_id( path_param_flow_analysis_id = retrives_all_previous_pathtraces_summary(api).response[0].id, payload = '' )
    return endpoint_result


def test_deletes_pathtrace_by_id(api):
    assert is_valid_deletes_pathtrace_by_id(deletes_pathtrace_by_id(api))


# 7ab9-a8bd-4f3b-86a4
def is_valid_retrieves_previous_pathtrace(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def retrieves_previous_pathtrace(api):
    endpoint_result = api.path_trace.retrieves_previous_pathtrace( path_param_flow_analysis_id = initiate_a_new_pathtrace(api).response.flowAnalysisId, payload = '' )
    return endpoint_result


def test_retrieves_previous_pathtrace(api):
    assert is_valid_retrieves_previous_pathtrace(retrieves_previous_pathtrace(api))


# 55bc-3bf9-4e38-b6ff
def is_valid_retrives_all_previous_pathtraces_summary(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def retrives_all_previous_pathtraces_summary(api):
    endpoint_result = api.path_trace.retrives_all_previous_pathtraces_summary( param_dest_ip = None, param_dest_port = None, param_gt_create_time = None, param_last_update_time = None, param_limit = None, param_lt_create_time = None, param_offset = None, param_order = None, param_periodic_refresh = None, param_protocol = None, param_sort_by = None, param_source_ip = '10.10.22.98', param_source_port = None, param_status = None, param_task_id = None, payload = '' )
    return endpoint_result


def test_retrives_all_previous_pathtraces_summary(api):
    assert is_valid_retrives_all_previous_pathtraces_summary(retrives_all_previous_pathtraces_summary(api))


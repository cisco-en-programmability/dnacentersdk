# -*- coding: utf-8 -*-
"""DNACenterAPI task API fixtures and tests.

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




# e78b-b8a2-449b-9eed
def is_valid_get_tasks(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_tasks(api):
    endpoint_result = api.task.get_tasks( param_data = None, param_end_time = None, param_error_code = None, param_failure_reason = None, param_is_error = None, param_limit = None, param_offset = None, param_order = None, param_parent_id = None, param_progress = None, param_service_type = None, param_sort_by = None, param_start_time = None, param_username = None, payload = '' )
    return endpoint_result


def test_get_tasks(api):
    assert is_valid_get_tasks(get_tasks(api))


# f5a2-69c4-4f2a-95fa
def is_valid_get_task_tree(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_task_tree(api):
    endpoint_result = api.task.get_task_tree( path_param_task_id = get_tasks(api).response[0].id, payload = '' )
    return endpoint_result


def test_get_task_tree(api):
    assert is_valid_get_task_tree(get_task_tree(api))


# 26b4-4ab0-4649-a183
def is_valid_get_task_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_task_count(api):
    endpoint_result = api.task.get_task_count( param_data = None, param_end_time = None, param_error_code = None, param_failure_reason = None, param_is_error = None, param_parent_id = None, param_progress = None, param_service_type = None, param_start_time = None, param_username = None, payload = '' )
    return endpoint_result


def test_get_task_count(api):
    assert is_valid_get_task_count(get_task_count(api))


# a1a9-3873-46ba-92b1
def is_valid_get_task_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_task_by_id(api):
    endpoint_result = api.task.get_task_by_id( path_param_task_id = get_tasks(api).response[0].id, payload = '' )
    return endpoint_result


def test_get_task_by_id(api):
    assert is_valid_get_task_by_id(get_task_by_id(api))


# e487-f8d3-481b-94f2
def is_valid_get_task_by_operationid(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_task_by_operationid(api):
    endpoint_result = api.task.get_task_by_operationid( path_param_limit = 2, path_param_offset = 1, path_param_operation_id = list(filter(lambda x: x.operationIdList is not None, get_tasks(api).response))[0].operationIdList[0], payload = '' )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_task_by_operationid(api):
    assert is_valid_get_task_by_operationid(get_task_by_operationid(api))


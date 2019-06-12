# task

import pytest
import dnacentersdk


def is_valid_get_task_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_task_count(api):
    endpoint_result = api.task.get_task_count( param_data = None, param_end_time = None, param_error_code = None, param_failure_reason = None, param_is_error = None, param_parent_id = None, param_progress = None, param_service_type = None, param_start_time = None, param_username = None)
    assert is_valid_get_task_count(endpoint_result)


def is_valid_get_task_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_task_by_id(api):
    endpoint_result = api.task.get_task_by_id( path_param_task_id = '')
    assert is_valid_get_task_by_id(endpoint_result)


def is_valid_get_tasks(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_tasks(api):
    endpoint_result = api.task.get_tasks( param_data = None, param_end_time = None, param_error_code = None, param_failure_reason = None, param_is_error = None, param_limit = None, param_offset = None, param_order = None, param_parent_id = None, param_progress = None, param_service_type = None, param_sort_by = None, param_start_time = None, param_username = None)
    assert is_valid_get_tasks(endpoint_result)


def is_valid_get_task_tree(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_task_tree(api):
    endpoint_result = api.task.get_task_tree( path_param_task_id = '')
    assert is_valid_get_task_tree(endpoint_result)


def is_valid_get_task_by_operationid(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_task_by_operationid(api):
    endpoint_result = api.task.get_task_by_operationid( path_param_limit = '', path_param_offset = '', path_param_operation_id = '')
    assert is_valid_get_task_by_operationid(endpoint_result)


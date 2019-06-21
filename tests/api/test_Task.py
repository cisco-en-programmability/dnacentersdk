# task

import pytest
import dnacentersdk


# e78b-b8a2-449b-9eed
def is_valid_get_tasks(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# e78b-b8a2-449b-9eed
def get_tasks(api):
    endpoint_result = api.task.get_tasks( param_data = None, param_end_time = None, param_error_code = None, param_failure_reason = None, param_is_error = None, param_limit = None, param_offset = None, param_order = None, param_parent_id = None, param_progress = None, param_service_type = None, param_sort_by = None, param_start_time = None, param_username = None )
    return endpoint_result

# e78b-b8a2-449b-9eed
def test_get_tasks(api):
    assert is_valid_get_tasks(get_tasks(api))


# f5a2-69c4-4f2a-95fa
def is_valid_get_task_tree(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# f5a2-69c4-4f2a-95fa
def get_task_tree(api):
    endpoint_result = api.task.get_task_tree( path_param_task_id = get_tasks(api).response[0].id )
    return endpoint_result

# f5a2-69c4-4f2a-95fa
def test_get_task_tree(api):
    assert is_valid_get_task_tree(get_task_tree(api))


# 26b4-4ab0-4649-a183
def is_valid_get_task_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 26b4-4ab0-4649-a183
def get_task_count(api):
    endpoint_result = api.task.get_task_count( param_data = None, param_end_time = None, param_error_code = None, param_failure_reason = None, param_is_error = None, param_parent_id = None, param_progress = None, param_service_type = None, param_start_time = None, param_username = None )
    return endpoint_result

# 26b4-4ab0-4649-a183
def test_get_task_count(api):
    assert is_valid_get_task_count(get_task_count(api))


# a1a9-3873-46ba-92b1
def is_valid_get_task_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# a1a9-3873-46ba-92b1
def get_task_by_id(api):
    endpoint_result = api.task.get_task_by_id( path_param_task_id = get_tasks(api).response[0].id )
    return endpoint_result

# a1a9-3873-46ba-92b1
def test_get_task_by_id(api):
    assert is_valid_get_task_by_id(get_task_by_id(api))


# e487-f8d3-481b-94f2
def is_valid_get_task_by_operationid(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# e487-f8d3-481b-94f2
def get_task_by_operationid(api):
    endpoint_result = api.task.get_task_by_operationid( path_param_limit = 2, path_param_offset = 1, path_param_operation_id = list(filter(lambda x: x.operationIdList is not None, get_tasks(api).response))[0].operationIdList[0] )
    return endpoint_result

# e487-f8d3-481b-94f2
@pytest.mark.skip(reason="no way of currently testing this")
def test_get_task_by_operationid(api):
    assert is_valid_get_task_by_operationid(get_task_by_operationid(api))


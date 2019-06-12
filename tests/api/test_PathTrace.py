# path_trace

import pytest
import dnacentersdk


def is_valid_retrives_all_previous_pathtraces_summary(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_retrives_all_previous_pathtraces_summary(api):
    endpoint_result = api.path_trace.retrives_all_previous_pathtraces_summary( param_dest_i_p = None, param_dest_port = None, param_gt_create_time = None, param_last_update_time = None, param_limit = None, param_lt_create_time = None, param_offset = None, param_order = None, param_periodic_refresh = None, param_protocol = None, param_sort_by = None, param_source_i_p = None, param_source_port = None, param_status = None, param_task_id = None)
    assert is_valid_retrives_all_previous_pathtraces_summary(endpoint_result)


def is_valid_deletes_pathtrace_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_deletes_pathtrace_by_id(api):
    endpoint_result = api.path_trace.deletes_pathtrace_by_id( path_param_flow_analysis_id = '')
    assert is_valid_deletes_pathtrace_by_id(endpoint_result)


def is_valid_initiate_a_new_pathtrace(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_initiate_a_new_pathtrace(api):
    endpoint_result = api.path_trace.initiate_a_new_pathtrace( rq_controlPath = None, rq_destIP = None, rq_destPort = None, rq_inclusions = None, rq_periodicRefresh = None, rq_protocol = None, rq_sourceIP = None, rq_sourcePort = None)
    assert is_valid_initiate_a_new_pathtrace(endpoint_result)


def is_valid_retrieves_previous_pathtrace(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_retrieves_previous_pathtrace(api):
    endpoint_result = api.path_trace.retrieves_previous_pathtrace( path_param_flow_analysis_id = '')
    assert is_valid_retrieves_previous_pathtrace(endpoint_result)


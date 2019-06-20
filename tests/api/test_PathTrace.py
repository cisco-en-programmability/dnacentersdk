# path_trace

import pytest
import dnacentersdk


# a395-fae6-44ca-899c
def is_valid_initiate_a_new_pathtrace(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# a395-fae6-44ca-899c
def initiate_a_new_pathtrace(api):
    endpoint_result = api.path_trace.initiate_a_new_pathtrace( rq_controlPath = None, rq_destIP = '10.10.22.114', rq_destPort = None, rq_inclusions = None, rq_periodicRefresh = None, rq_protocol = None, rq_sourceIP = '10.10.22.98', rq_sourcePort = None )
    return endpoint_result

# a395-fae6-44ca-899c
def test_initiate_a_new_pathtrace(api):
    assert is_valid_initiate_a_new_pathtrace(initiate_a_new_pathtrace(api))


# 8a9d-2b76-443b-914e
def is_valid_deletes_pathtrace_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 8a9d-2b76-443b-914e
def deletes_pathtrace_by_id(api):
    endpoint_result = api.path_trace.deletes_pathtrace_by_id( path_param_flow_analysis_id = retrives_all_previous_pathtraces_summary(api).response[0].id )
    return endpoint_result

# 8a9d-2b76-443b-914e
def test_deletes_pathtrace_by_id(api):
    assert is_valid_deletes_pathtrace_by_id(deletes_pathtrace_by_id(api))


# 7ab9-a8bd-4f3b-86a4
def is_valid_retrieves_previous_pathtrace(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 7ab9-a8bd-4f3b-86a4
def retrieves_previous_pathtrace(api):
    endpoint_result = api.path_trace.retrieves_previous_pathtrace( path_param_flow_analysis_id = initiate_a_new_pathtrace(api).response.flowAnalysisId )
    return endpoint_result

# 7ab9-a8bd-4f3b-86a4
def test_retrieves_previous_pathtrace(api):
    assert is_valid_retrieves_previous_pathtrace(retrieves_previous_pathtrace(api))


# 55bc-3bf9-4e38-b6ff
def is_valid_retrives_all_previous_pathtraces_summary(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 55bc-3bf9-4e38-b6ff
def retrives_all_previous_pathtraces_summary(api):
    endpoint_result = api.path_trace.retrives_all_previous_pathtraces_summary( param_dest_ip = None, param_dest_port = None, param_gt_create_time = None, param_last_update_time = None, param_limit = None, param_lt_create_time = None, param_offset = None, param_order = None, param_periodic_refresh = None, param_protocol = None, param_sort_by = None, param_source_ip = '10.10.22.98', param_source_port = None, param_status = None, param_task_id = None )
    return endpoint_result

# 55bc-3bf9-4e38-b6ff
def test_retrives_all_previous_pathtraces_summary(api):
    assert is_valid_retrives_all_previous_pathtraces_summary(retrives_all_previous_pathtraces_summary(api))


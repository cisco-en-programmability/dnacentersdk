# clients

import pytest
import dnacentersdk


# e2ad-ba79-43ba-b3e9
def is_valid_get_client_detail(obj):
    some_keys = ['executionId', 'executionStatusUrl', 'message']
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# e2ad-ba79-43ba-b3e9
def get_client_detail(api):
    endpoint_result = api.clients.get_client_detail( param_mac_address = '', param_timestamp = '1561049238' )
    return endpoint_result

# e2ad-ba79-43ba-b3e9
def test_get_client_detail(api):
    assert is_valid_get_client_detail(get_client_detail(api))


# 149a-a93b-4ddb-80dd
def is_valid_get_overall_client_health(obj):
    some_keys = ['executionId', 'executionStatusUrl', 'message']
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 149a-a93b-4ddb-80dd
def get_overall_client_health(api):
    endpoint_result = api.clients.get_overall_client_health( param_timestamp = '1561049238' )
    return endpoint_result

# 149a-a93b-4ddb-80dd
def test_get_overall_client_health(api):
    assert is_valid_get_overall_client_health(get_overall_client_health(api))


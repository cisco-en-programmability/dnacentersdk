# sites

import pytest
import dnacentersdk


# 17a8-2ac9-4cf9-9ab0
def is_valid_get_site_health(obj):
    some_keys = ['executionId', 'executionStatusUrl', 'message']
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 17a8-2ac9-4cf9-9ab0
def get_site_health(api):
    endpoint_result = api.sites.get_site_health( param_timestamp = '1561049238' )
    return endpoint_result

# 17a8-2ac9-4cf9-9ab0
def test_get_site_health(api):
    assert is_valid_get_site_health(get_site_health(api))


# 50b5-89fd-4c7a-930a
def is_valid_create_site(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 50b5-89fd-4c7a-930a
def create_site(api):
    endpoint_result = api.sites.create_site( rq_site = None, rq_type = None )
    return endpoint_result

# 50b5-89fd-4c7a-930a
def test_create_site(api):
    assert is_valid_create_site(create_site(api))


# eeb1-68eb-4198-8e07
def is_valid_assign_device_to_site(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# eeb1-68eb-4198-8e07
def assign_device_to_site(api):
    endpoint_result = api.sites.assign_device_to_site( path_param_site_id = '', rq_device = None )
    return endpoint_result

# eeb1-68eb-4198-8e07
@pytest.mark.skip(reason="no way of currently testing this")
def test_assign_device_to_site(api):
    assert is_valid_assign_device_to_site(assign_device_to_site(api))


# sites

import pytest
import dnacentersdk


def is_valid_get_site_health(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_site_health(api):
    endpoint_result = api.sites.get_site_health( param_timestamp = '1560378327')
    assert is_valid_get_site_health(endpoint_result)


def is_valid_assign_device_to_site(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_assign_device_to_site(api):
    endpoint_result = api.sites.assign_device_to_site( path_param_site_id = '', rq_device = None)
    assert is_valid_assign_device_to_site(endpoint_result)


def is_valid_create_site(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_site(api):
    endpoint_result = api.sites.create_site( rq_site = None, rq_type = None)
    assert is_valid_create_site(endpoint_result)


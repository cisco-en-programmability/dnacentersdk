# site_profile

import pytest
import dnacentersdk


# 7fbe-4b80-4879-baa4
def is_valid_get_device_details_by_ip(obj):
    some_keys = ['executionId', 'executionStatusUrl', 'message']
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 7fbe-4b80-4879-baa4
def get_device_details_by_ip(api):
    endpoint_result = api.site_profile.get_device_details_by_ip( param_device_ip = '10.10.20.253' )
    return endpoint_result

# 7fbe-4b80-4879-baa4
def test_get_device_details_by_ip(api):
    assert is_valid_get_device_details_by_ip(get_device_details_by_ip(api))


# 8288-28f4-4f28-bd0d
def is_valid_provision_nfv(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 8288-28f4-4f28-bd0d
def provision_nfv(api):
    endpoint_result = api.site_profile.provision_nfv( rq_callbackUrl = None, rq_provisioning = None, rq_siteProfile = None )
    return endpoint_result

# 8288-28f4-4f28-bd0d
def test_provision_nfv(api):
    assert is_valid_provision_nfv(provision_nfv(api))


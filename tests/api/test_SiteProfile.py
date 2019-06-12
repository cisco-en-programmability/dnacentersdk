# site_profile

import pytest
import dnacentersdk


def is_valid_get_device_details_by_ip(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_details_by_ip(api):
    endpoint_result = api.site_profile.get_device_details_by_ip( param_device_ip = '')
    assert is_valid_get_device_details_by_ip(endpoint_result)


def is_valid_provision_nfv(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_provision_nfv(api):
    endpoint_result = api.site_profile.provision_nfv( rq_callbackUrl = None, rq_provisioning = None, rq_siteProfile = None)
    assert is_valid_provision_nfv(endpoint_result)


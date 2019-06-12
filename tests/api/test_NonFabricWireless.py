# non_fabric_wireless

import pytest
import dnacentersdk


def is_valid_delete_and_provision_ssid(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_and_provision_ssid(api):
    endpoint_result = api.non_fabric_wireless.delete_and_provision_ssid( path_param_managed_a_p_locations = '', path_param_ssid_name = '')
    assert is_valid_delete_and_provision_ssid(endpoint_result)


def is_valid_create_enterprise_ssid(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.create_enterprise_ssid( rq_enableBroadcastSSID = None, rq_enableFastLane = None, rq_enableMACFiltering = None, rq_fastTransition = None, rq_name = None, rq_passphrase = None, rq_radioPolicy = None, rq_securityLevel = None, rq_trafficType = None)
    assert is_valid_create_enterprise_ssid(endpoint_result)


def is_valid_create_and_provision_ssid(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_and_provision_ssid(api):
    endpoint_result = api.non_fabric_wireless.create_and_provision_ssid( rq_enableFabric = None, rq_flexConnect = None, rq_managedAPLocations = None, rq_ssidDetails = None, rq_ssidType = None, rq_vlanAndDynamicInterfaceDetails = None)
    assert is_valid_create_and_provision_ssid(endpoint_result)


def is_valid_delete_enterprise_ssid(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.delete_enterprise_ssid( path_param_ssid_name = '')
    assert is_valid_delete_enterprise_ssid(endpoint_result)


def is_valid_get_enterprise_ssid(obj):
    return len(obj) > 0 and all([ item for item in obj ])

def test_get_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.get_enterprise_ssid( param_ssid_name = None)
    assert is_valid_get_enterprise_ssid(endpoint_result)


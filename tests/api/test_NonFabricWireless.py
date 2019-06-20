# non_fabric_wireless

import pytest
import dnacentersdk


# 8a96-fb95-4d09-a349
def is_valid_create_enterprise_ssid(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 8a96-fb95-4d09-a349
def create_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.create_enterprise_ssid( rq_enableBroadcastSSID = None, rq_enableFastLane = None, rq_enableMACFiltering = None, rq_fastTransition = None, rq_name = None, rq_passphrase = None, rq_radioPolicy = None, rq_securityLevel = None, rq_trafficType = None )
    return endpoint_result

# 8a96-fb95-4d09-a349
@pytest.mark.skip(reason="no way of currently testing this")
def test_create_enterprise_ssid(api):
    assert is_valid_create_enterprise_ssid(create_enterprise_ssid(api))


# cca5-19ba-45eb-b423
def is_valid_get_enterprise_ssid(obj):
    return len(obj) > 0 and all([ item for item in obj ])


# cca5-19ba-45eb-b423
def get_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.get_enterprise_ssid( param_ssid_name = None )
    return endpoint_result

# cca5-19ba-45eb-b423
@pytest.mark.skip(reason="no way of currently testing this")
def test_get_enterprise_ssid(api):
    assert is_valid_get_enterprise_ssid(get_enterprise_ssid(api))


# c7a6-592b-4b98-a369
def is_valid_delete_enterprise_ssid(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# c7a6-592b-4b98-a369
def delete_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.delete_enterprise_ssid( path_param_ssid_name = '' )
    return endpoint_result

# c7a6-592b-4b98-a369
@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_enterprise_ssid(api):
    assert is_valid_delete_enterprise_ssid(delete_enterprise_ssid(api))


# db9f-997f-4e59-aec1
def is_valid_create_and_provision_ssid(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# db9f-997f-4e59-aec1
def create_and_provision_ssid(api):
    endpoint_result = api.non_fabric_wireless.create_and_provision_ssid( rq_enableFabric = None, rq_flexConnect = None, rq_managedAPLocations = None, rq_ssidDetails = None, rq_ssidType = None, rq_vlanAndDynamicInterfaceDetails = None )
    return endpoint_result

# db9f-997f-4e59-aec1
@pytest.mark.skip(reason="no way of currently testing this")
def test_create_and_provision_ssid(api):
    assert is_valid_create_and_provision_ssid(create_and_provision_ssid(api))


# cca0-9834-4a48-9dfa
def is_valid_delete_and_provision_ssid(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# cca0-9834-4a48-9dfa
def delete_and_provision_ssid(api):
    endpoint_result = api.non_fabric_wireless.delete_and_provision_ssid( path_param_managed_aplocations = '', path_param_ssid_name = '' )
    return endpoint_result

# cca0-9834-4a48-9dfa
@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_and_provision_ssid(api):
    assert is_valid_delete_and_provision_ssid(delete_and_provision_ssid(api))


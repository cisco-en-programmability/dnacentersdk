# fabric_wired

import pytest
import dnacentersdk


# bead-7b34-43b9-96a7
def is_valid_adds_border_device_in_sda_fabric(obj):
    some_keys = [ 'status', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# bead-7b34-43b9-96a7
def adds_border_device_in_sda_fabric(api):
    endpoint_result = api.fabric_wired.adds_border_device_in_sda_fabric( path_param_sda_border_device = '' )
    return endpoint_result

# bead-7b34-43b9-96a7
@pytest.mark.skip(reason="no way of currently testing this")
def test_adds_border_device_in_sda_fabric(api):
    assert is_valid_adds_border_device_in_sda_fabric(adds_border_device_in_sda_fabric(api))


# 98a3-9bf4-485a-9871
def is_valid_gets_border_device_details_from_sda_fabric(obj):
    some_keys = [ 'status', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 98a3-9bf4-485a-9871
def gets_border_device_details_from_sda_fabric(api):
    endpoint_result = api.fabric_wired.gets_border_device_details_from_sda_fabric( path_param_device_ip_address = '', path_param_sda_border_device = '' )
    return endpoint_result

# 98a3-9bf4-485a-9871
@pytest.mark.skip(reason="no way of currently testing this")
def test_gets_border_device_details_from_sda_fabric(api):
    assert is_valid_gets_border_device_details_from_sda_fabric(gets_border_device_details_from_sda_fabric(api))


# cb81-b935-40ba-aab0
def is_valid_deletes_border_device_from_sda_fabric(obj):
    some_keys = [ 'status', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# cb81-b935-40ba-aab0
def deletes_border_device_from_sda_fabric(api):
    endpoint_result = api.fabric_wired.deletes_border_device_from_sda_fabric( path_param_device_ip_address = '', path_param_sda_border_device = '' )
    return endpoint_result

# cb81-b935-40ba-aab0
@pytest.mark.skip(reason="no way of currently testing this")
def test_deletes_border_device_from_sda_fabric(api):
    assert is_valid_deletes_border_device_from_sda_fabric(deletes_border_device_from_sda_fabric(api))


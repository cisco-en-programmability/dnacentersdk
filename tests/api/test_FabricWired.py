# fabric_wired

import pytest
import dnacentersdk


def is_valid_gets_border_device_details_from_sda_fabric(obj):
    some_keys = [ 'status', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_gets_border_device_details_from_sda_fabric(api):
    endpoint_result = api.fabric_wired.gets_border_device_details_from_sda_fabric( path_param_device_ip_address = '', path_param_sda_border_device = '')
    assert is_valid_gets_border_device_details_from_sda_fabric(endpoint_result)


def is_valid_adds_border_device_in_sda_fabric(obj):
    some_keys = [ 'status', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_adds_border_device_in_sda_fabric(api):
    endpoint_result = api.fabric_wired.adds_border_device_in_sda_fabric( path_param_sda_border_device = '')
    assert is_valid_adds_border_device_in_sda_fabric(endpoint_result)


def is_valid_deletes_border_device_from_sda_fabric(obj):
    some_keys = [ 'status', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_deletes_border_device_from_sda_fabric(api):
    endpoint_result = api.fabric_wired.deletes_border_device_from_sda_fabric( path_param_device_ip_address = '', path_param_sda_border_device = '')
    assert is_valid_deletes_border_device_from_sda_fabric(endpoint_result)


# -*- coding: utf-8 -*-
"""DNACenterAPI devices API fixtures and tests.

Copyright (c) 2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import pytest
import dnacentersdk




# 3d92-3b18-4dc9-a4ca
def is_valid_get_device_interface_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_interface_count(api):
    endpoint_result = api.devices.get_device_interface_count( payload = '' )
    return endpoint_result


def test_get_device_interface_count(api):
    assert is_valid_get_device_interface_count(get_device_interface_count(api))


# 20b1-9b52-464b-8972
def is_valid_get_device_list(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_list(api):
    endpoint_result = api.devices.get_device_list( param_associated_wlc_ip = None, param_collection_interval = None, param_collection_status = None, param_error_code = None, param_error_description = None, param_family = None, param_hostname = None, param_id = None, param_license_name = None, param_license_status = None, param_license_type = None, param_location = None, param_location_name = None, param_mac_address = None, param_management_ip_address = None, param_module_equpimenttype = None, param_module_name = None, param_module_operationstatecode = None, param_module_partnumber = None, param_module_servicestate = None, param_module_vendorequipmenttype = None, param_not_synced_for_minutes = None, param_platform_id = None, param_reachability_status = None, param_role = None, param_serial_number = None, param_series = None, param_software_type = None, param_software_version = None, param_type = None, param_up_time = None, payload = '' )
    return endpoint_result


def test_get_device_list(api):
    assert is_valid_get_device_list(get_device_list(api))


# 3b9e-f967-4429-be4c
def is_valid_sync_devices_using_forcesync(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def sync_devices_using_forcesync(api):
    endpoint_result = api.devices.sync_devices_using_forcesync( param_force_sync = None, payload = ['get_device_list(api).response[0].id'] )
    return endpoint_result


def test_sync_devices_using_forcesync(api):
    assert is_valid_sync_devices_using_forcesync(sync_devices_using_forcesync(api))


# 38bd-0b88-4b89-a785
def is_valid_get_polling_interval_for_all_devices(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_polling_interval_for_all_devices(api):
    endpoint_result = api.devices.get_polling_interval_for_all_devices( payload = '' )
    return endpoint_result


def test_get_polling_interval_for_all_devices(api):
    assert is_valid_get_polling_interval_for_all_devices(get_polling_interval_for_all_devices(api))


# 5db2-1b8e-43fa-b7d8
def is_valid_get_device_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_count(api):
    endpoint_result = api.devices.get_device_count( payload = '' )
    return endpoint_result


def test_get_device_count(api):
    assert is_valid_get_device_count(get_device_count(api))


# 288d-f949-4f2a-9746
def is_valid_get_device_interface_vlans(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_interface_vlans(api):
    endpoint_result = api.devices.get_device_interface_vlans( path_param_id = get_device_list(api).response[0].id, param_interface_type = None, payload = '' )
    return endpoint_result


def test_get_device_interface_vlans(api):
    assert is_valid_get_device_interface_vlans(get_device_interface_vlans(api))


# 349c-8884-43b8-9a58
def is_valid_get_device_interfaces_by_specified_range(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_interfaces_by_specified_range(api):
    endpoint_result = api.devices.get_device_interfaces_by_specified_range( path_param_device_id = get_device_list(api).response[0].id, path_param_records_to_return = 1, path_param_start_index = 3, payload = '' )
    return endpoint_result


def test_get_device_interfaces_by_specified_range(api):
    assert is_valid_get_device_interfaces_by_specified_range(get_device_interfaces_by_specified_range(api))


# 84b3-3a9e-480a-bcaf
def is_valid_get_device_config_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_config_by_id(api):
    endpoint_result = api.devices.get_device_config_by_id( path_param_network_device_id = get_device_list(api).response[0].id, payload = '' )
    return endpoint_result


def test_get_device_config_by_id(api):
    assert is_valid_get_device_config_by_id(get_device_config_by_id(api))


# 888f-585c-49b8-8441
def is_valid_get_device_config_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_config_count(api):
    endpoint_result = api.devices.get_device_config_count( payload = '' )
    return endpoint_result


def test_get_device_config_count(api):
    assert is_valid_get_device_config_count(get_device_config_count(api))


# f594-7a4c-439a-8bf0
def is_valid_get_all_interfaces(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_all_interfaces(api):
    endpoint_result = api.devices.get_all_interfaces( param_limit = 500, param_offset = 1, payload = '' )
    return endpoint_result


def test_get_all_interfaces(api):
    assert is_valid_get_all_interfaces(get_all_interfaces(api))


# 4eb5-6a61-4cc9-a2d2
def is_valid_get_interface_details_by_device_id_and_interface_name(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_interface_details_by_device_id_and_interface_name(api):
    endpoint_result = api.devices.get_interface_details_by_device_id_and_interface_name( param_name = get_all_interfaces(api).response[0].portName, path_param_device_id = get_device_list(api).response[0].id, payload = '' )
    return endpoint_result


def test_get_interface_details_by_device_id_and_interface_name(api):
    assert is_valid_get_interface_details_by_device_id_and_interface_name(get_interface_details_by_device_id_and_interface_name(api))


# 8291-8a1b-4d28-9c5c
def is_valid_get_polling_interval_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_polling_interval_by_id(api):
    endpoint_result = api.devices.get_polling_interval_by_id( path_param_id = get_device_list(api).response[0].id, payload = '' )
    return endpoint_result


def test_get_polling_interval_by_id(api):
    assert is_valid_get_polling_interval_by_id(get_polling_interval_by_id(api))


# 8db9-3974-4649-a782
def is_valid_get_module_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_module_count(api):
    endpoint_result = api.devices.get_module_count( param_device_id = get_device_list(api).response[0].id, param_name_list = None, param_operational_state_code_list = None, param_part_number_list = None, param_vendor_equipment_type_list = None, payload = '' )
    return endpoint_result


def test_get_module_count(api):
    assert is_valid_get_module_count(get_module_count(api))


# ba9d-c85b-4b8a-9a17
def is_valid_get_interface_info_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_interface_info_by_id(api):
    endpoint_result = api.devices.get_interface_info_by_id( path_param_device_id = get_device_list(api).response[0].id, payload = '' )
    return endpoint_result


def test_get_interface_info_by_id(api):
    assert is_valid_get_interface_info_by_id(get_interface_info_by_id(api))


# 819f-9aa5-4fea-b7bf
def is_valid_get_device_summary(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_summary(api):
    endpoint_result = api.devices.get_device_summary( path_param_id = get_device_list(api).response[0].id, payload = '' )
    return endpoint_result


def test_get_device_summary(api):
    assert is_valid_get_device_summary(get_device_summary(api))


# c3b3-c9ef-4e6b-8a09
def is_valid_get_functional_capability_for_devices(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_functional_capability_for_devices(api):
    endpoint_result = api.devices.get_functional_capability_for_devices( param_device_id = get_device_list(api).response[0].id, param_function_name = None, payload = '' )
    return endpoint_result


def test_get_functional_capability_for_devices(api):
    assert is_valid_get_functional_capability_for_devices(get_functional_capability_for_devices(api))


# 3d92-3b18-4dc9-a4ca
def is_valid_get_device_interface_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_interface_count(api):
    endpoint_result = api.devices.get_device_interface_count( payload = '' )
    return endpoint_result


def test_get_device_interface_count(api):
    assert is_valid_get_device_interface_count(get_device_interface_count(api))


# eb82-49e3-4f69-b0f1
def is_valid_get_modules(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_modules(api):
    endpoint_result = api.devices.get_modules( param_device_id = get_device_list(api).response[0].id, param_limit = None, param_name_list = None, param_offset = None, param_operational_state_code_list = None, param_part_number_list = None, param_vendor_equipment_type_list = None, payload = '' )
    return endpoint_result


def test_get_modules(api):
    assert is_valid_get_modules(get_modules(api))


# f682-6a8e-41bb-a242
def is_valid_get_wireless_lan_controller_details_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_wireless_lan_controller_details_by_id(api):
    endpoint_result = api.devices.get_wireless_lan_controller_details_by_id( path_param_id = get_device_list(api).response[0].id, payload = '' )
    return endpoint_result


def test_get_wireless_lan_controller_details_by_id(api):
    assert is_valid_get_wireless_lan_controller_details_by_id(get_wireless_lan_controller_details_by_id(api))


# 84b3-7ae5-4c59-ab28
def is_valid_get_organization_list_for_meraki(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_organization_list_for_meraki(api):
    endpoint_result = api.devices.get_organization_list_for_meraki( path_param_id = get_device_list(api).response[0].id, payload = '' )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_organization_list_for_meraki(api):
    assert is_valid_get_organization_list_for_meraki(get_organization_list_for_meraki(api))


# 70ad-3976-49e9-b4d3
def is_valid_get_ospf_interfaces(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_ospf_interfaces(api):
    endpoint_result = api.devices.get_ospf_interfaces( payload = '' )
    return endpoint_result


def test_get_ospf_interfaces(api):
    assert is_valid_get_ospf_interfaces(get_ospf_interfaces(api))


# 81bb-4804-405a-8d2f
def is_valid_get_functional_capability_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_functional_capability_by_id(api):
    endpoint_result = api.devices.get_functional_capability_by_id( path_param_id = get_functional_capability_for_devices(api).response[0].functionalCapability[0].id, payload = '' )
    return endpoint_result


def test_get_functional_capability_by_id(api):
    assert is_valid_get_functional_capability_by_id(get_functional_capability_by_id(api))


# 84ad-8b0e-42ca-b48a
def is_valid_get_isis_interfaces(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_isis_interfaces(api):
    endpoint_result = api.devices.get_isis_interfaces( payload = '' )
    return endpoint_result


def test_get_isis_interfaces(api):
    assert is_valid_get_isis_interfaces(get_isis_interfaces(api))


# b7bc-aa08-4e2b-90d0
def is_valid_get_device_config_for_all_devices(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_config_for_all_devices(api):
    endpoint_result = api.devices.get_device_config_for_all_devices( payload = '' )
    return endpoint_result


def test_get_device_config_for_all_devices(api):
    assert is_valid_get_device_config_for_all_devices(get_device_config_for_all_devices(api))


# cd84-69e6-47ca-ab0e
def is_valid_get_interface_by_ip(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_interface_by_ip(api):
    endpoint_result = api.devices.get_interface_by_ip( path_param_ip_address = list(filter(lambda x: x.ipv4Address is not None, get_all_interfaces(api).response))[0].ipv4Address, payload = '' )
    return endpoint_result


def test_get_interface_by_ip(api):
    assert is_valid_get_interface_by_ip(get_interface_by_ip(api))


# d0a4-b881-45aa-bb51
def is_valid_get_network_device_by_ip(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_network_device_by_ip(api):
    endpoint_result = api.devices.get_network_device_by_ip( path_param_ip_address = get_device_list(api).response[0].managementIpAddress, payload = '' )
    return endpoint_result


def test_get_network_device_by_ip(api):
    assert is_valid_get_network_device_by_ip(get_network_device_by_ip(api))


# 8fa8-eb40-4a4a-8d96
def is_valid_get_device_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_by_id(api):
    endpoint_result = api.devices.get_device_by_id( path_param_id = get_device_list(api).response[0].id, payload = '' )
    return endpoint_result


def test_get_device_by_id(api):
    assert is_valid_get_device_by_id(get_device_by_id(api))


# aeb9-eb67-460b-92df
def is_valid_sync_devices(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def sync_devices(api):
    endpoint_result = api.devices.sync_devices( rq_cliTransport = None, rq_computeDevice = None, rq_enablePassword = None, rq_extendedDiscoveryInfo = None, rq_httpPassword = None, rq_httpPort = None, rq_httpSecure = None, rq_httpUserName = None, rq_ipAddress = None, rq_merakiOrgId = None, rq_netconfPort = None, rq_password = None, rq_serialNumber = None, rq_snmpAuthPassphrase = None, rq_snmpAuthProtocol = None, rq_snmpMode = None, rq_snmpPrivPassphrase = None, rq_snmpPrivProtocol = None, rq_snmpROCommunity = None, rq_snmpRWCommunity = None, rq_snmpRetry = None, rq_snmpTimeout = None, rq_snmpUserName = None, rq_snmpVersion = None, rq_type = None, rq_updateMgmtIPaddressList = None, rq_userName = None, payload = '' )
    return endpoint_result


def test_sync_devices(api):
    assert is_valid_sync_devices(sync_devices(api))


# b888-792d-43ba-ba46
def is_valid_get_interface_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_interface_by_id(api):
    endpoint_result = api.devices.get_interface_by_id( path_param_id = get_all_interfaces(api).response[0].id, payload = '' )
    return endpoint_result


def test_get_interface_by_id(api):
    assert is_valid_get_interface_by_id(get_interface_by_id(api))


# d888-ab6d-4d59-a8c1
def is_valid_get_device_by_serial_number(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_by_serial_number(api):
    endpoint_result = api.devices.get_device_by_serial_number( path_param_serial_number = get_device_list(api).response[0].serialNumber, payload = '' )
    return endpoint_result


def test_get_device_by_serial_number(api):
    assert is_valid_get_device_by_serial_number(get_device_by_serial_number(api))


# f495-48c5-4be8-a3e2
def is_valid_get_network_device_by_pagination_range(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_network_device_by_pagination_range(api):
    endpoint_result = api.devices.get_network_device_by_pagination_range( path_param_records_to_return = 4, path_param_start_index = 1, payload = '' )
    return endpoint_result


def test_get_network_device_by_pagination_range(api):
    assert is_valid_get_network_device_by_pagination_range(get_network_device_by_pagination_range(api))


# ffa7-48cc-44e9-a437
def is_valid_retrieves_all_network_devices(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def retrieves_all_network_devices(api):
    endpoint_result = api.devices.retrieves_all_network_devices( param_associated_wlc_ip = None, param_collection_interval = None, param_collection_status = None, param_error_code = None, param_family = None, param_hostname = get_device_list(api).response[0].hostname, param_limit = None, param_mac_address = None, param_management_ip_address = None, param_offset = None, param_platform_id = None, param_reachability_failure_reason = None, param_reachability_status = None, param_role = None, param_role_source = None, param_serial_number = None, param_series = None, param_software_type = None, param_software_version = None, param_type = None, param_up_time = None, param_vrf_name = None, payload = '' )
    return endpoint_result


def test_retrieves_all_network_devices(api):
    assert is_valid_retrieves_all_network_devices(retrieves_all_network_devices(api))


# 89b2-fb14-4f5b-b09b
def is_valid_get_device_detail(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_detail(api):
    endpoint_result = api.devices.get_device_detail( param_identifier = 'macAddress', param_search_by = get_device_list(api).response[0].macAddress, param_timestamp = '1561661891', payload = '' )
    return endpoint_result


def test_get_device_detail(api):
    assert is_valid_get_device_detail(get_device_detail(api))


# 0db7-da74-4c0b-83d8
def is_valid_get_module_info_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_module_info_by_id(api):
    endpoint_result = api.devices.get_module_info_by_id( path_param_id = get_device_list(api).response[0].lineCardId.split(',')[0], payload = '' )
    return endpoint_result


def test_get_module_info_by_id(api):
    assert is_valid_get_module_info_by_id(get_module_info_by_id(api))


# 4bb2-2af0-46fa-8f08
def is_valid_add_device(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def add_device(api):
    endpoint_result = api.devices.add_device( rq_cliTransport = None, rq_computeDevice = None, rq_enablePassword = None, rq_extendedDiscoveryInfo = None, rq_httpPassword = None, rq_httpPort = None, rq_httpSecure = None, rq_httpUserName = None, rq_ipAddress = [ get_device_list(api).response[0].managementIpAddress ], rq_merakiOrgId = None, rq_netconfPort = None, rq_password = None, rq_serialNumber = None, rq_snmpAuthPassphrase = None, rq_snmpAuthProtocol = None, rq_snmpMode = None, rq_snmpPrivPassphrase = None, rq_snmpPrivProtocol = None, rq_snmpROCommunity = None, rq_snmpRWCommunity = None, rq_snmpRetry = None, rq_snmpTimeout = None, rq_snmpUserName = None, rq_snmpVersion = None, rq_type = None, rq_updateMgmtIPaddressList = None, rq_userName = None, payload = {'cliTransport': 'string', 'enablePassword': 'string', 'password': 'string', 'snmpAuthPassphrase': 'string', 'snmpAuthProtocol': 'string', 'snmpMode': 'string', 'snmpPrivPassphrase': 'string', 'snmpPrivProtocol': 'string', 'snmpROCommunity': 'string', 'snmpRWCommunity': 'string', 'snmpRetry': 0, 'snmpTimeout': 0, 'snmpUserName': 'string', 'type': 'NETWORK_DEVICE', 'userName': 'string'} )
    return endpoint_result


def test_add_device(api):
    assert is_valid_add_device(add_device(api))


# b985-5ad5-4ae9-8156
def is_valid_update_device_role(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def update_device_role(api):
    endpoint_result = api.devices.update_device_role( rq_id = get_device_list(api).response[0].id, rq_role = get_device_list(api).response[0].role, rq_roleSource = get_device_list(api).response[0].roleSource, payload = '' )
    return endpoint_result


def test_update_device_role(api):
    assert is_valid_update_device_role(update_device_role(api))


# 1c89-4b58-48ea-b214
def is_valid_delete_device_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def delete_device_by_id(api):
    endpoint_result = api.devices.delete_device_by_id( path_param_id = get_device_list(api).response[0].id, param_is_force_delete = None, payload = '' )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_device_by_id(api):
    assert is_valid_delete_device_by_id(delete_device_by_id(api))


# c980-9b67-44f8-a502
def is_valid_register_device_for_wsa(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def register_device_for_wsa(api):
    endpoint_result = api.devices.register_device_for_wsa( param_macaddress = get_device_list(api).response[0].macAddress, param_serial_number = get_device_list(api).response[0].serialNumber, payload = '' )
    return endpoint_result


def test_register_device_for_wsa(api):
    assert is_valid_register_device_for_wsa(register_device_for_wsa(api))


# cd98-780f-4888-a66d
def is_valid_export_device_list(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def export_device_list(api):
    endpoint_result = api.devices.export_device_list( rq_deviceUuids = [ get_device_list(api).response[0].id ], rq_id = get_device_list(api).response[0].id, rq_operationEnum = 'CREDENTIALDETAILS', rq_parameters = None, rq_password = None, payload = '' )
    return endpoint_result


def test_export_device_list(api):
    assert is_valid_export_device_list(export_device_list(api))


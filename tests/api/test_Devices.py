# devices

import pytest
import dnacentersdk


# 3d92-3b18-4dc9-a4ca
def is_valid_get_device_interface_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 3d92-3b18-4dc9-a4ca
def get_device_interface_count(api):
    endpoint_result = api.devices.get_device_interface_count(  )
    return endpoint_result

# 3d92-3b18-4dc9-a4ca
def test_get_device_interface_count(api):
    assert is_valid_get_device_interface_count(get_device_interface_count(api))


# 3b9e-f967-4429-be4c
def is_valid_sync_devices_using_forcesync(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 3b9e-f967-4429-be4c
def sync_devices_using_forcesync(api):
    endpoint_result = api.devices.sync_devices_using_forcesync( param_force_sync = None )
    return endpoint_result

# 3b9e-f967-4429-be4c
def test_sync_devices_using_forcesync(api):
    assert is_valid_sync_devices_using_forcesync(sync_devices_using_forcesync(api))


# 20b1-9b52-464b-8972
def is_valid_get_device_list(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 20b1-9b52-464b-8972
def get_device_list(api):
    endpoint_result = api.devices.get_device_list( param_associated_wlc_ip = None, param_collection_interval = None, param_collection_status = None, param_error_code = None, param_error_description = None, param_family = None, param_hostname = None, param_id = None, param_license_name = None, param_license_status = None, param_license_type = None, param_location = None, param_location_name = None, param_mac_address = None, param_management_ip_address = None, param_module_equpimenttype = None, param_module_name = None, param_module_operationstatecode = None, param_module_partnumber = None, param_module_servicestate = None, param_module_vendorequipmenttype = None, param_not_synced_for_minutes = None, param_platform_id = None, param_reachability_status = None, param_role = None, param_serial_number = None, param_series = None, param_software_type = None, param_software_version = None, param_type = None, param_up_time = None )
    return endpoint_result

# 20b1-9b52-464b-8972
def test_get_device_list(api):
    assert is_valid_get_device_list(get_device_list(api))


# 38bd-0b88-4b89-a785
def is_valid_get_polling_interval_for_all_devices(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 38bd-0b88-4b89-a785
def get_polling_interval_for_all_devices(api):
    endpoint_result = api.devices.get_polling_interval_for_all_devices(  )
    return endpoint_result

# 38bd-0b88-4b89-a785
def test_get_polling_interval_for_all_devices(api):
    assert is_valid_get_polling_interval_for_all_devices(get_polling_interval_for_all_devices(api))


# 5db2-1b8e-43fa-b7d8
def is_valid_get_device_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 5db2-1b8e-43fa-b7d8
def get_device_count(api):
    endpoint_result = api.devices.get_device_count(  )
    return endpoint_result

# 5db2-1b8e-43fa-b7d8
def test_get_device_count(api):
    assert is_valid_get_device_count(get_device_count(api))


# 288d-f949-4f2a-9746
def is_valid_get_device_interface_vlans(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 288d-f949-4f2a-9746
def get_device_interface_vlans(api):
    endpoint_result = api.devices.get_device_interface_vlans( path_param_id = get_device_list(api).response[0].id, param_interface_type = None )
    return endpoint_result

# 288d-f949-4f2a-9746
def test_get_device_interface_vlans(api):
    assert is_valid_get_device_interface_vlans(get_device_interface_vlans(api))


# 349c-8884-43b8-9a58
def is_valid_get_device_interfaces_by_specified_range(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 349c-8884-43b8-9a58
def get_device_interfaces_by_specified_range(api):
    endpoint_result = api.devices.get_device_interfaces_by_specified_range( path_param_device_id = get_device_list(api).response[0].id, path_param_records_to_return = 1, path_param_start_index = 3 )
    return endpoint_result

# 349c-8884-43b8-9a58
def test_get_device_interfaces_by_specified_range(api):
    assert is_valid_get_device_interfaces_by_specified_range(get_device_interfaces_by_specified_range(api))


# 84b3-3a9e-480a-bcaf
def is_valid_get_device_config_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 84b3-3a9e-480a-bcaf
def get_device_config_by_id(api):
    endpoint_result = api.devices.get_device_config_by_id( path_param_network_device_id = get_device_list(api).response[0].id )
    return endpoint_result

# 84b3-3a9e-480a-bcaf
def test_get_device_config_by_id(api):
    assert is_valid_get_device_config_by_id(get_device_config_by_id(api))


# 888f-585c-49b8-8441
def is_valid_get_device_config_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 888f-585c-49b8-8441
def get_device_config_count(api):
    endpoint_result = api.devices.get_device_config_count(  )
    return endpoint_result

# 888f-585c-49b8-8441
def test_get_device_config_count(api):
    assert is_valid_get_device_config_count(get_device_config_count(api))


# f594-7a4c-439a-8bf0
def is_valid_get_all_interfaces(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# f594-7a4c-439a-8bf0
def get_all_interfaces(api):
    endpoint_result = api.devices.get_all_interfaces( param_limit = 500, param_offset = 1 )
    return endpoint_result

# f594-7a4c-439a-8bf0
def test_get_all_interfaces(api):
    assert is_valid_get_all_interfaces(get_all_interfaces(api))


# 4eb5-6a61-4cc9-a2d2
def is_valid_get_interface_details_by_device_id_and_interface_name(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 4eb5-6a61-4cc9-a2d2
def get_interface_details_by_device_id_and_interface_name(api):
    endpoint_result = api.devices.get_interface_details_by_device_id_and_interface_name( param_name = get_all_interfaces(api).response[0].portName, path_param_device_id = get_device_list(api).response[0].id )
    return endpoint_result

# 4eb5-6a61-4cc9-a2d2
def test_get_interface_details_by_device_id_and_interface_name(api):
    assert is_valid_get_interface_details_by_device_id_and_interface_name(get_interface_details_by_device_id_and_interface_name(api))


# 8291-8a1b-4d28-9c5c
def is_valid_get_polling_interval_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 8291-8a1b-4d28-9c5c
def get_polling_interval_by_id(api):
    endpoint_result = api.devices.get_polling_interval_by_id( path_param_id = get_device_list(api).response[0].id )
    return endpoint_result

# 8291-8a1b-4d28-9c5c
def test_get_polling_interval_by_id(api):
    assert is_valid_get_polling_interval_by_id(get_polling_interval_by_id(api))


# 8db9-3974-4649-a782
def is_valid_get_module_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 8db9-3974-4649-a782
def get_module_count(api):
    endpoint_result = api.devices.get_module_count( param_device_id = get_device_list(api).response[0].id, param_name_list = None, param_operational_state_code_list = None, param_part_number_list = None, param_vendor_equipment_type_list = None )
    return endpoint_result

# 8db9-3974-4649-a782
def test_get_module_count(api):
    assert is_valid_get_module_count(get_module_count(api))


# ba9d-c85b-4b8a-9a17
def is_valid_get_interface_info_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# ba9d-c85b-4b8a-9a17
def get_interface_info_by_id(api):
    endpoint_result = api.devices.get_interface_info_by_id( path_param_device_id = get_device_list(api).response[0].id )
    return endpoint_result

# ba9d-c85b-4b8a-9a17
def test_get_interface_info_by_id(api):
    assert is_valid_get_interface_info_by_id(get_interface_info_by_id(api))


# 819f-9aa5-4fea-b7bf
def is_valid_get_device_summary(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 819f-9aa5-4fea-b7bf
def get_device_summary(api):
    endpoint_result = api.devices.get_device_summary( path_param_id = get_device_list(api).response[0].id )
    return endpoint_result

# 819f-9aa5-4fea-b7bf
def test_get_device_summary(api):
    assert is_valid_get_device_summary(get_device_summary(api))


# c3b3-c9ef-4e6b-8a09
def is_valid_get_functional_capability_for_devices(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# c3b3-c9ef-4e6b-8a09
def get_functional_capability_for_devices(api):
    endpoint_result = api.devices.get_functional_capability_for_devices( param_device_id = get_device_list(api).response[0].id, param_function_name = None )
    return endpoint_result

# c3b3-c9ef-4e6b-8a09
def test_get_functional_capability_for_devices(api):
    assert is_valid_get_functional_capability_for_devices(get_functional_capability_for_devices(api))


# 3d92-3b18-4dc9-a4ca
def is_valid_get_device_interface_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 3d92-3b18-4dc9-a4ca
def get_device_interface_count(api):
    endpoint_result = api.devices.get_device_interface_count(  )
    return endpoint_result

# 3d92-3b18-4dc9-a4ca
def test_get_device_interface_count(api):
    assert is_valid_get_device_interface_count(get_device_interface_count(api))


# eb82-49e3-4f69-b0f1
def is_valid_get_modules(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# eb82-49e3-4f69-b0f1
def get_modules(api):
    endpoint_result = api.devices.get_modules( param_device_id = get_device_list(api).response[0].id, param_limit = None, param_name_list = None, param_offset = None, param_operational_state_code_list = None, param_part_number_list = None, param_vendor_equipment_type_list = None )
    return endpoint_result

# eb82-49e3-4f69-b0f1
def test_get_modules(api):
    assert is_valid_get_modules(get_modules(api))


# f682-6a8e-41bb-a242
def is_valid_get_wireless_lan_controller_details_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# f682-6a8e-41bb-a242
def get_wireless_lan_controller_details_by_id(api):
    endpoint_result = api.devices.get_wireless_lan_controller_details_by_id( path_param_id = get_device_list(api).response[0].id )
    return endpoint_result

# f682-6a8e-41bb-a242
def test_get_wireless_lan_controller_details_by_id(api):
    assert is_valid_get_wireless_lan_controller_details_by_id(get_wireless_lan_controller_details_by_id(api))


# 84b3-7ae5-4c59-ab28
def is_valid_get_organization_list_for_meraki(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 84b3-7ae5-4c59-ab28
def get_organization_list_for_meraki(api):
    endpoint_result = api.devices.get_organization_list_for_meraki( path_param_id = get_device_list(api).response[0].id )
    return endpoint_result

# 84b3-7ae5-4c59-ab28
@pytest.mark.skip(reason="no way of currently testing this")
def test_get_organization_list_for_meraki(api):
    assert is_valid_get_organization_list_for_meraki(get_organization_list_for_meraki(api))


# 70ad-3976-49e9-b4d3
def is_valid_get_ospf_interfaces(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 70ad-3976-49e9-b4d3
def get_ospf_interfaces(api):
    endpoint_result = api.devices.get_ospf_interfaces(  )
    return endpoint_result

# 70ad-3976-49e9-b4d3
def test_get_ospf_interfaces(api):
    assert is_valid_get_ospf_interfaces(get_ospf_interfaces(api))


# 81bb-4804-405a-8d2f
def is_valid_get_functional_capability_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 81bb-4804-405a-8d2f
def get_functional_capability_by_id(api):
    endpoint_result = api.devices.get_functional_capability_by_id( path_param_id = get_functional_capability_for_devices(api).response[0].functionalCapability[0].id )
    return endpoint_result

# 81bb-4804-405a-8d2f
def test_get_functional_capability_by_id(api):
    assert is_valid_get_functional_capability_by_id(get_functional_capability_by_id(api))


# 84ad-8b0e-42ca-b48a
def is_valid_get_isis_interfaces(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 84ad-8b0e-42ca-b48a
def get_isis_interfaces(api):
    endpoint_result = api.devices.get_isis_interfaces(  )
    return endpoint_result

# 84ad-8b0e-42ca-b48a
def test_get_isis_interfaces(api):
    assert is_valid_get_isis_interfaces(get_isis_interfaces(api))


# b7bc-aa08-4e2b-90d0
def is_valid_get_device_config_for_all_devices(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# b7bc-aa08-4e2b-90d0
def get_device_config_for_all_devices(api):
    endpoint_result = api.devices.get_device_config_for_all_devices(  )
    return endpoint_result

# b7bc-aa08-4e2b-90d0
def test_get_device_config_for_all_devices(api):
    assert is_valid_get_device_config_for_all_devices(get_device_config_for_all_devices(api))


# cd84-69e6-47ca-ab0e
def is_valid_get_interface_by_ip(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# cd84-69e6-47ca-ab0e
def get_interface_by_ip(api):
    endpoint_result = api.devices.get_interface_by_ip( path_param_ip_address = list(filter(lambda x: x.ipv4Address is not None, get_all_interfaces(api).response))[0].ipv4Address )
    return endpoint_result

# cd84-69e6-47ca-ab0e
def test_get_interface_by_ip(api):
    assert is_valid_get_interface_by_ip(get_interface_by_ip(api))


# d0a4-b881-45aa-bb51
def is_valid_get_network_device_by_ip(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# d0a4-b881-45aa-bb51
def get_network_device_by_ip(api):
    endpoint_result = api.devices.get_network_device_by_ip( path_param_ip_address = get_device_list(api).response[0].managementIpAddress )
    return endpoint_result

# d0a4-b881-45aa-bb51
def test_get_network_device_by_ip(api):
    assert is_valid_get_network_device_by_ip(get_network_device_by_ip(api))


# 8fa8-eb40-4a4a-8d96
def is_valid_get_device_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 8fa8-eb40-4a4a-8d96
def get_device_by_id(api):
    endpoint_result = api.devices.get_device_by_id( path_param_id = '' )
    return endpoint_result

# 8fa8-eb40-4a4a-8d96
def test_get_device_by_id(api):
    assert is_valid_get_device_by_id(get_device_by_id(api))


# aeb9-eb67-460b-92df
def is_valid_sync_devices(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# aeb9-eb67-460b-92df
def sync_devices(api):
    endpoint_result = api.devices.sync_devices( rq_cliTransport = None, rq_computeDevice = None, rq_enablePassword = None, rq_extendedDiscoveryInfo = None, rq_httpPassword = None, rq_httpPort = None, rq_httpSecure = None, rq_httpUserName = None, rq_ipAddress = None, rq_merakiOrgId = None, rq_netconfPort = None, rq_password = None, rq_serialNumber = None, rq_snmpAuthPassphrase = None, rq_snmpAuthProtocol = None, rq_snmpMode = None, rq_snmpPrivPassphrase = None, rq_snmpPrivProtocol = None, rq_snmpROCommunity = None, rq_snmpRWCommunity = None, rq_snmpRetry = None, rq_snmpTimeout = None, rq_snmpUserName = None, rq_snmpVersion = None, rq_type = None, rq_updateMgmtIPaddressList = None, rq_userName = None )
    return endpoint_result

# aeb9-eb67-460b-92df
def test_sync_devices(api):
    assert is_valid_sync_devices(sync_devices(api))


# b888-792d-43ba-ba46
def is_valid_get_interface_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# b888-792d-43ba-ba46
def get_interface_by_id(api):
    endpoint_result = api.devices.get_interface_by_id( path_param_id = get_all_interfaces(api).response[0].id )
    return endpoint_result

# b888-792d-43ba-ba46
def test_get_interface_by_id(api):
    assert is_valid_get_interface_by_id(get_interface_by_id(api))


# d888-ab6d-4d59-a8c1
def is_valid_get_device_by_serial_number(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# d888-ab6d-4d59-a8c1
def get_device_by_serial_number(api):
    endpoint_result = api.devices.get_device_by_serial_number( path_param_serial_number = get_device_list(api).response[0].serialNumber )
    return endpoint_result

# d888-ab6d-4d59-a8c1
def test_get_device_by_serial_number(api):
    assert is_valid_get_device_by_serial_number(get_device_by_serial_number(api))


# f495-48c5-4be8-a3e2
def is_valid_get_network_device_by_pagination_range(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# f495-48c5-4be8-a3e2
def get_network_device_by_pagination_range(api):
    endpoint_result = api.devices.get_network_device_by_pagination_range( path_param_records_to_return = 4, path_param_start_index = 1 )
    return endpoint_result

# f495-48c5-4be8-a3e2
def test_get_network_device_by_pagination_range(api):
    assert is_valid_get_network_device_by_pagination_range(get_network_device_by_pagination_range(api))


# ffa7-48cc-44e9-a437
def is_valid_retrieves_all_network_devices(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# ffa7-48cc-44e9-a437
def retrieves_all_network_devices(api):
    endpoint_result = api.devices.retrieves_all_network_devices( param_associated_wlc_ip = None, param_collection_interval = None, param_collection_status = None, param_error_code = None, param_family = None, param_hostname = get_device_list(api).response[0].hostname, param_limit = None, param_mac_address = None, param_management_ip_address = None, param_offset = None, param_platform_id = None, param_reachability_failure_reason = None, param_reachability_status = None, param_role = None, param_role_source = None, param_serial_number = None, param_series = None, param_software_type = None, param_software_version = None, param_type = None, param_up_time = None, param_vrf_name = None )
    return endpoint_result

# ffa7-48cc-44e9-a437
def test_retrieves_all_network_devices(api):
    assert is_valid_retrieves_all_network_devices(retrieves_all_network_devices(api))


# 89b2-fb14-4f5b-b09b
def is_valid_get_device_detail(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 89b2-fb14-4f5b-b09b
def get_device_detail(api):
    endpoint_result = api.devices.get_device_detail( param_identifier = 'macAddress', param_search_by = get_device_list(api).response[0].macAddress, param_timestamp = '1561076614' )
    return endpoint_result

# 89b2-fb14-4f5b-b09b
def test_get_device_detail(api):
    assert is_valid_get_device_detail(get_device_detail(api))


# 0db7-da74-4c0b-83d8
def is_valid_get_module_info_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 0db7-da74-4c0b-83d8
def get_module_info_by_id(api):
    endpoint_result = api.devices.get_module_info_by_id( path_param_id = get_device_list(api).response[0].lineCardId.split(',')[0] )
    return endpoint_result

# 0db7-da74-4c0b-83d8
def test_get_module_info_by_id(api):
    assert is_valid_get_module_info_by_id(get_module_info_by_id(api))


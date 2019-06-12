# devices

import pytest
import dnacentersdk


def is_valid_get_module_info_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_module_info_by_id(api):
    endpoint_result = api.devices.get_module_info_by_id( path_param_id = 'c5987ca2-3f69-4341-8cf5-00431f3add0c')
    assert is_valid_get_module_info_by_id(endpoint_result)


def is_valid_get_device_interface_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_interface_count(api):
    endpoint_result = api.devices.get_device_interface_count( )
    assert is_valid_get_device_interface_count(endpoint_result)


def is_valid_sync_devices_using_forcesync(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_sync_devices_using_forcesync(api):
    endpoint_result = api.devices.sync_devices_using_forcesync( param_force_sync = None)
    assert is_valid_sync_devices_using_forcesync(endpoint_result)


def is_valid_get_device_list(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_list(api):
    endpoint_result = api.devices.get_device_list( param_associated_wlc_ip = None, param_collection_interval = None, param_collection_status = None, param_error_code = None, param_error_description = None, param_family = None, param_hostname = None, param_id = None, param_license_name = None, param_license_status = None, param_license_type = None, param_location = None, param_location_name = None, param_mac_address = None, param_management_ip_address = None, param_module_equpimenttype = None, param_module_name = None, param_module_operationstatecode = None, param_module_partnumber = None, param_module_servicestate = None, param_module_vendorequipmenttype = None, param_not_synced_for_minutes = None, param_platform_id = None, param_reachability_status = None, param_role = None, param_serial_number = None, param_series = None, param_software_type = None, param_software_version = None, param_type = None, param_up_time = None)
    assert is_valid_get_device_list(endpoint_result)


def is_valid_get_polling_interval_for_all_devices(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_polling_interval_for_all_devices(api):
    endpoint_result = api.devices.get_polling_interval_for_all_devices( )
    assert is_valid_get_polling_interval_for_all_devices(endpoint_result)


def is_valid_get_device_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_count(api):
    endpoint_result = api.devices.get_device_count( )
    assert is_valid_get_device_count(endpoint_result)


def is_valid_get_device_interface_vlans(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_interface_vlans(api):
    endpoint_result = api.devices.get_device_interface_vlans( path_param_id = '1904ca0d-01be-4d13-88e5-4f4f9980b512', param_interface_type = None)
    assert is_valid_get_device_interface_vlans(endpoint_result)


def is_valid_get_device_interfaces_by_specified_range(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_interfaces_by_specified_range(api):
    endpoint_result = api.devices.get_device_interfaces_by_specified_range( path_param_device_id = '1904ca0d-01be-4d13-88e5-4f4f9980b512', path_param_records_to_return = 1, path_param_start_index = 3)
    assert is_valid_get_device_interfaces_by_specified_range(endpoint_result)


def is_valid_delete_device_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_device_by_id(api):
    endpoint_result = api.devices.delete_device_by_id( path_param_id = '', param_is_force_delete = None)
    assert is_valid_delete_device_by_id(endpoint_result)


def is_valid_get_device_config_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_config_by_id(api):
    endpoint_result = api.devices.get_device_config_by_id( path_param_network_device_id = '1904ca0d-01be-4d13-88e5-4f4f9980b512')
    assert is_valid_get_device_config_by_id(endpoint_result)


def is_valid_add_device(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_add_device(api):
    endpoint_result = api.devices.add_device( rq_cliTransport = None, rq_computeDevice = None, rq_enablePassword = None, rq_extendedDiscoveryInfo = None, rq_httpPassword = None, rq_httpPort = None, rq_httpSecure = None, rq_httpUserName = None, rq_ipAddress = None, rq_merakiOrgId = None, rq_netconfPort = None, rq_password = None, rq_serialNumber = None, rq_snmpAuthPassphrase = None, rq_snmpAuthProtocol = None, rq_snmpMode = None, rq_snmpPrivPassphrase = None, rq_snmpPrivProtocol = None, rq_snmpROCommunity = None, rq_snmpRWCommunity = None, rq_snmpRetry = None, rq_snmpTimeout = None, rq_snmpUserName = None, rq_snmpVersion = None, rq_type = None, rq_updateMgmtIPaddressList = None, rq_userName = None)
    assert is_valid_add_device(endpoint_result)


def is_valid_get_device_config_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_config_count(api):
    endpoint_result = api.devices.get_device_config_count( )
    assert is_valid_get_device_config_count(endpoint_result)


def is_valid_get_interface_details_by_device_id_and_interface_name(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_get_interface_details_by_device_id_and_interface_name(api):
    endpoint_result = api.devices.get_interface_details_by_device_id_and_interface_name( param_name = '', path_param_device_id = '1904ca0d-01be-4d13-88e5-4f4f9980b512')
    assert is_valid_get_interface_details_by_device_id_and_interface_name(endpoint_result)


def is_valid_get_polling_interval_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_polling_interval_by_id(api):
    endpoint_result = api.devices.get_polling_interval_by_id( path_param_id = '1904ca0d-01be-4d13-88e5-4f4f9980b512')
    assert is_valid_get_polling_interval_by_id(endpoint_result)


def is_valid_get_module_count(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_module_count(api):
    endpoint_result = api.devices.get_module_count( param_device_id = '1904ca0d-01be-4d13-88e5-4f4f9980b512', param_name_list = None, param_operational_state_code_list = None, param_part_number_list = None, param_vendor_equipment_type_list = None)
    assert is_valid_get_module_count(endpoint_result)


def is_valid_get_device_interface_count_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_interface_count_by_id(api):
    endpoint_result = api.devices.get_device_interface_count_by_id( path_param_device_id = '1904ca0d-01be-4d13-88e5-4f4f9980b512')
    assert is_valid_get_device_interface_count_by_id(endpoint_result)


def is_valid_get_organization_list_for_meraki(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_get_organization_list_for_meraki(api):
    endpoint_result = api.devices.get_organization_list_for_meraki( path_param_id = '')
    assert is_valid_get_organization_list_for_meraki(endpoint_result)


def is_valid_get_ospf_interfaces(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_ospf_interfaces(api):
    endpoint_result = api.devices.get_ospf_interfaces( )
    assert is_valid_get_ospf_interfaces(endpoint_result)


def is_valid_get_functional_capability_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_get_functional_capability_by_id(api):
    endpoint_result = api.devices.get_functional_capability_by_id( path_param_id = '')
    assert is_valid_get_functional_capability_by_id(endpoint_result)


def is_valid_get_isis_interfaces(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_isis_interfaces(api):
    endpoint_result = api.devices.get_isis_interfaces( )
    assert is_valid_get_isis_interfaces(endpoint_result)


def is_valid_get_device_config_for_all_devices(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_config_for_all_devices(api):
    endpoint_result = api.devices.get_device_config_for_all_devices( )
    assert is_valid_get_device_config_for_all_devices(endpoint_result)


def is_valid_update_device_role(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_device_role(api):
    endpoint_result = api.devices.update_device_role( rq_id = None, rq_role = None, rq_roleSource = None)
    assert is_valid_update_device_role(endpoint_result)


def is_valid_get_interface_info_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_interface_info_by_id(api):
    endpoint_result = api.devices.get_interface_info_by_id( path_param_device_id = '1904ca0d-01be-4d13-88e5-4f4f9980b512')
    assert is_valid_get_interface_info_by_id(endpoint_result)


def is_valid_get_interface_by_ip(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_interface_by_ip(api):
    endpoint_result = api.devices.get_interface_by_ip( path_param_ip_address = '10.2.2.1')
    assert is_valid_get_interface_by_ip(endpoint_result)


def is_valid_get_network_device_by_ip(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_network_device_by_ip(api):
    endpoint_result = api.devices.get_network_device_by_ip( path_param_ip_address = '10.10.22.66')
    assert is_valid_get_network_device_by_ip(endpoint_result)


def is_valid_get_device_summary(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_summary(api):
    endpoint_result = api.devices.get_device_summary( path_param_id = '1904ca0d-01be-4d13-88e5-4f4f9980b512')
    assert is_valid_get_device_summary(endpoint_result)


def is_valid_get_device_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_by_id(api):
    endpoint_result = api.devices.get_device_by_id( path_param_id = '')
    assert is_valid_get_device_by_id(endpoint_result)


def is_valid_get_all_interfaces(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_all_interfaces(api):
    endpoint_result = api.devices.get_all_interfaces( param_limit = 500, param_offset = 1)
    assert is_valid_get_all_interfaces(endpoint_result)


def is_valid_sync_devices(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_sync_devices(api):
    endpoint_result = api.devices.sync_devices( rq_cliTransport = None, rq_computeDevice = None, rq_enablePassword = None, rq_extendedDiscoveryInfo = None, rq_httpPassword = None, rq_httpPort = None, rq_httpSecure = None, rq_httpUserName = None, rq_ipAddress = None, rq_merakiOrgId = None, rq_netconfPort = None, rq_password = None, rq_serialNumber = None, rq_snmpAuthPassphrase = None, rq_snmpAuthProtocol = None, rq_snmpMode = None, rq_snmpPrivPassphrase = None, rq_snmpPrivProtocol = None, rq_snmpROCommunity = None, rq_snmpRWCommunity = None, rq_snmpRetry = None, rq_snmpTimeout = None, rq_snmpUserName = None, rq_snmpVersion = None, rq_type = None, rq_updateMgmtIPaddressList = None, rq_userName = None)
    assert is_valid_sync_devices(endpoint_result)


def is_valid_get_interface_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_interface_by_id(api):
    endpoint_result = api.devices.get_interface_by_id( path_param_id = '')
    assert is_valid_get_interface_by_id(endpoint_result)


def is_valid_get_functional_capability_for_devices(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_functional_capability_for_devices(api):
    endpoint_result = api.devices.get_functional_capability_for_devices( param_device_id = '1904ca0d-01be-4d13-88e5-4f4f9980b512', param_function_name = None)
    assert is_valid_get_functional_capability_for_devices(endpoint_result)


def is_valid_register_device_for_wsa(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_register_device_for_wsa(api):
    endpoint_result = api.devices.register_device_for_wsa( param_macaddress = '', param_serial_number = '')
    assert is_valid_register_device_for_wsa(endpoint_result)


def is_valid_get_device_by_serial_number(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_by_serial_number(api):
    endpoint_result = api.devices.get_device_by_serial_number( path_param_serial_number = 'FXS1932Q1SE')
    assert is_valid_get_device_by_serial_number(endpoint_result)


def is_valid_export_device_list(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_export_device_list(api):
    endpoint_result = api.devices.export_device_list( rq_deviceUuids = None, rq_id = None, rq_operationEnum = None, rq_parameters = None, rq_password = None)
    assert is_valid_export_device_list(endpoint_result)


def is_valid_get_network_device_by_pagination_range(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_network_device_by_pagination_range(api):
    endpoint_result = api.devices.get_network_device_by_pagination_range( path_param_records_to_return = 14, path_param_start_index = 1)
    assert is_valid_get_network_device_by_pagination_range(endpoint_result)


def is_valid_retrieves_all_network_devices(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_retrieves_all_network_devices(api):
    endpoint_result = api.devices.retrieves_all_network_devices( param_associated_wlc_ip = None, param_collection_interval = None, param_collection_status = None, param_error_code = None, param_family = None, param_hostname = 'cat_9k_1', param_limit = None, param_mac_address = None, param_management_ip_address = None, param_offset = None, param_platform_id = None, param_reachability_failure_reason = None, param_reachability_status = None, param_role = None, param_role_source = None, param_serial_number = None, param_series = None, param_software_type = None, param_software_version = None, param_type = None, param_up_time = None, param_vrf_name = None)
    assert is_valid_retrieves_all_network_devices(endpoint_result)


def is_valid_get_modules(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_modules(api):
    endpoint_result = api.devices.get_modules( param_device_id = '1904ca0d-01be-4d13-88e5-4f4f9980b512', param_limit = None, param_name_list = None, param_offset = None, param_operational_state_code_list = None, param_part_number_list = None, param_vendor_equipment_type_list = None)
    assert is_valid_get_modules(endpoint_result)


def is_valid_get_wireless_lan_controller_details_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_wireless_lan_controller_details_by_id(api):
    endpoint_result = api.devices.get_wireless_lan_controller_details_by_id( path_param_id = '1904ca0d-01be-4d13-88e5-4f4f9980b512')
    assert is_valid_get_wireless_lan_controller_details_by_id(endpoint_result)


def is_valid_get_device_detail(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_detail(api):
    endpoint_result = api.devices.get_device_detail( param_identifier = '', param_search_by = '', param_timestamp = '1560378629')
    assert is_valid_get_device_detail(endpoint_result)


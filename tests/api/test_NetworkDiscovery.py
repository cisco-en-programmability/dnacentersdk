# network_discovery

import pytest
import dnacentersdk


def is_valid_get_count_of_all_discovery_jobs(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_count_of_all_discovery_jobs(api):
    endpoint_result = api.network_discovery.get_count_of_all_discovery_jobs( )
    assert is_valid_get_count_of_all_discovery_jobs(endpoint_result)


def is_valid_create_netconf_credentials(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_netconf_credentials(api):
    endpoint_result = api.network_discovery.create_netconf_credentials( )
    assert is_valid_create_netconf_credentials(endpoint_result)


def is_valid_update_snmp_write_community(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_snmp_write_community(api):
    endpoint_result = api.network_discovery.update_snmp_write_community( rq_comments = None, rq_credentialType = None, rq_description = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_writeCommunity = None)
    assert is_valid_update_snmp_write_community(endpoint_result)


def is_valid_update_snmpv3_credentials(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_snmpv3_credentials(api):
    endpoint_result = api.network_discovery.update_snmpv3_credentials( rq_authPassword = None, rq_authType = None, rq_comments = None, rq_credentialType = None, rq_description = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_privacyPassword = None, rq_privacyType = None, rq_snmpMode = None, rq_username = None)
    assert is_valid_update_snmpv3_credentials(endpoint_result)


def is_valid_get_snmp_properties(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_snmp_properties(api):
    endpoint_result = api.network_discovery.get_snmp_properties( )
    assert is_valid_get_snmp_properties(endpoint_result)


def is_valid_delete_discovery_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_discovery_by_id(api):
    endpoint_result = api.network_discovery.delete_discovery_by_id( path_param_id = '')
    assert is_valid_delete_discovery_by_id(endpoint_result)


def is_valid_start_discovery(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_start_discovery(api):
    endpoint_result = api.network_discovery.start_discovery( rq_cdpLevel = None, rq_discoveryType = None, rq_enablePasswordList = None, rq_globalCredentialIdList = None, rq_httpReadCredential = None, rq_httpWriteCredential = None, rq_ipAddressList = None, rq_ipFilterList = None, rq_lldpLevel = None, rq_name = None, rq_netconfPort = None, rq_noAddNewDevice = None, rq_parentDiscoveryId = None, rq_passwordList = None, rq_preferredMgmtIPMethod = None, rq_protocolOrder = None, rq_reDiscovery = None, rq_retry = None, rq_snmpAuthPassphrase = None, rq_snmpAuthProtocol = None, rq_snmpMode = None, rq_snmpPrivPassphrase = None, rq_snmpPrivProtocol = None, rq_snmpROCommunity = None, rq_snmpROCommunityDesc = None, rq_snmpRWCommunity = None, rq_snmpRWCommunityDesc = None, rq_snmpUserName = None, rq_snmpVersion = None, rq_timeout = None, rq_updateMgmtIp = None, rq_userNameList = None)
    assert is_valid_start_discovery(endpoint_result)


def is_valid_create_snmp_write_community(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_snmp_write_community(api):
    endpoint_result = api.network_discovery.create_snmp_write_community( )
    assert is_valid_create_snmp_write_community(endpoint_result)


def is_valid_create_http_write_credentials(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_http_write_credentials(api):
    endpoint_result = api.network_discovery.create_http_write_credentials( )
    assert is_valid_create_http_write_credentials(endpoint_result)


def is_valid_get_network_devices_from_discovery(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_network_devices_from_discovery(api):
    endpoint_result = api.network_discovery.get_network_devices_from_discovery( path_param_id = '', param_cli_status = None, param_http_status = None, param_ip_address = None, param_netconf_status = None, param_ping_status = None, param_snmp_status = None, param_sort_by = None, param_sort_order = None, param_task_id = None)
    assert is_valid_get_network_devices_from_discovery(endpoint_result)


def is_valid_update_global_credentials(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_global_credentials(api):
    endpoint_result = api.network_discovery.update_global_credentials( path_param_global_credential_id = '', rq_siteUuids = None)
    assert is_valid_update_global_credentials(endpoint_result)


def is_valid_get_discoveries_by_range(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_discoveries_by_range(api):
    endpoint_result = api.network_discovery.get_discoveries_by_range( path_param_records_to_return = '', path_param_start_index = '')
    assert is_valid_get_discoveries_by_range(endpoint_result)


def is_valid_create_snmp_read_community(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_snmp_read_community(api):
    endpoint_result = api.network_discovery.create_snmp_read_community( )
    assert is_valid_create_snmp_read_community(endpoint_result)


def is_valid_get_discovery_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_discovery_by_id(api):
    endpoint_result = api.network_discovery.get_discovery_by_id( path_param_id = '')
    assert is_valid_get_discovery_by_id(endpoint_result)


def is_valid_updates_an_existing_discovery_by_specified_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_updates_an_existing_discovery_by_specified_id(api):
    endpoint_result = api.network_discovery.updates_an_existing_discovery_by_specified_id( rq_attributeInfo = None, rq_cdpLevel = None, rq_deviceIds = None, rq_discoveryCondition = None, rq_discoveryStatus = None, rq_discoveryType = None, rq_enablePasswordList = None, rq_globalCredentialIdList = None, rq_httpReadCredential = None, rq_httpWriteCredential = None, rq_id = None, rq_ipAddressList = None, rq_ipFilterList = None, rq_isAutoCdp = None, rq_lldpLevel = None, rq_name = None, rq_netconfPort = None, rq_numDevices = None, rq_parentDiscoveryId = None, rq_passwordList = None, rq_preferredMgmtIPMethod = None, rq_protocolOrder = None, rq_retryCount = None, rq_snmpAuthPassphrase = None, rq_snmpAuthProtocol = None, rq_snmpMode = None, rq_snmpPrivPassphrase = None, rq_snmpPrivProtocol = None, rq_snmpRoCommunity = None, rq_snmpRoCommunityDesc = None, rq_snmpRwCommunity = None, rq_snmpRwCommunityDesc = None, rq_snmpUserName = None, rq_timeOut = None, rq_updateMgmtIp = None, rq_userNameList = None)
    assert is_valid_updates_an_existing_discovery_by_specified_id(endpoint_result)


def is_valid_create_cli_credentials(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_cli_credentials(api):
    endpoint_result = api.network_discovery.create_cli_credentials( )
    assert is_valid_create_cli_credentials(endpoint_result)


def is_valid_update_snmp_read_community(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_snmp_read_community(api):
    endpoint_result = api.network_discovery.update_snmp_read_community( rq_comments = None, rq_credentialType = None, rq_description = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_readCommunity = None)
    assert is_valid_update_snmp_read_community(endpoint_result)


def is_valid_get_list_of_discoveries_by_discovery_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_list_of_discoveries_by_discovery_id(api):
    endpoint_result = api.network_discovery.get_list_of_discoveries_by_discovery_id( path_param_id = '', param_ip_address = None, param_limit = None, param_offset = None)
    assert is_valid_get_list_of_discoveries_by_discovery_id(endpoint_result)


def is_valid_create_update_snmp_properties(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_update_snmp_properties(api):
    endpoint_result = api.network_discovery.create_update_snmp_properties( )
    assert is_valid_create_update_snmp_properties(endpoint_result)


def is_valid_get_discovery_jobs_by_ip(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_discovery_jobs_by_ip(api):
    endpoint_result = api.network_discovery.get_discovery_jobs_by_ip( param_ip_address = '', param_limit = None, param_name = None, param_offset = None)
    assert is_valid_get_discovery_jobs_by_ip(endpoint_result)


def is_valid_get_discovered_devices_by_range(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_discovered_devices_by_range(api):
    endpoint_result = api.network_discovery.get_discovered_devices_by_range( path_param_id = '', path_param_records_to_return = '', path_param_start_index = '', param_task_id = None)
    assert is_valid_get_discovered_devices_by_range(endpoint_result)


def is_valid_get_credential_sub_type_by_credential_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_credential_sub_type_by_credential_id(api):
    endpoint_result = api.network_discovery.get_credential_sub_type_by_credential_id( path_param_id = '')
    assert is_valid_get_credential_sub_type_by_credential_id(endpoint_result)


def is_valid_update_http_write_credentials(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_http_write_credentials(api):
    endpoint_result = api.network_discovery.update_http_write_credentials( rq_comments = None, rq_credentialType = None, rq_description = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_password = None, rq_port = None, rq_secure = None, rq_username = None)
    assert is_valid_update_http_write_credentials(endpoint_result)


def is_valid_delete_discovery_by_specified_range(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_discovery_by_specified_range(api):
    endpoint_result = api.network_discovery.delete_discovery_by_specified_range( path_param_records_to_delete = '', path_param_start_index = '')
    assert is_valid_delete_discovery_by_specified_range(endpoint_result)


def is_valid_create_http_read_credentials(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_http_read_credentials(api):
    endpoint_result = api.network_discovery.create_http_read_credentials( )
    assert is_valid_create_http_read_credentials(endpoint_result)


def is_valid_update_netconf_credentials(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_netconf_credentials(api):
    endpoint_result = api.network_discovery.update_netconf_credentials( rq_comments = None, rq_credentialType = None, rq_description = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_netconfPort = None)
    assert is_valid_update_netconf_credentials(endpoint_result)


def is_valid_delete_all_discovery(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_all_discovery(api):
    endpoint_result = api.network_discovery.delete_all_discovery( )
    assert is_valid_delete_all_discovery(endpoint_result)


def is_valid_delete_global_credentials_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_global_credentials_by_id(api):
    endpoint_result = api.network_discovery.delete_global_credentials_by_id( path_param_global_credential_id = '')
    assert is_valid_delete_global_credentials_by_id(endpoint_result)


def is_valid_update_http_read_credential(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_http_read_credential(api):
    endpoint_result = api.network_discovery.update_http_read_credential( rq_comments = None, rq_credentialType = None, rq_description = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_password = None, rq_port = None, rq_secure = None, rq_username = None)
    assert is_valid_update_http_read_credential(endpoint_result)


def is_valid_update_cli_credentials(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_cli_credentials(api):
    endpoint_result = api.network_discovery.update_cli_credentials( rq_comments = None, rq_credentialType = None, rq_description = None, rq_enablePassword = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_password = None, rq_username = None)
    assert is_valid_update_cli_credentials(endpoint_result)


def is_valid_create_snmpv3_credentials(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_snmpv3_credentials(api):
    endpoint_result = api.network_discovery.create_snmpv3_credentials( )
    assert is_valid_create_snmpv3_credentials(endpoint_result)


def is_valid_get_devices_discovered_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_devices_discovered_by_id(api):
    endpoint_result = api.network_discovery.get_devices_discovered_by_id( path_param_id = '', param_task_id = None)
    assert is_valid_get_devices_discovered_by_id(endpoint_result)


def is_valid_get_discovered_network_devices_by_discovery_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_discovered_network_devices_by_discovery_id(api):
    endpoint_result = api.network_discovery.get_discovered_network_devices_by_discovery_id( path_param_id = '', param_task_id = None)
    assert is_valid_get_discovered_network_devices_by_discovery_id(endpoint_result)


def is_valid_get_global_credentials(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_global_credentials(api):
    endpoint_result = api.network_discovery.get_global_credentials( param_credential_sub_type = '', param_order = None, param_sort_by = None)
    assert is_valid_get_global_credentials(endpoint_result)


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
import time
from tests.environment import DNA_CENTER_VERSION
from tests.config import MERAKI_ORG_ID


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_get_device_interface_count(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_interface_count(api):
    endpoint_result = api.devices.get_device_interface_count(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count(api):
    assert is_valid_get_device_interface_count(
        get_device_interface_count(api)
    )


def is_valid_get_device_list(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_list(api):
    endpoint_result = api.devices.get_device_list(
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        error_code=None,
        error_description=None,
        family=None,
        hostname=None,
        id=None,
        license_name=None,
        license_status=None,
        license_type=None,
        location=None,
        location_name=None,
        mac_address=None,
        management_ip_address=None,
        module_equpimenttype=None,
        module_name=None,
        module_operationstatecode=None,
        module_partnumber=None,
        module_servicestate=None,
        module_vendorequipmenttype=None,
        not_synced_for_minutes=None,
        platform_id=None,
        reachability_status=None,
        role=None,
        serial_number=None,
        series=None,
        software_type=None,
        software_version=None,
        type=None,
        up_time=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_list(api):
    assert is_valid_get_device_list(
        get_device_list(api)
    )


def is_valid_sync_devices_using_forcesync(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def sync_devices_using_forcesync(api):
    endpoint_result = api.devices.sync_devices_using_forcesync(
        force_sync=None,
        payload=['get_device_list(api).response[0].id'],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices_using_forcesync(api):
    assert is_valid_sync_devices_using_forcesync(
        sync_devices_using_forcesync(api)
    )


def is_valid_get_polling_interval_for_all_devices(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_polling_interval_for_all_devices(api):
    endpoint_result = api.devices.get_polling_interval_for_all_devices(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_for_all_devices(api):
    assert is_valid_get_polling_interval_for_all_devices(
        get_polling_interval_for_all_devices(api)
    )


def is_valid_get_device_count(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_count(api):
    endpoint_result = api.devices.get_device_count(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_count(api):
    assert is_valid_get_device_count(
        get_device_count(api)
    )


def is_valid_get_device_interface_vlans(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_interface_vlans(api):
    devices = api.devices.get_device_list().response
    devices_filtered = [device if 'Switches and Hubs' in device.family
                        and device.interfaceCount and device.interfaceCount > "1"
                        else None for device in devices]
    devices_filtered = list(filter(lambda x: x, devices_filtered))
    endpoint_result = api.devices.get_device_interface_vlans(
        id=devices_filtered[0].id,
        interface_type=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_vlans(api):
    assert is_valid_get_device_interface_vlans(
        get_device_interface_vlans(api)
    )


def is_valid_get_device_interfaces_by_specified_range(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_interfaces_by_specified_range(api):
    endpoint_result = api.devices.get_device_interfaces_by_specified_range(
        device_id=get_device_list(api).response[0].id,
        records_to_return=1,
        start_index=3,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interfaces_by_specified_range(api):
    assert is_valid_get_device_interfaces_by_specified_range(
        get_device_interfaces_by_specified_range(api)
    )


def is_valid_get_device_config_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_config_by_id(api):
    endpoint_result = api.devices.get_device_config_by_id(
        network_device_id=get_device_list(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_by_id(api):
    assert is_valid_get_device_config_by_id(
        get_device_config_by_id(api)
    )


def is_valid_get_device_config_count(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_config_count(api):
    endpoint_result = api.devices.get_device_config_count(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_count(api):
    assert is_valid_get_device_config_count(
        get_device_config_count(api)
    )


def is_valid_get_all_interfaces(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_all_interfaces(api):
    endpoint_result = api.devices.get_all_interfaces(
        limit=500,
        offset=1,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_interfaces(api):
    assert is_valid_get_all_interfaces(
        get_all_interfaces(api)
    )


def is_valid_get_interface_details(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_interface_details(api):
    endpoint_result = api.devices.get_interface_details(
        device_id=get_device_list(api).response[0].id,
        name=get_device_interface_vlans(api).response[0].interfaceName,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_details(api):
    assert is_valid_get_interface_details(
        get_interface_details(api)
    )


def is_valid_get_polling_interval_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_polling_interval_by_id(api):
    endpoint_result = api.devices.get_polling_interval_by_id(
        id=get_device_list(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_by_id(api):
    assert is_valid_get_polling_interval_by_id(
        get_polling_interval_by_id(api)
    )


def is_valid_get_module_count(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_module_count(api):
    endpoint_result = api.devices.get_module_count(
        device_id=get_device_list(api).response[0].id,
        name_list=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_count(api):
    assert is_valid_get_module_count(
        get_module_count(api)
    )


def is_valid_get_interface_info_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_interface_info_by_id(api):
    endpoint_result = api.devices.get_interface_info_by_id(
        device_id=get_device_list(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_info_by_id(api):
    assert is_valid_get_interface_info_by_id(
        get_interface_info_by_id(api)
    )


def is_valid_get_device_summary(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_summary(api):
    endpoint_result = api.devices.get_device_summary(
        id=get_device_list(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_summary(api):
    assert is_valid_get_device_summary(
        get_device_summary(api)
    )


def is_valid_get_functional_capability_for_devices(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_functional_capability_for_devices(api):
    endpoint_result = api.devices.get_functional_capability_for_devices(
        device_id=get_device_list(api).response[0].id,
        function_name=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_for_devices(api):
    assert is_valid_get_functional_capability_for_devices(
        get_functional_capability_for_devices(api)
    )


def is_valid_get_device_interface_count_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_interface_count_by_id(api):
    endpoint_result = api.devices.get_device_interface_count_by_id(
        device_id=get_device_list(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count_by_id(api):
    assert is_valid_get_device_interface_count_by_id(
        get_device_interface_count_by_id(api)
    )


def is_valid_get_modules(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_modules(api):
    endpoint_result = api.devices.get_modules(
        device_id=get_device_list(api).response[0].id,
        limit=None,
        name_list=None,
        offset=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_modules(api):
    assert is_valid_get_modules(
        get_modules(api)
    )


def is_valid_get_wireless_lan_controller_details_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_wireless_lan_controller_details_by_id(api):
    endpoint_result = api.devices.get_wireless_lan_controller_details_by_id(
        id=get_device_list(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_wireless_lan_controller_details_by_id(api):
    assert is_valid_get_wireless_lan_controller_details_by_id(
        get_wireless_lan_controller_details_by_id(api)
    )


def is_valid_get_organization_list_for_meraki(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_organization_list_for_meraki(api):
    sub_type = "SNMPV2_READ_COMMUNITY"
    credentials = api.network_discovery.get_global_credentials(credential_sub_type=sub_type).response
    device_list_ips = [d.managementIpAddress for d in api.devices.get_device_list().response]
    device_ip = device_list_ips[0]
    a = list(filter(lambda x: x.rsplit('.', 1)[0] == device_ip.rsplit('.', 1)[0], device_list_ips))
    b = set(range(2, 103)) - set([int(x.rsplit('.', 1)[-1]) for x in a])
    new_ipAddress = device_ip.rsplit('.', 1)[0] + '.' + str(list(b)[0])
    api.devices.add_device(
        cliTransport="ssh",
        enablePassword="false",
        ipAddress=[new_ipAddress],
        merakiOrgId=MERAKI_ORG_ID,
        password="W.~&KV9ha",
        snmpMode="NOAUTHNOPRIV",
        snmpROCommunity=credentials[0].id,
        snmpRWCommunity="",
        snmpRetry=0,
        snmpTimeout=0,
        snmpUserName="test_user_devnet",
        snmpVersion="v2",
        type="NETWORK_DEVICE",
        userName="test_user_devnet",
        active_validation=True
    )
    time.sleep(10)
    filtered_device_list = api.devices.get_device_list(
        family='null', hostname='null', software_type='null',
        management_ip_address=new_ipAddress
    ).response
    endpoint_result = api.devices.get_organization_list_for_meraki(
        id=filtered_device_list[0].id,
        payload=None,
        active_validation=True
    )
    time.sleep(10)
    api.devices.delete_device_by_id(
        id=filtered_device_list[0].id,
        is_force_delete=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([MERAKI_ORG_ID]) is True,
                    reason="tests.config values required not present")
@pytest.mark.devices
def test_get_organization_list_for_meraki(api):
    assert is_valid_get_organization_list_for_meraki(
        get_organization_list_for_meraki(api)
    )


def is_valid_get_ospf_interfaces(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_ospf_interfaces(api):
    endpoint_result = api.devices.get_ospf_interfaces(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_ospf_interfaces(api):
    assert is_valid_get_ospf_interfaces(
        get_ospf_interfaces(api)
    )


def is_valid_get_functional_capability_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_functional_capability_by_id(api):
    functional_capability_devices = get_functional_capability_for_devices(api).response
    functional_capability = functional_capability_devices[0].functionalCapability[0]
    endpoint_result = api.devices.get_functional_capability_by_id(
        id=functional_capability.id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_by_id(api):
    assert is_valid_get_functional_capability_by_id(
        get_functional_capability_by_id(api)
    )


def is_valid_get_isis_interfaces(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_isis_interfaces(api):
    endpoint_result = api.devices.get_isis_interfaces(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_isis_interfaces(api):
    assert is_valid_get_isis_interfaces(
        get_isis_interfaces(api)
    )


def is_valid_get_device_config_for_all_devices(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_config_for_all_devices(api):
    endpoint_result = api.devices.get_device_config_for_all_devices(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_for_all_devices(api):
    assert is_valid_get_device_config_for_all_devices(
        get_device_config_for_all_devices(api)
    )


def is_valid_get_interface_by_ip(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_interface_by_ip(api):
    interfaces = get_all_interfaces(api).response
    filtered_interfaces = list(filter(lambda x: x.ipv4Address is not None, interfaces))
    endpoint_result = api.devices.get_interface_by_ip(
        ip_address=filtered_interfaces[0].ipv4Address,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_ip(api):
    assert is_valid_get_interface_by_ip(
        get_interface_by_ip(api)
    )


def is_valid_get_network_device_by_ip(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_network_device_by_ip(api):
    endpoint_result = api.devices.get_network_device_by_ip(
        ip_address=get_device_list(api).response[0].managementIpAddress,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_ip(api):
    assert is_valid_get_network_device_by_ip(
        get_network_device_by_ip(api)
    )


def is_valid_get_device_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_by_id(api):
    endpoint_result = api.devices.get_device_by_id(
        id=get_device_list(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_id(api):
    assert is_valid_get_device_by_id(
        get_device_by_id(api)
    )


def is_valid_sync_devices(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def sync_devices(api):
    endpoint_result = api.devices.sync_devices(
        cliTransport=None,
        computeDevice=None,
        enablePassword=None,
        extendedDiscoveryInfo=None,
        httpPassword=None,
        httpPort=None,
        httpSecure=None,
        httpUserName=None,
        ipAddress=None,
        merakiOrgId=None,
        netconfPort=None,
        password=None,
        serialNumber=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpRWCommunity=None,
        snmpRetry=None,
        snmpTimeout=None,
        snmpUserName=None,
        snmpVersion=None,
        type=None,
        updateMgmtIPaddressList=None,
        userName=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices(api):
    assert is_valid_sync_devices(
        sync_devices(api)
    )


def is_valid_get_interface_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_interface_by_id(api):
    endpoint_result = api.devices.get_interface_by_id(
        id=get_all_interfaces(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_id(api):
    assert is_valid_get_interface_by_id(
        get_interface_by_id(api)
    )


def is_valid_get_device_by_serial_number(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_by_serial_number(api):
    device_list = get_device_list(api).response
    filtered_device_list = list(filter(lambda x: x.serialNumber, device_list))
    endpoint_result = api.devices.get_device_by_serial_number(
        serial_number=filtered_device_list[0].serialNumber,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_serial_number(api):
    assert is_valid_get_device_by_serial_number(
        get_device_by_serial_number(api)
    )


def is_valid_get_network_device_by_pagination_range(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_network_device_by_pagination_range(api):
    endpoint_result = api.devices.get_network_device_by_pagination_range(
        records_to_return=4,
        start_index=1,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_pagination_range(api):
    assert is_valid_get_network_device_by_pagination_range(
        get_network_device_by_pagination_range(api)
    )


def is_valid_retrieves_all_network_devices(obj):
    some_keys = []
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def retrieves_all_network_devices(api):
    endpoint_result = api.devices.retrieves_all_network_devices(
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        error_code=None,
        family=None,
        hostname=get_device_list(api).response[0].hostname,
        limit=None,
        mac_address=None,
        management_ip_address=None,
        offset=None,
        platform_id=None,
        reachability_failure_reason=None,
        reachability_status=None,
        role=None,
        role_source=None,
        serial_number=None,
        series=None,
        software_type=None,
        software_version=None,
        type=None,
        up_time=None,
        vrf_name=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_all_network_devices(api):
    assert is_valid_retrieves_all_network_devices(
        retrieves_all_network_devices(api)
    )


def is_valid_get_device_detail(obj):
    some_keys = ['response']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_detail(api):
    endpoint_result = api.devices.get_device_detail(
        identifier='macAddress',
        search_by=get_device_list(api).response[0].macAddress,
        timestamp='',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_detail(api):
    assert is_valid_get_device_detail(
        get_device_detail(api)
    )


def is_valid_get_module_info_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_module_info_by_id(api):
    endpoint_result = api.devices.get_module_info_by_id(
        id=get_device_list(api).response[0].lineCardId.split(',')[0],
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_info_by_id(api):
    assert is_valid_get_module_info_by_id(
        get_module_info_by_id(api)
    )


def is_valid_add_device(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def add_device(api):
    sub_type = "SNMPV2_READ_COMMUNITY"
    credentials = api.network_discovery.get_global_credentials(credential_sub_type=sub_type).response
    device_list_ips = [d.managementIpAddress for d in api.devices.get_device_list().response]
    device_ip = device_list_ips[0]
    a = list(filter(lambda x: x.rsplit('.', 1)[0] == device_ip.rsplit('.', 1)[0], device_list_ips))
    b = set(range(2, 103)) - set([int(x.rsplit('.', 1)[-1]) for x in a])
    new_ipAddress = device_ip.rsplit('.', 1)[0] + '.' + str(list(b)[0])
    endpoint_result = api.devices.add_device(
        cliTransport=None,
        computeDevice=None,
        enablePassword=None,
        extendedDiscoveryInfo=None,
        httpPassword=None,
        httpPort=None,
        httpSecure=None,
        httpUserName=None,
        ipAddress=[new_ipAddress],
        merakiOrgId=None,
        netconfPort=None,
        password=None,
        serialNumber=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpRWCommunity=None,
        snmpRetry=None,
        snmpTimeout=None,
        snmpUserName=None,
        snmpVersion=None,
        type=None,
        updateMgmtIPaddressList=None,
        userName=None,
        payload={
            "cliTransport": "ssh",
            "enablePassword": "false",
            "snmpMode": "NOAUTHNOPRIV",
            "snmpROCommunity": credentials[0].id,
            "snmpRWCommunity": "",
            "snmpRetry": 0,
            "snmpTimeout": 0,
            "snmpUserName": "test_user_devnet",
            "snmpVersion": "v2",
            "type": "NETWORK_DEVICE",
            "userName": "test_user_devnet",
            "password": "W.~&KV9ha"
        },
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_add_device(api):
    assert is_valid_add_device(
        add_device(api)
    )


def is_valid_get_device_by_id_last(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_by_id_last(api):
    endpoint_result = api.devices.get_device_by_id(
        id=get_device_list(api).response[-1].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_id_last(api):
    assert is_valid_get_device_by_id_last(
        get_device_by_id_last(api)
    )


def is_valid_update_device_role(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_device_role(api):
    endpoint_result = api.devices.update_device_role(
        id=get_device_list(api).response[0].id,
        role=get_device_list(api).response[0].role,
        roleSource=get_device_list(api).response[0].roleSource,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_role(api):
    assert is_valid_update_device_role(
        update_device_role(api)
    )


def is_valid_register_device_for_wsa(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def register_device_for_wsa(api):
    endpoint_result = api.devices.register_device_for_wsa(
        macaddress=get_device_list(api).response[0].macAddress,
        serial_number=get_device_list(api).response[0].serialNumber,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_register_device_for_wsa(api):
    assert is_valid_register_device_for_wsa(
        register_device_for_wsa(api)
    )


def is_valid_export_device_list(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def export_device_list(api):
    endpoint_result = api.devices.export_device_list(
        deviceUuids=[get_device_list(api).response[0].id],
        id=get_device_list(api).response[0].id,
        operationEnum='CREDENTIALDETAILS',
        parameters=None,
        password=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_export_device_list(api):
    assert is_valid_export_device_list(
        export_device_list(api)
    )


def is_valid_delete_device_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_device_by_id(api):
    filtered_device_list = api.devices.get_device_list(
        family='null', hostname='null', software_type='null'
    ).response
    endpoint_result = api.devices.delete_device_by_id(
        id=filtered_device_list[0].id,
        is_force_delete=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_device_by_id(api):
    assert is_valid_delete_device_by_id(
        delete_device_by_id(api)
    )

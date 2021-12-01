# -*- coding: utf-8 -*-
"""DNACenterAPI devices API fixtures and tests.

Copyright (c) 2019-2021 Cisco Systems.

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
from fastjsonschema.exceptions import JsonSchemaException
from dnacentersdk.exceptions import MalformedRequest
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.3.3', reason='version does not match')


def is_valid_get_device_detail(json_schema_validate, obj):
    json_schema_validate('jsd_560c9ee787eb5a0391309f45ddf392ca_v2_2_3_3').validate(obj)
    return True


def get_device_detail(api):
    endpoint_result = api.devices.get_device_detail(
        identifier='string',
        search_by='string',
        timestamp='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_detail(api, validator):
    try:
        assert is_valid_get_device_detail(
            validator,
            get_device_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_detail_default_val(api):
    endpoint_result = api.devices.get_device_detail(
        identifier=None,
        search_by=None,
        timestamp=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_detail_default_val(api, validator):
    try:
        assert is_valid_get_device_detail(
            validator,
            get_device_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_enrichment_details(json_schema_validate, obj):
    json_schema_validate('jsd_08a20c25e0fa518bb186fd7747450ef6_v2_2_3_3').validate(obj)
    return True


def get_device_enrichment_details(api):
    endpoint_result = api.devices.get_device_enrichment_details(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_enrichment_details(api, validator):
    try:
        assert is_valid_get_device_enrichment_details(
            validator,
            get_device_enrichment_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_enrichment_details_default_val(api):
    endpoint_result = api.devices.get_device_enrichment_details(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_enrichment_details_default_val(api, validator):
    try:
        assert is_valid_get_device_enrichment_details(
            validator,
            get_device_enrichment_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_devices(json_schema_validate, obj):
    json_schema_validate('jsd_c75e364632e15384a18063458e2ba0e3_v2_2_3_3').validate(obj)
    return True


def devices(api):
    endpoint_result = api.devices.devices(
        device_role='string',
        end_time=0,
        health='string',
        limit=0,
        offset=0,
        site_id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.devices
def test_devices(api, validator):
    try:
        assert is_valid_devices(
            validator,
            devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def devices_default_val(api):
    endpoint_result = api.devices.devices(
        device_role=None,
        end_time=None,
        health=None,
        limit=None,
        offset=None,
        site_id=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_devices_default_val(api, validator):
    try:
        assert is_valid_devices(
            validator,
            devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_interfaces(json_schema_validate, obj):
    json_schema_validate('jsd_22d3d71136d95562afc211b40004d109_v2_2_3_3').validate(obj)
    return True


def get_all_interfaces(api):
    endpoint_result = api.devices.get_all_interfaces(
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_interfaces(api, validator):
    try:
        assert is_valid_get_all_interfaces(
            validator,
            get_all_interfaces(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_interfaces_default_val(api):
    endpoint_result = api.devices.get_all_interfaces(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_interfaces_default_val(api, validator):
    try:
        assert is_valid_get_all_interfaces(
            validator,
            get_all_interfaces_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_count(json_schema_validate, obj):
    json_schema_validate('jsd_0da44fbc3e415a99aac0bdd291e9a87a_v2_2_3_3').validate(obj)
    return True


def get_device_interface_count(api):
    endpoint_result = api.devices.get_device_interface_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count(api, validator):
    try:
        assert is_valid_get_device_interface_count(
            validator,
            get_device_interface_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_interface_count_default_val(api):
    endpoint_result = api.devices.get_device_interface_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count_default_val(api, validator):
    try:
        assert is_valid_get_device_interface_count(
            validator,
            get_device_interface_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_by_ip(json_schema_validate, obj):
    json_schema_validate('jsd_cf7fa95e3ed4527aa5ba8ca871a8c142_v2_2_3_3').validate(obj)
    return True


def get_interface_by_ip(api):
    endpoint_result = api.devices.get_interface_by_ip(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_ip(api, validator):
    try:
        assert is_valid_get_interface_by_ip(
            validator,
            get_interface_by_ip(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interface_by_ip_default_val(api):
    endpoint_result = api.devices.get_interface_by_ip(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_ip_default_val(api, validator):
    try:
        assert is_valid_get_interface_by_ip(
            validator,
            get_interface_by_ip_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_isis_interfaces(json_schema_validate, obj):
    json_schema_validate('jsd_af71ea437c8755869b00d26ba9234dff_v2_2_3_3').validate(obj)
    return True


def get_isis_interfaces(api):
    endpoint_result = api.devices.get_isis_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_isis_interfaces(api, validator):
    try:
        assert is_valid_get_isis_interfaces(
            validator,
            get_isis_interfaces(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_isis_interfaces_default_val(api):
    endpoint_result = api.devices.get_isis_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_isis_interfaces_default_val(api, validator):
    try:
        assert is_valid_get_isis_interfaces(
            validator,
            get_isis_interfaces_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_info_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_e057192b97615f0d99a10e2b66bab13a_v2_2_3_3').validate(obj)
    return True


def get_interface_info_by_id(api):
    endpoint_result = api.devices.get_interface_info_by_id(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_info_by_id(api, validator):
    try:
        assert is_valid_get_interface_info_by_id(
            validator,
            get_interface_info_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interface_info_by_id_default_val(api):
    endpoint_result = api.devices.get_interface_info_by_id(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_info_by_id_default_val(api, validator):
    try:
        assert is_valid_get_interface_info_by_id(
            validator,
            get_interface_info_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_count_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_34b7d6c62ea6522081fcf55de7eb9fd7_v2_2_3_3').validate(obj)
    return True


def get_device_interface_count_by_id(api):
    endpoint_result = api.devices.get_device_interface_count_by_id(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count_by_id(api, validator):
    try:
        assert is_valid_get_device_interface_count_by_id(
            validator,
            get_device_interface_count_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_interface_count_by_id_default_val(api):
    endpoint_result = api.devices.get_device_interface_count_by_id(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count_by_id_default_val(api, validator):
    try:
        assert is_valid_get_device_interface_count_by_id(
            validator,
            get_device_interface_count_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_details(json_schema_validate, obj):
    json_schema_validate('jsd_bef9e9b306085d879b877598fad71b51_v2_2_3_3').validate(obj)
    return True


def get_interface_details(api):
    endpoint_result = api.devices.get_interface_details(
        device_id='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_details(api, validator):
    try:
        assert is_valid_get_interface_details(
            validator,
            get_interface_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interface_details_default_val(api):
    endpoint_result = api.devices.get_interface_details(
        device_id='string',
        name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_details_default_val(api, validator):
    try:
        assert is_valid_get_interface_details(
            validator,
            get_interface_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interfaces_by_specified_range(json_schema_validate, obj):
    json_schema_validate('jsd_5a3d52c630ba5deaada16fe3b07af744_v2_2_3_3').validate(obj)
    return True


def get_device_interfaces_by_specified_range(api):
    endpoint_result = api.devices.get_device_interfaces_by_specified_range(
        device_id='string',
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interfaces_by_specified_range(api, validator):
    try:
        assert is_valid_get_device_interfaces_by_specified_range(
            validator,
            get_device_interfaces_by_specified_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_interfaces_by_specified_range_default_val(api):
    endpoint_result = api.devices.get_device_interfaces_by_specified_range(
        device_id='string',
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interfaces_by_specified_range_default_val(api, validator):
    try:
        assert is_valid_get_device_interfaces_by_specified_range(
            validator,
            get_device_interfaces_by_specified_range_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ospf_interfaces(json_schema_validate, obj):
    json_schema_validate('jsd_32a2868ff45f5621965f6ece01a742ce_v2_2_3_3').validate(obj)
    return True


def get_ospf_interfaces(api):
    endpoint_result = api.devices.get_ospf_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_ospf_interfaces(api, validator):
    try:
        assert is_valid_get_ospf_interfaces(
            validator,
            get_ospf_interfaces(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ospf_interfaces_default_val(api):
    endpoint_result = api.devices.get_ospf_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_ospf_interfaces_default_val(api, validator):
    try:
        assert is_valid_get_ospf_interfaces(
            validator,
            get_ospf_interfaces_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_17b16bff74ae54ca88a02b34df169218_v2_2_3_3').validate(obj)
    return True


def get_interface_by_id(api):
    endpoint_result = api.devices.get_interface_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_id(api, validator):
    try:
        assert is_valid_get_interface_by_id(
            validator,
            get_interface_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interface_by_id_default_val(api):
    endpoint_result = api.devices.get_interface_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_id_default_val(api, validator):
    try:
        assert is_valid_get_interface_by_id(
            validator,
            get_interface_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_list(json_schema_validate, obj):
    json_schema_validate('jsd_fe602e8165035b5cbc304fada4ee2f26_v2_2_3_3').validate(obj)
    return True


def get_device_list(api):
    endpoint_result = api.devices.get_device_list(
        associated_wlc_ip='value1,value2',
        collection_interval='value1,value2',
        collection_status='value1,value2',
        device_support_level='string',
        error_code='value1,value2',
        error_description='value1,value2',
        family='value1,value2',
        hostname='value1,value2',
        id='string',
        license_name='value1,value2',
        license_status='value1,value2',
        license_type='value1,value2',
        location='value1,value2',
        location_name='value1,value2',
        mac_address='value1,value2',
        management_ip_address='value1,value2',
        module_equpimenttype='value1,value2',
        module_name='value1,value2',
        module_operationstatecode='value1,value2',
        module_partnumber='value1,value2',
        module_servicestate='value1,value2',
        module_vendorequipmenttype='value1,value2',
        not_synced_for_minutes='value1,value2',
        platform_id='value1,value2',
        reachability_status='value1,value2',
        role='value1,value2',
        serial_number='value1,value2',
        series='value1,value2',
        software_type='value1,value2',
        software_version='value1,value2',
        type='value1,value2',
        up_time='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_list(api, validator):
    try:
        assert is_valid_get_device_list(
            validator,
            get_device_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_list_default_val(api):
    endpoint_result = api.devices.get_device_list(
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        device_support_level=None,
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
        up_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_list_default_val(api, validator):
    try:
        assert is_valid_get_device_list(
            validator,
            get_device_list_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_device(json_schema_validate, obj):
    json_schema_validate('jsd_62704fe3ec7651e79d891fce37a0d860_v2_2_3_3').validate(obj)
    return True


def add_device(api):
    endpoint_result = api.devices.add_device(
        active_validation=True,
        cliTransport='string',
        computeDevice=True,
        enablePassword='string',
        extendedDiscoveryInfo='string',
        httpPassword='string',
        httpPort='string',
        httpSecure=True,
        httpUserName='string',
        ipAddress=['string'],
        merakiOrgId=['string'],
        netconfPort='string',
        password='string',
        payload=None,
        serialNumber='string',
        snmpAuthPassphrase='string',
        snmpAuthProtocol='string',
        snmpMode='string',
        snmpPrivPassphrase='string',
        snmpPrivProtocol='string',
        snmpROCommunity='string',
        snmpRWCommunity='string',
        snmpRetry=0,
        snmpTimeout=0,
        snmpUserName='string',
        snmpVersion='string',
        type='string',
        updateMgmtIPaddressList=[{'existMgmtIpAddress': 'string', 'newMgmtIpAddress': 'string'}],
        userName='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_add_device(api, validator):
    try:
        assert is_valid_add_device(
            validator,
            add_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_device_default_val(api):
    endpoint_result = api.devices.add_device(
        active_validation=True,
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
        payload=None,
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
        userName=None
    )
    return endpoint_result


@pytest.mark.devices
def test_add_device_default_val(api, validator):
    try:
        assert is_valid_add_device(
            validator,
            add_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sync_devices(json_schema_validate, obj):
    json_schema_validate('jsd_8232fe06867e548bba1919024b40d992_v2_2_3_3').validate(obj)
    return True


def sync_devices(api):
    endpoint_result = api.devices.sync_devices(
        active_validation=True,
        cliTransport='string',
        computeDevice=True,
        enablePassword='string',
        extendedDiscoveryInfo='string',
        httpPassword='string',
        httpPort='string',
        httpSecure=True,
        httpUserName='string',
        ipAddress=['string'],
        merakiOrgId=['string'],
        netconfPort='string',
        password='string',
        payload=None,
        serialNumber='string',
        snmpAuthPassphrase='string',
        snmpAuthProtocol='string',
        snmpMode='string',
        snmpPrivPassphrase='string',
        snmpPrivProtocol='string',
        snmpROCommunity='string',
        snmpRWCommunity='string',
        snmpRetry=0,
        snmpTimeout=0,
        snmpUserName='string',
        snmpVersion='string',
        type='string',
        updateMgmtIPaddressList=[{'existMgmtIpAddress': 'string', 'newMgmtIpAddress': 'string'}],
        userName='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices(api, validator):
    try:
        assert is_valid_sync_devices(
            validator,
            sync_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def sync_devices_default_val(api):
    endpoint_result = api.devices.sync_devices(
        active_validation=True,
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
        payload=None,
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
        userName=None
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices_default_val(api, validator):
    try:
        assert is_valid_sync_devices(
            validator,
            sync_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_values_that_match_fully_or_partially_an_attribute(json_schema_validate, obj):
    json_schema_validate('jsd_b5a5c8da4aaa526da6a06e97c80a38be_v2_2_3_3').validate(obj)
    return True


def get_device_values_that_match_fully_or_partially_an_attribute(api):
    endpoint_result = api.devices.get_device_values_that_match_fully_or_partially_an_attribute(
        associated_wlc_ip='string',
        collection_interval='string',
        collection_status='string',
        error_code='string',
        family='string',
        hostname='string',
        limit=0,
        mac_address='string',
        management_ip_address='string',
        offset=0,
        platform_id='string',
        reachability_failure_reason='string',
        reachability_status='string',
        role='string',
        role_source='string',
        serial_number='string',
        series='string',
        software_type='string',
        software_version='string',
        type='string',
        up_time='string',
        vrf_name='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_values_that_match_fully_or_partially_an_attribute(api, validator):
    try:
        assert is_valid_get_device_values_that_match_fully_or_partially_an_attribute(
            validator,
            get_device_values_that_match_fully_or_partially_an_attribute(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_values_that_match_fully_or_partially_an_attribute_default_val(api):
    endpoint_result = api.devices.get_device_values_that_match_fully_or_partially_an_attribute(
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        error_code=None,
        family=None,
        hostname=None,
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
        vrf_name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_values_that_match_fully_or_partially_an_attribute_default_val(api, validator):
    try:
        assert is_valid_get_device_values_that_match_fully_or_partially_an_attribute(
            validator,
            get_device_values_that_match_fully_or_partially_an_attribute_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_role(json_schema_validate, obj):
    json_schema_validate('jsd_aa11f09d28165f4ea6c81b8642e59cc4_v2_2_3_3').validate(obj)
    return True


def update_device_role(api):
    endpoint_result = api.devices.update_device_role(
        active_validation=True,
        id='string',
        payload=None,
        role='string',
        roleSource='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_role(api, validator):
    try:
        assert is_valid_update_device_role(
            validator,
            update_device_role(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_role_default_val(api):
    endpoint_result = api.devices.update_device_role(
        active_validation=True,
        id=None,
        payload=None,
        role=None,
        roleSource=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_role_default_val(api, validator):
    try:
        assert is_valid_update_device_role(
            validator,
            update_device_role_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_polling_interval_for_all_devices(json_schema_validate, obj):
    json_schema_validate('jsd_ce94ab18ad505e8a9846f6c4c9df0d2b_v2_2_3_3').validate(obj)
    return True


def get_polling_interval_for_all_devices(api):
    endpoint_result = api.devices.get_polling_interval_for_all_devices(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_for_all_devices(api, validator):
    try:
        assert is_valid_get_polling_interval_for_all_devices(
            validator,
            get_polling_interval_for_all_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_polling_interval_for_all_devices_default_val(api):
    endpoint_result = api.devices.get_polling_interval_for_all_devices(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_for_all_devices_default_val(api, validator):
    try:
        assert is_valid_get_polling_interval_for_all_devices(
            validator,
            get_polling_interval_for_all_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_config_for_all_devices(json_schema_validate, obj):
    json_schema_validate('jsd_ed2bca4be412527198720a4dfec9604a_v2_2_3_3').validate(obj)
    return True


def get_device_config_for_all_devices(api):
    endpoint_result = api.devices.get_device_config_for_all_devices(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_for_all_devices(api, validator):
    try:
        assert is_valid_get_device_config_for_all_devices(
            validator,
            get_device_config_for_all_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_config_for_all_devices_default_val(api):
    endpoint_result = api.devices.get_device_config_for_all_devices(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_for_all_devices_default_val(api, validator):
    try:
        assert is_valid_get_device_config_for_all_devices(
            validator,
            get_device_config_for_all_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_config_count(json_schema_validate, obj):
    json_schema_validate('jsd_3dc0a72537a3578ca31cc5ef29131d35_v2_2_3_3').validate(obj)
    return True


def get_device_config_count(api):
    endpoint_result = api.devices.get_device_config_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_count(api, validator):
    try:
        assert is_valid_get_device_config_count(
            validator,
            get_device_config_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_config_count_default_val(api):
    endpoint_result = api.devices.get_device_config_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_count_default_val(api, validator):
    try:
        assert is_valid_get_device_config_count(
            validator,
            get_device_config_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_count(json_schema_validate, obj):
    json_schema_validate('jsd_bbfe7340fe6752e5bc273a303d165654_v2_2_3_3').validate(obj)
    return True


def get_device_count(api):
    endpoint_result = api.devices.get_device_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_count(api, validator):
    try:
        assert is_valid_get_device_count(
            validator,
            get_device_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_count_default_val(api):
    endpoint_result = api.devices.get_device_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_count_default_val(api, validator):
    try:
        assert is_valid_get_device_count(
            validator,
            get_device_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_export_device_list(json_schema_validate, obj):
    json_schema_validate('jsd_57e6ec627d3c587288978990aae75228_v2_2_3_3').validate(obj)
    return True


def export_device_list(api):
    endpoint_result = api.devices.export_device_list(
        active_validation=True,
        deviceUuids=['string'],
        id='string',
        operationEnum='string',
        parameters=['string'],
        password='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_export_device_list(api, validator):
    try:
        assert is_valid_export_device_list(
            validator,
            export_device_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def export_device_list_default_val(api):
    endpoint_result = api.devices.export_device_list(
        active_validation=True,
        deviceUuids=None,
        id=None,
        operationEnum=None,
        parameters=None,
        password=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_export_device_list_default_val(api, validator):
    try:
        assert is_valid_export_device_list(
            validator,
            export_device_list_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_functional_capability_for_devices(json_schema_validate, obj):
    json_schema_validate('jsd_ad8cea95d71352f0842a2c869765e6cf_v2_2_3_3').validate(obj)
    return True


def get_functional_capability_for_devices(api):
    endpoint_result = api.devices.get_functional_capability_for_devices(
        device_id='string',
        function_name='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_for_devices(api, validator):
    try:
        assert is_valid_get_functional_capability_for_devices(
            validator,
            get_functional_capability_for_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_functional_capability_for_devices_default_val(api):
    endpoint_result = api.devices.get_functional_capability_for_devices(
        device_id=None,
        function_name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_for_devices_default_val(api, validator):
    try:
        assert is_valid_get_functional_capability_for_devices(
            validator,
            get_functional_capability_for_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_functional_capability_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_7f494532c45654fdaeda8d46a0d9753d_v2_2_3_3').validate(obj)
    return True


def get_functional_capability_by_id(api):
    endpoint_result = api.devices.get_functional_capability_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_by_id(api, validator):
    try:
        assert is_valid_get_functional_capability_by_id(
            validator,
            get_functional_capability_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_functional_capability_by_id_default_val(api):
    endpoint_result = api.devices.get_functional_capability_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_by_id_default_val(api, validator):
    try:
        assert is_valid_get_functional_capability_by_id(
            validator,
            get_functional_capability_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_inventory_insight_device_link_mismatch(json_schema_validate, obj):
    json_schema_validate('jsd_eed1595442b757bf94938c858a257ced_v2_2_3_3').validate(obj)
    return True


def inventory_insight_device_link_mismatch(api):
    endpoint_result = api.devices.inventory_insight_device_link_mismatch(
        category='string',
        limit='string',
        offset='string',
        order='string',
        site_id='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_inventory_insight_device_link_mismatch(api, validator):
    try:
        assert is_valid_inventory_insight_device_link_mismatch(
            validator,
            inventory_insight_device_link_mismatch(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def inventory_insight_device_link_mismatch_default_val(api):
    endpoint_result = api.devices.inventory_insight_device_link_mismatch(
        category=None,
        limit=None,
        offset=None,
        order=None,
        site_id='string',
        sort_by=None
    )
    return endpoint_result


@pytest.mark.devices
def test_inventory_insight_device_link_mismatch_default_val(api, validator):
    try:
        assert is_valid_inventory_insight_device_link_mismatch(
            validator,
            inventory_insight_device_link_mismatch_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_devices_with_snmpv3_des(json_schema_validate, obj):
    json_schema_validate('jsd_bbc074b061d3575d8247084ca33c95d9_v2_2_3_3').validate(obj)
    return True


def get_devices_with_snmpv3_des(api):
    endpoint_result = api.devices.get_devices_with_snmpv3_des(
        limit='string',
        offset='string',
        order='string',
        site_id='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_devices_with_snmpv3_des(api, validator):
    try:
        assert is_valid_get_devices_with_snmpv3_des(
            validator,
            get_devices_with_snmpv3_des(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_devices_with_snmpv3_des_default_val(api):
    endpoint_result = api.devices.get_devices_with_snmpv3_des(
        limit=None,
        offset=None,
        order=None,
        site_id='string',
        sort_by=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_devices_with_snmpv3_des_default_val(api, validator):
    try:
        assert is_valid_get_devices_with_snmpv3_des(
            validator,
            get_devices_with_snmpv3_des_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device_by_ip(json_schema_validate, obj):
    json_schema_validate('jsd_40123dc74c2052a3a4eb7e2a01eaa8e7_v2_2_3_3').validate(obj)
    return True


def get_network_device_by_ip(api):
    endpoint_result = api.devices.get_network_device_by_ip(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_ip(api, validator):
    try:
        assert is_valid_get_network_device_by_ip(
            validator,
            get_network_device_by_ip(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_device_by_ip_default_val(api):
    endpoint_result = api.devices.get_network_device_by_ip(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_ip_default_val(api, validator):
    try:
        assert is_valid_get_network_device_by_ip(
            validator,
            get_network_device_by_ip_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_modules(json_schema_validate, obj):
    json_schema_validate('jsd_ce9e547725c45c66824afda98179d12f_v2_2_3_3').validate(obj)
    return True


def get_modules(api):
    endpoint_result = api.devices.get_modules(
        device_id='string',
        limit='string',
        name_list='value1,value2',
        offset='string',
        operational_state_code_list='value1,value2',
        part_number_list='value1,value2',
        vendor_equipment_type_list='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_modules(api, validator):
    try:
        assert is_valid_get_modules(
            validator,
            get_modules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_modules_default_val(api):
    endpoint_result = api.devices.get_modules(
        device_id=None,
        limit=None,
        name_list=None,
        offset=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_modules_default_val(api, validator):
    try:
        assert is_valid_get_modules(
            validator,
            get_modules_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_module_count(json_schema_validate, obj):
    json_schema_validate('jsd_fb11f997009751c991884b5fc02087c5_v2_2_3_3').validate(obj)
    return True


def get_module_count(api):
    endpoint_result = api.devices.get_module_count(
        device_id='string',
        name_list='value1,value2',
        operational_state_code_list='value1,value2',
        part_number_list='value1,value2',
        vendor_equipment_type_list='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_count(api, validator):
    try:
        assert is_valid_get_module_count(
            validator,
            get_module_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_module_count_default_val(api):
    endpoint_result = api.devices.get_module_count(
        device_id=None,
        name_list=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_count_default_val(api, validator):
    try:
        assert is_valid_get_module_count(
            validator,
            get_module_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_module_info_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_96a4588640da5b018b499c5760f4092a_v2_2_3_3').validate(obj)
    return True


def get_module_info_by_id(api):
    endpoint_result = api.devices.get_module_info_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_info_by_id(api, validator):
    try:
        assert is_valid_get_module_info_by_id(
            validator,
            get_module_info_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_module_info_by_id_default_val(api):
    endpoint_result = api.devices.get_module_info_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_info_by_id_default_val(api, validator):
    try:
        assert is_valid_get_module_info_by_id(
            validator,
            get_module_info_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_by_serial_number(json_schema_validate, obj):
    json_schema_validate('jsd_5c53d56c282e5f108c659009d21f9d26_v2_2_3_3').validate(obj)
    return True


def get_device_by_serial_number(api):
    endpoint_result = api.devices.get_device_by_serial_number(
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_serial_number(api, validator):
    try:
        assert is_valid_get_device_by_serial_number(
            validator,
            get_device_by_serial_number(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_by_serial_number_default_val(api):
    endpoint_result = api.devices.get_device_by_serial_number(
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_serial_number_default_val(api, validator):
    try:
        assert is_valid_get_device_by_serial_number(
            validator,
            get_device_by_serial_number_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sync_devices_using_forcesync(json_schema_validate, obj):
    json_schema_validate('jsd_9425f2c120b855cb8c852806ce72e54d_v2_2_3_3').validate(obj)
    return True


def sync_devices_using_forcesync(api):
    endpoint_result = api.devices.sync_devices_using_forcesync(
        active_validation=True,
        force_sync=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices_using_forcesync(api, validator):
    try:
        assert is_valid_sync_devices_using_forcesync(
            validator,
            sync_devices_using_forcesync(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def sync_devices_using_forcesync_default_val(api):
    endpoint_result = api.devices.sync_devices_using_forcesync(
        active_validation=True,
        force_sync=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices_using_forcesync_default_val(api, validator):
    try:
        assert is_valid_sync_devices_using_forcesync(
            validator,
            sync_devices_using_forcesync_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_register_device_for_wsa(json_schema_validate, obj):
    json_schema_validate('jsd_8770b2c39feb5e48913492c33add7f13_v2_2_3_3').validate(obj)
    return True


def register_device_for_wsa(api):
    endpoint_result = api.devices.register_device_for_wsa(
        macaddress='string',
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_register_device_for_wsa(api, validator):
    try:
        assert is_valid_register_device_for_wsa(
            validator,
            register_device_for_wsa(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def register_device_for_wsa_default_val(api):
    endpoint_result = api.devices.register_device_for_wsa(
        macaddress=None,
        serial_number=None
    )
    return endpoint_result


@pytest.mark.devices
def test_register_device_for_wsa_default_val(api, validator):
    try:
        assert is_valid_register_device_for_wsa(
            validator,
            register_device_for_wsa_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_chassis_details_for_device(json_schema_validate, obj):
    json_schema_validate('jsd_4a03cee8dfd7514487a134a422f5e0d7_v2_2_3_3').validate(obj)
    return True


def get_chassis_details_for_device(api):
    endpoint_result = api.devices.get_chassis_details_for_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_chassis_details_for_device(api, validator):
    try:
        assert is_valid_get_chassis_details_for_device(
            validator,
            get_chassis_details_for_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_chassis_details_for_device_default_val(api):
    endpoint_result = api.devices.get_chassis_details_for_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_chassis_details_for_device_default_val(api, validator):
    try:
        assert is_valid_get_chassis_details_for_device(
            validator,
            get_chassis_details_for_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_stack_details_for_device(json_schema_validate, obj):
    json_schema_validate('jsd_c07eaefa1fa45faa801764d9094336ae_v2_2_3_3').validate(obj)
    return True


def get_stack_details_for_device(api):
    endpoint_result = api.devices.get_stack_details_for_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_stack_details_for_device(api, validator):
    try:
        assert is_valid_get_stack_details_for_device(
            validator,
            get_stack_details_for_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_stack_details_for_device_default_val(api):
    endpoint_result = api.devices.get_stack_details_for_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_stack_details_for_device_default_val(api, validator):
    try:
        assert is_valid_get_stack_details_for_device(
            validator,
            get_stack_details_for_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_return_power_supply_fan_details_for_the_given_device(json_schema_validate, obj):
    json_schema_validate('jsd_520c1cb24a2b53ce8d29d119c6ee1112_v2_2_3_3').validate(obj)
    return True


def return_power_supply_fan_details_for_the_given_device(api):
    endpoint_result = api.devices.return_power_supply_fan_details_for_the_given_device(
        device_uuid='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_return_power_supply_fan_details_for_the_given_device(api, validator):
    try:
        assert is_valid_return_power_supply_fan_details_for_the_given_device(
            validator,
            return_power_supply_fan_details_for_the_given_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def return_power_supply_fan_details_for_the_given_device_default_val(api):
    endpoint_result = api.devices.return_power_supply_fan_details_for_the_given_device(
        device_uuid='string',
        type=None
    )
    return endpoint_result


@pytest.mark.devices
def test_return_power_supply_fan_details_for_the_given_device_default_val(api, validator):
    try:
        assert is_valid_return_power_supply_fan_details_for_the_given_device(
            validator,
            return_power_supply_fan_details_for_the_given_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_poe_interface_details(json_schema_validate, obj):
    json_schema_validate('jsd_ab3215d9be065533b7cbbc978cb4d905_v2_2_3_3').validate(obj)
    return True


def poe_interface_details(api):
    endpoint_result = api.devices.poe_interface_details(
        device_uuid='string',
        interface_name_list='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_poe_interface_details(api, validator):
    try:
        assert is_valid_poe_interface_details(
            validator,
            poe_interface_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def poe_interface_details_default_val(api):
    endpoint_result = api.devices.poe_interface_details(
        device_uuid='string',
        interface_name_list=None
    )
    return endpoint_result


@pytest.mark.devices
def test_poe_interface_details_default_val(api, validator):
    try:
        assert is_valid_poe_interface_details(
            validator,
            poe_interface_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_linecard_details(json_schema_validate, obj):
    json_schema_validate('jsd_bd31690b61f45d9f880d74d4e682b070_v2_2_3_3').validate(obj)
    return True


def get_linecard_details(api):
    endpoint_result = api.devices.get_linecard_details(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_linecard_details(api, validator):
    try:
        assert is_valid_get_linecard_details(
            validator,
            get_linecard_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_linecard_details_default_val(api):
    endpoint_result = api.devices.get_linecard_details(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_linecard_details_default_val(api, validator):
    try:
        assert is_valid_get_linecard_details(
            validator,
            get_linecard_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_poe_details(json_schema_validate, obj):
    json_schema_validate('jsd_f7a67aba0b365a1e9dae62d148511a25_v2_2_3_3').validate(obj)
    return True


def poe_details(api):
    endpoint_result = api.devices.poe_details(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_poe_details(api, validator):
    try:
        assert is_valid_poe_details(
            validator,
            poe_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def poe_details_default_val(api):
    endpoint_result = api.devices.poe_details(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_poe_details_default_val(api, validator):
    try:
        assert is_valid_poe_details(
            validator,
            poe_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_supervisor_card_detail(json_schema_validate, obj):
    json_schema_validate('jsd_4500eb13516155a28570e542dcf10a91_v2_2_3_3').validate(obj)
    return True


def get_supervisor_card_detail(api):
    endpoint_result = api.devices.get_supervisor_card_detail(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_supervisor_card_detail(api, validator):
    try:
        assert is_valid_get_supervisor_card_detail(
            validator,
            get_supervisor_card_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_supervisor_card_detail_default_val(api):
    endpoint_result = api.devices.get_supervisor_card_detail(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_supervisor_card_detail_default_val(api, validator):
    try:
        assert is_valid_get_supervisor_card_detail(
            validator,
            get_supervisor_card_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_358d86f657f8592f97014d2ebf8d37ac_v2_2_3_3').validate(obj)
    return True


def get_device_by_id(api):
    endpoint_result = api.devices.get_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_id(api, validator):
    try:
        assert is_valid_get_device_by_id(
            validator,
            get_device_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_by_id_default_val(api):
    endpoint_result = api.devices.get_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_id_default_val(api, validator):
    try:
        assert is_valid_get_device_by_id(
            validator,
            get_device_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_003e01233fa258e393239c4b41882806_v2_2_3_3').validate(obj)
    return True


def delete_device_by_id(api):
    endpoint_result = api.devices.delete_device_by_id(
        clean_config=True,
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_device_by_id(api, validator):
    try:
        assert is_valid_delete_device_by_id(
            validator,
            delete_device_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_by_id_default_val(api):
    endpoint_result = api.devices.delete_device_by_id(
        clean_config=None,
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_device_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_device_by_id(
            validator,
            delete_device_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_summary(json_schema_validate, obj):
    json_schema_validate('jsd_fe0153ca24205608b8741d51f5a6d54a_v2_2_3_3').validate(obj)
    return True


def get_device_summary(api):
    endpoint_result = api.devices.get_device_summary(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_summary(api, validator):
    try:
        assert is_valid_get_device_summary(
            validator,
            get_device_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_summary_default_val(api):
    endpoint_result = api.devices.get_device_summary(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_summary_default_val(api, validator):
    try:
        assert is_valid_get_device_summary(
            validator,
            get_device_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_polling_interval_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_f90daf1c279351f884ba3198d3b2d641_v2_2_3_3').validate(obj)
    return True


def get_polling_interval_by_id(api):
    endpoint_result = api.devices.get_polling_interval_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_by_id(api, validator):
    try:
        assert is_valid_get_polling_interval_by_id(
            validator,
            get_polling_interval_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_polling_interval_by_id_default_val(api):
    endpoint_result = api.devices.get_polling_interval_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_by_id_default_val(api, validator):
    try:
        assert is_valid_get_polling_interval_by_id(
            validator,
            get_polling_interval_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_organization_list_for_meraki(json_schema_validate, obj):
    json_schema_validate('jsd_790b4ba6d23d5e7eb62cbba4c9e1a29d_v2_2_3_3').validate(obj)
    return True


def get_organization_list_for_meraki(api):
    endpoint_result = api.devices.get_organization_list_for_meraki(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_organization_list_for_meraki(api, validator):
    try:
        assert is_valid_get_organization_list_for_meraki(
            validator,
            get_organization_list_for_meraki(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_organization_list_for_meraki_default_val(api):
    endpoint_result = api.devices.get_organization_list_for_meraki(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_organization_list_for_meraki_default_val(api, validator):
    try:
        assert is_valid_get_organization_list_for_meraki(
            validator,
            get_organization_list_for_meraki_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_vlans(json_schema_validate, obj):
    json_schema_validate('jsd_fd5fb603cba6523abb25c8ec131fbb8b_v2_2_3_3').validate(obj)
    return True


def get_device_interface_vlans(api):
    endpoint_result = api.devices.get_device_interface_vlans(
        id='string',
        interface_type='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_vlans(api, validator):
    try:
        assert is_valid_get_device_interface_vlans(
            validator,
            get_device_interface_vlans(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_interface_vlans_default_val(api):
    endpoint_result = api.devices.get_device_interface_vlans(
        id='string',
        interface_type=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_vlans_default_val(api, validator):
    try:
        assert is_valid_get_device_interface_vlans(
            validator,
            get_device_interface_vlans_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_wireless_lan_controller_details_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_c01ee650fcf858789ca00c8deda969b9_v2_2_3_3').validate(obj)
    return True


def get_wireless_lan_controller_details_by_id(api):
    endpoint_result = api.devices.get_wireless_lan_controller_details_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_wireless_lan_controller_details_by_id(api, validator):
    try:
        assert is_valid_get_wireless_lan_controller_details_by_id(
            validator,
            get_wireless_lan_controller_details_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_wireless_lan_controller_details_by_id_default_val(api):
    endpoint_result = api.devices.get_wireless_lan_controller_details_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_wireless_lan_controller_details_by_id_default_val(api, validator):
    try:
        assert is_valid_get_wireless_lan_controller_details_by_id(
            validator,
            get_wireless_lan_controller_details_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_config_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_5af0bbf34adb5146b931ec874fc2cc40_v2_2_3_3').validate(obj)
    return True


def get_device_config_by_id(api):
    endpoint_result = api.devices.get_device_config_by_id(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_by_id(api, validator):
    try:
        assert is_valid_get_device_config_by_id(
            validator,
            get_device_config_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_config_by_id_default_val(api):
    endpoint_result = api.devices.get_device_config_by_id(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_by_id_default_val(api, validator):
    try:
        assert is_valid_get_device_config_by_id(
            validator,
            get_device_config_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device_by_pagination_range(json_schema_validate, obj):
    json_schema_validate('jsd_60d7b6ce5abd5dad837e22ace817a6f0_v2_2_3_3').validate(obj)
    return True


def get_network_device_by_pagination_range(api):
    endpoint_result = api.devices.get_network_device_by_pagination_range(
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_pagination_range(api, validator):
    try:
        assert is_valid_get_network_device_by_pagination_range(
            validator,
            get_network_device_by_pagination_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_device_by_pagination_range_default_val(api):
    endpoint_result = api.devices.get_network_device_by_pagination_range(
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_pagination_range_default_val(api, validator):
    try:
        assert is_valid_get_network_device_by_pagination_range(
            validator,
            get_network_device_by_pagination_range_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_threat_details(json_schema_validate, obj):
    json_schema_validate('jsd_5f4ce55b5f235924903516ef31dc9e3c_v2_2_3_3').validate(obj)
    return True


def threat_details(api):
    endpoint_result = api.devices.threat_details(
        active_validation=True,
        endTime=0,
        isNewThreat=True,
        limit=0,
        offset=0,
        payload=None,
        siteId=['string'],
        startTime=0,
        threatLevel=['string'],
        threatType=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_threat_details(api, validator):
    try:
        assert is_valid_threat_details(
            validator,
            threat_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def threat_details_default_val(api):
    endpoint_result = api.devices.threat_details(
        active_validation=True,
        endTime=None,
        isNewThreat=None,
        limit=None,
        offset=None,
        payload=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None
    )
    return endpoint_result


@pytest.mark.devices
def test_threat_details_default_val(api, validator):
    try:
        assert is_valid_threat_details(
            validator,
            threat_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_threat_detail_count(json_schema_validate, obj):
    json_schema_validate('jsd_1137c7266d89581c9601b79b7304fda3_v2_2_3_3').validate(obj)
    return True


def threat_detail_count(api):
    endpoint_result = api.devices.threat_detail_count(
        active_validation=True,
        endTime=0,
        isNewThreat=True,
        limit=0,
        offset=0,
        payload=None,
        siteId=['string'],
        startTime=0,
        threatLevel=['string'],
        threatType=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_threat_detail_count(api, validator):
    try:
        assert is_valid_threat_detail_count(
            validator,
            threat_detail_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def threat_detail_count_default_val(api):
    endpoint_result = api.devices.threat_detail_count(
        active_validation=True,
        endTime=None,
        isNewThreat=None,
        limit=None,
        offset=None,
        payload=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None
    )
    return endpoint_result


@pytest.mark.devices
def test_threat_detail_count_default_val(api, validator):
    try:
        assert is_valid_threat_detail_count(
            validator,
            threat_detail_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_threat_summary(json_schema_validate, obj):
    json_schema_validate('jsd_e6eed78cb55d51a1bfe669729df25689_v2_2_3_3').validate(obj)
    return True


def threat_summary(api):
    endpoint_result = api.devices.threat_summary(
        active_validation=True,
        endTime=0,
        payload=None,
        siteId=['string'],
        startTime=0,
        threatLevel=['string'],
        threatType=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_threat_summary(api, validator):
    try:
        assert is_valid_threat_summary(
            validator,
            threat_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def threat_summary_default_val(api):
    endpoint_result = api.devices.threat_summary(
        active_validation=True,
        endTime=None,
        payload=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None
    )
    return endpoint_result


@pytest.mark.devices
def test_threat_summary_default_val(api, validator):
    try:
        assert is_valid_threat_summary(
            validator,
            threat_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI lan_automation API fixtures and tests.

Copyright (c) 2025 Cisco Systems.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '3.1.6.0', reason='version does not match')


def is_valid_lan_automation_start(json_schema_validate, obj):
    json_schema_validate('jsd_b119a4d455e35cc3b2cc6695a045cbfa_v3_1_6_0').validate(obj)
    return True


def lan_automation_start(api):
    endpoint_result = api.lan_automation.lan_automation_start(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_start(api, validator):
    try:
        assert is_valid_lan_automation_start(
            validator,
            lan_automation_start(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_start_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_start(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_start_default_val(api, validator):
    try:
        assert is_valid_lan_automation_start(
            validator,
            lan_automation_start_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_session_count(json_schema_validate, obj):
    json_schema_validate('jsd_130eea014edd5807925df3a414a92ed4_v3_1_6_0').validate(obj)
    return True


def lan_automation_session_count(api):
    endpoint_result = api.lan_automation.lan_automation_session_count(

    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_session_count(api, validator):
    try:
        assert is_valid_lan_automation_session_count(
            validator,
            lan_automation_session_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_session_count_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_session_count(

    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_session_count_default_val(api, validator):
    try:
        assert is_valid_lan_automation_session_count(
            validator,
            lan_automation_session_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_log(json_schema_validate, obj):
    json_schema_validate('jsd_3173e37f6c9650b68e0aaac866a162cf_v3_1_6_0').validate(obj)
    return True


def lan_automation_log(api):
    endpoint_result = api.lan_automation.lan_automation_log(
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_log(api, validator):
    try:
        assert is_valid_lan_automation_log(
            validator,
            lan_automation_log(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_log_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_log(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_log_default_val(api, validator):
    try:
        assert is_valid_lan_automation_log(
            validator,
            lan_automation_log_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_log_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_60e98b744fde50a1b53761251c43bfb0_v3_1_6_0').validate(obj)
    return True


def lan_automation_log_by_id(api):
    endpoint_result = api.lan_automation.lan_automation_log_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_log_by_id(api, validator):
    try:
        assert is_valid_lan_automation_log_by_id(
            validator,
            lan_automation_log_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_log_by_id_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_log_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_log_by_id_default_val(api, validator):
    try:
        assert is_valid_lan_automation_log_by_id(
            validator,
            lan_automation_log_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_logs_for_individual_devices(json_schema_validate, obj):
    json_schema_validate('jsd_26485c3441f7507a98d02579c25814f4_v3_1_6_0').validate(obj)
    return True


def lan_automation_logs_for_individual_devices(api):
    endpoint_result = api.lan_automation.lan_automation_logs_for_individual_devices(
        id='string',
        log_level='string',
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_logs_for_individual_devices(api, validator):
    try:
        assert is_valid_lan_automation_logs_for_individual_devices(
            validator,
            lan_automation_logs_for_individual_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_logs_for_individual_devices_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_logs_for_individual_devices(
        id='string',
        log_level=None,
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_logs_for_individual_devices_default_val(api, validator):
    try:
        assert is_valid_lan_automation_logs_for_individual_devices(
            validator,
            lan_automation_logs_for_individual_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_active_sessions(json_schema_validate, obj):
    json_schema_validate('jsd_5a19cf2241e75c648220d7172e9e4013_v3_1_6_0').validate(obj)
    return True


def lan_automation_active_sessions(api):
    endpoint_result = api.lan_automation.lan_automation_active_sessions(

    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_active_sessions(api, validator):
    try:
        assert is_valid_lan_automation_active_sessions(
            validator,
            lan_automation_active_sessions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_active_sessions_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_active_sessions(

    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_active_sessions_default_val(api, validator):
    try:
        assert is_valid_lan_automation_active_sessions(
            validator,
            lan_automation_active_sessions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_status(json_schema_validate, obj):
    json_schema_validate('jsd_40c56a6c58fd5b71b7949036855ee25b_v3_1_6_0').validate(obj)
    return True


def lan_automation_status(api):
    endpoint_result = api.lan_automation.lan_automation_status(
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_status(api, validator):
    try:
        assert is_valid_lan_automation_status(
            validator,
            lan_automation_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_status_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_status(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_status_default_val(api, validator):
    try:
        assert is_valid_lan_automation_status(
            validator,
            lan_automation_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_status_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_d5727c4bdb1056308cd10e99dff2acb8_v3_1_6_0').validate(obj)
    return True


def lan_automation_status_by_id(api):
    endpoint_result = api.lan_automation.lan_automation_status_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_status_by_id(api, validator):
    try:
        assert is_valid_lan_automation_status_by_id(
            validator,
            lan_automation_status_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_status_by_id_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_status_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_status_by_id_default_val(api, validator):
    try:
        assert is_valid_lan_automation_status_by_id(
            validator,
            lan_automation_status_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_device_update(json_schema_validate, obj):
    json_schema_validate('jsd_932aac9ba55e5043b4d5e0995c566dce_v3_1_6_0').validate(obj)
    return True


def lan_automation_device_update(api):
    endpoint_result = api.lan_automation.lan_automation_device_update(
        active_validation=True,
        feature='string',
        hostnameUpdateDevices=[{'deviceManagementIPAddress': 'string', 'newHostName': 'string'}],
        linkUpdate={'sourceDeviceManagementIPAddress': 'string', 'sourceDeviceInterfaceName': 'string', 'destinationDeviceManagementIPAddress': 'string', 'destinationDeviceInterfaceName': 'string', 'ipPoolName': 'string'},
        loopbackUpdateDeviceList=[{'deviceManagementIPAddress': 'string', 'newLoopback0IPAddress': 'string'}],
        payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_device_update(api, validator):
    try:
        assert is_valid_lan_automation_device_update(
            validator,
            lan_automation_device_update(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_device_update_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_device_update(
        active_validation=True,
        feature=None,
        hostnameUpdateDevices=None,
        linkUpdate=None,
        loopbackUpdateDeviceList=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_device_update_default_val(api, validator):
    try:
        assert is_valid_lan_automation_device_update(
            validator,
            lan_automation_device_update_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_stop(json_schema_validate, obj):
    json_schema_validate('jsd_ed815ca3e5ab5ae48720795217ec776b_v3_1_6_0').validate(obj)
    return True


def lan_automation_stop(api):
    endpoint_result = api.lan_automation.lan_automation_stop(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop(api, validator):
    try:
        assert is_valid_lan_automation_stop(
            validator,
            lan_automation_stop(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_stop_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_stop(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop_default_val(api, validator):
    try:
        assert is_valid_lan_automation_stop(
            validator,
            lan_automation_stop_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_stop_and_update_devices(json_schema_validate, obj):
    json_schema_validate('jsd_d413a3d054ac50fa921ca8cf7fdf5449_v3_1_6_0').validate(obj)
    return True


def lan_automation_stop_and_update_devices(api):
    endpoint_result = api.lan_automation.lan_automation_stop_and_update_devices(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop_and_update_devices(api, validator):
    try:
        assert is_valid_lan_automation_stop_and_update_devices(
            validator,
            lan_automation_stop_and_update_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_stop_and_update_devices_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_stop_and_update_devices(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop_and_update_devices_default_val(api, validator):
    try:
        assert is_valid_lan_automation_stop_and_update_devices(
            validator,
            lan_automation_stop_and_update_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_channels(json_schema_validate, obj):
    json_schema_validate('jsd_ee969674421c512494b828e1115d899f_v3_1_6_0').validate(obj)
    return True


def get_port_channels(api):
    endpoint_result = api.lan_automation.get_port_channels(
        device1_management_ipaddress='string',
        device1_uuid='string',
        device2_management_ipaddress='string',
        device2_uuid='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_get_port_channels(api, validator):
    try:
        assert is_valid_get_port_channels(
            validator,
            get_port_channels(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_port_channels_default_val(api):
    endpoint_result = api.lan_automation.get_port_channels(
        device1_management_ipaddress=None,
        device1_uuid=None,
        device2_management_ipaddress=None,
        device2_uuid=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_get_port_channels_default_val(api, validator):
    try:
        assert is_valid_get_port_channels(
            validator,
            get_port_channels_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_a_new_port_channel_between_devices(json_schema_validate, obj):
    json_schema_validate('jsd_37369cf0138550909ea413dab063868c_v3_1_6_0').validate(obj)
    return True


def create_a_new_port_channel_between_devices(api):
    endpoint_result = api.lan_automation.create_a_new_port_channel_between_devices(
        active_validation=True,
        device1ManagementIPAddress='string',
        device1Uuid='string',
        device2ManagementIPAddress='string',
        device2Uuid='string',
        payload=None,
        portChannelMembers=[{'device1InterfaceUuid': 'string', 'device1Interface': 'string', 'device2InterfaceUuid': 'string', 'device2Interface': 'string'}]
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_create_a_new_port_channel_between_devices(api, validator):
    try:
        assert is_valid_create_a_new_port_channel_between_devices(
            validator,
            create_a_new_port_channel_between_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_a_new_port_channel_between_devices_default_val(api):
    endpoint_result = api.lan_automation.create_a_new_port_channel_between_devices(
        active_validation=True,
        device1ManagementIPAddress=None,
        device1Uuid=None,
        device2ManagementIPAddress=None,
        device2Uuid=None,
        payload=None,
        portChannelMembers=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_create_a_new_port_channel_between_devices_default_val(api, validator):
    try:
        assert is_valid_create_a_new_port_channel_between_devices(
            validator,
            create_a_new_port_channel_between_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_channel(json_schema_validate, obj):
    json_schema_validate('jsd_bec4a00bb2bf5a63a75f745862904e4d_v3_1_6_0').validate(obj)
    return True


def delete_port_channel(api):
    endpoint_result = api.lan_automation.delete_port_channel(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_delete_port_channel(api, validator):
    try:
        assert is_valid_delete_port_channel(
            validator,
            delete_port_channel(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_port_channel_default_val(api):
    endpoint_result = api.lan_automation.delete_port_channel(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_delete_port_channel_default_val(api, validator):
    try:
        assert is_valid_delete_port_channel(
            validator,
            delete_port_channel_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_channel_information_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_6039e149c0cd53b8b8998d82fd3dc1d1_v3_1_6_0').validate(obj)
    return True


def get_port_channel_information_by_id(api):
    endpoint_result = api.lan_automation.get_port_channel_information_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_get_port_channel_information_by_id(api, validator):
    try:
        assert is_valid_get_port_channel_information_by_id(
            validator,
            get_port_channel_information_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_port_channel_information_by_id_default_val(api):
    endpoint_result = api.lan_automation.get_port_channel_information_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_get_port_channel_information_by_id_default_val(api, validator):
    try:
        assert is_valid_get_port_channel_information_by_id(
            validator,
            get_port_channel_information_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_a_lan_automated_link_to_a_port_channel(json_schema_validate, obj):
    json_schema_validate('jsd_fa8fb3bdbffe5958858f20447dcb3ca5_v3_1_6_0').validate(obj)
    return True


def add_a_lan_automated_link_to_a_port_channel(api):
    endpoint_result = api.lan_automation.add_a_lan_automated_link_to_a_port_channel(
        active_validation=True,
        id='string',
        payload=None,
        portChannelMembers=[{'device1InterfaceUuid': 'string', 'device1Interface': 'string', 'device2InterfaceUuid': 'string', 'device2Interface': 'string'}]
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_add_a_lan_automated_link_to_a_port_channel(api, validator):
    try:
        assert is_valid_add_a_lan_automated_link_to_a_port_channel(
            validator,
            add_a_lan_automated_link_to_a_port_channel(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_a_lan_automated_link_to_a_port_channel_default_val(api):
    endpoint_result = api.lan_automation.add_a_lan_automated_link_to_a_port_channel(
        active_validation=True,
        id='string',
        payload=None,
        portChannelMembers=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_add_a_lan_automated_link_to_a_port_channel_default_val(api, validator):
    try:
        assert is_valid_add_a_lan_automated_link_to_a_port_channel(
            validator,
            add_a_lan_automated_link_to_a_port_channel_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_a_link_from_port_channel(json_schema_validate, obj):
    json_schema_validate('jsd_6fb433ea1bbc5dc49dce4fde0a04e5ed_v3_1_6_0').validate(obj)
    return True


def remove_a_link_from_port_channel(api):
    endpoint_result = api.lan_automation.remove_a_link_from_port_channel(
        active_validation=True,
        id='string',
        payload=None,
        portChannelMembers=[{'device1InterfaceUuid': 'string', 'device1Interface': 'string', 'device2InterfaceUuid': 'string', 'device2Interface': 'string'}]
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_remove_a_link_from_port_channel(api, validator):
    try:
        assert is_valid_remove_a_link_from_port_channel(
            validator,
            remove_a_link_from_port_channel(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def remove_a_link_from_port_channel_default_val(api):
    endpoint_result = api.lan_automation.remove_a_link_from_port_channel(
        active_validation=True,
        id='string',
        payload=None,
        portChannelMembers=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_remove_a_link_from_port_channel_default_val(api, validator):
    try:
        assert is_valid_remove_a_link_from_port_channel(
            validator,
            remove_a_link_from_port_channel_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_start_v2(json_schema_validate, obj):
    json_schema_validate('jsd_dc5d352dfaeb5b17800b0af2858c2f5c_v3_1_6_0').validate(obj)
    return True


def lan_automation_start_v2(api):
    endpoint_result = api.lan_automation.lan_automation_start_v2(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_start_v2(api, validator):
    try:
        assert is_valid_lan_automation_start_v2(
            validator,
            lan_automation_start_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_start_v2_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_start_v2(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_start_v2_default_val(api, validator):
    try:
        assert is_valid_lan_automation_start_v2(
            validator,
            lan_automation_start_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_stop_and_update_devices_v2(json_schema_validate, obj):
    json_schema_validate('jsd_4421504ad0cb5a12a76384ba4644e55e_v3_1_6_0').validate(obj)
    return True


def lan_automation_stop_and_update_devices_v2(api):
    endpoint_result = api.lan_automation.lan_automation_stop_and_update_devices_v2(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop_and_update_devices_v2(api, validator):
    try:
        assert is_valid_lan_automation_stop_and_update_devices_v2(
            validator,
            lan_automation_stop_and_update_devices_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_stop_and_update_devices_v2_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_stop_and_update_devices_v2(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop_and_update_devices_v2_default_val(api, validator):
    try:
        assert is_valid_lan_automation_stop_and_update_devices_v2(
            validator,
            lan_automation_stop_and_update_devices_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

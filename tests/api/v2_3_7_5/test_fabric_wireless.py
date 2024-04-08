# -*- coding: utf-8 -*-
"""DNACenterAPI fabric_wireless API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.5', reason='version does not match')


def is_valid_add_ssid_to_ip_pool_mapping(json_schema_validate, obj):
    json_schema_validate('jsd_ad96e712f4525a128368b1bfe3afc21c_v2_3_7_5').validate(obj)
    return True


def add_ssid_to_ip_pool_mapping(api):
    endpoint_result = api.fabric_wireless.add_ssid_to_ip_pool_mapping(
        active_validation=True,
        payload=None,
        scalableGroupName='string',
        siteNameHierarchy='string',
        ssidNames=['string'],
        vlanName='string'
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_ssid_to_ip_pool_mapping(api, validator):
    try:
        assert is_valid_add_ssid_to_ip_pool_mapping(
            validator,
            add_ssid_to_ip_pool_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_ssid_to_ip_pool_mapping_default_val(api):
    endpoint_result = api.fabric_wireless.add_ssid_to_ip_pool_mapping(
        active_validation=True,
        payload=None,
        scalableGroupName=None,
        siteNameHierarchy=None,
        ssidNames=None,
        vlanName=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_ssid_to_ip_pool_mapping_default_val(api, validator):
    try:
        assert is_valid_add_ssid_to_ip_pool_mapping(
            validator,
            add_ssid_to_ip_pool_mapping_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_ssid_to_ip_pool_mapping(json_schema_validate, obj):
    json_schema_validate('jsd_249809f90ae8599c8a21c98b7a1ca804_v2_3_7_5').validate(obj)
    return True


def update_ssid_to_ip_pool_mapping(api):
    endpoint_result = api.fabric_wireless.update_ssid_to_ip_pool_mapping(
        active_validation=True,
        payload=None,
        scalableGroupName='string',
        siteNameHierarchy='string',
        ssidNames=['string'],
        vlanName='string'
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_update_ssid_to_ip_pool_mapping(api, validator):
    try:
        assert is_valid_update_ssid_to_ip_pool_mapping(
            validator,
            update_ssid_to_ip_pool_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_ssid_to_ip_pool_mapping_default_val(api):
    endpoint_result = api.fabric_wireless.update_ssid_to_ip_pool_mapping(
        active_validation=True,
        payload=None,
        scalableGroupName=None,
        siteNameHierarchy=None,
        ssidNames=None,
        vlanName=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_update_ssid_to_ip_pool_mapping_default_val(api, validator):
    try:
        assert is_valid_update_ssid_to_ip_pool_mapping(
            validator,
            update_ssid_to_ip_pool_mapping_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ssid_to_ip_pool_mapping(json_schema_validate, obj):
    json_schema_validate('jsd_2b0f6a0410705c75a61cdc51cc96c53f_v2_3_7_5').validate(obj)
    return True


def get_ssid_to_ip_pool_mapping(api):
    endpoint_result = api.fabric_wireless.get_ssid_to_ip_pool_mapping(
        site_name_hierarchy='string',
        vlan_name='string'
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_get_ssid_to_ip_pool_mapping(api, validator):
    try:
        assert is_valid_get_ssid_to_ip_pool_mapping(
            validator,
            get_ssid_to_ip_pool_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ssid_to_ip_pool_mapping_default_val(api):
    endpoint_result = api.fabric_wireless.get_ssid_to_ip_pool_mapping(
        site_name_hierarchy=None,
        vlan_name=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_get_ssid_to_ip_pool_mapping_default_val(api, validator):
    try:
        assert is_valid_get_ssid_to_ip_pool_mapping(
            validator,
            get_ssid_to_ip_pool_mapping_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_w_l_c_from_fabric_domain(json_schema_validate, obj):
    json_schema_validate('jsd_76039bb706025a9cb183ce7a60e0b5df_v2_3_7_5').validate(obj)
    return True


def remove_w_l_c_from_fabric_domain(api):
    endpoint_result = api.fabric_wireless.remove_w_l_c_from_fabric_domain(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_remove_w_l_c_from_fabric_domain(api, validator):
    try:
        assert is_valid_remove_w_l_c_from_fabric_domain(
            validator,
            remove_w_l_c_from_fabric_domain(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def remove_w_l_c_from_fabric_domain_default_val(api):
    endpoint_result = api.fabric_wireless.remove_w_l_c_from_fabric_domain(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_remove_w_l_c_from_fabric_domain_default_val(api, validator):
    try:
        assert is_valid_remove_w_l_c_from_fabric_domain(
            validator,
            remove_w_l_c_from_fabric_domain_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_w_l_c_to_fabric_domain(json_schema_validate, obj):
    json_schema_validate('jsd_6c4befbd77a452a9b7873ffc360a1f20_v2_3_7_5').validate(obj)
    return True


def add_w_l_c_to_fabric_domain(api):
    endpoint_result = api.fabric_wireless.add_w_l_c_to_fabric_domain(
        active_validation=True,
        deviceName='string',
        payload=None,
        siteNameHierarchy='string'
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_w_l_c_to_fabric_domain(api, validator):
    try:
        assert is_valid_add_w_l_c_to_fabric_domain(
            validator,
            add_w_l_c_to_fabric_domain(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_w_l_c_to_fabric_domain_default_val(api):
    endpoint_result = api.fabric_wireless.add_w_l_c_to_fabric_domain(
        active_validation=True,
        deviceName=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_w_l_c_to_fabric_domain_default_val(api, validator):
    try:
        assert is_valid_add_w_l_c_to_fabric_domain(
            validator,
            add_w_l_c_to_fabric_domain_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

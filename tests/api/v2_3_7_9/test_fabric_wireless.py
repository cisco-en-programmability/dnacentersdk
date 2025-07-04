# -*- coding: utf-8 -*-
"""CatalystCenterAPI fabric_wireless API fixtures and tests.

Copyright (c) 2024 Cisco Systems.

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

pytestmark = pytest.mark.skipif(
    DNA_CENTER_VERSION != "2.3.7.9", reason="version does not match"
)


def is_valid_add_ssid_to_ip_pool_mapping(json_schema_validate, obj):
    json_schema_validate("jsd_ad96e712f4525a128368b1bfe3afc21c_v2_3_7_9").validate(obj)
    return True


def add_ssid_to_ip_pool_mapping(api):
    endpoint_result = api.fabric_wireless.add_ssid_to_ip_pool_mapping(
        active_validation=True,
        payload=None,
        scalableGroupName="string",
        siteNameHierarchy="string",
        ssidNames=["string"],
        vlanName="string",
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_ssid_to_ip_pool_mapping(api, validator):
    try:
        assert is_valid_add_ssid_to_ip_pool_mapping(
            validator, add_ssid_to_ip_pool_mapping(api)
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
        vlanName=None,
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_ssid_to_ip_pool_mapping_default_val(api, validator):
    try:
        assert is_valid_add_ssid_to_ip_pool_mapping(
            validator, add_ssid_to_ip_pool_mapping_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_ssid_to_ip_pool_mapping(json_schema_validate, obj):
    json_schema_validate("jsd_249809f90ae8599c8a21c98b7a1ca804_v2_3_7_9").validate(obj)
    return True


def update_ssid_to_ip_pool_mapping(api):
    endpoint_result = api.fabric_wireless.update_ssid_to_ip_pool_mapping(
        active_validation=True,
        payload=None,
        scalableGroupName="string",
        siteNameHierarchy="string",
        ssidNames=["string"],
        vlanName="string",
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_update_ssid_to_ip_pool_mapping(api, validator):
    try:
        assert is_valid_update_ssid_to_ip_pool_mapping(
            validator, update_ssid_to_ip_pool_mapping(api)
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
        vlanName=None,
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_update_ssid_to_ip_pool_mapping_default_val(api, validator):
    try:
        assert is_valid_update_ssid_to_ip_pool_mapping(
            validator, update_ssid_to_ip_pool_mapping_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ssid_to_ip_pool_mapping(json_schema_validate, obj):
    json_schema_validate("jsd_2b0f6a0410705c75a61cdc51cc96c53f_v2_3_7_9").validate(obj)
    return True


def get_ssid_to_ip_pool_mapping(api):
    endpoint_result = api.fabric_wireless.get_ssid_to_ip_pool_mapping(
        site_name_hierarchy="string", vlan_name="string"
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_get_ssid_to_ip_pool_mapping(api, validator):
    try:
        assert is_valid_get_ssid_to_ip_pool_mapping(
            validator, get_ssid_to_ip_pool_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ssid_to_ip_pool_mapping_default_val(api):
    endpoint_result = api.fabric_wireless.get_ssid_to_ip_pool_mapping(
        site_name_hierarchy=None, vlan_name=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_get_ssid_to_ip_pool_mapping_default_val(api, validator):
    try:
        assert is_valid_get_ssid_to_ip_pool_mapping(
            validator, get_ssid_to_ip_pool_mapping_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_w_l_c_from_fabric_domain(json_schema_validate, obj):
    json_schema_validate("jsd_76039bb706025a9cb183ce7a60e0b5df_v2_3_7_9").validate(obj)
    return True


def remove_w_l_c_from_fabric_domain(api):
    endpoint_result = api.fabric_wireless.remove_w_l_c_from_fabric_domain(
        device_ipaddress="string"
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_remove_w_l_c_from_fabric_domain(api, validator):
    try:
        assert is_valid_remove_w_l_c_from_fabric_domain(
            validator, remove_w_l_c_from_fabric_domain(api)
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
            validator, remove_w_l_c_from_fabric_domain_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_w_l_c_to_fabric_domain(json_schema_validate, obj):
    json_schema_validate("jsd_6c4befbd77a452a9b7873ffc360a1f20_v2_3_7_9").validate(obj)
    return True


def add_w_l_c_to_fabric_domain(api):
    endpoint_result = api.fabric_wireless.add_w_l_c_to_fabric_domain(
        active_validation=True,
        deviceName="string",
        payload=None,
        siteNameHierarchy="string",
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_w_l_c_to_fabric_domain(api, validator):
    try:
        assert is_valid_add_w_l_c_to_fabric_domain(
            validator, add_w_l_c_to_fabric_domain(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_w_l_c_to_fabric_domain_default_val(api):
    endpoint_result = api.fabric_wireless.add_w_l_c_to_fabric_domain(
        active_validation=True, deviceName=None, payload=None, siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_w_l_c_to_fabric_domain_default_val(api, validator):
    try:
        assert is_valid_add_w_l_c_to_fabric_domain(
            validator, add_w_l_c_to_fabric_domain_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping(
    json_schema_validate, obj
):
    json_schema_validate("jsd_0fea6e17769f5b3eb5ee1696254d2973_v2_3_7_9").validate(obj)
    return True


def returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping(api):
    endpoint_result = (
        api.fabric_wireless.returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping(
            limit=0, offset=0
        )
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping(api, validator):
    try:
        assert is_valid_returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping(
            validator, returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_default_val(api):
    endpoint_result = (
        api.fabric_wireless.returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping(
            limit=None, offset=None
        )
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_default_val(
    api, validator
):
    try:
        assert is_valid_returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping(
            validator,
            returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping(
    json_schema_validate, obj
):
    json_schema_validate("jsd_233017be3f285e21b59701a1af044b28_v2_3_7_9").validate(obj)
    return True


def return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping(api):
    endpoint_result = (
        api.fabric_wireless.return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping()
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping(
    api, validator
):
    try:
        assert is_valid_return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping(
            validator,
            return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_default_val(
    api,
):
    endpoint_result = (
        api.fabric_wireless.return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping()
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_default_val(
    api, validator
):
    try:
        assert is_valid_return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping(
            validator,
            return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_switch_wireless_setting_and_rolling_ap_upgrade_management(
    json_schema_validate, obj
):
    json_schema_validate("jsd_1e5e51bcda0b5fec984ba8120f743fe2_v2_3_7_9").validate(obj)
    return True


def switch_wireless_setting_and_rolling_ap_upgrade_management(api):
    endpoint_result = (
        api.fabric_wireless.switch_wireless_setting_and_rolling_ap_upgrade_management(
            active_validation=True,
            enableWireless=True,
            fabric_id="string",
            id="string",
            payload=None,
            rollingApUpgrade={"enableRollingApUpgrade": True, "apRebootPercentage": 0},
        )
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_switch_wireless_setting_and_rolling_ap_upgrade_management(api, validator):
    try:
        assert is_valid_switch_wireless_setting_and_rolling_ap_upgrade_management(
            validator, switch_wireless_setting_and_rolling_ap_upgrade_management(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def switch_wireless_setting_and_rolling_ap_upgrade_management_default_val(api):
    endpoint_result = (
        api.fabric_wireless.switch_wireless_setting_and_rolling_ap_upgrade_management(
            active_validation=True,
            enableWireless=None,
            fabric_id="string",
            id=None,
            payload=None,
            rollingApUpgrade=None,
        )
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_switch_wireless_setting_and_rolling_ap_upgrade_management_default_val(
    api, validator
):
    try:
        assert is_valid_switch_wireless_setting_and_rolling_ap_upgrade_management(
            validator,
            switch_wireless_setting_and_rolling_ap_upgrade_management_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sda_wireless_details_from_switches(json_schema_validate, obj):
    json_schema_validate("jsd_1e33e204167d5408a6785177727f40c9_v2_3_7_9").validate(obj)
    return True


def get_sda_wireless_details_from_switches(api):
    endpoint_result = api.fabric_wireless.get_sda_wireless_details_from_switches(
        fabric_id="string"
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_get_sda_wireless_details_from_switches(api, validator):
    try:
        assert is_valid_get_sda_wireless_details_from_switches(
            validator, get_sda_wireless_details_from_switches(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sda_wireless_details_from_switches_default_val(api):
    endpoint_result = api.fabric_wireless.get_sda_wireless_details_from_switches(
        fabric_id="string"
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_get_sda_wireless_details_from_switches_default_val(api, validator):
    try:
        assert is_valid_get_sda_wireless_details_from_switches(
            validator, get_sda_wireless_details_from_switches_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reload_switch_for_wireless_controller_cleanup(json_schema_validate, obj):
    json_schema_validate("jsd_cdf8c0d3866d5147901c0cf4821a84a7_v2_3_7_9").validate(obj)
    return True


def reload_switch_for_wireless_controller_cleanup(api):
    endpoint_result = api.fabric_wireless.reload_switch_for_wireless_controller_cleanup(
        active_validation=True, deviceId="string", fabric_id="string", payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_reload_switch_for_wireless_controller_cleanup(api, validator):
    try:
        assert is_valid_reload_switch_for_wireless_controller_cleanup(
            validator, reload_switch_for_wireless_controller_cleanup(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def reload_switch_for_wireless_controller_cleanup_default_val(api):
    endpoint_result = api.fabric_wireless.reload_switch_for_wireless_controller_cleanup(
        active_validation=True, deviceId=None, fabric_id="string", payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_reload_switch_for_wireless_controller_cleanup_default_val(api, validator):
    try:
        assert is_valid_reload_switch_for_wireless_controller_cleanup(
            validator, reload_switch_for_wireless_controller_cleanup_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_update_or_remove_ssid_mapping_to_a_vlan(json_schema_validate, obj):
    json_schema_validate("jsd_a3d2432ae8c55fe793c5180d8d5fce25_v2_3_7_9").validate(obj)
    return True


def add_update_or_remove_ssid_mapping_to_a_vlan(api):
    endpoint_result = api.fabric_wireless.add_update_or_remove_ssid_mapping_to_a_vlan(
        active_validation=True, fabric_id="string", payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_update_or_remove_ssid_mapping_to_a_vlan(api, validator):
    try:
        assert is_valid_add_update_or_remove_ssid_mapping_to_a_vlan(
            validator, add_update_or_remove_ssid_mapping_to_a_vlan(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_update_or_remove_ssid_mapping_to_a_vlan_default_val(api):
    endpoint_result = api.fabric_wireless.add_update_or_remove_ssid_mapping_to_a_vlan(
        active_validation=True, fabric_id="string", payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_update_or_remove_ssid_mapping_to_a_vlan_default_val(api, validator):
    try:
        assert is_valid_add_update_or_remove_ssid_mapping_to_a_vlan(
            validator, add_update_or_remove_ssid_mapping_to_a_vlan_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site(
    json_schema_validate, obj
):
    json_schema_validate("jsd_6a18f012c54a5d34aef05d651f2dea18_v2_3_7_9").validate(obj)
    return True


def retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site(api):
    endpoint_result = api.fabric_wireless.retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site(
        fabric_id="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site(
    api, validator
):
    try:
        assert is_valid_retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site(
            validator,
            retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_default_val(
    api,
):
    endpoint_result = api.fabric_wireless.retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site(
        fabric_id="string", limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_default_val(
    api, validator
):
    try:
        assert is_valid_retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site(
            validator,
            retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site(
    json_schema_validate, obj
):
    json_schema_validate("jsd_ed14be6211da53ab832acf9b5aea599c_v2_3_7_9").validate(obj)
    return True


def returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site(api):
    endpoint_result = (
        api.fabric_wireless.returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site(
            fabric_id="string"
        )
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site(api, validator):
    try:
        assert is_valid_returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site(
            validator, returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_default_val(api):
    endpoint_result = (
        api.fabric_wireless.returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site(
            fabric_id="string"
        )
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_default_val(
    api, validator
):
    try:
        assert is_valid_returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site(
            validator,
            returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_sda_wireless_multicast(json_schema_validate, obj):
    json_schema_validate("jsd_41a2be6dde4c587389e79d6cb84e54a6_v2_3_7_9").validate(obj)
    return True


def update_sda_wireless_multicast(api):
    endpoint_result = api.fabric_wireless.update_sda_wireless_multicast(
        active_validation=True, fabric_id="string", multicastEnabled=True, payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_update_sda_wireless_multicast(api, validator):
    try:
        assert is_valid_update_sda_wireless_multicast(
            validator, update_sda_wireless_multicast(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_sda_wireless_multicast_default_val(api):
    endpoint_result = api.fabric_wireless.update_sda_wireless_multicast(
        active_validation=True, fabric_id="string", multicastEnabled=None, payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_update_sda_wireless_multicast_default_val(api, validator):
    try:
        assert is_valid_update_sda_wireless_multicast(
            validator, update_sda_wireless_multicast_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sda_wireless_multicast(json_schema_validate, obj):
    json_schema_validate("jsd_371fa08fad71522eb877d2356b584f7d_v2_3_7_9").validate(obj)
    return True


def get_sda_wireless_multicast(api):
    endpoint_result = api.fabric_wireless.get_sda_wireless_multicast(fabric_id="string")
    return endpoint_result


@pytest.mark.fabric_wireless
def test_get_sda_wireless_multicast(api, validator):
    try:
        assert is_valid_get_sda_wireless_multicast(
            validator, get_sda_wireless_multicast(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sda_wireless_multicast_default_val(api):
    endpoint_result = api.fabric_wireless.get_sda_wireless_multicast(fabric_id="string")
    return endpoint_result


@pytest.mark.fabric_wireless
def test_get_sda_wireless_multicast_default_val(api, validator):
    try:
        assert is_valid_get_sda_wireless_multicast(
            validator, get_sda_wireless_multicast_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI fabric_wireless API fixtures and tests.

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
    DNA_CENTER_VERSION != "2.3.7.6", reason="version does not match"
)


def is_valid_add_ssid_to_ip_pool_mapping_v1(json_schema_validate, obj):
    json_schema_validate("jsd_ad96e712f4525a128368b1bfe3afc21c_v2_3_7_6").validate(obj)
    return True


def add_ssid_to_ip_pool_mapping_v1(api):
    endpoint_result = api.fabric_wireless.add_ssid_to_ip_pool_mapping_v1(
        active_validation=True,
        payload=None,
        scalableGroupName="string",
        siteNameHierarchy="string",
        ssidNames=["string"],
        vlanName="string",
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_ssid_to_ip_pool_mapping_v1(api, validator):
    try:
        assert is_valid_add_ssid_to_ip_pool_mapping_v1(
            validator, add_ssid_to_ip_pool_mapping_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_ssid_to_ip_pool_mapping_v1_default_val(api):
    endpoint_result = api.fabric_wireless.add_ssid_to_ip_pool_mapping_v1(
        active_validation=True,
        payload=None,
        scalableGroupName=None,
        siteNameHierarchy=None,
        ssidNames=None,
        vlanName=None,
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_ssid_to_ip_pool_mapping_v1_default_val(api, validator):
    try:
        assert is_valid_add_ssid_to_ip_pool_mapping_v1(
            validator, add_ssid_to_ip_pool_mapping_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_ssid_to_ip_pool_mapping_v1(json_schema_validate, obj):
    json_schema_validate("jsd_249809f90ae8599c8a21c98b7a1ca804_v2_3_7_6").validate(obj)
    return True


def update_ssid_to_ip_pool_mapping_v1(api):
    endpoint_result = api.fabric_wireless.update_ssid_to_ip_pool_mapping_v1(
        active_validation=True,
        payload=None,
        scalableGroupName="string",
        siteNameHierarchy="string",
        ssidNames=["string"],
        vlanName="string",
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_update_ssid_to_ip_pool_mapping_v1(api, validator):
    try:
        assert is_valid_update_ssid_to_ip_pool_mapping_v1(
            validator, update_ssid_to_ip_pool_mapping_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_ssid_to_ip_pool_mapping_v1_default_val(api):
    endpoint_result = api.fabric_wireless.update_ssid_to_ip_pool_mapping_v1(
        active_validation=True,
        payload=None,
        scalableGroupName=None,
        siteNameHierarchy=None,
        ssidNames=None,
        vlanName=None,
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_update_ssid_to_ip_pool_mapping_v1_default_val(api, validator):
    try:
        assert is_valid_update_ssid_to_ip_pool_mapping_v1(
            validator, update_ssid_to_ip_pool_mapping_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ssid_to_ip_pool_mapping_v1(json_schema_validate, obj):
    json_schema_validate("jsd_2b0f6a0410705c75a61cdc51cc96c53f_v2_3_7_6").validate(obj)
    return True


def get_ssid_to_ip_pool_mapping_v1(api):
    endpoint_result = api.fabric_wireless.get_ssid_to_ip_pool_mapping_v1(
        site_name_hierarchy="string", vlan_name="string"
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_get_ssid_to_ip_pool_mapping_v1(api, validator):
    try:
        assert is_valid_get_ssid_to_ip_pool_mapping_v1(
            validator, get_ssid_to_ip_pool_mapping_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ssid_to_ip_pool_mapping_v1_default_val(api):
    endpoint_result = api.fabric_wireless.get_ssid_to_ip_pool_mapping_v1(
        site_name_hierarchy=None, vlan_name=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_get_ssid_to_ip_pool_mapping_v1_default_val(api, validator):
    try:
        assert is_valid_get_ssid_to_ip_pool_mapping_v1(
            validator, get_ssid_to_ip_pool_mapping_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_w_l_c_from_fabric_domain_v1(json_schema_validate, obj):
    json_schema_validate("jsd_76039bb706025a9cb183ce7a60e0b5df_v2_3_7_6").validate(obj)
    return True


def remove_w_l_c_from_fabric_domain_v1(api):
    endpoint_result = api.fabric_wireless.remove_w_l_c_from_fabric_domain_v1(
        device_ipaddress="string"
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_remove_w_l_c_from_fabric_domain_v1(api, validator):
    try:
        assert is_valid_remove_w_l_c_from_fabric_domain_v1(
            validator, remove_w_l_c_from_fabric_domain_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def remove_w_l_c_from_fabric_domain_v1_default_val(api):
    endpoint_result = api.fabric_wireless.remove_w_l_c_from_fabric_domain_v1(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_remove_w_l_c_from_fabric_domain_v1_default_val(api, validator):
    try:
        assert is_valid_remove_w_l_c_from_fabric_domain_v1(
            validator, remove_w_l_c_from_fabric_domain_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_w_l_c_to_fabric_domain_v1(json_schema_validate, obj):
    json_schema_validate("jsd_6c4befbd77a452a9b7873ffc360a1f20_v2_3_7_6").validate(obj)
    return True


def add_w_l_c_to_fabric_domain_v1(api):
    endpoint_result = api.fabric_wireless.add_w_l_c_to_fabric_domain_v1(
        active_validation=True,
        deviceName="string",
        payload=None,
        siteNameHierarchy="string",
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_w_l_c_to_fabric_domain_v1(api, validator):
    try:
        assert is_valid_add_w_l_c_to_fabric_domain_v1(
            validator, add_w_l_c_to_fabric_domain_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_w_l_c_to_fabric_domain_v1_default_val(api):
    endpoint_result = api.fabric_wireless.add_w_l_c_to_fabric_domain_v1(
        active_validation=True, deviceName=None, payload=None, siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_w_l_c_to_fabric_domain_v1_default_val(api, validator):
    try:
        assert is_valid_add_w_l_c_to_fabric_domain_v1(
            validator, add_w_l_c_to_fabric_domain_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_0fea6e17769f5b3eb5ee1696254d2973_v2_3_7_6").validate(obj)
    return True


def returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1(api):
    endpoint_result = api.fabric_wireless.returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1(
        limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1(api, validator):
    try:
        assert is_valid_returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1(
            validator,
            returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1_default_val(api):
    endpoint_result = api.fabric_wireless.returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1(
        limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1_default_val(
    api, validator
):
    try:
        assert is_valid_returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1(
            validator,
            returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_233017be3f285e21b59701a1af044b28_v2_3_7_6").validate(obj)
    return True


def return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1(api):
    endpoint_result = (
        api.fabric_wireless.return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1()
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1(
    api, validator
):
    try:
        assert is_valid_return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1(
            validator,
            return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1_default_val(
    api,
):
    endpoint_result = (
        api.fabric_wireless.return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1()
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1_default_val(
    api, validator
):
    try:
        assert is_valid_return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1(
            validator,
            return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_update_or_remove_ssid_mapping_to_a_vlan_v1(json_schema_validate, obj):
    json_schema_validate("jsd_a3d2432ae8c55fe793c5180d8d5fce25_v2_3_7_6").validate(obj)
    return True


def add_update_or_remove_ssid_mapping_to_a_vlan_v1(api):
    endpoint_result = (
        api.fabric_wireless.add_update_or_remove_ssid_mapping_to_a_vlan_v1(
            active_validation=True, fabric_id="string", payload=None
        )
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_update_or_remove_ssid_mapping_to_a_vlan_v1(api, validator):
    try:
        assert is_valid_add_update_or_remove_ssid_mapping_to_a_vlan_v1(
            validator, add_update_or_remove_ssid_mapping_to_a_vlan_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_update_or_remove_ssid_mapping_to_a_vlan_v1_default_val(api):
    endpoint_result = (
        api.fabric_wireless.add_update_or_remove_ssid_mapping_to_a_vlan_v1(
            active_validation=True, fabric_id="string", payload=None
        )
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_add_update_or_remove_ssid_mapping_to_a_vlan_v1_default_val(api, validator):
    try:
        assert is_valid_add_update_or_remove_ssid_mapping_to_a_vlan_v1(
            validator, add_update_or_remove_ssid_mapping_to_a_vlan_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_6a18f012c54a5d34aef05d651f2dea18_v2_3_7_6").validate(obj)
    return True


def retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1(api):
    endpoint_result = api.fabric_wireless.retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1(
        fabric_id="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1(
    api, validator
):
    try:
        assert is_valid_retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1(
            validator,
            retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1_default_val(
    api,
):
    endpoint_result = api.fabric_wireless.retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1(
        fabric_id="string", limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1_default_val(
    api, validator
):
    try:
        assert is_valid_retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1(
            validator,
            retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_ed14be6211da53ab832acf9b5aea599c_v2_3_7_6").validate(obj)
    return True


def returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1(api):
    endpoint_result = api.fabric_wireless.returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1(
        fabric_id="string"
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1(api, validator):
    try:
        assert is_valid_returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1(
            validator,
            returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1_default_val(api):
    endpoint_result = api.fabric_wireless.returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1(
        fabric_id="string"
    )
    return endpoint_result


@pytest.mark.fabric_wireless
def test_returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1_default_val(
    api, validator
):
    try:
        assert is_valid_returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1(
            validator,
            returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

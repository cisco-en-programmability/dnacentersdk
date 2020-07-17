# -*- coding: utf-8 -*-
"""DNACenterAPI fabric_wired API fixtures and tests.

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
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.1', reason='version does not match')


def is_valid_delete_ip_pool_from_sda_virtual_network(obj):
    json_schema_validate('jsd_549e4aff42bbb52a_v1_3_1').validate(obj)
    return True


def delete_ip_pool_from_sda_virtual_network(api):
    endpoint_result = api.fabric_wired.delete_ip_pool_from_sda_virtual_network(
        ip_pool_name='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_delete_ip_pool_from_sda_virtual_network(api):
    assert is_valid_delete_ip_pool_from_sda_virtual_network(
        delete_ip_pool_from_sda_virtual_network(api)
    )


def delete_ip_pool_from_sda_virtual_network_default(api):
    endpoint_result = api.fabric_wired.delete_ip_pool_from_sda_virtual_network(
        ip_pool_name=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_delete_ip_pool_from_sda_virtual_network_default(api):
    try:
        assert is_valid_delete_ip_pool_from_sda_virtual_network(
            delete_ip_pool_from_sda_virtual_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_edge_device(obj):
    json_schema_validate('jsd_1fb8f9f24c998133_v1_3_1').validate(obj)
    return True


def delete_edge_device(api):
    endpoint_result = api.fabric_wired.delete_edge_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_delete_edge_device(api):
    assert is_valid_delete_edge_device(
        delete_edge_device(api)
    )


def delete_edge_device_default(api):
    endpoint_result = api.fabric_wired.delete_edge_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_delete_edge_device_default(api):
    try:
        assert is_valid_delete_edge_device(
            delete_edge_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_default_authentication_profile(obj):
    json_schema_validate('jsd_3ebcda3e4acbafb7_v1_3_1').validate(obj)
    return True


def delete_default_authentication_profile(api):
    endpoint_result = api.fabric_wired.delete_default_authentication_profile(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_delete_default_authentication_profile(api):
    assert is_valid_delete_default_authentication_profile(
        delete_default_authentication_profile(api)
    )


def delete_default_authentication_profile_default(api):
    endpoint_result = api.fabric_wired.delete_default_authentication_profile(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_delete_default_authentication_profile_default(api):
    try:
        assert is_valid_delete_default_authentication_profile(
            delete_default_authentication_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_default_authentication_profile(obj):
    json_schema_validate('jsd_8984ea7744d98a54_v1_3_1').validate(obj)
    return True


def update_default_authentication_profile(api):
    endpoint_result = api.fabric_wired.update_default_authentication_profile(
        active_validation=True,
        payload=[{'siteNameHierarchy': 'string', 'authenticateTemplateName': 'string'}]
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_update_default_authentication_profile(api):
    assert is_valid_update_default_authentication_profile(
        update_default_authentication_profile(api)
    )


def update_default_authentication_profile_default(api):
    endpoint_result = api.fabric_wired.update_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_update_default_authentication_profile_default(api):
    try:
        assert is_valid_update_default_authentication_profile(
            update_default_authentication_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_edge_device(obj):
    json_schema_validate('jsd_7683f90b4efab090_v1_3_1').validate(obj)
    return True


def get_edge_device(api):
    endpoint_result = api.fabric_wired.get_edge_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_get_edge_device(api):
    assert is_valid_get_edge_device(
        get_edge_device(api)
    )


def get_edge_device_default(api):
    endpoint_result = api.fabric_wired.get_edge_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_get_edge_device_default(api):
    try:
        assert is_valid_get_edge_device(
            get_edge_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_add_port_assignment_for_user_device(obj):
    json_schema_validate('jsd_9582ab824ce8b29d_v1_3_1').validate(obj)
    return True


def add_port_assignment_for_user_device(api):
    endpoint_result = api.fabric_wired.add_port_assignment_for_user_device(
        active_validation=True,
        payload=[{'siteNameHierarchy': 'string', 'deviceManagementIpAddress': 'string', 'interfaceName': 'string', 'dataIpAddressPoolName': 'string', 'voiceIpAddressPoolName': 'string', 'authenticateTemplateName': 'string'}]
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_add_port_assignment_for_user_device(api):
    assert is_valid_add_port_assignment_for_user_device(
        add_port_assignment_for_user_device(api)
    )


def add_port_assignment_for_user_device_default(api):
    endpoint_result = api.fabric_wired.add_port_assignment_for_user_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_add_port_assignment_for_user_device_default(api):
    try:
        assert is_valid_add_port_assignment_for_user_device(
            add_port_assignment_for_user_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_deletes_border_device(obj):
    json_schema_validate('jsd_cb81b93540baaab0_v1_3_1').validate(obj)
    return True


def deletes_border_device(api):
    endpoint_result = api.fabric_wired.deletes_border_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_deletes_border_device(api):
    assert is_valid_deletes_border_device(
        deletes_border_device(api)
    )


def deletes_border_device_default(api):
    endpoint_result = api.fabric_wired.deletes_border_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_deletes_border_device_default(api):
    try:
        assert is_valid_deletes_border_device(
            deletes_border_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_add_edge_device(obj):
    json_schema_validate('jsd_87a8ba444ce9bc59_v1_3_1').validate(obj)
    return True


def add_edge_device(api):
    endpoint_result = api.fabric_wired.add_edge_device(
        active_validation=True,
        payload=[{'deviceManagementIpAddress': 'string', 'siteNameHierarchy': 'string'}]
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_add_edge_device(api):
    assert is_valid_add_edge_device(
        add_edge_device(api)
    )


def add_edge_device_default(api):
    endpoint_result = api.fabric_wired.add_edge_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_add_edge_device_default(api):
    try:
        assert is_valid_add_edge_device(
            add_edge_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_add_default_authentication_profile(obj):
    json_schema_validate('jsd_bca339d844c8a3c0_v1_3_1').validate(obj)
    return True


def add_default_authentication_profile(api):
    endpoint_result = api.fabric_wired.add_default_authentication_profile(
        active_validation=True,
        payload=[{'siteNameHierarchy': 'string', 'authenticateTemplateName': 'string'}]
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_add_default_authentication_profile(api):
    assert is_valid_add_default_authentication_profile(
        add_default_authentication_profile(api)
    )


def add_default_authentication_profile_default(api):
    endpoint_result = api.fabric_wired.add_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_add_default_authentication_profile_default(api):
    try:
        assert is_valid_add_default_authentication_profile(
            add_default_authentication_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_port_assignment_for_user_device(obj):
    json_schema_validate('jsd_cba5b8b14edb81f4_v1_3_1').validate(obj)
    return True


def delete_port_assignment_for_user_device(api):
    endpoint_result = api.fabric_wired.delete_port_assignment_for_user_device(
        device_ip='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_delete_port_assignment_for_user_device(api):
    assert is_valid_delete_port_assignment_for_user_device(
        delete_port_assignment_for_user_device(api)
    )


def delete_port_assignment_for_user_device_default(api):
    endpoint_result = api.fabric_wired.delete_port_assignment_for_user_device(
        device_ip=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_delete_port_assignment_for_user_device_default(api):
    try:
        assert is_valid_delete_port_assignment_for_user_device(
            delete_port_assignment_for_user_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_add_ip_pool_in_sda_virtual_network(obj):
    json_schema_validate('jsd_208579ea4ed98f4f_v1_3_1').validate(obj)
    return True


def add_ip_pool_in_sda_virtual_network(api):
    endpoint_result = api.fabric_wired.add_ip_pool_in_sda_virtual_network(
        active_validation=True,
        payload=[{'virtualNetworkName': 'string', 'ipPoolName': 'string', 'trafficType': 'string', 'authenticationPolicyName': 'string', 'scalableGroupName': 'string', 'isL2FloodingEnabled': True, 'isThisCriticalPool': True, 'poolType': 'string'}]
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_add_ip_pool_in_sda_virtual_network(api):
    assert is_valid_add_ip_pool_in_sda_virtual_network(
        add_ip_pool_in_sda_virtual_network(api)
    )


def add_ip_pool_in_sda_virtual_network_default(api):
    endpoint_result = api.fabric_wired.add_ip_pool_in_sda_virtual_network(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_add_ip_pool_in_sda_virtual_network_default(api):
    try:
        assert is_valid_add_ip_pool_in_sda_virtual_network(
            add_ip_pool_in_sda_virtual_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_gets_border_device_detail(obj):
    json_schema_validate('jsd_98a39bf4485a9871_v1_3_1').validate(obj)
    return True


def gets_border_device_detail(api):
    endpoint_result = api.fabric_wired.gets_border_device_detail(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_gets_border_device_detail(api):
    assert is_valid_gets_border_device_detail(
        gets_border_device_detail(api)
    )


def gets_border_device_detail_default(api):
    endpoint_result = api.fabric_wired.gets_border_device_detail(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_gets_border_device_detail_default(api):
    try:
        assert is_valid_gets_border_device_detail(
            gets_border_device_detail_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_port_assignment_for_user_device(obj):
    json_schema_validate('jsd_a4a1e8ed41cb9653_v1_3_1').validate(obj)
    return True


def get_port_assignment_for_user_device(api):
    endpoint_result = api.fabric_wired.get_port_assignment_for_user_device(
        device_ip='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_get_port_assignment_for_user_device(api):
    assert is_valid_get_port_assignment_for_user_device(
        get_port_assignment_for_user_device(api)
    )


def get_port_assignment_for_user_device_default(api):
    endpoint_result = api.fabric_wired.get_port_assignment_for_user_device(
        device_ip=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_get_port_assignment_for_user_device_default(api):
    try:
        assert is_valid_get_port_assignment_for_user_device(
            get_port_assignment_for_user_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_default_authentication_profile(obj):
    json_schema_validate('jsd_8b908a4e4c5a9a23_v1_3_1').validate(obj)
    return True


def get_default_authentication_profile(api):
    endpoint_result = api.fabric_wired.get_default_authentication_profile(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_get_default_authentication_profile(api):
    assert is_valid_get_default_authentication_profile(
        get_default_authentication_profile(api)
    )


def get_default_authentication_profile_default(api):
    endpoint_result = api.fabric_wired.get_default_authentication_profile(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_get_default_authentication_profile_default(api):
    try:
        assert is_valid_get_default_authentication_profile(
            get_default_authentication_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_adds_border_device(obj):
    json_schema_validate('jsd_bead7b3443b996a7_v1_3_1').validate(obj)
    return True


def adds_border_device(api):
    endpoint_result = api.fabric_wired.adds_border_device(
        active_validation=True,
        payload=[{'deviceManagementIpAddress': 'string', 'siteNameHierarchy': 'string', 'externalDomainRoutingProtocolName': 'string', 'externalConnectivityIpPoolName': 'string', 'internalAutonomouSystemNumber': 'string', 'borderSessionType': 'string', 'connectedToInternet': True, 'externalConnectivitySettings': [{'interfaceName': 'string', 'externalAutonomouSystemNumber': 'string', 'l3Handoff': [{'virtualNetwork': {'virtualNetworkName': 'string'}}]}]}]
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_adds_border_device(api):
    assert is_valid_adds_border_device(
        adds_border_device(api)
    )


def adds_border_device_default(api):
    endpoint_result = api.fabric_wired.adds_border_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_adds_border_device_default(api):
    try:
        assert is_valid_adds_border_device(
            adds_border_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_ip_pool_from_sda_virtual_network(obj):
    json_schema_validate('jsd_fa9219bf45c8b43b_v1_3_1').validate(obj)
    return True


def get_ip_pool_from_sda_virtual_network(api):
    endpoint_result = api.fabric_wired.get_ip_pool_from_sda_virtual_network(
        ip_pool_name='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_get_ip_pool_from_sda_virtual_network(api):
    assert is_valid_get_ip_pool_from_sda_virtual_network(
        get_ip_pool_from_sda_virtual_network(api)
    )


def get_ip_pool_from_sda_virtual_network_default(api):
    endpoint_result = api.fabric_wired.get_ip_pool_from_sda_virtual_network(
        ip_pool_name=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_get_ip_pool_from_sda_virtual_network_default(api):
    try:
        assert is_valid_get_ip_pool_from_sda_virtual_network(
            get_ip_pool_from_sda_virtual_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI industrial_configuration API fixtures and tests.

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


def is_valid_configure_a_r_e_p_ring_on_f_a_b_r_i_c_deployment(json_schema_validate, obj):
    json_schema_validate('jsd_f200dc9a10d25beab1243a5b29f99c7d_v3_1_6_0').validate(obj)
    return True


def configure_rep_ring_on_fabric_deployment(api):
    endpoint_result = api.industrial_configuration.configure_rep_ring_on_fabric_deployment(
        active_validation=True,
        deploymentMode='string',
        payload=None,
        ringName='string',
        rootNeighbourNetworkDeviceIds=['string'],
        rootNetworkDeviceId='string'
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_configure_a_r_e_p_ring_on_f_a_b_r_i_c_deployment(api, validator):
    try:
        assert is_valid_configure_a_r_e_p_ring_on_f_a_b_r_i_c_deployment(
            validator,
            configure_rep_ring_on_fabric_deployment(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def configure_a_r_e_p_ring_on_f_a_b_r_i_c_deployment_default_val(api):
    endpoint_result = api.industrial_configuration.configure_rep_ring_on_fabric_deployment(
        active_validation=True,
        deploymentMode=None,
        payload=None,
        ringName=None,
        rootNeighbourNetworkDeviceIds=None,
        rootNetworkDeviceId=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_configure_a_r_e_p_ring_on_f_a_b_r_i_c_deployment_default_val(api, validator):
    try:
        assert is_valid_configure_a_r_e_p_ring_on_f_a_b_r_i_c_deployment(
            validator,
            configure_a_r_e_p_ring_on_f_a_b_r_i_c_deployment_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_r_e_p_ring_configured_in_the_f_a_b_r_i_c_deployment(json_schema_validate, obj):
    json_schema_validate('jsd_743aca1b387f556ca0c87d563b3df8f2_v3_1_6_0').validate(obj)
    return True


def delete_rep_ring_configured_in_the_fabric_deployment(api):
    endpoint_result = api.industrial_configuration.delete_rep_ring_configured_in_the_fabric_deployment(
        id='string'
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_r_e_p_ring_configured_in_the_f_a_b_r_i_c_deployment(api, validator):
    try:
        assert is_valid_delete_r_e_p_ring_configured_in_the_f_a_b_r_i_c_deployment(
            validator,
            delete_rep_ring_configured_in_the_fabric_deployment(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_r_e_p_ring_configured_in_the_f_a_b_r_i_c_deployment_default_val(api):
    endpoint_result = api.industrial_configuration.delete_rep_ring_configured_in_the_fabric_deployment(
        id='string'
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_r_e_p_ring_configured_in_the_f_a_b_r_i_c_deployment_default_val(api, validator):
    try:
        assert is_valid_delete_r_e_p_ring_configured_in_the_f_a_b_r_i_c_deployment(
            validator,
            delete_r_e_p_ring_configured_in_the_f_a_b_r_i_c_deployment_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_m_r_p_rings(json_schema_validate, obj):
    json_schema_validate('jsd_70ef907f6fb75c9187c6377b24549af5_v3_1_6_0').validate(obj)
    return True


def retrieves_the_list_of_mrp_rings(api):
    endpoint_result = api.industrial_configuration.retrieves_the_list_of_mrp_rings(
        id=0,
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_list_of_m_r_p_rings(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_m_r_p_rings(
            validator,
            retrieves_the_list_of_mrp_rings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_m_r_p_rings_default_val(api):
    endpoint_result = api.industrial_configuration.retrieves_the_list_of_mrp_rings(
        id=None,
        limit=None,
        network_device_id='string',
        offset=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_list_of_m_r_p_rings_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_m_r_p_rings(
            validator,
            retrieves_the_list_of_m_r_p_rings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_m_r_p_rings(json_schema_validate, obj):
    json_schema_validate('jsd_54f4d2ca417d50d7912fb8ea4a31662d_v3_1_6_0').validate(obj)
    return True


def retrieves_the_count_of_m_r_p_rings(api):
    endpoint_result = api.industrial_configuration.retrieves_the_count_of_m_r_p_rings(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_count_of_m_r_p_rings(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_m_r_p_rings(
            validator,
            retrieves_the_count_of_m_r_p_rings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_m_r_p_rings_default_val(api):
    endpoint_result = api.industrial_configuration.retrieves_the_count_of_m_r_p_rings(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_count_of_m_r_p_rings_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_m_r_p_rings(
            validator,
            retrieves_the_count_of_m_r_p_rings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_network_devices_part_of_m_r_p_ring(json_schema_validate, obj):
    json_schema_validate('jsd_bf87f6cb9efb5451b84253593e548f98_v3_1_6_0').validate(obj)
    return True


def retrieves_the_list_of_network_devices_part_of_m_r_p_ring(api):
    endpoint_result = api.industrial_configuration.retrieves_the_list_of_network_devices_part_of_m_r_p_ring(
        id=0,
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_list_of_network_devices_part_of_m_r_p_ring(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_network_devices_part_of_m_r_p_ring(
            validator,
            retrieves_the_list_of_network_devices_part_of_m_r_p_ring(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_network_devices_part_of_m_r_p_ring_default_val(api):
    endpoint_result = api.industrial_configuration.retrieves_the_list_of_network_devices_part_of_m_r_p_ring(
        id=0,
        limit=None,
        network_device_id='string',
        offset=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_list_of_network_devices_part_of_m_r_p_ring_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_network_devices_part_of_m_r_p_ring(
            validator,
            retrieves_the_list_of_network_devices_part_of_m_r_p_ring_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_m_r_p_ring_members(json_schema_validate, obj):
    json_schema_validate('jsd_35bc1b3345f259e9859ac21a1ec694fe_v3_1_6_0').validate(obj)
    return True


def retrieves_the_count_of_m_r_p_ring_members(api):
    endpoint_result = api.industrial_configuration.retrieves_the_count_of_m_r_p_ring_members(
        id=0,
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_count_of_m_r_p_ring_members(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_m_r_p_ring_members(
            validator,
            retrieves_the_count_of_m_r_p_ring_members(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_m_r_p_ring_members_default_val(api):
    endpoint_result = api.industrial_configuration.retrieves_the_count_of_m_r_p_ring_members(
        id=0,
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_count_of_m_r_p_ring_members_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_m_r_p_ring_members(
            validator,
            retrieves_the_count_of_m_r_p_ring_members_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_configure_a_r_e_p_ring_on_n_o_n_f_a_b_r_i_c_deployment(json_schema_validate, obj):
    json_schema_validate('jsd_bbc4dab8193c546ab116e19863dff621_v3_1_6_0').validate(obj)
    return True


def configure_rep_ring_on_non_fabric_deployment(api):
    endpoint_result = api.industrial_configuration.configure_rep_ring_on_non_fabric_deployment(
        active_validation=True,
        deploymentMode='string',
        payload=None,
        ringName='string',
        rootNeighbourNetworkDeviceIds=['string'],
        rootNetworkDeviceId='string'
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_configure_a_r_e_p_ring_on_n_o_n_f_a_b_r_i_c_deployment(api, validator):
    try:
        assert is_valid_configure_a_r_e_p_ring_on_n_o_n_f_a_b_r_i_c_deployment(
            validator,
            configure_rep_ring_on_non_fabric_deployment(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def configure_a_r_e_p_ring_on_n_o_n_f_a_b_r_i_c_deployment_default_val(api):
    endpoint_result = api.industrial_configuration.configure_rep_ring_on_non_fabric_deployment(
        active_validation=True,
        deploymentMode=None,
        payload=None,
        ringName=None,
        rootNeighbourNetworkDeviceIds=None,
        rootNetworkDeviceId=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_configure_a_r_e_p_ring_on_n_o_n_f_a_b_r_i_c_deployment_default_val(api, validator):
    try:
        assert is_valid_configure_a_r_e_p_ring_on_n_o_n_f_a_b_r_i_c_deployment(
            validator,
            configure_a_r_e_p_ring_on_n_o_n_f_a_b_r_i_c_deployment_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_r_e_p_ring_configured_in_the_n_o_n_f_a_b_r_i_c_deployment(json_schema_validate, obj):
    json_schema_validate('jsd_4dcf9b8fecdd57f0bb7a33d358e6be37_v3_1_6_0').validate(obj)
    return True


def delete_rep_ring_configured_in_the_non_fabric_deployment(api):
    endpoint_result = api.industrial_configuration.delete_rep_ring_configured_in_the_non_fabric_deployment(
        id='string'
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_r_e_p_ring_configured_in_the_n_o_n_f_a_b_r_i_c_deployment(api, validator):
    try:
        assert is_valid_delete_r_e_p_ring_configured_in_the_n_o_n_f_a_b_r_i_c_deployment(
            validator,
            delete_rep_ring_configured_in_the_non_fabric_deployment(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_r_e_p_ring_configured_in_the_n_o_n_f_a_b_r_i_c_deployment_default_val(api):
    endpoint_result = api.industrial_configuration.delete_rep_ring_configured_in_the_non_fabric_deployment(
        id='string'
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_r_e_p_ring_configured_in_the_n_o_n_f_a_b_r_i_c_deployment_default_val(api, validator):
    try:
        assert is_valid_delete_r_e_p_ring_configured_in_the_n_o_n_f_a_b_r_i_c_deployment(
            validator,
            delete_r_e_p_ring_configured_in_the_n_o_n_f_a_b_r_i_c_deployment_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_r_e_p_rings(json_schema_validate, obj):
    json_schema_validate('jsd_5344fa2127b55124a3a00b2991b77db6_v3_1_6_0').validate(obj)
    return True


def retrieves_the_list_of_rep_rings(api):
    endpoint_result = api.industrial_configuration.retrieves_the_list_of_rep_rings(
        active_validation=True,
        deploymentMode='string',
        limit=0,
        networkDeviceId='string',
        offset=0,
        payload=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_list_of_r_e_p_rings(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_r_e_p_rings(
            validator,
            retrieves_the_list_of_rep_rings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_r_e_p_rings_default_val(api):
    endpoint_result = api.industrial_configuration.retrieves_the_list_of_rep_rings(
        active_validation=True,
        deploymentMode=None,
        limit=None,
        networkDeviceId=None,
        offset=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_list_of_r_e_p_rings_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_r_e_p_rings(
            validator,
            retrieves_the_list_of_r_e_p_rings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_r_e_p_rings(json_schema_validate, obj):
    json_schema_validate('jsd_2d9f276a532e5eeb86bb591f8537fcc7_v3_1_6_0').validate(obj)
    return True


def retrieves_the_count_of_rep_rings(api):
    endpoint_result = api.industrial_configuration.retrieves_the_count_of_rep_rings(
        active_validation=True,
        deploymentMode='string',
        networkDeviceId='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_count_of_r_e_p_rings(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_r_e_p_rings(
            validator,
            retrieves_the_count_of_rep_rings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_r_e_p_rings_default_val(api):
    endpoint_result = api.industrial_configuration.retrieves_the_count_of_rep_rings(
        active_validation=True,
        deploymentMode=None,
        networkDeviceId=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_count_of_r_e_p_rings_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_r_e_p_rings(
            validator,
            retrieves_the_count_of_r_e_p_rings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_r_e_p_ring_based_on_the_ring_id(json_schema_validate, obj):
    json_schema_validate('jsd_98534ce1469c515d8a72455779e3a484_v3_1_6_0').validate(obj)
    return True


def get_the_rep_ring_based_on_the_ring_id(api):
    endpoint_result = api.industrial_configuration.get_the_rep_ring_based_on_the_ring_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_get_the_r_e_p_ring_based_on_the_ring_id(api, validator):
    try:
        assert is_valid_get_the_r_e_p_ring_based_on_the_ring_id(
            validator,
            get_the_rep_ring_based_on_the_ring_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_r_e_p_ring_based_on_the_ring_id_default_val(api):
    endpoint_result = api.industrial_configuration.get_the_rep_ring_based_on_the_ring_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_get_the_r_e_p_ring_based_on_the_ring_id_default_val(api, validator):
    try:
        assert is_valid_get_the_r_e_p_ring_based_on_the_ring_id(
            validator,
            get_the_r_e_p_ring_based_on_the_ring_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

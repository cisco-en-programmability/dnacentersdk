# -*- coding: utf-8 -*-
"""CatalystCenterAPI topology API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '3.1.3.0', reason='version does not match')


def is_valid_get_overall_network_health_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4b0753b63045528194f2f5bbf8ae432d_v3_1_3_0').validate(obj)
    return True


def get_overall_network_health_v1(api):
    endpoint_result = api.topology.get_overall_network_health_v1(
        timestamp=0
    )
    return endpoint_result


@pytest.mark.topology
def test_get_overall_network_health_v1(api, validator):
    try:
        assert is_valid_get_overall_network_health_v1(
            validator,
            get_overall_network_health_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_overall_network_health_v1_default_val(api):
    endpoint_result = api.topology.get_overall_network_health_v1(
        timestamp=None
    )
    return endpoint_result


@pytest.mark.topology
def test_get_overall_network_health_v1_default_val(api, validator):
    try:
        assert is_valid_get_overall_network_health_v1(
            validator,
            get_overall_network_health_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_topology_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_392b3f79d3b45b98849d9180cc08018e_v3_1_3_0').validate(obj)
    return True


def get_topology_details_v1(api):
    endpoint_result = api.topology.get_topology_details_v1(
        vlan_id='string'
    )
    return endpoint_result


@pytest.mark.topology
def test_get_topology_details_v1(api, validator):
    try:
        assert is_valid_get_topology_details_v1(
            validator,
            get_topology_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_topology_details_v1_default_val(api):
    endpoint_result = api.topology.get_topology_details_v1(
        vlan_id='string'
    )
    return endpoint_result


@pytest.mark.topology
def test_get_topology_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_topology_details_v1(
            validator,
            get_topology_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_l3_topology_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c7e9c39880735e7684291bc5dc3ba994_v3_1_3_0').validate(obj)
    return True


def get_l3_topology_details_v1(api):
    endpoint_result = api.topology.get_l3_topology_details_v1(
        topology_type='string'
    )
    return endpoint_result


@pytest.mark.topology
def test_get_l3_topology_details_v1(api, validator):
    try:
        assert is_valid_get_l3_topology_details_v1(
            validator,
            get_l3_topology_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_l3_topology_details_v1_default_val(api):
    endpoint_result = api.topology.get_l3_topology_details_v1(
        topology_type='string'
    )
    return endpoint_result


@pytest.mark.topology
def test_get_l3_topology_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_l3_topology_details_v1(
            validator,
            get_l3_topology_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_physical_topology_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4199688eb4ab5a978fe8785516c8af42_v3_1_3_0').validate(obj)
    return True


def get_physical_topology_v1(api):
    endpoint_result = api.topology.get_physical_topology_v1(
        node_type='string'
    )
    return endpoint_result


@pytest.mark.topology
def test_get_physical_topology_v1(api, validator):
    try:
        assert is_valid_get_physical_topology_v1(
            validator,
            get_physical_topology_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_physical_topology_v1_default_val(api):
    endpoint_result = api.topology.get_physical_topology_v1(
        node_type=None
    )
    return endpoint_result


@pytest.mark.topology
def test_get_physical_topology_v1_default_val(api, validator):
    try:
        assert is_valid_get_physical_topology_v1(
            validator,
            get_physical_topology_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_topology_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f7abdb7ab46a5918a74e839488ff6ae0_v3_1_3_0').validate(obj)
    return True


def get_site_topology_v1(api):
    endpoint_result = api.topology.get_site_topology_v1(

    )
    return endpoint_result


@pytest.mark.topology
def test_get_site_topology_v1(api, validator):
    try:
        assert is_valid_get_site_topology_v1(
            validator,
            get_site_topology_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_topology_v1_default_val(api):
    endpoint_result = api.topology.get_site_topology_v1(

    )
    return endpoint_result


@pytest.mark.topology
def test_get_site_topology_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_topology_v1(
            validator,
            get_site_topology_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_vlan_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fb6000ce8d8854bc80be3803b8dee1b7_v3_1_3_0').validate(obj)
    return True


def get_vlan_details_v1(api):
    endpoint_result = api.topology.get_vlan_details_v1(

    )
    return endpoint_result


@pytest.mark.topology
def test_get_vlan_details_v1(api, validator):
    try:
        assert is_valid_get_vlan_details_v1(
            validator,
            get_vlan_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_vlan_details_v1_default_val(api):
    endpoint_result = api.topology.get_vlan_details_v1(

    )
    return endpoint_result


@pytest.mark.topology
def test_get_vlan_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_vlan_details_v1(
            validator,
            get_vlan_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

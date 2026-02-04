# -*- coding: utf-8 -*-
"""DNACenterAPI cisco_i_m_c API fixtures and tests.

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


def is_valid_retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes(json_schema_validate, obj):
    json_schema_validate('jsd_80b7ed1910345a8b9b9ad88aeee4f109_v3_1_6_0').validate(obj)
    return True


def retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes(api):
    endpoint_result = api.cisco_i_m_c.retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes(

    )
    return endpoint_result


@pytest.mark.cisco_i_m_c
def test_retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes(api, validator):
    try:
        assert is_valid_retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes(
            validator,
            retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes_default_val(api):
    endpoint_result = api.cisco_i_m_c.retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes(

    )
    return endpoint_result


@pytest.mark.cisco_i_m_c
def test_retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes_default_val(api, validator):
    try:
        assert is_valid_retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes(
            validator,
            retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_adds_cisco_i_m_c_configuration_to_a_catalyst_center_node(json_schema_validate, obj):
    json_schema_validate('jsd_00d5f8cf25475dc5be53f35357aca5a4_v3_1_6_0').validate(obj)
    return True


def adds_cisco_i_m_c_configuration_to_a_catalyst_center_node(api):
    endpoint_result = api.cisco_i_m_c.adds_cisco_i_m_c_configuration_to_a_catalyst_center_node(
        active_validation=True,
        ipAddress='string',
        nodeId='string',
        password='string',
        payload=None,
        username='string'
    )
    return endpoint_result


@pytest.mark.cisco_i_m_c
def test_adds_cisco_i_m_c_configuration_to_a_catalyst_center_node(api, validator):
    try:
        assert is_valid_adds_cisco_i_m_c_configuration_to_a_catalyst_center_node(
            validator,
            adds_cisco_i_m_c_configuration_to_a_catalyst_center_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def adds_cisco_i_m_c_configuration_to_a_catalyst_center_node_default_val(api):
    endpoint_result = api.cisco_i_m_c.adds_cisco_i_m_c_configuration_to_a_catalyst_center_node(
        active_validation=True,
        ipAddress=None,
        nodeId=None,
        password=None,
        payload=None,
        username=None
    )
    return endpoint_result


@pytest.mark.cisco_i_m_c
def test_adds_cisco_i_m_c_configuration_to_a_catalyst_center_node_default_val(api, validator):
    try:
        assert is_valid_adds_cisco_i_m_c_configuration_to_a_catalyst_center_node(
            validator,
            adds_cisco_i_m_c_configuration_to_a_catalyst_center_node_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(json_schema_validate, obj):
    json_schema_validate('jsd_6baa237a3253535e875c62928443888b_v3_1_6_0').validate(obj)
    return True


def deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(api):
    endpoint_result = api.cisco_i_m_c.deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
        id='string'
    )
    return endpoint_result


@pytest.mark.cisco_i_m_c
def test_deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(api, validator):
    try:
        assert is_valid_deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
            validator,
            deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_default_val(api):
    endpoint_result = api.cisco_i_m_c.deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
        id='string'
    )
    return endpoint_result


@pytest.mark.cisco_i_m_c
def test_deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_default_val(api, validator):
    try:
        assert is_valid_deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
            validator,
            deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(json_schema_validate, obj):
    json_schema_validate('jsd_3820afae98de597f918fe9d08045026c_v3_1_6_0').validate(obj)
    return True


def retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(api):
    endpoint_result = api.cisco_i_m_c.retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
        id='string'
    )
    return endpoint_result


@pytest.mark.cisco_i_m_c
def test_retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(api, validator):
    try:
        assert is_valid_retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
            validator,
            retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_default_val(api):
    endpoint_result = api.cisco_i_m_c.retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
        id='string'
    )
    return endpoint_result


@pytest.mark.cisco_i_m_c
def test_retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
            validator,
            retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(json_schema_validate, obj):
    json_schema_validate('jsd_19f2562a2d8e5ec287738032961762ed_v3_1_6_0').validate(obj)
    return True


def updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(api):
    endpoint_result = api.cisco_i_m_c.updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
        active_validation=True,
        id='string',
        ipAddress='string',
        password='string',
        payload=None,
        username='string'
    )
    return endpoint_result


@pytest.mark.cisco_i_m_c
def test_updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(api, validator):
    try:
        assert is_valid_updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
            validator,
            updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_default_val(api):
    endpoint_result = api.cisco_i_m_c.updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
        active_validation=True,
        id='string',
        ipAddress=None,
        password=None,
        payload=None,
        username=None
    )
    return endpoint_result


@pytest.mark.cisco_i_m_c
def test_updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_default_val(api, validator):
    try:
        assert is_valid_updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
            validator,
            updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

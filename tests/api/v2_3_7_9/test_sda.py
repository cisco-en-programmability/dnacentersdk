# -*- coding: utf-8 -*-
"""CatalystCenterAPI sda API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.9', reason='version does not match')


def is_valid_read_list_of_fabric_sites_with_their_health_summary_v1(json_schema_validate, obj):
    json_schema_validate('jsd_304921a4f14955aea82772d0299ffb0d_v2_3_7_9').validate(obj)
    return True


def read_list_of_fabric_sites_with_their_health_summary_v1(api):
    endpoint_result = api.sda.read_list_of_fabric_sites_with_their_health_summary_v1(
        attribute='string',
        end_time=0,
        id='string',
        limit=0,
        offset=0,
        order='string',
        sort_by='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_read_list_of_fabric_sites_with_their_health_summary_v1(api, validator):
    try:
        assert is_valid_read_list_of_fabric_sites_with_their_health_summary_v1(
            validator,
            read_list_of_fabric_sites_with_their_health_summary_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_list_of_fabric_sites_with_their_health_summary_v1_default_val(api):
    endpoint_result = api.sda.read_list_of_fabric_sites_with_their_health_summary_v1(
        attribute=None,
        end_time=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.sda
def test_read_list_of_fabric_sites_with_their_health_summary_v1_default_val(api, validator):
    try:
        assert is_valid_read_list_of_fabric_sites_with_their_health_summary_v1(
            validator,
            read_list_of_fabric_sites_with_their_health_summary_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_fabric_site_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1d7eeb4af6215c3599693c8f36711ddd_v2_3_7_9').validate(obj)
    return True


def read_fabric_site_count_v1(api):
    endpoint_result = api.sda.read_fabric_site_count_v1(
        end_time=0,
        id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.sda
def test_read_fabric_site_count_v1(api, validator):
    try:
        assert is_valid_read_fabric_site_count_v1(
            validator,
            read_fabric_site_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_fabric_site_count_v1_default_val(api):
    endpoint_result = api.sda.read_fabric_site_count_v1(
        end_time=None,
        id=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.sda
def test_read_fabric_site_count_v1_default_val(api, validator):
    try:
        assert is_valid_read_fabric_site_count_v1(
            validator,
            read_fabric_site_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_fabric_sites_with_health_summary_from_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_daad662049da50a985dbd37a3a7fd28c_v2_3_7_9').validate(obj)
    return True


def read_fabric_sites_with_health_summary_from_id_v1(api):
    endpoint_result = api.sda.read_fabric_sites_with_health_summary_from_id_v1(
        attribute='string',
        end_time=0,
        id='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_read_fabric_sites_with_health_summary_from_id_v1(api, validator):
    try:
        assert is_valid_read_fabric_sites_with_health_summary_from_id_v1(
            validator,
            read_fabric_sites_with_health_summary_from_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_fabric_sites_with_health_summary_from_id_v1_default_val(api):
    endpoint_result = api.sda.read_fabric_sites_with_health_summary_from_id_v1(
        attribute=None,
        end_time=None,
        id='string',
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.sda
def test_read_fabric_sites_with_health_summary_from_id_v1_default_val(api, validator):
    try:
        assert is_valid_read_fabric_sites_with_health_summary_from_id_v1(
            validator,
            read_fabric_sites_with_health_summary_from_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_the_trend_analytics_data_for_a_fabric_site_in_the_specified_time_range_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9f333e0d9b155d36a7dab8b54f9ef9b9_v2_3_7_9').validate(obj)
    return True


def the_trend_analytics_data_for_a_fabric_site_in_the_specified_time_range_v1(api):
    endpoint_result = api.sda.the_trend_analytics_data_for_a_fabric_site_in_the_specified_time_range_v1(
        attribute='string',
        end_time=0,
        id='string',
        limit=0,
        offset=0,
        order='string',
        start_time=0,
        trend_interval='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_the_trend_analytics_data_for_a_fabric_site_in_the_specified_time_range_v1(api, validator):
    try:
        assert is_valid_the_trend_analytics_data_for_a_fabric_site_in_the_specified_time_range_v1(
            validator,
            the_trend_analytics_data_for_a_fabric_site_in_the_specified_time_range_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def the_trend_analytics_data_for_a_fabric_site_in_the_specified_time_range_v1_default_val(api):
    endpoint_result = api.sda.the_trend_analytics_data_for_a_fabric_site_in_the_specified_time_range_v1(
        attribute=None,
        end_time=None,
        id='string',
        limit=None,
        offset=None,
        order=None,
        start_time=None,
        trend_interval=None
    )
    return endpoint_result


@pytest.mark.sda
def test_the_trend_analytics_data_for_a_fabric_site_in_the_specified_time_range_v1_default_val(api, validator):
    try:
        assert is_valid_the_trend_analytics_data_for_a_fabric_site_in_the_specified_time_range_v1(
            validator,
            the_trend_analytics_data_for_a_fabric_site_in_the_specified_time_range_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_fabric_entity_summary_v1(json_schema_validate, obj):
    json_schema_validate('jsd_847088ee22675da09af2616f46776746_v2_3_7_9').validate(obj)
    return True


def read_fabric_entity_summary_v1(api):
    endpoint_result = api.sda.read_fabric_entity_summary_v1(
        end_time=0,
        start_time=0
    )
    return endpoint_result


@pytest.mark.sda
def test_read_fabric_entity_summary_v1(api, validator):
    try:
        assert is_valid_read_fabric_entity_summary_v1(
            validator,
            read_fabric_entity_summary_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_fabric_entity_summary_v1_default_val(api):
    endpoint_result = api.sda.read_fabric_entity_summary_v1(
        end_time=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.sda
def test_read_fabric_entity_summary_v1_default_val(api, validator):
    try:
        assert is_valid_read_fabric_entity_summary_v1(
            validator,
            read_fabric_entity_summary_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_list_of_transit_networks_with_their_health_summary_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f6abbbea801355559c36dd413a32abe3_v2_3_7_9').validate(obj)
    return True


def read_list_of_transit_networks_with_their_health_summary_v1(api):
    endpoint_result = api.sda.read_list_of_transit_networks_with_their_health_summary_v1(
        attribute='string',
        end_time=0,
        id='string',
        limit=0,
        offset=0,
        order='string',
        sort_by='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_read_list_of_transit_networks_with_their_health_summary_v1(api, validator):
    try:
        assert is_valid_read_list_of_transit_networks_with_their_health_summary_v1(
            validator,
            read_list_of_transit_networks_with_their_health_summary_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_list_of_transit_networks_with_their_health_summary_v1_default_val(api):
    endpoint_result = api.sda.read_list_of_transit_networks_with_their_health_summary_v1(
        attribute=None,
        end_time=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.sda
def test_read_list_of_transit_networks_with_their_health_summary_v1_default_val(api, validator):
    try:
        assert is_valid_read_list_of_transit_networks_with_their_health_summary_v1(
            validator,
            read_list_of_transit_networks_with_their_health_summary_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_transit_networks_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5d8b91fbaa8f5872979edf536c094b30_v2_3_7_9').validate(obj)
    return True


def read_transit_networks_count_v1(api):
    endpoint_result = api.sda.read_transit_networks_count_v1(
        end_time=0,
        id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.sda
def test_read_transit_networks_count_v1(api, validator):
    try:
        assert is_valid_read_transit_networks_count_v1(
            validator,
            read_transit_networks_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_transit_networks_count_v1_default_val(api):
    endpoint_result = api.sda.read_transit_networks_count_v1(
        end_time=None,
        id=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.sda
def test_read_transit_networks_count_v1_default_val(api, validator):
    try:
        assert is_valid_read_transit_networks_count_v1(
            validator,
            read_transit_networks_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_transit_network_with_its_health_summary_from_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b95b73d75c7956acab07b3d5ba39d191_v2_3_7_9').validate(obj)
    return True


def read_transit_network_with_its_health_summary_from_id_v1(api):
    endpoint_result = api.sda.read_transit_network_with_its_health_summary_from_id_v1(
        attribute='string',
        end_time=0,
        id='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_read_transit_network_with_its_health_summary_from_id_v1(api, validator):
    try:
        assert is_valid_read_transit_network_with_its_health_summary_from_id_v1(
            validator,
            read_transit_network_with_its_health_summary_from_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_transit_network_with_its_health_summary_from_id_v1_default_val(api):
    endpoint_result = api.sda.read_transit_network_with_its_health_summary_from_id_v1(
        attribute=None,
        end_time=None,
        id='string',
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.sda
def test_read_transit_network_with_its_health_summary_from_id_v1_default_val(api, validator):
    try:
        assert is_valid_read_transit_network_with_its_health_summary_from_id_v1(
            validator,
            read_transit_network_with_its_health_summary_from_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3b57676da2385a4bb7c6e5dc9b8a89dc_v2_3_7_9').validate(obj)
    return True


def the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range_v1(api):
    endpoint_result = api.sda.the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range_v1(
        attribute='string',
        end_time=0,
        id='string',
        limit=0,
        offset=0,
        order='string',
        start_time=0,
        trend_interval='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range_v1(api, validator):
    try:
        assert is_valid_the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range_v1(
            validator,
            the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range_v1_default_val(api):
    endpoint_result = api.sda.the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range_v1(
        attribute=None,
        end_time=None,
        id='string',
        limit=None,
        offset=None,
        order=None,
        start_time=None,
        trend_interval=None
    )
    return endpoint_result


@pytest.mark.sda
def test_the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range_v1_default_val(api, validator):
    try:
        assert is_valid_the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range_v1(
            validator,
            the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_list_of_virtual_networks_with_their_health_summary_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a89a96bc132d58d5abc0bdf4d3868b42_v2_3_7_9').validate(obj)
    return True


def read_list_of_virtual_networks_with_their_health_summary_v1(api):
    endpoint_result = api.sda.read_list_of_virtual_networks_with_their_health_summary_v1(
        attribute='string',
        end_time=0,
        id='string',
        limit=0,
        offset=0,
        order='string',
        sort_by='string',
        start_time=0,
        view='string',
        vn_layer='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_read_list_of_virtual_networks_with_their_health_summary_v1(api, validator):
    try:
        assert is_valid_read_list_of_virtual_networks_with_their_health_summary_v1(
            validator,
            read_list_of_virtual_networks_with_their_health_summary_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_list_of_virtual_networks_with_their_health_summary_v1_default_val(api):
    endpoint_result = api.sda.read_list_of_virtual_networks_with_their_health_summary_v1(
        attribute=None,
        end_time=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        start_time=None,
        view=None,
        vn_layer=None
    )
    return endpoint_result


@pytest.mark.sda
def test_read_list_of_virtual_networks_with_their_health_summary_v1_default_val(api, validator):
    try:
        assert is_valid_read_list_of_virtual_networks_with_their_health_summary_v1(
            validator,
            read_list_of_virtual_networks_with_their_health_summary_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_virtual_networks_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8eb1c33328c25d25b062bc85609b23df_v2_3_7_9').validate(obj)
    return True


def read_virtual_networks_count_v1(api):
    endpoint_result = api.sda.read_virtual_networks_count_v1(
        end_time=0,
        id='string',
        start_time=0,
        vn_layer='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_read_virtual_networks_count_v1(api, validator):
    try:
        assert is_valid_read_virtual_networks_count_v1(
            validator,
            read_virtual_networks_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_virtual_networks_count_v1_default_val(api):
    endpoint_result = api.sda.read_virtual_networks_count_v1(
        end_time=None,
        id=None,
        start_time=None,
        vn_layer=None
    )
    return endpoint_result


@pytest.mark.sda
def test_read_virtual_networks_count_v1_default_val(api, validator):
    try:
        assert is_valid_read_virtual_networks_count_v1(
            validator,
            read_virtual_networks_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_virtual_network_with_its_health_summary_from_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bbb30e8498ac5c8f8bcb5c5fd33cff43_v2_3_7_9').validate(obj)
    return True


def read_virtual_network_with_its_health_summary_from_id_v1(api):
    endpoint_result = api.sda.read_virtual_network_with_its_health_summary_from_id_v1(
        attribute='string',
        end_time=0,
        id='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_read_virtual_network_with_its_health_summary_from_id_v1(api, validator):
    try:
        assert is_valid_read_virtual_network_with_its_health_summary_from_id_v1(
            validator,
            read_virtual_network_with_its_health_summary_from_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_virtual_network_with_its_health_summary_from_id_v1_default_val(api):
    endpoint_result = api.sda.read_virtual_network_with_its_health_summary_from_id_v1(
        attribute=None,
        end_time=None,
        id='string',
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.sda
def test_read_virtual_network_with_its_health_summary_from_id_v1_default_val(api, validator):
    try:
        assert is_valid_read_virtual_network_with_its_health_summary_from_id_v1(
            validator,
            read_virtual_network_with_its_health_summary_from_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_the_trend_analytics_data_for_a_virtual_network_in_the_specified_time_range_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1f73065603c85196a35142243bc48509_v2_3_7_9').validate(obj)
    return True


def the_trend_analytics_data_for_a_virtual_network_in_the_specified_time_range_v1(api):
    endpoint_result = api.sda.the_trend_analytics_data_for_a_virtual_network_in_the_specified_time_range_v1(
        attribute='string',
        end_time=0,
        id='string',
        limit=0,
        offset=0,
        order='string',
        start_time=0,
        trend_interval='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_the_trend_analytics_data_for_a_virtual_network_in_the_specified_time_range_v1(api, validator):
    try:
        assert is_valid_the_trend_analytics_data_for_a_virtual_network_in_the_specified_time_range_v1(
            validator,
            the_trend_analytics_data_for_a_virtual_network_in_the_specified_time_range_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def the_trend_analytics_data_for_a_virtual_network_in_the_specified_time_range_v1_default_val(api):
    endpoint_result = api.sda.the_trend_analytics_data_for_a_virtual_network_in_the_specified_time_range_v1(
        attribute=None,
        end_time=None,
        id='string',
        limit=None,
        offset=None,
        order=None,
        start_time=None,
        trend_interval=None
    )
    return endpoint_result


@pytest.mark.sda
def test_the_trend_analytics_data_for_a_virtual_network_in_the_specified_time_range_v1_default_val(api, validator):
    try:
        assert is_valid_the_trend_analytics_data_for_a_virtual_network_in_the_specified_time_range_v1(
            validator,
            the_trend_analytics_data_for_a_virtual_network_in_the_specified_time_range_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_e414dcbeeabd5a359352a0e2ad5ec3f5_v2_3_7_9').validate(obj)
    return True


def get_default_authentication_profile(api):
    endpoint_result = api.sda.get_default_authentication_profile(
        authenticate_template_name='string',
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_default_authentication_profile(api, validator):
    try:
        assert is_valid_get_default_authentication_profile(
            validator,
            get_default_authentication_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_default_authentication_profile_default_val(api):
    endpoint_result = api.sda.get_default_authentication_profile(
        authenticate_template_name=None,
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_default_authentication_profile_default_val(api, validator):
    try:
        assert is_valid_get_default_authentication_profile(
            validator,
            get_default_authentication_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_d1d42ef2f1895a82a2830bf1353e6baa_v2_3_7_9').validate(obj)
    return True


def add_default_authentication_profile(api):
    endpoint_result = api.sda.add_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_default_authentication_profile(api, validator):
    try:
        assert is_valid_add_default_authentication_profile(
            validator,
            add_default_authentication_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_default_authentication_profile_default_val(api):
    endpoint_result = api.sda.add_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_default_authentication_profile_default_val(api, validator):
    try:
        assert is_valid_add_default_authentication_profile(
            validator,
            add_default_authentication_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_0d999a1d36ee52babb6b619877dad734_v2_3_7_9').validate(obj)
    return True


def update_default_authentication_profile(api):
    endpoint_result = api.sda.update_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_default_authentication_profile(api, validator):
    try:
        assert is_valid_update_default_authentication_profile(
            validator,
            update_default_authentication_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_default_authentication_profile_default_val(api):
    endpoint_result = api.sda.update_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_default_authentication_profile_default_val(api, validator):
    try:
        assert is_valid_update_default_authentication_profile(
            validator,
            update_default_authentication_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_916231b2be8b5dda8b81620b903afe9f_v2_3_7_9').validate(obj)
    return True


def delete_default_authentication_profile(api):
    endpoint_result = api.sda.delete_default_authentication_profile(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_default_authentication_profile(api, validator):
    try:
        assert is_valid_delete_default_authentication_profile(
            validator,
            delete_default_authentication_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_default_authentication_profile_default_val(api):
    endpoint_result = api.sda.delete_default_authentication_profile(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_default_authentication_profile_default_val(api, validator):
    try:
        assert is_valid_delete_default_authentication_profile(
            validator,
            delete_default_authentication_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_adds_border_device(json_schema_validate, obj):
    json_schema_validate('jsd_b6f2d8e46cdd5f05bb06f52cd1b26fb2_v2_3_7_9').validate(obj)
    return True


def adds_border_device(api):
    endpoint_result = api.sda.adds_border_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_adds_border_device(api, validator):
    try:
        assert is_valid_adds_border_device(
            validator,
            adds_border_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def adds_border_device_default_val(api):
    endpoint_result = api.sda.adds_border_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_adds_border_device_default_val(api, validator):
    try:
        assert is_valid_adds_border_device(
            validator,
            adds_border_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_border_device_detail(json_schema_validate, obj):
    json_schema_validate('jsd_7aae881ff75d5488a5325ea949be4c5b_v2_3_7_9').validate(obj)
    return True


def gets_border_device_detail(api):
    endpoint_result = api.sda.gets_border_device_detail(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_gets_border_device_detail(api, validator):
    try:
        assert is_valid_gets_border_device_detail(
            validator,
            gets_border_device_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_border_device_detail_default_val(api):
    endpoint_result = api.sda.gets_border_device_detail(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_gets_border_device_detail_default_val(api, validator):
    try:
        assert is_valid_gets_border_device_detail(
            validator,
            gets_border_device_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_border_device(json_schema_validate, obj):
    json_schema_validate('jsd_9a102ba155e35f84b7af3396aa407d02_v2_3_7_9').validate(obj)
    return True


def deletes_border_device(api):
    endpoint_result = api.sda.deletes_border_device(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_deletes_border_device(api, validator):
    try:
        assert is_valid_deletes_border_device(
            validator,
            deletes_border_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_border_device_default_val(api):
    endpoint_result = api.sda.deletes_border_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_deletes_border_device_default_val(api, validator):
    try:
        assert is_valid_deletes_border_device(
            validator,
            deletes_border_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_control_plane_device(json_schema_validate, obj):
    json_schema_validate('jsd_6c05702ed7075a2f9ab14c051f1ac883_v2_3_7_9').validate(obj)
    return True


def delete_control_plane_device(api):
    endpoint_result = api.sda.delete_control_plane_device(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_control_plane_device(api, validator):
    try:
        assert is_valid_delete_control_plane_device(
            validator,
            delete_control_plane_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_control_plane_device_default_val(api):
    endpoint_result = api.sda.delete_control_plane_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_control_plane_device_default_val(api, validator):
    try:
        assert is_valid_delete_control_plane_device(
            validator,
            delete_control_plane_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_control_plane_device(json_schema_validate, obj):
    json_schema_validate('jsd_c1a89e4a8ff15608bc6c10d7ef7389d7_v2_3_7_9').validate(obj)
    return True


def get_control_plane_device(api):
    endpoint_result = api.sda.get_control_plane_device(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_control_plane_device(api, validator):
    try:
        assert is_valid_get_control_plane_device(
            validator,
            get_control_plane_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_control_plane_device_default_val(api):
    endpoint_result = api.sda.get_control_plane_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_control_plane_device_default_val(api, validator):
    try:
        assert is_valid_get_control_plane_device(
            validator,
            get_control_plane_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_control_plane_device(json_schema_validate, obj):
    json_schema_validate('jsd_54ae7f02a3d051f2baf7cc087990d658_v2_3_7_9').validate(obj)
    return True


def add_control_plane_device(api):
    endpoint_result = api.sda.add_control_plane_device(
        active_validation=True,
        deviceManagementIpAddress='string',
        payload=None,
        routeDistributionProtocol='string',
        siteNameHierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_add_control_plane_device(api, validator):
    try:
        assert is_valid_add_control_plane_device(
            validator,
            add_control_plane_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_control_plane_device_default_val(api):
    endpoint_result = api.sda.add_control_plane_device(
        active_validation=True,
        deviceManagementIpAddress=None,
        payload=None,
        routeDistributionProtocol=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_control_plane_device_default_val(api, validator):
    try:
        assert is_valid_add_control_plane_device(
            validator,
            add_control_plane_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_info(json_schema_validate, obj):
    json_schema_validate('jsd_d12790f461c553a08142ec740db5efbf_v2_3_7_9').validate(obj)
    return True


def get_device_info(api):
    endpoint_result = api.sda.get_device_info(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_device_info(api, validator):
    try:
        assert is_valid_get_device_info(
            validator,
            get_device_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_info_default_val(api):
    endpoint_result = api.sda.get_device_info(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_device_info_default_val(api, validator):
    try:
        assert is_valid_get_device_info(
            validator,
            get_device_info_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_role_in_sda_fabric_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1ea24b22ce355a229b7fd067401ddf3a_v2_3_7_9').validate(obj)
    return True


def get_device_role_in_sda_fabric_v1(api):
    endpoint_result = api.sda.get_device_role_in_sda_fabric_v1(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_device_role_in_sda_fabric_v1(api, validator):
    try:
        assert is_valid_get_device_role_in_sda_fabric_v1(
            validator,
            get_device_role_in_sda_fabric_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_role_in_sda_fabric_v1_default_val(api):
    endpoint_result = api.sda.get_device_role_in_sda_fabric_v1(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_device_role_in_sda_fabric_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_role_in_sda_fabric_v1(
            validator,
            get_device_role_in_sda_fabric_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_edge_device(json_schema_validate, obj):
    json_schema_validate('jsd_e0c7b28d55c85d49a84c1403ca14bd5f_v2_3_7_9').validate(obj)
    return True


def add_edge_device(api):
    endpoint_result = api.sda.add_edge_device(
        active_validation=True,
        deviceManagementIpAddress='string',
        payload=None,
        siteNameHierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_add_edge_device(api, validator):
    try:
        assert is_valid_add_edge_device(
            validator,
            add_edge_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_edge_device_default_val(api):
    endpoint_result = api.sda.add_edge_device(
        active_validation=True,
        deviceManagementIpAddress=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_edge_device_default_val(api, validator):
    try:
        assert is_valid_add_edge_device(
            validator,
            add_edge_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_edge_device(json_schema_validate, obj):
    json_schema_validate('jsd_409b70d8c6f85254a053ab281fd9e8fc_v2_3_7_9').validate(obj)
    return True


def delete_edge_device(api):
    endpoint_result = api.sda.delete_edge_device(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_edge_device(api, validator):
    try:
        assert is_valid_delete_edge_device(
            validator,
            delete_edge_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_edge_device_default_val(api):
    endpoint_result = api.sda.delete_edge_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_edge_device_default_val(api, validator):
    try:
        assert is_valid_delete_edge_device(
            validator,
            delete_edge_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_edge_device(json_schema_validate, obj):
    json_schema_validate('jsd_5a2ee396d6595001acfbbcdfa25093ff_v2_3_7_9').validate(obj)
    return True


def get_edge_device(api):
    endpoint_result = api.sda.get_edge_device(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_edge_device(api, validator):
    try:
        assert is_valid_get_edge_device(
            validator,
            get_edge_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_edge_device_default_val(api):
    endpoint_result = api.sda.get_edge_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_edge_device_default_val(api, validator):
    try:
        assert is_valid_get_edge_device(
            validator,
            get_edge_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site(json_schema_validate, obj):
    json_schema_validate('jsd_0d23f3e54f8c59caac3ca905f7bf543a_v2_3_7_9').validate(obj)
    return True


def get_site(api):
    endpoint_result = api.sda.get_site(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_site(api, validator):
    try:
        assert is_valid_get_site(
            validator,
            get_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_default_val(api):
    endpoint_result = api.sda.get_site(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_site_default_val(api, validator):
    try:
        assert is_valid_get_site(
            validator,
            get_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_site(json_schema_validate, obj):
    json_schema_validate('jsd_9124f9db3b115f0b8c8b3ce14bc5f975_v2_3_7_9').validate(obj)
    return True


def delete_site(api):
    endpoint_result = api.sda.delete_site(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_site(api, validator):
    try:
        assert is_valid_delete_site(
            validator,
            delete_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_site_default_val(api):
    endpoint_result = api.sda.delete_site(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_site_default_val(api, validator):
    try:
        assert is_valid_delete_site(
            validator,
            delete_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_site(json_schema_validate, obj):
    json_schema_validate('jsd_9a764c85d8df5c30b9143619d4f9cde9_v2_3_7_9').validate(obj)
    return True


def add_site(api):
    endpoint_result = api.sda.add_site(
        active_validation=True,
        fabricName='string',
        fabricType='string',
        payload=None,
        siteNameHierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_add_site(api, validator):
    try:
        assert is_valid_add_site(
            validator,
            add_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_site_default_val(api):
    endpoint_result = api.sda.add_site(
        active_validation=True,
        fabricName=None,
        fabricType=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_site_default_val(api, validator):
    try:
        assert is_valid_add_site(
            validator,
            add_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_port_assignment_for_access_point(json_schema_validate, obj):
    json_schema_validate('jsd_e4a09bf566f35babad9e27f5eb61a86d_v2_3_7_9').validate(obj)
    return True


def add_port_assignment_for_access_point(api):
    endpoint_result = api.sda.add_port_assignment_for_access_point(
        active_validation=True,
        authenticateTemplateName='string',
        dataIpAddressPoolName='string',
        deviceManagementIpAddress='string',
        interfaceDescription='string',
        interfaceName='string',
        payload=None,
        siteNameHierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_access_point(api, validator):
    try:
        assert is_valid_add_port_assignment_for_access_point(
            validator,
            add_port_assignment_for_access_point(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_port_assignment_for_access_point_default_val(api):
    endpoint_result = api.sda.add_port_assignment_for_access_point(
        active_validation=True,
        authenticateTemplateName=None,
        dataIpAddressPoolName=None,
        deviceManagementIpAddress=None,
        interfaceDescription=None,
        interfaceName=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_access_point_default_val(api, validator):
    try:
        assert is_valid_add_port_assignment_for_access_point(
            validator,
            add_port_assignment_for_access_point_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_assignment_for_access_point(json_schema_validate, obj):
    json_schema_validate('jsd_27bd26b08b64545bae20f60c56891576_v2_3_7_9').validate(obj)
    return True


def delete_port_assignment_for_access_point(api):
    endpoint_result = api.sda.delete_port_assignment_for_access_point(
        device_management_ip_address='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_access_point(api, validator):
    try:
        assert is_valid_delete_port_assignment_for_access_point(
            validator,
            delete_port_assignment_for_access_point(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_port_assignment_for_access_point_default_val(api):
    endpoint_result = api.sda.delete_port_assignment_for_access_point(
        device_management_ip_address=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_access_point_default_val(api, validator):
    try:
        assert is_valid_delete_port_assignment_for_access_point(
            validator,
            delete_port_assignment_for_access_point_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_assignment_for_access_point(json_schema_validate, obj):
    json_schema_validate('jsd_b035b0b3b60b5f2bb7c8c82e7f94b63b_v2_3_7_9').validate(obj)
    return True


def get_port_assignment_for_access_point(api):
    endpoint_result = api.sda.get_port_assignment_for_access_point(
        device_management_ip_address='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_access_point(api, validator):
    try:
        assert is_valid_get_port_assignment_for_access_point(
            validator,
            get_port_assignment_for_access_point(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_port_assignment_for_access_point_default_val(api):
    endpoint_result = api.sda.get_port_assignment_for_access_point(
        device_management_ip_address=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_access_point_default_val(api, validator):
    try:
        assert is_valid_get_port_assignment_for_access_point(
            validator,
            get_port_assignment_for_access_point_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_assignment_for_user_device(json_schema_validate, obj):
    json_schema_validate('jsd_072cb88b50dd5ead96ecfb4ab0390f47_v2_3_7_9').validate(obj)
    return True


def delete_port_assignment_for_user_device(api):
    endpoint_result = api.sda.delete_port_assignment_for_user_device(
        device_management_ip_address='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_user_device(api, validator):
    try:
        assert is_valid_delete_port_assignment_for_user_device(
            validator,
            delete_port_assignment_for_user_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_port_assignment_for_user_device_default_val(api):
    endpoint_result = api.sda.delete_port_assignment_for_user_device(
        device_management_ip_address=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_user_device_default_val(api, validator):
    try:
        assert is_valid_delete_port_assignment_for_user_device(
            validator,
            delete_port_assignment_for_user_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_port_assignment_for_user_device(json_schema_validate, obj):
    json_schema_validate('jsd_3af29516f0c8591da2a92523b5ab3386_v2_3_7_9').validate(obj)
    return True


def add_port_assignment_for_user_device(api):
    endpoint_result = api.sda.add_port_assignment_for_user_device(
        active_validation=True,
        authenticateTemplateName='string',
        dataIpAddressPoolName='string',
        deviceManagementIpAddress='string',
        interfaceDescription='string',
        interfaceName='string',
        interfaceNames=['string'],
        payload=None,
        scalableGroupName='string',
        siteNameHierarchy='string',
        voiceIpAddressPoolName='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_user_device(api, validator):
    try:
        assert is_valid_add_port_assignment_for_user_device(
            validator,
            add_port_assignment_for_user_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_port_assignment_for_user_device_default_val(api):
    endpoint_result = api.sda.add_port_assignment_for_user_device(
        active_validation=True,
        authenticateTemplateName=None,
        dataIpAddressPoolName=None,
        deviceManagementIpAddress=None,
        interfaceDescription=None,
        interfaceName=None,
        interfaceNames=None,
        payload=None,
        scalableGroupName=None,
        siteNameHierarchy=None,
        voiceIpAddressPoolName=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_user_device_default_val(api, validator):
    try:
        assert is_valid_add_port_assignment_for_user_device(
            validator,
            add_port_assignment_for_user_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_assignment_for_user_device(json_schema_validate, obj):
    json_schema_validate('jsd_a446d7327733580e9a6b661715eb4c09_v2_3_7_9').validate(obj)
    return True


def get_port_assignment_for_user_device(api):
    endpoint_result = api.sda.get_port_assignment_for_user_device(
        device_management_ip_address='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_user_device(api, validator):
    try:
        assert is_valid_get_port_assignment_for_user_device(
            validator,
            get_port_assignment_for_user_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_port_assignment_for_user_device_default_val(api):
    endpoint_result = api.sda.get_port_assignment_for_user_device(
        device_management_ip_address=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_user_device_default_val(api, validator):
    try:
        assert is_valid_get_port_assignment_for_user_device(
            validator,
            get_port_assignment_for_user_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_multicast_in_sda_fabric_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b7079a38844e56dd8f1b6b876880a02e_v2_3_7_9').validate(obj)
    return True


def add_multicast_in_sda_fabric_v1(api):
    endpoint_result = api.sda.add_multicast_in_sda_fabric_v1(
        active_validation=True,
        multicastMethod='string',
        multicastType='string',
        multicastVnInfo=[{'virtualNetworkName': 'string', 'ipPoolName': 'string', 'internalRpIpAddress': ['string'], 'externalRpIpAddress': 'string', 'ssmInfo': [{'ssmGroupRange': 'string', 'ssmWildcardMask': 'string'}]}],
        payload=None,
        siteNameHierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_add_multicast_in_sda_fabric_v1(api, validator):
    try:
        assert is_valid_add_multicast_in_sda_fabric_v1(
            validator,
            add_multicast_in_sda_fabric_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_multicast_in_sda_fabric_v1_default_val(api):
    endpoint_result = api.sda.add_multicast_in_sda_fabric_v1(
        active_validation=True,
        multicastMethod=None,
        multicastType=None,
        multicastVnInfo=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_multicast_in_sda_fabric_v1_default_val(api, validator):
    try:
        assert is_valid_add_multicast_in_sda_fabric_v1(
            validator,
            add_multicast_in_sda_fabric_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_multicast_details_from_sda_fabric_v1(json_schema_validate, obj):
    json_schema_validate('jsd_55c27bbb42365955bc210924e1362c34_v2_3_7_9').validate(obj)
    return True


def get_multicast_details_from_sda_fabric_v1(api):
    endpoint_result = api.sda.get_multicast_details_from_sda_fabric_v1(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_multicast_details_from_sda_fabric_v1(api, validator):
    try:
        assert is_valid_get_multicast_details_from_sda_fabric_v1(
            validator,
            get_multicast_details_from_sda_fabric_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_multicast_details_from_sda_fabric_v1_default_val(api):
    endpoint_result = api.sda.get_multicast_details_from_sda_fabric_v1(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_multicast_details_from_sda_fabric_v1_default_val(api, validator):
    try:
        assert is_valid_get_multicast_details_from_sda_fabric_v1(
            validator,
            get_multicast_details_from_sda_fabric_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_multicast_from_sda_fabric_v1(json_schema_validate, obj):
    json_schema_validate('jsd_45e8e007d3e25f7fb83a6579016aea72_v2_3_7_9').validate(obj)
    return True


def delete_multicast_from_sda_fabric_v1(api):
    endpoint_result = api.sda.delete_multicast_from_sda_fabric_v1(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_multicast_from_sda_fabric_v1(api, validator):
    try:
        assert is_valid_delete_multicast_from_sda_fabric_v1(
            validator,
            delete_multicast_from_sda_fabric_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_multicast_from_sda_fabric_v1_default_val(api):
    endpoint_result = api.sda.delete_multicast_from_sda_fabric_v1(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_multicast_from_sda_fabric_v1_default_val(api, validator):
    try:
        assert is_valid_delete_multicast_from_sda_fabric_v1(
            validator,
            delete_multicast_from_sda_fabric_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_provisioned_wired_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e5bd8dbbf65253f0aadd77a62b1b8b58_v2_3_7_9').validate(obj)
    return True


def delete_provisioned_wired_device_v1(api):
    endpoint_result = api.sda.delete_provisioned_wired_device_v1(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_wired_device_v1(api, validator):
    try:
        assert is_valid_delete_provisioned_wired_device_v1(
            validator,
            delete_provisioned_wired_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_provisioned_wired_device_v1_default_val(api):
    endpoint_result = api.sda.delete_provisioned_wired_device_v1(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_wired_device_v1_default_val(api, validator):
    try:
        assert is_valid_delete_provisioned_wired_device_v1(
            validator,
            delete_provisioned_wired_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_re_provision_wired_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fd488ff002115f3b8f0ee165e5347609_v2_3_7_9').validate(obj)
    return True


def re_provision_wired_device_v1(api):
    endpoint_result = api.sda.re_provision_wired_device_v1(
        active_validation=True,
        deviceManagementIpAddress='string',
        payload=None,
        siteNameHierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_re_provision_wired_device_v1(api, validator):
    try:
        assert is_valid_re_provision_wired_device_v1(
            validator,
            re_provision_wired_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def re_provision_wired_device_v1_default_val(api):
    endpoint_result = api.sda.re_provision_wired_device_v1(
        active_validation=True,
        deviceManagementIpAddress=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_re_provision_wired_device_v1_default_val(api, validator):
    try:
        assert is_valid_re_provision_wired_device_v1(
            validator,
            re_provision_wired_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_provision_wired_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7750d1608b2751c883a072ee3fb80228_v2_3_7_9').validate(obj)
    return True


def provision_wired_device_v1(api):
    endpoint_result = api.sda.provision_wired_device_v1(
        active_validation=True,
        deviceManagementIpAddress='string',
        payload=None,
        siteNameHierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_provision_wired_device_v1(api, validator):
    try:
        assert is_valid_provision_wired_device_v1(
            validator,
            provision_wired_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def provision_wired_device_v1_default_val(api):
    endpoint_result = api.sda.provision_wired_device_v1(
        active_validation=True,
        deviceManagementIpAddress=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_provision_wired_device_v1_default_val(api, validator):
    try:
        assert is_valid_provision_wired_device_v1(
            validator,
            provision_wired_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_provisioned_wired_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d8f10868c21856eab31776f109aba2bb_v2_3_7_9').validate(obj)
    return True


def get_provisioned_wired_device_v1(api):
    endpoint_result = api.sda.get_provisioned_wired_device_v1(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_wired_device_v1(api, validator):
    try:
        assert is_valid_get_provisioned_wired_device_v1(
            validator,
            get_provisioned_wired_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_provisioned_wired_device_v1_default_val(api):
    endpoint_result = api.sda.get_provisioned_wired_device_v1(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_wired_device_v1_default_val(api, validator):
    try:
        assert is_valid_get_provisioned_wired_device_v1(
            validator,
            get_provisioned_wired_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_transit_peer_network_v1(json_schema_validate, obj):
    json_schema_validate('jsd_770a34aab91750028f4d584d36811844_v2_3_7_9').validate(obj)
    return True


def delete_transit_peer_network_v1(api):
    endpoint_result = api.sda.delete_transit_peer_network_v1(
        transit_peer_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_transit_peer_network_v1(api, validator):
    try:
        assert is_valid_delete_transit_peer_network_v1(
            validator,
            delete_transit_peer_network_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_transit_peer_network_v1_default_val(api):
    endpoint_result = api.sda.delete_transit_peer_network_v1(
        transit_peer_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_transit_peer_network_v1_default_val(api, validator):
    try:
        assert is_valid_delete_transit_peer_network_v1(
            validator,
            delete_transit_peer_network_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_transit_peer_network_info_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6d39e10793a45d3db229d6d3820c665a_v2_3_7_9').validate(obj)
    return True


def get_transit_peer_network_info_v1(api):
    endpoint_result = api.sda.get_transit_peer_network_info_v1(
        transit_peer_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_transit_peer_network_info_v1(api, validator):
    try:
        assert is_valid_get_transit_peer_network_info_v1(
            validator,
            get_transit_peer_network_info_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_transit_peer_network_info_v1_default_val(api):
    endpoint_result = api.sda.get_transit_peer_network_info_v1(
        transit_peer_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_transit_peer_network_info_v1_default_val(api, validator):
    try:
        assert is_valid_get_transit_peer_network_info_v1(
            validator,
            get_transit_peer_network_info_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_transit_peer_network_v1(json_schema_validate, obj):
    json_schema_validate('jsd_096d7073129453698264e7519d82991c_v2_3_7_9').validate(obj)
    return True


def add_transit_peer_network_v1(api):
    endpoint_result = api.sda.add_transit_peer_network_v1(
        active_validation=True,
        ipTransitSettings={'routingProtocolName': 'string', 'autonomousSystemNumber': 'string'},
        payload=None,
        sdaTransitSettings={'transitControlPlaneSettings': [{'siteNameHierarchy': 'string', 'deviceManagementIpAddress': 'string'}]},
        transitPeerNetworkName='string',
        transitPeerNetworkType='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_add_transit_peer_network_v1(api, validator):
    try:
        assert is_valid_add_transit_peer_network_v1(
            validator,
            add_transit_peer_network_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_transit_peer_network_v1_default_val(api):
    endpoint_result = api.sda.add_transit_peer_network_v1(
        active_validation=True,
        ipTransitSettings=None,
        payload=None,
        sdaTransitSettings=None,
        transitPeerNetworkName=None,
        transitPeerNetworkType=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_transit_peer_network_v1_default_val(api, validator):
    try:
        assert is_valid_add_transit_peer_network_v1(
            validator,
            add_transit_peer_network_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_vn(json_schema_validate, obj):
    json_schema_validate('jsd_176cb9f8ad5359b2b2cbc151ac3a842a_v2_3_7_9').validate(obj)
    return True


def delete_vn(api):
    endpoint_result = api.sda.delete_vn(
        site_name_hierarchy='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_vn(api, validator):
    try:
        assert is_valid_delete_vn(
            validator,
            delete_vn(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_vn_default_val(api):
    endpoint_result = api.sda.delete_vn(
        site_name_hierarchy=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_vn_default_val(api, validator):
    try:
        assert is_valid_delete_vn(
            validator,
            delete_vn_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_vn(json_schema_validate, obj):
    json_schema_validate('jsd_cb1fe08692b85767a42b84340c4c7d53_v2_3_7_9').validate(obj)
    return True


def get_vn(api):
    endpoint_result = api.sda.get_vn(
        site_name_hierarchy='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_vn(api, validator):
    try:
        assert is_valid_get_vn(
            validator,
            get_vn(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_vn_default_val(api):
    endpoint_result = api.sda.get_vn(
        site_name_hierarchy=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_vn_default_val(api, validator):
    try:
        assert is_valid_get_vn(
            validator,
            get_vn_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_vn(json_schema_validate, obj):
    json_schema_validate('jsd_15e3a724a35854758d65a83823c88435_v2_3_7_9').validate(obj)
    return True


def add_vn(api):
    endpoint_result = api.sda.add_vn(
        active_validation=True,
        payload=None,
        siteNameHierarchy='string',
        virtualNetworkName='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_add_vn(api, validator):
    try:
        assert is_valid_add_vn(
            validator,
            add_vn(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_vn_default_val(api):
    endpoint_result = api.sda.add_vn(
        active_validation=True,
        payload=None,
        siteNameHierarchy=None,
        virtualNetworkName=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_vn_default_val(api, validator):
    try:
        assert is_valid_add_vn(
            validator,
            add_vn_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_virtual_network_summary_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ccf5ce99e049525f8184fcaa5991d919_v2_3_7_9').validate(obj)
    return True


def get_virtual_network_summary_v1(api):
    endpoint_result = api.sda.get_virtual_network_summary_v1(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_virtual_network_summary_v1(api, validator):
    try:
        assert is_valid_get_virtual_network_summary_v1(
            validator,
            get_virtual_network_summary_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_virtual_network_summary_v1_default_val(api):
    endpoint_result = api.sda.get_virtual_network_summary_v1(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_virtual_network_summary_v1_default_val(api, validator):
    try:
        assert is_valid_get_virtual_network_summary_v1(
            validator,
            get_virtual_network_summary_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ip_pool_from_sda_virtual_network_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b88723912610599ba42292db52d1dae4_v2_3_7_9').validate(obj)
    return True


def get_ip_pool_from_sda_virtual_network_v1(api):
    endpoint_result = api.sda.get_ip_pool_from_sda_virtual_network_v1(
        ip_pool_name='string',
        site_name_hierarchy='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_ip_pool_from_sda_virtual_network_v1(api, validator):
    try:
        assert is_valid_get_ip_pool_from_sda_virtual_network_v1(
            validator,
            get_ip_pool_from_sda_virtual_network_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ip_pool_from_sda_virtual_network_v1_default_val(api):
    endpoint_result = api.sda.get_ip_pool_from_sda_virtual_network_v1(
        ip_pool_name=None,
        site_name_hierarchy=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_ip_pool_from_sda_virtual_network_v1_default_val(api, validator):
    try:
        assert is_valid_get_ip_pool_from_sda_virtual_network_v1(
            validator,
            get_ip_pool_from_sda_virtual_network_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_ip_pool_from_sda_virtual_network_v1(json_schema_validate, obj):
    json_schema_validate('jsd_951c923d016d5401b7a9943724df3844_v2_3_7_9').validate(obj)
    return True


def delete_ip_pool_from_sda_virtual_network_v1(api):
    endpoint_result = api.sda.delete_ip_pool_from_sda_virtual_network_v1(
        ip_pool_name='string',
        site_name_hierarchy='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_ip_pool_from_sda_virtual_network_v1(api, validator):
    try:
        assert is_valid_delete_ip_pool_from_sda_virtual_network_v1(
            validator,
            delete_ip_pool_from_sda_virtual_network_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_ip_pool_from_sda_virtual_network_v1_default_val(api):
    endpoint_result = api.sda.delete_ip_pool_from_sda_virtual_network_v1(
        ip_pool_name=None,
        site_name_hierarchy=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_ip_pool_from_sda_virtual_network_v1_default_val(api, validator):
    try:
        assert is_valid_delete_ip_pool_from_sda_virtual_network_v1(
            validator,
            delete_ip_pool_from_sda_virtual_network_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_ip_pool_in_sda_virtual_network_v1(json_schema_validate, obj):
    json_schema_validate('jsd_62b07f187b7456c8bbb6088a2f24dcee_v2_3_7_9').validate(obj)
    return True


def add_ip_pool_in_sda_virtual_network_v1(api):
    endpoint_result = api.sda.add_ip_pool_in_sda_virtual_network_v1(
        active_validation=True,
        autoGenerateVlanName=True,
        ipPoolName='string',
        isBridgeModeVm=True,
        isCommonPool=True,
        isIpDirectedBroadcast=True,
        isL2FloodingEnabled=True,
        isLayer2Only=True,
        isThisCriticalPool=True,
        isWirelessPool=True,
        payload=None,
        poolType='string',
        scalableGroupName='string',
        siteNameHierarchy='string',
        trafficType='string',
        virtualNetworkName='string',
        vlanId='string',
        vlanName='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_add_ip_pool_in_sda_virtual_network_v1(api, validator):
    try:
        assert is_valid_add_ip_pool_in_sda_virtual_network_v1(
            validator,
            add_ip_pool_in_sda_virtual_network_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_ip_pool_in_sda_virtual_network_v1_default_val(api):
    endpoint_result = api.sda.add_ip_pool_in_sda_virtual_network_v1(
        active_validation=True,
        autoGenerateVlanName=None,
        ipPoolName=None,
        isBridgeModeVm=None,
        isCommonPool=None,
        isIpDirectedBroadcast=None,
        isL2FloodingEnabled=None,
        isLayer2Only=None,
        isThisCriticalPool=None,
        isWirelessPool=None,
        payload=None,
        poolType=None,
        scalableGroupName=None,
        siteNameHierarchy=None,
        trafficType=None,
        virtualNetworkName=None,
        vlanId=None,
        vlanName=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_ip_pool_in_sda_virtual_network_v1_default_val(api, validator):
    try:
        assert is_valid_add_ip_pool_in_sda_virtual_network_v1(
            validator,
            add_ip_pool_in_sda_virtual_network_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_anycast_gateways_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6f486694f3da57b4921b7f2036a1b754_v2_3_7_9').validate(obj)
    return True


def update_anycast_gateways_v1(api):
    endpoint_result = api.sda.update_anycast_gateways_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_anycast_gateways_v1(api, validator):
    try:
        assert is_valid_update_anycast_gateways_v1(
            validator,
            update_anycast_gateways_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_anycast_gateways_v1_default_val(api):
    endpoint_result = api.sda.update_anycast_gateways_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_anycast_gateways_v1_default_val(api, validator):
    try:
        assert is_valid_update_anycast_gateways_v1(
            validator,
            update_anycast_gateways_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_anycast_gateways_v1(json_schema_validate, obj):
    json_schema_validate('jsd_05ee8590b6b45048b84e814161272bee_v2_3_7_9').validate(obj)
    return True


def add_anycast_gateways_v1(api):
    endpoint_result = api.sda.add_anycast_gateways_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_anycast_gateways_v1(api, validator):
    try:
        assert is_valid_add_anycast_gateways_v1(
            validator,
            add_anycast_gateways_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_anycast_gateways_v1_default_val(api):
    endpoint_result = api.sda.add_anycast_gateways_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_anycast_gateways_v1_default_val(api, validator):
    try:
        assert is_valid_add_anycast_gateways_v1(
            validator,
            add_anycast_gateways_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_anycast_gateways_v1(json_schema_validate, obj):
    json_schema_validate('jsd_067c634a503551e885c053fd1ed9d3fd_v2_3_7_9').validate(obj)
    return True


def get_anycast_gateways_v1(api):
    endpoint_result = api.sda.get_anycast_gateways_v1(
        fabric_id='string',
        id='string',
        ip_pool_name='string',
        limit=0,
        offset=0,
        virtual_network_name='string',
        vlan_id=0,
        vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_anycast_gateways_v1(api, validator):
    try:
        assert is_valid_get_anycast_gateways_v1(
            validator,
            get_anycast_gateways_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_anycast_gateways_v1_default_val(api):
    endpoint_result = api.sda.get_anycast_gateways_v1(
        fabric_id=None,
        id=None,
        ip_pool_name=None,
        limit=None,
        offset=None,
        virtual_network_name=None,
        vlan_id=None,
        vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_anycast_gateways_v1_default_val(api, validator):
    try:
        assert is_valid_get_anycast_gateways_v1(
            validator,
            get_anycast_gateways_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_anycast_gateway_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_51126a280b785a3ca53c349c68ca9070_v2_3_7_9').validate(obj)
    return True


def get_anycast_gateway_count_v1(api):
    endpoint_result = api.sda.get_anycast_gateway_count_v1(
        fabric_id='string',
        ip_pool_name='string',
        virtual_network_name='string',
        vlan_id=0,
        vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_anycast_gateway_count_v1(api, validator):
    try:
        assert is_valid_get_anycast_gateway_count_v1(
            validator,
            get_anycast_gateway_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_anycast_gateway_count_v1_default_val(api):
    endpoint_result = api.sda.get_anycast_gateway_count_v1(
        fabric_id=None,
        ip_pool_name=None,
        virtual_network_name=None,
        vlan_id=None,
        vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_anycast_gateway_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_anycast_gateway_count_v1(
            validator,
            get_anycast_gateway_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_anycast_gateway_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_98e66d9fbfe55cf5882bf219b0fffa13_v2_3_7_9').validate(obj)
    return True


def delete_anycast_gateway_by_id_v1(api):
    endpoint_result = api.sda.delete_anycast_gateway_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_anycast_gateway_by_id_v1(api, validator):
    try:
        assert is_valid_delete_anycast_gateway_by_id_v1(
            validator,
            delete_anycast_gateway_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_anycast_gateway_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_anycast_gateway_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_anycast_gateway_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_anycast_gateway_by_id_v1(
            validator,
            delete_anycast_gateway_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_authentication_profiles_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3827e6713a34508993b3e9f6837dd690_v2_3_7_9').validate(obj)
    return True


def get_authentication_profiles_v1(api):
    endpoint_result = api.sda.get_authentication_profiles_v1(
        authentication_profile_name='string',
        fabric_id='string',
        is_global_authentication_profile=True,
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_authentication_profiles_v1(api, validator):
    try:
        assert is_valid_get_authentication_profiles_v1(
            validator,
            get_authentication_profiles_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_authentication_profiles_v1_default_val(api):
    endpoint_result = api.sda.get_authentication_profiles_v1(
        authentication_profile_name=None,
        fabric_id=None,
        is_global_authentication_profile=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_authentication_profiles_v1_default_val(api, validator):
    try:
        assert is_valid_get_authentication_profiles_v1(
            validator,
            get_authentication_profiles_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_authentication_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8948077ea8d75a9d8d9e6882da4a4a91_v2_3_7_9').validate(obj)
    return True


def update_authentication_profile_v1(api):
    endpoint_result = api.sda.update_authentication_profile_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_authentication_profile_v1(api, validator):
    try:
        assert is_valid_update_authentication_profile_v1(
            validator,
            update_authentication_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_authentication_profile_v1_default_val(api):
    endpoint_result = api.sda.update_authentication_profile_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_authentication_profile_v1_default_val(api, validator):
    try:
        assert is_valid_update_authentication_profile_v1(
            validator,
            update_authentication_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_extranet_policies_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8e5f7c332c255f34b7b6e2bd6ac13800_v2_3_7_9').validate(obj)
    return True


def delete_extranet_policies_v1(api):
    endpoint_result = api.sda.delete_extranet_policies_v1(
        extranet_policy_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_extranet_policies_v1(api, validator):
    try:
        assert is_valid_delete_extranet_policies_v1(
            validator,
            delete_extranet_policies_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_extranet_policies_v1_default_val(api):
    endpoint_result = api.sda.delete_extranet_policies_v1(
        extranet_policy_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_extranet_policies_v1_default_val(api, validator):
    try:
        assert is_valid_delete_extranet_policies_v1(
            validator,
            delete_extranet_policies_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_extranet_policy_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6ccd75f80ece59f08cadda085402cef5_v2_3_7_9').validate(obj)
    return True


def update_extranet_policy_v1(api):
    endpoint_result = api.sda.update_extranet_policy_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_extranet_policy_v1(api, validator):
    try:
        assert is_valid_update_extranet_policy_v1(
            validator,
            update_extranet_policy_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_extranet_policy_v1_default_val(api):
    endpoint_result = api.sda.update_extranet_policy_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_extranet_policy_v1_default_val(api, validator):
    try:
        assert is_valid_update_extranet_policy_v1(
            validator,
            update_extranet_policy_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_extranet_policy_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a0c237c8fc115b6f98b87cc7a1360dd0_v2_3_7_9').validate(obj)
    return True


def add_extranet_policy_v1(api):
    endpoint_result = api.sda.add_extranet_policy_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_extranet_policy_v1(api, validator):
    try:
        assert is_valid_add_extranet_policy_v1(
            validator,
            add_extranet_policy_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_extranet_policy_v1_default_val(api):
    endpoint_result = api.sda.add_extranet_policy_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_extranet_policy_v1_default_val(api, validator):
    try:
        assert is_valid_add_extranet_policy_v1(
            validator,
            add_extranet_policy_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_extranet_policies_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c88d4f7170b9553abf9af4d011a25f0f_v2_3_7_9').validate(obj)
    return True


def get_extranet_policies_v1(api):
    endpoint_result = api.sda.get_extranet_policies_v1(
        extranet_policy_name='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_extranet_policies_v1(api, validator):
    try:
        assert is_valid_get_extranet_policies_v1(
            validator,
            get_extranet_policies_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_extranet_policies_v1_default_val(api):
    endpoint_result = api.sda.get_extranet_policies_v1(
        extranet_policy_name=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_extranet_policies_v1_default_val(api, validator):
    try:
        assert is_valid_get_extranet_policies_v1(
            validator,
            get_extranet_policies_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_extranet_policy_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_dd8262eb13145dc292e7aee84e56e065_v2_3_7_9').validate(obj)
    return True


def get_extranet_policy_count_v1(api):
    endpoint_result = api.sda.get_extranet_policy_count_v1(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_extranet_policy_count_v1(api, validator):
    try:
        assert is_valid_get_extranet_policy_count_v1(
            validator,
            get_extranet_policy_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_extranet_policy_count_v1_default_val(api):
    endpoint_result = api.sda.get_extranet_policy_count_v1(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_extranet_policy_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_extranet_policy_count_v1(
            validator,
            get_extranet_policy_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_extranet_policy_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_22aeee667e2d567cbbff106e1888bbbe_v2_3_7_9').validate(obj)
    return True


def delete_extranet_policy_by_id_v1(api):
    endpoint_result = api.sda.delete_extranet_policy_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_extranet_policy_by_id_v1(api, validator):
    try:
        assert is_valid_delete_extranet_policy_by_id_v1(
            validator,
            delete_extranet_policy_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_extranet_policy_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_extranet_policy_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_extranet_policy_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_extranet_policy_by_id_v1(
            validator,
            delete_extranet_policy_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d5486968c9ff5b23ae1fdd15ad6da1ef_v2_3_7_9').validate(obj)
    return True


def get_fabric_devices_v1(api):
    endpoint_result = api.sda.get_fabric_devices_v1(
        device_roles='string',
        fabric_id='string',
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_v1(api, validator):
    try:
        assert is_valid_get_fabric_devices_v1(
            validator,
            get_fabric_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_v1_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_v1(
        device_roles=None,
        fabric_id=None,
        limit=None,
        network_device_id=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_v1_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_v1(
            validator,
            get_fabric_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_fabric_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_28a924f763a15125a8d5beaa6dd6fa2c_v2_3_7_9').validate(obj)
    return True


def update_fabric_devices_v1(api):
    endpoint_result = api.sda.update_fabric_devices_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_devices_v1(api, validator):
    try:
        assert is_valid_update_fabric_devices_v1(
            validator,
            update_fabric_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_fabric_devices_v1_default_val(api):
    endpoint_result = api.sda.update_fabric_devices_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_devices_v1_default_val(api, validator):
    try:
        assert is_valid_update_fabric_devices_v1(
            validator,
            update_fabric_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8010c5d22b295a4c8e4a1dfdb4645f92_v2_3_7_9').validate(obj)
    return True


def delete_fabric_devices_v1(api):
    endpoint_result = api.sda.delete_fabric_devices_v1(
        device_roles='string',
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_devices_v1(api, validator):
    try:
        assert is_valid_delete_fabric_devices_v1(
            validator,
            delete_fabric_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_devices_v1_default_val(api):
    endpoint_result = api.sda.delete_fabric_devices_v1(
        device_roles=None,
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_devices_v1_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_devices_v1(
            validator,
            delete_fabric_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_30d77719c37558f694e5545a21406275_v2_3_7_9').validate(obj)
    return True


def add_fabric_devices_v1(api):
    endpoint_result = api.sda.add_fabric_devices_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_v1(api, validator):
    try:
        assert is_valid_add_fabric_devices_v1(
            validator,
            add_fabric_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_devices_v1_default_val(api):
    endpoint_result = api.sda.add_fabric_devices_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_v1_default_val(api, validator):
    try:
        assert is_valid_add_fabric_devices_v1(
            validator,
            add_fabric_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2f081250cdc75361afea8d1624123bb4_v2_3_7_9').validate(obj)
    return True


def get_fabric_devices_count_v1(api):
    endpoint_result = api.sda.get_fabric_devices_count_v1(
        device_roles='string',
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_count_v1(api, validator):
    try:
        assert is_valid_get_fabric_devices_count_v1(
            validator,
            get_fabric_devices_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_count_v1_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_count_v1(
        device_roles=None,
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_count_v1(
            validator,
            get_fabric_devices_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_device_layer2_handoffs_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b6484275a25c54488d300c11c5ddd481_v2_3_7_9').validate(obj)
    return True


def delete_fabric_device_layer2_handoffs_v1(api):
    endpoint_result = api.sda.delete_fabric_device_layer2_handoffs_v1(
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer2_handoffs_v1(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer2_handoffs_v1(
            validator,
            delete_fabric_device_layer2_handoffs_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_device_layer2_handoffs_v1_default_val(api):
    endpoint_result = api.sda.delete_fabric_device_layer2_handoffs_v1(
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer2_handoffs_v1_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer2_handoffs_v1(
            validator,
            delete_fabric_device_layer2_handoffs_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_layer2_handoffs_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ec047337e36b59db977e1dae8dd724ef_v2_3_7_9').validate(obj)
    return True


def get_fabric_devices_layer2_handoffs_v1(api):
    endpoint_result = api.sda.get_fabric_devices_layer2_handoffs_v1(
        fabric_id='string',
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer2_handoffs_v1(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer2_handoffs_v1(
            validator,
            get_fabric_devices_layer2_handoffs_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_layer2_handoffs_v1_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_layer2_handoffs_v1(
        fabric_id=None,
        limit=None,
        network_device_id=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer2_handoffs_v1_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer2_handoffs_v1(
            validator,
            get_fabric_devices_layer2_handoffs_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric_devices_layer2_handoffs_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0e86b65311b05d29ba5eea0d5f1fd88f_v2_3_7_9').validate(obj)
    return True


def add_fabric_devices_layer2_handoffs_v1(api):
    endpoint_result = api.sda.add_fabric_devices_layer2_handoffs_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_layer2_handoffs_v1(api, validator):
    try:
        assert is_valid_add_fabric_devices_layer2_handoffs_v1(
            validator,
            add_fabric_devices_layer2_handoffs_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_devices_layer2_handoffs_v1_default_val(api):
    endpoint_result = api.sda.add_fabric_devices_layer2_handoffs_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_layer2_handoffs_v1_default_val(api, validator):
    try:
        assert is_valid_add_fabric_devices_layer2_handoffs_v1(
            validator,
            add_fabric_devices_layer2_handoffs_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_layer2_handoffs_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_35c6da6b1da95bb691d2e39cee84dbb2_v2_3_7_9').validate(obj)
    return True


def get_fabric_devices_layer2_handoffs_count_v1(api):
    endpoint_result = api.sda.get_fabric_devices_layer2_handoffs_count_v1(
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer2_handoffs_count_v1(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer2_handoffs_count_v1(
            validator,
            get_fabric_devices_layer2_handoffs_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_layer2_handoffs_count_v1_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_layer2_handoffs_count_v1(
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer2_handoffs_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer2_handoffs_count_v1(
            validator,
            get_fabric_devices_layer2_handoffs_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_device_layer2_handoff_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_380853b6406a55509e5aeaa71d960f98_v2_3_7_9').validate(obj)
    return True


def delete_fabric_device_layer2_handoff_by_id_v1(api):
    endpoint_result = api.sda.delete_fabric_device_layer2_handoff_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer2_handoff_by_id_v1(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer2_handoff_by_id_v1(
            validator,
            delete_fabric_device_layer2_handoff_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_device_layer2_handoff_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_fabric_device_layer2_handoff_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer2_handoff_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer2_handoff_by_id_v1(
            validator,
            delete_fabric_device_layer2_handoff_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric_devices_layer3_handoffs_with_ip_transit_v1(json_schema_validate, obj):
    json_schema_validate('jsd_69625c45c1c55d498d03a72933690098_v2_3_7_9').validate(obj)
    return True


def add_fabric_devices_layer3_handoffs_with_ip_transit_v1(api):
    endpoint_result = api.sda.add_fabric_devices_layer3_handoffs_with_ip_transit_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_layer3_handoffs_with_ip_transit_v1(api, validator):
    try:
        assert is_valid_add_fabric_devices_layer3_handoffs_with_ip_transit_v1(
            validator,
            add_fabric_devices_layer3_handoffs_with_ip_transit_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_devices_layer3_handoffs_with_ip_transit_v1_default_val(api):
    endpoint_result = api.sda.add_fabric_devices_layer3_handoffs_with_ip_transit_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_layer3_handoffs_with_ip_transit_v1_default_val(api, validator):
    try:
        assert is_valid_add_fabric_devices_layer3_handoffs_with_ip_transit_v1(
            validator,
            add_fabric_devices_layer3_handoffs_with_ip_transit_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_fabric_devices_layer3_handoffs_with_ip_transit_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f0942fbb79f855e889d60777f41ea944_v2_3_7_9').validate(obj)
    return True


def update_fabric_devices_layer3_handoffs_with_ip_transit_v1(api):
    endpoint_result = api.sda.update_fabric_devices_layer3_handoffs_with_ip_transit_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_devices_layer3_handoffs_with_ip_transit_v1(api, validator):
    try:
        assert is_valid_update_fabric_devices_layer3_handoffs_with_ip_transit_v1(
            validator,
            update_fabric_devices_layer3_handoffs_with_ip_transit_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_fabric_devices_layer3_handoffs_with_ip_transit_v1_default_val(api):
    endpoint_result = api.sda.update_fabric_devices_layer3_handoffs_with_ip_transit_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_devices_layer3_handoffs_with_ip_transit_v1_default_val(api, validator):
    try:
        assert is_valid_update_fabric_devices_layer3_handoffs_with_ip_transit_v1(
            validator,
            update_fabric_devices_layer3_handoffs_with_ip_transit_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_device_layer3_handoffs_with_ip_transit_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fdab9b7917a1567980b0071e058921fe_v2_3_7_9').validate(obj)
    return True


def delete_fabric_device_layer3_handoffs_with_ip_transit_v1(api):
    endpoint_result = api.sda.delete_fabric_device_layer3_handoffs_with_ip_transit_v1(
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer3_handoffs_with_ip_transit_v1(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer3_handoffs_with_ip_transit_v1(
            validator,
            delete_fabric_device_layer3_handoffs_with_ip_transit_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_device_layer3_handoffs_with_ip_transit_v1_default_val(api):
    endpoint_result = api.sda.delete_fabric_device_layer3_handoffs_with_ip_transit_v1(
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer3_handoffs_with_ip_transit_v1_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer3_handoffs_with_ip_transit_v1(
            validator,
            delete_fabric_device_layer3_handoffs_with_ip_transit_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_layer3_handoffs_with_ip_transit_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ee0d11a1e0dd573da2d6fb96d92c4bb8_v2_3_7_9').validate(obj)
    return True


def get_fabric_devices_layer3_handoffs_with_ip_transit_v1(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_ip_transit_v1(
        fabric_id='string',
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_ip_transit_v1(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_ip_transit_v1(
            validator,
            get_fabric_devices_layer3_handoffs_with_ip_transit_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_layer3_handoffs_with_ip_transit_v1_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_ip_transit_v1(
        fabric_id=None,
        limit=None,
        network_device_id=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_ip_transit_v1_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_ip_transit_v1(
            validator,
            get_fabric_devices_layer3_handoffs_with_ip_transit_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_layer3_handoffs_with_ip_transit_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_878592a4fa61561aa0fe56939c3f24d4_v2_3_7_9').validate(obj)
    return True


def get_fabric_devices_layer3_handoffs_with_ip_transit_count_v1(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_ip_transit_count_v1(
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_ip_transit_count_v1(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_ip_transit_count_v1(
            validator,
            get_fabric_devices_layer3_handoffs_with_ip_transit_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_layer3_handoffs_with_ip_transit_count_v1_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_ip_transit_count_v1(
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_ip_transit_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_ip_transit_count_v1(
            validator,
            get_fabric_devices_layer3_handoffs_with_ip_transit_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_device_layer3_handoff_with_ip_transit_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3fafe4d2d2fe510db8f0906e5f583559_v2_3_7_9').validate(obj)
    return True


def delete_fabric_device_layer3_handoff_with_ip_transit_by_id_v1(api):
    endpoint_result = api.sda.delete_fabric_device_layer3_handoff_with_ip_transit_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer3_handoff_with_ip_transit_by_id_v1(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer3_handoff_with_ip_transit_by_id_v1(
            validator,
            delete_fabric_device_layer3_handoff_with_ip_transit_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_device_layer3_handoff_with_ip_transit_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_fabric_device_layer3_handoff_with_ip_transit_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer3_handoff_with_ip_transit_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer3_handoff_with_ip_transit_by_id_v1(
            validator,
            delete_fabric_device_layer3_handoff_with_ip_transit_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_fabric_devices_layer3_handoffs_with_sda_transit_v1(json_schema_validate, obj):
    json_schema_validate('jsd_902c90c04b8356cf9974957e0f9516d0_v2_3_7_9').validate(obj)
    return True


def update_fabric_devices_layer3_handoffs_with_sda_transit_v1(api):
    endpoint_result = api.sda.update_fabric_devices_layer3_handoffs_with_sda_transit_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_devices_layer3_handoffs_with_sda_transit_v1(api, validator):
    try:
        assert is_valid_update_fabric_devices_layer3_handoffs_with_sda_transit_v1(
            validator,
            update_fabric_devices_layer3_handoffs_with_sda_transit_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_fabric_devices_layer3_handoffs_with_sda_transit_v1_default_val(api):
    endpoint_result = api.sda.update_fabric_devices_layer3_handoffs_with_sda_transit_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_devices_layer3_handoffs_with_sda_transit_v1_default_val(api, validator):
    try:
        assert is_valid_update_fabric_devices_layer3_handoffs_with_sda_transit_v1(
            validator,
            update_fabric_devices_layer3_handoffs_with_sda_transit_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_layer3_handoffs_with_sda_transit_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d8e5a783df185c88bae2bd8ba6b6bb2d_v2_3_7_9').validate(obj)
    return True


def get_fabric_devices_layer3_handoffs_with_sda_transit_v1(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_sda_transit_v1(
        fabric_id='string',
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_sda_transit_v1(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_sda_transit_v1(
            validator,
            get_fabric_devices_layer3_handoffs_with_sda_transit_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_layer3_handoffs_with_sda_transit_v1_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_sda_transit_v1(
        fabric_id=None,
        limit=None,
        network_device_id=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_sda_transit_v1_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_sda_transit_v1(
            validator,
            get_fabric_devices_layer3_handoffs_with_sda_transit_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_device_layer3_handoffs_with_sda_transit_v1(json_schema_validate, obj):
    json_schema_validate('jsd_62aae870923852f3ac5904f65812c559_v2_3_7_9').validate(obj)
    return True


def delete_fabric_device_layer3_handoffs_with_sda_transit_v1(api):
    endpoint_result = api.sda.delete_fabric_device_layer3_handoffs_with_sda_transit_v1(
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer3_handoffs_with_sda_transit_v1(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer3_handoffs_with_sda_transit_v1(
            validator,
            delete_fabric_device_layer3_handoffs_with_sda_transit_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_device_layer3_handoffs_with_sda_transit_v1_default_val(api):
    endpoint_result = api.sda.delete_fabric_device_layer3_handoffs_with_sda_transit_v1(
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer3_handoffs_with_sda_transit_v1_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer3_handoffs_with_sda_transit_v1(
            validator,
            delete_fabric_device_layer3_handoffs_with_sda_transit_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric_devices_layer3_handoffs_with_sda_transit_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f95014e3b3385f21afa39325f3508427_v2_3_7_9').validate(obj)
    return True


def add_fabric_devices_layer3_handoffs_with_sda_transit_v1(api):
    endpoint_result = api.sda.add_fabric_devices_layer3_handoffs_with_sda_transit_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_layer3_handoffs_with_sda_transit_v1(api, validator):
    try:
        assert is_valid_add_fabric_devices_layer3_handoffs_with_sda_transit_v1(
            validator,
            add_fabric_devices_layer3_handoffs_with_sda_transit_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_devices_layer3_handoffs_with_sda_transit_v1_default_val(api):
    endpoint_result = api.sda.add_fabric_devices_layer3_handoffs_with_sda_transit_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_layer3_handoffs_with_sda_transit_v1_default_val(api, validator):
    try:
        assert is_valid_add_fabric_devices_layer3_handoffs_with_sda_transit_v1(
            validator,
            add_fabric_devices_layer3_handoffs_with_sda_transit_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_layer3_handoffs_with_sda_transit_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9b183d0cc487506ab776e0d470b0db91_v2_3_7_9').validate(obj)
    return True


def get_fabric_devices_layer3_handoffs_with_sda_transit_count_v1(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_sda_transit_count_v1(
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_sda_transit_count_v1(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_sda_transit_count_v1(
            validator,
            get_fabric_devices_layer3_handoffs_with_sda_transit_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_layer3_handoffs_with_sda_transit_count_v1_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_sda_transit_count_v1(
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_sda_transit_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_sda_transit_count_v1(
            validator,
            get_fabric_devices_layer3_handoffs_with_sda_transit_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_device_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_497d9e0c5eb356eda1fa6f45928cb6f2_v2_3_7_9').validate(obj)
    return True


def delete_fabric_device_by_id_v1(api):
    endpoint_result = api.sda.delete_fabric_device_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_by_id_v1(api, validator):
    try:
        assert is_valid_delete_fabric_device_by_id_v1(
            validator,
            delete_fabric_device_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_device_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_fabric_device_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_device_by_id_v1(
            validator,
            delete_fabric_device_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_sites_v1(json_schema_validate, obj):
    json_schema_validate('jsd_07a7079f75dd5973b2bf50461bdcf2de_v2_3_7_9').validate(obj)
    return True


def get_fabric_sites_v1(api):
    endpoint_result = api.sda.get_fabric_sites_v1(
        id='string',
        limit=0,
        offset=0,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_sites_v1(api, validator):
    try:
        assert is_valid_get_fabric_sites_v1(
            validator,
            get_fabric_sites_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_sites_v1_default_val(api):
    endpoint_result = api.sda.get_fabric_sites_v1(
        id=None,
        limit=None,
        offset=None,
        site_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_sites_v1_default_val(api, validator):
    try:
        assert is_valid_get_fabric_sites_v1(
            validator,
            get_fabric_sites_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7680bfca373c5d7c863eef14abc654fd_v2_3_7_9').validate(obj)
    return True


def add_fabric_site_v1(api):
    endpoint_result = api.sda.add_fabric_site_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_site_v1(api, validator):
    try:
        assert is_valid_add_fabric_site_v1(
            validator,
            add_fabric_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_site_v1_default_val(api):
    endpoint_result = api.sda.add_fabric_site_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_site_v1_default_val(api, validator):
    try:
        assert is_valid_add_fabric_site_v1(
            validator,
            add_fabric_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_fabric_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5198effb55c158f28469762804e84633_v2_3_7_9').validate(obj)
    return True


def update_fabric_site_v1(api):
    endpoint_result = api.sda.update_fabric_site_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_site_v1(api, validator):
    try:
        assert is_valid_update_fabric_site_v1(
            validator,
            update_fabric_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_fabric_site_v1_default_val(api):
    endpoint_result = api.sda.update_fabric_site_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_site_v1_default_val(api, validator):
    try:
        assert is_valid_update_fabric_site_v1(
            validator,
            update_fabric_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_site_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b871b97883085717bfbb14e860ab6654_v2_3_7_9').validate(obj)
    return True


def get_fabric_site_count_v1(api):
    endpoint_result = api.sda.get_fabric_site_count_v1(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_site_count_v1(api, validator):
    try:
        assert is_valid_get_fabric_site_count_v1(
            validator,
            get_fabric_site_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_site_count_v1_default_val(api):
    endpoint_result = api.sda.get_fabric_site_count_v1(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_site_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_fabric_site_count_v1(
            validator,
            get_fabric_site_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_site_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_72c94ba483b75e03a2c23aae02c510ac_v2_3_7_9').validate(obj)
    return True


def delete_fabric_site_by_id_v1(api):
    endpoint_result = api.sda.delete_fabric_site_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_site_by_id_v1(api, validator):
    try:
        assert is_valid_delete_fabric_site_by_id_v1(
            validator,
            delete_fabric_site_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_site_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_fabric_site_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_site_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_site_by_id_v1(
            validator,
            delete_fabric_site_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_zones_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7e722d98d14d5e119ca03fa114edb38f_v2_3_7_9').validate(obj)
    return True


def get_fabric_zones_v1(api):
    endpoint_result = api.sda.get_fabric_zones_v1(
        id='string',
        limit=0,
        offset=0,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_zones_v1(api, validator):
    try:
        assert is_valid_get_fabric_zones_v1(
            validator,
            get_fabric_zones_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_zones_v1_default_val(api):
    endpoint_result = api.sda.get_fabric_zones_v1(
        id=None,
        limit=None,
        offset=None,
        site_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_zones_v1_default_val(api, validator):
    try:
        assert is_valid_get_fabric_zones_v1(
            validator,
            get_fabric_zones_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_fabric_zone_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ada3522de8ef54729e9fc242df292547_v2_3_7_9').validate(obj)
    return True


def update_fabric_zone_v1(api):
    endpoint_result = api.sda.update_fabric_zone_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_zone_v1(api, validator):
    try:
        assert is_valid_update_fabric_zone_v1(
            validator,
            update_fabric_zone_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_fabric_zone_v1_default_val(api):
    endpoint_result = api.sda.update_fabric_zone_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_zone_v1_default_val(api, validator):
    try:
        assert is_valid_update_fabric_zone_v1(
            validator,
            update_fabric_zone_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric_zone_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ae4d33eacca95f109bebc6fd0528ca48_v2_3_7_9').validate(obj)
    return True


def add_fabric_zone_v1(api):
    endpoint_result = api.sda.add_fabric_zone_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_zone_v1(api, validator):
    try:
        assert is_valid_add_fabric_zone_v1(
            validator,
            add_fabric_zone_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_zone_v1_default_val(api):
    endpoint_result = api.sda.add_fabric_zone_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_zone_v1_default_val(api, validator):
    try:
        assert is_valid_add_fabric_zone_v1(
            validator,
            add_fabric_zone_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_zone_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b7004918aecc58c7880ae97d344bb885_v2_3_7_9').validate(obj)
    return True


def get_fabric_zone_count_v1(api):
    endpoint_result = api.sda.get_fabric_zone_count_v1(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_zone_count_v1(api, validator):
    try:
        assert is_valid_get_fabric_zone_count_v1(
            validator,
            get_fabric_zone_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_zone_count_v1_default_val(api):
    endpoint_result = api.sda.get_fabric_zone_count_v1(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_zone_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_fabric_zone_count_v1(
            validator,
            get_fabric_zone_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_zone_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_232cdb33e11852af80e1ed8f26e4336d_v2_3_7_9').validate(obj)
    return True


def delete_fabric_zone_by_id_v1(api):
    endpoint_result = api.sda.delete_fabric_zone_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_zone_by_id_v1(api, validator):
    try:
        assert is_valid_delete_fabric_zone_by_id_v1(
            validator,
            delete_fabric_zone_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_zone_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_fabric_zone_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_zone_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_zone_by_id_v1(
            validator,
            delete_fabric_zone_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_layer2_virtual_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3f09c94c65c858e4b7be0b7cb3d25b7a_v2_3_7_9').validate(obj)
    return True


def add_layer2_virtual_networks_v1(api):
    endpoint_result = api.sda.add_layer2_virtual_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_layer2_virtual_networks_v1(api, validator):
    try:
        assert is_valid_add_layer2_virtual_networks_v1(
            validator,
            add_layer2_virtual_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_layer2_virtual_networks_v1_default_val(api):
    endpoint_result = api.sda.add_layer2_virtual_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_layer2_virtual_networks_v1_default_val(api, validator):
    try:
        assert is_valid_add_layer2_virtual_networks_v1(
            validator,
            add_layer2_virtual_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_layer2_virtual_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1fa8caf01309507e9be1544b9d1faa39_v2_3_7_9').validate(obj)
    return True


def delete_layer2_virtual_networks_v1(api):
    endpoint_result = api.sda.delete_layer2_virtual_networks_v1(
        associated_layer3_virtual_network_name='string',
        fabric_id='string',
        traffic_type='string',
        vlan_id=0,
        vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_layer2_virtual_networks_v1(api, validator):
    try:
        assert is_valid_delete_layer2_virtual_networks_v1(
            validator,
            delete_layer2_virtual_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_layer2_virtual_networks_v1_default_val(api):
    endpoint_result = api.sda.delete_layer2_virtual_networks_v1(
        associated_layer3_virtual_network_name=None,
        fabric_id=None,
        traffic_type=None,
        vlan_id=None,
        vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_layer2_virtual_networks_v1_default_val(api, validator):
    try:
        assert is_valid_delete_layer2_virtual_networks_v1(
            validator,
            delete_layer2_virtual_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_layer2_virtual_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_87c794771a235f0da82cf11d968c9ec3_v2_3_7_9').validate(obj)
    return True


def get_layer2_virtual_networks_v1(api):
    endpoint_result = api.sda.get_layer2_virtual_networks_v1(
        associated_layer3_virtual_network_name='string',
        fabric_id='string',
        id='string',
        limit=0,
        offset=0,
        traffic_type='string',
        vlan_id=0,
        vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_layer2_virtual_networks_v1(api, validator):
    try:
        assert is_valid_get_layer2_virtual_networks_v1(
            validator,
            get_layer2_virtual_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_layer2_virtual_networks_v1_default_val(api):
    endpoint_result = api.sda.get_layer2_virtual_networks_v1(
        associated_layer3_virtual_network_name=None,
        fabric_id=None,
        id=None,
        limit=None,
        offset=None,
        traffic_type=None,
        vlan_id=None,
        vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_layer2_virtual_networks_v1_default_val(api, validator):
    try:
        assert is_valid_get_layer2_virtual_networks_v1(
            validator,
            get_layer2_virtual_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_layer2_virtual_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_93bcb7a52e3c5763b246bcf438fe57c9_v2_3_7_9').validate(obj)
    return True


def update_layer2_virtual_networks_v1(api):
    endpoint_result = api.sda.update_layer2_virtual_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_layer2_virtual_networks_v1(api, validator):
    try:
        assert is_valid_update_layer2_virtual_networks_v1(
            validator,
            update_layer2_virtual_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_layer2_virtual_networks_v1_default_val(api):
    endpoint_result = api.sda.update_layer2_virtual_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_layer2_virtual_networks_v1_default_val(api, validator):
    try:
        assert is_valid_update_layer2_virtual_networks_v1(
            validator,
            update_layer2_virtual_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_layer2_virtual_network_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_98a69aee0c555fb5baaa9db43327f955_v2_3_7_9').validate(obj)
    return True


def get_layer2_virtual_network_count_v1(api):
    endpoint_result = api.sda.get_layer2_virtual_network_count_v1(
        associated_layer3_virtual_network_name='string',
        fabric_id='string',
        traffic_type='string',
        vlan_id=0,
        vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_layer2_virtual_network_count_v1(api, validator):
    try:
        assert is_valid_get_layer2_virtual_network_count_v1(
            validator,
            get_layer2_virtual_network_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_layer2_virtual_network_count_v1_default_val(api):
    endpoint_result = api.sda.get_layer2_virtual_network_count_v1(
        associated_layer3_virtual_network_name=None,
        fabric_id=None,
        traffic_type=None,
        vlan_id=None,
        vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_layer2_virtual_network_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_layer2_virtual_network_count_v1(
            validator,
            get_layer2_virtual_network_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_layer2_virtual_network_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_50bfbdb9daba59fc9587824918c61cd6_v2_3_7_9').validate(obj)
    return True


def delete_layer2_virtual_network_by_id_v1(api):
    endpoint_result = api.sda.delete_layer2_virtual_network_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_layer2_virtual_network_by_id_v1(api, validator):
    try:
        assert is_valid_delete_layer2_virtual_network_by_id_v1(
            validator,
            delete_layer2_virtual_network_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_layer2_virtual_network_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_layer2_virtual_network_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_layer2_virtual_network_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_layer2_virtual_network_by_id_v1(
            validator,
            delete_layer2_virtual_network_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_layer3_virtual_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3606dabd13cd5e9c928daf80d6758d62_v2_3_7_9').validate(obj)
    return True


def add_layer3_virtual_networks_v1(api):
    endpoint_result = api.sda.add_layer3_virtual_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_layer3_virtual_networks_v1(api, validator):
    try:
        assert is_valid_add_layer3_virtual_networks_v1(
            validator,
            add_layer3_virtual_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_layer3_virtual_networks_v1_default_val(api):
    endpoint_result = api.sda.add_layer3_virtual_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_layer3_virtual_networks_v1_default_val(api, validator):
    try:
        assert is_valid_add_layer3_virtual_networks_v1(
            validator,
            add_layer3_virtual_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_layer3_virtual_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2fa3e62148dd542a8452b68ea888833a_v2_3_7_9').validate(obj)
    return True


def get_layer3_virtual_networks_v1(api):
    endpoint_result = api.sda.get_layer3_virtual_networks_v1(
        anchored_site_id='string',
        fabric_id='string',
        limit=0,
        offset=0,
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_layer3_virtual_networks_v1(api, validator):
    try:
        assert is_valid_get_layer3_virtual_networks_v1(
            validator,
            get_layer3_virtual_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_layer3_virtual_networks_v1_default_val(api):
    endpoint_result = api.sda.get_layer3_virtual_networks_v1(
        anchored_site_id=None,
        fabric_id=None,
        limit=None,
        offset=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_layer3_virtual_networks_v1_default_val(api, validator):
    try:
        assert is_valid_get_layer3_virtual_networks_v1(
            validator,
            get_layer3_virtual_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_layer3_virtual_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_86e14a6db07f5c41903df6039be72e9c_v2_3_7_9').validate(obj)
    return True


def delete_layer3_virtual_networks_v1(api):
    endpoint_result = api.sda.delete_layer3_virtual_networks_v1(
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_layer3_virtual_networks_v1(api, validator):
    try:
        assert is_valid_delete_layer3_virtual_networks_v1(
            validator,
            delete_layer3_virtual_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_layer3_virtual_networks_v1_default_val(api):
    endpoint_result = api.sda.delete_layer3_virtual_networks_v1(
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_layer3_virtual_networks_v1_default_val(api, validator):
    try:
        assert is_valid_delete_layer3_virtual_networks_v1(
            validator,
            delete_layer3_virtual_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_layer3_virtual_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ed9125b257ea54b79ef2db2d8ebd9d00_v2_3_7_9').validate(obj)
    return True


def update_layer3_virtual_networks_v1(api):
    endpoint_result = api.sda.update_layer3_virtual_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_layer3_virtual_networks_v1(api, validator):
    try:
        assert is_valid_update_layer3_virtual_networks_v1(
            validator,
            update_layer3_virtual_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_layer3_virtual_networks_v1_default_val(api):
    endpoint_result = api.sda.update_layer3_virtual_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_layer3_virtual_networks_v1_default_val(api, validator):
    try:
        assert is_valid_update_layer3_virtual_networks_v1(
            validator,
            update_layer3_virtual_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_layer3_virtual_networks_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ced302dd267557c79c2f5aee72da9e4c_v2_3_7_9').validate(obj)
    return True


def get_layer3_virtual_networks_count_v1(api):
    endpoint_result = api.sda.get_layer3_virtual_networks_count_v1(
        anchored_site_id='string',
        fabric_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_layer3_virtual_networks_count_v1(api, validator):
    try:
        assert is_valid_get_layer3_virtual_networks_count_v1(
            validator,
            get_layer3_virtual_networks_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_layer3_virtual_networks_count_v1_default_val(api):
    endpoint_result = api.sda.get_layer3_virtual_networks_count_v1(
        anchored_site_id=None,
        fabric_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_layer3_virtual_networks_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_layer3_virtual_networks_count_v1(
            validator,
            get_layer3_virtual_networks_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_layer3_virtual_network_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_12a4e95fb6765d48bac0c654a393a0a8_v2_3_7_9').validate(obj)
    return True


def delete_layer3_virtual_network_by_id_v1(api):
    endpoint_result = api.sda.delete_layer3_virtual_network_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_layer3_virtual_network_by_id_v1(api, validator):
    try:
        assert is_valid_delete_layer3_virtual_network_by_id_v1(
            validator,
            delete_layer3_virtual_network_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_layer3_virtual_network_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_layer3_virtual_network_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_layer3_virtual_network_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_layer3_virtual_network_by_id_v1(
            validator,
            delete_layer3_virtual_network_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_multicast_v1(json_schema_validate, obj):
    json_schema_validate('jsd_049cfb964a2958909f7ca12d23ab2bdb_v2_3_7_9').validate(obj)
    return True


def update_multicast_v1(api):
    endpoint_result = api.sda.update_multicast_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_multicast_v1(api, validator):
    try:
        assert is_valid_update_multicast_v1(
            validator,
            update_multicast_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_multicast_v1_default_val(api):
    endpoint_result = api.sda.update_multicast_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_multicast_v1_default_val(api, validator):
    try:
        assert is_valid_update_multicast_v1(
            validator,
            update_multicast_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_multicast_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9eb648d275875745950bc33d3f12a28f_v2_3_7_9').validate(obj)
    return True


def get_multicast_v1(api):
    endpoint_result = api.sda.get_multicast_v1(
        fabric_id='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_multicast_v1(api, validator):
    try:
        assert is_valid_get_multicast_v1(
            validator,
            get_multicast_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_multicast_v1_default_val(api):
    endpoint_result = api.sda.get_multicast_v1(
        fabric_id=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_multicast_v1_default_val(api, validator):
    try:
        assert is_valid_get_multicast_v1(
            validator,
            get_multicast_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_multicast_virtual_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_03cdc0bafd4257e78d211a1f4120bfa9_v2_3_7_9').validate(obj)
    return True


def add_multicast_virtual_networks_v1(api):
    endpoint_result = api.sda.add_multicast_virtual_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_multicast_virtual_networks_v1(api, validator):
    try:
        assert is_valid_add_multicast_virtual_networks_v1(
            validator,
            add_multicast_virtual_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_multicast_virtual_networks_v1_default_val(api):
    endpoint_result = api.sda.add_multicast_virtual_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_multicast_virtual_networks_v1_default_val(api, validator):
    try:
        assert is_valid_add_multicast_virtual_networks_v1(
            validator,
            add_multicast_virtual_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_multicast_virtual_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bc8fbaa14c0b5064ba44a9aaf997a593_v2_3_7_9').validate(obj)
    return True


def get_multicast_virtual_networks_v1(api):
    endpoint_result = api.sda.get_multicast_virtual_networks_v1(
        fabric_id='string',
        limit=0,
        offset=0,
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_multicast_virtual_networks_v1(api, validator):
    try:
        assert is_valid_get_multicast_virtual_networks_v1(
            validator,
            get_multicast_virtual_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_multicast_virtual_networks_v1_default_val(api):
    endpoint_result = api.sda.get_multicast_virtual_networks_v1(
        fabric_id=None,
        limit=None,
        offset=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_multicast_virtual_networks_v1_default_val(api, validator):
    try:
        assert is_valid_get_multicast_virtual_networks_v1(
            validator,
            get_multicast_virtual_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_multicast_virtual_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_93144bc3ed6556f9b9c959e53e271d70_v2_3_7_9').validate(obj)
    return True


def update_multicast_virtual_networks_v1(api):
    endpoint_result = api.sda.update_multicast_virtual_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_multicast_virtual_networks_v1(api, validator):
    try:
        assert is_valid_update_multicast_virtual_networks_v1(
            validator,
            update_multicast_virtual_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_multicast_virtual_networks_v1_default_val(api):
    endpoint_result = api.sda.update_multicast_virtual_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_multicast_virtual_networks_v1_default_val(api, validator):
    try:
        assert is_valid_update_multicast_virtual_networks_v1(
            validator,
            update_multicast_virtual_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_multicast_virtual_network_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8948ecb8526b5333b7d7223dc4a68794_v2_3_7_9').validate(obj)
    return True


def get_multicast_virtual_network_count_v1(api):
    endpoint_result = api.sda.get_multicast_virtual_network_count_v1(
        fabric_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_multicast_virtual_network_count_v1(api, validator):
    try:
        assert is_valid_get_multicast_virtual_network_count_v1(
            validator,
            get_multicast_virtual_network_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_multicast_virtual_network_count_v1_default_val(api):
    endpoint_result = api.sda.get_multicast_virtual_network_count_v1(
        fabric_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_multicast_virtual_network_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_multicast_virtual_network_count_v1(
            validator,
            get_multicast_virtual_network_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_multicast_virtual_network_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e1e7b254440156e0a9ed4e72c5a9685a_v2_3_7_9').validate(obj)
    return True


def delete_multicast_virtual_network_by_id_v1(api):
    endpoint_result = api.sda.delete_multicast_virtual_network_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_multicast_virtual_network_by_id_v1(api, validator):
    try:
        assert is_valid_delete_multicast_virtual_network_by_id_v1(
            validator,
            delete_multicast_virtual_network_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_multicast_virtual_network_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_multicast_virtual_network_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_multicast_virtual_network_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_multicast_virtual_network_by_id_v1(
            validator,
            delete_multicast_virtual_network_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_pending_fabric_events_v1(json_schema_validate, obj):
    json_schema_validate('jsd_180e044ddd8c5804989c999cf6f87e3a_v2_3_7_9').validate(obj)
    return True


def get_pending_fabric_events_v1(api):
    endpoint_result = api.sda.get_pending_fabric_events_v1(
        fabric_id='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_pending_fabric_events_v1(api, validator):
    try:
        assert is_valid_get_pending_fabric_events_v1(
            validator,
            get_pending_fabric_events_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_pending_fabric_events_v1_default_val(api):
    endpoint_result = api.sda.get_pending_fabric_events_v1(
        fabric_id=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_pending_fabric_events_v1_default_val(api, validator):
    try:
        assert is_valid_get_pending_fabric_events_v1(
            validator,
            get_pending_fabric_events_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_apply_pending_fabric_events_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f20eecc6e2d95a03a9e8961cd4337467_v2_3_7_9').validate(obj)
    return True


def apply_pending_fabric_events_v1(api):
    endpoint_result = api.sda.apply_pending_fabric_events_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_apply_pending_fabric_events_v1(api, validator):
    try:
        assert is_valid_apply_pending_fabric_events_v1(
            validator,
            apply_pending_fabric_events_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def apply_pending_fabric_events_v1_default_val(api):
    endpoint_result = api.sda.apply_pending_fabric_events_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_apply_pending_fabric_events_v1_default_val(api, validator):
    try:
        assert is_valid_apply_pending_fabric_events_v1(
            validator,
            apply_pending_fabric_events_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_port_assignments_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8d6b58f378895114839682dceed1a9b5_v2_3_7_9').validate(obj)
    return True


def add_port_assignments_v1(api):
    endpoint_result = api.sda.add_port_assignments_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignments_v1(api, validator):
    try:
        assert is_valid_add_port_assignments_v1(
            validator,
            add_port_assignments_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_port_assignments_v1_default_val(api):
    endpoint_result = api.sda.add_port_assignments_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignments_v1_default_val(api, validator):
    try:
        assert is_valid_add_port_assignments_v1(
            validator,
            add_port_assignments_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_assignments_v1(json_schema_validate, obj):
    json_schema_validate('jsd_61a9bc4645925814ac76d95268fe3f05_v2_3_7_9').validate(obj)
    return True


def get_port_assignments_v1(api):
    endpoint_result = api.sda.get_port_assignments_v1(
        data_vlan_name='string',
        fabric_id='string',
        interface_name='string',
        limit=0,
        network_device_id='string',
        offset=0,
        voice_vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignments_v1(api, validator):
    try:
        assert is_valid_get_port_assignments_v1(
            validator,
            get_port_assignments_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_port_assignments_v1_default_val(api):
    endpoint_result = api.sda.get_port_assignments_v1(
        data_vlan_name=None,
        fabric_id=None,
        interface_name=None,
        limit=None,
        network_device_id=None,
        offset=None,
        voice_vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignments_v1_default_val(api, validator):
    try:
        assert is_valid_get_port_assignments_v1(
            validator,
            get_port_assignments_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_port_assignments_v1(json_schema_validate, obj):
    json_schema_validate('jsd_39350cad522e57a7b96b7238935689ed_v2_3_7_9').validate(obj)
    return True


def update_port_assignments_v1(api):
    endpoint_result = api.sda.update_port_assignments_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_port_assignments_v1(api, validator):
    try:
        assert is_valid_update_port_assignments_v1(
            validator,
            update_port_assignments_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_port_assignments_v1_default_val(api):
    endpoint_result = api.sda.update_port_assignments_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_port_assignments_v1_default_val(api, validator):
    try:
        assert is_valid_update_port_assignments_v1(
            validator,
            update_port_assignments_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_assignments_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3238ee38ba825f79a76d9e7e6074c450_v2_3_7_9').validate(obj)
    return True


def delete_port_assignments_v1(api):
    endpoint_result = api.sda.delete_port_assignments_v1(
        data_vlan_name='string',
        fabric_id='string',
        interface_name='string',
        network_device_id='string',
        voice_vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignments_v1(api, validator):
    try:
        assert is_valid_delete_port_assignments_v1(
            validator,
            delete_port_assignments_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_port_assignments_v1_default_val(api):
    endpoint_result = api.sda.delete_port_assignments_v1(
        data_vlan_name=None,
        fabric_id=None,
        interface_name=None,
        network_device_id=None,
        voice_vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignments_v1_default_val(api, validator):
    try:
        assert is_valid_delete_port_assignments_v1(
            validator,
            delete_port_assignments_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_assignment_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e11301d6336f512fbc6db01768e3ad5a_v2_3_7_9').validate(obj)
    return True


def get_port_assignment_count_v1(api):
    endpoint_result = api.sda.get_port_assignment_count_v1(
        data_vlan_name='string',
        fabric_id='string',
        interface_name='string',
        network_device_id='string',
        voice_vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_count_v1(api, validator):
    try:
        assert is_valid_get_port_assignment_count_v1(
            validator,
            get_port_assignment_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_port_assignment_count_v1_default_val(api):
    endpoint_result = api.sda.get_port_assignment_count_v1(
        data_vlan_name=None,
        fabric_id=None,
        interface_name=None,
        network_device_id=None,
        voice_vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_port_assignment_count_v1(
            validator,
            get_port_assignment_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_assignment_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7aa18582de8753438e0908cf9d92c2de_v2_3_7_9').validate(obj)
    return True


def delete_port_assignment_by_id_v1(api):
    endpoint_result = api.sda.delete_port_assignment_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_by_id_v1(api, validator):
    try:
        assert is_valid_delete_port_assignment_by_id_v1(
            validator,
            delete_port_assignment_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_port_assignment_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_port_assignment_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_port_assignment_by_id_v1(
            validator,
            delete_port_assignment_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_channels_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c747d79eb18e52f5a161006aa28df129_v2_3_7_9').validate(obj)
    return True


def get_port_channels_v1(api):
    endpoint_result = api.sda.get_port_channels_v1(
        connected_device_type='string',
        fabric_id='string',
        limit=0,
        network_device_id='string',
        offset=0,
        port_channel_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_channels_v1(api, validator):
    try:
        assert is_valid_get_port_channels_v1(
            validator,
            get_port_channels_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_port_channels_v1_default_val(api):
    endpoint_result = api.sda.get_port_channels_v1(
        connected_device_type=None,
        fabric_id=None,
        limit=None,
        network_device_id=None,
        offset=None,
        port_channel_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_channels_v1_default_val(api, validator):
    try:
        assert is_valid_get_port_channels_v1(
            validator,
            get_port_channels_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_port_channels_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7f2b137487385de6925b7b6136d4b027_v2_3_7_9').validate(obj)
    return True


def add_port_channels_v1(api):
    endpoint_result = api.sda.add_port_channels_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_channels_v1(api, validator):
    try:
        assert is_valid_add_port_channels_v1(
            validator,
            add_port_channels_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_port_channels_v1_default_val(api):
    endpoint_result = api.sda.add_port_channels_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_channels_v1_default_val(api, validator):
    try:
        assert is_valid_add_port_channels_v1(
            validator,
            add_port_channels_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_port_channels_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7bd421c1db8c5deaa3301b8cc73dd541_v2_3_7_9').validate(obj)
    return True


def update_port_channels_v1(api):
    endpoint_result = api.sda.update_port_channels_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_port_channels_v1(api, validator):
    try:
        assert is_valid_update_port_channels_v1(
            validator,
            update_port_channels_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_port_channels_v1_default_val(api):
    endpoint_result = api.sda.update_port_channels_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_port_channels_v1_default_val(api, validator):
    try:
        assert is_valid_update_port_channels_v1(
            validator,
            update_port_channels_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_channels_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1fd48c49a3f65cecb1f84f10b69b04f5_v2_3_7_9').validate(obj)
    return True


def delete_port_channels_v1(api):
    endpoint_result = api.sda.delete_port_channels_v1(
        connected_device_type='string',
        fabric_id='string',
        network_device_id='string',
        port_channel_ids='string',
        port_channel_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_channels_v1(api, validator):
    try:
        assert is_valid_delete_port_channels_v1(
            validator,
            delete_port_channels_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_port_channels_v1_default_val(api):
    endpoint_result = api.sda.delete_port_channels_v1(
        connected_device_type=None,
        fabric_id=None,
        network_device_id=None,
        port_channel_ids=None,
        port_channel_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_channels_v1_default_val(api, validator):
    try:
        assert is_valid_delete_port_channels_v1(
            validator,
            delete_port_channels_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_channel_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_292767b6ba7d5504bb3493964063611a_v2_3_7_9').validate(obj)
    return True


def get_port_channel_count_v1(api):
    endpoint_result = api.sda.get_port_channel_count_v1(
        connected_device_type='string',
        fabric_id='string',
        network_device_id='string',
        port_channel_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_channel_count_v1(api, validator):
    try:
        assert is_valid_get_port_channel_count_v1(
            validator,
            get_port_channel_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_port_channel_count_v1_default_val(api):
    endpoint_result = api.sda.get_port_channel_count_v1(
        connected_device_type=None,
        fabric_id=None,
        network_device_id=None,
        port_channel_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_channel_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_port_channel_count_v1(
            validator,
            get_port_channel_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_channel_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6bcad6a4ea0850bf9b099b938bc55932_v2_3_7_9').validate(obj)
    return True


def delete_port_channel_by_id_v1(api):
    endpoint_result = api.sda.delete_port_channel_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_channel_by_id_v1(api, validator):
    try:
        assert is_valid_delete_port_channel_by_id_v1(
            validator,
            delete_port_channel_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_port_channel_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_port_channel_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_channel_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_port_channel_by_id_v1(
            validator,
            delete_port_channel_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_provisioned_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b049914e384051afbf87971d3066152b_v2_3_7_9').validate(obj)
    return True


def delete_provisioned_devices_v1(api):
    endpoint_result = api.sda.delete_provisioned_devices_v1(
        clean_up_config=True,
        network_device_id='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_devices_v1(api, validator):
    try:
        assert is_valid_delete_provisioned_devices_v1(
            validator,
            delete_provisioned_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_provisioned_devices_v1_default_val(api):
    endpoint_result = api.sda.delete_provisioned_devices_v1(
        clean_up_config=None,
        network_device_id=None,
        site_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_devices_v1_default_val(api, validator):
    try:
        assert is_valid_delete_provisioned_devices_v1(
            validator,
            delete_provisioned_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_provision_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bdcb514ae33b571795e4a42147d11f87_v2_3_7_9').validate(obj)
    return True


def provision_devices_v1(api):
    endpoint_result = api.sda.provision_devices_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_provision_devices_v1(api, validator):
    try:
        assert is_valid_provision_devices_v1(
            validator,
            provision_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def provision_devices_v1_default_val(api):
    endpoint_result = api.sda.provision_devices_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_provision_devices_v1_default_val(api, validator):
    try:
        assert is_valid_provision_devices_v1(
            validator,
            provision_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_provisioned_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4f974cbea9645bfda97affac9ea41ffe_v2_3_7_9').validate(obj)
    return True


def get_provisioned_devices_v1(api):
    endpoint_result = api.sda.get_provisioned_devices_v1(
        id='string',
        limit=0,
        network_device_id='string',
        offset=0,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_devices_v1(api, validator):
    try:
        assert is_valid_get_provisioned_devices_v1(
            validator,
            get_provisioned_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_provisioned_devices_v1_default_val(api):
    endpoint_result = api.sda.get_provisioned_devices_v1(
        id=None,
        limit=None,
        network_device_id=None,
        offset=None,
        site_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_devices_v1_default_val(api, validator):
    try:
        assert is_valid_get_provisioned_devices_v1(
            validator,
            get_provisioned_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_re_provision_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_92843f4b2825561e808787a16f7e0a1f_v2_3_7_9').validate(obj)
    return True


def re_provision_devices_v1(api):
    endpoint_result = api.sda.re_provision_devices_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_re_provision_devices_v1(api, validator):
    try:
        assert is_valid_re_provision_devices_v1(
            validator,
            re_provision_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def re_provision_devices_v1_default_val(api):
    endpoint_result = api.sda.re_provision_devices_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_re_provision_devices_v1_default_val(api, validator):
    try:
        assert is_valid_re_provision_devices_v1(
            validator,
            re_provision_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_provisioned_devices_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_580acb7d048a5455b75965c3706f8977_v2_3_7_9').validate(obj)
    return True


def get_provisioned_devices_count_v1(api):
    endpoint_result = api.sda.get_provisioned_devices_count_v1(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_devices_count_v1(api, validator):
    try:
        assert is_valid_get_provisioned_devices_count_v1(
            validator,
            get_provisioned_devices_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_provisioned_devices_count_v1_default_val(api):
    endpoint_result = api.sda.get_provisioned_devices_count_v1(
        site_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_devices_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_provisioned_devices_count_v1(
            validator,
            get_provisioned_devices_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_provisioned_device_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ab7cbac7eaa45f259c9035fb828f6c08_v2_3_7_9').validate(obj)
    return True


def delete_provisioned_device_by_id_v1(api):
    endpoint_result = api.sda.delete_provisioned_device_by_id_v1(
        clean_up_config=True,
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_device_by_id_v1(api, validator):
    try:
        assert is_valid_delete_provisioned_device_by_id_v1(
            validator,
            delete_provisioned_device_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_provisioned_device_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_provisioned_device_by_id_v1(
        clean_up_config=None,
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_device_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_provisioned_device_by_id_v1(
            validator,
            delete_provisioned_device_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_transit_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_cc1599012a5a59c8abdda5376b5cc583_v2_3_7_9').validate(obj)
    return True


def update_transit_networks_v1(api):
    endpoint_result = api.sda.update_transit_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_transit_networks_v1(api, validator):
    try:
        assert is_valid_update_transit_networks_v1(
            validator,
            update_transit_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_transit_networks_v1_default_val(api):
    endpoint_result = api.sda.update_transit_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_transit_networks_v1_default_val(api, validator):
    try:
        assert is_valid_update_transit_networks_v1(
            validator,
            update_transit_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_transit_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_996eb415f4615ac09e61c6582ecca2fa_v2_3_7_9').validate(obj)
    return True


def get_transit_networks_v1(api):
    endpoint_result = api.sda.get_transit_networks_v1(
        id='string',
        limit=0,
        name='string',
        offset=0,
        type='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_transit_networks_v1(api, validator):
    try:
        assert is_valid_get_transit_networks_v1(
            validator,
            get_transit_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_transit_networks_v1_default_val(api):
    endpoint_result = api.sda.get_transit_networks_v1(
        id=None,
        limit=None,
        name=None,
        offset=None,
        type=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_transit_networks_v1_default_val(api, validator):
    try:
        assert is_valid_get_transit_networks_v1(
            validator,
            get_transit_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_transit_networks_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8ae57085565e551594fc05b4db6a64af_v2_3_7_9').validate(obj)
    return True


def add_transit_networks_v1(api):
    endpoint_result = api.sda.add_transit_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_transit_networks_v1(api, validator):
    try:
        assert is_valid_add_transit_networks_v1(
            validator,
            add_transit_networks_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_transit_networks_v1_default_val(api):
    endpoint_result = api.sda.add_transit_networks_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_transit_networks_v1_default_val(api, validator):
    try:
        assert is_valid_add_transit_networks_v1(
            validator,
            add_transit_networks_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_transit_networks_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fe6a7f95437d57bd997d2c8f0482310d_v2_3_7_9').validate(obj)
    return True


def get_transit_networks_count_v1(api):
    endpoint_result = api.sda.get_transit_networks_count_v1(
        type='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_transit_networks_count_v1(api, validator):
    try:
        assert is_valid_get_transit_networks_count_v1(
            validator,
            get_transit_networks_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_transit_networks_count_v1_default_val(api):
    endpoint_result = api.sda.get_transit_networks_count_v1(
        type=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_transit_networks_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_transit_networks_count_v1(
            validator,
            get_transit_networks_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_transit_network_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1bc1bbf0065150ebabbe5e5bee3d80d7_v2_3_7_9').validate(obj)
    return True


def delete_transit_network_by_id_v1(api):
    endpoint_result = api.sda.delete_transit_network_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_transit_network_by_id_v1(api, validator):
    try:
        assert is_valid_delete_transit_network_by_id_v1(
            validator,
            delete_transit_network_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_transit_network_by_id_v1_default_val(api):
    endpoint_result = api.sda.delete_transit_network_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_transit_network_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_transit_network_by_id_v1(
            validator,
            delete_transit_network_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_virtual_network_with_scalable_groups_v1(json_schema_validate, obj):
    json_schema_validate('jsd_72472f5ebb9d50aab287f320d32181c0_v2_3_7_9').validate(obj)
    return True


def add_virtual_network_with_scalable_groups_v1(api):
    endpoint_result = api.sda.add_virtual_network_with_scalable_groups_v1(
        active_validation=True,
        isGuestVirtualNetwork=True,
        payload=None,
        scalableGroupNames=['string'],
        vManageVpnId='string',
        virtualNetworkName='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_add_virtual_network_with_scalable_groups_v1(api, validator):
    try:
        assert is_valid_add_virtual_network_with_scalable_groups_v1(
            validator,
            add_virtual_network_with_scalable_groups_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_virtual_network_with_scalable_groups_v1_default_val(api):
    endpoint_result = api.sda.add_virtual_network_with_scalable_groups_v1(
        active_validation=True,
        isGuestVirtualNetwork=None,
        payload=None,
        scalableGroupNames=None,
        vManageVpnId=None,
        virtualNetworkName=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_virtual_network_with_scalable_groups_v1_default_val(api, validator):
    try:
        assert is_valid_add_virtual_network_with_scalable_groups_v1(
            validator,
            add_virtual_network_with_scalable_groups_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_virtual_network_with_scalable_groups_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2f2e8552eabc5e5f97e1f40bcc4b4c75_v2_3_7_9').validate(obj)
    return True


def delete_virtual_network_with_scalable_groups_v1(api):
    endpoint_result = api.sda.delete_virtual_network_with_scalable_groups_v1(
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_virtual_network_with_scalable_groups_v1(api, validator):
    try:
        assert is_valid_delete_virtual_network_with_scalable_groups_v1(
            validator,
            delete_virtual_network_with_scalable_groups_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_virtual_network_with_scalable_groups_v1_default_val(api):
    endpoint_result = api.sda.delete_virtual_network_with_scalable_groups_v1(
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_virtual_network_with_scalable_groups_v1_default_val(api, validator):
    try:
        assert is_valid_delete_virtual_network_with_scalable_groups_v1(
            validator,
            delete_virtual_network_with_scalable_groups_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_virtual_network_with_scalable_groups_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ea4b1c052b855bd9a0e99f803e6185a5_v2_3_7_9').validate(obj)
    return True


def get_virtual_network_with_scalable_groups_v1(api):
    endpoint_result = api.sda.get_virtual_network_with_scalable_groups_v1(
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_virtual_network_with_scalable_groups_v1(api, validator):
    try:
        assert is_valid_get_virtual_network_with_scalable_groups_v1(
            validator,
            get_virtual_network_with_scalable_groups_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_virtual_network_with_scalable_groups_v1_default_val(api):
    endpoint_result = api.sda.get_virtual_network_with_scalable_groups_v1(
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_virtual_network_with_scalable_groups_v1_default_val(api, validator):
    try:
        assert is_valid_get_virtual_network_with_scalable_groups_v1(
            validator,
            get_virtual_network_with_scalable_groups_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_virtual_network_with_scalable_groups_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f9492367570c5f009cf8b5955790e87c_v2_3_7_9').validate(obj)
    return True


def update_virtual_network_with_scalable_groups_v1(api):
    endpoint_result = api.sda.update_virtual_network_with_scalable_groups_v1(
        active_validation=True,
        isGuestVirtualNetwork=True,
        payload=None,
        scalableGroupNames=['string'],
        vManageVpnId='string',
        virtualNetworkName='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_update_virtual_network_with_scalable_groups_v1(api, validator):
    try:
        assert is_valid_update_virtual_network_with_scalable_groups_v1(
            validator,
            update_virtual_network_with_scalable_groups_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_virtual_network_with_scalable_groups_v1_default_val(api):
    endpoint_result = api.sda.update_virtual_network_with_scalable_groups_v1(
        active_validation=True,
        isGuestVirtualNetwork=None,
        payload=None,
        scalableGroupNames=None,
        vManageVpnId=None,
        virtualNetworkName=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_virtual_network_with_scalable_groups_v1_default_val(api, validator):
    try:
        assert is_valid_update_virtual_network_with_scalable_groups_v1(
            validator,
            update_virtual_network_with_scalable_groups_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

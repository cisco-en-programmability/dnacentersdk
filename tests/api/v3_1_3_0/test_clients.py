# -*- coding: utf-8 -*-
"""CatalystCenterAPI clients API fixtures and tests.

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


def is_valid_retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_v1(json_schema_validate, obj):
    json_schema_validate('jsd_dfcf64acc1815459acc146cd924e9877_v3_1_3_0').validate(obj)
    return True


def retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_v1(api):
    endpoint_result = api.clients.retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_v1(
        attribute='string',
        band='string',
        connected_network_device_name='string',
        end_time=0,
        ipv4_address='string',
        ipv6_address='string',
        limit=0,
        mac_address='string',
        offset=0,
        order='string',
        os_type='string',
        os_version='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        sort_by='string',
        ssid='string',
        start_time=0,
        type='string',
        view='string',
        wlc_name='string'
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_v1(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_v1(
            validator,
            retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_v1_default_val(api):
    endpoint_result = api.clients.retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_v1(
        attribute=None,
        band=None,
        connected_network_device_name=None,
        end_time=None,
        ipv4_address=None,
        ipv6_address=None,
        limit=None,
        mac_address=None,
        offset=None,
        order=None,
        os_type=None,
        os_version=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        sort_by=None,
        ssid=None,
        start_time=None,
        type=None,
        view=None,
        wlc_name=None
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_v1(
            validator,
            retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_count_of_clients_by_applying_basic_filtering_v1(json_schema_validate, obj):
    json_schema_validate('jsd_110ed18d78d455f9a51049a09ae12d48_v3_1_3_0').validate(obj)
    return True


def retrieves_the_total_count_of_clients_by_applying_basic_filtering_v1(api):
    endpoint_result = api.clients.retrieves_the_total_count_of_clients_by_applying_basic_filtering_v1(
        band='string',
        connected_network_device_name='string',
        end_time=0,
        ipv4_address='string',
        ipv6_address='string',
        mac_address='string',
        os_type='string',
        os_version='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        ssid='string',
        start_time=0,
        type='string',
        wlc_name='string'
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_total_count_of_clients_by_applying_basic_filtering_v1(api, validator):
    try:
        assert is_valid_retrieves_the_total_count_of_clients_by_applying_basic_filtering_v1(
            validator,
            retrieves_the_total_count_of_clients_by_applying_basic_filtering_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_count_of_clients_by_applying_basic_filtering_v1_default_val(api):
    endpoint_result = api.clients.retrieves_the_total_count_of_clients_by_applying_basic_filtering_v1(
        band=None,
        connected_network_device_name=None,
        end_time=None,
        ipv4_address=None,
        ipv6_address=None,
        mac_address=None,
        os_type=None,
        os_version=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        ssid=None,
        start_time=None,
        type=None,
        wlc_name=None
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_total_count_of_clients_by_applying_basic_filtering_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_total_count_of_clients_by_applying_basic_filtering_v1(
            validator,
            retrieves_the_total_count_of_clients_by_applying_basic_filtering_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ea5f116c0cd152bbb4a92c043738ea57_v3_1_3_0').validate(obj)
    return True


def retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_v1(api):
    endpoint_result = api.clients.retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 0}],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0,
        views=['string']
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_v1(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_v1(
            validator,
            retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_v1_default_val(api):
    endpoint_result = api.clients.retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_v1(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None,
        views=None
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_v1(
            validator,
            retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_number_of_clients_by_applying_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1628a2131eae5c1d8e73cd55eebf6a83_v3_1_3_0').validate(obj)
    return True


def retrieves_the_number_of_clients_by_applying_complex_filters_v1(api):
    endpoint_result = api.clients.retrieves_the_number_of_clients_by_applying_complex_filters_v1(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 0}],
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_number_of_clients_by_applying_complex_filters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_number_of_clients_by_applying_complex_filters_v1(
            validator,
            retrieves_the_number_of_clients_by_applying_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_number_of_clients_by_applying_complex_filters_v1_default_val(api):
    endpoint_result = api.clients.retrieves_the_number_of_clients_by_applying_complex_filters_v1(
        active_validation=True,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_number_of_clients_by_applying_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_number_of_clients_by_applying_complex_filters_v1(
            validator,
            retrieves_the_number_of_clients_by_applying_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_summary_analytics_data_related_to_clients_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f210ff2d89425b4790ce56f19da7be92_v3_1_3_0').validate(obj)
    return True


def retrieves_summary_analytics_data_related_to_clients_v1(api):
    endpoint_result = api.clients.retrieves_summary_analytics_data_related_to_clients_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 0}],
        groupBy=['string'],
        page={'limit': 0, 'cursor': 'string', 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_summary_analytics_data_related_to_clients_v1(api, validator):
    try:
        assert is_valid_retrieves_summary_analytics_data_related_to_clients_v1(
            validator,
            retrieves_summary_analytics_data_related_to_clients_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_summary_analytics_data_related_to_clients_v1_default_val(api):
    endpoint_result = api.clients.retrieves_summary_analytics_data_related_to_clients_v1(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_summary_analytics_data_related_to_clients_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_summary_analytics_data_related_to_clients_v1(
            validator,
            retrieves_summary_analytics_data_related_to_clients_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_top_n_analytics_data_related_to_clients_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0f44ddd3c38c5a9484f5cb4e125447bc_v3_1_3_0').validate(obj)
    return True


def retrieves_the_top_n_analytics_data_related_to_clients_v1(api):
    endpoint_result = api.clients.retrieves_the_top_n_analytics_data_related_to_clients_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 0}],
        groupBy=['string'],
        page={'limit': 0, 'cursor': 'string', 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0,
        topN=0
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_top_n_analytics_data_related_to_clients_v1(api, validator):
    try:
        assert is_valid_retrieves_the_top_n_analytics_data_related_to_clients_v1(
            validator,
            retrieves_the_top_n_analytics_data_related_to_clients_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_top_n_analytics_data_related_to_clients_v1_default_val(api):
    endpoint_result = api.clients.retrieves_the_top_n_analytics_data_related_to_clients_v1(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        payload=None,
        startTime=None,
        topN=None
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_top_n_analytics_data_related_to_clients_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_top_n_analytics_data_related_to_clients_v1(
            validator,
            retrieves_the_top_n_analytics_data_related_to_clients_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_trend_analytics_data_related_to_clients_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ffd2fefb57d5523c87a5d941eb93ddc3_v3_1_3_0').validate(obj)
    return True


def retrieves_the_trend_analytics_data_related_to_clients_v1(api):
    endpoint_result = api.clients.retrieves_the_trend_analytics_data_related_to_clients_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 0}],
        groupBy=['string'],
        page={'limit': 0, 'cursor': 'string', 'timeSortOrder': 'string'},
        payload=None,
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_trend_analytics_data_related_to_clients_v1(api, validator):
    try:
        assert is_valid_retrieves_the_trend_analytics_data_related_to_clients_v1(
            validator,
            retrieves_the_trend_analytics_data_related_to_clients_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_trend_analytics_data_related_to_clients_v1_default_val(api):
    endpoint_result = api.clients.retrieves_the_trend_analytics_data_related_to_clients_v1(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        payload=None,
        startTime=None,
        trendInterval=None
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_trend_analytics_data_related_to_clients_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_trend_analytics_data_related_to_clients_v1(
            validator,
            retrieves_the_trend_analytics_data_related_to_clients_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_specific_client_information_matching_the_macaddress_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ee00176282fd54ef90fc96a2c23d50ec_v3_1_3_0').validate(obj)
    return True


def retrieves_specific_client_information_matching_the_macaddress_v1(api):
    endpoint_result = api.clients.retrieves_specific_client_information_matching_the_macaddress_v1(
        attribute='string',
        end_time=0,
        id='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_specific_client_information_matching_the_macaddress_v1(api, validator):
    try:
        assert is_valid_retrieves_specific_client_information_matching_the_macaddress_v1(
            validator,
            retrieves_specific_client_information_matching_the_macaddress_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_specific_client_information_matching_the_macaddress_v1_default_val(api):
    endpoint_result = api.clients.retrieves_specific_client_information_matching_the_macaddress_v1(
        attribute=None,
        end_time=None,
        id='string',
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_specific_client_information_matching_the_macaddress_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_specific_client_information_matching_the_macaddress_v1(
            validator,
            retrieves_specific_client_information_matching_the_macaddress_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_specific_client_information_over_a_specified_period_of_time_v1(json_schema_validate, obj):
    json_schema_validate('jsd_311806d9a13d575abdc26d485af708e7_v3_1_3_0').validate(obj)
    return True


def retrieves_specific_client_information_over_a_specified_period_of_time_v1(api):
    endpoint_result = api.clients.retrieves_specific_client_information_over_a_specified_period_of_time_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 0}],
        groupBy=['string'],
        id='string',
        page={'limit': 0, 'cursor': 'string', 'timeSortOrder': 'string'},
        payload=None,
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_specific_client_information_over_a_specified_period_of_time_v1(api, validator):
    try:
        assert is_valid_retrieves_specific_client_information_over_a_specified_period_of_time_v1(
            validator,
            retrieves_specific_client_information_over_a_specified_period_of_time_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_specific_client_information_over_a_specified_period_of_time_v1_default_val(api):
    endpoint_result = api.clients.retrieves_specific_client_information_over_a_specified_period_of_time_v1(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        id='string',
        page=None,
        payload=None,
        startTime=None,
        trendInterval=None
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_specific_client_information_over_a_specified_period_of_time_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_specific_client_information_over_a_specified_period_of_time_v1(
            validator,
            retrieves_specific_client_information_over_a_specified_period_of_time_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_clients_energy_v1(json_schema_validate, obj):
    json_schema_validate('jsd_74dddfb3bc2f59f1905e64f5905e2296_v3_1_3_0').validate(obj)
    return True


def get_clients_energy_v1(api):
    endpoint_result = api.clients.get_clients_energy_v1(
        attribute='string',
        cursor='string',
        device_category='string',
        device_sub_category='string',
        end_time=0,
        id='string',
        limit=0,
        order='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        sort_by='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.clients
def test_get_clients_energy_v1(api, validator):
    try:
        assert is_valid_get_clients_energy_v1(
            validator,
            get_clients_energy_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_clients_energy_v1_default_val(api):
    endpoint_result = api.clients.get_clients_energy_v1(
        attribute=None,
        cursor=None,
        device_category=None,
        device_sub_category=None,
        end_time=None,
        id=None,
        limit=None,
        order=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.clients
def test_get_clients_energy_v1_default_val(api, validator):
    try:
        assert is_valid_get_clients_energy_v1(
            validator,
            get_clients_energy_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_clients_energy_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1460bc8798815ab89147f2054720da4d_v3_1_3_0').validate(obj)
    return True


def count_clients_energy_v1(api):
    endpoint_result = api.clients.count_clients_energy_v1(
        device_category='string',
        device_sub_category='string',
        end_time=0,
        id='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.clients
def test_count_clients_energy_v1(api, validator):
    try:
        assert is_valid_count_clients_energy_v1(
            validator,
            count_clients_energy_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_clients_energy_v1_default_val(api):
    endpoint_result = api.clients.count_clients_energy_v1(
        device_category=None,
        device_sub_category=None,
        end_time=None,
        id=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.clients
def test_count_clients_energy_v1_default_val(api, validator):
    try:
        assert is_valid_count_clients_energy_v1(
            validator,
            count_clients_energy_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_clients_energy_v1(json_schema_validate, obj):
    json_schema_validate('jsd_712464c536ac5a318629fc3d6b3dc236_v3_1_3_0').validate(obj)
    return True


def query_clients_energy_v1(api):
    endpoint_result = api.clients.query_clients_energy_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'logicalOperator': 'string', 'filters': [{'key': 'string', 'operator': 'string', 'value': ['string']}]}],
        page={'limit': 0, 'cursor': 'string', 'sortBy': [{'name': 'string', 'order': 'string', 'function': 'string'}]},
        payload=None,
        startTime=0,
        views=['string']
    )
    return endpoint_result


@pytest.mark.clients
def test_query_clients_energy_v1(api, validator):
    try:
        assert is_valid_query_clients_energy_v1(
            validator,
            query_clients_energy_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def query_clients_energy_v1_default_val(api):
    endpoint_result = api.clients.query_clients_energy_v1(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None,
        views=None
    )
    return endpoint_result


@pytest.mark.clients
def test_query_clients_energy_v1_default_val(api, validator):
    try:
        assert is_valid_query_clients_energy_v1(
            validator,
            query_clients_energy_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_clients_energy_from_query_v1(json_schema_validate, obj):
    json_schema_validate('jsd_201c765afc72581d862cd61f5139d224_v3_1_3_0').validate(obj)
    return True


def count_clients_energy_from_query_v1(api):
    endpoint_result = api.clients.count_clients_energy_from_query_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'logicalOperator': 'string', 'filters': [{'key': 'string', 'operator': 'string', 'value': ['string']}]}],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string', 'function': 'string'}]},
        payload=None,
        startTime=0,
        views=['string']
    )
    return endpoint_result


@pytest.mark.clients
def test_count_clients_energy_from_query_v1(api, validator):
    try:
        assert is_valid_count_clients_energy_from_query_v1(
            validator,
            count_clients_energy_from_query_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_clients_energy_from_query_v1_default_val(api):
    endpoint_result = api.clients.count_clients_energy_from_query_v1(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None,
        views=None
    )
    return endpoint_result


@pytest.mark.clients
def test_count_clients_energy_from_query_v1_default_val(api, validator):
    try:
        assert is_valid_count_clients_energy_from_query_v1(
            validator,
            count_clients_energy_from_query_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_client_energy_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6f090c2a6b325d32be55209cd6839f30_v3_1_3_0').validate(obj)
    return True


def get_client_energy_by_id_v1(api):
    endpoint_result = api.clients.get_client_energy_by_id_v1(
        attribute='string',
        end_time=0,
        id='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_energy_by_id_v1(api, validator):
    try:
        assert is_valid_get_client_energy_by_id_v1(
            validator,
            get_client_energy_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_client_energy_by_id_v1_default_val(api):
    endpoint_result = api.clients.get_client_energy_by_id_v1(
        attribute=None,
        end_time=None,
        id='string',
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_energy_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_client_energy_by_id_v1(
            validator,
            get_client_energy_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_client_detail_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f2c6333d8eb05491a16c2d32095e4352_v3_1_3_0').validate(obj)
    return True


def get_client_detail_v1(api):
    endpoint_result = api.clients.get_client_detail_v1(
        mac_address='string',
        timestamp=0
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_detail_v1(api, validator):
    try:
        assert is_valid_get_client_detail_v1(
            validator,
            get_client_detail_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_client_detail_v1_default_val(api):
    endpoint_result = api.clients.get_client_detail_v1(
        mac_address=None,
        timestamp=None
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_detail_v1_default_val(api, validator):
    try:
        assert is_valid_get_client_detail_v1(
            validator,
            get_client_detail_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_client_enrichment_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_991dfd2751065bfb8c2367dd726df316_v3_1_3_0').validate(obj)
    return True


def get_client_enrichment_details_v1(api):
    endpoint_result = api.clients.get_client_enrichment_details_v1(

    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_enrichment_details_v1(api, validator):
    try:
        assert is_valid_get_client_enrichment_details_v1(
            validator,
            get_client_enrichment_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_client_enrichment_details_v1_default_val(api):
    endpoint_result = api.clients.get_client_enrichment_details_v1(

    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_enrichment_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_client_enrichment_details_v1(
            validator,
            get_client_enrichment_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_overall_client_health_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f58ddf5cee095688aed79a9bb26e21e8_v3_1_3_0').validate(obj)
    return True


def get_overall_client_health_v1(api):
    endpoint_result = api.clients.get_overall_client_health_v1(
        timestamp=0
    )
    return endpoint_result


@pytest.mark.clients
def test_get_overall_client_health_v1(api, validator):
    try:
        assert is_valid_get_overall_client_health_v1(
            validator,
            get_overall_client_health_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_overall_client_health_v1_default_val(api):
    endpoint_result = api.clients.get_overall_client_health_v1(
        timestamp=None
    )
    return endpoint_result


@pytest.mark.clients
def test_get_overall_client_health_v1_default_val(api, validator):
    try:
        assert is_valid_get_overall_client_health_v1(
            validator,
            get_overall_client_health_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_client_proximity_v1(json_schema_validate, obj):
    json_schema_validate('jsd_23c141467ea25ec0aa91cbcaff070354_v3_1_3_0').validate(obj)
    return True


def client_proximity_v1(api):
    endpoint_result = api.clients.client_proximity_v1(
        number_days=0,
        time_resolution=0,
        username='string'
    )
    return endpoint_result


@pytest.mark.clients
def test_client_proximity_v1(api, validator):
    try:
        assert is_valid_client_proximity_v1(
            validator,
            client_proximity_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def client_proximity_v1_default_val(api):
    endpoint_result = api.clients.client_proximity_v1(
        number_days=None,
        time_resolution=None,
        username=None
    )
    return endpoint_result


@pytest.mark.clients
def test_client_proximity_v1_default_val(api, validator):
    try:
        assert is_valid_client_proximity_v1(
            validator,
            client_proximity_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI clients API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.6', reason='version does not match')


def is_valid_retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities(json_schema_validate, obj):
    json_schema_validate('jsd_dfcf64acc1815459acc146cd924e9877_v2_3_7_6').validate(obj)
    return True


def retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities(api):
    endpoint_result = api.clients.retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities(
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
def test_retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities(
            validator,
            retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_default_val(api):
    endpoint_result = api.clients.retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities(
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
def test_retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities(
            validator,
            retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_count_of_clients_by_applying_basic_filtering(json_schema_validate, obj):
    json_schema_validate('jsd_110ed18d78d455f9a51049a09ae12d48_v2_3_7_6').validate(obj)
    return True


def retrieves_the_total_count_of_clients_by_applying_basic_filtering(api):
    endpoint_result = api.clients.retrieves_the_total_count_of_clients_by_applying_basic_filtering(
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
def test_retrieves_the_total_count_of_clients_by_applying_basic_filtering(api, validator):
    try:
        assert is_valid_retrieves_the_total_count_of_clients_by_applying_basic_filtering(
            validator,
            retrieves_the_total_count_of_clients_by_applying_basic_filtering(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_count_of_clients_by_applying_basic_filtering_default_val(api):
    endpoint_result = api.clients.retrieves_the_total_count_of_clients_by_applying_basic_filtering(
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
def test_retrieves_the_total_count_of_clients_by_applying_basic_filtering_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_total_count_of_clients_by_applying_basic_filtering(
            validator,
            retrieves_the_total_count_of_clients_by_applying_basic_filtering_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes(json_schema_validate, obj):
    json_schema_validate('jsd_ea5f116c0cd152bbb4a92c043738ea57_v2_3_7_6').validate(obj)
    return True


def retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes(api):
    endpoint_result = api.clients.retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes(
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
def test_retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes(
            validator,
            retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_default_val(api):
    endpoint_result = api.clients.retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes(
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
def test_retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes(
            validator,
            retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_number_of_clients_by_applying_complex_filters(json_schema_validate, obj):
    json_schema_validate('jsd_1628a2131eae5c1d8e73cd55eebf6a83_v2_3_7_6').validate(obj)
    return True


def retrieves_the_number_of_clients_by_applying_complex_filters(api):
    endpoint_result = api.clients.retrieves_the_number_of_clients_by_applying_complex_filters(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 0}],
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_number_of_clients_by_applying_complex_filters(api, validator):
    try:
        assert is_valid_retrieves_the_number_of_clients_by_applying_complex_filters(
            validator,
            retrieves_the_number_of_clients_by_applying_complex_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_number_of_clients_by_applying_complex_filters_default_val(api):
    endpoint_result = api.clients.retrieves_the_number_of_clients_by_applying_complex_filters(
        active_validation=True,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_the_number_of_clients_by_applying_complex_filters_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_number_of_clients_by_applying_complex_filters(
            validator,
            retrieves_the_number_of_clients_by_applying_complex_filters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_summary_analytics_data_related_to_clients(json_schema_validate, obj):
    json_schema_validate('jsd_f210ff2d89425b4790ce56f19da7be92_v2_3_7_6').validate(obj)
    return True


def retrieves_summary_analytics_data_related_to_clients(api):
    endpoint_result = api.clients.retrieves_summary_analytics_data_related_to_clients(
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
def test_retrieves_summary_analytics_data_related_to_clients(api, validator):
    try:
        assert is_valid_retrieves_summary_analytics_data_related_to_clients(
            validator,
            retrieves_summary_analytics_data_related_to_clients(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_summary_analytics_data_related_to_clients_default_val(api):
    endpoint_result = api.clients.retrieves_summary_analytics_data_related_to_clients(
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
def test_retrieves_summary_analytics_data_related_to_clients_default_val(api, validator):
    try:
        assert is_valid_retrieves_summary_analytics_data_related_to_clients(
            validator,
            retrieves_summary_analytics_data_related_to_clients_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_top_n_analytics_data_related_to_clients(json_schema_validate, obj):
    json_schema_validate('jsd_0f44ddd3c38c5a9484f5cb4e125447bc_v2_3_7_6').validate(obj)
    return True


def retrieves_the_top_n_analytics_data_related_to_clients(api):
    endpoint_result = api.clients.retrieves_the_top_n_analytics_data_related_to_clients(
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
def test_retrieves_the_top_n_analytics_data_related_to_clients(api, validator):
    try:
        assert is_valid_retrieves_the_top_n_analytics_data_related_to_clients(
            validator,
            retrieves_the_top_n_analytics_data_related_to_clients(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_top_n_analytics_data_related_to_clients_default_val(api):
    endpoint_result = api.clients.retrieves_the_top_n_analytics_data_related_to_clients(
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
def test_retrieves_the_top_n_analytics_data_related_to_clients_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_top_n_analytics_data_related_to_clients(
            validator,
            retrieves_the_top_n_analytics_data_related_to_clients_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_trend_analytics_data_related_to_clients(json_schema_validate, obj):
    json_schema_validate('jsd_ffd2fefb57d5523c87a5d941eb93ddc3_v2_3_7_6').validate(obj)
    return True


def retrieves_the_trend_analytics_data_related_to_clients(api):
    endpoint_result = api.clients.retrieves_the_trend_analytics_data_related_to_clients(
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
def test_retrieves_the_trend_analytics_data_related_to_clients(api, validator):
    try:
        assert is_valid_retrieves_the_trend_analytics_data_related_to_clients(
            validator,
            retrieves_the_trend_analytics_data_related_to_clients(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_trend_analytics_data_related_to_clients_default_val(api):
    endpoint_result = api.clients.retrieves_the_trend_analytics_data_related_to_clients(
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
def test_retrieves_the_trend_analytics_data_related_to_clients_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_trend_analytics_data_related_to_clients(
            validator,
            retrieves_the_trend_analytics_data_related_to_clients_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_specific_client_information_matching_the_macaddress(json_schema_validate, obj):
    json_schema_validate('jsd_ee00176282fd54ef90fc96a2c23d50ec_v2_3_7_6').validate(obj)
    return True


def retrieves_specific_client_information_matching_the_macaddress(api):
    endpoint_result = api.clients.retrieves_specific_client_information_matching_the_macaddress(
        attribute='string',
        end_time=0,
        id='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_specific_client_information_matching_the_macaddress(api, validator):
    try:
        assert is_valid_retrieves_specific_client_information_matching_the_macaddress(
            validator,
            retrieves_specific_client_information_matching_the_macaddress(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_specific_client_information_matching_the_macaddress_default_val(api):
    endpoint_result = api.clients.retrieves_specific_client_information_matching_the_macaddress(
        attribute=None,
        end_time=None,
        id='string',
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.clients
def test_retrieves_specific_client_information_matching_the_macaddress_default_val(api, validator):
    try:
        assert is_valid_retrieves_specific_client_information_matching_the_macaddress(
            validator,
            retrieves_specific_client_information_matching_the_macaddress_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_specific_client_information_over_a_specified_period_of_time(json_schema_validate, obj):
    json_schema_validate('jsd_311806d9a13d575abdc26d485af708e7_v2_3_7_6').validate(obj)
    return True


def retrieves_specific_client_information_over_a_specified_period_of_time(api):
    endpoint_result = api.clients.retrieves_specific_client_information_over_a_specified_period_of_time(
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
def test_retrieves_specific_client_information_over_a_specified_period_of_time(api, validator):
    try:
        assert is_valid_retrieves_specific_client_information_over_a_specified_period_of_time(
            validator,
            retrieves_specific_client_information_over_a_specified_period_of_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_specific_client_information_over_a_specified_period_of_time_default_val(api):
    endpoint_result = api.clients.retrieves_specific_client_information_over_a_specified_period_of_time(
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
def test_retrieves_specific_client_information_over_a_specified_period_of_time_default_val(api, validator):
    try:
        assert is_valid_retrieves_specific_client_information_over_a_specified_period_of_time(
            validator,
            retrieves_specific_client_information_over_a_specified_period_of_time_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_client_detail(json_schema_validate, obj):
    json_schema_validate('jsd_f2c6333d8eb05491a16c2d32095e4352_v2_3_7_6').validate(obj)
    return True


def get_client_detail(api):
    endpoint_result = api.clients.get_client_detail(
        mac_address='string',
        timestamp=0
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_detail(api, validator):
    try:
        assert is_valid_get_client_detail(
            validator,
            get_client_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_client_detail_default_val(api):
    endpoint_result = api.clients.get_client_detail(
        mac_address=None,
        timestamp=None
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_detail_default_val(api, validator):
    try:
        assert is_valid_get_client_detail(
            validator,
            get_client_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_client_enrichment_details(json_schema_validate, obj):
    json_schema_validate('jsd_991dfd2751065bfb8c2367dd726df316_v2_3_7_6').validate(obj)
    return True


def get_client_enrichment_details(api):
    endpoint_result = api.clients.get_client_enrichment_details(

    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_enrichment_details(api, validator):
    try:
        assert is_valid_get_client_enrichment_details(
            validator,
            get_client_enrichment_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_client_enrichment_details_default_val(api):
    endpoint_result = api.clients.get_client_enrichment_details(

    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_enrichment_details_default_val(api, validator):
    try:
        assert is_valid_get_client_enrichment_details(
            validator,
            get_client_enrichment_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_overall_client_health(json_schema_validate, obj):
    json_schema_validate('jsd_f58ddf5cee095688aed79a9bb26e21e8_v2_3_7_6').validate(obj)
    return True


def get_overall_client_health(api):
    endpoint_result = api.clients.get_overall_client_health(
        timestamp=0
    )
    return endpoint_result


@pytest.mark.clients
def test_get_overall_client_health(api, validator):
    try:
        assert is_valid_get_overall_client_health(
            validator,
            get_overall_client_health(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_overall_client_health_default_val(api):
    endpoint_result = api.clients.get_overall_client_health(
        timestamp=None
    )
    return endpoint_result


@pytest.mark.clients
def test_get_overall_client_health_default_val(api, validator):
    try:
        assert is_valid_get_overall_client_health(
            validator,
            get_overall_client_health_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_client_proximity(json_schema_validate, obj):
    json_schema_validate('jsd_23c141467ea25ec0aa91cbcaff070354_v2_3_7_6').validate(obj)
    return True


def client_proximity(api):
    endpoint_result = api.clients.client_proximity(
        number_days=0,
        time_resolution=0,
        username='string'
    )
    return endpoint_result


@pytest.mark.clients
def test_client_proximity(api, validator):
    try:
        assert is_valid_client_proximity(
            validator,
            client_proximity(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def client_proximity_default_val(api):
    endpoint_result = api.clients.client_proximity(
        number_days=None,
        time_resolution=None,
        username=None
    )
    return endpoint_result


@pytest.mark.clients
def test_client_proximity_default_val(api, validator):
    try:
        assert is_valid_client_proximity(
            validator,
            client_proximity_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

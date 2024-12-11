# -*- coding: utf-8 -*-
"""CatalystCenterAPI devices API fixtures and tests.

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


def is_valid_retrieves_the_list_of_aaa_services_for_given_parameters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_61752607cc60533fba1ac9a077366acd_v2_3_7_9').validate(obj)
    return True


def retrieves_the_list_of_aaa_services_for_given_parameters_v1(api):
    endpoint_result = api.devices.retrieves_the_list_of_aaa_services_for_given_parameters_v1(
        device_id='string',
        device_name='string',
        device_site_hierarchy_id='string',
        end_time=0,
        limit=0,
        offset=0,
        order='string',
        server_ip='string',
        site_hierarchy='string',
        site_id='string',
        sort_by='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_list_of_aaa_services_for_given_parameters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_aaa_services_for_given_parameters_v1(
            validator,
            retrieves_the_list_of_aaa_services_for_given_parameters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_aaa_services_for_given_parameters_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_list_of_aaa_services_for_given_parameters_v1(
        device_id=None,
        device_name=None,
        device_site_hierarchy_id=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        server_ip=None,
        site_hierarchy=None,
        site_id=None,
        sort_by=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_list_of_aaa_services_for_given_parameters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_aaa_services_for_given_parameters_v1(
            validator,
            retrieves_the_list_of_aaa_services_for_given_parameters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_number_of_aaa_services_for_given_parameters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_527dd9685e1250c69fcc71fa7f766750_v2_3_7_9').validate(obj)
    return True


def retrieves_the_total_number_of_aaa_services_for_given_parameters_v1(api):
    endpoint_result = api.devices.retrieves_the_total_number_of_aaa_services_for_given_parameters_v1(
        device_id='string',
        device_name='string',
        device_site_hierarchy='string',
        device_site_hierarchy_id='string',
        device_site_id='string',
        end_time=0,
        server_ip='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_total_number_of_aaa_services_for_given_parameters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_aaa_services_for_given_parameters_v1(
            validator,
            retrieves_the_total_number_of_aaa_services_for_given_parameters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_number_of_aaa_services_for_given_parameters_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_total_number_of_aaa_services_for_given_parameters_v1(
        device_id=None,
        device_name=None,
        device_site_hierarchy=None,
        device_site_hierarchy_id=None,
        device_site_id=None,
        end_time=None,
        server_ip=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_total_number_of_aaa_services_for_given_parameters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_aaa_services_for_given_parameters_v1(
            validator,
            retrieves_the_total_number_of_aaa_services_for_given_parameters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_aaa_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_74544111f24a5ad5bf03fe236dd96dcb_v2_3_7_9').validate(obj)
    return True


def retrieves_the_list_of_aaa_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.retrieves_the_list_of_aaa_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': ['string']}],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_list_of_aaa_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_aaa_services_for_given_set_of_complex_filters_v1(
            validator,
            retrieves_the_list_of_aaa_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_list_of_aaa_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_list_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_aaa_services_for_given_set_of_complex_filters_v1(
            validator,
            retrieves_the_list_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_912544adfc115d6888722b71811ac96e_v2_3_7_9').validate(obj)
    return True


def retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': ['string']}],
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters_v1(
            validator,
            retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters_v1(
            validator,
            retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_summary_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7d54c40ecb5f531cb5a78d0cd5dd585e_v2_3_7_9').validate(obj)
    return True


def get_summary_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.get_summary_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'function': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_summary_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_get_summary_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(
            validator,
            get_summary_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_summary_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.get_summary_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(
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


@pytest.mark.devices
def test_get_summary_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_summary_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(
            validator,
            get_summary_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_top_n_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bdca1829ea705fa690922e3e0f8ff7b0_v2_3_7_9').validate(obj)
    return True


def get_top_n_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.get_top_n_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'function': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0,
        topN=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_top_n_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_get_top_n_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(
            validator,
            get_top_n_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_top_n_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.get_top_n_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(
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


@pytest.mark.devices
def test_get_top_n_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_top_n_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(
            validator,
            get_top_n_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trend_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c60312a923ee5a6fb3f2c725c32dc96f_v2_3_7_9').validate(obj)
    return True


def get_trend_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.get_trend_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'timestampOrder': 'string'},
        payload=None,
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_trend_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(
            validator,
            get_trend_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trend_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.get_trend_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(
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


@pytest.mark.devices
def test_get_trend_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1(
            validator,
            get_trend_analytics_data_of_aaa_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_details_of_a_specific_aaa_service_matching_the_id_of_the_service_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7509508a5f075784aa6b582aa9a24901_v2_3_7_9').validate(obj)
    return True


def retrieves_the_details_of_a_specific_aaa_service_matching_the_id_of_the_service_v1(api):
    endpoint_result = api.devices.retrieves_the_details_of_a_specific_aaa_service_matching_the_id_of_the_service_v1(
        end_time=0,
        id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_details_of_a_specific_aaa_service_matching_the_id_of_the_service_v1(api, validator):
    try:
        assert is_valid_retrieves_the_details_of_a_specific_aaa_service_matching_the_id_of_the_service_v1(
            validator,
            retrieves_the_details_of_a_specific_aaa_service_matching_the_id_of_the_service_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_details_of_a_specific_aaa_service_matching_the_id_of_the_service_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_details_of_a_specific_aaa_service_matching_the_id_of_the_service_v1(
        end_time=None,
        id='string',
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_details_of_a_specific_aaa_service_matching_the_id_of_the_service_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_details_of_a_specific_aaa_service_matching_the_id_of_the_service_v1(
            validator,
            retrieves_the_details_of_a_specific_aaa_service_matching_the_id_of_the_service_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trend_analytics_data_for_a_given_aaa_service_matching_the_id_of_the_service_v1(json_schema_validate, obj):
    json_schema_validate('jsd_34f33d768d01586c9133b155da5e5ade_v2_3_7_9').validate(obj)
    return True


def get_trend_analytics_data_for_a_given_aaa_service_matching_the_id_of_the_service_v1(api):
    endpoint_result = api.devices.get_trend_analytics_data_for_a_given_aaa_service_matching_the_id_of_the_service_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}],
        groupBy=['string'],
        id='string',
        page={'limit': 0, 'offset': 0, 'timestampOrder': 'string'},
        payload=None,
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_trend_analytics_data_for_a_given_aaa_service_matching_the_id_of_the_service_v1(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_for_a_given_aaa_service_matching_the_id_of_the_service_v1(
            validator,
            get_trend_analytics_data_for_a_given_aaa_service_matching_the_id_of_the_service_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trend_analytics_data_for_a_given_aaa_service_matching_the_id_of_the_service_v1_default_val(api):
    endpoint_result = api.devices.get_trend_analytics_data_for_a_given_aaa_service_matching_the_id_of_the_service_v1(
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


@pytest.mark.devices
def test_get_trend_analytics_data_for_a_given_aaa_service_matching_the_id_of_the_service_v1_default_val(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_for_a_given_aaa_service_matching_the_id_of_the_service_v1(
            validator,
            get_trend_analytics_data_for_a_given_aaa_service_matching_the_id_of_the_service_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_assurance_events_v1(json_schema_validate, obj):
    json_schema_validate('jsd_99114bc891de5102872b3415d23b7a0b_v2_3_7_9').validate(obj)
    return True


def query_assurance_events_v1(api):
    endpoint_result = api.devices.query_assurance_events_v1(
        ap_mac='string',
        attribute='string',
        client_mac='string',
        device_family='string',
        end_time=0,
        limit=0,
        message_type='string',
        network_device_id='string',
        network_device_name='string',
        offset=0,
        order='string',
        severity=0,
        site_hierarchy_id='string',
        site_id='string',
        sort_by='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_query_assurance_events_v1(api, validator):
    try:
        assert is_valid_query_assurance_events_v1(
            validator,
            query_assurance_events_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def query_assurance_events_v1_default_val(api):
    endpoint_result = api.devices.query_assurance_events_v1(
        ap_mac=None,
        attribute=None,
        client_mac=None,
        device_family=None,
        end_time=None,
        limit=None,
        message_type=None,
        network_device_id=None,
        network_device_name=None,
        offset=None,
        order=None,
        severity=None,
        site_hierarchy_id=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.devices
def test_query_assurance_events_v1_default_val(api, validator):
    try:
        assert is_valid_query_assurance_events_v1(
            validator,
            query_assurance_events_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_the_number_of_events_v1(json_schema_validate, obj):
    json_schema_validate('jsd_915abf597583520eb0a7a0b24e5c7f69_v2_3_7_9').validate(obj)
    return True


def count_the_number_of_events_v1(api):
    endpoint_result = api.devices.count_the_number_of_events_v1(
        ap_mac='string',
        client_mac='string',
        device_family='string',
        end_time='string',
        message_type='string',
        network_device_id='string',
        network_device_name='string',
        severity='string',
        site_hierarchy_id='string',
        site_id='string',
        start_time='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_count_the_number_of_events_v1(api, validator):
    try:
        assert is_valid_count_the_number_of_events_v1(
            validator,
            count_the_number_of_events_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_the_number_of_events_v1_default_val(api):
    endpoint_result = api.devices.count_the_number_of_events_v1(
        ap_mac=None,
        client_mac=None,
        device_family=None,
        end_time=None,
        message_type=None,
        network_device_id=None,
        network_device_name=None,
        severity=None,
        site_hierarchy_id=None,
        site_id=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_count_the_number_of_events_v1_default_val(api, validator):
    try:
        assert is_valid_count_the_number_of_events_v1(
            validator,
            count_the_number_of_events_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_assurance_events_with_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ef94c2c20ba15fd38e129ac75067de1e_v2_3_7_9').validate(obj)
    return True


def query_assurance_events_with_filters_v1(api):
    endpoint_result = api.devices.query_assurance_events_with_filters_v1(
        active_validation=True,
        attributes=['string'],
        deviceFamily=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        page={'offset': 0, 'limit': 0, 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0,
        views=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_query_assurance_events_with_filters_v1(api, validator):
    try:
        assert is_valid_query_assurance_events_with_filters_v1(
            validator,
            query_assurance_events_with_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def query_assurance_events_with_filters_v1_default_val(api):
    endpoint_result = api.devices.query_assurance_events_with_filters_v1(
        active_validation=True,
        attributes=None,
        deviceFamily=None,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None,
        views=None
    )
    return endpoint_result


@pytest.mark.devices
def test_query_assurance_events_with_filters_v1_default_val(api, validator):
    try:
        assert is_valid_query_assurance_events_with_filters_v1(
            validator,
            query_assurance_events_with_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_the_number_of_events_with_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a91eed12dfc85dbdaacab22e6e9f04a5_v2_3_7_9').validate(obj)
    return True


def count_the_number_of_events_with_filters_v1(api):
    endpoint_result = api.devices.count_the_number_of_events_with_filters_v1(
        active_validation=True,
        deviceFamily=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_count_the_number_of_events_with_filters_v1(api, validator):
    try:
        assert is_valid_count_the_number_of_events_with_filters_v1(
            validator,
            count_the_number_of_events_with_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_the_number_of_events_with_filters_v1_default_val(api):
    endpoint_result = api.devices.count_the_number_of_events_with_filters_v1(
        active_validation=True,
        deviceFamily=None,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.devices
def test_count_the_number_of_events_with_filters_v1_default_val(api, validator):
    try:
        assert is_valid_count_the_number_of_events_with_filters_v1(
            validator,
            count_the_number_of_events_with_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_details_of_a_single_assurance_event_v1(json_schema_validate, obj):
    json_schema_validate('jsd_031a36092e78528b9bd8730c93b5412d_v2_3_7_9').validate(obj)
    return True


def get_details_of_a_single_assurance_event_v1(api):
    endpoint_result = api.devices.get_details_of_a_single_assurance_event_v1(
        attribute='string',
        id='string',
        view='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_details_of_a_single_assurance_event_v1(api, validator):
    try:
        assert is_valid_get_details_of_a_single_assurance_event_v1(
            validator,
            get_details_of_a_single_assurance_event_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_details_of_a_single_assurance_event_v1_default_val(api):
    endpoint_result = api.devices.get_details_of_a_single_assurance_event_v1(
        attribute=None,
        id='string',
        view=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_details_of_a_single_assurance_event_v1_default_val(api, validator):
    try:
        assert is_valid_get_details_of_a_single_assurance_event_v1(
            validator,
            get_details_of_a_single_assurance_event_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_list_of_child_events_for_the_given_wireless_client_event_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d3cf1ace30895351b5b8c3f7919b972e_v2_3_7_9').validate(obj)
    return True


def get_list_of_child_events_for_the_given_wireless_client_event_v1(api):
    endpoint_result = api.devices.get_list_of_child_events_for_the_given_wireless_client_event_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_list_of_child_events_for_the_given_wireless_client_event_v1(api, validator):
    try:
        assert is_valid_get_list_of_child_events_for_the_given_wireless_client_event_v1(
            validator,
            get_list_of_child_events_for_the_given_wireless_client_event_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_list_of_child_events_for_the_given_wireless_client_event_v1_default_val(api):
    endpoint_result = api.devices.get_list_of_child_events_for_the_given_wireless_client_event_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_list_of_child_events_for_the_given_wireless_client_event_v1_default_val(api, validator):
    try:
        assert is_valid_get_list_of_child_events_for_the_given_wireless_client_event_v1(
            validator,
            get_list_of_child_events_for_the_given_wireless_client_event_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_d_h_c_p_services_for_given_parameters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d9a96f4107695eec9ce303b039ed4747_v2_3_7_9').validate(obj)
    return True


def retrieves_the_list_of_d_h_c_p_services_for_given_parameters_v1(api):
    endpoint_result = api.devices.retrieves_the_list_of_d_h_c_p_services_for_given_parameters_v1(
        device_id='string',
        device_name='string',
        device_site_hierarchy='string',
        device_site_hierarchy_id='string',
        device_site_id='string',
        end_time=0,
        limit=0,
        offset=0,
        order='string',
        server_ip='string',
        sort_by='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_list_of_d_h_c_p_services_for_given_parameters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_d_h_c_p_services_for_given_parameters_v1(
            validator,
            retrieves_the_list_of_d_h_c_p_services_for_given_parameters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_d_h_c_p_services_for_given_parameters_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_list_of_d_h_c_p_services_for_given_parameters_v1(
        device_id=None,
        device_name=None,
        device_site_hierarchy=None,
        device_site_hierarchy_id=None,
        device_site_id=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        server_ip=None,
        sort_by=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_list_of_d_h_c_p_services_for_given_parameters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_d_h_c_p_services_for_given_parameters_v1(
            validator,
            retrieves_the_list_of_d_h_c_p_services_for_given_parameters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_number_of_d_h_c_p_services_for_given_parameters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_cf3eff4f30ab56ef8e4cad0be8bac653_v2_3_7_9').validate(obj)
    return True


def retrieves_the_total_number_of_d_h_c_p_services_for_given_parameters_v1(api):
    endpoint_result = api.devices.retrieves_the_total_number_of_d_h_c_p_services_for_given_parameters_v1(
        device_id='string',
        device_name='string',
        device_site_hierarchy='string',
        device_site_hierarchy_id='string',
        device_site_id='string',
        end_time=0,
        server_ip='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_total_number_of_d_h_c_p_services_for_given_parameters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_d_h_c_p_services_for_given_parameters_v1(
            validator,
            retrieves_the_total_number_of_d_h_c_p_services_for_given_parameters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_number_of_d_h_c_p_services_for_given_parameters_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_total_number_of_d_h_c_p_services_for_given_parameters_v1(
        device_id=None,
        device_name=None,
        device_site_hierarchy=None,
        device_site_hierarchy_id=None,
        device_site_id=None,
        end_time=None,
        server_ip=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_total_number_of_d_h_c_p_services_for_given_parameters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_d_h_c_p_services_for_given_parameters_v1(
            validator,
            retrieves_the_total_number_of_d_h_c_p_services_for_given_parameters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e6c22549e5145c4892d0bd3b97614e07_v2_3_7_9').validate(obj)
    return True


def retrieves_the_list_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.retrieves_the_list_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': ['string']}],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_list_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
            validator,
            retrieves_the_list_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_list_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_list_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
            validator,
            retrieves_the_list_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_number_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_afcd4a0cbe985fd7aafa73d671c43a1e_v2_3_7_9').validate(obj)
    return True


def retrieves_the_total_number_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.retrieves_the_total_number_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': ['string']}],
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_total_number_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
            validator,
            retrieves_the_total_number_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_number_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_total_number_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_total_number_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
            validator,
            retrieves_the_total_number_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_summary_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a3fb2e7bb8aa50508425b1dd8818fda4_v2_3_7_9').validate(obj)
    return True


def get_summary_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.get_summary_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': [{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}]}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'function': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_summary_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_get_summary_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
            validator,
            get_summary_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_summary_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.get_summary_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
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


@pytest.mark.devices
def test_get_summary_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_summary_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
            validator,
            get_summary_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_top_n_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_edf997bb4bcc5dd6baca80647d8a47ce_v2_3_7_9').validate(obj)
    return True


def get_top_n_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.get_top_n_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'function': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0,
        topN=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_top_n_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_get_top_n_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
            validator,
            get_top_n_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_top_n_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.get_top_n_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
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


@pytest.mark.devices
def test_get_top_n_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_top_n_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
            validator,
            get_top_n_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trend_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_58d58baa26bd5a6d9c461592c872d515_v2_3_7_9').validate(obj)
    return True


def get_trend_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.get_trend_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'timestampOrder': 'string'},
        payload=None,
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_trend_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
            validator,
            get_trend_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trend_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.get_trend_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
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


@pytest.mark.devices
def test_get_trend_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1(
            validator,
            get_trend_analytics_data_of_d_h_c_p_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_details_of_a_specific_d_h_c_p_service_matching_the_id_of_the_service_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b5e7fa71240f5e669c902db27de09860_v2_3_7_9').validate(obj)
    return True


def retrieves_the_details_of_a_specific_d_h_c_p_service_matching_the_id_of_the_service_v1(api):
    endpoint_result = api.devices.retrieves_the_details_of_a_specific_d_h_c_p_service_matching_the_id_of_the_service_v1(
        end_time=0,
        id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_details_of_a_specific_d_h_c_p_service_matching_the_id_of_the_service_v1(api, validator):
    try:
        assert is_valid_retrieves_the_details_of_a_specific_d_h_c_p_service_matching_the_id_of_the_service_v1(
            validator,
            retrieves_the_details_of_a_specific_d_h_c_p_service_matching_the_id_of_the_service_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_details_of_a_specific_d_h_c_p_service_matching_the_id_of_the_service_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_details_of_a_specific_d_h_c_p_service_matching_the_id_of_the_service_v1(
        end_time=None,
        id='string',
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_details_of_a_specific_d_h_c_p_service_matching_the_id_of_the_service_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_details_of_a_specific_d_h_c_p_service_matching_the_id_of_the_service_v1(
            validator,
            retrieves_the_details_of_a_specific_d_h_c_p_service_matching_the_id_of_the_service_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trend_analytics_data_for_a_given_d_h_c_p_service_matching_the_id_of_the_service_v1(json_schema_validate, obj):
    json_schema_validate('jsd_597eb1227bb250799b6ca76ed4bee9d9_v2_3_7_9').validate(obj)
    return True


def get_trend_analytics_data_for_a_given_d_h_c_p_service_matching_the_id_of_the_service_v1(api):
    endpoint_result = api.devices.get_trend_analytics_data_for_a_given_d_h_c_p_service_matching_the_id_of_the_service_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}],
        groupBy=['string'],
        id='string',
        page={'limit': 0, 'offset': 0, 'timestampOrder': 'string'},
        payload=None,
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_trend_analytics_data_for_a_given_d_h_c_p_service_matching_the_id_of_the_service_v1(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_for_a_given_d_h_c_p_service_matching_the_id_of_the_service_v1(
            validator,
            get_trend_analytics_data_for_a_given_d_h_c_p_service_matching_the_id_of_the_service_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trend_analytics_data_for_a_given_d_h_c_p_service_matching_the_id_of_the_service_v1_default_val(api):
    endpoint_result = api.devices.get_trend_analytics_data_for_a_given_d_h_c_p_service_matching_the_id_of_the_service_v1(
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


@pytest.mark.devices
def test_get_trend_analytics_data_for_a_given_d_h_c_p_service_matching_the_id_of_the_service_v1_default_val(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_for_a_given_d_h_c_p_service_matching_the_id_of_the_service_v1(
            validator,
            get_trend_analytics_data_for_a_given_d_h_c_p_service_matching_the_id_of_the_service_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_d_n_s_services_for_given_parameters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e71b7fc7245755ec8be93800d32738a8_v2_3_7_9').validate(obj)
    return True


def retrieves_the_list_of_d_n_s_services_for_given_parameters_v1(api):
    endpoint_result = api.devices.retrieves_the_list_of_d_n_s_services_for_given_parameters_v1(
        device_id='string',
        device_site_hierarchy_id='string',
        device_site_id='string',
        end_time=0,
        limit=0,
        offset=0,
        order='string',
        server_ip='string',
        sort_by='string',
        ssid='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_list_of_d_n_s_services_for_given_parameters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_d_n_s_services_for_given_parameters_v1(
            validator,
            retrieves_the_list_of_d_n_s_services_for_given_parameters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_d_n_s_services_for_given_parameters_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_list_of_d_n_s_services_for_given_parameters_v1(
        device_id=None,
        device_site_hierarchy_id=None,
        device_site_id=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        server_ip=None,
        sort_by=None,
        ssid=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_list_of_d_n_s_services_for_given_parameters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_d_n_s_services_for_given_parameters_v1(
            validator,
            retrieves_the_list_of_d_n_s_services_for_given_parameters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_number_of_d_n_s_services_for_given_parameters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_16818199b1b7509cb0f7dc3d0a04479f_v2_3_7_9').validate(obj)
    return True


def retrieves_the_total_number_of_d_n_s_services_for_given_parameters_v1(api):
    endpoint_result = api.devices.retrieves_the_total_number_of_d_n_s_services_for_given_parameters_v1(
        device_id='string',
        device_site_hierarchy_id='string',
        device_site_id='string',
        end_time=0,
        server_ip='string',
        ssid='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_total_number_of_d_n_s_services_for_given_parameters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_d_n_s_services_for_given_parameters_v1(
            validator,
            retrieves_the_total_number_of_d_n_s_services_for_given_parameters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_number_of_d_n_s_services_for_given_parameters_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_total_number_of_d_n_s_services_for_given_parameters_v1(
        device_id=None,
        device_site_hierarchy_id=None,
        device_site_id=None,
        end_time=None,
        server_ip=None,
        ssid=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_total_number_of_d_n_s_services_for_given_parameters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_d_n_s_services_for_given_parameters_v1(
            validator,
            retrieves_the_total_number_of_d_n_s_services_for_given_parameters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_d_n_s_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0af7031cc5ca5b44af0e6454d558412c_v2_3_7_9').validate(obj)
    return True


def retrieves_the_list_of_d_n_s_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.retrieves_the_list_of_d_n_s_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': ['string']}],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_list_of_d_n_s_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_d_n_s_services_for_given_set_of_complex_filters_v1(
            validator,
            retrieves_the_list_of_d_n_s_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_list_of_d_n_s_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_list_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_d_n_s_services_for_given_set_of_complex_filters_v1(
            validator,
            retrieves_the_list_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_number_of_d_n_s_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9d10535ed2045b9bb5c58882e6f43cb2_v2_3_7_9').validate(obj)
    return True


def retrieves_the_total_number_of_d_n_s_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.retrieves_the_total_number_of_d_n_s_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': ['string']}],
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_total_number_of_d_n_s_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_d_n_s_services_for_given_set_of_complex_filters_v1(
            validator,
            retrieves_the_total_number_of_d_n_s_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_number_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_total_number_of_d_n_s_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_total_number_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_d_n_s_services_for_given_set_of_complex_filters_v1(
            validator,
            retrieves_the_total_number_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_summary_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_70358e9c5c3e5515a2e1b2cdee6928ab_v2_3_7_9').validate(obj)
    return True


def get_summary_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.get_summary_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': [{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}]}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'function': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_summary_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_get_summary_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(
            validator,
            get_summary_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_summary_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.get_summary_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(
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


@pytest.mark.devices
def test_get_summary_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_summary_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(
            validator,
            get_summary_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_top_n_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b43e0f60e9ac5bd4960f9772cf7a497b_v2_3_7_9').validate(obj)
    return True


def get_top_n_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.get_top_n_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'function': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0,
        topN=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_top_n_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_get_top_n_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(
            validator,
            get_top_n_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_top_n_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.get_top_n_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(
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


@pytest.mark.devices
def test_get_top_n_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_top_n_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(
            validator,
            get_top_n_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trend_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a837b8a46cd459c8b429d16fb17f1370_v2_3_7_9').validate(obj)
    return True


def get_trend_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(api):
    endpoint_result = api.devices.get_trend_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'timestampOrder': 'string'},
        payload=None,
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_trend_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(
            validator,
            get_trend_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trend_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api):
    endpoint_result = api.devices.get_trend_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(
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


@pytest.mark.devices
def test_get_trend_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1(
            validator,
            get_trend_analytics_data_of_d_n_s_services_for_given_set_of_complex_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_details_of_a_specific_d_n_s_service_matching_the_id_of_the_service_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d6e70722df04553c9806af12c6d097db_v2_3_7_9').validate(obj)
    return True


def retrieves_the_details_of_a_specific_d_n_s_service_matching_the_id_of_the_service_v1(api):
    endpoint_result = api.devices.retrieves_the_details_of_a_specific_d_n_s_service_matching_the_id_of_the_service_v1(
        end_time=0,
        id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_details_of_a_specific_d_n_s_service_matching_the_id_of_the_service_v1(api, validator):
    try:
        assert is_valid_retrieves_the_details_of_a_specific_d_n_s_service_matching_the_id_of_the_service_v1(
            validator,
            retrieves_the_details_of_a_specific_d_n_s_service_matching_the_id_of_the_service_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_details_of_a_specific_d_n_s_service_matching_the_id_of_the_service_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_details_of_a_specific_d_n_s_service_matching_the_id_of_the_service_v1(
        end_time=None,
        id='string',
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_details_of_a_specific_d_n_s_service_matching_the_id_of_the_service_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_details_of_a_specific_d_n_s_service_matching_the_id_of_the_service_v1(
            validator,
            retrieves_the_details_of_a_specific_d_n_s_service_matching_the_id_of_the_service_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trend_analytics_data_for_a_given_d_n_s_service_matching_the_id_of_the_service_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5f1debbfd4775faba3779c513181dfbf_v2_3_7_9').validate(obj)
    return True


def get_trend_analytics_data_for_a_given_d_n_s_service_matching_the_id_of_the_service_v1(api):
    endpoint_result = api.devices.get_trend_analytics_data_for_a_given_d_n_s_service_matching_the_id_of_the_service_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}],
        groupBy=['string'],
        id='string',
        page={'limit': 0, 'offset': 0, 'timestampOrder': 'string'},
        payload=None,
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_trend_analytics_data_for_a_given_d_n_s_service_matching_the_id_of_the_service_v1(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_for_a_given_d_n_s_service_matching_the_id_of_the_service_v1(
            validator,
            get_trend_analytics_data_for_a_given_d_n_s_service_matching_the_id_of_the_service_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trend_analytics_data_for_a_given_d_n_s_service_matching_the_id_of_the_service_v1_default_val(api):
    endpoint_result = api.devices.get_trend_analytics_data_for_a_given_d_n_s_service_matching_the_id_of_the_service_v1(
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


@pytest.mark.devices
def test_get_trend_analytics_data_for_a_given_d_n_s_service_matching_the_id_of_the_service_v1_default_val(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_for_a_given_d_n_s_service_matching_the_id_of_the_service_v1(
            validator,
            get_trend_analytics_data_for_a_given_d_n_s_service_matching_the_id_of_the_service_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_interfaces_along_with_statistics_and_poe_data_from_all_network_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1912fc7a61a854f2b2015d3f1c059ce9_v2_3_7_9').validate(obj)
    return True


def gets_interfaces_along_with_statistics_and_poe_data_from_all_network_devices_v1(api):
    endpoint_result = api.devices.gets_interfaces_along_with_statistics_and_poe_data_from_all_network_devices_v1(
        attribute='string',
        end_time=0,
        interface_id='string',
        interface_name='string',
        limit=0,
        network_device_id='string',
        network_device_ip_address='string',
        network_device_mac_address='string',
        offset=0,
        order='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        sort_by='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_interfaces_along_with_statistics_and_poe_data_from_all_network_devices_v1(api, validator):
    try:
        assert is_valid_gets_interfaces_along_with_statistics_and_poe_data_from_all_network_devices_v1(
            validator,
            gets_interfaces_along_with_statistics_and_poe_data_from_all_network_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_interfaces_along_with_statistics_and_poe_data_from_all_network_devices_v1_default_val(api):
    endpoint_result = api.devices.gets_interfaces_along_with_statistics_and_poe_data_from_all_network_devices_v1(
        attribute=None,
        end_time=None,
        interface_id=None,
        interface_name=None,
        limit=None,
        network_device_id=None,
        network_device_ip_address=None,
        network_device_mac_address=None,
        offset=None,
        order=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_interfaces_along_with_statistics_and_poe_data_from_all_network_devices_v1_default_val(api, validator):
    try:
        assert is_valid_gets_interfaces_along_with_statistics_and_poe_data_from_all_network_devices_v1(
            validator,
            gets_interfaces_along_with_statistics_and_poe_data_from_all_network_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_412775760f4b503bbce76ebb802f0ad7_v2_3_7_9').validate(obj)
    return True


def gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_v1(api):
    endpoint_result = api.devices.gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_v1(
        end_time=0,
        interface_id='string',
        interface_name='string',
        network_device_id='string',
        network_device_ip_address='string',
        network_device_mac_address='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_v1(api, validator):
    try:
        assert is_valid_gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_v1(
            validator,
            gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_v1_default_val(api):
    endpoint_result = api.devices.gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_v1(
        end_time=None,
        interface_id=None,
        interface_name=None,
        network_device_id=None,
        network_device_ip_address=None,
        network_device_mac_address=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_v1_default_val(api, validator):
    try:
        assert is_valid_gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_v1(
            validator,
            gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f667322836d5527482ad2100bec7feb4_v2_3_7_9').validate(obj)
    return True


def gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(api):
    endpoint_result = api.devices.gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': [{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}]}],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0,
        views=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(api, validator):
    try:
        assert is_valid_gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
            validator,
            gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1_default_val(api):
    endpoint_result = api.devices.gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
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


@pytest.mark.devices
def test_gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1_default_val(api, validator):
    try:
        assert is_valid_gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
            validator,
            gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_the_total_interfaces_count_across_the_network_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b0b146a144a65aa296b8b939c2926158_v2_3_7_9').validate(obj)
    return True


def the_total_interfaces_count_across_the_network_devices_v1(api):
    endpoint_result = api.devices.the_total_interfaces_count_across_the_network_devices_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0,
        views=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_the_total_interfaces_count_across_the_network_devices_v1(api, validator):
    try:
        assert is_valid_the_total_interfaces_count_across_the_network_devices_v1(
            validator,
            the_total_interfaces_count_across_the_network_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def the_total_interfaces_count_across_the_network_devices_v1_default_val(api):
    endpoint_result = api.devices.the_total_interfaces_count_across_the_network_devices_v1(
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


@pytest.mark.devices
def test_the_total_interfaces_count_across_the_network_devices_v1_default_val(api, validator):
    try:
        assert is_valid_the_total_interfaces_count_across_the_network_devices_v1(
            validator,
            the_total_interfaces_count_across_the_network_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_and_poe_data_v1(json_schema_validate, obj):
    json_schema_validate('jsd_56adcdf890505770af113b18b30c1b5f_v2_3_7_9').validate(obj)
    return True


def get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_and_poe_data_v1(api):
    endpoint_result = api.devices.get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_and_poe_data_v1(
        attribute='string',
        end_time=0,
        id='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_and_poe_data_v1(api, validator):
    try:
        assert is_valid_get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_and_poe_data_v1(
            validator,
            get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_and_poe_data_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_and_poe_data_v1_default_val(api):
    endpoint_result = api.devices.get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_and_poe_data_v1(
        attribute=None,
        end_time=None,
        id='string',
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_and_poe_data_v1_default_val(api, validator):
    try:
        assert is_valid_get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_and_poe_data_v1(
            validator,
            get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_and_poe_data_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2014b9be51e25efc9f41d4f68451f9a6_v2_3_7_9').validate(obj)
    return True


def the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range_v1(api):
    endpoint_result = api.devices.the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        id='string',
        payload=None,
        startTime=0,
        timestampOrder='string',
        trendIntervalInMinutes=0
    )
    return endpoint_result


@pytest.mark.devices
def test_the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range_v1(api, validator):
    try:
        assert is_valid_the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range_v1(
            validator,
            the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range_v1_default_val(api):
    endpoint_result = api.devices.the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range_v1(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        id='string',
        payload=None,
        startTime=None,
        timestampOrder=None,
        trendIntervalInMinutes=None
    )
    return endpoint_result


@pytest.mark.devices
def test_the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range_v1_default_val(api, validator):
    try:
        assert is_valid_the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range_v1(
            validator,
            the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_network_device_details_based_on_the_provided_query_parameters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_71c7314fc7e15dab859eb66f45b1e95a_v2_3_7_9').validate(obj)
    return True


def gets_the_network_device_details_based_on_the_provided_query_parameters_v1(api):
    endpoint_result = api.devices.gets_the_network_device_details_based_on_the_provided_query_parameters_v1(
        attribute='string',
        end_time=0,
        fabric_role='string',
        fabric_site_id='string',
        family='string',
        health_score='string',
        id='string',
        l2_vn='string',
        l3_vn='string',
        limit=0,
        mac_address='string',
        maintenance_mode=True,
        management_ip_address='string',
        offset=0,
        order='string',
        role='string',
        serial_number='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        software_version='string',
        sort_by='string',
        start_time=0,
        transit_network_id='string',
        type='string',
        view='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_network_device_details_based_on_the_provided_query_parameters_v1(api, validator):
    try:
        assert is_valid_gets_the_network_device_details_based_on_the_provided_query_parameters_v1(
            validator,
            gets_the_network_device_details_based_on_the_provided_query_parameters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_network_device_details_based_on_the_provided_query_parameters_v1_default_val(api):
    endpoint_result = api.devices.gets_the_network_device_details_based_on_the_provided_query_parameters_v1(
        attribute=None,
        end_time=None,
        fabric_role=None,
        fabric_site_id=None,
        family=None,
        health_score=None,
        id=None,
        l2_vn=None,
        l3_vn=None,
        limit=None,
        mac_address=None,
        maintenance_mode=None,
        management_ip_address=None,
        offset=None,
        order=None,
        role=None,
        serial_number=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        software_version=None,
        sort_by=None,
        start_time=None,
        transit_network_id=None,
        type=None,
        view=None
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_network_device_details_based_on_the_provided_query_parameters_v1_default_val(api, validator):
    try:
        assert is_valid_gets_the_network_device_details_based_on_the_provided_query_parameters_v1(
            validator,
            gets_the_network_device_details_based_on_the_provided_query_parameters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3d8782f4d285506d9e1391f0190ff738_v2_3_7_9').validate(obj)
    return True


def gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1(api):
    endpoint_result = api.devices.gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1(
        end_time=0,
        fabric_role='string',
        fabric_site_id='string',
        family='string',
        health_score='string',
        id='string',
        l2_vn='string',
        l3_vn='string',
        mac_address='string',
        maintenance_mode=True,
        management_ip_address='string',
        role='string',
        serial_number='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        software_version='string',
        start_time=0,
        transit_network_id='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1(api, validator):
    try:
        assert is_valid_gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1(
            validator,
            gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1_default_val(api):
    endpoint_result = api.devices.gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1(
        end_time=None,
        fabric_role=None,
        fabric_site_id=None,
        family=None,
        health_score=None,
        id=None,
        l2_vn=None,
        l3_vn=None,
        mac_address=None,
        maintenance_mode=None,
        management_ip_address=None,
        role=None,
        serial_number=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        software_version=None,
        start_time=None,
        transit_network_id=None,
        type=None
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1_default_val(api, validator):
    try:
        assert is_valid_gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1(
            validator,
            gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8bd1c59e9be75ac4a40decaa95ee9efd_v2_3_7_9').validate(obj)
    return True


def gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(api):
    endpoint_result = api.devices.gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        page={'limit': 0, 'offset': 0, 'count': 0, 'sortBy': 'string'},
        payload=None,
        startTime=0,
        views=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(api, validator):
    try:
        assert is_valid_gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
            validator,
            gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1_default_val(api):
    endpoint_result = api.devices.gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
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


@pytest.mark.devices
def test_gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1_default_val(api, validator):
    try:
        assert is_valid_gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
            validator,
            gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d05c763ada545fbe94a4c0391456b89f_v2_3_7_9').validate(obj)
    return True


def gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(api):
    endpoint_result = api.devices.gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(api, validator):
    try:
        assert is_valid_gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
            validator,
            gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1_default_val(api):
    endpoint_result = api.devices.gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
        active_validation=True,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1_default_val(api, validator):
    try:
        assert is_valid_gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
            validator,
            gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_summary_analytics_data_related_to_network_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_06bb7c52e5225e9398a006fecf4da06f_v2_3_7_9').validate(obj)
    return True


def gets_the_summary_analytics_data_related_to_network_devices_v1(api):
    endpoint_result = api.devices.gets_the_summary_analytics_data_related_to_network_devices_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_summary_analytics_data_related_to_network_devices_v1(api, validator):
    try:
        assert is_valid_gets_the_summary_analytics_data_related_to_network_devices_v1(
            validator,
            gets_the_summary_analytics_data_related_to_network_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_summary_analytics_data_related_to_network_devices_v1_default_val(api):
    endpoint_result = api.devices.gets_the_summary_analytics_data_related_to_network_devices_v1(
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


@pytest.mark.devices
def test_gets_the_summary_analytics_data_related_to_network_devices_v1_default_val(api, validator):
    try:
        assert is_valid_gets_the_summary_analytics_data_related_to_network_devices_v1(
            validator,
            gets_the_summary_analytics_data_related_to_network_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_top_n_analytics_data_related_to_network_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c5c273290fae513da209ec2c9270e46d_v2_3_7_9').validate(obj)
    return True


def gets_the_top_n_analytics_data_related_to_network_devices_v1(api):
    endpoint_result = api.devices.gets_the_top_n_analytics_data_related_to_network_devices_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=[{}],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string', 'function': 'string'}]},
        payload=None,
        startTime=0,
        topN=0
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_top_n_analytics_data_related_to_network_devices_v1(api, validator):
    try:
        assert is_valid_gets_the_top_n_analytics_data_related_to_network_devices_v1(
            validator,
            gets_the_top_n_analytics_data_related_to_network_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_top_n_analytics_data_related_to_network_devices_v1_default_val(api):
    endpoint_result = api.devices.gets_the_top_n_analytics_data_related_to_network_devices_v1(
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


@pytest.mark.devices
def test_gets_the_top_n_analytics_data_related_to_network_devices_v1_default_val(api, validator):
    try:
        assert is_valid_gets_the_top_n_analytics_data_related_to_network_devices_v1(
            validator,
            gets_the_top_n_analytics_data_related_to_network_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_trend_analytics_data_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ac7ce690e0f55a469b0a9bfa3d2c165e_v2_3_7_9').validate(obj)
    return True


def gets_the_trend_analytics_data_v1(api):
    endpoint_result = api.devices.gets_the_trend_analytics_data_v1(
        active_validation=True,
        aggregateAttributes=[{}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        groupBy=[{}],
        page={'limit': 0, 'offset': 0, 'timestampOrder': 'string'},
        payload=None,
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_trend_analytics_data_v1(api, validator):
    try:
        assert is_valid_gets_the_trend_analytics_data_v1(
            validator,
            gets_the_trend_analytics_data_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_trend_analytics_data_v1_default_val(api):
    endpoint_result = api.devices.gets_the_trend_analytics_data_v1(
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


@pytest.mark.devices
def test_gets_the_trend_analytics_data_v1_default_val(api, validator):
    try:
        assert is_valid_gets_the_trend_analytics_data_v1(
            validator,
            gets_the_trend_analytics_data_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_device_data_for_the_given_device_id_uuid_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f89c7ee84a615469b754add8feeabb5a_v2_3_7_9').validate(obj)
    return True


def get_the_device_data_for_the_given_device_id_uuid_v1(api):
    endpoint_result = api.devices.get_the_device_data_for_the_given_device_id_uuid_v1(
        attribute='string',
        end_time=0,
        id='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_device_data_for_the_given_device_id_uuid_v1(api, validator):
    try:
        assert is_valid_get_the_device_data_for_the_given_device_id_uuid_v1(
            validator,
            get_the_device_data_for_the_given_device_id_uuid_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_device_data_for_the_given_device_id_uuid_v1_default_val(api):
    endpoint_result = api.devices.get_the_device_data_for_the_given_device_id_uuid_v1(
        attribute=None,
        end_time=None,
        id='string',
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_device_data_for_the_given_device_id_uuid_v1_default_val(api, validator):
    try:
        assert is_valid_get_the_device_data_for_the_given_device_id_uuid_v1(
            validator,
            get_the_device_data_for_the_given_device_id_uuid_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1(json_schema_validate, obj):
    json_schema_validate('jsd_14ca2f659b595c0ba7c649fd8c8bdad6_v2_3_7_9').validate(obj)
    return True


def the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1(api):
    endpoint_result = api.devices.the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'logicalOperator': 'string', 'value': {}, 'filters': ['string']}],
        groupBy=['string'],
        id='string',
        page={'limit': 0, 'offset': 0, 'timestampOrder': 'string'},
        payload=None,
        startTime=0,
        trendIntervalInMinutes=0
    )
    return endpoint_result


@pytest.mark.devices
def test_the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1(api, validator):
    try:
        assert is_valid_the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1(
            validator,
            the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1_default_val(api):
    endpoint_result = api.devices.the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1(
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
        trendIntervalInMinutes=None
    )
    return endpoint_result


@pytest.mark.devices
def test_the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1_default_val(api, validator):
    try:
        assert is_valid_the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1(
            validator,
            the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_planned_access_points_for_building_v1(json_schema_validate, obj):
    json_schema_validate('jsd_30efc372d6eb577ca47e8c86f30c3d2f_v2_3_7_9').validate(obj)
    return True


def get_planned_access_points_for_building_v1(api):
    endpoint_result = api.devices.get_planned_access_points_for_building_v1(
        building_id='string',
        limit=0,
        offset=0,
        radios=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_planned_access_points_for_building_v1(api, validator):
    try:
        assert is_valid_get_planned_access_points_for_building_v1(
            validator,
            get_planned_access_points_for_building_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_planned_access_points_for_building_v1_default_val(api):
    endpoint_result = api.devices.get_planned_access_points_for_building_v1(
        building_id='string',
        limit=None,
        offset=None,
        radios=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_planned_access_points_for_building_v1_default_val(api, validator):
    try:
        assert is_valid_get_planned_access_points_for_building_v1(
            validator,
            get_planned_access_points_for_building_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_detail_v1(json_schema_validate, obj):
    json_schema_validate('jsd_560c9ee787eb5a0391309f45ddf392ca_v2_3_7_9').validate(obj)
    return True


def get_device_detail_v1(api):
    endpoint_result = api.devices.get_device_detail_v1(
        identifier='string',
        search_by='string',
        timestamp=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_detail_v1(api, validator):
    try:
        assert is_valid_get_device_detail_v1(
            validator,
            get_device_detail_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_detail_v1_default_val(api):
    endpoint_result = api.devices.get_device_detail_v1(
        identifier=None,
        search_by=None,
        timestamp=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_detail_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_detail_v1(
            validator,
            get_device_detail_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_enrichment_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_08a20c25e0fa518bb186fd7747450ef6_v2_3_7_9').validate(obj)
    return True


def get_device_enrichment_details_v1(api):
    endpoint_result = api.devices.get_device_enrichment_details_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_enrichment_details_v1(api, validator):
    try:
        assert is_valid_get_device_enrichment_details_v1(
            validator,
            get_device_enrichment_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_enrichment_details_v1_default_val(api):
    endpoint_result = api.devices.get_device_enrichment_details_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_enrichment_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_enrichment_details_v1(
            validator,
            get_device_enrichment_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c75e364632e15384a18063458e2ba0e3_v2_3_7_9').validate(obj)
    return True


def devices_v1(api):
    endpoint_result = api.devices.devices_v1(
        device_role='string',
        end_time=0,
        health='string',
        limit=0,
        offset=0,
        site_id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.devices
def test_devices_v1(api, validator):
    try:
        assert is_valid_devices_v1(
            validator,
            devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def devices_v1_default_val(api):
    endpoint_result = api.devices.devices_v1(
        device_role=None,
        end_time=None,
        health=None,
        limit=None,
        offset=None,
        site_id=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_devices_v1_default_val(api, validator):
    try:
        assert is_valid_devices_v1(
            validator,
            devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_planned_access_point_for_floor_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f6f9dde38ce458fcaf27ffd4f84bfe68_v2_3_7_9').validate(obj)
    return True


def update_planned_access_point_for_floor_v1(api):
    endpoint_result = api.devices.update_planned_access_point_for_floor_v1(
        active_validation=True,
        attributes={'createDate': 0, 'domain': 'string', 'heirarchyName': 'string', 'id': 0, 'instanceUuid': 'string', 'macAddress': 'string', 'name': 'string', 'source': 'string', 'typeString': 'string'},
        floor_id='string',
        isSensor=True,
        location={'altitude': 0, 'lattitude': 0, 'longtitude': 0},
        payload=None,
        position={'x': 0, 'y': 0, 'z': 0},
        radioCount=0,
        radios=[{'antenna': {'azimuthAngle': 0, 'elevationAngle': 0, 'gain': 0, 'mode': 'string', 'name': 'string', 'type': 'string'}, 'attributes': {'channel': 0, 'channelString': 'string', 'id': 0, 'ifMode': 'string', 'ifTypeString': 'string', 'ifTypeSubband': 'string', 'instanceUuid': 'string', 'slotId': 0, 'txPowerLevel': 0}, 'isSensor': True}]
    )
    return endpoint_result


@pytest.mark.devices
def test_update_planned_access_point_for_floor_v1(api, validator):
    try:
        assert is_valid_update_planned_access_point_for_floor_v1(
            validator,
            update_planned_access_point_for_floor_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_planned_access_point_for_floor_v1_default_val(api):
    endpoint_result = api.devices.update_planned_access_point_for_floor_v1(
        active_validation=True,
        attributes=None,
        floor_id='string',
        isSensor=None,
        location=None,
        payload=None,
        position=None,
        radioCount=None,
        radios=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_planned_access_point_for_floor_v1_default_val(api, validator):
    try:
        assert is_valid_update_planned_access_point_for_floor_v1(
            validator,
            update_planned_access_point_for_floor_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_planned_access_point_for_floor_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ca2fe989a227585086452d24d32867a6_v2_3_7_9').validate(obj)
    return True


def create_planned_access_point_for_floor_v1(api):
    endpoint_result = api.devices.create_planned_access_point_for_floor_v1(
        active_validation=True,
        attributes={'createDate': 0, 'domain': 'string', 'heirarchyName': 'string', 'id': 0, 'instanceUuid': 'string', 'macAddress': 'string', 'name': 'string', 'source': 'string', 'typeString': 'string'},
        floor_id='string',
        isSensor=True,
        location={'altitude': 0, 'lattitude': 0, 'longtitude': 0},
        payload=None,
        position={'x': 0, 'y': 0, 'z': 0},
        radioCount=0,
        radios=[{'antenna': {'azimuthAngle': 0, 'elevationAngle': 0, 'gain': 0, 'mode': 'string', 'name': 'string', 'type': 'string'}, 'attributes': {'channel': 0, 'channelString': 'string', 'id': 0, 'ifMode': 'string', 'ifTypeString': 'string', 'ifTypeSubband': 'string', 'instanceUuid': 'string', 'slotId': 0, 'txPowerLevel': 0}, 'isSensor': True}]
    )
    return endpoint_result


@pytest.mark.devices
def test_create_planned_access_point_for_floor_v1(api, validator):
    try:
        assert is_valid_create_planned_access_point_for_floor_v1(
            validator,
            create_planned_access_point_for_floor_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_planned_access_point_for_floor_v1_default_val(api):
    endpoint_result = api.devices.create_planned_access_point_for_floor_v1(
        active_validation=True,
        attributes=None,
        floor_id='string',
        isSensor=None,
        location=None,
        payload=None,
        position=None,
        radioCount=None,
        radios=None
    )
    return endpoint_result


@pytest.mark.devices
def test_create_planned_access_point_for_floor_v1_default_val(api, validator):
    try:
        assert is_valid_create_planned_access_point_for_floor_v1(
            validator,
            create_planned_access_point_for_floor_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_planned_access_points_for_floor_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9a570c5ee77b59d8b9cd203e566288e1_v2_3_7_9').validate(obj)
    return True


def get_planned_access_points_for_floor_v1(api):
    endpoint_result = api.devices.get_planned_access_points_for_floor_v1(
        floor_id='string',
        limit=0,
        offset=0,
        radios=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_planned_access_points_for_floor_v1(api, validator):
    try:
        assert is_valid_get_planned_access_points_for_floor_v1(
            validator,
            get_planned_access_points_for_floor_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_planned_access_points_for_floor_v1_default_val(api):
    endpoint_result = api.devices.get_planned_access_points_for_floor_v1(
        floor_id='string',
        limit=None,
        offset=None,
        radios=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_planned_access_points_for_floor_v1_default_val(api, validator):
    try:
        assert is_valid_get_planned_access_points_for_floor_v1(
            validator,
            get_planned_access_points_for_floor_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_planned_access_point_for_floor_v1(json_schema_validate, obj):
    json_schema_validate('jsd_cb644669ab8d5955826d23197015e208_v2_3_7_9').validate(obj)
    return True


def delete_planned_access_point_for_floor_v1(api):
    endpoint_result = api.devices.delete_planned_access_point_for_floor_v1(
        floor_id='string',
        planned_access_point_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_planned_access_point_for_floor_v1(api, validator):
    try:
        assert is_valid_delete_planned_access_point_for_floor_v1(
            validator,
            delete_planned_access_point_for_floor_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_planned_access_point_for_floor_v1_default_val(api):
    endpoint_result = api.devices.delete_planned_access_point_for_floor_v1(
        floor_id='string',
        planned_access_point_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_planned_access_point_for_floor_v1_default_val(api, validator):
    try:
        assert is_valid_delete_planned_access_point_for_floor_v1(
            validator,
            delete_planned_access_point_for_floor_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_health_score_definitions_for_given_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_84dea15738b550f3b147965f64050c97_v2_3_7_9').validate(obj)
    return True


def get_all_health_score_definitions_for_given_filters_v1(api):
    endpoint_result = api.devices.get_all_health_score_definitions_for_given_filters_v1(
        attribute='string',
        device_type='string',
        id='string',
        include_for_overall_health=True,
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_health_score_definitions_for_given_filters_v1(api, validator):
    try:
        assert is_valid_get_all_health_score_definitions_for_given_filters_v1(
            validator,
            get_all_health_score_definitions_for_given_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_health_score_definitions_for_given_filters_v1_default_val(api):
    endpoint_result = api.devices.get_all_health_score_definitions_for_given_filters_v1(
        attribute=None,
        device_type=None,
        id=None,
        include_for_overall_health=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_health_score_definitions_for_given_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_all_health_score_definitions_for_given_filters_v1(
            validator,
            get_all_health_score_definitions_for_given_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_health_score_definitions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b08f499f995f5f46ba52e0385b54721a_v2_3_7_9').validate(obj)
    return True


def update_health_score_definitions_v1(api):
    endpoint_result = api.devices.update_health_score_definitions_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_health_score_definitions_v1(api, validator):
    try:
        assert is_valid_update_health_score_definitions_v1(
            validator,
            update_health_score_definitions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_health_score_definitions_v1_default_val(api):
    endpoint_result = api.devices.update_health_score_definitions_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_health_score_definitions_v1_default_val(api, validator):
    try:
        assert is_valid_update_health_score_definitions_v1(
            validator,
            update_health_score_definitions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_count_of_health_score_definitions_based_on_provided_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_777d7eefccfc590dae32a123469f9fe3_v2_3_7_9').validate(obj)
    return True


def get_the_count_of_health_score_definitions_based_on_provided_filters_v1(api):
    endpoint_result = api.devices.get_the_count_of_health_score_definitions_based_on_provided_filters_v1(
        device_type='string',
        id='string',
        include_for_overall_health=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_count_of_health_score_definitions_based_on_provided_filters_v1(api, validator):
    try:
        assert is_valid_get_the_count_of_health_score_definitions_based_on_provided_filters_v1(
            validator,
            get_the_count_of_health_score_definitions_based_on_provided_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_count_of_health_score_definitions_based_on_provided_filters_v1_default_val(api):
    endpoint_result = api.devices.get_the_count_of_health_score_definitions_based_on_provided_filters_v1(
        device_type=None,
        id=None,
        include_for_overall_health=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_count_of_health_score_definitions_based_on_provided_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_the_count_of_health_score_definitions_based_on_provided_filters_v1(
            validator,
            get_the_count_of_health_score_definitions_based_on_provided_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_health_score_definition_for_the_given_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_15d2a0bbce2c5b6ba0b4aee3248ace42_v2_3_7_9').validate(obj)
    return True


def get_health_score_definition_for_the_given_id_v1(api):
    endpoint_result = api.devices.get_health_score_definition_for_the_given_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_health_score_definition_for_the_given_id_v1(api, validator):
    try:
        assert is_valid_get_health_score_definition_for_the_given_id_v1(
            validator,
            get_health_score_definition_for_the_given_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_health_score_definition_for_the_given_id_v1_default_val(api):
    endpoint_result = api.devices.get_health_score_definition_for_the_given_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_health_score_definition_for_the_given_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_health_score_definition_for_the_given_id_v1(
            validator,
            get_health_score_definition_for_the_given_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_health_score_definition_for_the_given_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b4f52e69ddca5b2583b28fb4c96447aa_v2_3_7_9').validate(obj)
    return True


def update_health_score_definition_for_the_given_id_v1(api):
    endpoint_result = api.devices.update_health_score_definition_for_the_given_id_v1(
        active_validation=True,
        id='string',
        includeForOverallHealth=True,
        payload=None,
        synchronizeToIssueThreshold=True,
        thresholdValue=0
    )
    return endpoint_result


@pytest.mark.devices
def test_update_health_score_definition_for_the_given_id_v1(api, validator):
    try:
        assert is_valid_update_health_score_definition_for_the_given_id_v1(
            validator,
            update_health_score_definition_for_the_given_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_health_score_definition_for_the_given_id_v1_default_val(api):
    endpoint_result = api.devices.update_health_score_definition_for_the_given_id_v1(
        active_validation=True,
        id='string',
        includeForOverallHealth=None,
        payload=None,
        synchronizeToIssueThreshold=None,
        thresholdValue=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_health_score_definition_for_the_given_id_v1_default_val(api, validator):
    try:
        assert is_valid_update_health_score_definition_for_the_given_id_v1(
            validator,
            update_health_score_definition_for_the_given_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_interfaces_v1(json_schema_validate, obj):
    json_schema_validate('jsd_22d3d71136d95562afc211b40004d109_v2_3_7_9').validate(obj)
    return True


def get_all_interfaces_v1(api):
    endpoint_result = api.devices.get_all_interfaces_v1(
        last_input_time='string',
        last_output_time='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_interfaces_v1(api, validator):
    try:
        assert is_valid_get_all_interfaces_v1(
            validator,
            get_all_interfaces_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_interfaces_v1_default_val(api):
    endpoint_result = api.devices.get_all_interfaces_v1(
        last_input_time=None,
        last_output_time=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_interfaces_v1_default_val(api, validator):
    try:
        assert is_valid_get_all_interfaces_v1(
            validator,
            get_all_interfaces_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_count(json_schema_validate, obj):
    json_schema_validate('jsd_0da44fbc3e415a99aac0bdd291e9a87a_v2_3_7_9').validate(obj)
    return True


def get_device_interface_count(api):
    endpoint_result = api.devices.get_device_interface_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count(api, validator):
    try:
        assert is_valid_get_device_interface_count(
            validator,
            get_device_interface_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_interface_count_default_val(api):
    endpoint_result = api.devices.get_device_interface_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count_default_val(api, validator):
    try:
        assert is_valid_get_device_interface_count(
            validator,
            get_device_interface_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_by_ip_v1(json_schema_validate, obj):
    json_schema_validate('jsd_cf7fa95e3ed4527aa5ba8ca871a8c142_v2_3_7_9').validate(obj)
    return True


def get_interface_by_ip_v1(api):
    endpoint_result = api.devices.get_interface_by_ip_v1(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_ip_v1(api, validator):
    try:
        assert is_valid_get_interface_by_ip_v1(
            validator,
            get_interface_by_ip_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interface_by_ip_v1_default_val(api):
    endpoint_result = api.devices.get_interface_by_ip_v1(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_ip_v1_default_val(api, validator):
    try:
        assert is_valid_get_interface_by_ip_v1(
            validator,
            get_interface_by_ip_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_isis_interfaces_v1(json_schema_validate, obj):
    json_schema_validate('jsd_af71ea437c8755869b00d26ba9234dff_v2_3_7_9').validate(obj)
    return True


def get_isis_interfaces_v1(api):
    endpoint_result = api.devices.get_isis_interfaces_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_isis_interfaces_v1(api, validator):
    try:
        assert is_valid_get_isis_interfaces_v1(
            validator,
            get_isis_interfaces_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_isis_interfaces_v1_default_val(api):
    endpoint_result = api.devices.get_isis_interfaces_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_isis_interfaces_v1_default_val(api, validator):
    try:
        assert is_valid_get_isis_interfaces_v1(
            validator,
            get_isis_interfaces_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_info_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e057192b97615f0d99a10e2b66bab13a_v2_3_7_9').validate(obj)
    return True


def get_interface_info_by_id_v1(api):
    endpoint_result = api.devices.get_interface_info_by_id_v1(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_info_by_id_v1(api, validator):
    try:
        assert is_valid_get_interface_info_by_id_v1(
            validator,
            get_interface_info_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interface_info_by_id_v1_default_val(api):
    endpoint_result = api.devices.get_interface_info_by_id_v1(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_info_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_interface_info_by_id_v1(
            validator,
            get_interface_info_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_count_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_34b7d6c62ea6522081fcf55de7eb9fd7_v2_3_7_9').validate(obj)
    return True


def get_device_interface_count_by_id(api):
    endpoint_result = api.devices.get_device_interface_count_by_id(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count_by_id(api, validator):
    try:
        assert is_valid_get_device_interface_count_by_id(
            validator,
            get_device_interface_count_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_interface_count_by_id_default_val(api):
    endpoint_result = api.devices.get_device_interface_count_by_id(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count_by_id_default_val(api, validator):
    try:
        assert is_valid_get_device_interface_count_by_id(
            validator,
            get_device_interface_count_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_details(json_schema_validate, obj):
    json_schema_validate('jsd_bef9e9b306085d879b877598fad71b51_v2_3_7_9').validate(obj)
    return True


def get_interface_details(api):
    endpoint_result = api.devices.get_interface_details(
        device_id='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_details(api, validator):
    try:
        assert is_valid_get_interface_details(
            validator,
            get_interface_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interface_details_default_val(api):
    endpoint_result = api.devices.get_interface_details(
        device_id='string',
        name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_details_default_val(api, validator):
    try:
        assert is_valid_get_interface_details(
            validator,
            get_interface_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interfaces_by_specified_range_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5a3d52c630ba5deaada16fe3b07af744_v2_3_7_9').validate(obj)
    return True


def get_device_interfaces_by_specified_range_v1(api):
    endpoint_result = api.devices.get_device_interfaces_by_specified_range_v1(
        device_id='string',
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interfaces_by_specified_range_v1(api, validator):
    try:
        assert is_valid_get_device_interfaces_by_specified_range_v1(
            validator,
            get_device_interfaces_by_specified_range_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_interfaces_by_specified_range_v1_default_val(api):
    endpoint_result = api.devices.get_device_interfaces_by_specified_range_v1(
        device_id='string',
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interfaces_by_specified_range_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_interfaces_by_specified_range_v1(
            validator,
            get_device_interfaces_by_specified_range_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ospf_interfaces_v1(json_schema_validate, obj):
    json_schema_validate('jsd_32a2868ff45f5621965f6ece01a742ce_v2_3_7_9').validate(obj)
    return True


def get_ospf_interfaces_v1(api):
    endpoint_result = api.devices.get_ospf_interfaces_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_ospf_interfaces_v1(api, validator):
    try:
        assert is_valid_get_ospf_interfaces_v1(
            validator,
            get_ospf_interfaces_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ospf_interfaces_v1_default_val(api):
    endpoint_result = api.devices.get_ospf_interfaces_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_ospf_interfaces_v1_default_val(api, validator):
    try:
        assert is_valid_get_ospf_interfaces_v1(
            validator,
            get_ospf_interfaces_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_17b16bff74ae54ca88a02b34df169218_v2_3_7_9').validate(obj)
    return True


def get_interface_by_id_v1(api):
    endpoint_result = api.devices.get_interface_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_id_v1(api, validator):
    try:
        assert is_valid_get_interface_by_id_v1(
            validator,
            get_interface_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interface_by_id_v1_default_val(api):
    endpoint_result = api.devices.get_interface_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_interface_by_id_v1(
            validator,
            get_interface_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_interface_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2441213b887c55faaca726bbe4ac2564_v2_3_7_9').validate(obj)
    return True


def update_interface_details_v1(api):
    endpoint_result = api.devices.update_interface_details_v1(
        active_validation=True,
        adminStatus='string',
        deployment_mode='string',
        description='string',
        interface_uuid='string',
        payload=None,
        vlanId=0,
        voiceVlanId=0
    )
    return endpoint_result


@pytest.mark.devices
def test_update_interface_details_v1(api, validator):
    try:
        assert is_valid_update_interface_details_v1(
            validator,
            update_interface_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_interface_details_v1_default_val(api):
    endpoint_result = api.devices.update_interface_details_v1(
        active_validation=True,
        adminStatus=None,
        deployment_mode=None,
        description=None,
        interface_uuid='string',
        payload=None,
        vlanId=None,
        voiceVlanId=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_interface_details_v1_default_val(api, validator):
    try:
        assert is_valid_update_interface_details_v1(
            validator,
            update_interface_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_legit_operations_for_interface_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fe6d62edcec25921926043ca25f75bed_v2_3_7_9').validate(obj)
    return True


def legit_operations_for_interface_v1(api):
    endpoint_result = api.devices.legit_operations_for_interface_v1(
        interface_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_legit_operations_for_interface_v1(api, validator):
    try:
        assert is_valid_legit_operations_for_interface_v1(
            validator,
            legit_operations_for_interface_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def legit_operations_for_interface_v1_default_val(api):
    endpoint_result = api.devices.legit_operations_for_interface_v1(
        interface_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_legit_operations_for_interface_v1_default_val(api, validator):
    try:
        assert is_valid_legit_operations_for_interface_v1(
            validator,
            legit_operations_for_interface_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_clear_mac_address_table_v1(json_schema_validate, obj):
    json_schema_validate('jsd_399e702d5786552992aa76b930780569_v2_3_7_9').validate(obj)
    return True


def clear_mac_address_table_v1(api):
    endpoint_result = api.devices.clear_mac_address_table_v1(
        active_validation=True,
        deployment_mode='string',
        interface_uuid='string',
        operation='string',
        payload=None,
        payload={}
    )
    return endpoint_result


@pytest.mark.devices
def test_clear_mac_address_table_v1(api, validator):
    try:
        assert is_valid_clear_mac_address_table_v1(
            validator,
            clear_mac_address_table_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def clear_mac_address_table_v1_default_val(api):
    endpoint_result = api.devices.clear_mac_address_table_v1(
        active_validation=True,
        deployment_mode=None,
        interface_uuid='string',
        operation=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_clear_mac_address_table_v1_default_val(api, validator):
    try:
        assert is_valid_clear_mac_address_table_v1(
            validator,
            clear_mac_address_table_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_list_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fe602e8165035b5cbc304fada4ee2f26_v2_3_7_9').validate(obj)
    return True


def get_device_list_v1(api):
    endpoint_result = api.devices.get_device_list_v1(
        associated_wlc_ip='value1,value2',
        collection_interval='value1,value2',
        collection_status='value1,value2',
        device_support_level='string',
        error_code='value1,value2',
        error_description='value1,value2',
        family='value1,value2',
        hostname='value1,value2',
        id='string',
        license_name='value1,value2',
        license_status='value1,value2',
        license_type='value1,value2',
        limit=0,
        location='value1,value2',
        location_name='value1,value2',
        mac_address='value1,value2',
        management_ip_address='value1,value2',
        module_equpimenttype='value1,value2',
        module_name='value1,value2',
        module_operationstatecode='value1,value2',
        module_partnumber='value1,value2',
        module_servicestate='value1,value2',
        module_vendorequipmenttype='value1,value2',
        not_synced_for_minutes='value1,value2',
        offset=0,
        platform_id='value1,value2',
        reachability_status='value1,value2',
        role='value1,value2',
        serial_number='value1,value2',
        series='value1,value2',
        software_type='value1,value2',
        software_version='value1,value2',
        type='value1,value2',
        up_time='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_list_v1(api, validator):
    try:
        assert is_valid_get_device_list_v1(
            validator,
            get_device_list_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_list_v1_default_val(api):
    endpoint_result = api.devices.get_device_list_v1(
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        device_support_level=None,
        error_code=None,
        error_description=None,
        family=None,
        hostname=None,
        id=None,
        license_name=None,
        license_status=None,
        license_type=None,
        limit=None,
        location=None,
        location_name=None,
        mac_address=None,
        management_ip_address=None,
        module_equpimenttype=None,
        module_name=None,
        module_operationstatecode=None,
        module_partnumber=None,
        module_servicestate=None,
        module_vendorequipmenttype=None,
        not_synced_for_minutes=None,
        offset=None,
        platform_id=None,
        reachability_status=None,
        role=None,
        serial_number=None,
        series=None,
        software_type=None,
        software_version=None,
        type=None,
        up_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_list_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_list_v1(
            validator,
            get_device_list_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_device(json_schema_validate, obj):
    json_schema_validate('jsd_62704fe3ec7651e79d891fce37a0d860_v2_3_7_9').validate(obj)
    return True


def add_device(api):
    endpoint_result = api.devices.add_device(
        active_validation=True,
        cliTransport='string',
        computeDevice=True,
        enablePassword='string',
        extendedDiscoveryInfo='string',
        httpPassword='string',
        httpPort='string',
        httpSecure=True,
        httpUserName='string',
        ipAddress=['string'],
        merakiOrgId=['string'],
        netconfPort='string',
        password='string',
        payload=None,
        serialNumber='string',
        snmpAuthPassphrase='string',
        snmpAuthProtocol='string',
        snmpMode='string',
        snmpPrivPassphrase='string',
        snmpPrivProtocol='string',
        snmpROCommunity='string',
        snmpRWCommunity='string',
        snmpRetry=0,
        snmpTimeout=0,
        snmpUserName='string',
        snmpVersion='string',
        type='string',
        userName='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_add_device(api, validator):
    try:
        assert is_valid_add_device(
            validator,
            add_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_device_default_val(api):
    endpoint_result = api.devices.add_device(
        active_validation=True,
        cliTransport=None,
        computeDevice=None,
        enablePassword=None,
        extendedDiscoveryInfo=None,
        httpPassword=None,
        httpPort=None,
        httpSecure=None,
        httpUserName=None,
        ipAddress=None,
        merakiOrgId=None,
        netconfPort=None,
        password=None,
        payload=None,
        serialNumber=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpRWCommunity=None,
        snmpRetry=None,
        snmpTimeout=None,
        snmpUserName=None,
        snmpVersion=None,
        type=None,
        userName=None
    )
    return endpoint_result


@pytest.mark.devices
def test_add_device_default_val(api, validator):
    try:
        assert is_valid_add_device(
            validator,
            add_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sync_devices(json_schema_validate, obj):
    json_schema_validate('jsd_8232fe06867e548bba1919024b40d992_v2_3_7_9').validate(obj)
    return True


def sync_devices(api):
    endpoint_result = api.devices.sync_devices(
        active_validation=True,
        cliTransport='string',
        computeDevice=True,
        enablePassword='string',
        extendedDiscoveryInfo='string',
        httpPassword='string',
        httpPort='string',
        httpSecure=True,
        httpUserName='string',
        ipAddress=['string'],
        merakiOrgId=['string'],
        netconfPort='string',
        password='string',
        payload=None,
        serialNumber='string',
        snmpAuthPassphrase='string',
        snmpAuthProtocol='string',
        snmpMode='string',
        snmpPrivPassphrase='string',
        snmpPrivProtocol='string',
        snmpROCommunity='string',
        snmpRWCommunity='string',
        snmpRetry=0,
        snmpTimeout=0,
        snmpUserName='string',
        snmpVersion='string',
        type='string',
        updateMgmtIPaddressList=[{'existMgmtIpAddress': 'string', 'newMgmtIpAddress': 'string'}],
        userName='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices(api, validator):
    try:
        assert is_valid_sync_devices(
            validator,
            sync_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def sync_devices_default_val(api):
    endpoint_result = api.devices.sync_devices(
        active_validation=True,
        cliTransport=None,
        computeDevice=None,
        enablePassword=None,
        extendedDiscoveryInfo=None,
        httpPassword=None,
        httpPort=None,
        httpSecure=None,
        httpUserName=None,
        ipAddress=None,
        merakiOrgId=None,
        netconfPort=None,
        password=None,
        payload=None,
        serialNumber=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpRWCommunity=None,
        snmpRetry=None,
        snmpTimeout=None,
        snmpUserName=None,
        snmpVersion=None,
        type=None,
        updateMgmtIPaddressList=None,
        userName=None
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices_default_val(api, validator):
    try:
        assert is_valid_sync_devices(
            validator,
            sync_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_values_that_match_fully_or_partially_an_attribute_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b5a5c8da4aaa526da6a06e97c80a38be_v2_3_7_9').validate(obj)
    return True


def get_device_values_that_match_fully_or_partially_an_attribute_v1(api):
    endpoint_result = api.devices.get_device_values_that_match_fully_or_partially_an_attribute_v1(
        associated_wlc_ip='string',
        collection_interval='string',
        collection_status='string',
        error_code='string',
        family='string',
        hostname='string',
        limit=0,
        mac_address='string',
        management_ip_address='string',
        offset=0,
        platform_id='string',
        reachability_failure_reason='string',
        reachability_status='string',
        role='string',
        role_source='string',
        serial_number='string',
        series='string',
        software_type='string',
        software_version='string',
        type='string',
        up_time='string',
        vrf_name='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_values_that_match_fully_or_partially_an_attribute_v1(api, validator):
    try:
        assert is_valid_get_device_values_that_match_fully_or_partially_an_attribute_v1(
            validator,
            get_device_values_that_match_fully_or_partially_an_attribute_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_values_that_match_fully_or_partially_an_attribute_v1_default_val(api):
    endpoint_result = api.devices.get_device_values_that_match_fully_or_partially_an_attribute_v1(
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        error_code=None,
        family=None,
        hostname=None,
        limit=None,
        mac_address=None,
        management_ip_address=None,
        offset=None,
        platform_id=None,
        reachability_failure_reason=None,
        reachability_status=None,
        role=None,
        role_source=None,
        serial_number=None,
        series=None,
        software_type=None,
        software_version=None,
        type=None,
        up_time=None,
        vrf_name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_values_that_match_fully_or_partially_an_attribute_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_values_that_match_fully_or_partially_an_attribute_v1(
            validator,
            get_device_values_that_match_fully_or_partially_an_attribute_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_role_v1(json_schema_validate, obj):
    json_schema_validate('jsd_aa11f09d28165f4ea6c81b8642e59cc4_v2_3_7_9').validate(obj)
    return True


def update_device_role_v1(api):
    endpoint_result = api.devices.update_device_role_v1(
        active_validation=True,
        id='string',
        payload=None,
        role='string',
        roleSource='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_role_v1(api, validator):
    try:
        assert is_valid_update_device_role_v1(
            validator,
            update_device_role_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_role_v1_default_val(api):
    endpoint_result = api.devices.update_device_role_v1(
        active_validation=True,
        id=None,
        payload=None,
        role=None,
        roleSource=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_role_v1_default_val(api, validator):
    try:
        assert is_valid_update_device_role_v1(
            validator,
            update_device_role_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_polling_interval_for_all_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ce94ab18ad505e8a9846f6c4c9df0d2b_v2_3_7_9').validate(obj)
    return True


def get_polling_interval_for_all_devices_v1(api):
    endpoint_result = api.devices.get_polling_interval_for_all_devices_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_for_all_devices_v1(api, validator):
    try:
        assert is_valid_get_polling_interval_for_all_devices_v1(
            validator,
            get_polling_interval_for_all_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_polling_interval_for_all_devices_v1_default_val(api):
    endpoint_result = api.devices.get_polling_interval_for_all_devices_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_for_all_devices_v1_default_val(api, validator):
    try:
        assert is_valid_get_polling_interval_for_all_devices_v1(
            validator,
            get_polling_interval_for_all_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_config_for_all_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ed2bca4be412527198720a4dfec9604a_v2_3_7_9').validate(obj)
    return True


def get_device_config_for_all_devices_v1(api):
    endpoint_result = api.devices.get_device_config_for_all_devices_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_for_all_devices_v1(api, validator):
    try:
        assert is_valid_get_device_config_for_all_devices_v1(
            validator,
            get_device_config_for_all_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_config_for_all_devices_v1_default_val(api):
    endpoint_result = api.devices.get_device_config_for_all_devices_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_for_all_devices_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_config_for_all_devices_v1(
            validator,
            get_device_config_for_all_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_config_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3dc0a72537a3578ca31cc5ef29131d35_v2_3_7_9').validate(obj)
    return True


def get_device_config_count_v1(api):
    endpoint_result = api.devices.get_device_config_count_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_count_v1(api, validator):
    try:
        assert is_valid_get_device_config_count_v1(
            validator,
            get_device_config_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_config_count_v1_default_val(api):
    endpoint_result = api.devices.get_device_config_count_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_config_count_v1(
            validator,
            get_device_config_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_count(json_schema_validate, obj):
    json_schema_validate('jsd_bbfe7340fe6752e5bc273a303d165654_v2_3_7_9').validate(obj)
    return True


def get_device_count(api):
    endpoint_result = api.devices.get_device_count(
        hostname='value1,value2',
        location_name='value1,value2',
        mac_address='value1,value2',
        management_ip_address='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_count(api, validator):
    try:
        assert is_valid_get_device_count(
            validator,
            get_device_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_count_default_val(api):
    endpoint_result = api.devices.get_device_count(
        hostname=None,
        location_name=None,
        mac_address=None,
        management_ip_address=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_count_default_val(api, validator):
    try:
        assert is_valid_get_device_count(
            validator,
            get_device_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_export_device_list_v1(json_schema_validate, obj):
    json_schema_validate('jsd_57e6ec627d3c587288978990aae75228_v2_3_7_9').validate(obj)
    return True


def export_device_list_v1(api):
    endpoint_result = api.devices.export_device_list_v1(
        active_validation=True,
        deviceUuids=['string'],
        operationEnum='string',
        parameters=['string'],
        password='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_export_device_list_v1(api, validator):
    try:
        assert is_valid_export_device_list_v1(
            validator,
            export_device_list_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def export_device_list_v1_default_val(api):
    endpoint_result = api.devices.export_device_list_v1(
        active_validation=True,
        deviceUuids=None,
        operationEnum=None,
        parameters=None,
        password=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_export_device_list_v1_default_val(api, validator):
    try:
        assert is_valid_export_device_list_v1(
            validator,
            export_device_list_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_functional_capability_for_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ad8cea95d71352f0842a2c869765e6cf_v2_3_7_9').validate(obj)
    return True


def get_functional_capability_for_devices_v1(api):
    endpoint_result = api.devices.get_functional_capability_for_devices_v1(
        device_id='string',
        function_name='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_for_devices_v1(api, validator):
    try:
        assert is_valid_get_functional_capability_for_devices_v1(
            validator,
            get_functional_capability_for_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_functional_capability_for_devices_v1_default_val(api):
    endpoint_result = api.devices.get_functional_capability_for_devices_v1(
        device_id=None,
        function_name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_for_devices_v1_default_val(api, validator):
    try:
        assert is_valid_get_functional_capability_for_devices_v1(
            validator,
            get_functional_capability_for_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_functional_capability_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7f494532c45654fdaeda8d46a0d9753d_v2_3_7_9').validate(obj)
    return True


def get_functional_capability_by_id_v1(api):
    endpoint_result = api.devices.get_functional_capability_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_by_id_v1(api, validator):
    try:
        assert is_valid_get_functional_capability_by_id_v1(
            validator,
            get_functional_capability_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_functional_capability_by_id_v1_default_val(api):
    endpoint_result = api.devices.get_functional_capability_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_functional_capability_by_id_v1(
            validator,
            get_functional_capability_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_inventory_insight_device_link_mismatch(json_schema_validate, obj):
    json_schema_validate('jsd_eed1595442b757bf94938c858a257ced_v2_3_7_9').validate(obj)
    return True


def inventory_insight_device_link_mismatch(api):
    endpoint_result = api.devices.inventory_insight_device_link_mismatch(
        category='string',
        limit=0,
        offset=0,
        order='string',
        site_id='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_inventory_insight_device_link_mismatch(api, validator):
    try:
        assert is_valid_inventory_insight_device_link_mismatch(
            validator,
            inventory_insight_device_link_mismatch(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def inventory_insight_device_link_mismatch_default_val(api):
    endpoint_result = api.devices.inventory_insight_device_link_mismatch(
        category=None,
        limit=None,
        offset=None,
        order=None,
        site_id='string',
        sort_by=None
    )
    return endpoint_result


@pytest.mark.devices
def test_inventory_insight_device_link_mismatch_default_val(api, validator):
    try:
        assert is_valid_inventory_insight_device_link_mismatch(
            validator,
            inventory_insight_device_link_mismatch_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device_by_ip_v1(json_schema_validate, obj):
    json_schema_validate('jsd_40123dc74c2052a3a4eb7e2a01eaa8e7_v2_3_7_9').validate(obj)
    return True


def get_network_device_by_ip_v1(api):
    endpoint_result = api.devices.get_network_device_by_ip_v1(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_ip_v1(api, validator):
    try:
        assert is_valid_get_network_device_by_ip_v1(
            validator,
            get_network_device_by_ip_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_device_by_ip_v1_default_val(api):
    endpoint_result = api.devices.get_network_device_by_ip_v1(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_ip_v1_default_val(api, validator):
    try:
        assert is_valid_get_network_device_by_ip_v1(
            validator,
            get_network_device_by_ip_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_modules_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ce9e547725c45c66824afda98179d12f_v2_3_7_9').validate(obj)
    return True


def get_modules_v1(api):
    endpoint_result = api.devices.get_modules_v1(
        device_id='string',
        limit=0,
        name_list='value1,value2',
        offset=0,
        operational_state_code_list='value1,value2',
        part_number_list='value1,value2',
        vendor_equipment_type_list='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_modules_v1(api, validator):
    try:
        assert is_valid_get_modules_v1(
            validator,
            get_modules_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_modules_v1_default_val(api):
    endpoint_result = api.devices.get_modules_v1(
        device_id=None,
        limit=None,
        name_list=None,
        offset=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_modules_v1_default_val(api, validator):
    try:
        assert is_valid_get_modules_v1(
            validator,
            get_modules_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_module_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fb11f997009751c991884b5fc02087c5_v2_3_7_9').validate(obj)
    return True


def get_module_count_v1(api):
    endpoint_result = api.devices.get_module_count_v1(
        device_id='string',
        name_list='value1,value2',
        operational_state_code_list='value1,value2',
        part_number_list='value1,value2',
        vendor_equipment_type_list='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_count_v1(api, validator):
    try:
        assert is_valid_get_module_count_v1(
            validator,
            get_module_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_module_count_v1_default_val(api):
    endpoint_result = api.devices.get_module_count_v1(
        device_id=None,
        name_list=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_module_count_v1(
            validator,
            get_module_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_module_info_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_96a4588640da5b018b499c5760f4092a_v2_3_7_9').validate(obj)
    return True


def get_module_info_by_id_v1(api):
    endpoint_result = api.devices.get_module_info_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_info_by_id_v1(api, validator):
    try:
        assert is_valid_get_module_info_by_id_v1(
            validator,
            get_module_info_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_module_info_by_id_v1_default_val(api):
    endpoint_result = api.devices.get_module_info_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_info_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_module_info_by_id_v1(
            validator,
            get_module_info_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_by_serial_number_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5c53d56c282e5f108c659009d21f9d26_v2_3_7_9').validate(obj)
    return True


def get_device_by_serial_number_v1(api):
    endpoint_result = api.devices.get_device_by_serial_number_v1(
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_serial_number_v1(api, validator):
    try:
        assert is_valid_get_device_by_serial_number_v1(
            validator,
            get_device_by_serial_number_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_by_serial_number_v1_default_val(api):
    endpoint_result = api.devices.get_device_by_serial_number_v1(
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_serial_number_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_by_serial_number_v1(
            validator,
            get_device_by_serial_number_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sync_devices_using_forcesync(json_schema_validate, obj):
    json_schema_validate('jsd_9425f2c120b855cb8c852806ce72e54d_v2_3_7_9').validate(obj)
    return True


def sync_devices_using_forcesync(api):
    endpoint_result = api.devices.sync_devices_using_forcesync(
        active_validation=True,
        force_sync=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices_using_forcesync(api, validator):
    try:
        assert is_valid_sync_devices_using_forcesync(
            validator,
            sync_devices_using_forcesync(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def sync_devices_using_forcesync_default_val(api):
    endpoint_result = api.devices.sync_devices_using_forcesync(
        active_validation=True,
        force_sync=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices_using_forcesync_default_val(api, validator):
    try:
        assert is_valid_sync_devices_using_forcesync(
            validator,
            sync_devices_using_forcesync_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_devices_registered_for_wsa_notification_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8770b2c39feb5e48913492c33add7f13_v2_3_7_9').validate(obj)
    return True


def get_devices_registered_for_wsa_notification_v1(api):
    endpoint_result = api.devices.get_devices_registered_for_wsa_notification_v1(
        macaddress='string',
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_devices_registered_for_wsa_notification_v1(api, validator):
    try:
        assert is_valid_get_devices_registered_for_wsa_notification_v1(
            validator,
            get_devices_registered_for_wsa_notification_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_devices_registered_for_wsa_notification_v1_default_val(api):
    endpoint_result = api.devices.get_devices_registered_for_wsa_notification_v1(
        macaddress=None,
        serial_number=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_devices_registered_for_wsa_notification_v1_default_val(api, validator):
    try:
        assert is_valid_get_devices_registered_for_wsa_notification_v1(
            validator,
            get_devices_registered_for_wsa_notification_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_user_defined_fields_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d31b0bb4bde55bb8a3078b66c81f3a22_v2_3_7_9').validate(obj)
    return True


def get_all_user_defined_fields_v1(api):
    endpoint_result = api.devices.get_all_user_defined_fields_v1(
        id='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_user_defined_fields_v1(api, validator):
    try:
        assert is_valid_get_all_user_defined_fields_v1(
            validator,
            get_all_user_defined_fields_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_user_defined_fields_v1_default_val(api):
    endpoint_result = api.devices.get_all_user_defined_fields_v1(
        id=None,
        name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_user_defined_fields_v1_default_val(api, validator):
    try:
        assert is_valid_get_all_user_defined_fields_v1(
            validator,
            get_all_user_defined_fields_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_user_defined_field_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ed266e6eda225aedbf581508635da822_v2_3_7_9').validate(obj)
    return True


def create_user_defined_field_v1(api):
    endpoint_result = api.devices.create_user_defined_field_v1(
        active_validation=True,
        description='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_create_user_defined_field_v1(api, validator):
    try:
        assert is_valid_create_user_defined_field_v1(
            validator,
            create_user_defined_field_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_user_defined_field_v1_default_val(api):
    endpoint_result = api.devices.create_user_defined_field_v1(
        active_validation=True,
        description=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_create_user_defined_field_v1_default_val(api, validator):
    try:
        assert is_valid_create_user_defined_field_v1(
            validator,
            create_user_defined_field_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_user_defined_field_v1(json_schema_validate, obj):
    json_schema_validate('jsd_119d76a951f85a7a927afc2f1ea935c8_v2_3_7_9').validate(obj)
    return True


def update_user_defined_field_v1(api):
    endpoint_result = api.devices.update_user_defined_field_v1(
        active_validation=True,
        description='string',
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_user_defined_field_v1(api, validator):
    try:
        assert is_valid_update_user_defined_field_v1(
            validator,
            update_user_defined_field_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_user_defined_field_v1_default_val(api):
    endpoint_result = api.devices.update_user_defined_field_v1(
        active_validation=True,
        description=None,
        id='string',
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_user_defined_field_v1_default_val(api, validator):
    try:
        assert is_valid_update_user_defined_field_v1(
            validator,
            update_user_defined_field_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_user_defined_field_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6854f0f19119501094fb5fafe05dfbca_v2_3_7_9').validate(obj)
    return True


def delete_user_defined_field_v1(api):
    endpoint_result = api.devices.delete_user_defined_field_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_user_defined_field_v1(api, validator):
    try:
        assert is_valid_delete_user_defined_field_v1(
            validator,
            delete_user_defined_field_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_user_defined_field_v1_default_val(api):
    endpoint_result = api.devices.delete_user_defined_field_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_user_defined_field_v1_default_val(api, validator):
    try:
        assert is_valid_delete_user_defined_field_v1(
            validator,
            delete_user_defined_field_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_chassis_details_for_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4a03cee8dfd7514487a134a422f5e0d7_v2_3_7_9').validate(obj)
    return True


def get_chassis_details_for_device_v1(api):
    endpoint_result = api.devices.get_chassis_details_for_device_v1(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_chassis_details_for_device_v1(api, validator):
    try:
        assert is_valid_get_chassis_details_for_device_v1(
            validator,
            get_chassis_details_for_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_chassis_details_for_device_v1_default_val(api):
    endpoint_result = api.devices.get_chassis_details_for_device_v1(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_chassis_details_for_device_v1_default_val(api, validator):
    try:
        assert is_valid_get_chassis_details_for_device_v1(
            validator,
            get_chassis_details_for_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_stack_details_for_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c07eaefa1fa45faa801764d9094336ae_v2_3_7_9').validate(obj)
    return True


def get_stack_details_for_device_v1(api):
    endpoint_result = api.devices.get_stack_details_for_device_v1(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_stack_details_for_device_v1(api, validator):
    try:
        assert is_valid_get_stack_details_for_device_v1(
            validator,
            get_stack_details_for_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_stack_details_for_device_v1_default_val(api):
    endpoint_result = api.devices.get_stack_details_for_device_v1(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_stack_details_for_device_v1_default_val(api, validator):
    try:
        assert is_valid_get_stack_details_for_device_v1(
            validator,
            get_stack_details_for_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_user_defined_field_from_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c1144f7a496455f99f95d36d6474c4b4_v2_3_7_9').validate(obj)
    return True


def remove_user_defined_field_from_device_v1(api):
    endpoint_result = api.devices.remove_user_defined_field_from_device_v1(
        device_id='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_remove_user_defined_field_from_device_v1(api, validator):
    try:
        assert is_valid_remove_user_defined_field_from_device_v1(
            validator,
            remove_user_defined_field_from_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def remove_user_defined_field_from_device_v1_default_val(api):
    endpoint_result = api.devices.remove_user_defined_field_from_device_v1(
        device_id='string',
        name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_remove_user_defined_field_from_device_v1_default_val(api, validator):
    try:
        assert is_valid_remove_user_defined_field_from_device_v1(
            validator,
            remove_user_defined_field_from_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_user_defined_field_to_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a73fbc67627e5bbbafe748de84d42df6_v2_3_7_9').validate(obj)
    return True


def add_user_defined_field_to_device_v1(api):
    endpoint_result = api.devices.add_user_defined_field_to_device_v1(
        active_validation=True,
        device_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_add_user_defined_field_to_device_v1(api, validator):
    try:
        assert is_valid_add_user_defined_field_to_device_v1(
            validator,
            add_user_defined_field_to_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_user_defined_field_to_device_v1_default_val(api):
    endpoint_result = api.devices.add_user_defined_field_to_device_v1(
        active_validation=True,
        device_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_add_user_defined_field_to_device_v1_default_val(api, validator):
    try:
        assert is_valid_add_user_defined_field_to_device_v1(
            validator,
            add_user_defined_field_to_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_details_of_physical_components_of_the_given_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_520c1cb24a2b53ce8d29d119c6ee1112_v2_3_7_9').validate(obj)
    return True


def get_the_details_of_physical_components_of_the_given_device_v1(api):
    endpoint_result = api.devices.get_the_details_of_physical_components_of_the_given_device_v1(
        device_uuid='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_details_of_physical_components_of_the_given_device_v1(api, validator):
    try:
        assert is_valid_get_the_details_of_physical_components_of_the_given_device_v1(
            validator,
            get_the_details_of_physical_components_of_the_given_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_details_of_physical_components_of_the_given_device_v1_default_val(api):
    endpoint_result = api.devices.get_the_details_of_physical_components_of_the_given_device_v1(
        device_uuid='string',
        type=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_details_of_physical_components_of_the_given_device_v1_default_val(api, validator):
    try:
        assert is_valid_get_the_details_of_physical_components_of_the_given_device_v1(
            validator,
            get_the_details_of_physical_components_of_the_given_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_poe_interface_details(json_schema_validate, obj):
    json_schema_validate('jsd_ab3215d9be065533b7cbbc978cb4d905_v2_3_7_9').validate(obj)
    return True


def poe_interface_details(api):
    endpoint_result = api.devices.poe_interface_details(
        device_uuid='string',
        interface_name_list='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_poe_interface_details(api, validator):
    try:
        assert is_valid_poe_interface_details(
            validator,
            poe_interface_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def poe_interface_details_default_val(api):
    endpoint_result = api.devices.poe_interface_details(
        device_uuid='string',
        interface_name_list=None
    )
    return endpoint_result


@pytest.mark.devices
def test_poe_interface_details_default_val(api, validator):
    try:
        assert is_valid_poe_interface_details(
            validator,
            poe_interface_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_connected_device_detail_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a1878314ffd35d29bea49f12d10b59c8_v2_3_7_9').validate(obj)
    return True


def get_connected_device_detail_v1(api):
    endpoint_result = api.devices.get_connected_device_detail_v1(
        device_uuid='string',
        interface_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_connected_device_detail_v1(api, validator):
    try:
        assert is_valid_get_connected_device_detail_v1(
            validator,
            get_connected_device_detail_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_connected_device_detail_v1_default_val(api):
    endpoint_result = api.devices.get_connected_device_detail_v1(
        device_uuid='string',
        interface_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_connected_device_detail_v1_default_val(api, validator):
    try:
        assert is_valid_get_connected_device_detail_v1(
            validator,
            get_connected_device_detail_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_linecard_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bd31690b61f45d9f880d74d4e682b070_v2_3_7_9').validate(obj)
    return True


def get_linecard_details_v1(api):
    endpoint_result = api.devices.get_linecard_details_v1(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_linecard_details_v1(api, validator):
    try:
        assert is_valid_get_linecard_details_v1(
            validator,
            get_linecard_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_linecard_details_v1_default_val(api):
    endpoint_result = api.devices.get_linecard_details_v1(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_linecard_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_linecard_details_v1(
            validator,
            get_linecard_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_poe_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f7a67aba0b365a1e9dae62d148511a25_v2_3_7_9').validate(obj)
    return True


def poe_details_v1(api):
    endpoint_result = api.devices.poe_details_v1(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_poe_details_v1(api, validator):
    try:
        assert is_valid_poe_details_v1(
            validator,
            poe_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def poe_details_v1_default_val(api):
    endpoint_result = api.devices.poe_details_v1(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_poe_details_v1_default_val(api, validator):
    try:
        assert is_valid_poe_details_v1(
            validator,
            poe_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_supervisor_card_detail_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4500eb13516155a28570e542dcf10a91_v2_3_7_9').validate(obj)
    return True


def get_supervisor_card_detail_v1(api):
    endpoint_result = api.devices.get_supervisor_card_detail_v1(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_supervisor_card_detail_v1(api, validator):
    try:
        assert is_valid_get_supervisor_card_detail_v1(
            validator,
            get_supervisor_card_detail_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_supervisor_card_detail_v1_default_val(api):
    endpoint_result = api.devices.get_supervisor_card_detail_v1(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_supervisor_card_detail_v1_default_val(api, validator):
    try:
        assert is_valid_get_supervisor_card_detail_v1(
            validator,
            get_supervisor_card_detail_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_management_address_v1(json_schema_validate, obj):
    json_schema_validate('jsd_39cb98464ddb5ee9ba7ebb4428443ba9_v2_3_7_9').validate(obj)
    return True


def update_device_management_address_v1(api):
    endpoint_result = api.devices.update_device_management_address_v1(
        active_validation=True,
        deviceid='string',
        newIP='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_management_address_v1(api, validator):
    try:
        assert is_valid_update_device_management_address_v1(
            validator,
            update_device_management_address_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_management_address_v1_default_val(api):
    endpoint_result = api.devices.update_device_management_address_v1(
        active_validation=True,
        deviceid='string',
        newIP=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_management_address_v1_default_val(api, validator):
    try:
        assert is_valid_update_device_management_address_v1(
            validator,
            update_device_management_address_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_358d86f657f8592f97014d2ebf8d37ac_v2_3_7_9').validate(obj)
    return True


def get_device_by_id_v1(api):
    endpoint_result = api.devices.get_device_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_id_v1(api, validator):
    try:
        assert is_valid_get_device_by_id_v1(
            validator,
            get_device_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_by_id_v1_default_val(api):
    endpoint_result = api.devices.get_device_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_by_id_v1(
            validator,
            get_device_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_003e01233fa258e393239c4b41882806_v2_3_7_9').validate(obj)
    return True


def delete_device_by_id_v1(api):
    endpoint_result = api.devices.delete_device_by_id_v1(
        clean_config=True,
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_device_by_id_v1(api, validator):
    try:
        assert is_valid_delete_device_by_id_v1(
            validator,
            delete_device_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_by_id_v1_default_val(api):
    endpoint_result = api.devices.delete_device_by_id_v1(
        clean_config=None,
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_device_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_device_by_id_v1(
            validator,
            delete_device_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_summary_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fe0153ca24205608b8741d51f5a6d54a_v2_3_7_9').validate(obj)
    return True


def get_device_summary_v1(api):
    endpoint_result = api.devices.get_device_summary_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_summary_v1(api, validator):
    try:
        assert is_valid_get_device_summary_v1(
            validator,
            get_device_summary_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_summary_v1_default_val(api):
    endpoint_result = api.devices.get_device_summary_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_summary_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_summary_v1(
            validator,
            get_device_summary_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_polling_interval_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f90daf1c279351f884ba3198d3b2d641_v2_3_7_9').validate(obj)
    return True


def get_polling_interval_by_id_v1(api):
    endpoint_result = api.devices.get_polling_interval_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_by_id_v1(api, validator):
    try:
        assert is_valid_get_polling_interval_by_id_v1(
            validator,
            get_polling_interval_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_polling_interval_by_id_v1_default_val(api):
    endpoint_result = api.devices.get_polling_interval_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_polling_interval_by_id_v1(
            validator,
            get_polling_interval_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_organization_list_for_meraki_v1(json_schema_validate, obj):
    json_schema_validate('jsd_790b4ba6d23d5e7eb62cbba4c9e1a29d_v2_3_7_9').validate(obj)
    return True


def get_organization_list_for_meraki_v1(api):
    endpoint_result = api.devices.get_organization_list_for_meraki_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_organization_list_for_meraki_v1(api, validator):
    try:
        assert is_valid_get_organization_list_for_meraki_v1(
            validator,
            get_organization_list_for_meraki_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_organization_list_for_meraki_v1_default_val(api):
    endpoint_result = api.devices.get_organization_list_for_meraki_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_organization_list_for_meraki_v1_default_val(api, validator):
    try:
        assert is_valid_get_organization_list_for_meraki_v1(
            validator,
            get_organization_list_for_meraki_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_vlans_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fd5fb603cba6523abb25c8ec131fbb8b_v2_3_7_9').validate(obj)
    return True


def get_device_interface_vlans_v1(api):
    endpoint_result = api.devices.get_device_interface_vlans_v1(
        id='string',
        interface_type='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_vlans_v1(api, validator):
    try:
        assert is_valid_get_device_interface_vlans_v1(
            validator,
            get_device_interface_vlans_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_interface_vlans_v1_default_val(api):
    endpoint_result = api.devices.get_device_interface_vlans_v1(
        id='string',
        interface_type=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_vlans_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_interface_vlans_v1(
            validator,
            get_device_interface_vlans_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_wireless_lan_controller_details_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c01ee650fcf858789ca00c8deda969b9_v2_3_7_9').validate(obj)
    return True


def get_wireless_lan_controller_details_by_id_v1(api):
    endpoint_result = api.devices.get_wireless_lan_controller_details_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_wireless_lan_controller_details_by_id_v1(api, validator):
    try:
        assert is_valid_get_wireless_lan_controller_details_by_id_v1(
            validator,
            get_wireless_lan_controller_details_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_wireless_lan_controller_details_by_id_v1_default_val(api):
    endpoint_result = api.devices.get_wireless_lan_controller_details_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_wireless_lan_controller_details_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_wireless_lan_controller_details_by_id_v1(
            validator,
            get_wireless_lan_controller_details_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_config_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5af0bbf34adb5146b931ec874fc2cc40_v2_3_7_9').validate(obj)
    return True


def get_device_config_by_id_v1(api):
    endpoint_result = api.devices.get_device_config_by_id_v1(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_by_id_v1(api, validator):
    try:
        assert is_valid_get_device_config_by_id_v1(
            validator,
            get_device_config_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_config_by_id_v1_default_val(api):
    endpoint_result = api.devices.get_device_config_by_id_v1(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_config_by_id_v1(
            validator,
            get_device_config_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device_by_pagination_range_v1(json_schema_validate, obj):
    json_schema_validate('jsd_60d7b6ce5abd5dad837e22ace817a6f0_v2_3_7_9').validate(obj)
    return True


def get_network_device_by_pagination_range_v1(api):
    endpoint_result = api.devices.get_network_device_by_pagination_range_v1(
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_pagination_range_v1(api, validator):
    try:
        assert is_valid_get_network_device_by_pagination_range_v1(
            validator,
            get_network_device_by_pagination_range_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_device_by_pagination_range_v1_default_val(api):
    endpoint_result = api.devices.get_network_device_by_pagination_range_v1(
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_pagination_range_v1_default_val(api, validator):
    try:
        assert is_valid_get_network_device_by_pagination_range_v1(
            validator,
            get_network_device_by_pagination_range_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_maintenance_schedule_for_network_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c1dae5c13e6959348fe1fe0652958647_v2_3_7_9').validate(obj)
    return True


def create_maintenance_schedule_for_network_devices_v1(api):
    endpoint_result = api.devices.create_maintenance_schedule_for_network_devices_v1(
        active_validation=True,
        description='string',
        maintenanceSchedule={'startTime': 0, 'endTime': 0, 'recurrence': {'interval': 0, 'recurrenceEndTime': 0}},
        networkDeviceIds=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_create_maintenance_schedule_for_network_devices_v1(api, validator):
    try:
        assert is_valid_create_maintenance_schedule_for_network_devices_v1(
            validator,
            create_maintenance_schedule_for_network_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_maintenance_schedule_for_network_devices_v1_default_val(api):
    endpoint_result = api.devices.create_maintenance_schedule_for_network_devices_v1(
        active_validation=True,
        description=None,
        maintenanceSchedule=None,
        networkDeviceIds=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_create_maintenance_schedule_for_network_devices_v1_default_val(api, validator):
    try:
        assert is_valid_create_maintenance_schedule_for_network_devices_v1(
            validator,
            create_maintenance_schedule_for_network_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_scheduled_maintenance_windows_for_network_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a90a937a8af85fbfa73d607be7ebafc2_v2_3_7_9').validate(obj)
    return True


def retrieve_scheduled_maintenance_windows_for_network_devices_v1(api):
    endpoint_result = api.devices.retrieve_scheduled_maintenance_windows_for_network_devices_v1(
        limit='string',
        network_device_ids='string',
        offset='string',
        order='string',
        sort_by='string',
        status='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieve_scheduled_maintenance_windows_for_network_devices_v1(api, validator):
    try:
        assert is_valid_retrieve_scheduled_maintenance_windows_for_network_devices_v1(
            validator,
            retrieve_scheduled_maintenance_windows_for_network_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_scheduled_maintenance_windows_for_network_devices_v1_default_val(api):
    endpoint_result = api.devices.retrieve_scheduled_maintenance_windows_for_network_devices_v1(
        limit=None,
        network_device_ids=None,
        offset=None,
        order=None,
        sort_by=None,
        status=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieve_scheduled_maintenance_windows_for_network_devices_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_scheduled_maintenance_windows_for_network_devices_v1(
            validator,
            retrieve_scheduled_maintenance_windows_for_network_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_total_number_of_scheduled_maintenance_windows_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c0a858b81cc65ae4b0eb0e69995b8e8c_v2_3_7_9').validate(obj)
    return True


def retrieve_the_total_number_of_scheduled_maintenance_windows_v1(api):
    endpoint_result = api.devices.retrieve_the_total_number_of_scheduled_maintenance_windows_v1(
        network_device_ids='string',
        status='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieve_the_total_number_of_scheduled_maintenance_windows_v1(api, validator):
    try:
        assert is_valid_retrieve_the_total_number_of_scheduled_maintenance_windows_v1(
            validator,
            retrieve_the_total_number_of_scheduled_maintenance_windows_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_total_number_of_scheduled_maintenance_windows_v1_default_val(api):
    endpoint_result = api.devices.retrieve_the_total_number_of_scheduled_maintenance_windows_v1(
        network_device_ids=None,
        status=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieve_the_total_number_of_scheduled_maintenance_windows_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_total_number_of_scheduled_maintenance_windows_v1(
            validator,
            retrieve_the_total_number_of_scheduled_maintenance_windows_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_the_maintenance_schedule_information_v1(json_schema_validate, obj):
    json_schema_validate('jsd_116e5bb87a955e33a7ee46f1085fd880_v2_3_7_9').validate(obj)
    return True


def updates_the_maintenance_schedule_information_v1(api):
    endpoint_result = api.devices.updates_the_maintenance_schedule_information_v1(
        active_validation=True,
        description='string',
        id='string',
        maintenanceSchedule={'startTime': 0, 'endTime': 0, 'recurrence': {'interval': 0, 'recurrenceEndTime': 0}},
        networkDeviceIds=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_updates_the_maintenance_schedule_information_v1(api, validator):
    try:
        assert is_valid_updates_the_maintenance_schedule_information_v1(
            validator,
            updates_the_maintenance_schedule_information_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_the_maintenance_schedule_information_v1_default_val(api):
    endpoint_result = api.devices.updates_the_maintenance_schedule_information_v1(
        active_validation=True,
        description=None,
        id='string',
        maintenanceSchedule=None,
        networkDeviceIds=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_updates_the_maintenance_schedule_information_v1_default_val(api, validator):
    try:
        assert is_valid_updates_the_maintenance_schedule_information_v1(
            validator,
            updates_the_maintenance_schedule_information_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_maintenance_schedule_information_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ce5b6297263a50feb20e532932d39580_v2_3_7_9').validate(obj)
    return True


def retrieves_the_maintenance_schedule_information_v1(api):
    endpoint_result = api.devices.retrieves_the_maintenance_schedule_information_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_maintenance_schedule_information_v1(api, validator):
    try:
        assert is_valid_retrieves_the_maintenance_schedule_information_v1(
            validator,
            retrieves_the_maintenance_schedule_information_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_maintenance_schedule_information_v1_default_val(api):
    endpoint_result = api.devices.retrieves_the_maintenance_schedule_information_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_the_maintenance_schedule_information_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_maintenance_schedule_information_v1(
            validator,
            retrieves_the_maintenance_schedule_information_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_maintenance_schedule_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8ff24d0609c3514fbb7377f5dbd70d0a_v2_3_7_9').validate(obj)
    return True


def delete_maintenance_schedule_v1(api):
    endpoint_result = api.devices.delete_maintenance_schedule_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_maintenance_schedule_v1(api, validator):
    try:
        assert is_valid_delete_maintenance_schedule_v1(
            validator,
            delete_maintenance_schedule_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_maintenance_schedule_v1_default_val(api):
    endpoint_result = api.devices.delete_maintenance_schedule_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_maintenance_schedule_v1_default_val(api, validator):
    try:
        assert is_valid_delete_maintenance_schedule_v1(
            validator,
            delete_maintenance_schedule_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_network_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_87e78bc218325565becdd907ff2e4e30_v2_3_7_9').validate(obj)
    return True


def retrieve_network_devices_v1(api):
    endpoint_result = api.devices.retrieve_network_devices_v1(
        family='string',
        id='string',
        limit='string',
        management_address='string',
        management_state='string',
        offset='string',
        order='string',
        reachability_status='string',
        role='string',
        serial_number='string',
        sort_by='string',
        stack_device='string',
        status='string',
        views='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieve_network_devices_v1(api, validator):
    try:
        assert is_valid_retrieve_network_devices_v1(
            validator,
            retrieve_network_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_network_devices_v1_default_val(api):
    endpoint_result = api.devices.retrieve_network_devices_v1(
        family=None,
        id=None,
        limit=None,
        management_address=None,
        management_state=None,
        offset=None,
        order=None,
        reachability_status=None,
        role=None,
        serial_number=None,
        sort_by=None,
        stack_device=None,
        status=None,
        views=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieve_network_devices_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_network_devices_v1(
            validator,
            retrieve_network_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_the_number_of_network_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fc60c9c2ca32545fab1bbe540a99c218_v2_3_7_9').validate(obj)
    return True


def count_the_number_of_network_devices_v1(api):
    endpoint_result = api.devices.count_the_number_of_network_devices_v1(
        family='string',
        id='string',
        management_address='string',
        management_state='string',
        reachability_status='string',
        role='string',
        serial_number='string',
        stack_device='string',
        status='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_count_the_number_of_network_devices_v1(api, validator):
    try:
        assert is_valid_count_the_number_of_network_devices_v1(
            validator,
            count_the_number_of_network_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_the_number_of_network_devices_v1_default_val(api):
    endpoint_result = api.devices.count_the_number_of_network_devices_v1(
        family=None,
        id=None,
        management_address=None,
        management_state=None,
        reachability_status=None,
        role=None,
        serial_number=None,
        stack_device=None,
        status=None
    )
    return endpoint_result


@pytest.mark.devices
def test_count_the_number_of_network_devices_v1_default_val(api, validator):
    try:
        assert is_valid_count_the_number_of_network_devices_v1(
            validator,
            count_the_number_of_network_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_device_with_configuration_cleanup_v1(json_schema_validate, obj):
    json_schema_validate('jsd_63a18e761ac8592e9a5c4e0bb2308cf0_v2_3_7_9').validate(obj)
    return True


def delete_network_device_with_configuration_cleanup_v1(api):
    endpoint_result = api.devices.delete_network_device_with_configuration_cleanup_v1(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_network_device_with_configuration_cleanup_v1(api, validator):
    try:
        assert is_valid_delete_network_device_with_configuration_cleanup_v1(
            validator,
            delete_network_device_with_configuration_cleanup_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_device_with_configuration_cleanup_v1_default_val(api):
    endpoint_result = api.devices.delete_network_device_with_configuration_cleanup_v1(
        active_validation=True,
        id=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_network_device_with_configuration_cleanup_v1_default_val(api, validator):
    try:
        assert is_valid_delete_network_device_with_configuration_cleanup_v1(
            validator,
            delete_network_device_with_configuration_cleanup_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_network_device_without_configuration_cleanup_v1(json_schema_validate, obj):
    json_schema_validate('jsd_115ce6c2c14553f9a4a88f66a04c21c4_v2_3_7_9').validate(obj)
    return True


def delete_a_network_device_without_configuration_cleanup_v1(api):
    endpoint_result = api.devices.delete_a_network_device_without_configuration_cleanup_v1(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_a_network_device_without_configuration_cleanup_v1(api, validator):
    try:
        assert is_valid_delete_a_network_device_without_configuration_cleanup_v1(
            validator,
            delete_a_network_device_without_configuration_cleanup_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_network_device_without_configuration_cleanup_v1_default_val(api):
    endpoint_result = api.devices.delete_a_network_device_without_configuration_cleanup_v1(
        active_validation=True,
        id=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_a_network_device_without_configuration_cleanup_v1_default_val(api, validator):
    try:
        assert is_valid_delete_a_network_device_without_configuration_cleanup_v1(
            validator,
            delete_a_network_device_without_configuration_cleanup_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_network_devices_with_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9fff3662537e538f82bfb5809e30b3df_v2_3_7_9').validate(obj)
    return True


def query_network_devices_with_filters_v1(api):
    endpoint_result = api.devices.query_network_devices_with_filters_v1(
        active_validation=True,
        filter={'logicalOperator': 'string', 'filters': [{'key': 'string', 'operator': 'string', 'value': {}}]},
        page={'sortBy': {'name': 'string', 'order': 'string'}, 'limit': 0, 'offset': 0},
        payload=None,
        views=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_query_network_devices_with_filters_v1(api, validator):
    try:
        assert is_valid_query_network_devices_with_filters_v1(
            validator,
            query_network_devices_with_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def query_network_devices_with_filters_v1_default_val(api):
    endpoint_result = api.devices.query_network_devices_with_filters_v1(
        active_validation=True,
        filter=None,
        page=None,
        payload=None,
        views=None
    )
    return endpoint_result


@pytest.mark.devices
def test_query_network_devices_with_filters_v1_default_val(api, validator):
    try:
        assert is_valid_query_network_devices_with_filters_v1(
            validator,
            query_network_devices_with_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_the_number_of_network_devices_with_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2a7283357c1657bf8ccb3d32a96249d4_v2_3_7_9').validate(obj)
    return True


def count_the_number_of_network_devices_with_filters_v1(api):
    endpoint_result = api.devices.count_the_number_of_network_devices_with_filters_v1(
        active_validation=True,
        filter={'logicalOperator': 'string', 'filters': [{'key': 'string', 'operator': 'string', 'value': {}}]},
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_count_the_number_of_network_devices_with_filters_v1(api, validator):
    try:
        assert is_valid_count_the_number_of_network_devices_with_filters_v1(
            validator,
            count_the_number_of_network_devices_with_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_the_number_of_network_devices_with_filters_v1_default_val(api):
    endpoint_result = api.devices.count_the_number_of_network_devices_with_filters_v1(
        active_validation=True,
        filter=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_count_the_number_of_network_devices_with_filters_v1_default_val(api, validator):
    try:
        assert is_valid_count_the_number_of_network_devices_with_filters_v1(
            validator,
            count_the_number_of_network_devices_with_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_global_resync_interval_v1(json_schema_validate, obj):
    json_schema_validate('jsd_37537a64bd4956649de3a61e10f0637e_v2_3_7_9').validate(obj)
    return True


def update_global_resync_interval_v1(api):
    endpoint_result = api.devices.update_global_resync_interval_v1(
        active_validation=True,
        interval=0,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_global_resync_interval_v1(api, validator):
    try:
        assert is_valid_update_global_resync_interval_v1(
            validator,
            update_global_resync_interval_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_global_resync_interval_v1_default_val(api):
    endpoint_result = api.devices.update_global_resync_interval_v1(
        active_validation=True,
        interval=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_global_resync_interval_v1_default_val(api, validator):
    try:
        assert is_valid_update_global_resync_interval_v1(
            validator,
            update_global_resync_interval_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_override_resync_interval_v1(json_schema_validate, obj):
    json_schema_validate('jsd_dc239a9ab9e5562b93a45ea0b9708b84_v2_3_7_9').validate(obj)
    return True


def override_resync_interval_v1(api):
    endpoint_result = api.devices.override_resync_interval_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_override_resync_interval_v1(api, validator):
    try:
        assert is_valid_override_resync_interval_v1(
            validator,
            override_resync_interval_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def override_resync_interval_v1_default_val(api):
    endpoint_result = api.devices.override_resync_interval_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_override_resync_interval_v1_default_val(api, validator):
    try:
        assert is_valid_override_resync_interval_v1(
            validator,
            override_resync_interval_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_details_of_a_single_network_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9fc15032bbf55ec0bbdd3964c9f00089_v2_3_7_9').validate(obj)
    return True


def get_details_of_a_single_network_device_v1(api):
    endpoint_result = api.devices.get_details_of_a_single_network_device_v1(
        id='string',
        views='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_details_of_a_single_network_device_v1(api, validator):
    try:
        assert is_valid_get_details_of_a_single_network_device_v1(
            validator,
            get_details_of_a_single_network_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_details_of_a_single_network_device_v1_default_val(api):
    endpoint_result = api.devices.get_details_of_a_single_network_device_v1(
        id='string',
        views=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_details_of_a_single_network_device_v1_default_val(api, validator):
    try:
        assert is_valid_get_details_of_a_single_network_device_v1(
            validator,
            get_details_of_a_single_network_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_resync_interval_for_the_network_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fdfc828270d950ecb75480fe03f7d573_v2_3_7_9').validate(obj)
    return True


def update_resync_interval_for_the_network_device_v1(api):
    endpoint_result = api.devices.update_resync_interval_for_the_network_device_v1(
        active_validation=True,
        id='string',
        interval=0,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_resync_interval_for_the_network_device_v1(api, validator):
    try:
        assert is_valid_update_resync_interval_for_the_network_device_v1(
            validator,
            update_resync_interval_for_the_network_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_resync_interval_for_the_network_device_v1_default_val(api):
    endpoint_result = api.devices.update_resync_interval_for_the_network_device_v1(
        active_validation=True,
        id='string',
        interval=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_resync_interval_for_the_network_device_v1_default_val(api, validator):
    try:
        assert is_valid_update_resync_interval_for_the_network_device_v1(
            validator,
            update_resync_interval_for_the_network_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_resync_interval_for_the_network_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e56a4c0d91dd53ecb737da824115a050_v2_3_7_9').validate(obj)
    return True


def get_resync_interval_for_the_network_device_v1(api):
    endpoint_result = api.devices.get_resync_interval_for_the_network_device_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_resync_interval_for_the_network_device_v1(api, validator):
    try:
        assert is_valid_get_resync_interval_for_the_network_device_v1(
            validator,
            get_resync_interval_for_the_network_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_resync_interval_for_the_network_device_v1_default_val(api):
    endpoint_result = api.devices.get_resync_interval_for_the_network_device_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_resync_interval_for_the_network_device_v1_default_val(api, validator):
    try:
        assert is_valid_get_resync_interval_for_the_network_device_v1(
            validator,
            get_resync_interval_for_the_network_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_rogue_additional_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5c8354b61a36524cbb2e1037bd814807_v2_3_7_9').validate(obj)
    return True


def rogue_additional_details_v1(api):
    endpoint_result = api.devices.rogue_additional_details_v1(
        active_validation=True,
        endTime=0,
        limit=0,
        offset=0,
        payload=None,
        siteId=['string'],
        startTime=0,
        threatLevel=['string'],
        threatType=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_rogue_additional_details_v1(api, validator):
    try:
        assert is_valid_rogue_additional_details_v1(
            validator,
            rogue_additional_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def rogue_additional_details_v1_default_val(api):
    endpoint_result = api.devices.rogue_additional_details_v1(
        active_validation=True,
        endTime=None,
        limit=None,
        offset=None,
        payload=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None
    )
    return endpoint_result


@pytest.mark.devices
def test_rogue_additional_details_v1_default_val(api, validator):
    try:
        assert is_valid_rogue_additional_details_v1(
            validator,
            rogue_additional_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_rogue_additional_detail_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_29de4c9b685250dfa8556ab1ec20407c_v2_3_7_9').validate(obj)
    return True


def rogue_additional_detail_count_v1(api):
    endpoint_result = api.devices.rogue_additional_detail_count_v1(
        active_validation=True,
        endTime=0,
        payload=None,
        siteId=['string'],
        startTime=0,
        threatLevel=['string'],
        threatType=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_rogue_additional_detail_count_v1(api, validator):
    try:
        assert is_valid_rogue_additional_detail_count_v1(
            validator,
            rogue_additional_detail_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def rogue_additional_detail_count_v1_default_val(api):
    endpoint_result = api.devices.rogue_additional_detail_count_v1(
        active_validation=True,
        endTime=None,
        payload=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None
    )
    return endpoint_result


@pytest.mark.devices
def test_rogue_additional_detail_count_v1_default_val(api, validator):
    try:
        assert is_valid_rogue_additional_detail_count_v1(
            validator,
            rogue_additional_detail_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_start_wireless_rogue_ap_containment_v1(json_schema_validate, obj):
    json_schema_validate('jsd_48fe62979a925778bdb0a974a7d86a12_v2_3_7_9').validate(obj)
    return True


def start_wireless_rogue_ap_containment_v1(api):
    endpoint_result = api.devices.start_wireless_rogue_ap_containment_v1(
        active_validation=True,
        macAddress='string',
        payload=None,
        type=0
    )
    return endpoint_result


@pytest.mark.devices
def test_start_wireless_rogue_ap_containment_v1(api, validator):
    try:
        assert is_valid_start_wireless_rogue_ap_containment_v1(
            validator,
            start_wireless_rogue_ap_containment_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def start_wireless_rogue_ap_containment_v1_default_val(api):
    endpoint_result = api.devices.start_wireless_rogue_ap_containment_v1(
        active_validation=True,
        macAddress=None,
        payload=None,
        type=None
    )
    return endpoint_result


@pytest.mark.devices
def test_start_wireless_rogue_ap_containment_v1_default_val(api, validator):
    try:
        assert is_valid_start_wireless_rogue_ap_containment_v1(
            validator,
            start_wireless_rogue_ap_containment_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_wireless_rogue_ap_containment_status_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e81244d1a2d9513384d543f0362c35d1_v2_3_7_9').validate(obj)
    return True


def wireless_rogue_ap_containment_status_v1(api):
    endpoint_result = api.devices.wireless_rogue_ap_containment_status_v1(
        mac_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_wireless_rogue_ap_containment_status_v1(api, validator):
    try:
        assert is_valid_wireless_rogue_ap_containment_status_v1(
            validator,
            wireless_rogue_ap_containment_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def wireless_rogue_ap_containment_status_v1_default_val(api):
    endpoint_result = api.devices.wireless_rogue_ap_containment_status_v1(
        mac_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_wireless_rogue_ap_containment_status_v1_default_val(api, validator):
    try:
        assert is_valid_wireless_rogue_ap_containment_status_v1(
            validator,
            wireless_rogue_ap_containment_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_stop_wireless_rogue_ap_containment_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2d9ed5bba1155b9c8fe132640832f94e_v2_3_7_9').validate(obj)
    return True


def stop_wireless_rogue_ap_containment_v1(api):
    endpoint_result = api.devices.stop_wireless_rogue_ap_containment_v1(
        active_validation=True,
        macAddress='string',
        payload=None,
        type=0,
        wlcIp='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_stop_wireless_rogue_ap_containment_v1(api, validator):
    try:
        assert is_valid_stop_wireless_rogue_ap_containment_v1(
            validator,
            stop_wireless_rogue_ap_containment_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def stop_wireless_rogue_ap_containment_v1_default_val(api):
    endpoint_result = api.devices.stop_wireless_rogue_ap_containment_v1(
        active_validation=True,
        macAddress=None,
        payload=None,
        type=None,
        wlcIp=None
    )
    return endpoint_result


@pytest.mark.devices
def test_stop_wireless_rogue_ap_containment_v1_default_val(api, validator):
    try:
        assert is_valid_stop_wireless_rogue_ap_containment_v1(
            validator,
            stop_wireless_rogue_ap_containment_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_threat_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5f4ce55b5f235924903516ef31dc9e3c_v2_3_7_9').validate(obj)
    return True


def threat_details_v1(api):
    endpoint_result = api.devices.threat_details_v1(
        active_validation=True,
        endTime=0,
        isNewThreat=True,
        limit=0,
        offset=0,
        payload=None,
        siteId=['string'],
        startTime=0,
        threatLevel=['string'],
        threatType=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_threat_details_v1(api, validator):
    try:
        assert is_valid_threat_details_v1(
            validator,
            threat_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def threat_details_v1_default_val(api):
    endpoint_result = api.devices.threat_details_v1(
        active_validation=True,
        endTime=None,
        isNewThreat=None,
        limit=None,
        offset=None,
        payload=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None
    )
    return endpoint_result


@pytest.mark.devices
def test_threat_details_v1_default_val(api, validator):
    try:
        assert is_valid_threat_details_v1(
            validator,
            threat_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_threat_detail_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1137c7266d89581c9601b79b7304fda3_v2_3_7_9').validate(obj)
    return True


def threat_detail_count_v1(api):
    endpoint_result = api.devices.threat_detail_count_v1(
        active_validation=True,
        endTime=0,
        isNewThreat=True,
        limit=0,
        offset=0,
        payload=None,
        siteId=['string'],
        startTime=0,
        threatLevel=['string'],
        threatType=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_threat_detail_count_v1(api, validator):
    try:
        assert is_valid_threat_detail_count_v1(
            validator,
            threat_detail_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def threat_detail_count_v1_default_val(api):
    endpoint_result = api.devices.threat_detail_count_v1(
        active_validation=True,
        endTime=None,
        isNewThreat=None,
        limit=None,
        offset=None,
        payload=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None
    )
    return endpoint_result


@pytest.mark.devices
def test_threat_detail_count_v1_default_val(api, validator):
    try:
        assert is_valid_threat_detail_count_v1(
            validator,
            threat_detail_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_threat_levels_v1(json_schema_validate, obj):
    json_schema_validate('jsd_eb1bd16969ed5cee8eb0a208b7441edd_v2_3_7_9').validate(obj)
    return True


def get_threat_levels_v1(api):
    endpoint_result = api.devices.get_threat_levels_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_threat_levels_v1(api, validator):
    try:
        assert is_valid_get_threat_levels_v1(
            validator,
            get_threat_levels_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_threat_levels_v1_default_val(api):
    endpoint_result = api.devices.get_threat_levels_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_threat_levels_v1_default_val(api, validator):
    try:
        assert is_valid_get_threat_levels_v1(
            validator,
            get_threat_levels_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_allowed_mac_address_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6fdd36dd2454547096bb65df3755710f_v2_3_7_9').validate(obj)
    return True


def add_allowed_mac_address_v1(api):
    endpoint_result = api.devices.add_allowed_mac_address_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_add_allowed_mac_address_v1(api, validator):
    try:
        assert is_valid_add_allowed_mac_address_v1(
            validator,
            add_allowed_mac_address_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_allowed_mac_address_v1_default_val(api):
    endpoint_result = api.devices.add_allowed_mac_address_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_add_allowed_mac_address_v1_default_val(api, validator):
    try:
        assert is_valid_add_allowed_mac_address_v1(
            validator,
            add_allowed_mac_address_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_allowed_mac_address_v1(json_schema_validate, obj):
    json_schema_validate('jsd_777b22e597335a8ba98dc758699726b3_v2_3_7_9').validate(obj)
    return True


def get_allowed_mac_address_v1(api):
    endpoint_result = api.devices.get_allowed_mac_address_v1(
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_allowed_mac_address_v1(api, validator):
    try:
        assert is_valid_get_allowed_mac_address_v1(
            validator,
            get_allowed_mac_address_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_allowed_mac_address_v1_default_val(api):
    endpoint_result = api.devices.get_allowed_mac_address_v1(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_allowed_mac_address_v1_default_val(api, validator):
    try:
        assert is_valid_get_allowed_mac_address_v1(
            validator,
            get_allowed_mac_address_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_allowed_mac_address_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f1a062d6eeac569b9ab40cf2d3b0ffa7_v2_3_7_9').validate(obj)
    return True


def get_allowed_mac_address_count_v1(api):
    endpoint_result = api.devices.get_allowed_mac_address_count_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_allowed_mac_address_count_v1(api, validator):
    try:
        assert is_valid_get_allowed_mac_address_count_v1(
            validator,
            get_allowed_mac_address_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_allowed_mac_address_count_v1_default_val(api):
    endpoint_result = api.devices.get_allowed_mac_address_count_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_allowed_mac_address_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_allowed_mac_address_count_v1(
            validator,
            get_allowed_mac_address_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_allowed_mac_address_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2dda7feeaa3a564d97eb01f9843ed720_v2_3_7_9').validate(obj)
    return True


def remove_allowed_mac_address_v1(api):
    endpoint_result = api.devices.remove_allowed_mac_address_v1(
        mac_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_remove_allowed_mac_address_v1(api, validator):
    try:
        assert is_valid_remove_allowed_mac_address_v1(
            validator,
            remove_allowed_mac_address_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def remove_allowed_mac_address_v1_default_val(api):
    endpoint_result = api.devices.remove_allowed_mac_address_v1(
        mac_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_remove_allowed_mac_address_v1_default_val(api, validator):
    try:
        assert is_valid_remove_allowed_mac_address_v1(
            validator,
            remove_allowed_mac_address_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_threat_summary_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e6eed78cb55d51a1bfe669729df25689_v2_3_7_9').validate(obj)
    return True


def threat_summary_v1(api):
    endpoint_result = api.devices.threat_summary_v1(
        active_validation=True,
        endTime=0,
        payload=None,
        siteId=['string'],
        startTime=0,
        threatLevel=['string'],
        threatType=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_threat_summary_v1(api, validator):
    try:
        assert is_valid_threat_summary_v1(
            validator,
            threat_summary_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def threat_summary_v1_default_val(api):
    endpoint_result = api.devices.threat_summary_v1(
        active_validation=True,
        endTime=None,
        payload=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None
    )
    return endpoint_result


@pytest.mark.devices
def test_threat_summary_v1_default_val(api, validator):
    try:
        assert is_valid_threat_summary_v1(
            validator,
            threat_summary_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_threat_types_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c1720793d71052418cadda1f9fd5f977_v2_3_7_9').validate(obj)
    return True


def get_threat_types_v1(api):
    endpoint_result = api.devices.get_threat_types_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_threat_types_v1(api, validator):
    try:
        assert is_valid_get_threat_types_v1(
            validator,
            get_threat_types_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_threat_types_v1_default_val(api):
    endpoint_result = api.devices.get_threat_types_v1(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_threat_types_v1_default_val(api, validator):
    try:
        assert is_valid_get_threat_types_v1(
            validator,
            get_threat_types_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_stats_info_v2(json_schema_validate, obj):
    json_schema_validate('jsd_a9e0722d184658c592bd130ff03e1dde_v2_3_7_9').validate(obj)
    return True


def get_device_interface_stats_info_v2(api):
    endpoint_result = api.devices.get_device_interface_stats_info_v2(
        active_validation=True,
        device_id='string',
        endTime=0,
        payload=None,
        query={'fields': [{}], 'filters': [{'key': 'string', 'operator': 'string', 'value': 'string'}], 'page': {'limit': 0, 'offset': 0, 'orderBy': [{'name': 'string', 'order': 'string'}]}},
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_stats_info_v2(api, validator):
    try:
        assert is_valid_get_device_interface_stats_info_v2(
            validator,
            get_device_interface_stats_info_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_interface_stats_info_v2_default_val(api):
    endpoint_result = api.devices.get_device_interface_stats_info_v2(
        active_validation=True,
        device_id='string',
        endTime=None,
        payload=None,
        query=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_stats_info_v2_default_val(api, validator):
    try:
        assert is_valid_get_device_interface_stats_info_v2(
            validator,
            get_device_interface_stats_info_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

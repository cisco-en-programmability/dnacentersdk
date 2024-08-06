# -*- coding: utf-8 -*-
"""DNACenterAPI devices API fixtures and tests.

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


def is_valid_gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(json_schema_validate, obj):
    json_schema_validate('jsd_0928a421626459dcbe382c43ffcbddae_v2_3_7_6').validate(obj)
    return True


def gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(api):
    endpoint_result = api.devices.gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0,
        views=['string']
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(api, validator):
    try:
        assert is_valid_gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
            validator,
            gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_default_val(api):
    endpoint_result = api.devices.gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
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
def test_gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_default_val(api, validator):
    try:
        assert is_valid_gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
            validator,
            gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_assurance_events(json_schema_validate, obj):
    json_schema_validate('jsd_99114bc891de5102872b3415d23b7a0b_v2_3_7_6').validate(obj)
    return True


def query_assurance_events(api):
    endpoint_result = api.devices.query_assurance_events(
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
def test_query_assurance_events(api, validator):
    try:
        assert is_valid_query_assurance_events(
            validator,
            query_assurance_events(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def query_assurance_events_default_val(api):
    endpoint_result = api.devices.query_assurance_events(
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
def test_query_assurance_events_default_val(api, validator):
    try:
        assert is_valid_query_assurance_events(
            validator,
            query_assurance_events_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_the_number_of_events(json_schema_validate, obj):
    json_schema_validate('jsd_915abf597583520eb0a7a0b24e5c7f69_v2_3_7_6').validate(obj)
    return True


def count_the_number_of_events(api):
    endpoint_result = api.devices.count_the_number_of_events(
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
def test_count_the_number_of_events(api, validator):
    try:
        assert is_valid_count_the_number_of_events(
            validator,
            count_the_number_of_events(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_the_number_of_events_default_val(api):
    endpoint_result = api.devices.count_the_number_of_events(
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
def test_count_the_number_of_events_default_val(api, validator):
    try:
        assert is_valid_count_the_number_of_events(
            validator,
            count_the_number_of_events_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_assurance_events_with_filters(json_schema_validate, obj):
    json_schema_validate('jsd_ef94c2c20ba15fd38e129ac75067de1e_v2_3_7_6').validate(obj)
    return True


def query_assurance_events_with_filters(api):
    endpoint_result = api.devices.query_assurance_events_with_filters(
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
def test_query_assurance_events_with_filters(api, validator):
    try:
        assert is_valid_query_assurance_events_with_filters(
            validator,
            query_assurance_events_with_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def query_assurance_events_with_filters_default_val(api):
    endpoint_result = api.devices.query_assurance_events_with_filters(
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
def test_query_assurance_events_with_filters_default_val(api, validator):
    try:
        assert is_valid_query_assurance_events_with_filters(
            validator,
            query_assurance_events_with_filters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_the_number_of_events_with_filters(json_schema_validate, obj):
    json_schema_validate('jsd_a91eed12dfc85dbdaacab22e6e9f04a5_v2_3_7_6').validate(obj)
    return True


def count_the_number_of_events_with_filters(api):
    endpoint_result = api.devices.count_the_number_of_events_with_filters(
        active_validation=True,
        deviceFamily=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_count_the_number_of_events_with_filters(api, validator):
    try:
        assert is_valid_count_the_number_of_events_with_filters(
            validator,
            count_the_number_of_events_with_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_the_number_of_events_with_filters_default_val(api):
    endpoint_result = api.devices.count_the_number_of_events_with_filters(
        active_validation=True,
        deviceFamily=None,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.devices
def test_count_the_number_of_events_with_filters_default_val(api, validator):
    try:
        assert is_valid_count_the_number_of_events_with_filters(
            validator,
            count_the_number_of_events_with_filters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_details_of_a_single_assurance_event(json_schema_validate, obj):
    json_schema_validate('jsd_031a36092e78528b9bd8730c93b5412d_v2_3_7_6').validate(obj)
    return True


def get_details_of_a_single_assurance_event(api):
    endpoint_result = api.devices.get_details_of_a_single_assurance_event(
        attribute='string',
        id='string',
        view='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_details_of_a_single_assurance_event(api, validator):
    try:
        assert is_valid_get_details_of_a_single_assurance_event(
            validator,
            get_details_of_a_single_assurance_event(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_details_of_a_single_assurance_event_default_val(api):
    endpoint_result = api.devices.get_details_of_a_single_assurance_event(
        attribute=None,
        id='string',
        view=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_details_of_a_single_assurance_event_default_val(api, validator):
    try:
        assert is_valid_get_details_of_a_single_assurance_event(
            validator,
            get_details_of_a_single_assurance_event_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_list_of_child_events_for_the_given_wireless_client_event(json_schema_validate, obj):
    json_schema_validate('jsd_d3cf1ace30895351b5b8c3f7919b972e_v2_3_7_6').validate(obj)
    return True


def get_list_of_child_events_for_the_given_wireless_client_event(api):
    endpoint_result = api.devices.get_list_of_child_events_for_the_given_wireless_client_event(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_list_of_child_events_for_the_given_wireless_client_event(api, validator):
    try:
        assert is_valid_get_list_of_child_events_for_the_given_wireless_client_event(
            validator,
            get_list_of_child_events_for_the_given_wireless_client_event(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_list_of_child_events_for_the_given_wireless_client_event_default_val(api):
    endpoint_result = api.devices.get_list_of_child_events_for_the_given_wireless_client_event(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_list_of_child_events_for_the_given_wireless_client_event_default_val(api, validator):
    try:
        assert is_valid_get_list_of_child_events_for_the_given_wireless_client_event(
            validator,
            get_list_of_child_events_for_the_given_wireless_client_event_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_interfaces_along_with_statistics_data_from_all_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_1912fc7a61a854f2b2015d3f1c059ce9_v2_3_7_6').validate(obj)
    return True


def gets_interfaces_along_with_statistics_data_from_all_network_devices(api):
    endpoint_result = api.devices.gets_interfaces_along_with_statistics_data_from_all_network_devices(
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
def test_gets_interfaces_along_with_statistics_data_from_all_network_devices(api, validator):
    try:
        assert is_valid_gets_interfaces_along_with_statistics_data_from_all_network_devices(
            validator,
            gets_interfaces_along_with_statistics_data_from_all_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_interfaces_along_with_statistics_data_from_all_network_devices_default_val(api):
    endpoint_result = api.devices.gets_interfaces_along_with_statistics_data_from_all_network_devices(
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
def test_gets_interfaces_along_with_statistics_data_from_all_network_devices_default_val(api, validator):
    try:
        assert is_valid_gets_interfaces_along_with_statistics_data_from_all_network_devices(
            validator,
            gets_interfaces_along_with_statistics_data_from_all_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count(json_schema_validate, obj):
    json_schema_validate('jsd_412775760f4b503bbce76ebb802f0ad7_v2_3_7_6').validate(obj)
    return True


def gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count(api):
    endpoint_result = api.devices.gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count(
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
def test_gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count(api, validator):
    try:
        assert is_valid_gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count(
            validator,
            gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_default_val(api):
    endpoint_result = api.devices.gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count(
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
def test_gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_default_val(api, validator):
    try:
        assert is_valid_gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count(
            validator,
            gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(json_schema_validate, obj):
    json_schema_validate('jsd_f667322836d5527482ad2100bec7feb4_v2_3_7_6').validate(obj)
    return True


def gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(api):
    endpoint_result = api.devices.gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
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
def test_gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(api, validator):
    try:
        assert is_valid_gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
            validator,
            gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_default_val(api):
    endpoint_result = api.devices.gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
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
def test_gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_default_val(api, validator):
    try:
        assert is_valid_gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
            validator,
            gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_the_total_interfaces_count_across_the_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_b0b146a144a65aa296b8b939c2926158_v2_3_7_6').validate(obj)
    return True


def the_total_interfaces_count_across_the_network_devices(api):
    endpoint_result = api.devices.the_total_interfaces_count_across_the_network_devices(
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
def test_the_total_interfaces_count_across_the_network_devices(api, validator):
    try:
        assert is_valid_the_total_interfaces_count_across_the_network_devices(
            validator,
            the_total_interfaces_count_across_the_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def the_total_interfaces_count_across_the_network_devices_default_val(api):
    endpoint_result = api.devices.the_total_interfaces_count_across_the_network_devices(
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
def test_the_total_interfaces_count_across_the_network_devices_default_val(api, validator):
    try:
        assert is_valid_the_total_interfaces_count_across_the_network_devices(
            validator,
            the_total_interfaces_count_across_the_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data(json_schema_validate, obj):
    json_schema_validate('jsd_56adcdf890505770af113b18b30c1b5f_v2_3_7_6').validate(obj)
    return True


def get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data(api):
    endpoint_result = api.devices.get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data(
        attribute='string',
        end_time=0,
        id='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data(api, validator):
    try:
        assert is_valid_get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data(
            validator,
            get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data_default_val(api):
    endpoint_result = api.devices.get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data(
        attribute=None,
        end_time=None,
        id='string',
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data_default_val(api, validator):
    try:
        assert is_valid_get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data(
            validator,
            get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_network_device_details_based_on_the_provided_query_parameters(json_schema_validate, obj):
    json_schema_validate('jsd_71c7314fc7e15dab859eb66f45b1e95a_v2_3_7_6').validate(obj)
    return True


def gets_the_network_device_details_based_on_the_provided_query_parameters(api):
    endpoint_result = api.devices.gets_the_network_device_details_based_on_the_provided_query_parameters(
        attribute='string',
        end_time=0,
        family='string',
        health_score='string',
        id='string',
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
        type='string',
        view='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_network_device_details_based_on_the_provided_query_parameters(api, validator):
    try:
        assert is_valid_gets_the_network_device_details_based_on_the_provided_query_parameters(
            validator,
            gets_the_network_device_details_based_on_the_provided_query_parameters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_network_device_details_based_on_the_provided_query_parameters_default_val(api):
    endpoint_result = api.devices.gets_the_network_device_details_based_on_the_provided_query_parameters(
        attribute=None,
        end_time=None,
        family=None,
        health_score=None,
        id=None,
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
        type=None,
        view=None
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_network_device_details_based_on_the_provided_query_parameters_default_val(api, validator):
    try:
        assert is_valid_gets_the_network_device_details_based_on_the_provided_query_parameters(
            validator,
            gets_the_network_device_details_based_on_the_provided_query_parameters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_total_network_device_counts_based_on_the_provided_query_parameters(json_schema_validate, obj):
    json_schema_validate('jsd_3d8782f4d285506d9e1391f0190ff738_v2_3_7_6').validate(obj)
    return True


def gets_the_total_network_device_counts_based_on_the_provided_query_parameters(api):
    endpoint_result = api.devices.gets_the_total_network_device_counts_based_on_the_provided_query_parameters(
        attribute='string',
        end_time=0,
        family='string',
        health_score='string',
        id='string',
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
        type='string',
        view='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_total_network_device_counts_based_on_the_provided_query_parameters(api, validator):
    try:
        assert is_valid_gets_the_total_network_device_counts_based_on_the_provided_query_parameters(
            validator,
            gets_the_total_network_device_counts_based_on_the_provided_query_parameters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_total_network_device_counts_based_on_the_provided_query_parameters_default_val(api):
    endpoint_result = api.devices.gets_the_total_network_device_counts_based_on_the_provided_query_parameters(
        attribute=None,
        end_time=None,
        family=None,
        health_score=None,
        id=None,
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
        type=None,
        view=None
    )
    return endpoint_result


@pytest.mark.devices
def test_gets_the_total_network_device_counts_based_on_the_provided_query_parameters_default_val(api, validator):
    try:
        assert is_valid_gets_the_total_network_device_counts_based_on_the_provided_query_parameters(
            validator,
            gets_the_total_network_device_counts_based_on_the_provided_query_parameters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(json_schema_validate, obj):
    json_schema_validate('jsd_8bd1c59e9be75ac4a40decaa95ee9efd_v2_3_7_6').validate(obj)
    return True


def gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(api):
    endpoint_result = api.devices.gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
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
def test_gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(api, validator):
    try:
        assert is_valid_gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
            validator,
            gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_default_val(api):
    endpoint_result = api.devices.gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
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
def test_gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_default_val(api, validator):
    try:
        assert is_valid_gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
            validator,
            gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_summary_analytics_data_related_to_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_06bb7c52e5225e9398a006fecf4da06f_v2_3_7_6').validate(obj)
    return True


def gets_the_summary_analytics_data_related_to_network_devices(api):
    endpoint_result = api.devices.gets_the_summary_analytics_data_related_to_network_devices(
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
def test_gets_the_summary_analytics_data_related_to_network_devices(api, validator):
    try:
        assert is_valid_gets_the_summary_analytics_data_related_to_network_devices(
            validator,
            gets_the_summary_analytics_data_related_to_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_summary_analytics_data_related_to_network_devices_default_val(api):
    endpoint_result = api.devices.gets_the_summary_analytics_data_related_to_network_devices(
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
def test_gets_the_summary_analytics_data_related_to_network_devices_default_val(api, validator):
    try:
        assert is_valid_gets_the_summary_analytics_data_related_to_network_devices(
            validator,
            gets_the_summary_analytics_data_related_to_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_trend_analytics_data(json_schema_validate, obj):
    json_schema_validate('jsd_ac7ce690e0f55a469b0a9bfa3d2c165e_v2_3_7_6').validate(obj)
    return True


def gets_the_trend_analytics_data(api):
    endpoint_result = api.devices.gets_the_trend_analytics_data(
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
def test_gets_the_trend_analytics_data(api, validator):
    try:
        assert is_valid_gets_the_trend_analytics_data(
            validator,
            gets_the_trend_analytics_data(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_trend_analytics_data_default_val(api):
    endpoint_result = api.devices.gets_the_trend_analytics_data(
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
def test_gets_the_trend_analytics_data_default_val(api, validator):
    try:
        assert is_valid_gets_the_trend_analytics_data(
            validator,
            gets_the_trend_analytics_data_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_device_data_for_the_given_device_id_uuid(json_schema_validate, obj):
    json_schema_validate('jsd_f89c7ee84a615469b754add8feeabb5a_v2_3_7_6').validate(obj)
    return True


def get_the_device_data_for_the_given_device_id_uuid(api):
    endpoint_result = api.devices.get_the_device_data_for_the_given_device_id_uuid(
        attribute='string',
        end_time=0,
        id='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_device_data_for_the_given_device_id_uuid(api, validator):
    try:
        assert is_valid_get_the_device_data_for_the_given_device_id_uuid(
            validator,
            get_the_device_data_for_the_given_device_id_uuid(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_device_data_for_the_given_device_id_uuid_default_val(api):
    endpoint_result = api.devices.get_the_device_data_for_the_given_device_id_uuid(
        attribute=None,
        end_time=None,
        id='string',
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_device_data_for_the_given_device_id_uuid_default_val(api, validator):
    try:
        assert is_valid_get_the_device_data_for_the_given_device_id_uuid(
            validator,
            get_the_device_data_for_the_given_device_id_uuid_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_the_trend_analytics_data_for_the_network_device_in_the_specified_time_range(json_schema_validate, obj):
    json_schema_validate('jsd_14ca2f659b595c0ba7c649fd8c8bdad6_v2_3_7_6').validate(obj)
    return True


def the_trend_analytics_data_for_the_network_device_in_the_specified_time_range(api):
    endpoint_result = api.devices.the_trend_analytics_data_for_the_network_device_in_the_specified_time_range(
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
def test_the_trend_analytics_data_for_the_network_device_in_the_specified_time_range(api, validator):
    try:
        assert is_valid_the_trend_analytics_data_for_the_network_device_in_the_specified_time_range(
            validator,
            the_trend_analytics_data_for_the_network_device_in_the_specified_time_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_default_val(api):
    endpoint_result = api.devices.the_trend_analytics_data_for_the_network_device_in_the_specified_time_range(
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
def test_the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_default_val(api, validator):
    try:
        assert is_valid_the_trend_analytics_data_for_the_network_device_in_the_specified_time_range(
            validator,
            the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_planned_access_points_for_building(json_schema_validate, obj):
    json_schema_validate('jsd_30efc372d6eb577ca47e8c86f30c3d2f_v2_3_7_6').validate(obj)
    return True


def get_planned_access_points_for_building(api):
    endpoint_result = api.devices.get_planned_access_points_for_building(
        building_id='string',
        limit=0,
        offset=0,
        radios=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_planned_access_points_for_building(api, validator):
    try:
        assert is_valid_get_planned_access_points_for_building(
            validator,
            get_planned_access_points_for_building(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_planned_access_points_for_building_default_val(api):
    endpoint_result = api.devices.get_planned_access_points_for_building(
        building_id='string',
        limit=None,
        offset=None,
        radios=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_planned_access_points_for_building_default_val(api, validator):
    try:
        assert is_valid_get_planned_access_points_for_building(
            validator,
            get_planned_access_points_for_building_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_detail(json_schema_validate, obj):
    json_schema_validate('jsd_560c9ee787eb5a0391309f45ddf392ca_v2_3_7_6').validate(obj)
    return True


def get_device_detail(api):
    endpoint_result = api.devices.get_device_detail(
        identifier='string',
        search_by='string',
        timestamp=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_detail(api, validator):
    try:
        assert is_valid_get_device_detail(
            validator,
            get_device_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_detail_default_val(api):
    endpoint_result = api.devices.get_device_detail(
        identifier=None,
        search_by=None,
        timestamp=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_detail_default_val(api, validator):
    try:
        assert is_valid_get_device_detail(
            validator,
            get_device_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_enrichment_details(json_schema_validate, obj):
    json_schema_validate('jsd_08a20c25e0fa518bb186fd7747450ef6_v2_3_7_6').validate(obj)
    return True


def get_device_enrichment_details(api):
    endpoint_result = api.devices.get_device_enrichment_details(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_enrichment_details(api, validator):
    try:
        assert is_valid_get_device_enrichment_details(
            validator,
            get_device_enrichment_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_enrichment_details_default_val(api):
    endpoint_result = api.devices.get_device_enrichment_details(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_enrichment_details_default_val(api, validator):
    try:
        assert is_valid_get_device_enrichment_details(
            validator,
            get_device_enrichment_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_devices(json_schema_validate, obj):
    json_schema_validate('jsd_c75e364632e15384a18063458e2ba0e3_v2_3_7_6').validate(obj)
    return True


def devices(api):
    endpoint_result = api.devices.devices(
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
def test_devices(api, validator):
    try:
        assert is_valid_devices(
            validator,
            devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def devices_default_val(api):
    endpoint_result = api.devices.devices(
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
def test_devices_default_val(api, validator):
    try:
        assert is_valid_devices(
            validator,
            devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_planned_access_point_for_floor(json_schema_validate, obj):
    json_schema_validate('jsd_f6f9dde38ce458fcaf27ffd4f84bfe68_v2_3_7_6').validate(obj)
    return True


def update_planned_access_point_for_floor(api):
    endpoint_result = api.devices.update_planned_access_point_for_floor(
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
def test_update_planned_access_point_for_floor(api, validator):
    try:
        assert is_valid_update_planned_access_point_for_floor(
            validator,
            update_planned_access_point_for_floor(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_planned_access_point_for_floor_default_val(api):
    endpoint_result = api.devices.update_planned_access_point_for_floor(
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
def test_update_planned_access_point_for_floor_default_val(api, validator):
    try:
        assert is_valid_update_planned_access_point_for_floor(
            validator,
            update_planned_access_point_for_floor_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_planned_access_point_for_floor(json_schema_validate, obj):
    json_schema_validate('jsd_ca2fe989a227585086452d24d32867a6_v2_3_7_6').validate(obj)
    return True


def create_planned_access_point_for_floor(api):
    endpoint_result = api.devices.create_planned_access_point_for_floor(
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
def test_create_planned_access_point_for_floor(api, validator):
    try:
        assert is_valid_create_planned_access_point_for_floor(
            validator,
            create_planned_access_point_for_floor(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_planned_access_point_for_floor_default_val(api):
    endpoint_result = api.devices.create_planned_access_point_for_floor(
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
def test_create_planned_access_point_for_floor_default_val(api, validator):
    try:
        assert is_valid_create_planned_access_point_for_floor(
            validator,
            create_planned_access_point_for_floor_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_planned_access_points_for_floor(json_schema_validate, obj):
    json_schema_validate('jsd_9a570c5ee77b59d8b9cd203e566288e1_v2_3_7_6').validate(obj)
    return True


def get_planned_access_points_for_floor(api):
    endpoint_result = api.devices.get_planned_access_points_for_floor(
        floor_id='string',
        limit=0,
        offset=0,
        radios=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_planned_access_points_for_floor(api, validator):
    try:
        assert is_valid_get_planned_access_points_for_floor(
            validator,
            get_planned_access_points_for_floor(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_planned_access_points_for_floor_default_val(api):
    endpoint_result = api.devices.get_planned_access_points_for_floor(
        floor_id='string',
        limit=None,
        offset=None,
        radios=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_planned_access_points_for_floor_default_val(api, validator):
    try:
        assert is_valid_get_planned_access_points_for_floor(
            validator,
            get_planned_access_points_for_floor_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_planned_access_point_for_floor(json_schema_validate, obj):
    json_schema_validate('jsd_cb644669ab8d5955826d23197015e208_v2_3_7_6').validate(obj)
    return True


def delete_planned_access_point_for_floor(api):
    endpoint_result = api.devices.delete_planned_access_point_for_floor(
        floor_id='string',
        planned_access_point_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_planned_access_point_for_floor(api, validator):
    try:
        assert is_valid_delete_planned_access_point_for_floor(
            validator,
            delete_planned_access_point_for_floor(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_planned_access_point_for_floor_default_val(api):
    endpoint_result = api.devices.delete_planned_access_point_for_floor(
        floor_id='string',
        planned_access_point_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_planned_access_point_for_floor_default_val(api, validator):
    try:
        assert is_valid_delete_planned_access_point_for_floor(
            validator,
            delete_planned_access_point_for_floor_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_health_score_definitions_for_given_filters(json_schema_validate, obj):
    json_schema_validate('jsd_84dea15738b550f3b147965f64050c97_v2_3_7_6').validate(obj)
    return True


def get_all_health_score_definitions_for_given_filters(api):
    endpoint_result = api.devices.get_all_health_score_definitions_for_given_filters(
        attribute='string',
        device_type='string',
        id='string',
        include_for_overall_health=True,
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_health_score_definitions_for_given_filters(api, validator):
    try:
        assert is_valid_get_all_health_score_definitions_for_given_filters(
            validator,
            get_all_health_score_definitions_for_given_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_health_score_definitions_for_given_filters_default_val(api):
    endpoint_result = api.devices.get_all_health_score_definitions_for_given_filters(
        attribute=None,
        device_type=None,
        id=None,
        include_for_overall_health=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_health_score_definitions_for_given_filters_default_val(api, validator):
    try:
        assert is_valid_get_all_health_score_definitions_for_given_filters(
            validator,
            get_all_health_score_definitions_for_given_filters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_health_score_definitions(json_schema_validate, obj):
    json_schema_validate('jsd_b08f499f995f5f46ba52e0385b54721a_v2_3_7_6').validate(obj)
    return True


def update_health_score_definitions(api):
    endpoint_result = api.devices.update_health_score_definitions(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_health_score_definitions(api, validator):
    try:
        assert is_valid_update_health_score_definitions(
            validator,
            update_health_score_definitions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_health_score_definitions_default_val(api):
    endpoint_result = api.devices.update_health_score_definitions(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_health_score_definitions_default_val(api, validator):
    try:
        assert is_valid_update_health_score_definitions(
            validator,
            update_health_score_definitions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_health_score_definition_for_the_given_id(json_schema_validate, obj):
    json_schema_validate('jsd_15d2a0bbce2c5b6ba0b4aee3248ace42_v2_3_7_6').validate(obj)
    return True


def get_health_score_definition_for_the_given_id(api):
    endpoint_result = api.devices.get_health_score_definition_for_the_given_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_health_score_definition_for_the_given_id(api, validator):
    try:
        assert is_valid_get_health_score_definition_for_the_given_id(
            validator,
            get_health_score_definition_for_the_given_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_health_score_definition_for_the_given_id_default_val(api):
    endpoint_result = api.devices.get_health_score_definition_for_the_given_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_health_score_definition_for_the_given_id_default_val(api, validator):
    try:
        assert is_valid_get_health_score_definition_for_the_given_id(
            validator,
            get_health_score_definition_for_the_given_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_health_score_definition_for_the_given_id(json_schema_validate, obj):
    json_schema_validate('jsd_b4f52e69ddca5b2583b28fb4c96447aa_v2_3_7_6').validate(obj)
    return True


def update_health_score_definition_for_the_given_id(api):
    endpoint_result = api.devices.update_health_score_definition_for_the_given_id(
        active_validation=True,
        id='string',
        includeForOverallHealth=True,
        payload=None,
        synchronizeToIssueThreshold=True,
        thresholdValue=0
    )
    return endpoint_result


@pytest.mark.devices
def test_update_health_score_definition_for_the_given_id(api, validator):
    try:
        assert is_valid_update_health_score_definition_for_the_given_id(
            validator,
            update_health_score_definition_for_the_given_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_health_score_definition_for_the_given_id_default_val(api):
    endpoint_result = api.devices.update_health_score_definition_for_the_given_id(
        active_validation=True,
        id='string',
        includeForOverallHealth=None,
        payload=None,
        synchronizeToIssueThreshold=None,
        thresholdValue=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_health_score_definition_for_the_given_id_default_val(api, validator):
    try:
        assert is_valid_update_health_score_definition_for_the_given_id(
            validator,
            update_health_score_definition_for_the_given_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_interfaces(json_schema_validate, obj):
    json_schema_validate('jsd_22d3d71136d95562afc211b40004d109_v2_3_7_6').validate(obj)
    return True


def get_all_interfaces(api):
    endpoint_result = api.devices.get_all_interfaces(
        last_input_time='string',
        last_output_time='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_interfaces(api, validator):
    try:
        assert is_valid_get_all_interfaces(
            validator,
            get_all_interfaces(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_interfaces_default_val(api):
    endpoint_result = api.devices.get_all_interfaces(
        last_input_time=None,
        last_output_time=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_interfaces_default_val(api, validator):
    try:
        assert is_valid_get_all_interfaces(
            validator,
            get_all_interfaces_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_count(json_schema_validate, obj):
    json_schema_validate('jsd_0da44fbc3e415a99aac0bdd291e9a87a_v2_3_7_6').validate(obj)
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


def is_valid_get_interface_by_ip(json_schema_validate, obj):
    json_schema_validate('jsd_cf7fa95e3ed4527aa5ba8ca871a8c142_v2_3_7_6').validate(obj)
    return True


def get_interface_by_ip(api):
    endpoint_result = api.devices.get_interface_by_ip(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_ip(api, validator):
    try:
        assert is_valid_get_interface_by_ip(
            validator,
            get_interface_by_ip(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interface_by_ip_default_val(api):
    endpoint_result = api.devices.get_interface_by_ip(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_ip_default_val(api, validator):
    try:
        assert is_valid_get_interface_by_ip(
            validator,
            get_interface_by_ip_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_isis_interfaces(json_schema_validate, obj):
    json_schema_validate('jsd_af71ea437c8755869b00d26ba9234dff_v2_3_7_6').validate(obj)
    return True


def get_isis_interfaces(api):
    endpoint_result = api.devices.get_isis_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_isis_interfaces(api, validator):
    try:
        assert is_valid_get_isis_interfaces(
            validator,
            get_isis_interfaces(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_isis_interfaces_default_val(api):
    endpoint_result = api.devices.get_isis_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_isis_interfaces_default_val(api, validator):
    try:
        assert is_valid_get_isis_interfaces(
            validator,
            get_isis_interfaces_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_info_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_e057192b97615f0d99a10e2b66bab13a_v2_3_7_6').validate(obj)
    return True


def get_interface_info_by_id(api):
    endpoint_result = api.devices.get_interface_info_by_id(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_info_by_id(api, validator):
    try:
        assert is_valid_get_interface_info_by_id(
            validator,
            get_interface_info_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interface_info_by_id_default_val(api):
    endpoint_result = api.devices.get_interface_info_by_id(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_info_by_id_default_val(api, validator):
    try:
        assert is_valid_get_interface_info_by_id(
            validator,
            get_interface_info_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_count_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_34b7d6c62ea6522081fcf55de7eb9fd7_v2_3_7_6').validate(obj)
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
    json_schema_validate('jsd_bef9e9b306085d879b877598fad71b51_v2_3_7_6').validate(obj)
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


def is_valid_get_device_interfaces_by_specified_range(json_schema_validate, obj):
    json_schema_validate('jsd_5a3d52c630ba5deaada16fe3b07af744_v2_3_7_6').validate(obj)
    return True


def get_device_interfaces_by_specified_range(api):
    endpoint_result = api.devices.get_device_interfaces_by_specified_range(
        device_id='string',
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interfaces_by_specified_range(api, validator):
    try:
        assert is_valid_get_device_interfaces_by_specified_range(
            validator,
            get_device_interfaces_by_specified_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_interfaces_by_specified_range_default_val(api):
    endpoint_result = api.devices.get_device_interfaces_by_specified_range(
        device_id='string',
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interfaces_by_specified_range_default_val(api, validator):
    try:
        assert is_valid_get_device_interfaces_by_specified_range(
            validator,
            get_device_interfaces_by_specified_range_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ospf_interfaces(json_schema_validate, obj):
    json_schema_validate('jsd_32a2868ff45f5621965f6ece01a742ce_v2_3_7_6').validate(obj)
    return True


def get_ospf_interfaces(api):
    endpoint_result = api.devices.get_ospf_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_ospf_interfaces(api, validator):
    try:
        assert is_valid_get_ospf_interfaces(
            validator,
            get_ospf_interfaces(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ospf_interfaces_default_val(api):
    endpoint_result = api.devices.get_ospf_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_ospf_interfaces_default_val(api, validator):
    try:
        assert is_valid_get_ospf_interfaces(
            validator,
            get_ospf_interfaces_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_17b16bff74ae54ca88a02b34df169218_v2_3_7_6').validate(obj)
    return True


def get_interface_by_id(api):
    endpoint_result = api.devices.get_interface_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_id(api, validator):
    try:
        assert is_valid_get_interface_by_id(
            validator,
            get_interface_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interface_by_id_default_val(api):
    endpoint_result = api.devices.get_interface_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_id_default_val(api, validator):
    try:
        assert is_valid_get_interface_by_id(
            validator,
            get_interface_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_interface_details(json_schema_validate, obj):
    json_schema_validate('jsd_2441213b887c55faaca726bbe4ac2564_v2_3_7_6').validate(obj)
    return True


def update_interface_details(api):
    endpoint_result = api.devices.update_interface_details(
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
def test_update_interface_details(api, validator):
    try:
        assert is_valid_update_interface_details(
            validator,
            update_interface_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_interface_details_default_val(api):
    endpoint_result = api.devices.update_interface_details(
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
def test_update_interface_details_default_val(api, validator):
    try:
        assert is_valid_update_interface_details(
            validator,
            update_interface_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_legit_operations_for_interface(json_schema_validate, obj):
    json_schema_validate('jsd_fe6d62edcec25921926043ca25f75bed_v2_3_7_6').validate(obj)
    return True


def legit_operations_for_interface(api):
    endpoint_result = api.devices.legit_operations_for_interface(
        interface_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_legit_operations_for_interface(api, validator):
    try:
        assert is_valid_legit_operations_for_interface(
            validator,
            legit_operations_for_interface(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def legit_operations_for_interface_default_val(api):
    endpoint_result = api.devices.legit_operations_for_interface(
        interface_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_legit_operations_for_interface_default_val(api, validator):
    try:
        assert is_valid_legit_operations_for_interface(
            validator,
            legit_operations_for_interface_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_clear_mac_address_table(json_schema_validate, obj):
    json_schema_validate('jsd_399e702d5786552992aa76b930780569_v2_3_7_6').validate(obj)
    return True


def clear_mac_address_table(api):
    endpoint_result = api.devices.clear_mac_address_table(
        active_validation=True,
        deployment_mode='string',
        interface_uuid='string',
        operation='string',
        payload=None,
        payload={}
    )
    return endpoint_result


@pytest.mark.devices
def test_clear_mac_address_table(api, validator):
    try:
        assert is_valid_clear_mac_address_table(
            validator,
            clear_mac_address_table(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def clear_mac_address_table_default_val(api):
    endpoint_result = api.devices.clear_mac_address_table(
        active_validation=True,
        deployment_mode=None,
        interface_uuid='string',
        operation=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_clear_mac_address_table_default_val(api, validator):
    try:
        assert is_valid_clear_mac_address_table(
            validator,
            clear_mac_address_table_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_list(json_schema_validate, obj):
    json_schema_validate('jsd_fe602e8165035b5cbc304fada4ee2f26_v2_3_7_6').validate(obj)
    return True


def get_device_list(api):
    endpoint_result = api.devices.get_device_list(
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
def test_get_device_list(api, validator):
    try:
        assert is_valid_get_device_list(
            validator,
            get_device_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_list_default_val(api):
    endpoint_result = api.devices.get_device_list(
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
def test_get_device_list_default_val(api, validator):
    try:
        assert is_valid_get_device_list(
            validator,
            get_device_list_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_device(json_schema_validate, obj):
    json_schema_validate('jsd_62704fe3ec7651e79d891fce37a0d860_v2_3_7_6').validate(obj)
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
    json_schema_validate('jsd_8232fe06867e548bba1919024b40d992_v2_3_7_6').validate(obj)
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


def is_valid_get_device_values_that_match_fully_or_partially_an_attribute(json_schema_validate, obj):
    json_schema_validate('jsd_b5a5c8da4aaa526da6a06e97c80a38be_v2_3_7_6').validate(obj)
    return True


def get_device_values_that_match_fully_or_partially_an_attribute(api):
    endpoint_result = api.devices.get_device_values_that_match_fully_or_partially_an_attribute(
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
def test_get_device_values_that_match_fully_or_partially_an_attribute(api, validator):
    try:
        assert is_valid_get_device_values_that_match_fully_or_partially_an_attribute(
            validator,
            get_device_values_that_match_fully_or_partially_an_attribute(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_values_that_match_fully_or_partially_an_attribute_default_val(api):
    endpoint_result = api.devices.get_device_values_that_match_fully_or_partially_an_attribute(
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
def test_get_device_values_that_match_fully_or_partially_an_attribute_default_val(api, validator):
    try:
        assert is_valid_get_device_values_that_match_fully_or_partially_an_attribute(
            validator,
            get_device_values_that_match_fully_or_partially_an_attribute_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_role(json_schema_validate, obj):
    json_schema_validate('jsd_aa11f09d28165f4ea6c81b8642e59cc4_v2_3_7_6').validate(obj)
    return True


def update_device_role(api):
    endpoint_result = api.devices.update_device_role(
        active_validation=True,
        id='string',
        payload=None,
        role='string',
        roleSource='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_role(api, validator):
    try:
        assert is_valid_update_device_role(
            validator,
            update_device_role(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_role_default_val(api):
    endpoint_result = api.devices.update_device_role(
        active_validation=True,
        id=None,
        payload=None,
        role=None,
        roleSource=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_role_default_val(api, validator):
    try:
        assert is_valid_update_device_role(
            validator,
            update_device_role_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_polling_interval_for_all_devices(json_schema_validate, obj):
    json_schema_validate('jsd_ce94ab18ad505e8a9846f6c4c9df0d2b_v2_3_7_6').validate(obj)
    return True


def get_polling_interval_for_all_devices(api):
    endpoint_result = api.devices.get_polling_interval_for_all_devices(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_for_all_devices(api, validator):
    try:
        assert is_valid_get_polling_interval_for_all_devices(
            validator,
            get_polling_interval_for_all_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_polling_interval_for_all_devices_default_val(api):
    endpoint_result = api.devices.get_polling_interval_for_all_devices(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_for_all_devices_default_val(api, validator):
    try:
        assert is_valid_get_polling_interval_for_all_devices(
            validator,
            get_polling_interval_for_all_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_config_for_all_devices(json_schema_validate, obj):
    json_schema_validate('jsd_ed2bca4be412527198720a4dfec9604a_v2_3_7_6').validate(obj)
    return True


def get_device_config_for_all_devices(api):
    endpoint_result = api.devices.get_device_config_for_all_devices(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_for_all_devices(api, validator):
    try:
        assert is_valid_get_device_config_for_all_devices(
            validator,
            get_device_config_for_all_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_config_for_all_devices_default_val(api):
    endpoint_result = api.devices.get_device_config_for_all_devices(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_for_all_devices_default_val(api, validator):
    try:
        assert is_valid_get_device_config_for_all_devices(
            validator,
            get_device_config_for_all_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_config_count(json_schema_validate, obj):
    json_schema_validate('jsd_3dc0a72537a3578ca31cc5ef29131d35_v2_3_7_6').validate(obj)
    return True


def get_device_config_count(api):
    endpoint_result = api.devices.get_device_config_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_count(api, validator):
    try:
        assert is_valid_get_device_config_count(
            validator,
            get_device_config_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_config_count_default_val(api):
    endpoint_result = api.devices.get_device_config_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_count_default_val(api, validator):
    try:
        assert is_valid_get_device_config_count(
            validator,
            get_device_config_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_count(json_schema_validate, obj):
    json_schema_validate('jsd_bbfe7340fe6752e5bc273a303d165654_v2_3_7_6').validate(obj)
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


def is_valid_export_device_list(json_schema_validate, obj):
    json_schema_validate('jsd_57e6ec627d3c587288978990aae75228_v2_3_7_6').validate(obj)
    return True


def export_device_list(api):
    endpoint_result = api.devices.export_device_list(
        active_validation=True,
        deviceUuids=['string'],
        operationEnum='string',
        parameters=['string'],
        password='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_export_device_list(api, validator):
    try:
        assert is_valid_export_device_list(
            validator,
            export_device_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def export_device_list_default_val(api):
    endpoint_result = api.devices.export_device_list(
        active_validation=True,
        deviceUuids=None,
        operationEnum=None,
        parameters=None,
        password=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_export_device_list_default_val(api, validator):
    try:
        assert is_valid_export_device_list(
            validator,
            export_device_list_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_functional_capability_for_devices(json_schema_validate, obj):
    json_schema_validate('jsd_ad8cea95d71352f0842a2c869765e6cf_v2_3_7_6').validate(obj)
    return True


def get_functional_capability_for_devices(api):
    endpoint_result = api.devices.get_functional_capability_for_devices(
        device_id='string',
        function_name='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_for_devices(api, validator):
    try:
        assert is_valid_get_functional_capability_for_devices(
            validator,
            get_functional_capability_for_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_functional_capability_for_devices_default_val(api):
    endpoint_result = api.devices.get_functional_capability_for_devices(
        device_id=None,
        function_name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_for_devices_default_val(api, validator):
    try:
        assert is_valid_get_functional_capability_for_devices(
            validator,
            get_functional_capability_for_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_functional_capability_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_7f494532c45654fdaeda8d46a0d9753d_v2_3_7_6').validate(obj)
    return True


def get_functional_capability_by_id(api):
    endpoint_result = api.devices.get_functional_capability_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_by_id(api, validator):
    try:
        assert is_valid_get_functional_capability_by_id(
            validator,
            get_functional_capability_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_functional_capability_by_id_default_val(api):
    endpoint_result = api.devices.get_functional_capability_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_by_id_default_val(api, validator):
    try:
        assert is_valid_get_functional_capability_by_id(
            validator,
            get_functional_capability_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_inventory_insight_device_link_mismatch(json_schema_validate, obj):
    json_schema_validate('jsd_eed1595442b757bf94938c858a257ced_v2_3_7_6').validate(obj)
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


def is_valid_get_network_device_by_ip(json_schema_validate, obj):
    json_schema_validate('jsd_40123dc74c2052a3a4eb7e2a01eaa8e7_v2_3_7_6').validate(obj)
    return True


def get_network_device_by_ip(api):
    endpoint_result = api.devices.get_network_device_by_ip(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_ip(api, validator):
    try:
        assert is_valid_get_network_device_by_ip(
            validator,
            get_network_device_by_ip(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_device_by_ip_default_val(api):
    endpoint_result = api.devices.get_network_device_by_ip(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_ip_default_val(api, validator):
    try:
        assert is_valid_get_network_device_by_ip(
            validator,
            get_network_device_by_ip_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_modules(json_schema_validate, obj):
    json_schema_validate('jsd_ce9e547725c45c66824afda98179d12f_v2_3_7_6').validate(obj)
    return True


def get_modules(api):
    endpoint_result = api.devices.get_modules(
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
def test_get_modules(api, validator):
    try:
        assert is_valid_get_modules(
            validator,
            get_modules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_modules_default_val(api):
    endpoint_result = api.devices.get_modules(
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
def test_get_modules_default_val(api, validator):
    try:
        assert is_valid_get_modules(
            validator,
            get_modules_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_module_count(json_schema_validate, obj):
    json_schema_validate('jsd_fb11f997009751c991884b5fc02087c5_v2_3_7_6').validate(obj)
    return True


def get_module_count(api):
    endpoint_result = api.devices.get_module_count(
        device_id='string',
        name_list='value1,value2',
        operational_state_code_list='value1,value2',
        part_number_list='value1,value2',
        vendor_equipment_type_list='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_count(api, validator):
    try:
        assert is_valid_get_module_count(
            validator,
            get_module_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_module_count_default_val(api):
    endpoint_result = api.devices.get_module_count(
        device_id=None,
        name_list=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_count_default_val(api, validator):
    try:
        assert is_valid_get_module_count(
            validator,
            get_module_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_module_info_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_96a4588640da5b018b499c5760f4092a_v2_3_7_6').validate(obj)
    return True


def get_module_info_by_id(api):
    endpoint_result = api.devices.get_module_info_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_info_by_id(api, validator):
    try:
        assert is_valid_get_module_info_by_id(
            validator,
            get_module_info_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_module_info_by_id_default_val(api):
    endpoint_result = api.devices.get_module_info_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_info_by_id_default_val(api, validator):
    try:
        assert is_valid_get_module_info_by_id(
            validator,
            get_module_info_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_by_serial_number(json_schema_validate, obj):
    json_schema_validate('jsd_5c53d56c282e5f108c659009d21f9d26_v2_3_7_6').validate(obj)
    return True


def get_device_by_serial_number(api):
    endpoint_result = api.devices.get_device_by_serial_number(
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_serial_number(api, validator):
    try:
        assert is_valid_get_device_by_serial_number(
            validator,
            get_device_by_serial_number(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_by_serial_number_default_val(api):
    endpoint_result = api.devices.get_device_by_serial_number(
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_serial_number_default_val(api, validator):
    try:
        assert is_valid_get_device_by_serial_number(
            validator,
            get_device_by_serial_number_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sync_devices_using_forcesync(json_schema_validate, obj):
    json_schema_validate('jsd_9425f2c120b855cb8c852806ce72e54d_v2_3_7_6').validate(obj)
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


def is_valid_get_devices_registered_for_wsa_notification(json_schema_validate, obj):
    json_schema_validate('jsd_8770b2c39feb5e48913492c33add7f13_v2_3_7_6').validate(obj)
    return True


def get_devices_registered_for_wsa_notification(api):
    endpoint_result = api.devices.get_devices_registered_for_wsa_notification(
        macaddress='string',
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_devices_registered_for_wsa_notification(api, validator):
    try:
        assert is_valid_get_devices_registered_for_wsa_notification(
            validator,
            get_devices_registered_for_wsa_notification(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_devices_registered_for_wsa_notification_default_val(api):
    endpoint_result = api.devices.get_devices_registered_for_wsa_notification(
        macaddress=None,
        serial_number=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_devices_registered_for_wsa_notification_default_val(api, validator):
    try:
        assert is_valid_get_devices_registered_for_wsa_notification(
            validator,
            get_devices_registered_for_wsa_notification_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_user_defined_fields(json_schema_validate, obj):
    json_schema_validate('jsd_d31b0bb4bde55bb8a3078b66c81f3a22_v2_3_7_6').validate(obj)
    return True


def get_all_user_defined_fields(api):
    endpoint_result = api.devices.get_all_user_defined_fields(
        id='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_user_defined_fields(api, validator):
    try:
        assert is_valid_get_all_user_defined_fields(
            validator,
            get_all_user_defined_fields(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_user_defined_fields_default_val(api):
    endpoint_result = api.devices.get_all_user_defined_fields(
        id=None,
        name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_user_defined_fields_default_val(api, validator):
    try:
        assert is_valid_get_all_user_defined_fields(
            validator,
            get_all_user_defined_fields_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_user_defined_field(json_schema_validate, obj):
    json_schema_validate('jsd_ed266e6eda225aedbf581508635da822_v2_3_7_6').validate(obj)
    return True


def create_user_defined_field(api):
    endpoint_result = api.devices.create_user_defined_field(
        active_validation=True,
        description='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_create_user_defined_field(api, validator):
    try:
        assert is_valid_create_user_defined_field(
            validator,
            create_user_defined_field(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_user_defined_field_default_val(api):
    endpoint_result = api.devices.create_user_defined_field(
        active_validation=True,
        description=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_create_user_defined_field_default_val(api, validator):
    try:
        assert is_valid_create_user_defined_field(
            validator,
            create_user_defined_field_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_user_defined_field(json_schema_validate, obj):
    json_schema_validate('jsd_119d76a951f85a7a927afc2f1ea935c8_v2_3_7_6').validate(obj)
    return True


def update_user_defined_field(api):
    endpoint_result = api.devices.update_user_defined_field(
        active_validation=True,
        description='string',
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_user_defined_field(api, validator):
    try:
        assert is_valid_update_user_defined_field(
            validator,
            update_user_defined_field(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_user_defined_field_default_val(api):
    endpoint_result = api.devices.update_user_defined_field(
        active_validation=True,
        description=None,
        id='string',
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_user_defined_field_default_val(api, validator):
    try:
        assert is_valid_update_user_defined_field(
            validator,
            update_user_defined_field_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_user_defined_field(json_schema_validate, obj):
    json_schema_validate('jsd_6854f0f19119501094fb5fafe05dfbca_v2_3_7_6').validate(obj)
    return True


def delete_user_defined_field(api):
    endpoint_result = api.devices.delete_user_defined_field(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_user_defined_field(api, validator):
    try:
        assert is_valid_delete_user_defined_field(
            validator,
            delete_user_defined_field(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_user_defined_field_default_val(api):
    endpoint_result = api.devices.delete_user_defined_field(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_user_defined_field_default_val(api, validator):
    try:
        assert is_valid_delete_user_defined_field(
            validator,
            delete_user_defined_field_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_chassis_details_for_device(json_schema_validate, obj):
    json_schema_validate('jsd_4a03cee8dfd7514487a134a422f5e0d7_v2_3_7_6').validate(obj)
    return True


def get_chassis_details_for_device(api):
    endpoint_result = api.devices.get_chassis_details_for_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_chassis_details_for_device(api, validator):
    try:
        assert is_valid_get_chassis_details_for_device(
            validator,
            get_chassis_details_for_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_chassis_details_for_device_default_val(api):
    endpoint_result = api.devices.get_chassis_details_for_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_chassis_details_for_device_default_val(api, validator):
    try:
        assert is_valid_get_chassis_details_for_device(
            validator,
            get_chassis_details_for_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_stack_details_for_device(json_schema_validate, obj):
    json_schema_validate('jsd_c07eaefa1fa45faa801764d9094336ae_v2_3_7_6').validate(obj)
    return True


def get_stack_details_for_device(api):
    endpoint_result = api.devices.get_stack_details_for_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_stack_details_for_device(api, validator):
    try:
        assert is_valid_get_stack_details_for_device(
            validator,
            get_stack_details_for_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_stack_details_for_device_default_val(api):
    endpoint_result = api.devices.get_stack_details_for_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_stack_details_for_device_default_val(api, validator):
    try:
        assert is_valid_get_stack_details_for_device(
            validator,
            get_stack_details_for_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_user_defined_field_from_device(json_schema_validate, obj):
    json_schema_validate('jsd_c1144f7a496455f99f95d36d6474c4b4_v2_3_7_6').validate(obj)
    return True


def remove_user_defined_field_from_device(api):
    endpoint_result = api.devices.remove_user_defined_field_from_device(
        device_id='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_remove_user_defined_field_from_device(api, validator):
    try:
        assert is_valid_remove_user_defined_field_from_device(
            validator,
            remove_user_defined_field_from_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def remove_user_defined_field_from_device_default_val(api):
    endpoint_result = api.devices.remove_user_defined_field_from_device(
        device_id='string',
        name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_remove_user_defined_field_from_device_default_val(api, validator):
    try:
        assert is_valid_remove_user_defined_field_from_device(
            validator,
            remove_user_defined_field_from_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_user_defined_field_to_device(json_schema_validate, obj):
    json_schema_validate('jsd_a73fbc67627e5bbbafe748de84d42df6_v2_3_7_6').validate(obj)
    return True


def add_user_defined_field_to_device(api):
    endpoint_result = api.devices.add_user_defined_field_to_device(
        active_validation=True,
        device_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_add_user_defined_field_to_device(api, validator):
    try:
        assert is_valid_add_user_defined_field_to_device(
            validator,
            add_user_defined_field_to_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_user_defined_field_to_device_default_val(api):
    endpoint_result = api.devices.add_user_defined_field_to_device(
        active_validation=True,
        device_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_add_user_defined_field_to_device_default_val(api, validator):
    try:
        assert is_valid_add_user_defined_field_to_device(
            validator,
            add_user_defined_field_to_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_details_of_physical_components_of_the_given_device(json_schema_validate, obj):
    json_schema_validate('jsd_520c1cb24a2b53ce8d29d119c6ee1112_v2_3_7_6').validate(obj)
    return True


def get_the_details_of_physical_components_of_the_given_device(api):
    endpoint_result = api.devices.get_the_details_of_physical_components_of_the_given_device(
        device_uuid='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_details_of_physical_components_of_the_given_device(api, validator):
    try:
        assert is_valid_get_the_details_of_physical_components_of_the_given_device(
            validator,
            get_the_details_of_physical_components_of_the_given_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_details_of_physical_components_of_the_given_device_default_val(api):
    endpoint_result = api.devices.get_the_details_of_physical_components_of_the_given_device(
        device_uuid='string',
        type=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_details_of_physical_components_of_the_given_device_default_val(api, validator):
    try:
        assert is_valid_get_the_details_of_physical_components_of_the_given_device(
            validator,
            get_the_details_of_physical_components_of_the_given_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_poe_interface_details(json_schema_validate, obj):
    json_schema_validate('jsd_ab3215d9be065533b7cbbc978cb4d905_v2_3_7_6').validate(obj)
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


def is_valid_get_connected_device_detail(json_schema_validate, obj):
    json_schema_validate('jsd_a1878314ffd35d29bea49f12d10b59c8_v2_3_7_6').validate(obj)
    return True


def get_connected_device_detail(api):
    endpoint_result = api.devices.get_connected_device_detail(
        device_uuid='string',
        interface_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_connected_device_detail(api, validator):
    try:
        assert is_valid_get_connected_device_detail(
            validator,
            get_connected_device_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_connected_device_detail_default_val(api):
    endpoint_result = api.devices.get_connected_device_detail(
        device_uuid='string',
        interface_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_connected_device_detail_default_val(api, validator):
    try:
        assert is_valid_get_connected_device_detail(
            validator,
            get_connected_device_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_linecard_details(json_schema_validate, obj):
    json_schema_validate('jsd_bd31690b61f45d9f880d74d4e682b070_v2_3_7_6').validate(obj)
    return True


def get_linecard_details(api):
    endpoint_result = api.devices.get_linecard_details(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_linecard_details(api, validator):
    try:
        assert is_valid_get_linecard_details(
            validator,
            get_linecard_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_linecard_details_default_val(api):
    endpoint_result = api.devices.get_linecard_details(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_linecard_details_default_val(api, validator):
    try:
        assert is_valid_get_linecard_details(
            validator,
            get_linecard_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_poe_details(json_schema_validate, obj):
    json_schema_validate('jsd_f7a67aba0b365a1e9dae62d148511a25_v2_3_7_6').validate(obj)
    return True


def poe_details(api):
    endpoint_result = api.devices.poe_details(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_poe_details(api, validator):
    try:
        assert is_valid_poe_details(
            validator,
            poe_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def poe_details_default_val(api):
    endpoint_result = api.devices.poe_details(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_poe_details_default_val(api, validator):
    try:
        assert is_valid_poe_details(
            validator,
            poe_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_supervisor_card_detail(json_schema_validate, obj):
    json_schema_validate('jsd_4500eb13516155a28570e542dcf10a91_v2_3_7_6').validate(obj)
    return True


def get_supervisor_card_detail(api):
    endpoint_result = api.devices.get_supervisor_card_detail(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_supervisor_card_detail(api, validator):
    try:
        assert is_valid_get_supervisor_card_detail(
            validator,
            get_supervisor_card_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_supervisor_card_detail_default_val(api):
    endpoint_result = api.devices.get_supervisor_card_detail(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_supervisor_card_detail_default_val(api, validator):
    try:
        assert is_valid_get_supervisor_card_detail(
            validator,
            get_supervisor_card_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_management_address(json_schema_validate, obj):
    json_schema_validate('jsd_39cb98464ddb5ee9ba7ebb4428443ba9_v2_3_7_6').validate(obj)
    return True


def update_device_management_address(api):
    endpoint_result = api.devices.update_device_management_address(
        active_validation=True,
        deviceid='string',
        newIP='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_management_address(api, validator):
    try:
        assert is_valid_update_device_management_address(
            validator,
            update_device_management_address(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_management_address_default_val(api):
    endpoint_result = api.devices.update_device_management_address(
        active_validation=True,
        deviceid='string',
        newIP=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_management_address_default_val(api, validator):
    try:
        assert is_valid_update_device_management_address(
            validator,
            update_device_management_address_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_358d86f657f8592f97014d2ebf8d37ac_v2_3_7_6').validate(obj)
    return True


def get_device_by_id(api):
    endpoint_result = api.devices.get_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_id(api, validator):
    try:
        assert is_valid_get_device_by_id(
            validator,
            get_device_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_by_id_default_val(api):
    endpoint_result = api.devices.get_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_id_default_val(api, validator):
    try:
        assert is_valid_get_device_by_id(
            validator,
            get_device_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_003e01233fa258e393239c4b41882806_v2_3_7_6').validate(obj)
    return True


def delete_device_by_id(api):
    endpoint_result = api.devices.delete_device_by_id(
        clean_config=True,
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_device_by_id(api, validator):
    try:
        assert is_valid_delete_device_by_id(
            validator,
            delete_device_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_by_id_default_val(api):
    endpoint_result = api.devices.delete_device_by_id(
        clean_config=None,
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_device_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_device_by_id(
            validator,
            delete_device_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_summary(json_schema_validate, obj):
    json_schema_validate('jsd_fe0153ca24205608b8741d51f5a6d54a_v2_3_7_6').validate(obj)
    return True


def get_device_summary(api):
    endpoint_result = api.devices.get_device_summary(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_summary(api, validator):
    try:
        assert is_valid_get_device_summary(
            validator,
            get_device_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_summary_default_val(api):
    endpoint_result = api.devices.get_device_summary(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_summary_default_val(api, validator):
    try:
        assert is_valid_get_device_summary(
            validator,
            get_device_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_polling_interval_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_f90daf1c279351f884ba3198d3b2d641_v2_3_7_6').validate(obj)
    return True


def get_polling_interval_by_id(api):
    endpoint_result = api.devices.get_polling_interval_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_by_id(api, validator):
    try:
        assert is_valid_get_polling_interval_by_id(
            validator,
            get_polling_interval_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_polling_interval_by_id_default_val(api):
    endpoint_result = api.devices.get_polling_interval_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_by_id_default_val(api, validator):
    try:
        assert is_valid_get_polling_interval_by_id(
            validator,
            get_polling_interval_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_organization_list_for_meraki(json_schema_validate, obj):
    json_schema_validate('jsd_790b4ba6d23d5e7eb62cbba4c9e1a29d_v2_3_7_6').validate(obj)
    return True


def get_organization_list_for_meraki(api):
    endpoint_result = api.devices.get_organization_list_for_meraki(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_organization_list_for_meraki(api, validator):
    try:
        assert is_valid_get_organization_list_for_meraki(
            validator,
            get_organization_list_for_meraki(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_organization_list_for_meraki_default_val(api):
    endpoint_result = api.devices.get_organization_list_for_meraki(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_organization_list_for_meraki_default_val(api, validator):
    try:
        assert is_valid_get_organization_list_for_meraki(
            validator,
            get_organization_list_for_meraki_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_vlans(json_schema_validate, obj):
    json_schema_validate('jsd_fd5fb603cba6523abb25c8ec131fbb8b_v2_3_7_6').validate(obj)
    return True


def get_device_interface_vlans(api):
    endpoint_result = api.devices.get_device_interface_vlans(
        id='string',
        interface_type='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_vlans(api, validator):
    try:
        assert is_valid_get_device_interface_vlans(
            validator,
            get_device_interface_vlans(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_interface_vlans_default_val(api):
    endpoint_result = api.devices.get_device_interface_vlans(
        id='string',
        interface_type=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_vlans_default_val(api, validator):
    try:
        assert is_valid_get_device_interface_vlans(
            validator,
            get_device_interface_vlans_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_wireless_lan_controller_details_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_c01ee650fcf858789ca00c8deda969b9_v2_3_7_6').validate(obj)
    return True


def get_wireless_lan_controller_details_by_id(api):
    endpoint_result = api.devices.get_wireless_lan_controller_details_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_wireless_lan_controller_details_by_id(api, validator):
    try:
        assert is_valid_get_wireless_lan_controller_details_by_id(
            validator,
            get_wireless_lan_controller_details_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_wireless_lan_controller_details_by_id_default_val(api):
    endpoint_result = api.devices.get_wireless_lan_controller_details_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_wireless_lan_controller_details_by_id_default_val(api, validator):
    try:
        assert is_valid_get_wireless_lan_controller_details_by_id(
            validator,
            get_wireless_lan_controller_details_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_config_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_5af0bbf34adb5146b931ec874fc2cc40_v2_3_7_6').validate(obj)
    return True


def get_device_config_by_id(api):
    endpoint_result = api.devices.get_device_config_by_id(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_by_id(api, validator):
    try:
        assert is_valid_get_device_config_by_id(
            validator,
            get_device_config_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_config_by_id_default_val(api):
    endpoint_result = api.devices.get_device_config_by_id(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_by_id_default_val(api, validator):
    try:
        assert is_valid_get_device_config_by_id(
            validator,
            get_device_config_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device_by_pagination_range(json_schema_validate, obj):
    json_schema_validate('jsd_60d7b6ce5abd5dad837e22ace817a6f0_v2_3_7_6').validate(obj)
    return True


def get_network_device_by_pagination_range(api):
    endpoint_result = api.devices.get_network_device_by_pagination_range(
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_pagination_range(api, validator):
    try:
        assert is_valid_get_network_device_by_pagination_range(
            validator,
            get_network_device_by_pagination_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_device_by_pagination_range_default_val(api):
    endpoint_result = api.devices.get_network_device_by_pagination_range(
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_pagination_range_default_val(api, validator):
    try:
        assert is_valid_get_network_device_by_pagination_range(
            validator,
            get_network_device_by_pagination_range_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_global_resync_interval(json_schema_validate, obj):
    json_schema_validate('jsd_37537a64bd4956649de3a61e10f0637e_v2_3_7_6').validate(obj)
    return True


def update_global_resync_interval(api):
    endpoint_result = api.devices.update_global_resync_interval(
        active_validation=True,
        interval=0,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_global_resync_interval(api, validator):
    try:
        assert is_valid_update_global_resync_interval(
            validator,
            update_global_resync_interval(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_global_resync_interval_default_val(api):
    endpoint_result = api.devices.update_global_resync_interval(
        active_validation=True,
        interval=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_global_resync_interval_default_val(api, validator):
    try:
        assert is_valid_update_global_resync_interval(
            validator,
            update_global_resync_interval_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_override_resync_interval(json_schema_validate, obj):
    json_schema_validate('jsd_dc239a9ab9e5562b93a45ea0b9708b84_v2_3_7_6').validate(obj)
    return True


def override_resync_interval(api):
    endpoint_result = api.devices.override_resync_interval(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_override_resync_interval(api, validator):
    try:
        assert is_valid_override_resync_interval(
            validator,
            override_resync_interval(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def override_resync_interval_default_val(api):
    endpoint_result = api.devices.override_resync_interval(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_override_resync_interval_default_val(api, validator):
    try:
        assert is_valid_override_resync_interval(
            validator,
            override_resync_interval_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_resync_interval_for_the_network_device(json_schema_validate, obj):
    json_schema_validate('jsd_fdfc828270d950ecb75480fe03f7d573_v2_3_7_6').validate(obj)
    return True


def update_resync_interval_for_the_network_device(api):
    endpoint_result = api.devices.update_resync_interval_for_the_network_device(
        active_validation=True,
        id='string',
        interval=0,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_resync_interval_for_the_network_device(api, validator):
    try:
        assert is_valid_update_resync_interval_for_the_network_device(
            validator,
            update_resync_interval_for_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_resync_interval_for_the_network_device_default_val(api):
    endpoint_result = api.devices.update_resync_interval_for_the_network_device(
        active_validation=True,
        id='string',
        interval=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_resync_interval_for_the_network_device_default_val(api, validator):
    try:
        assert is_valid_update_resync_interval_for_the_network_device(
            validator,
            update_resync_interval_for_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_resync_interval_for_the_network_device(json_schema_validate, obj):
    json_schema_validate('jsd_e56a4c0d91dd53ecb737da824115a050_v2_3_7_6').validate(obj)
    return True


def get_resync_interval_for_the_network_device(api):
    endpoint_result = api.devices.get_resync_interval_for_the_network_device(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_resync_interval_for_the_network_device(api, validator):
    try:
        assert is_valid_get_resync_interval_for_the_network_device(
            validator,
            get_resync_interval_for_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_resync_interval_for_the_network_device_default_val(api):
    endpoint_result = api.devices.get_resync_interval_for_the_network_device(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_resync_interval_for_the_network_device_default_val(api, validator):
    try:
        assert is_valid_get_resync_interval_for_the_network_device(
            validator,
            get_resync_interval_for_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_stats_info(json_schema_validate, obj):
    json_schema_validate('jsd_a9e0722d184658c592bd130ff03e1dde_v2_3_7_6').validate(obj)
    return True


def get_device_interface_stats_info(api):
    endpoint_result = api.devices.get_device_interface_stats_info(
        active_validation=True,
        device_id='string',
        endTime=0,
        payload=None,
        query={'fields': [{}], 'filters': [{'key': 'string', 'operator': 'string', 'value': 'string'}], 'page': {'limit': 0, 'offset': 0, 'orderBy': [{'name': 'string', 'order': 'string'}]}},
        startTime=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_stats_info(api, validator):
    try:
        assert is_valid_get_device_interface_stats_info(
            validator,
            get_device_interface_stats_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_interface_stats_info_default_val(api):
    endpoint_result = api.devices.get_device_interface_stats_info(
        active_validation=True,
        device_id='string',
        endTime=None,
        payload=None,
        query=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_stats_info_default_val(api, validator):
    try:
        assert is_valid_get_device_interface_stats_info(
            validator,
            get_device_interface_stats_info_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_count_of_health_score_definitions_based_on_provided_filters(json_schema_validate, obj):
    json_schema_validate('jsd_6a51fd8467055ff1a69ade1ae8096993_v2_3_7_6').validate(obj)
    return True


def get_the_count_of_health_score_definitions_based_on_provided_filters(api):
    endpoint_result = api.devices.get_the_count_of_health_score_definitions_based_on_provided_filters(
        device_type='string',
        id='string',
        include_for_overall_health=True
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_count_of_health_score_definitions_based_on_provided_filters(api, validator):
    try:
        assert is_valid_get_the_count_of_health_score_definitions_based_on_provided_filters(
            validator,
            get_the_count_of_health_score_definitions_based_on_provided_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_count_of_health_score_definitions_based_on_provided_filters_default_val(api):
    endpoint_result = api.devices.get_the_count_of_health_score_definitions_based_on_provided_filters(
        device_type=None,
        id=None,
        include_for_overall_health=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_the_count_of_health_score_definitions_based_on_provided_filters_default_val(api, validator):
    try:
        assert is_valid_get_the_count_of_health_score_definitions_based_on_provided_filters(
            validator,
            get_the_count_of_health_score_definitions_based_on_provided_filters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

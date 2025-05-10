# -*- coding: utf-8 -*-
"""CatalystCenterAPI sites API fixtures and tests.

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


def is_valid_get_sites_energy_v1(json_schema_validate, obj):
    json_schema_validate('jsd_91270011e9d85a8da71b95b17b58263c_v3_1_3_0').validate(obj)
    return True


def get_sites_energy_v1(api):
    endpoint_result = api.sites.get_sites_energy_v1(
        attribute='string',
        device_category='string',
        end_time=0,
        limit=0,
        offset=0,
        order='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        site_name='string',
        site_type='string',
        sort_by='string',
        start_time=0,
        task_id='string',
        views='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_sites_energy_v1(api, validator):
    try:
        assert is_valid_get_sites_energy_v1(
            validator,
            get_sites_energy_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sites_energy_v1_default_val(api):
    endpoint_result = api.sites.get_sites_energy_v1(
        attribute=None,
        device_category=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_name=None,
        site_type=None,
        sort_by=None,
        start_time=None,
        task_id=None,
        views=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_sites_energy_v1_default_val(api, validator):
    try:
        assert is_valid_get_sites_energy_v1(
            validator,
            get_sites_energy_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_sites_energy_v1(json_schema_validate, obj):
    json_schema_validate('jsd_85c449f48a0b517185b32bfd53f33a5b_v3_1_3_0').validate(obj)
    return True


def count_sites_energy_v1(api):
    endpoint_result = api.sites.count_sites_energy_v1(
        device_category='string',
        end_time=0,
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        site_name='string',
        site_type='string',
        start_time=0,
        task_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_count_sites_energy_v1(api, validator):
    try:
        assert is_valid_count_sites_energy_v1(
            validator,
            count_sites_energy_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_sites_energy_v1_default_val(api):
    endpoint_result = api.sites.count_sites_energy_v1(
        device_category=None,
        end_time=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_name=None,
        site_type=None,
        start_time=None,
        task_id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_count_sites_energy_v1_default_val(api, validator):
    try:
        assert is_valid_count_sites_energy_v1(
            validator,
            count_sites_energy_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_submit_request_to_query_sites_energy_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ae8282c90a7059ceb31b4072429d00cd_v3_1_3_0').validate(obj)
    return True


def submit_request_to_query_sites_energy_v1(api):
    endpoint_result = api.sites.submit_request_to_query_sites_energy_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'logicalOperator': 'string', 'filters': [{'key': 'string', 'operator': 'string', 'value': ['string']}]}],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string', 'function': 'string'}]},
        payload=None,
        startTime=0,
        task_id='string',
        views=['string']
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_to_query_sites_energy_v1(api, validator):
    try:
        assert is_valid_submit_request_to_query_sites_energy_v1(
            validator,
            submit_request_to_query_sites_energy_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def submit_request_to_query_sites_energy_v1_default_val(api):
    endpoint_result = api.sites.submit_request_to_query_sites_energy_v1(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None,
        task_id=None,
        views=None
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_to_query_sites_energy_v1_default_val(api, validator):
    try:
        assert is_valid_submit_request_to_query_sites_energy_v1(
            validator,
            submit_request_to_query_sites_energy_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_sites_energy_for_the_given_task_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_715e06041b1f59638e377ae39ed162bd_v3_1_3_0').validate(obj)
    return True


def query_sites_energy_for_the_given_task_id_v1(api):
    endpoint_result = api.sites.query_sites_energy_for_the_given_task_id_v1(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_query_sites_energy_for_the_given_task_id_v1(api, validator):
    try:
        assert is_valid_query_sites_energy_for_the_given_task_id_v1(
            validator,
            query_sites_energy_for_the_given_task_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def query_sites_energy_for_the_given_task_id_v1_default_val(api):
    endpoint_result = api.sites.query_sites_energy_for_the_given_task_id_v1(
        task_id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_query_sites_energy_for_the_given_task_id_v1_default_val(api, validator):
    try:
        assert is_valid_query_sites_energy_for_the_given_task_id_v1(
            validator,
            query_sites_energy_for_the_given_task_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_sites_energy_for_the_given_task_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8cc0a299df36558d8646580f0a0d283c_v3_1_3_0').validate(obj)
    return True


def count_sites_energy_for_the_given_task_id_v1(api):
    endpoint_result = api.sites.count_sites_energy_for_the_given_task_id_v1(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_count_sites_energy_for_the_given_task_id_v1(api, validator):
    try:
        assert is_valid_count_sites_energy_for_the_given_task_id_v1(
            validator,
            count_sites_energy_for_the_given_task_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_sites_energy_for_the_given_task_id_v1_default_val(api):
    endpoint_result = api.sites.count_sites_energy_for_the_given_task_id_v1(
        task_id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_count_sites_energy_for_the_given_task_id_v1_default_val(api, validator):
    try:
        assert is_valid_count_sites_energy_for_the_given_task_id_v1(
            validator,
            count_sites_energy_for_the_given_task_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_submit_request_to_count_sites_energy_from_query_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d0e1021de57d5e95bbea5d5bd86b481a_v3_1_3_0').validate(obj)
    return True


def submit_request_to_count_sites_energy_from_query_v1(api):
    endpoint_result = api.sites.submit_request_to_count_sites_energy_from_query_v1(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'logicalOperator': 'string', 'filters': [{'key': 'string', 'operator': 'string', 'value': ['string']}]}],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string', 'function': 'string'}]},
        payload=None,
        startTime=0,
        task_id='string',
        views=['string']
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_to_count_sites_energy_from_query_v1(api, validator):
    try:
        assert is_valid_submit_request_to_count_sites_energy_from_query_v1(
            validator,
            submit_request_to_count_sites_energy_from_query_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def submit_request_to_count_sites_energy_from_query_v1_default_val(api):
    endpoint_result = api.sites.submit_request_to_count_sites_energy_from_query_v1(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None,
        task_id=None,
        views=None
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_to_count_sites_energy_from_query_v1_default_val(api, validator):
    try:
        assert is_valid_submit_request_to_count_sites_energy_from_query_v1(
            validator,
            submit_request_to_count_sites_energy_from_query_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_energy_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b688ff94649e552ca2d9535136b2c0a6_v3_1_3_0').validate(obj)
    return True


def get_site_energy_by_id_v1(api):
    endpoint_result = api.sites.get_site_energy_by_id_v1(
        attribute='string',
        device_category='string',
        end_time=0,
        id='string',
        start_time=0,
        task_id='string',
        views='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_energy_by_id_v1(api, validator):
    try:
        assert is_valid_get_site_energy_by_id_v1(
            validator,
            get_site_energy_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_energy_by_id_v1_default_val(api):
    endpoint_result = api.sites.get_site_energy_by_id_v1(
        attribute=None,
        device_category=None,
        end_time=None,
        id='string',
        start_time=None,
        task_id=None,
        views=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_energy_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_energy_by_id_v1(
            validator,
            get_site_energy_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_list_of_site_health_summaries_v1(json_schema_validate, obj):
    json_schema_validate('jsd_870b40b4f6d558bfbebcf8fcbc4df56b_v3_1_3_0').validate(obj)
    return True


def read_list_of_site_health_summaries_v1(api):
    endpoint_result = api.sites.read_list_of_site_health_summaries_v1(
        attribute='string',
        end_time=0,
        id='string',
        limit=0,
        offset=0,
        order='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_type='string',
        sort_by='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_read_list_of_site_health_summaries_v1(api, validator):
    try:
        assert is_valid_read_list_of_site_health_summaries_v1(
            validator,
            read_list_of_site_health_summaries_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_list_of_site_health_summaries_v1_default_val(api):
    endpoint_result = api.sites.read_list_of_site_health_summaries_v1(
        attribute=None,
        end_time=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_type=None,
        sort_by=None,
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.sites
def test_read_list_of_site_health_summaries_v1_default_val(api, validator):
    try:
        assert is_valid_read_list_of_site_health_summaries_v1(
            validator,
            read_list_of_site_health_summaries_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_site_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e67558dd99925a0385f5f870bbb8f634_v3_1_3_0').validate(obj)
    return True


def read_site_count_v1(api):
    endpoint_result = api.sites.read_site_count_v1(
        end_time=0,
        id='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_type='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_read_site_count_v1(api, validator):
    try:
        assert is_valid_read_site_count_v1(
            validator,
            read_site_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_site_count_v1_default_val(api):
    endpoint_result = api.sites.read_site_count_v1(
        end_time=None,
        id=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_read_site_count_v1_default_val(api, validator):
    try:
        assert is_valid_read_site_count_v1(
            validator,
            read_site_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_an_aggregated_summary_of_site_health_data_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fc80b3e12ee9577a8e7fa5d4cd84e8fc_v3_1_3_0').validate(obj)
    return True


def read_an_aggregated_summary_of_site_health_data_v1(api):
    endpoint_result = api.sites.read_an_aggregated_summary_of_site_health_data_v1(
        attribute='string',
        end_time=0,
        id='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_type='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_read_an_aggregated_summary_of_site_health_data_v1(api, validator):
    try:
        assert is_valid_read_an_aggregated_summary_of_site_health_data_v1(
            validator,
            read_an_aggregated_summary_of_site_health_data_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_an_aggregated_summary_of_site_health_data_v1_default_val(api):
    endpoint_result = api.sites.read_an_aggregated_summary_of_site_health_data_v1(
        attribute=None,
        end_time=None,
        id=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_type=None,
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.sites
def test_read_an_aggregated_summary_of_site_health_data_v1_default_val(api, validator):
    try:
        assert is_valid_read_an_aggregated_summary_of_site_health_data_v1(
            validator,
            read_an_aggregated_summary_of_site_health_data_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_an_aggregated_summary_of_site_health_data_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8bec2dde673c5b2f940d0474fed32af6_v3_1_3_0').validate(obj)
    return True


def query_an_aggregated_summary_of_site_health_data_v1(api):
    endpoint_result = api.sites.query_an_aggregated_summary_of_site_health_data_v1(
        active_validation=True,
        attributes=['string'],
        endTime=0,
        id='string',
        payload=None,
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_type='string',
        startTime=0,
        views=['string']
    )
    return endpoint_result


@pytest.mark.sites
def test_query_an_aggregated_summary_of_site_health_data_v1(api, validator):
    try:
        assert is_valid_query_an_aggregated_summary_of_site_health_data_v1(
            validator,
            query_an_aggregated_summary_of_site_health_data_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def query_an_aggregated_summary_of_site_health_data_v1_default_val(api):
    endpoint_result = api.sites.query_an_aggregated_summary_of_site_health_data_v1(
        active_validation=True,
        attributes=None,
        endTime=None,
        id=None,
        payload=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_type=None,
        startTime=None,
        views=None
    )
    return endpoint_result


@pytest.mark.sites
def test_query_an_aggregated_summary_of_site_health_data_v1_default_val(api, validator):
    try:
        assert is_valid_query_an_aggregated_summary_of_site_health_data_v1(
            validator,
            query_an_aggregated_summary_of_site_health_data_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0181a47540d95b8ba6d78bfe5db7dbe2_v3_1_3_0').validate(obj)
    return True


def read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_v1(api):
    endpoint_result = api.sites.read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_v1(
        attribute='string',
        end_time=0,
        id='string',
        limit=0,
        offset=0,
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_type='string',
        start_time=0,
        task_id='string',
        time_sort_order='string',
        trend_interval='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_v1(api, validator):
    try:
        assert is_valid_read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_v1(
            validator,
            read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_v1_default_val(api):
    endpoint_result = api.sites.read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_v1(
        attribute=None,
        end_time=None,
        id=None,
        limit=None,
        offset=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_type=None,
        start_time=None,
        task_id=None,
        time_sort_order=None,
        trend_interval=None
    )
    return endpoint_result


@pytest.mark.sites
def test_read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_v1_default_val(api, validator):
    try:
        assert is_valid_read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_v1(
            validator,
            read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_site_health_summary_data_by_site_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_062572f214555abaa6a30cdbcc32e713_v3_1_3_0').validate(obj)
    return True


def read_site_health_summary_data_by_site_id_v1(api):
    endpoint_result = api.sites.read_site_health_summary_data_by_site_id_v1(
        attribute='string',
        end_time=0,
        id='string',
        start_time=0,
        view='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_read_site_health_summary_data_by_site_id_v1(api, validator):
    try:
        assert is_valid_read_site_health_summary_data_by_site_id_v1(
            validator,
            read_site_health_summary_data_by_site_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_site_health_summary_data_by_site_id_v1_default_val(api):
    endpoint_result = api.sites.read_site_health_summary_data_by_site_id_v1(
        attribute=None,
        end_time=None,
        id='string',
        start_time=None,
        view=None
    )
    return endpoint_result


@pytest.mark.sites
def test_read_site_health_summary_data_by_site_id_v1_default_val(api, validator):
    try:
        assert is_valid_read_site_health_summary_data_by_site_id_v1(
            validator,
            read_site_health_summary_data_by_site_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_trend_analytics_data_for_a_specific_site_in_your_network_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a75ee097a016562cbf861c4c52df3e30_v3_1_3_0').validate(obj)
    return True


def read_trend_analytics_data_for_a_specific_site_in_your_network_v1(api):
    endpoint_result = api.sites.read_trend_analytics_data_for_a_specific_site_in_your_network_v1(
        attribute='string',
        end_time=0,
        id='string',
        limit=0,
        offset=0,
        start_time=0,
        task_id='string',
        time_sort_order='string',
        trend_interval='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_read_trend_analytics_data_for_a_specific_site_in_your_network_v1(api, validator):
    try:
        assert is_valid_read_trend_analytics_data_for_a_specific_site_in_your_network_v1(
            validator,
            read_trend_analytics_data_for_a_specific_site_in_your_network_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_trend_analytics_data_for_a_specific_site_in_your_network_v1_default_val(api):
    endpoint_result = api.sites.read_trend_analytics_data_for_a_specific_site_in_your_network_v1(
        attribute=None,
        end_time=None,
        id='string',
        limit=None,
        offset=None,
        start_time=None,
        task_id=None,
        time_sort_order=None,
        trend_interval=None
    )
    return endpoint_result


@pytest.mark.sites
def test_read_trend_analytics_data_for_a_specific_site_in_your_network_v1_default_val(api, validator):
    try:
        assert is_valid_read_trend_analytics_data_for_a_specific_site_in_your_network_v1(
            validator,
            read_trend_analytics_data_for_a_specific_site_in_your_network_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4181fd376c6a5d9382d5bee853c43031_v3_1_3_0').validate(obj)
    return True


def get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_v1(api):
    endpoint_result = api.sites.get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_v1(
        attribute='string',
        band='string',
        end_time=0,
        failure_category='string',
        failure_reason='string',
        limit=0,
        offset=0,
        order='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        site_type='string',
        sort_by='string',
        ssid='string',
        start_time=0,
        task_id='string',
        view='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_v1(api, validator):
    try:
        assert is_valid_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_v1(
            validator,
            get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_v1_default_val(api):
    endpoint_result = api.sites.get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_v1(
        attribute=None,
        band=None,
        end_time=None,
        failure_category=None,
        failure_reason=None,
        limit=None,
        offset=None,
        order=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_type=None,
        sort_by=None,
        ssid=None,
        start_time=None,
        task_id=None,
        view=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_v1(
            validator,
            get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_af22da7f49fd5d658d0ce2992ea7fef9_v3_1_3_0').validate(obj)
    return True


def get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_v1(api):
    endpoint_result = api.sites.get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_v1(
        end_time=0,
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        site_type='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.sites
def test_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_v1(api, validator):
    try:
        assert is_valid_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_v1(
            validator,
            get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_v1_default_val(api):
    endpoint_result = api.sites.get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_v1(
        end_time=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_type=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_v1_default_val(api, validator):
    try:
        assert is_valid_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_v1(
            validator,
            get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2647a4829a44597bbf9813664eb75de0_v3_1_3_0').validate(obj)
    return True


def get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_v1(api):
    endpoint_result = api.sites.get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_v1(
        active_validation=True,
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        page={'limit': 0, 'offset': 0, 'sortBy': {'name': 'string', 'order': 'string'}},
        payload=None,
        startTime=0,
        views=['string']
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_v1(api, validator):
    try:
        assert is_valid_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_v1(
            validator,
            get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_v1_default_val(api):
    endpoint_result = api.sites.get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_v1(
        active_validation=True,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None,
        views=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_v1(
            validator,
            get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4db690b800995e35bc4e8c43d8ea6c18_v3_1_3_0').validate(obj)
    return True


def get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_v1(api):
    endpoint_result = api.sites.get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_v1(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.sites
def test_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_v1(api, validator):
    try:
        assert is_valid_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_v1(
            validator,
            get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_v1_default_val(api):
    endpoint_result = api.sites.get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_v1(
        active_validation=True,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_v1_default_val(api, validator):
    try:
        assert is_valid_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_v1(
            validator,
            get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_analytics_summary_data_for_the_given_task_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_131c846dfbe75601831b5de7e8771829_v3_1_3_0').validate(obj)
    return True


def get_site_analytics_summary_data_for_the_given_task_id_v1(api):
    endpoint_result = api.sites.get_site_analytics_summary_data_for_the_given_task_id_v1(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_summary_data_for_the_given_task_id_v1(api, validator):
    try:
        assert is_valid_get_site_analytics_summary_data_for_the_given_task_id_v1(
            validator,
            get_site_analytics_summary_data_for_the_given_task_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_analytics_summary_data_for_the_given_task_id_v1_default_val(api):
    endpoint_result = api.sites.get_site_analytics_summary_data_for_the_given_task_id_v1(
        task_id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_summary_data_for_the_given_task_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_analytics_summary_data_for_the_given_task_id_v1(
            validator,
            get_site_analytics_summary_data_for_the_given_task_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_submit_request_for_site_analytics_summary_data_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5345b8a44ba454de8a7bb52d3efe97ca_v3_1_3_0').validate(obj)
    return True


def submit_request_for_site_analytics_summary_data_v1(api):
    endpoint_result = api.sites.submit_request_for_site_analytics_summary_data_v1(
        active_validation=True,
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_for_site_analytics_summary_data_v1(api, validator):
    try:
        assert is_valid_submit_request_for_site_analytics_summary_data_v1(
            validator,
            submit_request_for_site_analytics_summary_data_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def submit_request_for_site_analytics_summary_data_v1_default_val(api):
    endpoint_result = api.sites.submit_request_for_site_analytics_summary_data_v1(
        active_validation=True,
        attributes=None,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_for_site_analytics_summary_data_v1_default_val(api, validator):
    try:
        assert is_valid_submit_request_for_site_analytics_summary_data_v1(
            validator,
            submit_request_for_site_analytics_summary_data_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_top_n_entities_related_to_site_analytics_for_the_given_task_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_20e256f5fc9757c483f41ffef3677fef_v3_1_3_0').validate(obj)
    return True


def get_top_n_entities_related_to_site_analytics_for_the_given_task_id_v1(api):
    endpoint_result = api.sites.get_top_n_entities_related_to_site_analytics_for_the_given_task_id_v1(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_top_n_entities_related_to_site_analytics_for_the_given_task_id_v1(api, validator):
    try:
        assert is_valid_get_top_n_entities_related_to_site_analytics_for_the_given_task_id_v1(
            validator,
            get_top_n_entities_related_to_site_analytics_for_the_given_task_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_top_n_entities_related_to_site_analytics_for_the_given_task_id_v1_default_val(api):
    endpoint_result = api.sites.get_top_n_entities_related_to_site_analytics_for_the_given_task_id_v1(
        task_id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_top_n_entities_related_to_site_analytics_for_the_given_task_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_top_n_entities_related_to_site_analytics_for_the_given_task_id_v1(
            validator,
            get_top_n_entities_related_to_site_analytics_for_the_given_task_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_submit_request_for_top_n_entities_related_to_site_analytics_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d9e3276d1ed3511b80b22ea8388959c8_v3_1_3_0').validate(obj)
    return True


def submit_request_for_top_n_entities_related_to_site_analytics_v1(api):
    endpoint_result = api.sites.submit_request_for_top_n_entities_related_to_site_analytics_v1(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        groupBy=['string'],
        payload=None,
        startTime=0,
        topN=0
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_for_top_n_entities_related_to_site_analytics_v1(api, validator):
    try:
        assert is_valid_submit_request_for_top_n_entities_related_to_site_analytics_v1(
            validator,
            submit_request_for_top_n_entities_related_to_site_analytics_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def submit_request_for_top_n_entities_related_to_site_analytics_v1_default_val(api):
    endpoint_result = api.sites.submit_request_for_top_n_entities_related_to_site_analytics_v1(
        active_validation=True,
        endTime=None,
        filters=None,
        groupBy=None,
        payload=None,
        startTime=None,
        topN=None
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_for_top_n_entities_related_to_site_analytics_v1_default_val(api, validator):
    try:
        assert is_valid_submit_request_for_top_n_entities_related_to_site_analytics_v1(
            validator,
            submit_request_for_top_n_entities_related_to_site_analytics_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_analytics_trend_data_for_the_given_task_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3f396d5c149b510a8cd8e560f8baae4b_v3_1_3_0').validate(obj)
    return True


def get_site_analytics_trend_data_for_the_given_task_id_v1(api):
    endpoint_result = api.sites.get_site_analytics_trend_data_for_the_given_task_id_v1(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_trend_data_for_the_given_task_id_v1(api, validator):
    try:
        assert is_valid_get_site_analytics_trend_data_for_the_given_task_id_v1(
            validator,
            get_site_analytics_trend_data_for_the_given_task_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_analytics_trend_data_for_the_given_task_id_v1_default_val(api):
    endpoint_result = api.sites.get_site_analytics_trend_data_for_the_given_task_id_v1(
        task_id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_trend_data_for_the_given_task_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_analytics_trend_data_for_the_given_task_id_v1(
            validator,
            get_site_analytics_trend_data_for_the_given_task_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_submit_request_for_site_analytics_trend_data_v1(json_schema_validate, obj):
    json_schema_validate('jsd_65edc44e0e7a513191cc16dc2b4da88e_v3_1_3_0').validate(obj)
    return True


def submit_request_for_site_analytics_trend_data_v1(api):
    endpoint_result = api.sites.submit_request_for_site_analytics_trend_data_v1(
        active_validation=True,
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        page={'limit': 0, 'offset': 0, 'timestampOrder': 'string'},
        payload=None,
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_for_site_analytics_trend_data_v1(api, validator):
    try:
        assert is_valid_submit_request_for_site_analytics_trend_data_v1(
            validator,
            submit_request_for_site_analytics_trend_data_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def submit_request_for_site_analytics_trend_data_v1_default_val(api):
    endpoint_result = api.sites.submit_request_for_site_analytics_trend_data_v1(
        active_validation=True,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None,
        trendInterval=None
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_for_site_analytics_trend_data_v1_default_val(api, validator):
    try:
        assert is_valid_submit_request_for_site_analytics_trend_data_v1(
            validator,
            submit_request_for_site_analytics_trend_data_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_analytics_for_one_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_69aec803dd6056a0b2a3ebd66dc136d3_v3_1_3_0').validate(obj)
    return True


def get_site_analytics_for_one_site_v1(api):
    endpoint_result = api.sites.get_site_analytics_for_one_site_v1(
        attribute='string',
        band='string',
        end_time=0,
        failure_category='string',
        failure_reason='string',
        id='string',
        ssid='string',
        start_time=0,
        task_id='string',
        view='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_for_one_site_v1(api, validator):
    try:
        assert is_valid_get_site_analytics_for_one_site_v1(
            validator,
            get_site_analytics_for_one_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_analytics_for_one_site_v1_default_val(api):
    endpoint_result = api.sites.get_site_analytics_for_one_site_v1(
        attribute=None,
        band=None,
        end_time=None,
        failure_category=None,
        failure_reason=None,
        id='string',
        ssid=None,
        start_time=None,
        task_id=None,
        view=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_for_one_site_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_analytics_for_one_site_v1(
            validator,
            get_site_analytics_for_one_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_devices_to_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0a544e27e18e5412af3b68d915c8ca50_v3_1_3_0').validate(obj)
    return True


def assign_devices_to_site_v1(api):
    endpoint_result = api.sites.assign_devices_to_site_v1(
        active_validation=True,
        device=[{'ip': 'string'}],
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_assign_devices_to_site_v1(api, validator):
    try:
        assert is_valid_assign_devices_to_site_v1(
            validator,
            assign_devices_to_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_devices_to_site_v1_default_val(api):
    endpoint_result = api.sites.assign_devices_to_site_v1(
        active_validation=True,
        device=None,
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_assign_devices_to_site_v1_default_val(api, validator):
    try:
        assert is_valid_assign_devices_to_site_v1(
            validator,
            assign_devices_to_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_export_map_archive_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c937494318f952ba92eaeb82b144c338_v3_1_3_0').validate(obj)
    return True


def export_map_archive_v1(api):
    endpoint_result = api.sites.export_map_archive_v1(
        active_validation=True,
        payload=None,
        site_hierarchy_uuid='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_export_map_archive_v1(api, validator):
    try:
        assert is_valid_export_map_archive_v1(
            validator,
            export_map_archive_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def export_map_archive_v1_default_val(api):
    endpoint_result = api.sites.export_map_archive_v1(
        active_validation=True,
        payload=None,
        site_hierarchy_uuid='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_export_map_archive_v1_default_val(api, validator):
    try:
        assert is_valid_export_map_archive_v1(
            validator,
            export_map_archive_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_map_archive_start_import_v1(json_schema_validate, obj):
    json_schema_validate('jsd_07ea81890f92553aaed79952ab7ab363_v3_1_3_0').validate(obj)
    return True


def import_map_archive_start_import_v1(api):
    endpoint_result = api.sites.import_map_archive_start_import_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_start_import_v1(api, validator):
    try:
        assert is_valid_import_map_archive_start_import_v1(
            validator,
            import_map_archive_start_import_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_map_archive_start_import_v1_default_val(api):
    endpoint_result = api.sites.import_map_archive_start_import_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_start_import_v1_default_val(api, validator):
    try:
        assert is_valid_import_map_archive_start_import_v1(
            validator,
            import_map_archive_start_import_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_map_archive_cancel_an_import_v1(json_schema_validate, obj):
    json_schema_validate('jsd_44580624a59853e8a3462db736556ab4_v3_1_3_0').validate(obj)
    return True


def import_map_archive_cancel_an_import_v1(api):
    endpoint_result = api.sites.import_map_archive_cancel_an_import_v1(
        import_context_uuid='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_cancel_an_import_v1(api, validator):
    try:
        assert is_valid_import_map_archive_cancel_an_import_v1(
            validator,
            import_map_archive_cancel_an_import_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_map_archive_cancel_an_import_v1_default_val(api):
    endpoint_result = api.sites.import_map_archive_cancel_an_import_v1(
        import_context_uuid='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_cancel_an_import_v1_default_val(api, validator):
    try:
        assert is_valid_import_map_archive_cancel_an_import_v1(
            validator,
            import_map_archive_cancel_an_import_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_map_archive_perform_import_v1(json_schema_validate, obj):
    json_schema_validate('jsd_df05fb7a09595d0b9f6bc46b24275927_v3_1_3_0').validate(obj)
    return True


def import_map_archive_perform_import_v1(api):
    endpoint_result = api.sites.import_map_archive_perform_import_v1(
        active_validation=True,
        import_context_uuid='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_perform_import_v1(api, validator):
    try:
        assert is_valid_import_map_archive_perform_import_v1(
            validator,
            import_map_archive_perform_import_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_map_archive_perform_import_v1_default_val(api):
    endpoint_result = api.sites.import_map_archive_perform_import_v1(
        active_validation=True,
        import_context_uuid='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_perform_import_v1_default_val(api, validator):
    try:
        assert is_valid_import_map_archive_perform_import_v1(
            validator,
            import_map_archive_perform_import_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_map_archive_import_status_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c04c790688e4566c9f5eaa52b8fe39c8_v3_1_3_0').validate(obj)
    return True


def import_map_archive_import_status_v1(api):
    endpoint_result = api.sites.import_map_archive_import_status_v1(
        import_context_uuid='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_import_status_v1(api, validator):
    try:
        assert is_valid_import_map_archive_import_status_v1(
            validator,
            import_map_archive_import_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_map_archive_import_status_v1_default_val(api):
    endpoint_result = api.sites.import_map_archive_import_status_v1(
        import_context_uuid='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_import_status_v1_default_val(api, validator):
    try:
        assert is_valid_import_map_archive_import_status_v1(
            validator,
            import_map_archive_import_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_maps_supported_access_points_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8a5e16b065e3534c8894e52d52540f99_v3_1_3_0').validate(obj)
    return True


def maps_supported_access_points_v1(api):
    endpoint_result = api.sites.maps_supported_access_points_v1(

    )
    return endpoint_result


@pytest.mark.sites
def test_maps_supported_access_points_v1(api, validator):
    try:
        assert is_valid_maps_supported_access_points_v1(
            validator,
            maps_supported_access_points_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def maps_supported_access_points_v1_default_val(api):
    endpoint_result = api.sites.maps_supported_access_points_v1(

    )
    return endpoint_result


@pytest.mark.sites
def test_maps_supported_access_points_v1_default_val(api, validator):
    try:
        assert is_valid_maps_supported_access_points_v1(
            validator,
            maps_supported_access_points_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_membership_v1(json_schema_validate, obj):
    json_schema_validate('jsd_63284ca11e0b5f8d91395e2462a9cfdc_v3_1_3_0').validate(obj)
    return True


def get_membership_v1(api):
    endpoint_result = api.sites.get_membership_v1(
        device_family='string',
        limit=0,
        offset=0,
        serial_number='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_membership_v1(api, validator):
    try:
        assert is_valid_get_membership_v1(
            validator,
            get_membership_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_membership_v1_default_val(api):
    endpoint_result = api.sites.get_membership_v1(
        device_family=None,
        limit=None,
        offset=None,
        serial_number=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_membership_v1_default_val(api, validator):
    try:
        assert is_valid_get_membership_v1(
            validator,
            get_membership_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bce8e6b307ce52dd8f5546fbd78e05ee_v3_1_3_0').validate(obj)
    return True


def create_site_v1(api):
    endpoint_result = api.sites.create_site_v1(
        active_validation=True,
        payload=None,
        site={'area': {'name': 'string', 'parentName': 'string'}, 'building': {'name': 'string', 'address': 'string', 'parentName': 'string', 'latitude': 0, 'longitude': 0, 'country': 'string'}, 'floor': {'name': 'string', 'parentName': 'string', 'rfModel': 'string', 'width': 0, 'length': 0, 'height': 0, 'floorNumber': 0}},
        type='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_create_site_v1(api, validator):
    try:
        assert is_valid_create_site_v1(
            validator,
            create_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_site_v1_default_val(api):
    endpoint_result = api.sites.create_site_v1(
        active_validation=True,
        payload=None,
        site=None,
        type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_create_site_v1_default_val(api, validator):
    try:
        assert is_valid_create_site_v1(
            validator,
            create_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_dbdd6074bedc59b9a3edd6477897d659_v3_1_3_0').validate(obj)
    return True


def get_site_v1(api):
    endpoint_result = api.sites.get_site_v1(
        limit=0,
        name='string',
        offset=0,
        site_id='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_v1(api, validator):
    try:
        assert is_valid_get_site_v1(
            validator,
            get_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_v1_default_val(api):
    endpoint_result = api.sites.get_site_v1(
        limit=None,
        name=None,
        offset=None,
        site_id=None,
        type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_v1(
            validator,
            get_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_health_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ae4b592f66035f24b55028f79c1b7290_v3_1_3_0').validate(obj)
    return True


def get_site_health_v1(api):
    endpoint_result = api.sites.get_site_health_v1(
        limit=0,
        offset=0,
        site_type='string',
        timestamp=0
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_health_v1(api, validator):
    try:
        assert is_valid_get_site_health_v1(
            validator,
            get_site_health_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_health_v1_default_val(api):
    endpoint_result = api.sites.get_site_health_v1(
        limit=None,
        offset=None,
        site_type=None,
        timestamp=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_health_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_health_v1(
            validator,
            get_site_health_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_devices_that_are_assigned_to_a_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_cfabe762b2af55f282076fe2a14b6792_v3_1_3_0').validate(obj)
    return True


def get_devices_that_are_assigned_to_a_site_v1(api):
    endpoint_result = api.sites.get_devices_that_are_assigned_to_a_site_v1(
        id='string',
        level='string',
        limit='string',
        member_type='string',
        offset='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_devices_that_are_assigned_to_a_site_v1(api, validator):
    try:
        assert is_valid_get_devices_that_are_assigned_to_a_site_v1(
            validator,
            get_devices_that_are_assigned_to_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_devices_that_are_assigned_to_a_site_v1_default_val(api):
    endpoint_result = api.sites.get_devices_that_are_assigned_to_a_site_v1(
        id='string',
        level=None,
        limit=None,
        member_type=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_devices_that_are_assigned_to_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_get_devices_that_are_assigned_to_a_site_v1(
            validator,
            get_devices_that_are_assigned_to_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e7a025fbe2c452fc82eedd5c50104aba_v3_1_3_0').validate(obj)
    return True


def get_site_count_v1(api):
    endpoint_result = api.sites.get_site_count_v1(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_count_v1(api, validator):
    try:
        assert is_valid_get_site_count_v1(
            validator,
            get_site_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_count_v1_default_val(api):
    endpoint_result = api.sites.get_site_count_v1(
        site_id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_count_v1(
            validator,
            get_site_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_27df9908ad265e83ab77d73803925678_v3_1_3_0').validate(obj)
    return True


def update_site_v1(api):
    endpoint_result = api.sites.update_site_v1(
        active_validation=True,
        payload=None,
        site={'area': {'name': 'string', 'parentName': 'string'}, 'building': {'name': 'string', 'address': 'string', 'parentName': 'string', 'latitude': 0, 'longitude': 0, 'country': 'string'}, 'floor': {'name': 'string', 'rfModel': 'string', 'width': 0, 'length': 0, 'height': 0, 'floorNumber': 0, 'parentName': 'string'}},
        site_id='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_update_site_v1(api, validator):
    try:
        assert is_valid_update_site_v1(
            validator,
            update_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_site_v1_default_val(api):
    endpoint_result = api.sites.update_site_v1(
        active_validation=True,
        payload=None,
        site=None,
        site_id='string',
        type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_update_site_v1_default_val(api, validator):
    try:
        assert is_valid_update_site_v1(
            validator,
            update_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ba5567f03dea5b6891957dd410319e3f_v3_1_3_0').validate(obj)
    return True


def delete_site_v1(api):
    endpoint_result = api.sites.delete_site_v1(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_delete_site_v1(api, validator):
    try:
        assert is_valid_delete_site_v1(
            validator,
            delete_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_site_v1_default_val(api):
    endpoint_result = api.sites.delete_site_v1(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_delete_site_v1_default_val(api, validator):
    try:
        assert is_valid_delete_site_v1(
            validator,
            delete_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_v2(json_schema_validate, obj):
    json_schema_validate('jsd_43c5e65cce2954fdb7177ac0a8e0b76f_v3_1_3_0').validate(obj)
    return True


def get_site_v2(api):
    endpoint_result = api.sites.get_site_v2(
        group_name_hierarchy='string',
        id='string',
        limit='string',
        offset='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_v2(api, validator):
    try:
        assert is_valid_get_site_v2(
            validator,
            get_site_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_v2_default_val(api):
    endpoint_result = api.sites.get_site_v2(
        group_name_hierarchy=None,
        id=None,
        limit=None,
        offset=None,
        type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_v2_default_val(api, validator):
    try:
        assert is_valid_get_site_v2(
            validator,
            get_site_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_count_v2(json_schema_validate, obj):
    json_schema_validate('jsd_371b10ff66e5568ebe6d41faeeabda22_v3_1_3_0').validate(obj)
    return True


def get_site_count_v2(api):
    endpoint_result = api.sites.get_site_count_v2(
        id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_count_v2(api, validator):
    try:
        assert is_valid_get_site_count_v2(
            validator,
            get_site_count_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_count_v2_default_val(api):
    endpoint_result = api.sites.get_site_count_v2(
        id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_count_v2_default_val(api, validator):
    try:
        assert is_valid_get_site_count_v2(
            validator,
            get_site_count_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

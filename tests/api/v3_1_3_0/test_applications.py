# -*- coding: utf-8 -*-
"""CatalystCenterAPI applications API fixtures and tests.

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


def is_valid_retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(json_schema_validate, obj):
    json_schema_validate('jsd_fb02436a6c935d5d8a536b86de8b2846_v3_1_3_0').validate(obj)
    return True


def retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(api):
    endpoint_result = api.applications.retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
        application_name='string',
        attribute='string',
        business_relevance='string',
        end_time=0,
        limit=0,
        offset=0,
        order='string',
        site_id='string',
        sort_by='string',
        ssid='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
            validator,
            retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics_default_val(api):
    endpoint_result = api.applications.retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
        application_name=None,
        attribute=None,
        business_relevance=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        site_id=None,
        sort_by=None,
        ssid=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
            validator,
            retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(json_schema_validate, obj):
    json_schema_validate('jsd_43c50def6b3a58e5acab3ae592a57da8_v3_1_3_0').validate(obj)
    return True


def retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(api):
    endpoint_result = api.applications.retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(
        application_name='string',
        business_relevance='string',
        end_time=0,
        site_id='string',
        ssid='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(api, validator):
    try:
        assert is_valid_retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(
            validator,
            retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_count_of_network_applications_by_applying_basic_filtering_default_val(api):
    endpoint_result = api.applications.retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(
        application_name=None,
        business_relevance=None,
        end_time=None,
        site_id=None,
        ssid=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_total_count_of_network_applications_by_applying_basic_filtering_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(
            validator,
            retrieves_the_total_count_of_network_applications_by_applying_basic_filtering_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(json_schema_validate, obj):
    json_schema_validate('jsd_ded95db0af275081801b54e0ce105c71_v3_1_3_0').validate(obj)
    return True


def retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(api):
    endpoint_result = api.applications.retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 0}],
        page={'limit': 0, 'offset': 0, 'cursor': 'string', 'sortBy': [{'name': 'string', 'function': 'string', 'order': 'string'}]},
        payload=None,
        siteIds=['string'],
        startTime=0
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(api, validator):
    try:
        assert is_valid_retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
            validator,
            retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics_default_val(api):
    endpoint_result = api.applications.retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        siteIds=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics_default_val(api, validator):
    try:
        assert is_valid_retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
            validator,
            retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_trend_analytics_data_related_to_network_applications(json_schema_validate, obj):
    json_schema_validate('jsd_154870476ce35f19bc4c1d058aa01536_v3_1_3_0').validate(obj)
    return True


def retrieves_the_trend_analytics_data_related_to_network_applications(api):
    endpoint_result = api.applications.retrieves_the_trend_analytics_data_related_to_network_applications(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 0}],
        groupBy=['string'],
        page={'limit': 0, 'cursor': 'string', 'timeSortOrder': 'string'},
        payload=None,
        siteIds=['string'],
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_trend_analytics_data_related_to_network_applications(api, validator):
    try:
        assert is_valid_retrieves_the_trend_analytics_data_related_to_network_applications(
            validator,
            retrieves_the_trend_analytics_data_related_to_network_applications(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_trend_analytics_data_related_to_network_applications_default_val(api):
    endpoint_result = api.applications.retrieves_the_trend_analytics_data_related_to_network_applications(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        payload=None,
        siteIds=None,
        startTime=None,
        trendInterval=None
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_trend_analytics_data_related_to_network_applications_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_trend_analytics_data_related_to_network_applications(
            validator,
            retrieves_the_trend_analytics_data_related_to_network_applications_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_trend_analytics_related_to_specific_network_application(json_schema_validate, obj):
    json_schema_validate('jsd_755b33956f3e56c6b8d234e7ed6a20e6_v3_1_3_0').validate(obj)
    return True


def retrieves_the_trend_analytics_related_to_specific_network_application(api):
    endpoint_result = api.applications.retrieves_the_trend_analytics_related_to_specific_network_application(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string'}],
        id='string',
        page={'limit': 0, 'cursor': 'string', 'timeSortOrder': 'string'},
        payload=None,
        siteIds=['string'],
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_trend_analytics_related_to_specific_network_application(api, validator):
    try:
        assert is_valid_retrieves_the_trend_analytics_related_to_specific_network_application(
            validator,
            retrieves_the_trend_analytics_related_to_specific_network_application(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_trend_analytics_related_to_specific_network_application_default_val(api):
    endpoint_result = api.applications.retrieves_the_trend_analytics_related_to_specific_network_application(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        id='string',
        page=None,
        payload=None,
        siteIds=None,
        startTime=None,
        trendInterval=None
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_trend_analytics_related_to_specific_network_application_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_trend_analytics_related_to_specific_network_application(
            validator,
            retrieves_the_trend_analytics_related_to_specific_network_application_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(json_schema_validate, obj):
    json_schema_validate('jsd_a499ab977fea5c139c9344227c7769a5_v3_1_3_0').validate(obj)
    return True


def retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(api):
    endpoint_result = api.applications.retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(
        agent_id='string',
        attribute='string',
        end_time=0,
        limit=0,
        network_device_name='string',
        offset=0,
        order='string',
        site_id='string',
        sort_by='string',
        start_time=0,
        test_id='string',
        test_name='string',
        test_type='string'
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(
            validator,
            retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics_default_val(api):
    endpoint_result = api.applications.retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(
        agent_id=None,
        attribute=None,
        end_time=None,
        limit=None,
        network_device_name=None,
        offset=None,
        order=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        test_id=None,
        test_name=None,
        test_type=None
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(
            validator,
            retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_count_of_thousand_eyes_test_results(json_schema_validate, obj):
    json_schema_validate('jsd_ef366ca484355d15937dd851a67c88e3_v3_1_3_0').validate(obj)
    return True


def retrieves_the_total_count_of_thousand_eyes_test_results(api):
    endpoint_result = api.applications.retrieves_the_total_count_of_thousand_eyes_test_results(
        agent_id='string',
        end_time=0,
        network_device_name='string',
        site_id='string',
        start_time=0,
        test_id='string',
        test_name='string',
        test_type='string'
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_total_count_of_thousand_eyes_test_results(api, validator):
    try:
        assert is_valid_retrieves_the_total_count_of_thousand_eyes_test_results(
            validator,
            retrieves_the_total_count_of_thousand_eyes_test_results(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_count_of_thousand_eyes_test_results_default_val(api):
    endpoint_result = api.applications.retrieves_the_total_count_of_thousand_eyes_test_results(
        agent_id=None,
        end_time=None,
        network_device_name=None,
        site_id=None,
        start_time=None,
        test_id=None,
        test_name=None,
        test_type=None
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_total_count_of_thousand_eyes_test_results_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_total_count_of_thousand_eyes_test_results(
            validator,
            retrieves_the_total_count_of_thousand_eyes_test_results_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(json_schema_validate, obj):
    json_schema_validate('jsd_42af0e7bab8659f19c619fae31772d15_v3_1_3_0').validate(obj)
    return True


def the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(api):
    endpoint_result = api.applications.the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
        agent_id='string',
        end_time=0,
        limit=0,
        network_device_name='string',
        offset=0,
        order='string',
        site_id='string',
        start_time=0,
        test_id='string',
        test_name='string',
        test_type='string',
        trend_interval='string'
    )
    return endpoint_result


@pytest.mark.applications
def test_the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(api, validator):
    try:
        assert is_valid_the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
            validator,
            the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range_default_val(api):
    endpoint_result = api.applications.the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
        agent_id=None,
        end_time=None,
        limit=None,
        network_device_name=None,
        offset=None,
        order=None,
        site_id=None,
        start_time=None,
        test_id=None,
        test_name=None,
        test_type=None,
        trend_interval=None
    )
    return endpoint_result


@pytest.mark.applications
def test_the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range_default_val(api, validator):
    try:
        assert is_valid_the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
            validator,
            the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_applications(json_schema_validate, obj):
    json_schema_validate('jsd_1b85e4ce533d5ff49ddd3b2f9657cfa5_v3_1_3_0').validate(obj)
    return True


def applications(api):
    endpoint_result = api.applications.applications(
        application_health='string',
        application_name='string',
        device_id='string',
        end_time=0,
        limit=0,
        mac_address='string',
        offset=0,
        site_id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.applications
def test_applications(api, validator):
    try:
        assert is_valid_applications(
            validator,
            applications(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def applications_default_val(api):
    endpoint_result = api.applications.applications(
        application_health=None,
        application_name=None,
        device_id=None,
        end_time=None,
        limit=None,
        mac_address=None,
        offset=None,
        site_id=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.applications
def test_applications_default_val(api, validator):
    try:
        assert is_valid_applications(
            validator,
            applications_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

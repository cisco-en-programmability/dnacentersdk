# -*- coding: utf-8 -*-
"""CatalystCenterAPI sites API fixtures and tests.

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

pytestmark = pytest.mark.skipif(
    DNA_CENTER_VERSION != "2.3.7.9", reason="version does not match"
)


def is_valid_read_list_of_site_health_summaries(json_schema_validate, obj):
    json_schema_validate("jsd_870b40b4f6d558bfbebcf8fcbc4df56b_v2_3_7_9").validate(obj)
    return True


def read_list_of_site_health_summaries(api):
    endpoint_result = api.sites.read_list_of_site_health_summaries(
        attribute="string",
        end_time=0,
        id="string",
        limit=0,
        offset=0,
        order="string",
        site_hierarchy="string",
        site_hierarchy_id="string",
        site_type="string",
        sort_by="string",
        start_time=0,
        view="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_read_list_of_site_health_summaries(api, validator):
    try:
        assert is_valid_read_list_of_site_health_summaries(
            validator, read_list_of_site_health_summaries(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_list_of_site_health_summaries_default_val(api):
    endpoint_result = api.sites.read_list_of_site_health_summaries(
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
        view=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_read_list_of_site_health_summaries_default_val(api, validator):
    try:
        assert is_valid_read_list_of_site_health_summaries(
            validator, read_list_of_site_health_summaries_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_site_count(json_schema_validate, obj):
    json_schema_validate("jsd_e67558dd99925a0385f5f870bbb8f634_v2_3_7_9").validate(obj)
    return True


def read_site_count(api):
    endpoint_result = api.sites.read_site_count(
        end_time=0,
        id="string",
        site_hierarchy="string",
        site_hierarchy_id="string",
        site_type="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_read_site_count(api, validator):
    try:
        assert is_valid_read_site_count(validator, read_site_count(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_site_count_default_val(api):
    endpoint_result = api.sites.read_site_count(
        end_time=None,
        id=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_type=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_read_site_count_default_val(api, validator):
    try:
        assert is_valid_read_site_count(validator, read_site_count_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_an_aggregated_summary_of_site_health_data(json_schema_validate, obj):
    json_schema_validate("jsd_fc80b3e12ee9577a8e7fa5d4cd84e8fc_v2_3_7_9").validate(obj)
    return True


def read_an_aggregated_summary_of_site_health_data(api):
    endpoint_result = api.sites.read_an_aggregated_summary_of_site_health_data(
        attribute="string",
        end_time=0,
        id="string",
        site_hierarchy="string",
        site_hierarchy_id="string",
        site_type="string",
        start_time=0,
        view="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_read_an_aggregated_summary_of_site_health_data(api, validator):
    try:
        assert is_valid_read_an_aggregated_summary_of_site_health_data(
            validator, read_an_aggregated_summary_of_site_health_data(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_an_aggregated_summary_of_site_health_data_default_val(api):
    endpoint_result = api.sites.read_an_aggregated_summary_of_site_health_data(
        attribute=None,
        end_time=None,
        id=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_type=None,
        start_time=None,
        view=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_read_an_aggregated_summary_of_site_health_data_default_val(api, validator):
    try:
        assert is_valid_read_an_aggregated_summary_of_site_health_data(
            validator, read_an_aggregated_summary_of_site_health_data_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_an_aggregated_summary_of_site_health_data(json_schema_validate, obj):
    json_schema_validate("jsd_8bec2dde673c5b2f940d0474fed32af6_v2_3_7_9").validate(obj)
    return True


def query_an_aggregated_summary_of_site_health_data(api):
    endpoint_result = api.sites.query_an_aggregated_summary_of_site_health_data(
        active_validation=True,
        attributes=["string"],
        endTime=0,
        id="string",
        payload=None,
        site_hierarchy="string",
        site_hierarchy_id="string",
        site_type="string",
        startTime=0,
        views=["string"],
    )
    return endpoint_result


@pytest.mark.sites
def test_query_an_aggregated_summary_of_site_health_data(api, validator):
    try:
        assert is_valid_query_an_aggregated_summary_of_site_health_data(
            validator, query_an_aggregated_summary_of_site_health_data(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def query_an_aggregated_summary_of_site_health_data_default_val(api):
    endpoint_result = api.sites.query_an_aggregated_summary_of_site_health_data(
        active_validation=True,
        attributes=None,
        endTime=None,
        id=None,
        payload=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_type=None,
        startTime=None,
        views=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_query_an_aggregated_summary_of_site_health_data_default_val(api, validator):
    try:
        assert is_valid_query_an_aggregated_summary_of_site_health_data(
            validator, query_an_aggregated_summary_of_site_health_data_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_trend_analytics_data_for_a_grouping_of_sites_in_your_network(
    json_schema_validate, obj
):
    json_schema_validate("jsd_0181a47540d95b8ba6d78bfe5db7dbe2_v2_3_7_9").validate(obj)
    return True


def read_trend_analytics_data_for_a_grouping_of_sites_in_your_network(api):
    endpoint_result = (
        api.sites.read_trend_analytics_data_for_a_grouping_of_sites_in_your_network(
            attribute="string",
            end_time=0,
            id="string",
            limit=0,
            offset=0,
            site_hierarchy="string",
            site_hierarchy_id="string",
            site_type="string",
            start_time=0,
            task_id="string",
            time_sort_order="string",
            trend_interval="string",
        )
    )
    return endpoint_result


@pytest.mark.sites
def test_read_trend_analytics_data_for_a_grouping_of_sites_in_your_network(
    api, validator
):
    try:
        assert (
            is_valid_read_trend_analytics_data_for_a_grouping_of_sites_in_your_network(
                validator,
                read_trend_analytics_data_for_a_grouping_of_sites_in_your_network(api),
            )
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_default_val(api):
    endpoint_result = (
        api.sites.read_trend_analytics_data_for_a_grouping_of_sites_in_your_network(
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
            trend_interval=None,
        )
    )
    return endpoint_result


@pytest.mark.sites
def test_read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_default_val(
    api, validator
):
    try:
        assert is_valid_read_trend_analytics_data_for_a_grouping_of_sites_in_your_network(
            validator,
            read_trend_analytics_data_for_a_grouping_of_sites_in_your_network_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_site_health_summary_data_by_site_id(json_schema_validate, obj):
    json_schema_validate("jsd_062572f214555abaa6a30cdbcc32e713_v2_3_7_9").validate(obj)
    return True


def read_site_health_summary_data_by_site_id(api):
    endpoint_result = api.sites.read_site_health_summary_data_by_site_id(
        attribute="string", end_time=0, id="string", start_time=0, view="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_read_site_health_summary_data_by_site_id(api, validator):
    try:
        assert is_valid_read_site_health_summary_data_by_site_id(
            validator, read_site_health_summary_data_by_site_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_site_health_summary_data_by_site_id_default_val(api):
    endpoint_result = api.sites.read_site_health_summary_data_by_site_id(
        attribute=None, end_time=None, id="string", start_time=None, view=None
    )
    return endpoint_result


@pytest.mark.sites
def test_read_site_health_summary_data_by_site_id_default_val(api, validator):
    try:
        assert is_valid_read_site_health_summary_data_by_site_id(
            validator, read_site_health_summary_data_by_site_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_trend_analytics_data_for_a_specific_site_in_your_network(
    json_schema_validate, obj
):
    json_schema_validate("jsd_a75ee097a016562cbf861c4c52df3e30_v2_3_7_9").validate(obj)
    return True


def read_trend_analytics_data_for_a_specific_site_in_your_network(api):
    endpoint_result = (
        api.sites.read_trend_analytics_data_for_a_specific_site_in_your_network(
            attribute="string",
            end_time=0,
            id="string",
            limit=0,
            offset=0,
            start_time=0,
            task_id="string",
            time_sort_order="string",
            trend_interval="string",
        )
    )
    return endpoint_result


@pytest.mark.sites
def test_read_trend_analytics_data_for_a_specific_site_in_your_network(api, validator):
    try:
        assert is_valid_read_trend_analytics_data_for_a_specific_site_in_your_network(
            validator,
            read_trend_analytics_data_for_a_specific_site_in_your_network(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_trend_analytics_data_for_a_specific_site_in_your_network_default_val(api):
    endpoint_result = (
        api.sites.read_trend_analytics_data_for_a_specific_site_in_your_network(
            attribute=None,
            end_time=None,
            id="string",
            limit=None,
            offset=None,
            start_time=None,
            task_id=None,
            time_sort_order=None,
            trend_interval=None,
        )
    )
    return endpoint_result


@pytest.mark.sites
def test_read_trend_analytics_data_for_a_specific_site_in_your_network_default_val(
    api, validator
):
    try:
        assert is_valid_read_trend_analytics_data_for_a_specific_site_in_your_network(
            validator,
            read_trend_analytics_data_for_a_specific_site_in_your_network_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters(
    json_schema_validate, obj
):
    json_schema_validate("jsd_4181fd376c6a5d9382d5bee853c43031_v2_3_7_9").validate(obj)
    return True


def get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters(
    api,
):
    endpoint_result = api.sites.get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters(
        attribute="string",
        band="string",
        end_time=0,
        failure_category="string",
        failure_reason="string",
        limit=0,
        offset=0,
        order="string",
        site_hierarchy="string",
        site_hierarchy_id="string",
        site_id="string",
        site_type="string",
        sort_by="string",
        ssid="string",
        start_time=0,
        task_id="string",
        view="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters(
    api, validator
):
    try:
        assert is_valid_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters(
            validator,
            get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_default_val(
    api,
):
    endpoint_result = api.sites.get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters(
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
        view=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_default_val(
    api, validator
):
    try:
        assert is_valid_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters(
            validator,
            get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters(
    json_schema_validate, obj
):
    json_schema_validate("jsd_af22da7f49fd5d658d0ce2992ea7fef9_v2_3_7_9").validate(obj)
    return True


def get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters(
    api,
):
    endpoint_result = api.sites.get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters(
        end_time=0,
        site_hierarchy="string",
        site_hierarchy_id="string",
        site_id="string",
        site_type="string",
        start_time=0,
    )
    return endpoint_result


@pytest.mark.sites
def test_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters(
    api, validator
):
    try:
        assert is_valid_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters(
            validator,
            get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_default_val(
    api,
):
    endpoint_result = api.sites.get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters(
        end_time=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_type=None,
        start_time=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_default_val(
    api, validator
):
    try:
        assert is_valid_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters(
            validator,
            get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters(
    json_schema_validate, obj
):
    json_schema_validate("jsd_2647a4829a44597bbf9813664eb75de0_v2_3_7_9").validate(obj)
    return True


def get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters(api):
    endpoint_result = api.sites.get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters(
        active_validation=True,
        attributes=["string"],
        endTime=0,
        filters=[{"key": "string", "operator": "string", "value": "string"}],
        page={"limit": 0, "offset": 0, "sortBy": {"name": "string", "order": "string"}},
        payload=None,
        startTime=0,
        views=["string"],
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters(
    api, validator
):
    try:
        assert is_valid_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters(
            validator,
            get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_default_val(
    api,
):
    endpoint_result = api.sites.get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters(
        active_validation=True,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None,
        views=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_default_val(
    api, validator
):
    try:
        assert is_valid_get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters(
            validator,
            get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters(
    json_schema_validate, obj
):
    json_schema_validate("jsd_4db690b800995e35bc4e8c43d8ea6c18_v2_3_7_9").validate(obj)
    return True


def get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters(
    api,
):
    endpoint_result = api.sites.get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters(
        active_validation=True,
        endTime=0,
        filters=[{"key": "string", "operator": "string", "value": "string"}],
        payload=None,
        startTime=0,
    )
    return endpoint_result


@pytest.mark.sites
def test_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters(
    api, validator
):
    try:
        assert is_valid_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters(
            validator,
            get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_default_val(
    api,
):
    endpoint_result = api.sites.get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters(
        active_validation=True, endTime=None, filters=None, payload=None, startTime=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_default_val(
    api, validator
):
    try:
        assert is_valid_get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters(
            validator,
            get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_analytics_summary_data_for_the_given_task_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_131c846dfbe75601831b5de7e8771829_v2_3_7_9").validate(obj)
    return True


def get_site_analytics_summary_data_for_the_given_task_id(api):
    endpoint_result = api.sites.get_site_analytics_summary_data_for_the_given_task_id(
        task_id="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_summary_data_for_the_given_task_id(api, validator):
    try:
        assert is_valid_get_site_analytics_summary_data_for_the_given_task_id(
            validator, get_site_analytics_summary_data_for_the_given_task_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_analytics_summary_data_for_the_given_task_id_default_val(api):
    endpoint_result = api.sites.get_site_analytics_summary_data_for_the_given_task_id(
        task_id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_summary_data_for_the_given_task_id_default_val(
    api, validator
):
    try:
        assert is_valid_get_site_analytics_summary_data_for_the_given_task_id(
            validator,
            get_site_analytics_summary_data_for_the_given_task_id_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_submit_request_for_site_analytics_summary_data(json_schema_validate, obj):
    json_schema_validate("jsd_5345b8a44ba454de8a7bb52d3efe97ca_v2_3_7_9").validate(obj)
    return True


def submit_request_for_site_analytics_summary_data(api):
    endpoint_result = api.sites.submit_request_for_site_analytics_summary_data(
        active_validation=True,
        attributes=["string"],
        endTime=0,
        filters=[{"key": "string", "operator": "string", "value": "string"}],
        payload=None,
        startTime=0,
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_for_site_analytics_summary_data(api, validator):
    try:
        assert is_valid_submit_request_for_site_analytics_summary_data(
            validator, submit_request_for_site_analytics_summary_data(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def submit_request_for_site_analytics_summary_data_default_val(api):
    endpoint_result = api.sites.submit_request_for_site_analytics_summary_data(
        active_validation=True,
        attributes=None,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_for_site_analytics_summary_data_default_val(api, validator):
    try:
        assert is_valid_submit_request_for_site_analytics_summary_data(
            validator, submit_request_for_site_analytics_summary_data_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_top_n_entities_related_to_site_analytics_for_the_given_task_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_20e256f5fc9757c483f41ffef3677fef_v2_3_7_9").validate(obj)
    return True


def get_top_n_entities_related_to_site_analytics_for_the_given_task_id(api):
    endpoint_result = (
        api.sites.get_top_n_entities_related_to_site_analytics_for_the_given_task_id(
            task_id="string"
        )
    )
    return endpoint_result


@pytest.mark.sites
def test_get_top_n_entities_related_to_site_analytics_for_the_given_task_id(
    api, validator
):
    try:
        assert (
            is_valid_get_top_n_entities_related_to_site_analytics_for_the_given_task_id(
                validator,
                get_top_n_entities_related_to_site_analytics_for_the_given_task_id(api),
            )
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_top_n_entities_related_to_site_analytics_for_the_given_task_id_default_val(api):
    endpoint_result = (
        api.sites.get_top_n_entities_related_to_site_analytics_for_the_given_task_id(
            task_id=None
        )
    )
    return endpoint_result


@pytest.mark.sites
def test_get_top_n_entities_related_to_site_analytics_for_the_given_task_id_default_val(
    api, validator
):
    try:
        assert is_valid_get_top_n_entities_related_to_site_analytics_for_the_given_task_id(
            validator,
            get_top_n_entities_related_to_site_analytics_for_the_given_task_id_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_submit_request_for_top_n_entities_related_to_site_analytics(
    json_schema_validate, obj
):
    json_schema_validate("jsd_d9e3276d1ed3511b80b22ea8388959c8_v2_3_7_9").validate(obj)
    return True


def submit_request_for_top_n_entities_related_to_site_analytics(api):
    endpoint_result = (
        api.sites.submit_request_for_top_n_entities_related_to_site_analytics(
            active_validation=True,
            endTime=0,
            filters=[{"key": "string", "operator": "string", "value": "string"}],
            groupBy=["string"],
            payload=None,
            startTime=0,
            topN=0,
        )
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_for_top_n_entities_related_to_site_analytics(api, validator):
    try:
        assert is_valid_submit_request_for_top_n_entities_related_to_site_analytics(
            validator, submit_request_for_top_n_entities_related_to_site_analytics(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def submit_request_for_top_n_entities_related_to_site_analytics_default_val(api):
    endpoint_result = (
        api.sites.submit_request_for_top_n_entities_related_to_site_analytics(
            active_validation=True,
            endTime=None,
            filters=None,
            groupBy=None,
            payload=None,
            startTime=None,
            topN=None,
        )
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_for_top_n_entities_related_to_site_analytics_default_val(
    api, validator
):
    try:
        assert is_valid_submit_request_for_top_n_entities_related_to_site_analytics(
            validator,
            submit_request_for_top_n_entities_related_to_site_analytics_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_analytics_trend_data_for_the_given_task_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_3f396d5c149b510a8cd8e560f8baae4b_v2_3_7_9").validate(obj)
    return True


def get_site_analytics_trend_data_for_the_given_task_id(api):
    endpoint_result = api.sites.get_site_analytics_trend_data_for_the_given_task_id(
        task_id="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_trend_data_for_the_given_task_id(api, validator):
    try:
        assert is_valid_get_site_analytics_trend_data_for_the_given_task_id(
            validator, get_site_analytics_trend_data_for_the_given_task_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_analytics_trend_data_for_the_given_task_id_default_val(api):
    endpoint_result = api.sites.get_site_analytics_trend_data_for_the_given_task_id(
        task_id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_trend_data_for_the_given_task_id_default_val(
    api, validator
):
    try:
        assert is_valid_get_site_analytics_trend_data_for_the_given_task_id(
            validator,
            get_site_analytics_trend_data_for_the_given_task_id_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_submit_request_for_site_analytics_trend_data(json_schema_validate, obj):
    json_schema_validate("jsd_65edc44e0e7a513191cc16dc2b4da88e_v2_3_7_9").validate(obj)
    return True


def submit_request_for_site_analytics_trend_data(api):
    endpoint_result = api.sites.submit_request_for_site_analytics_trend_data(
        active_validation=True,
        attributes=["string"],
        endTime=0,
        filters=[{"key": "string", "operator": "string", "value": "string"}],
        page={"limit": 0, "offset": 0, "timestampOrder": "string"},
        payload=None,
        startTime=0,
        trendInterval="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_for_site_analytics_trend_data(api, validator):
    try:
        assert is_valid_submit_request_for_site_analytics_trend_data(
            validator, submit_request_for_site_analytics_trend_data(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def submit_request_for_site_analytics_trend_data_default_val(api):
    endpoint_result = api.sites.submit_request_for_site_analytics_trend_data(
        active_validation=True,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        startTime=None,
        trendInterval=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_submit_request_for_site_analytics_trend_data_default_val(api, validator):
    try:
        assert is_valid_submit_request_for_site_analytics_trend_data(
            validator, submit_request_for_site_analytics_trend_data_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_analytics_for_one_site(json_schema_validate, obj):
    json_schema_validate("jsd_69aec803dd6056a0b2a3ebd66dc136d3_v2_3_7_9").validate(obj)
    return True


def get_site_analytics_for_one_site(api):
    endpoint_result = api.sites.get_site_analytics_for_one_site(
        attribute="string",
        band="string",
        end_time=0,
        failure_category="string",
        failure_reason="string",
        id="string",
        ssid="string",
        start_time=0,
        task_id="string",
        view="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_for_one_site(api, validator):
    try:
        assert is_valid_get_site_analytics_for_one_site(
            validator, get_site_analytics_for_one_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_analytics_for_one_site_default_val(api):
    endpoint_result = api.sites.get_site_analytics_for_one_site(
        attribute=None,
        band=None,
        end_time=None,
        failure_category=None,
        failure_reason=None,
        id="string",
        ssid=None,
        start_time=None,
        task_id=None,
        view=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_analytics_for_one_site_default_val(api, validator):
    try:
        assert is_valid_get_site_analytics_for_one_site(
            validator, get_site_analytics_for_one_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_devices_to_site(json_schema_validate, obj):
    json_schema_validate("jsd_0a544e27e18e5412af3b68d915c8ca50_v2_3_7_9").validate(obj)
    return True


def assign_devices_to_site(api):
    endpoint_result = api.sites.assign_devices_to_site(
        active_validation=True,
        device=[{"ip": "string"}],
        payload=None,
        site_id="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_assign_devices_to_site(api, validator):
    try:
        assert is_valid_assign_devices_to_site(validator, assign_devices_to_site(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_devices_to_site_default_val(api):
    endpoint_result = api.sites.assign_devices_to_site(
        active_validation=True, device=None, payload=None, site_id="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_assign_devices_to_site_default_val(api, validator):
    try:
        assert is_valid_assign_devices_to_site(
            validator, assign_devices_to_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_export_map_archive(json_schema_validate, obj):
    json_schema_validate("jsd_c937494318f952ba92eaeb82b144c338_v2_3_7_9").validate(obj)
    return True


def export_map_archive(api):
    endpoint_result = api.sites.export_map_archive(
        active_validation=True, payload=None, site_hierarchy_uuid="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_export_map_archive(api, validator):
    try:
        assert is_valid_export_map_archive(validator, export_map_archive(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def export_map_archive_default_val(api):
    endpoint_result = api.sites.export_map_archive(
        active_validation=True, payload=None, site_hierarchy_uuid="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_export_map_archive_default_val(api, validator):
    try:
        assert is_valid_export_map_archive(
            validator, export_map_archive_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_map_archive_start_import(json_schema_validate, obj):
    json_schema_validate("jsd_07ea81890f92553aaed79952ab7ab363_v2_3_7_9").validate(obj)
    return True


def import_map_archive_start_import(api):
    endpoint_result = api.sites.import_map_archive_start_import(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_start_import(api, validator):
    try:
        assert is_valid_import_map_archive_start_import(
            validator, import_map_archive_start_import(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_map_archive_start_import_default_val(api):
    endpoint_result = api.sites.import_map_archive_start_import(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_start_import_default_val(api, validator):
    try:
        assert is_valid_import_map_archive_start_import(
            validator, import_map_archive_start_import_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_map_archive_cancel_an_import(json_schema_validate, obj):
    json_schema_validate("jsd_44580624a59853e8a3462db736556ab4_v2_3_7_9").validate(obj)
    return True


def import_map_archive_cancel_an_import(api):
    endpoint_result = api.sites.import_map_archive_cancel_an_import(
        import_context_uuid="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_cancel_an_import(api, validator):
    try:
        assert is_valid_import_map_archive_cancel_an_import(
            validator, import_map_archive_cancel_an_import(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_map_archive_cancel_an_import_default_val(api):
    endpoint_result = api.sites.import_map_archive_cancel_an_import(
        import_context_uuid="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_cancel_an_import_default_val(api, validator):
    try:
        assert is_valid_import_map_archive_cancel_an_import(
            validator, import_map_archive_cancel_an_import_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_map_archive_perform_import(json_schema_validate, obj):
    json_schema_validate("jsd_df05fb7a09595d0b9f6bc46b24275927_v2_3_7_9").validate(obj)
    return True


def import_map_archive_perform_import(api):
    endpoint_result = api.sites.import_map_archive_perform_import(
        active_validation=True, import_context_uuid="string", payload=None
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_perform_import(api, validator):
    try:
        assert is_valid_import_map_archive_perform_import(
            validator, import_map_archive_perform_import(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_map_archive_perform_import_default_val(api):
    endpoint_result = api.sites.import_map_archive_perform_import(
        active_validation=True, import_context_uuid="string", payload=None
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_perform_import_default_val(api, validator):
    try:
        assert is_valid_import_map_archive_perform_import(
            validator, import_map_archive_perform_import_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_map_archive_import_status(json_schema_validate, obj):
    json_schema_validate("jsd_c04c790688e4566c9f5eaa52b8fe39c8_v2_3_7_9").validate(obj)
    return True


def import_map_archive_import_status(api):
    endpoint_result = api.sites.import_map_archive_import_status(
        import_context_uuid="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_import_status(api, validator):
    try:
        assert is_valid_import_map_archive_import_status(
            validator, import_map_archive_import_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_map_archive_import_status_default_val(api):
    endpoint_result = api.sites.import_map_archive_import_status(
        import_context_uuid="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_import_status_default_val(api, validator):
    try:
        assert is_valid_import_map_archive_import_status(
            validator, import_map_archive_import_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_maps_supported_access_points(json_schema_validate, obj):
    json_schema_validate("jsd_8a5e16b065e3534c8894e52d52540f99_v2_3_7_9").validate(obj)
    return True


def maps_supported_access_points(api):
    endpoint_result = api.sites.maps_supported_access_points()
    return endpoint_result


@pytest.mark.sites
def test_maps_supported_access_points(api, validator):
    try:
        assert is_valid_maps_supported_access_points(
            validator, maps_supported_access_points(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def maps_supported_access_points_default_val(api):
    endpoint_result = api.sites.maps_supported_access_points()
    return endpoint_result


@pytest.mark.sites
def test_maps_supported_access_points_default_val(api, validator):
    try:
        assert is_valid_maps_supported_access_points(
            validator, maps_supported_access_points_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_membership(json_schema_validate, obj):
    json_schema_validate("jsd_63284ca11e0b5f8d91395e2462a9cfdc_v2_3_7_9").validate(obj)
    return True


def get_membership(api):
    endpoint_result = api.sites.get_membership(
        device_family="string",
        limit=0,
        offset=0,
        serial_number="string",
        site_id="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_get_membership(api, validator):
    try:
        assert is_valid_get_membership(validator, get_membership(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_membership_default_val(api):
    endpoint_result = api.sites.get_membership(
        device_family=None,
        limit=None,
        offset=None,
        serial_number=None,
        site_id="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_get_membership_default_val(api, validator):
    try:
        assert is_valid_get_membership(validator, get_membership_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_site(json_schema_validate, obj):
    json_schema_validate("jsd_bce8e6b307ce52dd8f5546fbd78e05ee_v2_3_7_9").validate(obj)
    return True


def create_site(api):
    endpoint_result = api.sites.create_site(
        active_validation=True,
        payload=None,
        site={
            "area": {"name": "string", "parentName": "string"},
            "building": {
                "name": "string",
                "address": "string",
                "parentName": "string",
                "latitude": 0,
                "longitude": 0,
                "country": "string",
            },
            "floor": {
                "name": "string",
                "parentName": "string",
                "rfModel": "string",
                "width": 0,
                "length": 0,
                "height": 0,
                "floorNumber": 0,
            },
        },
        type="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_create_site(api, validator):
    try:
        assert is_valid_create_site(validator, create_site(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_site_default_val(api):
    endpoint_result = api.sites.create_site(
        active_validation=True, payload=None, site=None, type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_create_site_default_val(api, validator):
    try:
        assert is_valid_create_site(validator, create_site_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site(json_schema_validate, obj):
    json_schema_validate("jsd_dbdd6074bedc59b9a3edd6477897d659_v2_3_7_9").validate(obj)
    return True


def get_site(api):
    endpoint_result = api.sites.get_site(
        limit=0, name="string", offset=0, site_id="string", type="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site(api, validator):
    try:
        assert is_valid_get_site(validator, get_site(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_default_val(api):
    endpoint_result = api.sites.get_site(
        limit=None, name=None, offset=None, site_id=None, type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_default_val(api, validator):
    try:
        assert is_valid_get_site(validator, get_site_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_health(json_schema_validate, obj):
    json_schema_validate("jsd_ae4b592f66035f24b55028f79c1b7290_v2_3_7_9").validate(obj)
    return True


def get_site_health(api):
    endpoint_result = api.sites.get_site_health(
        limit=0, offset=0, site_type="string", timestamp=0
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_health(api, validator):
    try:
        assert is_valid_get_site_health(validator, get_site_health(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_health_default_val(api):
    endpoint_result = api.sites.get_site_health(
        limit=None, offset=None, site_type=None, timestamp=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_health_default_val(api, validator):
    try:
        assert is_valid_get_site_health(validator, get_site_health_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_devices_that_are_assigned_to_a_site(json_schema_validate, obj):
    json_schema_validate("jsd_cfabe762b2af55f282076fe2a14b6792_v2_3_7_9").validate(obj)
    return True


def get_devices_that_are_assigned_to_a_site(api):
    endpoint_result = api.sites.get_devices_that_are_assigned_to_a_site(
        id="string",
        level="string",
        limit="string",
        member_type="string",
        offset="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_get_devices_that_are_assigned_to_a_site(api, validator):
    try:
        assert is_valid_get_devices_that_are_assigned_to_a_site(
            validator, get_devices_that_are_assigned_to_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_devices_that_are_assigned_to_a_site_default_val(api):
    endpoint_result = api.sites.get_devices_that_are_assigned_to_a_site(
        id="string", level=None, limit=None, member_type=None, offset=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_devices_that_are_assigned_to_a_site_default_val(api, validator):
    try:
        assert is_valid_get_devices_that_are_assigned_to_a_site(
            validator, get_devices_that_are_assigned_to_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_count(json_schema_validate, obj):
    json_schema_validate("jsd_e7a025fbe2c452fc82eedd5c50104aba_v2_3_7_9").validate(obj)
    return True


def get_site_count(api):
    endpoint_result = api.sites.get_site_count(site_id="string")
    return endpoint_result


@pytest.mark.sites
def test_get_site_count(api, validator):
    try:
        assert is_valid_get_site_count(validator, get_site_count(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_count_default_val(api):
    endpoint_result = api.sites.get_site_count(site_id=None)
    return endpoint_result


@pytest.mark.sites
def test_get_site_count_default_val(api, validator):
    try:
        assert is_valid_get_site_count(validator, get_site_count_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_site(json_schema_validate, obj):
    json_schema_validate("jsd_27df9908ad265e83ab77d73803925678_v2_3_7_9").validate(obj)
    return True


def update_site(api):
    endpoint_result = api.sites.update_site(
        active_validation=True,
        payload=None,
        site={
            "area": {"name": "string", "parentName": "string"},
            "building": {
                "name": "string",
                "address": "string",
                "parentName": "string",
                "latitude": 0,
                "longitude": 0,
                "country": "string",
            },
            "floor": {
                "name": "string",
                "rfModel": "string",
                "width": 0,
                "length": 0,
                "height": 0,
                "floorNumber": 0,
                "parentName": "string",
            },
        },
        site_id="string",
        type="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_update_site(api, validator):
    try:
        assert is_valid_update_site(validator, update_site(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_site_default_val(api):
    endpoint_result = api.sites.update_site(
        active_validation=True, payload=None, site=None, site_id="string", type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_update_site_default_val(api, validator):
    try:
        assert is_valid_update_site(validator, update_site_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_site(json_schema_validate, obj):
    json_schema_validate("jsd_ba5567f03dea5b6891957dd410319e3f_v2_3_7_9").validate(obj)
    return True


def delete_site(api):
    endpoint_result = api.sites.delete_site(site_id="string")
    return endpoint_result


@pytest.mark.sites
def test_delete_site(api, validator):
    try:
        assert is_valid_delete_site(validator, delete_site(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_site_default_val(api):
    endpoint_result = api.sites.delete_site(site_id="string")
    return endpoint_result


@pytest.mark.sites
def test_delete_site_default_val(api, validator):
    try:
        assert is_valid_delete_site(validator, delete_site_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_v2(json_schema_validate, obj):
    json_schema_validate("jsd_43c5e65cce2954fdb7177ac0a8e0b76f_v2_3_7_9").validate(obj)
    return True


def get_site_v2(api):
    endpoint_result = api.sites.get_site_v2(
        group_name_hierarchy="string",
        id="string",
        limit="string",
        offset="string",
        type="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_v2(api, validator):
    try:
        assert is_valid_get_site_v2(validator, get_site_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_v2_default_val(api):
    endpoint_result = api.sites.get_site_v2(
        group_name_hierarchy=None, id=None, limit=None, offset=None, type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_v2_default_val(api, validator):
    try:
        assert is_valid_get_site_v2(validator, get_site_v2_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_count_v2(json_schema_validate, obj):
    json_schema_validate("jsd_371b10ff66e5568ebe6d41faeeabda22_v2_3_7_9").validate(obj)
    return True


def get_site_count_v2(api):
    endpoint_result = api.sites.get_site_count_v2(id="string")
    return endpoint_result


@pytest.mark.sites
def test_get_site_count_v2(api, validator):
    try:
        assert is_valid_get_site_count_v2(validator, get_site_count_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_count_v2_default_val(api):
    endpoint_result = api.sites.get_site_count_v2(id=None)
    return endpoint_result


@pytest.mark.sites
def test_get_site_count_v2_default_val(api, validator):
    try:
        assert is_valid_get_site_count_v2(validator, get_site_count_v2_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

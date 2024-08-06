# -*- coding: utf-8 -*-
"""DNACenterAPI issues API fixtures and tests.

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


def is_valid_get_the_details_of_issues_for_given_set_of_filters2(json_schema_validate, obj):
    json_schema_validate('jsd_fe0609bc1db7594aabd91218a84f7cbf_v2_3_7_6').validate(obj)
    return True


def get_the_details_of_issues_for_given_set_of_filters2(api):
    endpoint_result = api.issues.get_the_details_of_issues_for_given_set_of_filters2(
        ai_driven=True,
        attribute='string',
        category='string',
        device_type='string',
        end_time=0,
        entity_id='string',
        entity_type='string',
        fabric_driven=True,
        fabric_site_driven=True,
        fabric_site_id='string',
        fabric_transit_driven=True,
        fabric_transit_site_id='string',
        fabric_vn_driven=True,
        fabric_vn_name='string',
        is_global=True,
        issue_id='string',
        limit=0,
        mac_address='string',
        name='string',
        network_device_id='string',
        network_device_ip_address='string',
        offset=0,
        order='string',
        priority='string',
        severity='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        site_name='string',
        sort_by='string',
        start_time=0,
        status='string',
        updated_by='string',
        view='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_details_of_issues_for_given_set_of_filters2(api, validator):
    try:
        assert is_valid_get_the_details_of_issues_for_given_set_of_filters2(
            validator,
            get_the_details_of_issues_for_given_set_of_filters2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_details_of_issues_for_given_set_of_filters2_default_val(api):
    endpoint_result = api.issues.get_the_details_of_issues_for_given_set_of_filters2(
        ai_driven=None,
        attribute=None,
        category=None,
        device_type=None,
        end_time=None,
        entity_id=None,
        entity_type=None,
        fabric_driven=None,
        fabric_site_driven=None,
        fabric_site_id=None,
        fabric_transit_driven=None,
        fabric_transit_site_id=None,
        fabric_vn_driven=None,
        fabric_vn_name=None,
        is_global=None,
        issue_id=None,
        limit=None,
        mac_address=None,
        name=None,
        network_device_id=None,
        network_device_ip_address=None,
        offset=None,
        order=None,
        priority=None,
        severity=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_name=None,
        sort_by=None,
        start_time=None,
        status=None,
        updated_by=None,
        view=None
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_details_of_issues_for_given_set_of_filters2_default_val(api, validator):
    try:
        assert is_valid_get_the_details_of_issues_for_given_set_of_filters2(
            validator,
            get_the_details_of_issues_for_given_set_of_filters2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_total_number_of_issues_for_given_set_of_filters2(json_schema_validate, obj):
    json_schema_validate('jsd_537ada8eb3ff5b8db9eccfb778cc578e_v2_3_7_6').validate(obj)
    return True


def get_the_total_number_of_issues_for_given_set_of_filters2(api):
    endpoint_result = api.issues.get_the_total_number_of_issues_for_given_set_of_filters2(
        ai_driven=True,
        category='string',
        device_type='string',
        end_time=0,
        entity_id='string',
        entity_type='string',
        fabric_driven=True,
        fabric_site_driven=True,
        fabric_site_id='string',
        fabric_transit_driven=True,
        fabric_transit_site_id='string',
        fabric_vn_driven=True,
        fabric_vn_name='string',
        is_global=True,
        issue_id='string',
        mac_address='string',
        name='string',
        network_device_id='string',
        network_device_ip_address='string',
        priority='string',
        severity='string',
        site_hierarchy='string',
        site_hierarchy_id='string',
        site_id='string',
        site_name='string',
        start_time=0,
        status='string',
        updated_by='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_total_number_of_issues_for_given_set_of_filters2(api, validator):
    try:
        assert is_valid_get_the_total_number_of_issues_for_given_set_of_filters2(
            validator,
            get_the_total_number_of_issues_for_given_set_of_filters2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_total_number_of_issues_for_given_set_of_filters2_default_val(api):
    endpoint_result = api.issues.get_the_total_number_of_issues_for_given_set_of_filters2(
        ai_driven=None,
        category=None,
        device_type=None,
        end_time=None,
        entity_id=None,
        entity_type=None,
        fabric_driven=None,
        fabric_site_driven=None,
        fabric_site_id=None,
        fabric_transit_driven=None,
        fabric_transit_site_id=None,
        fabric_vn_driven=None,
        fabric_vn_name=None,
        is_global=None,
        issue_id=None,
        mac_address=None,
        name=None,
        network_device_id=None,
        network_device_ip_address=None,
        priority=None,
        severity=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_name=None,
        start_time=None,
        status=None,
        updated_by=None
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_total_number_of_issues_for_given_set_of_filters2_default_val(api, validator):
    try:
        assert is_valid_get_the_total_number_of_issues_for_given_set_of_filters2(
            validator,
            get_the_total_number_of_issues_for_given_set_of_filters2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_details_of_issues_for_given_set_of_filters(json_schema_validate, obj):
    json_schema_validate('jsd_93b818044610579a9b74ec582e7739ab_v2_3_7_6').validate(obj)
    return True


def get_the_details_of_issues_for_given_set_of_filters(api):
    endpoint_result = api.issues.get_the_details_of_issues_for_given_set_of_filters(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string', 'logicalOperator': 'string', 'filters': [{'key': 'string', 'operator': 'string', 'value': 'string'}]}],
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_details_of_issues_for_given_set_of_filters(api, validator):
    try:
        assert is_valid_get_the_details_of_issues_for_given_set_of_filters(
            validator,
            get_the_details_of_issues_for_given_set_of_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_details_of_issues_for_given_set_of_filters_default_val(api):
    endpoint_result = api.issues.get_the_details_of_issues_for_given_set_of_filters(
        active_validation=True,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_details_of_issues_for_given_set_of_filters_default_val(api, validator):
    try:
        assert is_valid_get_the_details_of_issues_for_given_set_of_filters(
            validator,
            get_the_details_of_issues_for_given_set_of_filters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_total_number_of_issues_for_given_set_of_filters(json_schema_validate, obj):
    json_schema_validate('jsd_959c14a815ec5938950343f6188f0785_v2_3_7_6').validate(obj)
    return True


def get_the_total_number_of_issues_for_given_set_of_filters(api):
    endpoint_result = api.issues.get_the_total_number_of_issues_for_given_set_of_filters(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string', 'logicalOperator': 'string', 'filters': [{'key': 'string', 'operator': 'string', 'value': 'string'}]}],
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_total_number_of_issues_for_given_set_of_filters(api, validator):
    try:
        assert is_valid_get_the_total_number_of_issues_for_given_set_of_filters(
            validator,
            get_the_total_number_of_issues_for_given_set_of_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_total_number_of_issues_for_given_set_of_filters_default_val(api):
    endpoint_result = api.issues.get_the_total_number_of_issues_for_given_set_of_filters(
        active_validation=True,
        endTime=None,
        filters=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_total_number_of_issues_for_given_set_of_filters_default_val(api, validator):
    try:
        assert is_valid_get_the_total_number_of_issues_for_given_set_of_filters(
            validator,
            get_the_total_number_of_issues_for_given_set_of_filters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_summary_analytics_data_of_issues(json_schema_validate, obj):
    json_schema_validate('jsd_1b269afaaa855d3291b825f724fc8ea9_v2_3_7_6').validate(obj)
    return True


def get_summary_analytics_data_of_issues(api):
    endpoint_result = api.issues.get_summary_analytics_data_of_issues(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string', 'logicalOperator': 'string', 'filters': [{'key': 'string', 'operator': 'string', 'value': 'string'}]}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.issues
def test_get_summary_analytics_data_of_issues(api, validator):
    try:
        assert is_valid_get_summary_analytics_data_of_issues(
            validator,
            get_summary_analytics_data_of_issues(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_summary_analytics_data_of_issues_default_val(api):
    endpoint_result = api.issues.get_summary_analytics_data_of_issues(
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


@pytest.mark.issues
def test_get_summary_analytics_data_of_issues_default_val(api, validator):
    try:
        assert is_valid_get_summary_analytics_data_of_issues(
            validator,
            get_summary_analytics_data_of_issues_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_top_n_analytics_data_of_issues(json_schema_validate, obj):
    json_schema_validate('jsd_e7af120721c7519a84b13bbe4a1a0362_v2_3_7_6').validate(obj)
    return True


def get_top_n_analytics_data_of_issues(api):
    endpoint_result = api.issues.get_top_n_analytics_data_of_issues(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 'string', 'logicalOperator': 'string', 'filters': [{'key': 'string', 'operator': 'string', 'value': 'string'}]}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string'}]},
        payload=None,
        startTime=0,
        topN=0
    )
    return endpoint_result


@pytest.mark.issues
def test_get_top_n_analytics_data_of_issues(api, validator):
    try:
        assert is_valid_get_top_n_analytics_data_of_issues(
            validator,
            get_top_n_analytics_data_of_issues(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_top_n_analytics_data_of_issues_default_val(api):
    endpoint_result = api.issues.get_top_n_analytics_data_of_issues(
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


@pytest.mark.issues
def test_get_top_n_analytics_data_of_issues_default_val(api, validator):
    try:
        assert is_valid_get_top_n_analytics_data_of_issues(
            validator,
            get_top_n_analytics_data_of_issues_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trend_analytics_data_of_issues(json_schema_validate, obj):
    json_schema_validate('jsd_46fee1860b4d509585956565df54a91a_v2_3_7_6').validate(obj)
    return True


def get_trend_analytics_data_of_issues(api):
    endpoint_result = api.issues.get_trend_analytics_data_of_issues(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'key': 'string', 'value': 'string', 'operator': 'string'}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'timestampOrder': 'string'},
        payload=None,
        startTime=0,
        trendInterval='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_get_trend_analytics_data_of_issues(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_of_issues(
            validator,
            get_trend_analytics_data_of_issues(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trend_analytics_data_of_issues_default_val(api):
    endpoint_result = api.issues.get_trend_analytics_data_of_issues(
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


@pytest.mark.issues
def test_get_trend_analytics_data_of_issues_default_val(api, validator):
    try:
        assert is_valid_get_trend_analytics_data_of_issues(
            validator,
            get_trend_analytics_data_of_issues_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id(json_schema_validate, obj):
    json_schema_validate('jsd_0e350bcc73ba5202aeaeed88175f0d44_v2_3_7_6').validate(obj)
    return True


def get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id(api):
    endpoint_result = api.issues.get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id(
        attribute='string',
        id='string',
        view='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id(api, validator):
    try:
        assert is_valid_get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id(
            validator,
            get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id_default_val(api):
    endpoint_result = api.issues.get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id(
        attribute=None,
        id='string',
        view=None
    )
    return endpoint_result


@pytest.mark.issues
def test_get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id_default_val(api, validator):
    try:
        assert is_valid_get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id(
            validator,
            get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_ignore_the_given_list_of_issues(json_schema_validate, obj):
    json_schema_validate('jsd_133f2c49c69c53e7b4f57f2af9a6f597_v2_3_7_6').validate(obj)
    return True


def ignore_the_given_list_of_issues(api):
    endpoint_result = api.issues.ignore_the_given_list_of_issues(
        active_validation=True,
        issueIds=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.issues
def test_ignore_the_given_list_of_issues(api, validator):
    try:
        assert is_valid_ignore_the_given_list_of_issues(
            validator,
            ignore_the_given_list_of_issues(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def ignore_the_given_list_of_issues_default_val(api):
    endpoint_result = api.issues.ignore_the_given_list_of_issues(
        active_validation=True,
        issueIds=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.issues
def test_ignore_the_given_list_of_issues_default_val(api, validator):
    try:
        assert is_valid_ignore_the_given_list_of_issues(
            validator,
            ignore_the_given_list_of_issues_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_resolve_the_given_lists_of_issues(json_schema_validate, obj):
    json_schema_validate('jsd_638710c10072541e94bd16f1aebffe32_v2_3_7_6').validate(obj)
    return True


def resolve_the_given_lists_of_issues(api):
    endpoint_result = api.issues.resolve_the_given_lists_of_issues(
        active_validation=True,
        issueIds=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.issues
def test_resolve_the_given_lists_of_issues(api, validator):
    try:
        assert is_valid_resolve_the_given_lists_of_issues(
            validator,
            resolve_the_given_lists_of_issues(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def resolve_the_given_lists_of_issues_default_val(api):
    endpoint_result = api.issues.resolve_the_given_lists_of_issues(
        active_validation=True,
        issueIds=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.issues
def test_resolve_the_given_lists_of_issues_default_val(api, validator):
    try:
        assert is_valid_resolve_the_given_lists_of_issues(
            validator,
            resolve_the_given_lists_of_issues_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_the_given_issue_by_updating_selected_fields(json_schema_validate, obj):
    json_schema_validate('jsd_03240454bece53a182b45ffa4a1a435e_v2_3_7_6').validate(obj)
    return True


def update_the_given_issue_by_updating_selected_fields(api):
    endpoint_result = api.issues.update_the_given_issue_by_updating_selected_fields(
        active_validation=True,
        id='string',
        notes='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.issues
def test_update_the_given_issue_by_updating_selected_fields(api, validator):
    try:
        assert is_valid_update_the_given_issue_by_updating_selected_fields(
            validator,
            update_the_given_issue_by_updating_selected_fields(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_the_given_issue_by_updating_selected_fields_default_val(api):
    endpoint_result = api.issues.update_the_given_issue_by_updating_selected_fields(
        active_validation=True,
        id='string',
        notes=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.issues
def test_update_the_given_issue_by_updating_selected_fields_default_val(api, validator):
    try:
        assert is_valid_update_the_given_issue_by_updating_selected_fields(
            validator,
            update_the_given_issue_by_updating_selected_fields_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_a_new_user_defined_issue_definitions(json_schema_validate, obj):
    json_schema_validate('jsd_94a4d8313a955433858e0137ba7ef672_v2_3_7_6').validate(obj)
    return True


def creates_a_new_user_defined_issue_definitions(api):
    endpoint_result = api.issues.creates_a_new_user_defined_issue_definitions(
        active_validation=True,
        description='string',
        isEnabled=True,
        isNotificationEnabled=True,
        name='string',
        payload=None,
        priority='string',
        rules=[{'severity': 0, 'facility': 'string', 'mnemonic': 'string', 'pattern': 'string', 'occurrences': 0, 'durationInMinutes': 0}]
    )
    return endpoint_result


@pytest.mark.issues
def test_creates_a_new_user_defined_issue_definitions(api, validator):
    try:
        assert is_valid_creates_a_new_user_defined_issue_definitions(
            validator,
            creates_a_new_user_defined_issue_definitions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_a_new_user_defined_issue_definitions_default_val(api):
    endpoint_result = api.issues.creates_a_new_user_defined_issue_definitions(
        active_validation=True,
        description=None,
        isEnabled=None,
        isNotificationEnabled=None,
        name=None,
        payload=None,
        priority=None,
        rules=None
    )
    return endpoint_result


@pytest.mark.issues
def test_creates_a_new_user_defined_issue_definitions_default_val(api, validator):
    try:
        assert is_valid_creates_a_new_user_defined_issue_definitions(
            validator,
            creates_a_new_user_defined_issue_definitions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_the_custom_issue_definitions_based_on_the_given_filters(json_schema_validate, obj):
    json_schema_validate('jsd_a51b856ea8005c8cbf42ab64da3e1786_v2_3_7_6').validate(obj)
    return True


def get_all_the_custom_issue_definitions_based_on_the_given_filters(api):
    endpoint_result = api.issues.get_all_the_custom_issue_definitions_based_on_the_given_filters(
        facility='string',
        id='string',
        is_enabled=True,
        limit=0,
        mnemonic='string',
        name='string',
        offset=0,
        order='string',
        priority='string',
        profile_id='string',
        severity=0,
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_get_all_the_custom_issue_definitions_based_on_the_given_filters(api, validator):
    try:
        assert is_valid_get_all_the_custom_issue_definitions_based_on_the_given_filters(
            validator,
            get_all_the_custom_issue_definitions_based_on_the_given_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_the_custom_issue_definitions_based_on_the_given_filters_default_val(api):
    endpoint_result = api.issues.get_all_the_custom_issue_definitions_based_on_the_given_filters(
        facility=None,
        id=None,
        is_enabled=None,
        limit=None,
        mnemonic=None,
        name=None,
        offset=None,
        order=None,
        priority=None,
        profile_id=None,
        severity=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.issues
def test_get_all_the_custom_issue_definitions_based_on_the_given_filters_default_val(api, validator):
    try:
        assert is_valid_get_all_the_custom_issue_definitions_based_on_the_given_filters(
            validator,
            get_all_the_custom_issue_definitions_based_on_the_given_filters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_total_custom_issue_definitions_count_based_on_the_provided_filters(json_schema_validate, obj):
    json_schema_validate('jsd_9ae1668865945349b9dcef2d60b7ba03_v2_3_7_6').validate(obj)
    return True


def get_the_total_custom_issue_definitions_count_based_on_the_provided_filters(api):
    endpoint_result = api.issues.get_the_total_custom_issue_definitions_count_based_on_the_provided_filters(
        facility='string',
        id='string',
        is_enabled=True,
        mnemonic='string',
        name='string',
        priority='string',
        profile_id='string',
        severity=0
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_total_custom_issue_definitions_count_based_on_the_provided_filters(api, validator):
    try:
        assert is_valid_get_the_total_custom_issue_definitions_count_based_on_the_provided_filters(
            validator,
            get_the_total_custom_issue_definitions_count_based_on_the_provided_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_total_custom_issue_definitions_count_based_on_the_provided_filters_default_val(api):
    endpoint_result = api.issues.get_the_total_custom_issue_definitions_count_based_on_the_provided_filters(
        facility=None,
        id=None,
        is_enabled=None,
        mnemonic=None,
        name=None,
        priority=None,
        profile_id=None,
        severity=None
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_total_custom_issue_definitions_count_based_on_the_provided_filters_default_val(api, validator):
    try:
        assert is_valid_get_the_total_custom_issue_definitions_count_based_on_the_provided_filters(
            validator,
            get_the_total_custom_issue_definitions_count_based_on_the_provided_filters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_an_existing_custom_issue_definition_based_on_the_provided_id(json_schema_validate, obj):
    json_schema_validate('jsd_5559c0204c665262a712caef988d7d88_v2_3_7_6').validate(obj)
    return True


def updates_an_existing_custom_issue_definition_based_on_the_provided_id(api):
    endpoint_result = api.issues.updates_an_existing_custom_issue_definition_based_on_the_provided_id(
        active_validation=True,
        description='string',
        id='string',
        isEnabled=True,
        isNotificationEnabled=True,
        name='string',
        payload=None,
        priority='string',
        rules=[{'severity': 0, 'facility': 'string', 'mnemonic': 'string', 'pattern': 'string', 'occurrences': 0, 'durationInMinutes': 0}]
    )
    return endpoint_result


@pytest.mark.issues
def test_updates_an_existing_custom_issue_definition_based_on_the_provided_id(api, validator):
    try:
        assert is_valid_updates_an_existing_custom_issue_definition_based_on_the_provided_id(
            validator,
            updates_an_existing_custom_issue_definition_based_on_the_provided_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_an_existing_custom_issue_definition_based_on_the_provided_id_default_val(api):
    endpoint_result = api.issues.updates_an_existing_custom_issue_definition_based_on_the_provided_id(
        active_validation=True,
        description=None,
        id='string',
        isEnabled=None,
        isNotificationEnabled=None,
        name=None,
        payload=None,
        priority=None,
        rules=None
    )
    return endpoint_result


@pytest.mark.issues
def test_updates_an_existing_custom_issue_definition_based_on_the_provided_id_default_val(api, validator):
    try:
        assert is_valid_updates_an_existing_custom_issue_definition_based_on_the_provided_id(
            validator,
            updates_an_existing_custom_issue_definition_based_on_the_provided_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_an_existing_custom_issue_definition(json_schema_validate, obj):
    json_schema_validate('jsd_f5ace826dd39514dbb0e0dde0599c1f5_v2_3_7_6').validate(obj)
    return True


def deletes_an_existing_custom_issue_definition(api):
    endpoint_result = api.issues.deletes_an_existing_custom_issue_definition(
        id='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_deletes_an_existing_custom_issue_definition(api, validator):
    try:
        assert is_valid_deletes_an_existing_custom_issue_definition(
            validator,
            deletes_an_existing_custom_issue_definition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_an_existing_custom_issue_definition_default_val(api):
    endpoint_result = api.issues.deletes_an_existing_custom_issue_definition(
        id='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_deletes_an_existing_custom_issue_definition_default_val(api, validator):
    try:
        assert is_valid_deletes_an_existing_custom_issue_definition(
            validator,
            deletes_an_existing_custom_issue_definition_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_execute_suggested_actions_commands(json_schema_validate, obj):
    json_schema_validate('jsd_915745bc55e6552fac58cc0aaacd773a_v2_3_7_6').validate(obj)
    return True


def execute_suggested_actions_commands(api):
    endpoint_result = api.issues.execute_suggested_actions_commands(
        active_validation=True,
        entity_type='string',
        entity_value='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.issues
def test_execute_suggested_actions_commands(api, validator):
    try:
        assert is_valid_execute_suggested_actions_commands(
            validator,
            execute_suggested_actions_commands(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def execute_suggested_actions_commands_default_val(api):
    endpoint_result = api.issues.execute_suggested_actions_commands(
        active_validation=True,
        entity_type=None,
        entity_value=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.issues
def test_execute_suggested_actions_commands_default_val(api, validator):
    try:
        assert is_valid_execute_suggested_actions_commands(
            validator,
            execute_suggested_actions_commands_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_issue_enrichment_details(json_schema_validate, obj):
    json_schema_validate('jsd_02f2f039811951c0af53e3381ae91225_v2_3_7_6').validate(obj)
    return True


def get_issue_enrichment_details(api):
    endpoint_result = api.issues.get_issue_enrichment_details(

    )
    return endpoint_result


@pytest.mark.issues
def test_get_issue_enrichment_details(api, validator):
    try:
        assert is_valid_get_issue_enrichment_details(
            validator,
            get_issue_enrichment_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_issue_enrichment_details_default_val(api):
    endpoint_result = api.issues.get_issue_enrichment_details(

    )
    return endpoint_result


@pytest.mark.issues
def test_get_issue_enrichment_details_default_val(api, validator):
    try:
        assert is_valid_get_issue_enrichment_details(
            validator,
            get_issue_enrichment_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_issues(json_schema_validate, obj):
    json_schema_validate('jsd_759522aaef3b519ba8b9fb2cbf43b985_v2_3_7_6').validate(obj)
    return True


def issues(api):
    endpoint_result = api.issues.issues(
        ai_driven='string',
        device_id='string',
        end_time=0,
        issue_status='string',
        mac_address='string',
        priority='string',
        site_id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.issues
def test_issues(api, validator):
    try:
        assert is_valid_issues(
            validator,
            issues(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def issues_default_val(api):
    endpoint_result = api.issues.issues(
        ai_driven=None,
        device_id=None,
        end_time=None,
        issue_status=None,
        mac_address=None,
        priority=None,
        site_id=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.issues
def test_issues_default_val(api, validator):
    try:
        assert is_valid_issues(
            validator,
            issues_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_returns_all_issue_trigger_definitions_for_given_filters(json_schema_validate, obj):
    json_schema_validate('jsd_d97f6433e45a53d2a56a958ba83faab5_v2_3_7_6').validate(obj)
    return True


def returns_all_issue_trigger_definitions_for_given_filters(api):
    endpoint_result = api.issues.returns_all_issue_trigger_definitions_for_given_filters(
        attribute='string',
        device_type='string',
        id='string',
        issue_enabled=True,
        limit=0,
        name='string',
        offset=0,
        order='string',
        priority='string',
        profile_id='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_returns_all_issue_trigger_definitions_for_given_filters(api, validator):
    try:
        assert is_valid_returns_all_issue_trigger_definitions_for_given_filters(
            validator,
            returns_all_issue_trigger_definitions_for_given_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def returns_all_issue_trigger_definitions_for_given_filters_default_val(api):
    endpoint_result = api.issues.returns_all_issue_trigger_definitions_for_given_filters(
        attribute=None,
        device_type=None,
        id=None,
        issue_enabled=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        priority=None,
        profile_id=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.issues
def test_returns_all_issue_trigger_definitions_for_given_filters_default_val(api, validator):
    try:
        assert is_valid_returns_all_issue_trigger_definitions_for_given_filters(
            validator,
            returns_all_issue_trigger_definitions_for_given_filters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_count_of_system_defined_issue_definitions_based_on_provided_filters(json_schema_validate, obj):
    json_schema_validate('jsd_0cdb71530b2359e2bcb1e212aad71b6d_v2_3_7_6').validate(obj)
    return True


def get_the_count_of_system_defined_issue_definitions_based_on_provided_filters(api):
    endpoint_result = api.issues.get_the_count_of_system_defined_issue_definitions_based_on_provided_filters(
        device_type='string',
        id='string',
        issue_enabled=True,
        name='string',
        priority='string',
        profile_id='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_count_of_system_defined_issue_definitions_based_on_provided_filters(api, validator):
    try:
        assert is_valid_get_the_count_of_system_defined_issue_definitions_based_on_provided_filters(
            validator,
            get_the_count_of_system_defined_issue_definitions_based_on_provided_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_count_of_system_defined_issue_definitions_based_on_provided_filters_default_val(api):
    endpoint_result = api.issues.get_the_count_of_system_defined_issue_definitions_based_on_provided_filters(
        device_type=None,
        id=None,
        issue_enabled=None,
        name=None,
        priority=None,
        profile_id=None
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_count_of_system_defined_issue_definitions_based_on_provided_filters_default_val(api, validator):
    try:
        assert is_valid_get_the_count_of_system_defined_issue_definitions_based_on_provided_filters(
            validator,
            get_the_count_of_system_defined_issue_definitions_based_on_provided_filters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_issue_trigger_definition_for_given_id(json_schema_validate, obj):
    json_schema_validate('jsd_cccbb5d35c9c5be9b837a0c1a33cbff8_v2_3_7_6').validate(obj)
    return True


def get_issue_trigger_definition_for_given_id(api):
    endpoint_result = api.issues.get_issue_trigger_definition_for_given_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_get_issue_trigger_definition_for_given_id(api, validator):
    try:
        assert is_valid_get_issue_trigger_definition_for_given_id(
            validator,
            get_issue_trigger_definition_for_given_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_issue_trigger_definition_for_given_id_default_val(api):
    endpoint_result = api.issues.get_issue_trigger_definition_for_given_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_get_issue_trigger_definition_for_given_id_default_val(api, validator):
    try:
        assert is_valid_get_issue_trigger_definition_for_given_id(
            validator,
            get_issue_trigger_definition_for_given_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_issue_trigger_definition_update(json_schema_validate, obj):
    json_schema_validate('jsd_3f25c825ca6e58a5b1c2294b11558e7b_v2_3_7_6').validate(obj)
    return True


def issue_trigger_definition_update(api):
    endpoint_result = api.issues.issue_trigger_definition_update(
        active_validation=True,
        id='string',
        issueEnabled=True,
        payload=None,
        priority='string',
        synchronizeToHealthThreshold=True,
        thresholdValue=0
    )
    return endpoint_result


@pytest.mark.issues
def test_issue_trigger_definition_update(api, validator):
    try:
        assert is_valid_issue_trigger_definition_update(
            validator,
            issue_trigger_definition_update(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def issue_trigger_definition_update_default_val(api):
    endpoint_result = api.issues.issue_trigger_definition_update(
        active_validation=True,
        id='string',
        issueEnabled=None,
        payload=None,
        priority=None,
        synchronizeToHealthThreshold=None,
        thresholdValue=None
    )
    return endpoint_result


@pytest.mark.issues
def test_issue_trigger_definition_update_default_val(api, validator):
    try:
        assert is_valid_issue_trigger_definition_update(
            validator,
            issue_trigger_definition_update_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_custom_issue_definition_for_the_given_custom_issue_definition_id(json_schema_validate, obj):
    json_schema_validate('jsd_32a2d089359a5a9899444a01a727453a_v2_3_7_6').validate(obj)
    return True


def get_the_custom_issue_definition_for_the_given_custom_issue_definition_id(api):
    endpoint_result = api.issues.get_the_custom_issue_definition_for_the_given_custom_issue_definition_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_custom_issue_definition_for_the_given_custom_issue_definition_id(api, validator):
    try:
        assert is_valid_get_the_custom_issue_definition_for_the_given_custom_issue_definition_id(
            validator,
            get_the_custom_issue_definition_for_the_given_custom_issue_definition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_custom_issue_definition_for_the_given_custom_issue_definition_id_default_val(api):
    endpoint_result = api.issues.get_the_custom_issue_definition_for_the_given_custom_issue_definition_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.issues
def test_get_the_custom_issue_definition_for_the_given_custom_issue_definition_id_default_val(api, validator):
    try:
        assert is_valid_get_the_custom_issue_definition_for_the_given_custom_issue_definition_id(
            validator,
            get_the_custom_issue_definition_for_the_given_custom_issue_definition_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

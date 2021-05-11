# -*- coding: utf-8 -*-
"""DNACenterAPI reports API fixtures and tests.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.1', reason='version does not match')


def is_valid_get_views_for_a_given_view_group(json_schema_validate, obj):
    json_schema_validate('jsd_03b6aa2b4ddaa555_v2_2_1').validate(obj)
    return True


def get_views_for_a_given_view_group(api):
    endpoint_result = api.reports.get_views_for_a_given_view_group(
        view_group_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_views_for_a_given_view_group(api, validator):
    assert is_valid_get_views_for_a_given_view_group(
        validator,
        get_views_for_a_given_view_group(api)
    )


def get_views_for_a_given_view_group_default(api):
    endpoint_result = api.reports.get_views_for_a_given_view_group(
        view_group_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_views_for_a_given_view_group_default(api, validator):
    try:
        assert is_valid_get_views_for_a_given_view_group(
            validator,
            get_views_for_a_given_view_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_view_details_for_a_given_view_group_and_view(json_schema_validate, obj):
    json_schema_validate('jsd_1d9aba2f4f89ae51_v2_2_1').validate(obj)
    return True


def get_view_details_for_a_given_view_group_and_view(api):
    endpoint_result = api.reports.get_view_details_for_a_given_view_group_and_view(
        view_group_id='string',
        view_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_view_details_for_a_given_view_group_and_view(api, validator):
    assert is_valid_get_view_details_for_a_given_view_group_and_view(
        validator,
        get_view_details_for_a_given_view_group_and_view(api)
    )


def get_view_details_for_a_given_view_group_and_view_default(api):
    endpoint_result = api.reports.get_view_details_for_a_given_view_group_and_view(
        view_group_id='string',
        view_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_view_details_for_a_given_view_group_and_view_default(api, validator):
    try:
        assert is_valid_get_view_details_for_a_given_view_group_and_view(
            validator,
            get_view_details_for_a_given_view_group_and_view_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_a_scheduled_report(json_schema_validate, obj):
    json_schema_validate('jsd_239c69214f9bb12e_v2_2_1').validate(obj)
    return True


def delete_a_scheduled_report(api):
    endpoint_result = api.reports.delete_a_scheduled_report(
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_delete_a_scheduled_report(api, validator):
    assert is_valid_delete_a_scheduled_report(
        validator,
        delete_a_scheduled_report(api)
    )


def delete_a_scheduled_report_default(api):
    endpoint_result = api.reports.delete_a_scheduled_report(
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_delete_a_scheduled_report_default(api, validator):
    try:
        assert is_valid_delete_a_scheduled_report(
            validator,
            delete_a_scheduled_report_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_all_view_groups(json_schema_validate, obj):
    json_schema_validate('jsd_2f904a3544abb1c9_v2_2_1').validate(obj)
    return True


def get_all_view_groups(api):
    endpoint_result = api.reports.get_all_view_groups(

    )
    return endpoint_result


@pytest.mark.reports
def test_get_all_view_groups(api, validator):
    assert is_valid_get_all_view_groups(
        validator,
        get_all_view_groups(api)
    )


def get_all_view_groups_default(api):
    endpoint_result = api.reports.get_all_view_groups(

    )
    return endpoint_result


@pytest.mark.reports
def test_get_all_view_groups_default(api, validator):
    try:
        assert is_valid_get_all_view_groups(
            validator,
            get_all_view_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_list_of_scheduled_reports(json_schema_validate, obj):
    json_schema_validate('jsd_2ab4b80d49caae42_v2_2_1').validate(obj)
    return True


def get_list_of_scheduled_reports(api):
    endpoint_result = api.reports.get_list_of_scheduled_reports(
        view_group_id='string',
        view_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_list_of_scheduled_reports(api, validator):
    assert is_valid_get_list_of_scheduled_reports(
        validator,
        get_list_of_scheduled_reports(api)
    )


def get_list_of_scheduled_reports_default(api):
    endpoint_result = api.reports.get_list_of_scheduled_reports(
        view_group_id=None,
        view_id=None
    )
    return endpoint_result


@pytest.mark.reports
def test_get_list_of_scheduled_reports_default(api, validator):
    try:
        assert is_valid_get_list_of_scheduled_reports(
            validator,
            get_list_of_scheduled_reports_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_or_schedule_a_report(json_schema_validate, obj):
    json_schema_validate('jsd_8abf291a42aa8860_v2_2_1').validate(obj)
    return True


def create_or_schedule_a_report(api):
    endpoint_result = api.reports.create_or_schedule_a_report(
        active_validation=True,
        deliveries=[{}],
        name='string',
        payload=None,
        schedule='string',
        tags=['string'],
        view={'fieldGroups': [{'fieldGroupDisplayName': 'string', 'fieldGroupName': 'string', 'fields': [{'displayName': 'string', 'name': 'string'}]}], 'filters': [{'displayName': 'string', 'name': 'string', 'type': 'string', 'value': {}}], 'format': {'formatType': 'string', 'name': 'string'}, 'name': 'string', 'viewId': 'string'},
        viewGroupId='string',
        viewGroupVersion='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_create_or_schedule_a_report(api, validator):
    assert is_valid_create_or_schedule_a_report(
        validator,
        create_or_schedule_a_report(api)
    )


def create_or_schedule_a_report_default(api):
    endpoint_result = api.reports.create_or_schedule_a_report(
        active_validation=True,
        deliveries=None,
        name=None,
        payload=None,
        schedule=None,
        tags=None,
        view=None,
        viewGroupId=None,
        viewGroupVersion=None
    )
    return endpoint_result


@pytest.mark.reports
def test_create_or_schedule_a_report_default(api, validator):
    try:
        assert is_valid_create_or_schedule_a_report(
            validator,
            create_or_schedule_a_report_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_all_execution_details_for_a_given_report(json_schema_validate, obj):
    json_schema_validate('jsd_91b9d8304679a273_v2_2_1').validate(obj)
    return True


def get_all_execution_details_for_a_given_report(api):
    endpoint_result = api.reports.get_all_execution_details_for_a_given_report(
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_all_execution_details_for_a_given_report(api, validator):
    assert is_valid_get_all_execution_details_for_a_given_report(
        validator,
        get_all_execution_details_for_a_given_report(api)
    )


def get_all_execution_details_for_a_given_report_default(api):
    endpoint_result = api.reports.get_all_execution_details_for_a_given_report(
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_all_execution_details_for_a_given_report_default(api, validator):
    try:
        assert is_valid_get_all_execution_details_for_a_given_report(
            validator,
            get_all_execution_details_for_a_given_report_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_a_scheduled_report(json_schema_validate, obj):
    json_schema_validate('jsd_b79a39104e189251_v2_2_1').validate(obj)
    return True


def get_a_scheduled_report(api):
    endpoint_result = api.reports.get_a_scheduled_report(
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_a_scheduled_report(api, validator):
    assert is_valid_get_a_scheduled_report(
        validator,
        get_a_scheduled_report(api)
    )


def get_a_scheduled_report_default(api):
    endpoint_result = api.reports.get_a_scheduled_report(
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_a_scheduled_report_default(api, validator):
    try:
        assert is_valid_get_a_scheduled_report(
            validator,
            get_a_scheduled_report_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_download_report_content(json_schema_validate, obj):
    json_schema_validate('jsd_d6bbebd74a4887bd_v2_2_1').validate(obj)
    return True


def download_report_content(api):
    endpoint_result = api.reports.download_report_content(
        execution_id='string',
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_download_report_content(api, validator):
    assert is_valid_download_report_content(
        validator,
        download_report_content(api)
    )


def download_report_content_default(api):
    endpoint_result = api.reports.download_report_content(
        execution_id='string',
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_download_report_content_default(api, validator):
    try:
        assert is_valid_download_report_content(
            validator,
            download_report_content_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

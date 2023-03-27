# -*- coding: utf-8 -*-
"""DNACenterAPI reports API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.5.3', reason='version does not match')


def is_valid_create_or_schedule_a_report(json_schema_validate, obj):
    json_schema_validate('jsd_220fa310ab095148bdb00d7d3d5e1676_v2_3_5_3').validate(obj)
    return True


def create_or_schedule_a_report(api):
    endpoint_result = api.reports.create_or_schedule_a_report(
        active_validation=True,
        deliveries=[{}],
        name='string',
        payload=None,
        schedule={},
        tags=['string'],
        view={'fieldGroups': [{'fieldGroupDisplayName': 'string', 'fieldGroupName': 'string', 'fields': [{'displayName': 'string', 'name': 'string'}]}], 'filters': [{'displayName': 'string', 'name': 'string', 'type': 'string', 'value': {}}], 'format': {'formatType': 'string', 'name': 'string'}, 'name': 'string', 'viewId': 'string'},
        viewGroupId='string',
        viewGroupVersion='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_create_or_schedule_a_report(api, validator):
    try:
        assert is_valid_create_or_schedule_a_report(
            validator,
            create_or_schedule_a_report(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_or_schedule_a_report_default_val(api):
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
def test_create_or_schedule_a_report_default_val(api, validator):
    try:
        assert is_valid_create_or_schedule_a_report(
            validator,
            create_or_schedule_a_report_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_list_of_scheduled_reports(json_schema_validate, obj):
    json_schema_validate('jsd_095d89e1c3e150ef9faaff44fa483de5_v2_3_5_3').validate(obj)
    return True


def get_list_of_scheduled_reports(api):
    endpoint_result = api.reports.get_list_of_scheduled_reports(
        view_group_id='string',
        view_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_list_of_scheduled_reports(api, validator):
    try:
        assert is_valid_get_list_of_scheduled_reports(
            validator,
            get_list_of_scheduled_reports(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_list_of_scheduled_reports_default_val(api):
    endpoint_result = api.reports.get_list_of_scheduled_reports(
        view_group_id=None,
        view_id=None
    )
    return endpoint_result


@pytest.mark.reports
def test_get_list_of_scheduled_reports_default_val(api, validator):
    try:
        assert is_valid_get_list_of_scheduled_reports(
            validator,
            get_list_of_scheduled_reports_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_a_scheduled_report(json_schema_validate, obj):
    json_schema_validate('jsd_76f9cb7c424b5502b4ad54ccbb1ca4f4_v2_3_5_3').validate(obj)
    return True


def get_a_scheduled_report(api):
    endpoint_result = api.reports.get_a_scheduled_report(
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_a_scheduled_report(api, validator):
    try:
        assert is_valid_get_a_scheduled_report(
            validator,
            get_a_scheduled_report(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_a_scheduled_report_default_val(api):
    endpoint_result = api.reports.get_a_scheduled_report(
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_a_scheduled_report_default_val(api, validator):
    try:
        assert is_valid_get_a_scheduled_report(
            validator,
            get_a_scheduled_report_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_scheduled_report(json_schema_validate, obj):
    json_schema_validate('jsd_8a6a151b68d450dfaf1e8a92e0f5cc68_v2_3_5_3').validate(obj)
    return True


def delete_a_scheduled_report(api):
    endpoint_result = api.reports.delete_a_scheduled_report(
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_delete_a_scheduled_report(api, validator):
    try:
        assert is_valid_delete_a_scheduled_report(
            validator,
            delete_a_scheduled_report(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_scheduled_report_default_val(api):
    endpoint_result = api.reports.delete_a_scheduled_report(
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_delete_a_scheduled_report_default_val(api, validator):
    try:
        assert is_valid_delete_a_scheduled_report(
            validator,
            delete_a_scheduled_report_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_execution_details_for_a_given_report(json_schema_validate, obj):
    json_schema_validate('jsd_a4b1ca0320185570bc12da238f0e88bb_v2_3_5_3').validate(obj)
    return True


def get_all_execution_details_for_a_given_report(api):
    endpoint_result = api.reports.get_all_execution_details_for_a_given_report(
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_all_execution_details_for_a_given_report(api, validator):
    try:
        assert is_valid_get_all_execution_details_for_a_given_report(
            validator,
            get_all_execution_details_for_a_given_report(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_execution_details_for_a_given_report_default_val(api):
    endpoint_result = api.reports.get_all_execution_details_for_a_given_report(
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_all_execution_details_for_a_given_report_default_val(api, validator):
    try:
        assert is_valid_get_all_execution_details_for_a_given_report(
            validator,
            get_all_execution_details_for_a_given_report_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_download_report_content(json_schema_validate, obj):
    json_schema_validate('jsd_2921b2790cdb5abf98c8e00011de86a4_v2_3_5_3').validate(obj)
    return True


def download_report_content(api):
    endpoint_result = api.reports.download_report_content(
        dirpath=None,
        save_file=None,
        filename=None,
        execution_id='string',
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_download_report_content(api, validator):
    try:
        assert is_valid_download_report_content(
            validator,
            download_report_content(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def download_report_content_default_val(api):
    endpoint_result = api.reports.download_report_content(
        dirpath=None,
        save_file=None,
        filename=None,
        execution_id='string',
        report_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_download_report_content_default_val(api, validator):
    try:
        assert is_valid_download_report_content(
            validator,
            download_report_content_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_view_groups(json_schema_validate, obj):
    json_schema_validate('jsd_bbff833d5d5756698f4764a9d488cc98_v2_3_5_3').validate(obj)
    return True


def get_all_view_groups(api):
    endpoint_result = api.reports.get_all_view_groups(

    )
    return endpoint_result


@pytest.mark.reports
def test_get_all_view_groups(api, validator):
    try:
        assert is_valid_get_all_view_groups(
            validator,
            get_all_view_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_view_groups_default_val(api):
    endpoint_result = api.reports.get_all_view_groups(

    )
    return endpoint_result


@pytest.mark.reports
def test_get_all_view_groups_default_val(api, validator):
    try:
        assert is_valid_get_all_view_groups(
            validator,
            get_all_view_groups_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_views_for_a_given_view_group(json_schema_validate, obj):
    json_schema_validate('jsd_c5879612ddc05cd0a0de09d29da4907e_v2_3_5_3').validate(obj)
    return True


def get_views_for_a_given_view_group(api):
    endpoint_result = api.reports.get_views_for_a_given_view_group(
        view_group_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_views_for_a_given_view_group(api, validator):
    try:
        assert is_valid_get_views_for_a_given_view_group(
            validator,
            get_views_for_a_given_view_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_views_for_a_given_view_group_default_val(api):
    endpoint_result = api.reports.get_views_for_a_given_view_group(
        view_group_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_views_for_a_given_view_group_default_val(api, validator):
    try:
        assert is_valid_get_views_for_a_given_view_group(
            validator,
            get_views_for_a_given_view_group_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_view_details_for_a_given_view_group_and_view(json_schema_validate, obj):
    json_schema_validate('jsd_3d1944177c95598ebd1986582dc8069a_v2_3_5_3').validate(obj)
    return True


def get_view_details_for_a_given_view_group_and_view(api):
    endpoint_result = api.reports.get_view_details_for_a_given_view_group_and_view(
        view_group_id='string',
        view_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_view_details_for_a_given_view_group_and_view(api, validator):
    try:
        assert is_valid_get_view_details_for_a_given_view_group_and_view(
            validator,
            get_view_details_for_a_given_view_group_and_view(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_view_details_for_a_given_view_group_and_view_default_val(api):
    endpoint_result = api.reports.get_view_details_for_a_given_view_group_and_view(
        view_group_id='string',
        view_id='string'
    )
    return endpoint_result


@pytest.mark.reports
def test_get_view_details_for_a_given_view_group_and_view_default_val(api, validator):
    try:
        assert is_valid_get_view_details_for_a_given_view_group_and_view(
            validator,
            get_view_details_for_a_given_view_group_and_view_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

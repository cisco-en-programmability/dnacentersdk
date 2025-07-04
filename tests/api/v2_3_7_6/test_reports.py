# -*- coding: utf-8 -*-
"""DNACenterAPI reports API fixtures and tests.

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
    DNA_CENTER_VERSION != "2.3.7.6", reason="version does not match"
)


def is_valid_download_flexible_report_v1(json_schema_validate, obj):
    json_schema_validate("jsd_fc4acf45953f5b68be682c3c5906bf14_v2_3_7_6").validate(obj)
    return True


def download_flexible_report_v1(api):
    endpoint_result = api.reports.download_flexible_report_v1(
        execution_id="string", report_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_download_flexible_report_v1(api, validator):
    try:
        assert is_valid_download_flexible_report_v1(
            validator, download_flexible_report_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def download_flexible_report_v1_default_val(api):
    endpoint_result = api.reports.download_flexible_report_v1(
        execution_id="string", report_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_download_flexible_report_v1_default_val(api, validator):
    try:
        assert is_valid_download_flexible_report_v1(
            validator, download_flexible_report_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_executing_the_flexible_report_v1(json_schema_validate, obj):
    json_schema_validate("jsd_3156737c2c0c5f9fa208985865f05eca_v2_3_7_6").validate(obj)
    return True


def executing_the_flexible_report_v1(api):
    endpoint_result = api.reports.executing_the_flexible_report_v1(
        active_validation=True, payload=None, report_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_executing_the_flexible_report_v1(api, validator):
    try:
        assert is_valid_executing_the_flexible_report_v1(
            validator, executing_the_flexible_report_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def executing_the_flexible_report_v1_default_val(api):
    endpoint_result = api.reports.executing_the_flexible_report_v1(
        active_validation=True, payload=None, report_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_executing_the_flexible_report_v1_default_val(api, validator):
    try:
        assert is_valid_executing_the_flexible_report_v1(
            validator, executing_the_flexible_report_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_execution_id_by_report_id_v1(json_schema_validate, obj):
    json_schema_validate("jsd_458edf3c4d58586fb15a5b62256f94a6_v2_3_7_6").validate(obj)
    return True


def get_execution_id_by_report_id_v1(api):
    endpoint_result = api.reports.get_execution_id_by_report_id_v1(report_id="string")
    return endpoint_result


@pytest.mark.reports
def test_get_execution_id_by_report_id_v1(api, validator):
    try:
        assert is_valid_get_execution_id_by_report_id_v1(
            validator, get_execution_id_by_report_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_execution_id_by_report_id_v1_default_val(api):
    endpoint_result = api.reports.get_execution_id_by_report_id_v1(report_id="string")
    return endpoint_result


@pytest.mark.reports
def test_get_execution_id_by_report_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_execution_id_by_report_id_v1(
            validator, get_execution_id_by_report_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_schedule_of_flexible_report_v1(json_schema_validate, obj):
    json_schema_validate("jsd_a93d01238de0537dbb3d358f9cce0bd2_v2_3_7_6").validate(obj)
    return True


def update_schedule_of_flexible_report_v1(api):
    endpoint_result = api.reports.update_schedule_of_flexible_report_v1(
        active_validation=True, payload=None, report_id="string", schedule={}
    )
    return endpoint_result


@pytest.mark.reports
def test_update_schedule_of_flexible_report_v1(api, validator):
    try:
        assert is_valid_update_schedule_of_flexible_report_v1(
            validator, update_schedule_of_flexible_report_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_schedule_of_flexible_report_v1_default_val(api):
    endpoint_result = api.reports.update_schedule_of_flexible_report_v1(
        active_validation=True, payload=None, report_id="string", schedule=None
    )
    return endpoint_result


@pytest.mark.reports
def test_update_schedule_of_flexible_report_v1_default_val(api, validator):
    try:
        assert is_valid_update_schedule_of_flexible_report_v1(
            validator, update_schedule_of_flexible_report_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_flexible_report_schedule_by_report_id_v1(json_schema_validate, obj):
    json_schema_validate("jsd_a2a4b5bdcace5b55a5962ae85ff59d87_v2_3_7_6").validate(obj)
    return True


def get_flexible_report_schedule_by_report_id_v1(api):
    endpoint_result = api.reports.get_flexible_report_schedule_by_report_id_v1(
        report_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_get_flexible_report_schedule_by_report_id_v1(api, validator):
    try:
        assert is_valid_get_flexible_report_schedule_by_report_id_v1(
            validator, get_flexible_report_schedule_by_report_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_flexible_report_schedule_by_report_id_v1_default_val(api):
    endpoint_result = api.reports.get_flexible_report_schedule_by_report_id_v1(
        report_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_get_flexible_report_schedule_by_report_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_flexible_report_schedule_by_report_id_v1(
            validator, get_flexible_report_schedule_by_report_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_flexible_report_schedules_v1(json_schema_validate, obj):
    json_schema_validate("jsd_6dfd5cfd8a985505aaa606be4599319f_v2_3_7_6").validate(obj)
    return True


def get_all_flexible_report_schedules_v1(api):
    endpoint_result = api.reports.get_all_flexible_report_schedules_v1()
    return endpoint_result


@pytest.mark.reports
def test_get_all_flexible_report_schedules_v1(api, validator):
    try:
        assert is_valid_get_all_flexible_report_schedules_v1(
            validator, get_all_flexible_report_schedules_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_flexible_report_schedules_v1_default_val(api):
    endpoint_result = api.reports.get_all_flexible_report_schedules_v1()
    return endpoint_result


@pytest.mark.reports
def test_get_all_flexible_report_schedules_v1_default_val(api, validator):
    try:
        assert is_valid_get_all_flexible_report_schedules_v1(
            validator, get_all_flexible_report_schedules_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_or_schedule_a_report_v1(json_schema_validate, obj):
    json_schema_validate("jsd_220fa310ab095148bdb00d7d3d5e1676_v2_3_7_6").validate(obj)
    return True


def create_or_schedule_a_report_v1(api):
    endpoint_result = api.reports.create_or_schedule_a_report_v1(
        active_validation=True,
        dataCategory="string",
        deliveries=[{}],
        name="string",
        payload=None,
        schedule={},
        tags=["string"],
        view={
            "fieldGroups": [
                {
                    "fieldGroupDisplayName": "string",
                    "fieldGroupName": "string",
                    "fields": [{"displayName": "string", "name": "string"}],
                }
            ],
            "filters": [
                {
                    "displayName": "string",
                    "name": "string",
                    "type": "string",
                    "value": {},
                }
            ],
            "format": {"formatType": "string", "name": "string"},
            "name": "string",
            "viewId": "string",
        },
        viewGroupId="string",
        viewGroupVersion="string",
    )
    return endpoint_result


@pytest.mark.reports
def test_create_or_schedule_a_report_v1(api, validator):
    try:
        assert is_valid_create_or_schedule_a_report_v1(
            validator, create_or_schedule_a_report_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_or_schedule_a_report_v1_default_val(api):
    endpoint_result = api.reports.create_or_schedule_a_report_v1(
        active_validation=True,
        dataCategory=None,
        deliveries=None,
        name=None,
        payload=None,
        schedule=None,
        tags=None,
        view=None,
        viewGroupId=None,
        viewGroupVersion=None,
    )
    return endpoint_result


@pytest.mark.reports
def test_create_or_schedule_a_report_v1_default_val(api, validator):
    try:
        assert is_valid_create_or_schedule_a_report_v1(
            validator, create_or_schedule_a_report_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_list_of_scheduled_reports_v1(json_schema_validate, obj):
    json_schema_validate("jsd_095d89e1c3e150ef9faaff44fa483de5_v2_3_7_6").validate(obj)
    return True


def get_list_of_scheduled_reports_v1(api):
    endpoint_result = api.reports.get_list_of_scheduled_reports_v1(
        view_group_id="string", view_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_get_list_of_scheduled_reports_v1(api, validator):
    try:
        assert is_valid_get_list_of_scheduled_reports_v1(
            validator, get_list_of_scheduled_reports_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_list_of_scheduled_reports_v1_default_val(api):
    endpoint_result = api.reports.get_list_of_scheduled_reports_v1(
        view_group_id=None, view_id=None
    )
    return endpoint_result


@pytest.mark.reports
def test_get_list_of_scheduled_reports_v1_default_val(api, validator):
    try:
        assert is_valid_get_list_of_scheduled_reports_v1(
            validator, get_list_of_scheduled_reports_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_a_scheduled_report_v1(json_schema_validate, obj):
    json_schema_validate("jsd_76f9cb7c424b5502b4ad54ccbb1ca4f4_v2_3_7_6").validate(obj)
    return True


def get_a_scheduled_report_v1(api):
    endpoint_result = api.reports.get_a_scheduled_report_v1(report_id="string")
    return endpoint_result


@pytest.mark.reports
def test_get_a_scheduled_report_v1(api, validator):
    try:
        assert is_valid_get_a_scheduled_report_v1(
            validator, get_a_scheduled_report_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_a_scheduled_report_v1_default_val(api):
    endpoint_result = api.reports.get_a_scheduled_report_v1(report_id="string")
    return endpoint_result


@pytest.mark.reports
def test_get_a_scheduled_report_v1_default_val(api, validator):
    try:
        assert is_valid_get_a_scheduled_report_v1(
            validator, get_a_scheduled_report_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_scheduled_report_v1(json_schema_validate, obj):
    json_schema_validate("jsd_8a6a151b68d450dfaf1e8a92e0f5cc68_v2_3_7_6").validate(obj)
    return True


def delete_a_scheduled_report_v1(api):
    endpoint_result = api.reports.delete_a_scheduled_report_v1(report_id="string")
    return endpoint_result


@pytest.mark.reports
def test_delete_a_scheduled_report_v1(api, validator):
    try:
        assert is_valid_delete_a_scheduled_report_v1(
            validator, delete_a_scheduled_report_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_scheduled_report_v1_default_val(api):
    endpoint_result = api.reports.delete_a_scheduled_report_v1(report_id="string")
    return endpoint_result


@pytest.mark.reports
def test_delete_a_scheduled_report_v1_default_val(api, validator):
    try:
        assert is_valid_delete_a_scheduled_report_v1(
            validator, delete_a_scheduled_report_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_execution_details_for_a_given_report_v1(json_schema_validate, obj):
    json_schema_validate("jsd_a4b1ca0320185570bc12da238f0e88bb_v2_3_7_6").validate(obj)
    return True


def get_all_execution_details_for_a_given_report_v1(api):
    endpoint_result = api.reports.get_all_execution_details_for_a_given_report_v1(
        report_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_get_all_execution_details_for_a_given_report_v1(api, validator):
    try:
        assert is_valid_get_all_execution_details_for_a_given_report_v1(
            validator, get_all_execution_details_for_a_given_report_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_execution_details_for_a_given_report_v1_default_val(api):
    endpoint_result = api.reports.get_all_execution_details_for_a_given_report_v1(
        report_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_get_all_execution_details_for_a_given_report_v1_default_val(api, validator):
    try:
        assert is_valid_get_all_execution_details_for_a_given_report_v1(
            validator, get_all_execution_details_for_a_given_report_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_download_report_content_v1(json_schema_validate, obj):
    json_schema_validate("jsd_2921b2790cdb5abf98c8e00011de86a4_v2_3_7_6").validate(obj)
    return True


def download_report_content_v1(api):
    endpoint_result = api.reports.download_report_content_v1(
        execution_id="string", report_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_download_report_content_v1(api, validator):
    try:
        assert is_valid_download_report_content_v1(
            validator, download_report_content_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def download_report_content_v1_default_val(api):
    endpoint_result = api.reports.download_report_content_v1(
        execution_id="string", report_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_download_report_content_v1_default_val(api, validator):
    try:
        assert is_valid_download_report_content_v1(
            validator, download_report_content_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_view_groups_v1(json_schema_validate, obj):
    json_schema_validate("jsd_bbff833d5d5756698f4764a9d488cc98_v2_3_7_6").validate(obj)
    return True


def get_all_view_groups_v1(api):
    endpoint_result = api.reports.get_all_view_groups_v1()
    return endpoint_result


@pytest.mark.reports
def test_get_all_view_groups_v1(api, validator):
    try:
        assert is_valid_get_all_view_groups_v1(validator, get_all_view_groups_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_view_groups_v1_default_val(api):
    endpoint_result = api.reports.get_all_view_groups_v1()
    return endpoint_result


@pytest.mark.reports
def test_get_all_view_groups_v1_default_val(api, validator):
    try:
        assert is_valid_get_all_view_groups_v1(
            validator, get_all_view_groups_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_views_for_a_given_view_group_v1(json_schema_validate, obj):
    json_schema_validate("jsd_c5879612ddc05cd0a0de09d29da4907e_v2_3_7_6").validate(obj)
    return True


def get_views_for_a_given_view_group_v1(api):
    endpoint_result = api.reports.get_views_for_a_given_view_group_v1(
        view_group_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_get_views_for_a_given_view_group_v1(api, validator):
    try:
        assert is_valid_get_views_for_a_given_view_group_v1(
            validator, get_views_for_a_given_view_group_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_views_for_a_given_view_group_v1_default_val(api):
    endpoint_result = api.reports.get_views_for_a_given_view_group_v1(
        view_group_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_get_views_for_a_given_view_group_v1_default_val(api, validator):
    try:
        assert is_valid_get_views_for_a_given_view_group_v1(
            validator, get_views_for_a_given_view_group_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_view_details_for_a_given_view_group_and_view(
    json_schema_validate, obj
):
    json_schema_validate("jsd_3d1944177c95598ebd1986582dc8069a_v2_3_7_6").validate(obj)
    return True


def get_view_details_for_a_given_view_group_and_view(api):
    endpoint_result = api.reports.get_view_details_for_a_given_view_group_and_view(
        view_group_id="string", view_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_get_view_details_for_a_given_view_group_and_view(api, validator):
    try:
        assert is_valid_get_view_details_for_a_given_view_group_and_view(
            validator, get_view_details_for_a_given_view_group_and_view(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_view_details_for_a_given_view_group_and_view_default_val(api):
    endpoint_result = api.reports.get_view_details_for_a_given_view_group_and_view(
        view_group_id="string", view_id="string"
    )
    return endpoint_result


@pytest.mark.reports
def test_get_view_details_for_a_given_view_group_and_view_default_val(api, validator):
    try:
        assert is_valid_get_view_details_for_a_given_view_group_and_view(
            validator, get_view_details_for_a_given_view_group_and_view_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

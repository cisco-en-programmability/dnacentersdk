# -*- coding: utf-8 -*-
"""DNACenterAPI sites API fixtures and tests.

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


def is_valid_read_list_of_site_health_summaries_v1(json_schema_validate, obj):
    json_schema_validate("jsd_870b40b4f6d558bfbebcf8fcbc4df56b_v2_3_7_6").validate(obj)
    return True


def read_list_of_site_health_summaries_v1(api):
    endpoint_result = api.sites.read_list_of_site_health_summaries_v1(
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
def test_read_list_of_site_health_summaries_v1(api, validator):
    try:
        assert is_valid_read_list_of_site_health_summaries_v1(
            validator, read_list_of_site_health_summaries_v1(api)
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
        view=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_read_list_of_site_health_summaries_v1_default_val(api, validator):
    try:
        assert is_valid_read_list_of_site_health_summaries_v1(
            validator, read_list_of_site_health_summaries_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_site_count_v1(json_schema_validate, obj):
    json_schema_validate("jsd_e67558dd99925a0385f5f870bbb8f634_v2_3_7_6").validate(obj)
    return True


def read_site_count_v1(api):
    endpoint_result = api.sites.read_site_count_v1(
        end_time=0,
        id="string",
        site_hierarchy="string",
        site_hierarchy_id="string",
        site_type="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_read_site_count_v1(api, validator):
    try:
        assert is_valid_read_site_count_v1(validator, read_site_count_v1(api))
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
        site_type=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_read_site_count_v1_default_val(api, validator):
    try:
        assert is_valid_read_site_count_v1(
            validator, read_site_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_an_aggregated_summary_of_site_health_data_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_fc80b3e12ee9577a8e7fa5d4cd84e8fc_v2_3_7_6").validate(obj)
    return True


def read_an_aggregated_summary_of_site_health_data_v1(api):
    endpoint_result = api.sites.read_an_aggregated_summary_of_site_health_data_v1(
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
def test_read_an_aggregated_summary_of_site_health_data_v1(api, validator):
    try:
        assert is_valid_read_an_aggregated_summary_of_site_health_data_v1(
            validator, read_an_aggregated_summary_of_site_health_data_v1(api)
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
        view=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_read_an_aggregated_summary_of_site_health_data_v1_default_val(api, validator):
    try:
        assert is_valid_read_an_aggregated_summary_of_site_health_data_v1(
            validator,
            read_an_aggregated_summary_of_site_health_data_v1_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_an_aggregated_summary_of_site_health_data_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_8bec2dde673c5b2f940d0474fed32af6_v2_3_7_6").validate(obj)
    return True


def query_an_aggregated_summary_of_site_health_data_v1(api):
    endpoint_result = api.sites.query_an_aggregated_summary_of_site_health_data_v1(
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
def test_query_an_aggregated_summary_of_site_health_data_v1(api, validator):
    try:
        assert is_valid_query_an_aggregated_summary_of_site_health_data_v1(
            validator, query_an_aggregated_summary_of_site_health_data_v1(api)
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
        views=None,
    )
    return endpoint_result


@pytest.mark.sites
def test_query_an_aggregated_summary_of_site_health_data_v1_default_val(api, validator):
    try:
        assert is_valid_query_an_aggregated_summary_of_site_health_data_v1(
            validator,
            query_an_aggregated_summary_of_site_health_data_v1_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_read_site_health_summary_data_by_site_id_v1(json_schema_validate, obj):
    json_schema_validate("jsd_062572f214555abaa6a30cdbcc32e713_v2_3_7_6").validate(obj)
    return True


def read_site_health_summary_data_by_site_id_v1(api):
    endpoint_result = api.sites.read_site_health_summary_data_by_site_id_v1(
        attribute="string", end_time=0, id="string", start_time=0, view="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_read_site_health_summary_data_by_site_id_v1(api, validator):
    try:
        assert is_valid_read_site_health_summary_data_by_site_id_v1(
            validator, read_site_health_summary_data_by_site_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def read_site_health_summary_data_by_site_id_v1_default_val(api):
    endpoint_result = api.sites.read_site_health_summary_data_by_site_id_v1(
        attribute=None, end_time=None, id="string", start_time=None, view=None
    )
    return endpoint_result


@pytest.mark.sites
def test_read_site_health_summary_data_by_site_id_v1_default_val(api, validator):
    try:
        assert is_valid_read_site_health_summary_data_by_site_id_v1(
            validator, read_site_health_summary_data_by_site_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_devices_to_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_0a544e27e18e5412af3b68d915c8ca50_v2_3_7_6").validate(obj)
    return True


def assign_devices_to_site_v1(api):
    endpoint_result = api.sites.assign_devices_to_site_v1(
        active_validation=True,
        device=[{"ip": "string"}],
        payload=None,
        site_id="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_assign_devices_to_site_v1(api, validator):
    try:
        assert is_valid_assign_devices_to_site_v1(
            validator, assign_devices_to_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_devices_to_site_v1_default_val(api):
    endpoint_result = api.sites.assign_devices_to_site_v1(
        active_validation=True, device=None, payload=None, site_id="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_assign_devices_to_site_v1_default_val(api, validator):
    try:
        assert is_valid_assign_devices_to_site_v1(
            validator, assign_devices_to_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_export_map_archive_v1(json_schema_validate, obj):
    json_schema_validate("jsd_c937494318f952ba92eaeb82b144c338_v2_3_7_6").validate(obj)
    return True


def export_map_archive_v1(api):
    endpoint_result = api.sites.export_map_archive_v1(
        active_validation=True, payload=None, site_hierarchy_uuid="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_export_map_archive_v1(api, validator):
    try:
        assert is_valid_export_map_archive_v1(validator, export_map_archive_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def export_map_archive_v1_default_val(api):
    endpoint_result = api.sites.export_map_archive_v1(
        active_validation=True, payload=None, site_hierarchy_uuid="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_export_map_archive_v1_default_val(api, validator):
    try:
        assert is_valid_export_map_archive_v1(
            validator, export_map_archive_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_map_archive_start_import_v1(json_schema_validate, obj):
    json_schema_validate("jsd_07ea81890f92553aaed79952ab7ab363_v2_3_7_6").validate(obj)
    return True


def import_map_archive_start_import_v1(api):
    endpoint_result = api.sites.import_map_archive_start_import_v1(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_start_import_v1(api, validator):
    try:
        assert is_valid_import_map_archive_start_import_v1(
            validator, import_map_archive_start_import_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_map_archive_start_import_v1_default_val(api):
    endpoint_result = api.sites.import_map_archive_start_import_v1(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_start_import_v1_default_val(api, validator):
    try:
        assert is_valid_import_map_archive_start_import_v1(
            validator, import_map_archive_start_import_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_map_archive_cancel_an_import_v1(json_schema_validate, obj):
    json_schema_validate("jsd_44580624a59853e8a3462db736556ab4_v2_3_7_6").validate(obj)
    return True


def import_map_archive_cancel_an_import_v1(api):
    endpoint_result = api.sites.import_map_archive_cancel_an_import_v1(
        import_context_uuid="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_cancel_an_import_v1(api, validator):
    try:
        assert is_valid_import_map_archive_cancel_an_import_v1(
            validator, import_map_archive_cancel_an_import_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_map_archive_cancel_an_import_v1_default_val(api):
    endpoint_result = api.sites.import_map_archive_cancel_an_import_v1(
        import_context_uuid="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_cancel_an_import_v1_default_val(api, validator):
    try:
        assert is_valid_import_map_archive_cancel_an_import_v1(
            validator, import_map_archive_cancel_an_import_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_map_archive_perform_import_v1(json_schema_validate, obj):
    json_schema_validate("jsd_df05fb7a09595d0b9f6bc46b24275927_v2_3_7_6").validate(obj)
    return True


def import_map_archive_perform_import_v1(api):
    endpoint_result = api.sites.import_map_archive_perform_import_v1(
        active_validation=True, import_context_uuid="string", payload=None
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_perform_import_v1(api, validator):
    try:
        assert is_valid_import_map_archive_perform_import_v1(
            validator, import_map_archive_perform_import_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_map_archive_perform_import_v1_default_val(api):
    endpoint_result = api.sites.import_map_archive_perform_import_v1(
        active_validation=True, import_context_uuid="string", payload=None
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_perform_import_v1_default_val(api, validator):
    try:
        assert is_valid_import_map_archive_perform_import_v1(
            validator, import_map_archive_perform_import_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_map_archive_import_status_v1(json_schema_validate, obj):
    json_schema_validate("jsd_c04c790688e4566c9f5eaa52b8fe39c8_v2_3_7_6").validate(obj)
    return True


def import_map_archive_import_status_v1(api):
    endpoint_result = api.sites.import_map_archive_import_status_v1(
        import_context_uuid="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_import_status_v1(api, validator):
    try:
        assert is_valid_import_map_archive_import_status_v1(
            validator, import_map_archive_import_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_map_archive_import_status_v1_default_val(api):
    endpoint_result = api.sites.import_map_archive_import_status_v1(
        import_context_uuid="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_import_map_archive_import_status_v1_default_val(api, validator):
    try:
        assert is_valid_import_map_archive_import_status_v1(
            validator, import_map_archive_import_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_maps_supported_access_points_v1(json_schema_validate, obj):
    json_schema_validate("jsd_8a5e16b065e3534c8894e52d52540f99_v2_3_7_6").validate(obj)
    return True


def maps_supported_access_points_v1(api):
    endpoint_result = api.sites.maps_supported_access_points_v1()
    return endpoint_result


@pytest.mark.sites
def test_maps_supported_access_points_v1(api, validator):
    try:
        assert is_valid_maps_supported_access_points_v1(
            validator, maps_supported_access_points_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def maps_supported_access_points_v1_default_val(api):
    endpoint_result = api.sites.maps_supported_access_points_v1()
    return endpoint_result


@pytest.mark.sites
def test_maps_supported_access_points_v1_default_val(api, validator):
    try:
        assert is_valid_maps_supported_access_points_v1(
            validator, maps_supported_access_points_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_membership_v1(json_schema_validate, obj):
    json_schema_validate("jsd_63284ca11e0b5f8d91395e2462a9cfdc_v2_3_7_6").validate(obj)
    return True


def get_membership_v1(api):
    endpoint_result = api.sites.get_membership_v1(
        device_family="string",
        limit=0,
        offset=0,
        serial_number="string",
        site_id="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_get_membership_v1(api, validator):
    try:
        assert is_valid_get_membership_v1(validator, get_membership_v1(api))
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
        site_id="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_get_membership_v1_default_val(api, validator):
    try:
        assert is_valid_get_membership_v1(validator, get_membership_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_bce8e6b307ce52dd8f5546fbd78e05ee_v2_3_7_6").validate(obj)
    return True


def create_site_v1(api):
    endpoint_result = api.sites.create_site_v1(
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
def test_create_site_v1(api, validator):
    try:
        assert is_valid_create_site_v1(validator, create_site_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_site_v1_default_val(api):
    endpoint_result = api.sites.create_site_v1(
        active_validation=True, payload=None, site=None, type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_create_site_v1_default_val(api, validator):
    try:
        assert is_valid_create_site_v1(validator, create_site_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_dbdd6074bedc59b9a3edd6477897d659_v2_3_7_6").validate(obj)
    return True


def get_site_v1(api):
    endpoint_result = api.sites.get_site_v1(
        limit=0, name="string", offset=0, site_id="string", type="string"
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_v1(api, validator):
    try:
        assert is_valid_get_site_v1(validator, get_site_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_v1_default_val(api):
    endpoint_result = api.sites.get_site_v1(
        limit=None, name=None, offset=None, site_id=None, type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_v1(validator, get_site_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_health_v1(json_schema_validate, obj):
    json_schema_validate("jsd_ae4b592f66035f24b55028f79c1b7290_v2_3_7_6").validate(obj)
    return True


def get_site_health_v1(api):
    endpoint_result = api.sites.get_site_health_v1(
        limit=0, offset=0, site_type="string", timestamp=0
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_health_v1(api, validator):
    try:
        assert is_valid_get_site_health_v1(validator, get_site_health_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_health_v1_default_val(api):
    endpoint_result = api.sites.get_site_health_v1(
        limit=None, offset=None, site_type=None, timestamp=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_health_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_health_v1(
            validator, get_site_health_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_devices_that_are_assigned_to_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_cfabe762b2af55f282076fe2a14b6792_v2_3_7_6").validate(obj)
    return True


def get_devices_that_are_assigned_to_a_site_v1(api):
    endpoint_result = api.sites.get_devices_that_are_assigned_to_a_site_v1(
        id="string",
        level="string",
        limit="string",
        member_type="string",
        offset="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_get_devices_that_are_assigned_to_a_site_v1(api, validator):
    try:
        assert is_valid_get_devices_that_are_assigned_to_a_site_v1(
            validator, get_devices_that_are_assigned_to_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_devices_that_are_assigned_to_a_site_v1_default_val(api):
    endpoint_result = api.sites.get_devices_that_are_assigned_to_a_site_v1(
        id="string", level=None, limit=None, member_type=None, offset=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_devices_that_are_assigned_to_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_get_devices_that_are_assigned_to_a_site_v1(
            validator, get_devices_that_are_assigned_to_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_count_v1(json_schema_validate, obj):
    json_schema_validate("jsd_e7a025fbe2c452fc82eedd5c50104aba_v2_3_7_6").validate(obj)
    return True


def get_site_count_v1(api):
    endpoint_result = api.sites.get_site_count_v1(site_id="string")
    return endpoint_result


@pytest.mark.sites
def test_get_site_count_v1(api, validator):
    try:
        assert is_valid_get_site_count_v1(validator, get_site_count_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_count_v1_default_val(api):
    endpoint_result = api.sites.get_site_count_v1(site_id=None)
    return endpoint_result


@pytest.mark.sites
def test_get_site_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_count_v1(validator, get_site_count_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_27df9908ad265e83ab77d73803925678_v2_3_7_6").validate(obj)
    return True


def update_site_v1(api):
    endpoint_result = api.sites.update_site_v1(
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
            },
        },
        site_id="string",
        type="string",
    )
    return endpoint_result


@pytest.mark.sites
def test_update_site_v1(api, validator):
    try:
        assert is_valid_update_site_v1(validator, update_site_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_site_v1_default_val(api):
    endpoint_result = api.sites.update_site_v1(
        active_validation=True, payload=None, site=None, site_id="string", type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_update_site_v1_default_val(api, validator):
    try:
        assert is_valid_update_site_v1(validator, update_site_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_ba5567f03dea5b6891957dd410319e3f_v2_3_7_6").validate(obj)
    return True


def delete_site_v1(api):
    endpoint_result = api.sites.delete_site_v1(site_id="string")
    return endpoint_result


@pytest.mark.sites
def test_delete_site_v1(api, validator):
    try:
        assert is_valid_delete_site_v1(validator, delete_site_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_site_v1_default_val(api):
    endpoint_result = api.sites.delete_site_v1(site_id="string")
    return endpoint_result


@pytest.mark.sites
def test_delete_site_v1_default_val(api, validator):
    try:
        assert is_valid_delete_site_v1(validator, delete_site_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_v2(json_schema_validate, obj):
    json_schema_validate("jsd_43c5e65cce2954fdb7177ac0a8e0b76f_v2_3_7_6").validate(obj)
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
    json_schema_validate("jsd_371b10ff66e5568ebe6d41faeeabda22_v2_3_7_6").validate(obj)
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

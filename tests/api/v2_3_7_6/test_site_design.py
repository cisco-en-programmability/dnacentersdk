# -*- coding: utf-8 -*-
"""DNACenterAPI site_design API fixtures and tests.

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


def is_valid_creates_an_area_v1(json_schema_validate, obj):
    json_schema_validate("jsd_f6a4086c00f45dc5a634f0b8db5cdfd3_v2_3_7_6").validate(obj)
    return True


def creates_an_area_v1(api):
    endpoint_result = api.site_design.creates_an_area_v1(
        active_validation=True, name="string", parentId="string", payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_creates_an_area_v1(api, validator):
    try:
        assert is_valid_creates_an_area_v1(validator, creates_an_area_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_an_area_v1_default_val(api):
    endpoint_result = api.site_design.creates_an_area_v1(
        active_validation=True, name=None, parentId=None, payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_creates_an_area_v1_default_val(api, validator):
    try:
        assert is_valid_creates_an_area_v1(
            validator, creates_an_area_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_an_area_v1(json_schema_validate, obj):
    json_schema_validate("jsd_55f50f8c552f5d2eb68d715e1318976e_v2_3_7_6").validate(obj)
    return True


def updates_an_area_v1(api):
    endpoint_result = api.site_design.updates_an_area_v1(
        active_validation=True,
        id="string",
        name="string",
        parentId="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.site_design
def test_updates_an_area_v1(api, validator):
    try:
        assert is_valid_updates_an_area_v1(validator, updates_an_area_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_an_area_v1_default_val(api):
    endpoint_result = api.site_design.updates_an_area_v1(
        active_validation=True, id="string", name=None, parentId=None, payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_updates_an_area_v1_default_val(api, validator):
    try:
        assert is_valid_updates_an_area_v1(
            validator, updates_an_area_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_an_area_v1(json_schema_validate, obj):
    json_schema_validate("jsd_e3604000c24755bd855c3124712ed10f_v2_3_7_6").validate(obj)
    return True


def deletes_an_area_v1(api):
    endpoint_result = api.site_design.deletes_an_area_v1(id="string")
    return endpoint_result


@pytest.mark.site_design
def test_deletes_an_area_v1(api, validator):
    try:
        assert is_valid_deletes_an_area_v1(validator, deletes_an_area_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_an_area_v1_default_val(api):
    endpoint_result = api.site_design.deletes_an_area_v1(id="string")
    return endpoint_result


@pytest.mark.site_design
def test_deletes_an_area_v1_default_val(api, validator):
    try:
        assert is_valid_deletes_an_area_v1(
            validator, deletes_an_area_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_an_area_v1(json_schema_validate, obj):
    json_schema_validate("jsd_608d4479806c54eb89c4214f716731fc_v2_3_7_6").validate(obj)
    return True


def gets_an_area_v1(api):
    endpoint_result = api.site_design.gets_an_area_v1(id="string")
    return endpoint_result


@pytest.mark.site_design
def test_gets_an_area_v1(api, validator):
    try:
        assert is_valid_gets_an_area_v1(validator, gets_an_area_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_an_area_v1_default_val(api):
    endpoint_result = api.site_design.gets_an_area_v1(id="string")
    return endpoint_result


@pytest.mark.site_design
def test_gets_an_area_v1_default_val(api, validator):
    try:
        assert is_valid_gets_an_area_v1(validator, gets_an_area_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_network_devices_to_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_31c279ba052250d883ef87775a415089_v2_3_7_6").validate(obj)
    return True


def assign_network_devices_to_a_site_v1(api):
    endpoint_result = api.site_design.assign_network_devices_to_a_site_v1(
        active_validation=True, deviceIds=["string"], payload=None, siteId="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_assign_network_devices_to_a_site_v1(api, validator):
    try:
        assert is_valid_assign_network_devices_to_a_site_v1(
            validator, assign_network_devices_to_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_network_devices_to_a_site_v1_default_val(api):
    endpoint_result = api.site_design.assign_network_devices_to_a_site_v1(
        active_validation=True, deviceIds=None, payload=None, siteId=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_assign_network_devices_to_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_assign_network_devices_to_a_site_v1(
            validator, assign_network_devices_to_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_assigned_network_devices_v1(json_schema_validate, obj):
    json_schema_validate("jsd_0c8f7e2eddc752739209482b6386e2d5_v2_3_7_6").validate(obj)
    return True


def get_site_assigned_network_devices_v1(api):
    endpoint_result = api.site_design.get_site_assigned_network_devices_v1(
        limit=0, offset=0, site_id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_site_assigned_network_devices_v1(api, validator):
    try:
        assert is_valid_get_site_assigned_network_devices_v1(
            validator, get_site_assigned_network_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_assigned_network_devices_v1_default_val(api):
    endpoint_result = api.site_design.get_site_assigned_network_devices_v1(
        limit=None, offset=None, site_id=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_site_assigned_network_devices_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_assigned_network_devices_v1(
            validator, get_site_assigned_network_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_assigned_network_devices_count_v1(json_schema_validate, obj):
    json_schema_validate("jsd_72ac24397435521da0a2feaf8af96162_v2_3_7_6").validate(obj)
    return True


def get_site_assigned_network_devices_count_v1(api):
    endpoint_result = api.site_design.get_site_assigned_network_devices_count_v1(
        site_id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_site_assigned_network_devices_count_v1(api, validator):
    try:
        assert is_valid_get_site_assigned_network_devices_count_v1(
            validator, get_site_assigned_network_devices_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_assigned_network_devices_count_v1_default_val(api):
    endpoint_result = api.site_design.get_site_assigned_network_devices_count_v1(
        site_id=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_site_assigned_network_devices_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_assigned_network_devices_count_v1(
            validator, get_site_assigned_network_devices_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_controllability_settings_v1(json_schema_validate, obj):
    json_schema_validate("jsd_751818a9b27c573ea0530ce2858a1c1d_v2_3_7_6").validate(obj)
    return True


def get_device_controllability_settings_v1(api):
    endpoint_result = api.site_design.get_device_controllability_settings_v1()
    return endpoint_result


@pytest.mark.site_design
def test_get_device_controllability_settings_v1(api, validator):
    try:
        assert is_valid_get_device_controllability_settings_v1(
            validator, get_device_controllability_settings_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_controllability_settings_v1_default_val(api):
    endpoint_result = api.site_design.get_device_controllability_settings_v1()
    return endpoint_result


@pytest.mark.site_design
def test_get_device_controllability_settings_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_controllability_settings_v1(
            validator, get_device_controllability_settings_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_controllability_settings_v1(json_schema_validate, obj):
    json_schema_validate("jsd_c7f28c3d23ba5384be5e769ae0505d00_v2_3_7_6").validate(obj)
    return True


def update_device_controllability_settings_v1(api):
    endpoint_result = api.site_design.update_device_controllability_settings_v1(
        active_validation=True,
        autocorrectTelemetryConfig=True,
        deviceControllability=True,
        payload=None,
    )
    return endpoint_result


@pytest.mark.site_design
def test_update_device_controllability_settings_v1(api, validator):
    try:
        assert is_valid_update_device_controllability_settings_v1(
            validator, update_device_controllability_settings_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_controllability_settings_v1_default_val(api):
    endpoint_result = api.site_design.update_device_controllability_settings_v1(
        active_validation=True,
        autocorrectTelemetryConfig=None,
        deviceControllability=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.site_design
def test_update_device_controllability_settings_v1_default_val(api, validator):
    try:
        assert is_valid_update_device_controllability_settings_v1(
            validator, update_device_controllability_settings_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_not_assigned_network_devices_v1(json_schema_validate, obj):
    json_schema_validate("jsd_abb50ef5853d5772a8c7184b972af6d5_v2_3_7_6").validate(obj)
    return True


def get_site_not_assigned_network_devices_v1(api):
    endpoint_result = api.site_design.get_site_not_assigned_network_devices_v1(
        limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_site_not_assigned_network_devices_v1(api, validator):
    try:
        assert is_valid_get_site_not_assigned_network_devices_v1(
            validator, get_site_not_assigned_network_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_not_assigned_network_devices_v1_default_val(api):
    endpoint_result = api.site_design.get_site_not_assigned_network_devices_v1(
        limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_site_not_assigned_network_devices_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_not_assigned_network_devices_v1(
            validator, get_site_not_assigned_network_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_not_assigned_network_devices_count_v1(json_schema_validate, obj):
    json_schema_validate("jsd_f0f95023b5e85d68916757f62ebe3a39_v2_3_7_6").validate(obj)
    return True


def get_site_not_assigned_network_devices_count_v1(api):
    endpoint_result = api.site_design.get_site_not_assigned_network_devices_count_v1()
    return endpoint_result


@pytest.mark.site_design
def test_get_site_not_assigned_network_devices_count_v1(api, validator):
    try:
        assert is_valid_get_site_not_assigned_network_devices_count_v1(
            validator, get_site_not_assigned_network_devices_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_not_assigned_network_devices_count_v1_default_val(api):
    endpoint_result = api.site_design.get_site_not_assigned_network_devices_count_v1()
    return endpoint_result


@pytest.mark.site_design
def test_get_site_not_assigned_network_devices_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_not_assigned_network_devices_count_v1(
            validator, get_site_not_assigned_network_devices_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_unassign_network_devices_from_sites_v1(json_schema_validate, obj):
    json_schema_validate("jsd_a41113bc28515538af4fe4d2ff707f60_v2_3_7_6").validate(obj)
    return True


def unassign_network_devices_from_sites_v1(api):
    endpoint_result = api.site_design.unassign_network_devices_from_sites_v1(
        active_validation=True, deviceIds=["string"], payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_unassign_network_devices_from_sites_v1(api, validator):
    try:
        assert is_valid_unassign_network_devices_from_sites_v1(
            validator, unassign_network_devices_from_sites_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def unassign_network_devices_from_sites_v1_default_val(api):
    endpoint_result = api.site_design.unassign_network_devices_from_sites_v1(
        active_validation=True, deviceIds=None, payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_unassign_network_devices_from_sites_v1_default_val(api, validator):
    try:
        assert is_valid_unassign_network_devices_from_sites_v1(
            validator, unassign_network_devices_from_sites_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_assigned_network_device_v1(json_schema_validate, obj):
    json_schema_validate("jsd_f439c50a9743505a89dd01b099ae2ac2_v2_3_7_6").validate(obj)
    return True


def get_site_assigned_network_device_v1(api):
    endpoint_result = api.site_design.get_site_assigned_network_device_v1(id="string")
    return endpoint_result


@pytest.mark.site_design
def test_get_site_assigned_network_device_v1(api, validator):
    try:
        assert is_valid_get_site_assigned_network_device_v1(
            validator, get_site_assigned_network_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_assigned_network_device_v1_default_val(api):
    endpoint_result = api.site_design.get_site_assigned_network_device_v1(id="string")
    return endpoint_result


@pytest.mark.site_design
def test_get_site_assigned_network_device_v1_default_val(api, validator):
    try:
        assert is_valid_get_site_assigned_network_device_v1(
            validator, get_site_assigned_network_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_network_profiles_for_sites_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_1f98e2b2923855879acfcb06c5723add_v2_3_7_6").validate(obj)
    return True


def retrieves_the_list_of_network_profiles_for_sites_v1(api):
    endpoint_result = (
        api.site_design.retrieves_the_list_of_network_profiles_for_sites_v1(
            limit=0, offset=0, order="string", sort_by="string", type="string"
        )
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieves_the_list_of_network_profiles_for_sites_v1(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_network_profiles_for_sites_v1(
            validator, retrieves_the_list_of_network_profiles_for_sites_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_network_profiles_for_sites_v1_default_val(api):
    endpoint_result = (
        api.site_design.retrieves_the_list_of_network_profiles_for_sites_v1(
            limit=None, offset=None, order=None, sort_by=None, type=None
        )
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieves_the_list_of_network_profiles_for_sites_v1_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_network_profiles_for_sites_v1(
            validator,
            retrieves_the_list_of_network_profiles_for_sites_v1_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_network_profiles_for_sites_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_ee735f82a2d9552097c69352326c3630_v2_3_7_6").validate(obj)
    return True


def retrieves_the_count_of_network_profiles_for_sites_v1(api):
    endpoint_result = (
        api.site_design.retrieves_the_count_of_network_profiles_for_sites_v1(
            type="string"
        )
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieves_the_count_of_network_profiles_for_sites_v1(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_network_profiles_for_sites_v1(
            validator, retrieves_the_count_of_network_profiles_for_sites_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_network_profiles_for_sites_v1_default_val(api):
    endpoint_result = (
        api.site_design.retrieves_the_count_of_network_profiles_for_sites_v1(type=None)
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieves_the_count_of_network_profiles_for_sites_v1_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_count_of_network_profiles_for_sites_v1(
            validator,
            retrieves_the_count_of_network_profiles_for_sites_v1_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_a_network_profile_for_sites_v1(json_schema_validate, obj):
    json_schema_validate("jsd_e753f36584d75677a7076577f36dd515_v2_3_7_6").validate(obj)
    return True


def deletes_a_network_profile_for_sites_v1(api):
    endpoint_result = api.site_design.deletes_a_network_profile_for_sites_v1(
        id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_deletes_a_network_profile_for_sites_v1(api, validator):
    try:
        assert is_valid_deletes_a_network_profile_for_sites_v1(
            validator, deletes_a_network_profile_for_sites_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_a_network_profile_for_sites_v1_default_val(api):
    endpoint_result = api.site_design.deletes_a_network_profile_for_sites_v1(
        id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_deletes_a_network_profile_for_sites_v1_default_val(api, validator):
    try:
        assert is_valid_deletes_a_network_profile_for_sites_v1(
            validator, deletes_a_network_profile_for_sites_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_network_profile_for_sites_by_id_v1(json_schema_validate, obj):
    json_schema_validate("jsd_e67cf4ec83635f318184f32dff700aa7_v2_3_7_6").validate(obj)
    return True


def retrieve_a_network_profile_for_sites_by_id_v1(api):
    endpoint_result = api.site_design.retrieve_a_network_profile_for_sites_by_id_v1(
        id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieve_a_network_profile_for_sites_by_id_v1(api, validator):
    try:
        assert is_valid_retrieve_a_network_profile_for_sites_by_id_v1(
            validator, retrieve_a_network_profile_for_sites_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_network_profile_for_sites_by_id_v1_default_val(api):
    endpoint_result = api.site_design.retrieve_a_network_profile_for_sites_by_id_v1(
        id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieve_a_network_profile_for_sites_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_network_profile_for_sites_by_id_v1(
            validator, retrieve_a_network_profile_for_sites_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_a_network_profile_for_sites_to_the_given_site_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_b350fb0876a25879973b0840fbb690bb_v2_3_7_6").validate(obj)
    return True


def assign_a_network_profile_for_sites_to_the_given_site_v1(api):
    endpoint_result = (
        api.site_design.assign_a_network_profile_for_sites_to_the_given_site_v1(
            active_validation=True, id="string", payload=None, profile_id="string"
        )
    )
    return endpoint_result


@pytest.mark.site_design
def test_assign_a_network_profile_for_sites_to_the_given_site_v1(api, validator):
    try:
        assert is_valid_assign_a_network_profile_for_sites_to_the_given_site_v1(
            validator, assign_a_network_profile_for_sites_to_the_given_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_a_network_profile_for_sites_to_the_given_site_v1_default_val(api):
    endpoint_result = (
        api.site_design.assign_a_network_profile_for_sites_to_the_given_site_v1(
            active_validation=True, id=None, payload=None, profile_id="string"
        )
    )
    return endpoint_result


@pytest.mark.site_design
def test_assign_a_network_profile_for_sites_to_the_given_site_v1_default_val(
    api, validator
):
    try:
        assert is_valid_assign_a_network_profile_for_sites_to_the_given_site_v1(
            validator,
            assign_a_network_profile_for_sites_to_the_given_site_v1_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_c5786cf2e69852a1aefbcd9f06a0366d_v2_3_7_6").validate(obj)
    return True


def retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
    api,
):
    endpoint_result = api.site_design.retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
        limit=0, offset=0, profile_id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
            validator,
            retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1_default_val(
    api,
):
    endpoint_result = api.site_design.retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
        limit=None, offset=None, profile_id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
            validator,
            retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_a_network_profile_for_sites_to_a_list_of_sites_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_796eea0014365ef78d30d9ba8f1752e8_v2_3_7_6").validate(obj)
    return True


def assign_a_network_profile_for_sites_to_a_list_of_sites_v1(api):
    endpoint_result = (
        api.site_design.assign_a_network_profile_for_sites_to_a_list_of_sites_v1(
            active_validation=True, payload=None, profile_id="string", type={}
        )
    )
    return endpoint_result


@pytest.mark.site_design
def test_assign_a_network_profile_for_sites_to_a_list_of_sites_v1(api, validator):
    try:
        assert is_valid_assign_a_network_profile_for_sites_to_a_list_of_sites_v1(
            validator, assign_a_network_profile_for_sites_to_a_list_of_sites_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_a_network_profile_for_sites_to_a_list_of_sites_v1_default_val(api):
    endpoint_result = (
        api.site_design.assign_a_network_profile_for_sites_to_a_list_of_sites_v1(
            active_validation=True, payload=None, profile_id="string", type=None
        )
    )
    return endpoint_result


@pytest.mark.site_design
def test_assign_a_network_profile_for_sites_to_a_list_of_sites_v1_default_val(
    api, validator
):
    try:
        assert is_valid_assign_a_network_profile_for_sites_to_a_list_of_sites_v1(
            validator,
            assign_a_network_profile_for_sites_to_a_list_of_sites_v1_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_unassigns_a_network_profile_for_sites_from_multiple_sites_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_1821d9b6dfe95d348865dfe1710ad9a9_v2_3_7_6").validate(obj)
    return True


def unassigns_a_network_profile_for_sites_from_multiple_sites_v1(api):
    endpoint_result = (
        api.site_design.unassigns_a_network_profile_for_sites_from_multiple_sites_v1(
            profile_id="string", site_id="string"
        )
    )
    return endpoint_result


@pytest.mark.site_design
def test_unassigns_a_network_profile_for_sites_from_multiple_sites_v1(api, validator):
    try:
        assert is_valid_unassigns_a_network_profile_for_sites_from_multiple_sites_v1(
            validator, unassigns_a_network_profile_for_sites_from_multiple_sites_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def unassigns_a_network_profile_for_sites_from_multiple_sites_v1_default_val(api):
    endpoint_result = (
        api.site_design.unassigns_a_network_profile_for_sites_from_multiple_sites_v1(
            profile_id="string", site_id=None
        )
    )
    return endpoint_result


@pytest.mark.site_design
def test_unassigns_a_network_profile_for_sites_from_multiple_sites_v1_default_val(
    api, validator
):
    try:
        assert is_valid_unassigns_a_network_profile_for_sites_from_multiple_sites_v1(
            validator,
            unassigns_a_network_profile_for_sites_from_multiple_sites_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_475c26aa98f05665962c91a1d780b943_v2_3_7_6").validate(obj)
    return True


def retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
    api,
):
    endpoint_result = api.site_design.retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
        profile_id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
    api, validator
):
    try:
        assert is_valid_retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
            validator,
            retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1_default_val(
    api,
):
    endpoint_result = api.site_design.retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
        profile_id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
            validator,
            retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_unassigns_a_network_profile_for_sites_from_a_site_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_60a1e170a11d519b88cadd674fa2ea31_v2_3_7_6").validate(obj)
    return True


def unassigns_a_network_profile_for_sites_from_a_site_v1(api):
    endpoint_result = (
        api.site_design.unassigns_a_network_profile_for_sites_from_a_site_v1(
            id="string", profile_id="string"
        )
    )
    return endpoint_result


@pytest.mark.site_design
def test_unassigns_a_network_profile_for_sites_from_a_site_v1(api, validator):
    try:
        assert is_valid_unassigns_a_network_profile_for_sites_from_a_site_v1(
            validator, unassigns_a_network_profile_for_sites_from_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def unassigns_a_network_profile_for_sites_from_a_site_v1_default_val(api):
    endpoint_result = (
        api.site_design.unassigns_a_network_profile_for_sites_from_a_site_v1(
            id="string", profile_id="string"
        )
    )
    return endpoint_result


@pytest.mark.site_design
def test_unassigns_a_network_profile_for_sites_from_a_site_v1_default_val(
    api, validator
):
    try:
        assert is_valid_unassigns_a_network_profile_for_sites_from_a_site_v1(
            validator,
            unassigns_a_network_profile_for_sites_from_a_site_v1_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_associate_v1(json_schema_validate, obj):
    json_schema_validate("jsd_378a1800508058e4b82a08ea5637b794_v2_3_7_6").validate(obj)
    return True


def associate_v1(api):
    endpoint_result = api.site_design.associate_v1(
        active_validation=True,
        network_profile_id="string",
        payload=None,
        site_id="string",
    )
    return endpoint_result


@pytest.mark.site_design
def test_associate_v1(api, validator):
    try:
        assert is_valid_associate_v1(validator, associate_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def associate_v1_default_val(api):
    endpoint_result = api.site_design.associate_v1(
        active_validation=True,
        network_profile_id="string",
        payload=None,
        site_id="string",
    )
    return endpoint_result


@pytest.mark.site_design
def test_associate_v1_default_val(api, validator):
    try:
        assert is_valid_associate_v1(validator, associate_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_disassociate_v1(json_schema_validate, obj):
    json_schema_validate("jsd_21c8936d6a0c54e89b471fe36bf28de8_v2_3_7_6").validate(obj)
    return True


def disassociate_v1(api):
    endpoint_result = api.site_design.disassociate_v1(
        network_profile_id="string", site_id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_disassociate_v1(api, validator):
    try:
        assert is_valid_disassociate_v1(validator, disassociate_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def disassociate_v1_default_val(api):
    endpoint_result = api.site_design.disassociate_v1(
        network_profile_id="string", site_id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_disassociate_v1_default_val(api, validator):
    try:
        assert is_valid_disassociate_v1(validator, disassociate_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sites_v1(json_schema_validate, obj):
    json_schema_validate("jsd_a36b1e624416553eb72d8f1c9461c938_v2_3_7_6").validate(obj)
    return True


def get_sites_v1(api):
    endpoint_result = api.site_design.get_sites_v1(
        limit=0,
        name="string",
        name_hierarchy="string",
        offset=0,
        type="string",
        units_of_measure="string",
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_sites_v1(api, validator):
    try:
        assert is_valid_get_sites_v1(validator, get_sites_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sites_v1_default_val(api):
    endpoint_result = api.site_design.get_sites_v1(
        limit=None,
        name=None,
        name_hierarchy=None,
        offset=None,
        type=None,
        units_of_measure=None,
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_sites_v1_default_val(api, validator):
    try:
        assert is_valid_get_sites_v1(validator, get_sites_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sites_v1(json_schema_validate, obj):
    json_schema_validate("jsd_39d292147221524a96616d982b0147c0_v2_3_7_6").validate(obj)
    return True


def create_sites_v1(api):
    endpoint_result = api.site_design.create_sites_v1(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_create_sites_v1(api, validator):
    try:
        assert is_valid_create_sites_v1(validator, create_sites_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_sites_v1_default_val(api):
    endpoint_result = api.site_design.create_sites_v1(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_create_sites_v1_default_val(api, validator):
    try:
        assert is_valid_create_sites_v1(validator, create_sites_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sites_count_v1(json_schema_validate, obj):
    json_schema_validate("jsd_837486c2d6e954468a7300d9ff8b2e22_v2_3_7_6").validate(obj)
    return True


def get_sites_count_v1(api):
    endpoint_result = api.site_design.get_sites_count_v1(name="string")
    return endpoint_result


@pytest.mark.site_design
def test_get_sites_count_v1(api, validator):
    try:
        assert is_valid_get_sites_count_v1(validator, get_sites_count_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sites_count_v1_default_val(api):
    endpoint_result = api.site_design.get_sites_count_v1(name=None)
    return endpoint_result


@pytest.mark.site_design
def test_get_sites_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_sites_count_v1(
            validator, get_sites_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_f12eba75e472591490a014a7335e1e9b_v2_3_7_6").validate(obj)
    return True


def retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1(
    api,
):
    endpoint_result = api.site_design.retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1(
        limit=0, offset=0, site_id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1(
            validator,
            retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1_default_val(
    api,
):
    endpoint_result = api.site_design.retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1(
        limit=None, offset=None, site_id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1(
            validator,
            retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_dc2361873bf7553c8fa5c7cb2024e5bb_v2_3_7_6").validate(obj)
    return True


def retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1(api):
    endpoint_result = api.site_design.retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1(
        site_id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1(
    api, validator
):
    try:
        assert is_valid_retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1(
            validator,
            retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1_default_val(
    api,
):
    endpoint_result = api.site_design.retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1(
        site_id="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1(
            validator,
            retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_a_building_v2(json_schema_validate, obj):
    json_schema_validate("jsd_549fc95c917352ad8410ffe6d6e522ed_v2_3_7_6").validate(obj)
    return True


def creates_a_building_v2(api):
    endpoint_result = api.site_design.creates_a_building_v2(
        active_validation=True,
        address="string",
        country="string",
        latitude=0,
        longitude=0,
        name="string",
        parentId="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.site_design
def test_creates_a_building_v2(api, validator):
    try:
        assert is_valid_creates_a_building_v2(validator, creates_a_building_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_a_building_v2_default_val(api):
    endpoint_result = api.site_design.creates_a_building_v2(
        active_validation=True,
        address=None,
        country=None,
        latitude=None,
        longitude=None,
        name=None,
        parentId=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.site_design
def test_creates_a_building_v2_default_val(api, validator):
    try:
        assert is_valid_creates_a_building_v2(
            validator, creates_a_building_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_a_building_v2(json_schema_validate, obj):
    json_schema_validate("jsd_105cd16daa50533eb0f5873b7601abb2_v2_3_7_6").validate(obj)
    return True


def updates_a_building_v2(api):
    endpoint_result = api.site_design.updates_a_building_v2(
        active_validation=True,
        address="string",
        country="string",
        id="string",
        latitude=0,
        longitude=0,
        name="string",
        parentId="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.site_design
def test_updates_a_building_v2(api, validator):
    try:
        assert is_valid_updates_a_building_v2(validator, updates_a_building_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_a_building_v2_default_val(api):
    endpoint_result = api.site_design.updates_a_building_v2(
        active_validation=True,
        address=None,
        country=None,
        id="string",
        latitude=None,
        longitude=None,
        name=None,
        parentId=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.site_design
def test_updates_a_building_v2_default_val(api, validator):
    try:
        assert is_valid_updates_a_building_v2(
            validator, updates_a_building_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_a_building_v2(json_schema_validate, obj):
    json_schema_validate("jsd_303203592e5b54d99d30ea084daf36dc_v2_3_7_6").validate(obj)
    return True


def deletes_a_building_v2(api):
    endpoint_result = api.site_design.deletes_a_building_v2(id="string")
    return endpoint_result


@pytest.mark.site_design
def test_deletes_a_building_v2(api, validator):
    try:
        assert is_valid_deletes_a_building_v2(validator, deletes_a_building_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_a_building_v2_default_val(api):
    endpoint_result = api.site_design.deletes_a_building_v2(id="string")
    return endpoint_result


@pytest.mark.site_design
def test_deletes_a_building_v2_default_val(api, validator):
    try:
        assert is_valid_deletes_a_building_v2(
            validator, deletes_a_building_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_a_building_v2(json_schema_validate, obj):
    json_schema_validate("jsd_90ab03e8addf5c7e98475769ae1a97a8_v2_3_7_6").validate(obj)
    return True


def gets_a_building_v2(api):
    endpoint_result = api.site_design.gets_a_building_v2(id="string")
    return endpoint_result


@pytest.mark.site_design
def test_gets_a_building_v2(api, validator):
    try:
        assert is_valid_gets_a_building_v2(validator, gets_a_building_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_a_building_v2_default_val(api):
    endpoint_result = api.site_design.gets_a_building_v2(id="string")
    return endpoint_result


@pytest.mark.site_design
def test_gets_a_building_v2_default_val(api, validator):
    try:
        assert is_valid_gets_a_building_v2(
            validator, gets_a_building_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_a_floor_v2(json_schema_validate, obj):
    json_schema_validate("jsd_bfb1005f4d265f8bb340637175a5841f_v2_3_7_6").validate(obj)
    return True


def creates_a_floor_v2(api):
    endpoint_result = api.site_design.creates_a_floor_v2(
        active_validation=True,
        floorNumber=0,
        height=0,
        length=0,
        name="string",
        parentId="string",
        payload=None,
        rfModel="string",
        unitsOfMeasure="string",
        width=0,
    )
    return endpoint_result


@pytest.mark.site_design
def test_creates_a_floor_v2(api, validator):
    try:
        assert is_valid_creates_a_floor_v2(validator, creates_a_floor_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_a_floor_v2_default_val(api):
    endpoint_result = api.site_design.creates_a_floor_v2(
        active_validation=True,
        floorNumber=None,
        height=None,
        length=None,
        name=None,
        parentId=None,
        payload=None,
        rfModel=None,
        unitsOfMeasure=None,
        width=None,
    )
    return endpoint_result


@pytest.mark.site_design
def test_creates_a_floor_v2_default_val(api, validator):
    try:
        assert is_valid_creates_a_floor_v2(
            validator, creates_a_floor_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_floor_settings_v2(json_schema_validate, obj):
    json_schema_validate("jsd_ad936677c99a58f6b532359d66fe98a7_v2_3_7_6").validate(obj)
    return True


def updates_floor_settings_v2(api):
    endpoint_result = api.site_design.updates_floor_settings_v2(
        active_validation=True, payload=None, unitsOfMeasure="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_updates_floor_settings_v2(api, validator):
    try:
        assert is_valid_updates_floor_settings_v2(
            validator, updates_floor_settings_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_floor_settings_v2_default_val(api):
    endpoint_result = api.site_design.updates_floor_settings_v2(
        active_validation=True, payload=None, unitsOfMeasure=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_updates_floor_settings_v2_default_val(api, validator):
    try:
        assert is_valid_updates_floor_settings_v2(
            validator, updates_floor_settings_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_floor_settings_v2(json_schema_validate, obj):
    json_schema_validate("jsd_01a774ea6dda56adb3fc81df221f62c8_v2_3_7_6").validate(obj)
    return True


def get_floor_settings_v2(api):
    endpoint_result = api.site_design.get_floor_settings_v2()
    return endpoint_result


@pytest.mark.site_design
def test_get_floor_settings_v2(api, validator):
    try:
        assert is_valid_get_floor_settings_v2(validator, get_floor_settings_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_floor_settings_v2_default_val(api):
    endpoint_result = api.site_design.get_floor_settings_v2()
    return endpoint_result


@pytest.mark.site_design
def test_get_floor_settings_v2_default_val(api, validator):
    try:
        assert is_valid_get_floor_settings_v2(
            validator, get_floor_settings_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_a_floor_v2(json_schema_validate, obj):
    json_schema_validate("jsd_07236d5da0365e31972173f015ed3614_v2_3_7_6").validate(obj)
    return True


def updates_a_floor_v2(api):
    endpoint_result = api.site_design.updates_a_floor_v2(
        active_validation=True,
        floorNumber=0,
        height=0,
        id="string",
        length=0,
        name="string",
        parentId="string",
        payload=None,
        rfModel="string",
        unitsOfMeasure="string",
        width=0,
    )
    return endpoint_result


@pytest.mark.site_design
def test_updates_a_floor_v2(api, validator):
    try:
        assert is_valid_updates_a_floor_v2(validator, updates_a_floor_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_a_floor_v2_default_val(api):
    endpoint_result = api.site_design.updates_a_floor_v2(
        active_validation=True,
        floorNumber=None,
        height=None,
        id="string",
        length=None,
        name=None,
        parentId=None,
        payload=None,
        rfModel=None,
        unitsOfMeasure=None,
        width=None,
    )
    return endpoint_result


@pytest.mark.site_design
def test_updates_a_floor_v2_default_val(api, validator):
    try:
        assert is_valid_updates_a_floor_v2(
            validator, updates_a_floor_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_a_floor_v2(json_schema_validate, obj):
    json_schema_validate("jsd_8f2f085a136a55e6a03f75ca03de17bd_v2_3_7_6").validate(obj)
    return True


def gets_a_floor_v2(api):
    endpoint_result = api.site_design.gets_a_floor_v2(
        id="string", units_of_measure="string"
    )
    return endpoint_result


@pytest.mark.site_design
def test_gets_a_floor_v2(api, validator):
    try:
        assert is_valid_gets_a_floor_v2(validator, gets_a_floor_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_a_floor_v2_default_val(api):
    endpoint_result = api.site_design.gets_a_floor_v2(
        id="string", units_of_measure=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_gets_a_floor_v2_default_val(api, validator):
    try:
        assert is_valid_gets_a_floor_v2(validator, gets_a_floor_v2_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_a_floor_v2(json_schema_validate, obj):
    json_schema_validate("jsd_071ec0e563f25f44bbe568527ea87fd6_v2_3_7_6").validate(obj)
    return True


def deletes_a_floor_v2(api):
    endpoint_result = api.site_design.deletes_a_floor_v2(id="string")
    return endpoint_result


@pytest.mark.site_design
def test_deletes_a_floor_v2(api, validator):
    try:
        assert is_valid_deletes_a_floor_v2(validator, deletes_a_floor_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_a_floor_v2_default_val(api):
    endpoint_result = api.site_design.deletes_a_floor_v2(id="string")
    return endpoint_result


@pytest.mark.site_design
def test_deletes_a_floor_v2_default_val(api, validator):
    try:
        assert is_valid_deletes_a_floor_v2(
            validator, deletes_a_floor_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_uploads_floor_image_v2(json_schema_validate, obj):
    json_schema_validate("jsd_520df8448b465a0abdc9bb7ee17aac9f_v2_3_7_6").validate(obj)
    return True


def uploads_floor_image_v2(api):
    endpoint_result = api.site_design.uploads_floor_image_v2(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_uploads_floor_image_v2(api, validator):
    try:
        assert is_valid_uploads_floor_image_v2(validator, uploads_floor_image_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def uploads_floor_image_v2_default_val(api):
    endpoint_result = api.site_design.uploads_floor_image_v2(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_uploads_floor_image_v2_default_val(api, validator):
    try:
        assert is_valid_uploads_floor_image_v2(
            validator, uploads_floor_image_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

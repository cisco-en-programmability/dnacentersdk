# -*- coding: utf-8 -*-
"""CatalystCenterAPI software_image_management_swim API fixtures and tests.

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

pytestmark = pytest.mark.skipif(
    DNA_CENTER_VERSION != "3.1.3.0", reason="version does not match"
)


def is_valid_trigger_software_image_activation(json_schema_validate, obj):
    json_schema_validate("jsd_22891a9136d5513985f15e91a19da66c_v3_1_3_0").validate(obj)
    return True


def trigger_software_image_activation(api):
    endpoint_result = (
        api.software_image_management_swim.trigger_software_image_activation(
            active_validation=True, payload=None, schedule_validate=True
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_trigger_software_image_activation(api, validator):
    try:
        assert is_valid_trigger_software_image_activation(
            validator, trigger_software_image_activation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def trigger_software_image_activation_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.trigger_software_image_activation(
            active_validation=True, payload=None, schedule_validate=None
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_trigger_software_image_activation_default_val(api, validator):
    try:
        assert is_valid_trigger_software_image_activation(
            validator, trigger_software_image_activation_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_trigger_software_image_distribution(json_schema_validate, obj):
    json_schema_validate("jsd_6c8d11fb9fc752ab8bb8e2b1413ccc92_v3_1_3_0").validate(obj)
    return True


def trigger_software_image_distribution(api):
    endpoint_result = (
        api.software_image_management_swim.trigger_software_image_distribution(
            active_validation=True, payload=None
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_trigger_software_image_distribution(api, validator):
    try:
        assert is_valid_trigger_software_image_distribution(
            validator, trigger_software_image_distribution(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def trigger_software_image_distribution_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.trigger_software_image_distribution(
            active_validation=True, payload=None
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_trigger_software_image_distribution_default_val(api, validator):
    try:
        assert is_valid_trigger_software_image_distribution(
            validator, trigger_software_image_distribution_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_software_image_details(json_schema_validate, obj):
    json_schema_validate("jsd_039f73101d5d5e409f571084ab4c6049_v3_1_3_0").validate(obj)
    return True


def get_software_image_details(api):
    endpoint_result = api.software_image_management_swim.get_software_image_details(
        application_type="string",
        created_time=0,
        family="string",
        image_integrity_status="string",
        image_name="string",
        image_series="string",
        image_size_greater_than=0,
        image_size_lesser_than=0,
        image_uuid="string",
        is_cco_latest=True,
        is_cco_recommended=True,
        is_tagged_golden=True,
        limit=0,
        name="string",
        offset=0,
        sort_by="string",
        sort_order="string",
        version="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_software_image_details(api, validator):
    try:
        assert is_valid_get_software_image_details(
            validator, get_software_image_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_software_image_details_default_val(api):
    endpoint_result = api.software_image_management_swim.get_software_image_details(
        application_type=None,
        created_time=None,
        family=None,
        image_integrity_status=None,
        image_name=None,
        image_series=None,
        image_size_greater_than=None,
        image_size_lesser_than=None,
        image_uuid=None,
        is_cco_latest=None,
        is_cco_recommended=None,
        is_tagged_golden=None,
        limit=None,
        name=None,
        offset=None,
        sort_by=None,
        sort_order=None,
        version=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_software_image_details_default_val(api, validator):
    try:
        assert is_valid_get_software_image_details(
            validator, get_software_image_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_family_identifiers(json_schema_validate, obj):
    json_schema_validate("jsd_b5c47f316ff058eb979bdea047f9d5b5_v3_1_3_0").validate(obj)
    return True


def get_device_family_identifiers(api):
    endpoint_result = api.software_image_management_swim.get_device_family_identifiers()
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_device_family_identifiers(api, validator):
    try:
        assert is_valid_get_device_family_identifiers(
            validator, get_device_family_identifiers(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_family_identifiers_default_val(api):
    endpoint_result = api.software_image_management_swim.get_device_family_identifiers()
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_device_family_identifiers_default_val(api, validator):
    try:
        assert is_valid_get_device_family_identifiers(
            validator, get_device_family_identifiers_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_tag_as_golden_image(json_schema_validate, obj):
    json_schema_validate("jsd_a9b864257b965fe4bd8b0293f41f1537_v3_1_3_0").validate(obj)
    return True


def tag_as_golden_image(api):
    endpoint_result = api.software_image_management_swim.tag_as_golden_image(
        active_validation=True,
        deviceFamilyIdentifier="string",
        deviceRole="string",
        imageId="string",
        payload=None,
        siteId="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_tag_as_golden_image(api, validator):
    try:
        assert is_valid_tag_as_golden_image(validator, tag_as_golden_image(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def tag_as_golden_image_default_val(api):
    endpoint_result = api.software_image_management_swim.tag_as_golden_image(
        active_validation=True,
        deviceFamilyIdentifier=None,
        deviceRole=None,
        imageId=None,
        payload=None,
        siteId=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_tag_as_golden_image_default_val(api, validator):
    try:
        assert is_valid_tag_as_golden_image(
            validator, tag_as_golden_image_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_golden_tag_for_image(json_schema_validate, obj):
    json_schema_validate("jsd_2405e9dd960c5378ab442f235c8135d0_v3_1_3_0").validate(obj)
    return True


def remove_golden_tag_for_image(api):
    endpoint_result = api.software_image_management_swim.remove_golden_tag_for_image(
        device_family_identifier="string",
        device_role="string",
        image_id="string",
        site_id="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_remove_golden_tag_for_image(api, validator):
    try:
        assert is_valid_remove_golden_tag_for_image(
            validator, remove_golden_tag_for_image(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def remove_golden_tag_for_image_default_val(api):
    endpoint_result = api.software_image_management_swim.remove_golden_tag_for_image(
        device_family_identifier="string",
        device_role="string",
        image_id="string",
        site_id="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_remove_golden_tag_for_image_default_val(api, validator):
    try:
        assert is_valid_remove_golden_tag_for_image(
            validator, remove_golden_tag_for_image_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_golden_tag_status_of_an_image(json_schema_validate, obj):
    json_schema_validate("jsd_97ab6266cac654d394cf943a161fcc7b_v3_1_3_0").validate(obj)
    return True


def get_golden_tag_status_of_an_image(api):
    endpoint_result = (
        api.software_image_management_swim.get_golden_tag_status_of_an_image(
            device_family_identifier="string",
            device_role="string",
            image_id="string",
            site_id="string",
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_golden_tag_status_of_an_image(api, validator):
    try:
        assert is_valid_get_golden_tag_status_of_an_image(
            validator, get_golden_tag_status_of_an_image(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_golden_tag_status_of_an_image_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.get_golden_tag_status_of_an_image(
            device_family_identifier="string",
            device_role="string",
            image_id="string",
            site_id="string",
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_golden_tag_status_of_an_image_default_val(api, validator):
    try:
        assert is_valid_get_golden_tag_status_of_an_image(
            validator, get_golden_tag_status_of_an_image_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_local_software_image(json_schema_validate, obj):
    json_schema_validate("jsd_2399c1cf6d5d5f0fa2e92539134b6c1d_v3_1_3_0").validate(obj)
    return True


def import_local_software_image(api):
    endpoint_result = api.software_image_management_swim.import_local_software_image(
        active_validation=True,
        is_third_party=True,
        payload=None,
        third_party_application_type="string",
        third_party_image_family="string",
        third_party_vendor="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_import_local_software_image(api, validator):
    try:
        assert is_valid_import_local_software_image(
            validator, import_local_software_image(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_local_software_image_default_val(api):
    endpoint_result = api.software_image_management_swim.import_local_software_image(
        active_validation=True,
        is_third_party=None,
        payload=None,
        third_party_application_type=None,
        third_party_image_family=None,
        third_party_vendor=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_import_local_software_image_default_val(api, validator):
    try:
        assert is_valid_import_local_software_image(
            validator, import_local_software_image_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_software_image_via_url(json_schema_validate, obj):
    json_schema_validate("jsd_7be8cdb967555fcca03a4c1f796eee56_v3_1_3_0").validate(obj)
    return True


def import_software_image_via_url(api):
    endpoint_result = api.software_image_management_swim.import_software_image_via_url(
        active_validation=True,
        payload=None,
        schedule_at="string",
        schedule_desc="string",
        schedule_origin="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_import_software_image_via_url(api, validator):
    try:
        assert is_valid_import_software_image_via_url(
            validator, import_software_image_via_url(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_software_image_via_url_default_val(api):
    endpoint_result = api.software_image_management_swim.import_software_image_via_url(
        active_validation=True,
        payload=None,
        schedule_at=None,
        schedule_desc=None,
        schedule_origin=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_import_software_image_via_url_default_val(api, validator):
    try:
        assert is_valid_import_software_image_via_url(
            validator, import_software_image_via_url_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_returns_list_of_software_images(json_schema_validate, obj):
    json_schema_validate("jsd_17eb239c565c57d59cd6d6f7d193a993_v3_1_3_0").validate(obj)
    return True


def returns_list_of_software_images(api):
    endpoint_result = (
        api.software_image_management_swim.returns_list_of_software_images(
            golden=True,
            has_addon_images=True,
            imported=True,
            integrity="string",
            is_addon_images=True,
            limit=0,
            name="string",
            offset=0,
            product_name_ordinal=0,
            site_id="string",
            supervisor_product_name_ordinal=0,
            version="string",
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_returns_list_of_software_images(api, validator):
    try:
        assert is_valid_returns_list_of_software_images(
            validator, returns_list_of_software_images(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def returns_list_of_software_images_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.returns_list_of_software_images(
            golden=None,
            has_addon_images=None,
            imported=None,
            integrity=None,
            is_addon_images=None,
            limit=None,
            name=None,
            offset=None,
            product_name_ordinal=None,
            site_id=None,
            supervisor_product_name_ordinal=None,
            version=None,
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_returns_list_of_software_images_default_val(api, validator):
    try:
        assert is_valid_returns_list_of_software_images(
            validator, returns_list_of_software_images_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_initiates_sync_of_software_images_from_cisco_com(
    json_schema_validate, obj
):
    json_schema_validate("jsd_febee79ae42f5ae481d85e3e5ad6fac8_v3_1_3_0").validate(obj)
    return True


def initiates_sync_of_software_images_from_cisco_com(api):
    endpoint_result = api.software_image_management_swim.initiates_sync_of_software_images_from_cisco_com(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_initiates_sync_of_software_images_from_cisco_com(api, validator):
    try:
        assert is_valid_initiates_sync_of_software_images_from_cisco_com(
            validator, initiates_sync_of_software_images_from_cisco_com(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def initiates_sync_of_software_images_from_cisco_com_default_val(api):
    endpoint_result = api.software_image_management_swim.initiates_sync_of_software_images_from_cisco_com(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_initiates_sync_of_software_images_from_cisco_com_default_val(api, validator):
    try:
        assert is_valid_initiates_sync_of_software_images_from_cisco_com(
            validator, initiates_sync_of_software_images_from_cisco_com_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_returns_count_of_software_images(json_schema_validate, obj):
    json_schema_validate("jsd_bdcd5a6fab705566a60c7885a18bf1ac_v3_1_3_0").validate(obj)
    return True


def returns_count_of_software_images(api):
    endpoint_result = (
        api.software_image_management_swim.returns_count_of_software_images(
            golden="string",
            has_addon_images=True,
            imported=True,
            integrity="string",
            is_addon_images=True,
            name="string",
            product_name_ordinal=0,
            site_id="string",
            supervisor_product_name_ordinal=0,
            version="string",
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_returns_count_of_software_images(api, validator):
    try:
        assert is_valid_returns_count_of_software_images(
            validator, returns_count_of_software_images(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def returns_count_of_software_images_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.returns_count_of_software_images(
            golden=None,
            has_addon_images=None,
            imported=None,
            integrity=None,
            is_addon_images=None,
            name=None,
            product_name_ordinal=None,
            site_id=None,
            supervisor_product_name_ordinal=None,
            version=None,
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_returns_count_of_software_images_default_val(api, validator):
    try:
        assert is_valid_returns_count_of_software_images(
            validator, returns_count_of_software_images_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_image_distribution_server(json_schema_validate, obj):
    json_schema_validate("jsd_db0f8e07ae0d5ecc83e34d29e5e57b41_v3_1_3_0").validate(obj)
    return True


def add_image_distribution_server(api):
    endpoint_result = api.software_image_management_swim.add_image_distribution_server(
        active_validation=True,
        password="string",
        payload=None,
        portNumber=0,
        rootLocation="string",
        serverAddress="string",
        username="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_add_image_distribution_server(api, validator):
    try:
        assert is_valid_add_image_distribution_server(
            validator, add_image_distribution_server(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_image_distribution_server_default_val(api):
    endpoint_result = api.software_image_management_swim.add_image_distribution_server(
        active_validation=True,
        password=None,
        payload=None,
        portNumber=None,
        rootLocation=None,
        serverAddress=None,
        username=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_add_image_distribution_server_default_val(api, validator):
    try:
        assert is_valid_add_image_distribution_server(
            validator, add_image_distribution_server_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_image_distribution_servers(json_schema_validate, obj):
    json_schema_validate("jsd_e2c81db557e753178af3bec81caa7a02_v3_1_3_0").validate(obj)
    return True


def retrieve_image_distribution_servers(api):
    endpoint_result = (
        api.software_image_management_swim.retrieve_image_distribution_servers()
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieve_image_distribution_servers(api, validator):
    try:
        assert is_valid_retrieve_image_distribution_servers(
            validator, retrieve_image_distribution_servers(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_image_distribution_servers_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.retrieve_image_distribution_servers()
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieve_image_distribution_servers_default_val(api, validator):
    try:
        assert is_valid_retrieve_image_distribution_servers(
            validator, retrieve_image_distribution_servers_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_remote_image_distribution_server(json_schema_validate, obj):
    json_schema_validate("jsd_89c49a8488cd52158790aac513e7184a_v3_1_3_0").validate(obj)
    return True


def update_remote_image_distribution_server(api):
    endpoint_result = (
        api.software_image_management_swim.update_remote_image_distribution_server(
            active_validation=True,
            id="string",
            password="string",
            payload=None,
            portNumber=0,
            username="string",
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_update_remote_image_distribution_server(api, validator):
    try:
        assert is_valid_update_remote_image_distribution_server(
            validator, update_remote_image_distribution_server(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_remote_image_distribution_server_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.update_remote_image_distribution_server(
            active_validation=True,
            id="string",
            password=None,
            payload=None,
            portNumber=None,
            username=None,
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_update_remote_image_distribution_server_default_val(api, validator):
    try:
        assert is_valid_update_remote_image_distribution_server(
            validator, update_remote_image_distribution_server_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_specific_image_distribution_server(json_schema_validate, obj):
    json_schema_validate("jsd_fe1411fc463c506591c20a0d6fbabca9_v3_1_3_0").validate(obj)
    return True


def retrieve_specific_image_distribution_server(api):
    endpoint_result = (
        api.software_image_management_swim.retrieve_specific_image_distribution_server(
            id="string"
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieve_specific_image_distribution_server(api, validator):
    try:
        assert is_valid_retrieve_specific_image_distribution_server(
            validator, retrieve_specific_image_distribution_server(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_specific_image_distribution_server_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.retrieve_specific_image_distribution_server(
            id="string"
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieve_specific_image_distribution_server_default_val(api, validator):
    try:
        assert is_valid_retrieve_specific_image_distribution_server(
            validator, retrieve_specific_image_distribution_server_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_image_distribution_server(json_schema_validate, obj):
    json_schema_validate("jsd_8832ba08e3af5db79aaef9e2909aa312_v3_1_3_0").validate(obj)
    return True


def remove_image_distribution_server(api):
    endpoint_result = (
        api.software_image_management_swim.remove_image_distribution_server(id="string")
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_remove_image_distribution_server(api, validator):
    try:
        assert is_valid_remove_image_distribution_server(
            validator, remove_image_distribution_server(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def remove_image_distribution_server_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.remove_image_distribution_server(id="string")
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_remove_image_distribution_server_default_val(api, validator):
    try:
        assert is_valid_remove_image_distribution_server(
            validator, remove_image_distribution_server_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_image(json_schema_validate, obj):
    json_schema_validate("jsd_af3d9db14c855d1a863625d4a33eb9ac_v3_1_3_0").validate(obj)
    return True


def delete_image(api):
    endpoint_result = api.software_image_management_swim.delete_image(id="string")
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_delete_image(api, validator):
    try:
        assert is_valid_delete_image(validator, delete_image(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_image_default_val(api):
    endpoint_result = api.software_image_management_swim.delete_image(id="string")
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_delete_image_default_val(api, validator):
    try:
        assert is_valid_delete_image(validator, delete_image_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_applicable_add_on_images_for_the_given_software_image(
    json_schema_validate, obj
):
    json_schema_validate("jsd_991f6787ea025b02b69de4030f36cc5c_v3_1_3_0").validate(obj)
    return True


def retrieve_applicable_add_on_images_for_the_given_software_image(api):
    endpoint_result = api.software_image_management_swim.retrieve_applicable_add_on_images_for_the_given_software_image(
        id="string"
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieve_applicable_add_on_images_for_the_given_software_image(api, validator):
    try:
        assert is_valid_retrieve_applicable_add_on_images_for_the_given_software_image(
            validator,
            retrieve_applicable_add_on_images_for_the_given_software_image(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_applicable_add_on_images_for_the_given_software_image_default_val(api):
    endpoint_result = api.software_image_management_swim.retrieve_applicable_add_on_images_for_the_given_software_image(
        id="string"
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieve_applicable_add_on_images_for_the_given_software_image_default_val(
    api, validator
):
    try:
        assert is_valid_retrieve_applicable_add_on_images_for_the_given_software_image(
            validator,
            retrieve_applicable_add_on_images_for_the_given_software_image_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_returns_count_of_add_on_images(json_schema_validate, obj):
    json_schema_validate("jsd_77d86809df17513dbe211ec7c5591a5f_v3_1_3_0").validate(obj)
    return True


def returns_count_of_add_on_images(api):
    endpoint_result = api.software_image_management_swim.returns_count_of_add_on_images(
        id="string"
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_returns_count_of_add_on_images(api, validator):
    try:
        assert is_valid_returns_count_of_add_on_images(
            validator, returns_count_of_add_on_images(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def returns_count_of_add_on_images_default_val(api):
    endpoint_result = api.software_image_management_swim.returns_count_of_add_on_images(
        id="string"
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_returns_count_of_add_on_images_default_val(api, validator):
    try:
        assert is_valid_returns_count_of_add_on_images(
            validator, returns_count_of_add_on_images_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_download_the_software_image(json_schema_validate, obj):
    json_schema_validate("jsd_cd82233a8af55e49ba9a202607561de9_v3_1_3_0").validate(obj)
    return True


def download_the_software_image(api):
    endpoint_result = api.software_image_management_swim.download_the_software_image(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_download_the_software_image(api, validator):
    try:
        assert is_valid_download_the_software_image(
            validator, download_the_software_image(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def download_the_software_image_default_val(api):
    endpoint_result = api.software_image_management_swim.download_the_software_image(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_download_the_software_image_default_val(api, validator):
    try:
        assert is_valid_download_the_software_image(
            validator, download_the_software_image_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_tagging_golden_image(json_schema_validate, obj):
    json_schema_validate("jsd_38febb2149ac5f8ba25dbf4d9a862d94_v3_1_3_0").validate(obj)
    return True


def tagging_golden_image(api):
    endpoint_result = api.software_image_management_swim.tagging_golden_image(
        active_validation=True,
        deviceRoles=["string"],
        deviceTags=["string"],
        id="string",
        payload=None,
        productNameOrdinal=0,
        site_id="string",
        supervisorProductNameOrdinal=0,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_tagging_golden_image(api, validator):
    try:
        assert is_valid_tagging_golden_image(validator, tagging_golden_image(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def tagging_golden_image_default_val(api):
    endpoint_result = api.software_image_management_swim.tagging_golden_image(
        active_validation=True,
        deviceRoles=None,
        deviceTags=None,
        id="string",
        payload=None,
        productNameOrdinal=None,
        site_id="string",
        supervisorProductNameOrdinal=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_tagging_golden_image_default_val(api, validator):
    try:
        assert is_valid_tagging_golden_image(
            validator, tagging_golden_image_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_untagging_golden_image(json_schema_validate, obj):
    json_schema_validate("jsd_5375b3ff5f865f1c8122a0ec8ca73921_v3_1_3_0").validate(obj)
    return True


def untagging_golden_image(api):
    endpoint_result = api.software_image_management_swim.untagging_golden_image(
        active_validation=True,
        deviceRoles=["string"],
        deviceTags=["string"],
        id="string",
        payload=None,
        productNameOrdinal=0,
        site_id="string",
        supervisorProductNameOrdinal=0,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_untagging_golden_image(api, validator):
    try:
        assert is_valid_untagging_golden_image(validator, untagging_golden_image(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def untagging_golden_image_default_val(api):
    endpoint_result = api.software_image_management_swim.untagging_golden_image(
        active_validation=True,
        deviceRoles=None,
        deviceTags=None,
        id="string",
        payload=None,
        productNameOrdinal=None,
        site_id="string",
        supervisorProductNameOrdinal=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_untagging_golden_image_default_val(api, validator):
    try:
        assert is_valid_untagging_golden_image(
            validator, untagging_golden_image_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_network_device_product_name_to_the_given_software_image(
    json_schema_validate, obj
):
    json_schema_validate("jsd_eb4a05f61e475ad0b9e74f963f27ea1d_v3_1_3_0").validate(obj)
    return True


def assign_network_device_product_name_to_the_given_software_image(api):
    endpoint_result = api.software_image_management_swim.assign_network_device_product_name_to_the_given_software_image(
        active_validation=True,
        image_id="string",
        payload=None,
        productNameOrdinal=0,
        siteIds=["string"],
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_assign_network_device_product_name_to_the_given_software_image(api, validator):
    try:
        assert is_valid_assign_network_device_product_name_to_the_given_software_image(
            validator,
            assign_network_device_product_name_to_the_given_software_image(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_network_device_product_name_to_the_given_software_image_default_val(api):
    endpoint_result = api.software_image_management_swim.assign_network_device_product_name_to_the_given_software_image(
        active_validation=True,
        image_id="string",
        payload=None,
        productNameOrdinal=None,
        siteIds=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_assign_network_device_product_name_to_the_given_software_image_default_val(
    api, validator
):
    try:
        assert is_valid_assign_network_device_product_name_to_the_given_software_image(
            validator,
            assign_network_device_product_name_to_the_given_software_image_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_network_device_product_names_assigned_to_a_software_image(
    json_schema_validate, obj
):
    json_schema_validate("jsd_fb538ce59b945302bfaf521c6794691e_v3_1_3_0").validate(obj)
    return True


def retrieves_network_device_product_names_assigned_to_a_software_image(api):
    endpoint_result = api.software_image_management_swim.retrieves_network_device_product_names_assigned_to_a_software_image(
        assigned="string",
        image_id="string",
        limit=0,
        offset=0,
        product_id="string",
        product_name="string",
        recommended="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieves_network_device_product_names_assigned_to_a_software_image(
    api, validator
):
    try:
        assert is_valid_retrieves_network_device_product_names_assigned_to_a_software_image(
            validator,
            retrieves_network_device_product_names_assigned_to_a_software_image(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_network_device_product_names_assigned_to_a_software_image_default_val(
    api,
):
    endpoint_result = api.software_image_management_swim.retrieves_network_device_product_names_assigned_to_a_software_image(
        assigned=None,
        image_id="string",
        limit=None,
        offset=None,
        product_id=None,
        product_name=None,
        recommended=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieves_network_device_product_names_assigned_to_a_software_image_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_network_device_product_names_assigned_to_a_software_image(
            validator,
            retrieves_network_device_product_names_assigned_to_a_software_image_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_assigned_network_device_products(
    json_schema_validate, obj
):
    json_schema_validate("jsd_febd252a9e4d5411bfbb98d538210ea3_v3_1_3_0").validate(obj)
    return True


def retrieves_the_count_of_assigned_network_device_products(api):
    endpoint_result = api.software_image_management_swim.retrieves_the_count_of_assigned_network_device_products(
        assigned="string",
        image_id="string",
        product_id="string",
        product_name="string",
        recommended="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieves_the_count_of_assigned_network_device_products(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_assigned_network_device_products(
            validator, retrieves_the_count_of_assigned_network_device_products(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_assigned_network_device_products_default_val(api):
    endpoint_result = api.software_image_management_swim.retrieves_the_count_of_assigned_network_device_products(
        assigned=None,
        image_id="string",
        product_id=None,
        product_name=None,
        recommended=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieves_the_count_of_assigned_network_device_products_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_count_of_assigned_network_device_products(
            validator,
            retrieves_the_count_of_assigned_network_device_products_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_unassign_network_device_product_name_from_the_given_software_image(
    json_schema_validate, obj
):
    json_schema_validate("jsd_1ecf7c4398475f279abe95abdf5500f2_v3_1_3_0").validate(obj)
    return True


def unassign_network_device_product_name_from_the_given_software_image(api):
    endpoint_result = api.software_image_management_swim.unassign_network_device_product_name_from_the_given_software_image(
        image_id="string", product_name_ordinal=0
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_unassign_network_device_product_name_from_the_given_software_image(
    api, validator
):
    try:
        assert (
            is_valid_unassign_network_device_product_name_from_the_given_software_image(
                validator,
                unassign_network_device_product_name_from_the_given_software_image(api),
            )
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def unassign_network_device_product_name_from_the_given_software_image_default_val(api):
    endpoint_result = api.software_image_management_swim.unassign_network_device_product_name_from_the_given_software_image(
        image_id="string", product_name_ordinal=0
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_unassign_network_device_product_name_from_the_given_software_image_default_val(
    api, validator
):
    try:
        assert is_valid_unassign_network_device_product_name_from_the_given_software_image(
            validator,
            unassign_network_device_product_name_from_the_given_software_image_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image(
    json_schema_validate, obj
):
    json_schema_validate("jsd_2c224ae3007d5486bbc5abb1f88e95e6_v3_1_3_0").validate(obj)
    return True


def update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image(
    api,
):
    endpoint_result = api.software_image_management_swim.update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image(
        active_validation=True,
        image_id="string",
        payload=None,
        product_name_ordinal=0,
        siteIds=["string"],
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image(
    api, validator
):
    try:
        assert is_valid_update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image(
            validator,
            update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image_default_val(
    api,
):
    endpoint_result = api.software_image_management_swim.update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image(
        active_validation=True,
        image_id="string",
        payload=None,
        product_name_ordinal=0,
        siteIds=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image_default_val(
    api, validator
):
    try:
        assert is_valid_update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image(
            validator,
            update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device_image_updates(json_schema_validate, obj):
    json_schema_validate("jsd_8581ab118a78541c9b7e3f3857d6d1f5_v3_1_3_0").validate(obj)
    return True


def get_network_device_image_updates(api):
    endpoint_result = (
        api.software_image_management_swim.get_network_device_image_updates(
            end_time=0,
            host_name="string",
            id="string",
            image_name="string",
            limit=0,
            management_address="string",
            network_device_id="string",
            offset=0,
            order="string",
            parent_id="string",
            sort_by="string",
            start_time=0,
            status="string",
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_network_device_image_updates(api, validator):
    try:
        assert is_valid_get_network_device_image_updates(
            validator, get_network_device_image_updates(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_device_image_updates_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.get_network_device_image_updates(
            end_time=None,
            host_name=None,
            id=None,
            image_name=None,
            limit=None,
            management_address=None,
            network_device_id=None,
            offset=None,
            order=None,
            parent_id=None,
            sort_by=None,
            start_time=None,
            status=None,
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_network_device_image_updates_default_val(api, validator):
    try:
        assert is_valid_get_network_device_image_updates(
            validator, get_network_device_image_updates_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_of_network_device_image_updates(json_schema_validate, obj):
    json_schema_validate("jsd_9138034de19e56c5aab0f9d10589871d_v3_1_3_0").validate(obj)
    return True


def count_of_network_device_image_updates(api):
    endpoint_result = (
        api.software_image_management_swim.count_of_network_device_image_updates(
            end_time=0,
            host_name="string",
            id="string",
            image_name="string",
            management_address="string",
            network_device_id="string",
            parent_id="string",
            start_time=0,
            status="string",
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_count_of_network_device_image_updates(api, validator):
    try:
        assert is_valid_count_of_network_device_image_updates(
            validator, count_of_network_device_image_updates(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_of_network_device_image_updates_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.count_of_network_device_image_updates(
            end_time=None,
            host_name=None,
            id=None,
            image_name=None,
            management_address=None,
            network_device_id=None,
            parent_id=None,
            start_time=None,
            status=None,
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_count_of_network_device_image_updates_default_val(api, validator):
    try:
        assert is_valid_count_of_network_device_image_updates(
            validator, count_of_network_device_image_updates_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_list_of_network_devices_with_image_details(
    json_schema_validate, obj
):
    json_schema_validate("jsd_079e39b6621058569039ee9a6e935145_v3_1_3_0").validate(obj)
    return True


def get_the_list_of_network_devices_with_image_details(api):
    endpoint_result = api.software_image_management_swim.get_the_list_of_network_devices_with_image_details(
        limit=0,
        management_address="string",
        network_device_image_status="string",
        network_device_update_status="string",
        offset=0,
        order="string",
        sort_by="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_the_list_of_network_devices_with_image_details(api, validator):
    try:
        assert is_valid_get_the_list_of_network_devices_with_image_details(
            validator, get_the_list_of_network_devices_with_image_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_list_of_network_devices_with_image_details_default_val(api):
    endpoint_result = api.software_image_management_swim.get_the_list_of_network_devices_with_image_details(
        limit=None,
        management_address=None,
        network_device_image_status=None,
        network_device_update_status=None,
        offset=None,
        order=None,
        sort_by=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_the_list_of_network_devices_with_image_details_default_val(api, validator):
    try:
        assert is_valid_get_the_list_of_network_devices_with_image_details(
            validator,
            get_the_list_of_network_devices_with_image_details_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_update_images_on_network_devices(json_schema_validate, obj):
    json_schema_validate("jsd_197f21b7552158e889b51d0c109c15db_v3_1_3_0").validate(obj)
    return True


def bulk_update_images_on_network_devices(api):
    endpoint_result = (
        api.software_image_management_swim.bulk_update_images_on_network_devices(
            active_validation=True, payload=None
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_bulk_update_images_on_network_devices(api, validator):
    try:
        assert is_valid_bulk_update_images_on_network_devices(
            validator, bulk_update_images_on_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def bulk_update_images_on_network_devices_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.bulk_update_images_on_network_devices(
            active_validation=True, payload=None
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_bulk_update_images_on_network_devices_default_val(api, validator):
    try:
        assert is_valid_bulk_update_images_on_network_devices(
            validator, bulk_update_images_on_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_of_network_devices_for_the_given_status_filters(
    json_schema_validate, obj
):
    json_schema_validate("jsd_1eb5a6c6193a58ed9624f466a3e90bc4_v3_1_3_0").validate(obj)
    return True


def count_of_network_devices_for_the_given_status_filters(api):
    endpoint_result = api.software_image_management_swim.count_of_network_devices_for_the_given_status_filters(
        management_address="string",
        network_device_image_status="string",
        network_device_update_status="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_count_of_network_devices_for_the_given_status_filters(api, validator):
    try:
        assert is_valid_count_of_network_devices_for_the_given_status_filters(
            validator, count_of_network_devices_for_the_given_status_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_of_network_devices_for_the_given_status_filters_default_val(api):
    endpoint_result = api.software_image_management_swim.count_of_network_devices_for_the_given_status_filters(
        management_address=None,
        network_device_image_status=None,
        network_device_update_status=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_count_of_network_devices_for_the_given_status_filters_default_val(
    api, validator
):
    try:
        assert is_valid_count_of_network_devices_for_the_given_status_filters(
            validator,
            count_of_network_devices_for_the_given_status_filters_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_distribute_images_on_network_devices(json_schema_validate, obj):
    json_schema_validate("jsd_c1fa19f9295c50018132c6c9ebc3fc35_v3_1_3_0").validate(obj)
    return True


def bulk_distribute_images_on_network_devices(api):
    endpoint_result = (
        api.software_image_management_swim.bulk_distribute_images_on_network_devices(
            active_validation=True, payload=None
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_bulk_distribute_images_on_network_devices(api, validator):
    try:
        assert is_valid_bulk_distribute_images_on_network_devices(
            validator, bulk_distribute_images_on_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def bulk_distribute_images_on_network_devices_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.bulk_distribute_images_on_network_devices(
            active_validation=True, payload=None
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_bulk_distribute_images_on_network_devices_default_val(api, validator):
    try:
        assert is_valid_bulk_distribute_images_on_network_devices(
            validator, bulk_distribute_images_on_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_network_device_image_update_validation_results(json_schema_validate, obj):
    json_schema_validate("jsd_ef43a0018635536f9208b408a799c844_v3_1_3_0").validate(obj)
    return True


def network_device_image_update_validation_results(api):
    endpoint_result = api.software_image_management_swim.network_device_image_update_validation_results(
        id="string",
        limit=0,
        network_device_id="string",
        offset=0,
        operation_type="string",
        order="string",
        sort_by="string",
        status="string",
        type="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_network_device_image_update_validation_results(api, validator):
    try:
        assert is_valid_network_device_image_update_validation_results(
            validator, network_device_image_update_validation_results(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def network_device_image_update_validation_results_default_val(api):
    endpoint_result = api.software_image_management_swim.network_device_image_update_validation_results(
        id=None,
        limit=None,
        network_device_id=None,
        offset=None,
        operation_type=None,
        order=None,
        sort_by=None,
        status=None,
        type=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_network_device_image_update_validation_results_default_val(api, validator):
    try:
        assert is_valid_network_device_image_update_validation_results(
            validator, network_device_image_update_validation_results_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_of_network_device_image_update_validation_results(
    json_schema_validate, obj
):
    json_schema_validate("jsd_daeb0e5e463d553fa456fe8500a132ba_v3_1_3_0").validate(obj)
    return True


def count_of_network_device_image_update_validation_results(api):
    endpoint_result = api.software_image_management_swim.count_of_network_device_image_update_validation_results(
        network_device_id="string",
        operation_type="string",
        status="string",
        type="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_count_of_network_device_image_update_validation_results(api, validator):
    try:
        assert is_valid_count_of_network_device_image_update_validation_results(
            validator, count_of_network_device_image_update_validation_results(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_of_network_device_image_update_validation_results_default_val(api):
    endpoint_result = api.software_image_management_swim.count_of_network_device_image_update_validation_results(
        network_device_id=None, operation_type=None, status=None, type=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_count_of_network_device_image_update_validation_results_default_val(
    api, validator
):
    try:
        assert is_valid_count_of_network_device_image_update_validation_results(
            validator,
            count_of_network_device_image_update_validation_results_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_custom_network_device_validation(json_schema_validate, obj):
    json_schema_validate("jsd_1ca519342eb25dfcaf15f8f44baf0ee0_v3_1_3_0").validate(obj)
    return True


def create_custom_network_device_validation(api):
    endpoint_result = (
        api.software_image_management_swim.create_custom_network_device_validation(
            active_validation=True,
            cli="string",
            description="string",
            name="string",
            operationType="string",
            payload=None,
            productSeriesOrdinals=[0],
            type="string",
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_create_custom_network_device_validation(api, validator):
    try:
        assert is_valid_create_custom_network_device_validation(
            validator, create_custom_network_device_validation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_custom_network_device_validation_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.create_custom_network_device_validation(
            active_validation=True,
            cli=None,
            description=None,
            name=None,
            operationType=None,
            payload=None,
            productSeriesOrdinals=None,
            type=None,
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_create_custom_network_device_validation_default_val(api, validator):
    try:
        assert is_valid_create_custom_network_device_validation(
            validator, create_custom_network_device_validation_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_list_of_custom_network_device_validations(
    json_schema_validate, obj
):
    json_schema_validate("jsd_c38b9dd078265df3a306553baf0e064c_v3_1_3_0").validate(obj)
    return True


def get_the_list_of_custom_network_device_validations(api):
    endpoint_result = api.software_image_management_swim.get_the_list_of_custom_network_device_validations(
        limit=0,
        offset=0,
        operation_type="string",
        order="string",
        product_series_ordinal=0,
        type="string",
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_the_list_of_custom_network_device_validations(api, validator):
    try:
        assert is_valid_get_the_list_of_custom_network_device_validations(
            validator, get_the_list_of_custom_network_device_validations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_list_of_custom_network_device_validations_default_val(api):
    endpoint_result = api.software_image_management_swim.get_the_list_of_custom_network_device_validations(
        limit=None,
        offset=None,
        operation_type=None,
        order=None,
        product_series_ordinal=None,
        type=None,
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_the_list_of_custom_network_device_validations_default_val(api, validator):
    try:
        assert is_valid_get_the_list_of_custom_network_device_validations(
            validator,
            get_the_list_of_custom_network_device_validations_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_of_custom_network_device_validations(json_schema_validate, obj):
    json_schema_validate("jsd_044b2a0b2686505a9148599e9c52837f_v3_1_3_0").validate(obj)
    return True


def count_of_custom_network_device_validations(api):
    endpoint_result = (
        api.software_image_management_swim.count_of_custom_network_device_validations(
            operation_type="string", product_series_ordinal=0, type="string"
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_count_of_custom_network_device_validations(api, validator):
    try:
        assert is_valid_count_of_custom_network_device_validations(
            validator, count_of_custom_network_device_validations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_of_custom_network_device_validations_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.count_of_custom_network_device_validations(
            operation_type=None, product_series_ordinal=None, type=None
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_count_of_custom_network_device_validations_default_val(api, validator):
    try:
        assert is_valid_count_of_custom_network_device_validations(
            validator, count_of_custom_network_device_validations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_custom_network_device_validation(json_schema_validate, obj):
    json_schema_validate("jsd_908cf0f416ef5c25a159f4c3e376741a_v3_1_3_0").validate(obj)
    return True


def update_custom_network_device_validation(api):
    endpoint_result = (
        api.software_image_management_swim.update_custom_network_device_validation(
            active_validation=True,
            cli="string",
            description="string",
            id="string",
            payload=None,
            productSeriesOrdinals=[0],
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_update_custom_network_device_validation(api, validator):
    try:
        assert is_valid_update_custom_network_device_validation(
            validator, update_custom_network_device_validation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_custom_network_device_validation_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.update_custom_network_device_validation(
            active_validation=True,
            cli=None,
            description=None,
            id="string",
            payload=None,
            productSeriesOrdinals=None,
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_update_custom_network_device_validation_default_val(api, validator):
    try:
        assert is_valid_update_custom_network_device_validation(
            validator, update_custom_network_device_validation_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_custom_network_device_validation_details(json_schema_validate, obj):
    json_schema_validate("jsd_d0a1ee8bf91f567d863552a06fb37885_v3_1_3_0").validate(obj)
    return True


def get_custom_network_device_validation_details(api):
    endpoint_result = (
        api.software_image_management_swim.get_custom_network_device_validation_details(
            id="string"
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_custom_network_device_validation_details(api, validator):
    try:
        assert is_valid_get_custom_network_device_validation_details(
            validator, get_custom_network_device_validation_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_custom_network_device_validation_details_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.get_custom_network_device_validation_details(
            id="string"
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_custom_network_device_validation_details_default_val(api, validator):
    try:
        assert is_valid_get_custom_network_device_validation_details(
            validator, get_custom_network_device_validation_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_custom_network_device_validation(json_schema_validate, obj):
    json_schema_validate("jsd_f3847fd15d8d5299ada781bab2e084f9_v3_1_3_0").validate(obj)
    return True


def delete_custom_network_device_validation(api):
    endpoint_result = (
        api.software_image_management_swim.delete_custom_network_device_validation(
            id="string"
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_delete_custom_network_device_validation(api, validator):
    try:
        assert is_valid_delete_custom_network_device_validation(
            validator, delete_custom_network_device_validation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_custom_network_device_validation_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.delete_custom_network_device_validation(
            id="string"
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_delete_custom_network_device_validation_default_val(api, validator):
    try:
        assert is_valid_delete_custom_network_device_validation(
            validator, delete_custom_network_device_validation_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_fetch_network_device_with_image_details(json_schema_validate, obj):
    json_schema_validate("jsd_f34cbcb416c95e4bbc7898768716a018_v3_1_3_0").validate(obj)
    return True


def fetch_network_device_with_image_details(api):
    endpoint_result = (
        api.software_image_management_swim.fetch_network_device_with_image_details(
            id="string"
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_fetch_network_device_with_image_details(api, validator):
    try:
        assert is_valid_fetch_network_device_with_image_details(
            validator, fetch_network_device_with_image_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def fetch_network_device_with_image_details_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.fetch_network_device_with_image_details(
            id="string"
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_fetch_network_device_with_image_details_default_val(api, validator):
    try:
        assert is_valid_fetch_network_device_with_image_details(
            validator, fetch_network_device_with_image_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_images_on_the_network_device(json_schema_validate, obj):
    json_schema_validate("jsd_02402cd9d7d858f094469abf9464431f_v3_1_3_0").validate(obj)
    return True


def update_images_on_the_network_device(api):
    endpoint_result = (
        api.software_image_management_swim.update_images_on_the_network_device(
            active_validation=True,
            compatibleFeatures=[{"key": "string", "value": "string"}],
            id="string",
            installedImages=[{"id": "string"}],
            networkValidationIds=["string"],
            payload=None,
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_update_images_on_the_network_device(api, validator):
    try:
        assert is_valid_update_images_on_the_network_device(
            validator, update_images_on_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_images_on_the_network_device_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.update_images_on_the_network_device(
            active_validation=True,
            compatibleFeatures=None,
            id="string",
            installedImages=None,
            networkValidationIds=None,
            payload=None,
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_update_images_on_the_network_device_default_val(api, validator):
    try:
        assert is_valid_update_images_on_the_network_device(
            validator, update_images_on_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_distribute_images_on_the_network_device(json_schema_validate, obj):
    json_schema_validate("jsd_a914cc0c96a35a06a54856e778742a8c_v3_1_3_0").validate(obj)
    return True


def distribute_images_on_the_network_device(api):
    endpoint_result = (
        api.software_image_management_swim.distribute_images_on_the_network_device(
            active_validation=True,
            distributedImages=[{"id": "string"}],
            id="string",
            networkValidationIds=["string"],
            payload=None,
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_distribute_images_on_the_network_device(api, validator):
    try:
        assert is_valid_distribute_images_on_the_network_device(
            validator, distribute_images_on_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def distribute_images_on_the_network_device_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.distribute_images_on_the_network_device(
            active_validation=True,
            distributedImages=None,
            id="string",
            networkValidationIds=None,
            payload=None,
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_distribute_images_on_the_network_device_default_val(api, validator):
    try:
        assert is_valid_distribute_images_on_the_network_device(
            validator, distribute_images_on_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_trigger_update_readiness_for_network_device(json_schema_validate, obj):
    json_schema_validate("jsd_0a6ad169a14d54c6b6d0111c7b38e69d_v3_1_3_0").validate(obj)
    return True


def trigger_update_readiness_for_network_device(api):
    endpoint_result = (
        api.software_image_management_swim.trigger_update_readiness_for_network_device(
            active_validation=True, id="string", payload=None
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_trigger_update_readiness_for_network_device(api, validator):
    try:
        assert is_valid_trigger_update_readiness_for_network_device(
            validator, trigger_update_readiness_for_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def trigger_update_readiness_for_network_device_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.trigger_update_readiness_for_network_device(
            active_validation=True, id="string", payload=None
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_trigger_update_readiness_for_network_device_default_val(api, validator):
    try:
        assert is_valid_trigger_update_readiness_for_network_device(
            validator, trigger_update_readiness_for_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_network_device_product_names(
    json_schema_validate, obj
):
    json_schema_validate("jsd_73b13b416b145acba7f74764f49364cd_v3_1_3_0").validate(obj)
    return True


def retrieves_the_list_of_network_device_product_names(api):
    endpoint_result = api.software_image_management_swim.retrieves_the_list_of_network_device_product_names(
        limit=0, offset=0, product_id="string", product_name="string"
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieves_the_list_of_network_device_product_names(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_network_device_product_names(
            validator, retrieves_the_list_of_network_device_product_names(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_network_device_product_names_default_val(api):
    endpoint_result = api.software_image_management_swim.retrieves_the_list_of_network_device_product_names(
        limit=None, offset=None, product_id=None, product_name=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieves_the_list_of_network_device_product_names_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_network_device_product_names(
            validator,
            retrieves_the_list_of_network_device_product_names_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_of_network_product_names(json_schema_validate, obj):
    json_schema_validate("jsd_09f933fdff7c5744a163227040d0367b_v3_1_3_0").validate(obj)
    return True


def count_of_network_product_names(api):
    endpoint_result = api.software_image_management_swim.count_of_network_product_names(
        product_id="string", product_name="string"
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_count_of_network_product_names(api, validator):
    try:
        assert is_valid_count_of_network_product_names(
            validator, count_of_network_product_names(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_of_network_product_names_default_val(api):
    endpoint_result = api.software_image_management_swim.count_of_network_product_names(
        product_id=None, product_name=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_count_of_network_product_names_default_val(api, validator):
    try:
        assert is_valid_count_of_network_product_names(
            validator, count_of_network_product_names_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_network_device_product_name(json_schema_validate, obj):
    json_schema_validate("jsd_a6c00bdb02675408b8f0fb0107dcb7ed_v3_1_3_0").validate(obj)
    return True


def retrieve_network_device_product_name(api):
    endpoint_result = (
        api.software_image_management_swim.retrieve_network_device_product_name(
            product_name_ordinal=0
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieve_network_device_product_name(api, validator):
    try:
        assert is_valid_retrieve_network_device_product_name(
            validator, retrieve_network_device_product_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_network_device_product_name_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.retrieve_network_device_product_name(
            product_name_ordinal=0
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieve_network_device_product_name_default_val(api, validator):
    try:
        assert is_valid_retrieve_network_device_product_name(
            validator, retrieve_network_device_product_name_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_network_device_product_series(
    json_schema_validate, obj
):
    json_schema_validate("jsd_a5801264fcc15304be778491a0d356f9_v3_1_3_0").validate(obj)
    return True


def retrieves_the_list_of_network_device_product_series(api):
    endpoint_result = api.software_image_management_swim.retrieves_the_list_of_network_device_product_series(
        limit=0, name="string", offset=0
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieves_the_list_of_network_device_product_series(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_network_device_product_series(
            validator, retrieves_the_list_of_network_device_product_series(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_network_device_product_series_default_val(api):
    endpoint_result = api.software_image_management_swim.retrieves_the_list_of_network_device_product_series(
        limit=None, name=None, offset=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieves_the_list_of_network_device_product_series_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_network_device_product_series(
            validator,
            retrieves_the_list_of_network_device_product_series_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_of_network_product_series(json_schema_validate, obj):
    json_schema_validate("jsd_ae3f664755d35cbfa22f54ab07fda9e8_v3_1_3_0").validate(obj)
    return True


def count_of_network_product_series(api):
    endpoint_result = (
        api.software_image_management_swim.count_of_network_product_series(
            name="string"
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_count_of_network_product_series(api, validator):
    try:
        assert is_valid_count_of_network_product_series(
            validator, count_of_network_product_series(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_of_network_product_series_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.count_of_network_product_series(name=None)
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_count_of_network_product_series_default_val(api, validator):
    try:
        assert is_valid_count_of_network_product_series(
            validator, count_of_network_product_series_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_network_device_product_series(json_schema_validate, obj):
    json_schema_validate("jsd_e96f4748798d55d2a9257675107b7d7d_v3_1_3_0").validate(obj)
    return True


def retrieve_network_device_product_series(api):
    endpoint_result = (
        api.software_image_management_swim.retrieve_network_device_product_series(
            product_series_ordinal=0
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieve_network_device_product_series(api, validator):
    try:
        assert is_valid_retrieve_network_device_product_series(
            validator, retrieve_network_device_product_series(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_network_device_product_series_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.retrieve_network_device_product_series(
            product_series_ordinal=0
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_retrieve_network_device_product_series_default_val(api, validator):
    try:
        assert is_valid_retrieve_network_device_product_series(
            validator, retrieve_network_device_product_series_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_returns_the_image_summary_for_the_given_site(json_schema_validate, obj):
    json_schema_validate("jsd_a2a643a99f01589ca0e12920ac5b257d_v3_1_3_0").validate(obj)
    return True


def returns_the_image_summary_for_the_given_site(api):
    endpoint_result = (
        api.software_image_management_swim.returns_the_image_summary_for_the_given_site(
            site_id="string"
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_returns_the_image_summary_for_the_given_site(api, validator):
    try:
        assert is_valid_returns_the_image_summary_for_the_given_site(
            validator, returns_the_image_summary_for_the_given_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def returns_the_image_summary_for_the_given_site_default_val(api):
    endpoint_result = (
        api.software_image_management_swim.returns_the_image_summary_for_the_given_site(
            site_id=None
        )
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_returns_the_image_summary_for_the_given_site_default_val(api, validator):
    try:
        assert is_valid_returns_the_image_summary_for_the_given_site(
            validator, returns_the_image_summary_for_the_given_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_returns_network_device_product_names_for_a_site(json_schema_validate, obj):
    json_schema_validate("jsd_9293a2ca9a4f55d0b44d7041186b9bab_v3_1_3_0").validate(obj)
    return True


def returns_network_device_product_names_for_a_site(api):
    endpoint_result = api.software_image_management_swim.returns_network_device_product_names_for_a_site(
        limit=0, offset=0, product_name="string", site_id="string"
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_returns_network_device_product_names_for_a_site(api, validator):
    try:
        assert is_valid_returns_network_device_product_names_for_a_site(
            validator, returns_network_device_product_names_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def returns_network_device_product_names_for_a_site_default_val(api):
    endpoint_result = api.software_image_management_swim.returns_network_device_product_names_for_a_site(
        limit=None, offset=None, product_name=None, site_id=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_returns_network_device_product_names_for_a_site_default_val(api, validator):
    try:
        assert is_valid_returns_network_device_product_names_for_a_site(
            validator, returns_network_device_product_names_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_returns_the_count_of_network_device_product_names_for_a_site(
    json_schema_validate, obj
):
    json_schema_validate("jsd_241ade3fee0a5a8eb0a7ced03126d560_v3_1_3_0").validate(obj)
    return True


def returns_the_count_of_network_device_product_names_for_a_site(api):
    endpoint_result = api.software_image_management_swim.returns_the_count_of_network_device_product_names_for_a_site(
        product_name="string", site_id="string"
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_returns_the_count_of_network_device_product_names_for_a_site(api, validator):
    try:
        assert is_valid_returns_the_count_of_network_device_product_names_for_a_site(
            validator, returns_the_count_of_network_device_product_names_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def returns_the_count_of_network_device_product_names_for_a_site_default_val(api):
    endpoint_result = api.software_image_management_swim.returns_the_count_of_network_device_product_names_for_a_site(
        product_name=None, site_id=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_returns_the_count_of_network_device_product_names_for_a_site_default_val(
    api, validator
):
    try:
        assert is_valid_returns_the_count_of_network_device_product_names_for_a_site(
            validator,
            returns_the_count_of_network_device_product_names_for_a_site_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

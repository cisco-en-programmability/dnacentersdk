# -*- coding: utf-8 -*-
"""DNACenterAPI software_image_management_swim API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.3', reason='version does not match')


def is_valid_trigger_software_image_activation(json_schema_validate, obj):
    json_schema_validate('jsd_22891a9136d5513985f15e91a19da66c_v2_3_7_3').validate(obj)
    return True


def trigger_software_image_activation(api):
    endpoint_result = api.software_image_management_swim.trigger_software_image_activation(
        active_validation=True,
        payload=None,
        schedule_validate=True
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_trigger_software_image_activation(api, validator):
    try:
        assert is_valid_trigger_software_image_activation(
            validator,
            trigger_software_image_activation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def trigger_software_image_activation_default_val(api):
    endpoint_result = api.software_image_management_swim.trigger_software_image_activation(
        active_validation=True,
        payload=None,
        schedule_validate=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_trigger_software_image_activation_default_val(api, validator):
    try:
        assert is_valid_trigger_software_image_activation(
            validator,
            trigger_software_image_activation_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_trigger_software_image_distribution(json_schema_validate, obj):
    json_schema_validate('jsd_6c8d11fb9fc752ab8bb8e2b1413ccc92_v2_3_7_3').validate(obj)
    return True


def trigger_software_image_distribution(api):
    endpoint_result = api.software_image_management_swim.trigger_software_image_distribution(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_trigger_software_image_distribution(api, validator):
    try:
        assert is_valid_trigger_software_image_distribution(
            validator,
            trigger_software_image_distribution(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def trigger_software_image_distribution_default_val(api):
    endpoint_result = api.software_image_management_swim.trigger_software_image_distribution(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_trigger_software_image_distribution_default_val(api, validator):
    try:
        assert is_valid_trigger_software_image_distribution(
            validator,
            trigger_software_image_distribution_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_software_image_details(json_schema_validate, obj):
    json_schema_validate('jsd_039f73101d5d5e409f571084ab4c6049_v2_3_7_3').validate(obj)
    return True


def get_software_image_details(api):
    endpoint_result = api.software_image_management_swim.get_software_image_details(
        application_type='string',
        created_time=0,
        family='string',
        image_integrity_status='string',
        image_name='string',
        image_series='string',
        image_size_greater_than=0,
        image_size_lesser_than=0,
        image_uuid='string',
        is_cco_latest=True,
        is_cco_recommended=True,
        is_tagged_golden=True,
        limit=0,
        name='string',
        offset=0,
        sort_by='string',
        sort_order='string',
        version='string'
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_software_image_details(api, validator):
    try:
        assert is_valid_get_software_image_details(
            validator,
            get_software_image_details(api)
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
        version=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_software_image_details_default_val(api, validator):
    try:
        assert is_valid_get_software_image_details(
            validator,
            get_software_image_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_family_identifiers(json_schema_validate, obj):
    json_schema_validate('jsd_b5c47f316ff058eb979bdea047f9d5b5_v2_3_7_3').validate(obj)
    return True


def get_device_family_identifiers(api):
    endpoint_result = api.software_image_management_swim.get_device_family_identifiers(

    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_device_family_identifiers(api, validator):
    try:
        assert is_valid_get_device_family_identifiers(
            validator,
            get_device_family_identifiers(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_family_identifiers_default_val(api):
    endpoint_result = api.software_image_management_swim.get_device_family_identifiers(

    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_device_family_identifiers_default_val(api, validator):
    try:
        assert is_valid_get_device_family_identifiers(
            validator,
            get_device_family_identifiers_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_tag_as_golden_image(json_schema_validate, obj):
    json_schema_validate('jsd_a9b864257b965fe4bd8b0293f41f1537_v2_3_7_3').validate(obj)
    return True


def tag_as_golden_image(api):
    endpoint_result = api.software_image_management_swim.tag_as_golden_image(
        active_validation=True,
        deviceFamilyIdentifier='string',
        deviceRole='string',
        imageId='string',
        payload=None,
        siteId='string'
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_tag_as_golden_image(api, validator):
    try:
        assert is_valid_tag_as_golden_image(
            validator,
            tag_as_golden_image(api)
        )
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
        siteId=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_tag_as_golden_image_default_val(api, validator):
    try:
        assert is_valid_tag_as_golden_image(
            validator,
            tag_as_golden_image_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_golden_tag_for_image(json_schema_validate, obj):
    json_schema_validate('jsd_2405e9dd960c5378ab442f235c8135d0_v2_3_7_3').validate(obj)
    return True


def remove_golden_tag_for_image(api):
    endpoint_result = api.software_image_management_swim.remove_golden_tag_for_image(
        device_family_identifier='string',
        device_role='string',
        image_id='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_remove_golden_tag_for_image(api, validator):
    try:
        assert is_valid_remove_golden_tag_for_image(
            validator,
            remove_golden_tag_for_image(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def remove_golden_tag_for_image_default_val(api):
    endpoint_result = api.software_image_management_swim.remove_golden_tag_for_image(
        device_family_identifier='string',
        device_role='string',
        image_id='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_remove_golden_tag_for_image_default_val(api, validator):
    try:
        assert is_valid_remove_golden_tag_for_image(
            validator,
            remove_golden_tag_for_image_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_golden_tag_status_of_an_image(json_schema_validate, obj):
    json_schema_validate('jsd_97ab6266cac654d394cf943a161fcc7b_v2_3_7_3').validate(obj)
    return True


def get_golden_tag_status_of_an_image(api):
    endpoint_result = api.software_image_management_swim.get_golden_tag_status_of_an_image(
        device_family_identifier='string',
        device_role='string',
        image_id='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_golden_tag_status_of_an_image(api, validator):
    try:
        assert is_valid_get_golden_tag_status_of_an_image(
            validator,
            get_golden_tag_status_of_an_image(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_golden_tag_status_of_an_image_default_val(api):
    endpoint_result = api.software_image_management_swim.get_golden_tag_status_of_an_image(
        device_family_identifier='string',
        device_role='string',
        image_id='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_get_golden_tag_status_of_an_image_default_val(api, validator):
    try:
        assert is_valid_get_golden_tag_status_of_an_image(
            validator,
            get_golden_tag_status_of_an_image_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_local_software_image(json_schema_validate, obj):
    json_schema_validate('jsd_2399c1cf6d5d5f0fa2e92539134b6c1d_v2_3_7_3').validate(obj)
    return True


def import_local_software_image(api):
    endpoint_result = api.software_image_management_swim.import_local_software_image(
        multipart_fields={'file': ('test-1592357065255.csv', open('./tests/test-1592357065255.csv', 'rb'))},
        multipart_monitor_callback=None,
        active_validation=True,
        is_third_party=True,
        payload=None,
        third_party_application_type='string',
        third_party_image_family='string',
        third_party_vendor='string'
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_import_local_software_image(api, validator):
    try:
        assert is_valid_import_local_software_image(
            validator,
            import_local_software_image(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_local_software_image_default_val(api):
    endpoint_result = api.software_image_management_swim.import_local_software_image(
        multipart_fields={'file': ('test-1592357065255.csv', open('./tests/test-1592357065255.csv', 'rb'))},
        multipart_monitor_callback=None,
        active_validation=True,
        is_third_party=None,
        payload=None,
        third_party_application_type=None,
        third_party_image_family=None,
        third_party_vendor=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_import_local_software_image_default_val(api, validator):
    try:
        assert is_valid_import_local_software_image(
            validator,
            import_local_software_image_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_software_image_via_url(json_schema_validate, obj):
    json_schema_validate('jsd_7be8cdb967555fcca03a4c1f796eee56_v2_3_7_3').validate(obj)
    return True


def import_software_image_via_url(api):
    endpoint_result = api.software_image_management_swim.import_software_image_via_url(
        active_validation=True,
        payload=None,
        schedule_at='string',
        schedule_desc='string',
        schedule_origin='string'
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_import_software_image_via_url(api, validator):
    try:
        assert is_valid_import_software_image_via_url(
            validator,
            import_software_image_via_url(api)
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
        schedule_origin=None
    )
    return endpoint_result


@pytest.mark.software_image_management_swim
def test_import_software_image_via_url_default_val(api, validator):
    try:
        assert is_valid_import_software_image_via_url(
            validator,
            import_software_image_via_url_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

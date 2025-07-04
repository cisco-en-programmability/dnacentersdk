# -*- coding: utf-8 -*-
"""DNACenterAPI licenses API fixtures and tests.

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

pytestmark = pytest.mark.skipif(
    DNA_CENTER_VERSION != "2.3.5.3", reason="version does not match"
)


def is_valid_device_count_details2(json_schema_validate, obj):
    json_schema_validate("jsd_87c0cf04bdc758b29bb11abbdacbd921_v2_3_5_3").validate(obj)
    return True


def device_count_details2(api):
    endpoint_result = api.licenses.device_count_details2(
        device_type="string",
        dna_level="string",
        registration_status="string",
        smart_account_id="string",
        virtual_account_name="string",
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_count_details2(api, validator):
    try:
        assert is_valid_device_count_details2(validator, device_count_details2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_count_details2_default_val(api):
    endpoint_result = api.licenses.device_count_details2(
        device_type=None,
        dna_level=None,
        registration_status=None,
        smart_account_id=None,
        virtual_account_name=None,
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_count_details2_default_val(api, validator):
    try:
        assert is_valid_device_count_details2(
            validator, device_count_details2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_device_license_summary2(json_schema_validate, obj):
    json_schema_validate("jsd_f4ba64eef4085d518a612835e128fe3c_v2_3_5_3").validate(obj)
    return True


def device_license_summary2(api):
    endpoint_result = api.licenses.device_license_summary2(
        device_type="string",
        device_uuid="string",
        dna_level="string",
        limit=0,
        order="string",
        page_number=0,
        registration_status="string",
        smart_account_id=0,
        sort_by="string",
        virtual_account_name="string",
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_license_summary2(api, validator):
    try:
        assert is_valid_device_license_summary2(validator, device_license_summary2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_license_summary2_default_val(api):
    endpoint_result = api.licenses.device_license_summary2(
        device_type=None,
        device_uuid=None,
        dna_level=None,
        limit=None,
        order=None,
        page_number=None,
        registration_status=None,
        smart_account_id=None,
        sort_by=None,
        virtual_account_name=None,
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_license_summary2_default_val(api, validator):
    try:
        assert is_valid_device_license_summary2(
            validator, device_license_summary2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_device_license_details2(json_schema_validate, obj):
    json_schema_validate("jsd_6f04f865c01d5c17a5f0cb5abe620dd8_v2_3_5_3").validate(obj)
    return True


def device_license_details2(api):
    endpoint_result = api.licenses.device_license_details2(device_uuid="string")
    return endpoint_result


@pytest.mark.licenses
def test_device_license_details2(api, validator):
    try:
        assert is_valid_device_license_details2(validator, device_license_details2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_license_details2_default_val(api):
    endpoint_result = api.licenses.device_license_details2(device_uuid="string")
    return endpoint_result


@pytest.mark.licenses
def test_device_license_details2_default_val(api, validator):
    try:
        assert is_valid_device_license_details2(
            validator, device_license_details2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_device_deregistration2(json_schema_validate, obj):
    json_schema_validate("jsd_0109b2f15d0c54c2862a60a904289ddd_v2_3_5_3").validate(obj)
    return True


def device_deregistration2(api):
    endpoint_result = api.licenses.device_deregistration2(
        active_validation=True, device_uuids=["string"], payload=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_deregistration2(api, validator):
    try:
        assert is_valid_device_deregistration2(validator, device_deregistration2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_deregistration2_default_val(api):
    endpoint_result = api.licenses.device_deregistration2(
        active_validation=True, device_uuids=None, payload=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_deregistration2_default_val(api, validator):
    try:
        assert is_valid_device_deregistration2(
            validator, device_deregistration2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_device_registration2(json_schema_validate, obj):
    json_schema_validate("jsd_df26f516755a50b5b5477324cf5cb649_v2_3_5_3").validate(obj)
    return True


def device_registration2(api):
    endpoint_result = api.licenses.device_registration2(
        active_validation=True,
        device_uuids=["string"],
        payload=None,
        virtual_account_name="string",
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_registration2(api, validator):
    try:
        assert is_valid_device_registration2(validator, device_registration2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_registration2_default_val(api):
    endpoint_result = api.licenses.device_registration2(
        active_validation=True,
        device_uuids=None,
        payload=None,
        virtual_account_name="string",
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_registration2_default_val(api, validator):
    try:
        assert is_valid_device_registration2(
            validator, device_registration2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_change_virtual_account2(json_schema_validate, obj):
    json_schema_validate("jsd_4bd5b507f58a50aab614e3d7409eec4c_v2_3_5_3").validate(obj)
    return True


def change_virtual_account2(api):
    endpoint_result = api.licenses.change_virtual_account2(
        active_validation=True,
        device_uuids=["string"],
        payload=None,
        smart_account_id="string",
        virtual_account_name="string",
    )
    return endpoint_result


@pytest.mark.licenses
def test_change_virtual_account2(api, validator):
    try:
        assert is_valid_change_virtual_account2(validator, change_virtual_account2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def change_virtual_account2_default_val(api):
    endpoint_result = api.licenses.change_virtual_account2(
        active_validation=True,
        device_uuids=None,
        payload=None,
        smart_account_id="string",
        virtual_account_name="string",
    )
    return endpoint_result


@pytest.mark.licenses
def test_change_virtual_account2_default_val(api, validator):
    try:
        assert is_valid_change_virtual_account2(
            validator, change_virtual_account2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_virtual_account_details2(json_schema_validate, obj):
    json_schema_validate("jsd_8ab450b197375fa9bcd95219113a3075_v2_3_5_3").validate(obj)
    return True


def virtual_account_details2(api):
    endpoint_result = api.licenses.virtual_account_details2(smart_account_id="string")
    return endpoint_result


@pytest.mark.licenses
def test_virtual_account_details2(api, validator):
    try:
        assert is_valid_virtual_account_details2(
            validator, virtual_account_details2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def virtual_account_details2_default_val(api):
    endpoint_result = api.licenses.virtual_account_details2(smart_account_id="string")
    return endpoint_result


@pytest.mark.licenses
def test_virtual_account_details2_default_val(api, validator):
    try:
        assert is_valid_virtual_account_details2(
            validator, virtual_account_details2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_smart_account_details(json_schema_validate, obj):
    json_schema_validate("jsd_ea3fdbde23325051a76b9d062c2962a0_v2_3_5_3").validate(obj)
    return True


def smart_account_details(api):
    endpoint_result = api.licenses.smart_account_details()
    return endpoint_result


@pytest.mark.licenses
def test_smart_account_details(api, validator):
    try:
        assert is_valid_smart_account_details(validator, smart_account_details(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def smart_account_details_default_val(api):
    endpoint_result = api.licenses.smart_account_details()
    return endpoint_result


@pytest.mark.licenses
def test_smart_account_details_default_val(api, validator):
    try:
        assert is_valid_smart_account_details(
            validator, smart_account_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_license_term_details2(json_schema_validate, obj):
    json_schema_validate("jsd_df2d278e89b45c8ea0ca0a945c001f08_v2_3_5_3").validate(obj)
    return True


def license_term_details2(api):
    endpoint_result = api.licenses.license_term_details2(
        device_type="string", smart_account_id="string", virtual_account_name="string"
    )
    return endpoint_result


@pytest.mark.licenses
def test_license_term_details2(api, validator):
    try:
        assert is_valid_license_term_details2(validator, license_term_details2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def license_term_details2_default_val(api):
    endpoint_result = api.licenses.license_term_details2(
        device_type=None, smart_account_id="string", virtual_account_name="string"
    )
    return endpoint_result


@pytest.mark.licenses
def test_license_term_details2_default_val(api, validator):
    try:
        assert is_valid_license_term_details2(
            validator, license_term_details2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_license_usage_details2(json_schema_validate, obj):
    json_schema_validate("jsd_46e55ecbbda454c6a01d905e6f4cce16_v2_3_5_3").validate(obj)
    return True


def license_usage_details2(api):
    endpoint_result = api.licenses.license_usage_details2(
        device_type="string", smart_account_id="string", virtual_account_name="string"
    )
    return endpoint_result


@pytest.mark.licenses
def test_license_usage_details2(api, validator):
    try:
        assert is_valid_license_usage_details2(validator, license_usage_details2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def license_usage_details2_default_val(api):
    endpoint_result = api.licenses.license_usage_details2(
        device_type=None, smart_account_id="string", virtual_account_name="string"
    )
    return endpoint_result


@pytest.mark.licenses
def test_license_usage_details2_default_val(api, validator):
    try:
        assert is_valid_license_usage_details2(
            validator, license_usage_details2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

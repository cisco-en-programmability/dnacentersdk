# -*- coding: utf-8 -*-
"""CatalystCenterAPI licenses API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '3.1.3.0', reason='version does not match')


def is_valid_retrieves_c_s_s_m_connection_mode_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a32ed6ebdd945af9889223196c925a17_v3_1_3_0').validate(obj)
    return True


def retrieves_c_s_s_m_connection_mode_v1(api):
    endpoint_result = api.licenses.retrieves_c_s_s_m_connection_mode_v1(

    )
    return endpoint_result


@pytest.mark.licenses
def test_retrieves_c_s_s_m_connection_mode_v1(api, validator):
    try:
        assert is_valid_retrieves_c_s_s_m_connection_mode_v1(
            validator,
            retrieves_c_s_s_m_connection_mode_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_c_s_s_m_connection_mode_v1_default_val(api):
    endpoint_result = api.licenses.retrieves_c_s_s_m_connection_mode_v1(

    )
    return endpoint_result


@pytest.mark.licenses
def test_retrieves_c_s_s_m_connection_mode_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_c_s_s_m_connection_mode_v1(
            validator,
            retrieves_c_s_s_m_connection_mode_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_c_s_s_m_connection_mode_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c85b39d6bae0536695992ddbb91ea96d_v3_1_3_0').validate(obj)
    return True


def update_c_s_s_m_connection_mode_v1(api):
    endpoint_result = api.licenses.update_c_s_s_m_connection_mode_v1(
        active_validation=True,
        connectionMode='string',
        parameters={'onPremiseHost': 'string', 'smartAccountName': 'string', 'clientId': 'string', 'clientSecret': 'string'},
        payload=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_update_c_s_s_m_connection_mode_v1(api, validator):
    try:
        assert is_valid_update_c_s_s_m_connection_mode_v1(
            validator,
            update_c_s_s_m_connection_mode_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_c_s_s_m_connection_mode_v1_default_val(api):
    endpoint_result = api.licenses.update_c_s_s_m_connection_mode_v1(
        active_validation=True,
        connectionMode=None,
        parameters=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_update_c_s_s_m_connection_mode_v1_default_val(api, validator):
    try:
        assert is_valid_update_c_s_s_m_connection_mode_v1(
            validator,
            update_c_s_s_m_connection_mode_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_license_setting_v1(json_schema_validate, obj):
    json_schema_validate('jsd_420b5ef334945074a609698223cf05db_v3_1_3_0').validate(obj)
    return True


def retrieve_license_setting_v1(api):
    endpoint_result = api.licenses.retrieve_license_setting_v1(

    )
    return endpoint_result


@pytest.mark.licenses
def test_retrieve_license_setting_v1(api, validator):
    try:
        assert is_valid_retrieve_license_setting_v1(
            validator,
            retrieve_license_setting_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_license_setting_v1_default_val(api):
    endpoint_result = api.licenses.retrieve_license_setting_v1(

    )
    return endpoint_result


@pytest.mark.licenses
def test_retrieve_license_setting_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_license_setting_v1(
            validator,
            retrieve_license_setting_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_license_setting_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1d9bd7c527d254ecb63d2b709c428043_v3_1_3_0').validate(obj)
    return True


def update_license_setting_v1(api):
    endpoint_result = api.licenses.update_license_setting_v1(
        active_validation=True,
        autoRegistrationVirtualAccountId='string',
        defaultSmartAccountId='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_update_license_setting_v1(api, validator):
    try:
        assert is_valid_update_license_setting_v1(
            validator,
            update_license_setting_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_license_setting_v1_default_val(api):
    endpoint_result = api.licenses.update_license_setting_v1(
        active_validation=True,
        autoRegistrationVirtualAccountId=None,
        defaultSmartAccountId=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_update_license_setting_v1_default_val(api, validator):
    try:
        assert is_valid_update_license_setting_v1(
            validator,
            update_license_setting_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_device_count_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_87c0cf04bdc758b29bb11abbdacbd921_v3_1_3_0').validate(obj)
    return True


def device_count_details_v1(api):
    endpoint_result = api.licenses.device_count_details_v1(
        device_type='string',
        dna_level='string',
        registration_status='string',
        smart_account_id='string',
        virtual_account_name='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_count_details_v1(api, validator):
    try:
        assert is_valid_device_count_details_v1(
            validator,
            device_count_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_count_details_v1_default_val(api):
    endpoint_result = api.licenses.device_count_details_v1(
        device_type=None,
        dna_level=None,
        registration_status=None,
        smart_account_id=None,
        virtual_account_name=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_count_details_v1_default_val(api, validator):
    try:
        assert is_valid_device_count_details_v1(
            validator,
            device_count_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_device_license_summary_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f4ba64eef4085d518a612835e128fe3c_v3_1_3_0').validate(obj)
    return True


def device_license_summary_v1(api):
    endpoint_result = api.licenses.device_license_summary_v1(
        device_type='string',
        device_uuid='string',
        dna_level='string',
        limit=0,
        order='string',
        page_number=0,
        registration_status='string',
        smart_account_id=0,
        sort_by='string',
        virtual_account_name='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_license_summary_v1(api, validator):
    try:
        assert is_valid_device_license_summary_v1(
            validator,
            device_license_summary_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_license_summary_v1_default_val(api):
    endpoint_result = api.licenses.device_license_summary_v1(
        device_type=None,
        device_uuid=None,
        dna_level=None,
        limit=None,
        order=None,
        page_number=None,
        registration_status=None,
        smart_account_id=None,
        sort_by=None,
        virtual_account_name=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_license_summary_v1_default_val(api, validator):
    try:
        assert is_valid_device_license_summary_v1(
            validator,
            device_license_summary_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_device_license_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6f04f865c01d5c17a5f0cb5abe620dd8_v3_1_3_0').validate(obj)
    return True


def device_license_details_v1(api):
    endpoint_result = api.licenses.device_license_details_v1(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_license_details_v1(api, validator):
    try:
        assert is_valid_device_license_details_v1(
            validator,
            device_license_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_license_details_v1_default_val(api):
    endpoint_result = api.licenses.device_license_details_v1(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_license_details_v1_default_val(api, validator):
    try:
        assert is_valid_device_license_details_v1(
            validator,
            device_license_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_device_deregistration_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0109b2f15d0c54c2862a60a904289ddd_v3_1_3_0').validate(obj)
    return True


def device_deregistration_v1(api):
    endpoint_result = api.licenses.device_deregistration_v1(
        active_validation=True,
        device_uuids=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_deregistration_v1(api, validator):
    try:
        assert is_valid_device_deregistration_v1(
            validator,
            device_deregistration_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_deregistration_v1_default_val(api):
    endpoint_result = api.licenses.device_deregistration_v1(
        active_validation=True,
        device_uuids=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_deregistration_v1_default_val(api, validator):
    try:
        assert is_valid_device_deregistration_v1(
            validator,
            device_deregistration_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_device_registration_v1(json_schema_validate, obj):
    json_schema_validate('jsd_df26f516755a50b5b5477324cf5cb649_v3_1_3_0').validate(obj)
    return True


def device_registration_v1(api):
    endpoint_result = api.licenses.device_registration_v1(
        active_validation=True,
        device_uuids=['string'],
        payload=None,
        virtual_account_name='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_registration_v1(api, validator):
    try:
        assert is_valid_device_registration_v1(
            validator,
            device_registration_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_registration_v1_default_val(api):
    endpoint_result = api.licenses.device_registration_v1(
        active_validation=True,
        device_uuids=None,
        payload=None,
        virtual_account_name='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_device_registration_v1_default_val(api, validator):
    try:
        assert is_valid_device_registration_v1(
            validator,
            device_registration_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_change_virtual_account_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4bd5b507f58a50aab614e3d7409eec4c_v3_1_3_0').validate(obj)
    return True


def change_virtual_account_v1(api):
    endpoint_result = api.licenses.change_virtual_account_v1(
        active_validation=True,
        device_uuids=['string'],
        payload=None,
        smart_account_id='string',
        virtual_account_name='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_change_virtual_account_v1(api, validator):
    try:
        assert is_valid_change_virtual_account_v1(
            validator,
            change_virtual_account_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def change_virtual_account_v1_default_val(api):
    endpoint_result = api.licenses.change_virtual_account_v1(
        active_validation=True,
        device_uuids=None,
        payload=None,
        smart_account_id='string',
        virtual_account_name='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_change_virtual_account_v1_default_val(api, validator):
    try:
        assert is_valid_change_virtual_account_v1(
            validator,
            change_virtual_account_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_virtual_account_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8ab450b197375fa9bcd95219113a3075_v3_1_3_0').validate(obj)
    return True


def virtual_account_details_v1(api):
    endpoint_result = api.licenses.virtual_account_details_v1(
        smart_account_id='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_virtual_account_details_v1(api, validator):
    try:
        assert is_valid_virtual_account_details_v1(
            validator,
            virtual_account_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def virtual_account_details_v1_default_val(api):
    endpoint_result = api.licenses.virtual_account_details_v1(
        smart_account_id='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_virtual_account_details_v1_default_val(api, validator):
    try:
        assert is_valid_virtual_account_details_v1(
            validator,
            virtual_account_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_smart_account_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ea3fdbde23325051a76b9d062c2962a0_v3_1_3_0').validate(obj)
    return True


def smart_account_details_v1(api):
    endpoint_result = api.licenses.smart_account_details_v1(

    )
    return endpoint_result


@pytest.mark.licenses
def test_smart_account_details_v1(api, validator):
    try:
        assert is_valid_smart_account_details_v1(
            validator,
            smart_account_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def smart_account_details_v1_default_val(api):
    endpoint_result = api.licenses.smart_account_details_v1(

    )
    return endpoint_result


@pytest.mark.licenses
def test_smart_account_details_v1_default_val(api, validator):
    try:
        assert is_valid_smart_account_details_v1(
            validator,
            smart_account_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_license_term_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_df2d278e89b45c8ea0ca0a945c001f08_v3_1_3_0').validate(obj)
    return True


def license_term_details_v1(api):
    endpoint_result = api.licenses.license_term_details_v1(
        device_type='string',
        smart_account_id='string',
        virtual_account_name='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_license_term_details_v1(api, validator):
    try:
        assert is_valid_license_term_details_v1(
            validator,
            license_term_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def license_term_details_v1_default_val(api):
    endpoint_result = api.licenses.license_term_details_v1(
        device_type=None,
        smart_account_id='string',
        virtual_account_name='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_license_term_details_v1_default_val(api, validator):
    try:
        assert is_valid_license_term_details_v1(
            validator,
            license_term_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_license_usage_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_46e55ecbbda454c6a01d905e6f4cce16_v3_1_3_0').validate(obj)
    return True


def license_usage_details_v1(api):
    endpoint_result = api.licenses.license_usage_details_v1(
        device_type='string',
        smart_account_id='string',
        virtual_account_name='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_license_usage_details_v1(api, validator):
    try:
        assert is_valid_license_usage_details_v1(
            validator,
            license_usage_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def license_usage_details_v1_default_val(api):
    endpoint_result = api.licenses.license_usage_details_v1(
        device_type=None,
        smart_account_id='string',
        virtual_account_name='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_license_usage_details_v1_default_val(api, validator):
    try:
        assert is_valid_license_usage_details_v1(
            validator,
            license_usage_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_summary_of_network_device_licenses_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5df7151bbd7053ef8b010321bfa2bb84_v3_1_3_0').validate(obj)
    return True


def retrieves_summary_of_network_device_licenses_v1(api):
    endpoint_result = api.licenses.retrieves_summary_of_network_device_licenses_v1(

    )
    return endpoint_result


@pytest.mark.licenses
def test_retrieves_summary_of_network_device_licenses_v1(api, validator):
    try:
        assert is_valid_retrieves_summary_of_network_device_licenses_v1(
            validator,
            retrieves_summary_of_network_device_licenses_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_summary_of_network_device_licenses_v1_default_val(api):
    endpoint_result = api.licenses.retrieves_summary_of_network_device_licenses_v1(

    )
    return endpoint_result


@pytest.mark.licenses
def test_retrieves_summary_of_network_device_licenses_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_summary_of_network_device_licenses_v1(
            validator,
            retrieves_summary_of_network_device_licenses_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_smart_licensing_deregistration_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3df787402ab25f32b53dcf395b2742a8_v3_1_3_0').validate(obj)
    return True


def smart_licensing_deregistration_v1(api):
    endpoint_result = api.licenses.smart_licensing_deregistration_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_smart_licensing_deregistration_v1(api, validator):
    try:
        assert is_valid_smart_licensing_deregistration_v1(
            validator,
            smart_licensing_deregistration_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def smart_licensing_deregistration_v1_default_val(api):
    endpoint_result = api.licenses.smart_licensing_deregistration_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_smart_licensing_deregistration_v1_default_val(api, validator):
    try:
        assert is_valid_smart_licensing_deregistration_v1(
            validator,
            smart_licensing_deregistration_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_system_licensing_last_operation_status_v1(json_schema_validate, obj):
    json_schema_validate('jsd_49172923d1275a6eacbbda807ec535c5_v3_1_3_0').validate(obj)
    return True


def system_licensing_last_operation_status_v1(api):
    endpoint_result = api.licenses.system_licensing_last_operation_status_v1(

    )
    return endpoint_result


@pytest.mark.licenses
def test_system_licensing_last_operation_status_v1(api, validator):
    try:
        assert is_valid_system_licensing_last_operation_status_v1(
            validator,
            system_licensing_last_operation_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def system_licensing_last_operation_status_v1_default_val(api):
    endpoint_result = api.licenses.system_licensing_last_operation_status_v1(

    )
    return endpoint_result


@pytest.mark.licenses
def test_system_licensing_last_operation_status_v1_default_val(api, validator):
    try:
        assert is_valid_system_licensing_last_operation_status_v1(
            validator,
            system_licensing_last_operation_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_system_licensing_registration_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8762e6bca55256a0aac288486e38049b_v3_1_3_0').validate(obj)
    return True


def system_licensing_registration_v1(api):
    endpoint_result = api.licenses.system_licensing_registration_v1(
        active_validation=True,
        payload=None,
        smartAccountId='string',
        virtualAccountId='string'
    )
    return endpoint_result


@pytest.mark.licenses
def test_system_licensing_registration_v1(api, validator):
    try:
        assert is_valid_system_licensing_registration_v1(
            validator,
            system_licensing_registration_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def system_licensing_registration_v1_default_val(api):
    endpoint_result = api.licenses.system_licensing_registration_v1(
        active_validation=True,
        payload=None,
        smartAccountId=None,
        virtualAccountId=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_system_licensing_registration_v1_default_val(api, validator):
    try:
        assert is_valid_system_licensing_registration_v1(
            validator,
            system_licensing_registration_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_smart_licensing_renew_operation_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f059aef5236f531b918cf6f8bd766f79_v3_1_3_0').validate(obj)
    return True


def smart_licensing_renew_operation_v1(api):
    endpoint_result = api.licenses.smart_licensing_renew_operation_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_smart_licensing_renew_operation_v1(api, validator):
    try:
        assert is_valid_smart_licensing_renew_operation_v1(
            validator,
            smart_licensing_renew_operation_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def smart_licensing_renew_operation_v1_default_val(api):
    endpoint_result = api.licenses.smart_licensing_renew_operation_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.licenses
def test_smart_licensing_renew_operation_v1_default_val(api, validator):
    try:
        assert is_valid_smart_licensing_renew_operation_v1(
            validator,
            smart_licensing_renew_operation_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_system_licensing_status_v1(json_schema_validate, obj):
    json_schema_validate('jsd_39ad6565535c567d951cdaf7bdaf7972_v3_1_3_0').validate(obj)
    return True


def system_licensing_status_v1(api):
    endpoint_result = api.licenses.system_licensing_status_v1(

    )
    return endpoint_result


@pytest.mark.licenses
def test_system_licensing_status_v1(api, validator):
    try:
        assert is_valid_system_licensing_status_v1(
            validator,
            system_licensing_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def system_licensing_status_v1_default_val(api):
    endpoint_result = api.licenses.system_licensing_status_v1(

    )
    return endpoint_result


@pytest.mark.licenses
def test_system_licensing_status_v1_default_val(api, validator):
    try:
        assert is_valid_system_licensing_status_v1(
            validator,
            system_licensing_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

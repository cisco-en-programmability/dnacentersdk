# -*- coding: utf-8 -*-
"""DNACenterAPI itsm_integration API fixtures and tests.

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


def is_valid_create_itsm_integration_setting_v1(json_schema_validate, obj):
    json_schema_validate("jsd_2bb01b6bd31b53bfb12bbe327320392e_v2_3_7_6").validate(obj)
    return True


def create_itsm_integration_setting_v1(api):
    endpoint_result = api.itsm_integration.create_itsm_integration_setting_v1(
        active_validation=True,
        data={
            "ConnectionSettings": {
                "Url": "string",
                "Auth_UserName": "string",
                "Auth_Password": "string",
            }
        },
        description="string",
        dypName="string",
        name="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.itsm_integration
def test_create_itsm_integration_setting_v1(api, validator):
    try:
        assert is_valid_create_itsm_integration_setting_v1(
            validator, create_itsm_integration_setting_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_itsm_integration_setting_v1_default_val(api):
    endpoint_result = api.itsm_integration.create_itsm_integration_setting_v1(
        active_validation=True,
        data=None,
        description=None,
        dypName=None,
        name=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.itsm_integration
def test_create_itsm_integration_setting_v1_default_val(api, validator):
    try:
        assert is_valid_create_itsm_integration_setting_v1(
            validator, create_itsm_integration_setting_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_itsm_integration_setting_v1(json_schema_validate, obj):
    json_schema_validate("jsd_c9b5b83e67195b649077a05e42897cc4_v2_3_7_6").validate(obj)
    return True


def update_itsm_integration_setting_v1(api):
    endpoint_result = api.itsm_integration.update_itsm_integration_setting_v1(
        active_validation=True,
        data={
            "ConnectionSettings": {
                "Url": "string",
                "Auth_UserName": "string",
                "Auth_Password": "string",
            }
        },
        description="string",
        dypName="string",
        instance_id="string",
        name="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.itsm_integration
def test_update_itsm_integration_setting_v1(api, validator):
    try:
        assert is_valid_update_itsm_integration_setting_v1(
            validator, update_itsm_integration_setting_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_itsm_integration_setting_v1_default_val(api):
    endpoint_result = api.itsm_integration.update_itsm_integration_setting_v1(
        active_validation=True,
        data=None,
        description=None,
        dypName=None,
        instance_id="string",
        name=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.itsm_integration
def test_update_itsm_integration_setting_v1_default_val(api, validator):
    try:
        assert is_valid_update_itsm_integration_setting_v1(
            validator, update_itsm_integration_setting_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_itsm_integration_setting_by_id_v1(json_schema_validate, obj):
    json_schema_validate("jsd_53ca7a97d4665bca9634b6fb41cd7d29_v2_3_7_6").validate(obj)
    return True


def get_itsm_integration_setting_by_id_v1(api):
    endpoint_result = api.itsm_integration.get_itsm_integration_setting_by_id_v1(
        instance_id="string"
    )
    return endpoint_result


@pytest.mark.itsm_integration
def test_get_itsm_integration_setting_by_id_v1(api, validator):
    try:
        assert is_valid_get_itsm_integration_setting_by_id_v1(
            validator, get_itsm_integration_setting_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_itsm_integration_setting_by_id_v1_default_val(api):
    endpoint_result = api.itsm_integration.get_itsm_integration_setting_by_id_v1(
        instance_id="string"
    )
    return endpoint_result


@pytest.mark.itsm_integration
def test_get_itsm_integration_setting_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_itsm_integration_setting_by_id_v1(
            validator, get_itsm_integration_setting_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_itsm_integration_setting_v1(json_schema_validate, obj):
    json_schema_validate("jsd_7ae71ae83f7f530c81e650c1455567e8_v2_3_7_6").validate(obj)
    return True


def delete_itsm_integration_setting_v1(api):
    endpoint_result = api.itsm_integration.delete_itsm_integration_setting_v1(
        instance_id="string"
    )
    return endpoint_result


@pytest.mark.itsm_integration
def test_delete_itsm_integration_setting_v1(api, validator):
    try:
        assert is_valid_delete_itsm_integration_setting_v1(
            validator, delete_itsm_integration_setting_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_itsm_integration_setting_v1_default_val(api):
    endpoint_result = api.itsm_integration.delete_itsm_integration_setting_v1(
        instance_id="string"
    )
    return endpoint_result


@pytest.mark.itsm_integration
def test_delete_itsm_integration_setting_v1_default_val(api, validator):
    try:
        assert is_valid_delete_itsm_integration_setting_v1(
            validator, delete_itsm_integration_setting_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_itsm_integration_settings_v1(json_schema_validate, obj):
    json_schema_validate("jsd_ac54638bea4157f2bbd03f329ac25e27_v2_3_7_6").validate(obj)
    return True


def get_all_itsm_integration_settings_v1(api):
    endpoint_result = api.itsm_integration.get_all_itsm_integration_settings_v1()
    return endpoint_result


@pytest.mark.itsm_integration
def test_get_all_itsm_integration_settings_v1(api, validator):
    try:
        assert is_valid_get_all_itsm_integration_settings_v1(
            validator, get_all_itsm_integration_settings_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_itsm_integration_settings_v1_default_val(api):
    endpoint_result = api.itsm_integration.get_all_itsm_integration_settings_v1()
    return endpoint_result


@pytest.mark.itsm_integration
def test_get_all_itsm_integration_settings_v1_default_val(api, validator):
    try:
        assert is_valid_get_all_itsm_integration_settings_v1(
            validator, get_all_itsm_integration_settings_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_itsm_integration_status_v1(json_schema_validate, obj):
    json_schema_validate("jsd_e8398520e0aa5a549ddb60c11581b93d_v2_3_7_6").validate(obj)
    return True


def get_itsm_integration_status_v1(api):
    endpoint_result = api.itsm_integration.get_itsm_integration_status_v1()
    return endpoint_result


@pytest.mark.itsm_integration
def test_get_itsm_integration_status_v1(api, validator):
    try:
        assert is_valid_get_itsm_integration_status_v1(
            validator, get_itsm_integration_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_itsm_integration_status_v1_default_val(api):
    endpoint_result = api.itsm_integration.get_itsm_integration_status_v1()
    return endpoint_result


@pytest.mark.itsm_integration
def test_get_itsm_integration_status_v1_default_val(api, validator):
    try:
        assert is_valid_get_itsm_integration_status_v1(
            validator, get_itsm_integration_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

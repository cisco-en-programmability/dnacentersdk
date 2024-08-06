# -*- coding: utf-8 -*-
"""DNACenterAPI userand_roles API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.6', reason='version does not match')


def is_valid_add_role_api(json_schema_validate, obj):
    json_schema_validate('jsd_38a88c7510a15578b8eb2df183a92d5d_v2_3_7_6').validate(obj)
    return True


def add_role_api(api):
    endpoint_result = api.userand_roles.add_role_api(
        active_validation=True,
        description='string',
        payload=None,
        resourceTypes=[{'type': 'string', 'operations': ['string']}],
        role='string'
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_add_role_api(api, validator):
    try:
        assert is_valid_add_role_api(
            validator,
            add_role_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_role_api_default_val(api):
    endpoint_result = api.userand_roles.add_role_api(
        active_validation=True,
        description=None,
        payload=None,
        resourceTypes=None,
        role=None
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_add_role_api_default_val(api, validator):
    try:
        assert is_valid_add_role_api(
            validator,
            add_role_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_role_api(json_schema_validate, obj):
    json_schema_validate('jsd_ff5bf5a67c6c5c0aa9e7ba84c088e1a6_v2_3_7_6').validate(obj)
    return True


def update_role_api(api):
    endpoint_result = api.userand_roles.update_role_api(
        active_validation=True,
        description='string',
        payload=None,
        resourceTypes=[{'type': 'string', 'operations': ['string']}],
        roleId='string'
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_update_role_api(api, validator):
    try:
        assert is_valid_update_role_api(
            validator,
            update_role_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_role_api_default_val(api):
    endpoint_result = api.userand_roles.update_role_api(
        active_validation=True,
        description=None,
        payload=None,
        resourceTypes=None,
        roleId=None
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_update_role_api_default_val(api, validator):
    try:
        assert is_valid_update_role_api(
            validator,
            update_role_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_permissions_api(json_schema_validate, obj):
    json_schema_validate('jsd_9ec0b30eca9d540a845848cffd7c602a_v2_3_7_6').validate(obj)
    return True


def get_permissions_api(api):
    endpoint_result = api.userand_roles.get_permissions_api(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_permissions_api(api, validator):
    try:
        assert is_valid_get_permissions_api(
            validator,
            get_permissions_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_permissions_api_default_val(api):
    endpoint_result = api.userand_roles.get_permissions_api(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_permissions_api_default_val(api, validator):
    try:
        assert is_valid_get_permissions_api(
            validator,
            get_permissions_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_role_api(json_schema_validate, obj):
    json_schema_validate('jsd_da9e850c44d353f78ab002a640e5604f_v2_3_7_6').validate(obj)
    return True


def delete_role_api(api):
    endpoint_result = api.userand_roles.delete_role_api(
        role_id='string'
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_delete_role_api(api, validator):
    try:
        assert is_valid_delete_role_api(
            validator,
            delete_role_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_role_api_default_val(api):
    endpoint_result = api.userand_roles.delete_role_api(
        role_id='string'
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_delete_role_api_default_val(api, validator):
    try:
        assert is_valid_delete_role_api(
            validator,
            delete_role_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_roles_api(json_schema_validate, obj):
    json_schema_validate('jsd_bef02e8f6f8354dc99e375826a87c88c_v2_3_7_6').validate(obj)
    return True


def get_roles_api(api):
    endpoint_result = api.userand_roles.get_roles_api(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_roles_api(api, validator):
    try:
        assert is_valid_get_roles_api(
            validator,
            get_roles_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_roles_api_default_val(api):
    endpoint_result = api.userand_roles.get_roles_api(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_roles_api_default_val(api, validator):
    try:
        assert is_valid_get_roles_api(
            validator,
            get_roles_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_users_api(json_schema_validate, obj):
    json_schema_validate('jsd_7fa405b6d1be56739f2dfeea63212015_v2_3_7_6').validate(obj)
    return True


def get_users_api(api):
    endpoint_result = api.userand_roles.get_users_api(
        auth_source='string',
        invoke_source='string'
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_users_api(api, validator):
    try:
        assert is_valid_get_users_api(
            validator,
            get_users_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_users_api_default_val(api):
    endpoint_result = api.userand_roles.get_users_api(
        auth_source=None,
        invoke_source=None
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_users_api_default_val(api, validator):
    try:
        assert is_valid_get_users_api(
            validator,
            get_users_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_user_api(json_schema_validate, obj):
    json_schema_validate('jsd_6d82755e5e03510daf0951c1f42c2702_v2_3_7_6').validate(obj)
    return True


def add_user_api(api):
    endpoint_result = api.userand_roles.add_user_api(
        active_validation=True,
        email='string',
        firstName='string',
        lastName='string',
        password='string',
        payload=None,
        roleList=['string'],
        username='string'
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_add_user_api(api, validator):
    try:
        assert is_valid_add_user_api(
            validator,
            add_user_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_user_api_default_val(api):
    endpoint_result = api.userand_roles.add_user_api(
        active_validation=True,
        email=None,
        firstName=None,
        lastName=None,
        password=None,
        payload=None,
        roleList=None,
        username=None
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_add_user_api_default_val(api, validator):
    try:
        assert is_valid_add_user_api(
            validator,
            add_user_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_user_api(json_schema_validate, obj):
    json_schema_validate('jsd_34d2bd5f05bd535a89ebadb30e2ede9e_v2_3_7_6').validate(obj)
    return True


def update_user_api(api):
    endpoint_result = api.userand_roles.update_user_api(
        active_validation=True,
        email='string',
        firstName='string',
        lastName='string',
        payload=None,
        roleList=['string'],
        userId='string',
        username='string'
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_update_user_api(api, validator):
    try:
        assert is_valid_update_user_api(
            validator,
            update_user_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_user_api_default_val(api):
    endpoint_result = api.userand_roles.update_user_api(
        active_validation=True,
        email=None,
        firstName=None,
        lastName=None,
        payload=None,
        roleList=None,
        userId=None,
        username=None
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_update_user_api_default_val(api, validator):
    try:
        assert is_valid_update_user_api(
            validator,
            update_user_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_user_api(json_schema_validate, obj):
    json_schema_validate('jsd_3556c65c6cc65f068766cbb8a42ad387_v2_3_7_6').validate(obj)
    return True


def delete_user_api(api):
    endpoint_result = api.userand_roles.delete_user_api(
        user_id='string'
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_delete_user_api(api, validator):
    try:
        assert is_valid_delete_user_api(
            validator,
            delete_user_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_user_api_default_val(api):
    endpoint_result = api.userand_roles.delete_user_api(
        user_id='string'
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_delete_user_api_default_val(api, validator):
    try:
        assert is_valid_delete_user_api(
            validator,
            delete_user_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_external_authentication_setting_api(json_schema_validate, obj):
    json_schema_validate('jsd_5490ac03ba045f60925fd7843bf9e279_v2_3_7_6').validate(obj)
    return True


def get_external_authentication_setting_api(api):
    endpoint_result = api.userand_roles.get_external_authentication_setting_api(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_external_authentication_setting_api(api, validator):
    try:
        assert is_valid_get_external_authentication_setting_api(
            validator,
            get_external_authentication_setting_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_external_authentication_setting_api_default_val(api):
    endpoint_result = api.userand_roles.get_external_authentication_setting_api(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_external_authentication_setting_api_default_val(api, validator):
    try:
        assert is_valid_get_external_authentication_setting_api(
            validator,
            get_external_authentication_setting_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_manage_external_authentication_setting_api(json_schema_validate, obj):
    json_schema_validate('jsd_6e4f57e8f06856ee9a7e490d01f7f692_v2_3_7_6').validate(obj)
    return True


def manage_external_authentication_setting_api(api):
    endpoint_result = api.userand_roles.manage_external_authentication_setting_api(
        active_validation=True,
        enable=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_manage_external_authentication_setting_api(api, validator):
    try:
        assert is_valid_manage_external_authentication_setting_api(
            validator,
            manage_external_authentication_setting_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def manage_external_authentication_setting_api_default_val(api):
    endpoint_result = api.userand_roles.manage_external_authentication_setting_api(
        active_validation=True,
        enable=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_manage_external_authentication_setting_api_default_val(api, validator):
    try:
        assert is_valid_manage_external_authentication_setting_api(
            validator,
            manage_external_authentication_setting_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_external_authentication_servers_api(json_schema_validate, obj):
    json_schema_validate('jsd_452738def9045d4d9c96bcd42172a79c_v2_3_7_6').validate(obj)
    return True


def get_external_authentication_servers_api(api):
    endpoint_result = api.userand_roles.get_external_authentication_servers_api(
        invoke_source='string'
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_external_authentication_servers_api(api, validator):
    try:
        assert is_valid_get_external_authentication_servers_api(
            validator,
            get_external_authentication_servers_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_external_authentication_servers_api_default_val(api):
    endpoint_result = api.userand_roles.get_external_authentication_servers_api(
        invoke_source=None
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_external_authentication_servers_api_default_val(api, validator):
    try:
        assert is_valid_get_external_authentication_servers_api(
            validator,
            get_external_authentication_servers_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_and_update_a_a_a_attribute_api(json_schema_validate, obj):
    json_schema_validate('jsd_9f5bfccc7e30550baa7046f74daa1ef2_v2_3_7_6').validate(obj)
    return True


def add_and_update_a_a_a_attribute_api(api):
    endpoint_result = api.userand_roles.add_and_update_a_a_a_attribute_api(
        active_validation=True,
        attributeName='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_add_and_update_a_a_a_attribute_api(api, validator):
    try:
        assert is_valid_add_and_update_a_a_a_attribute_api(
            validator,
            add_and_update_a_a_a_attribute_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_and_update_a_a_a_attribute_api_default_val(api):
    endpoint_result = api.userand_roles.add_and_update_a_a_a_attribute_api(
        active_validation=True,
        attributeName=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_add_and_update_a_a_a_attribute_api_default_val(api, validator):
    try:
        assert is_valid_add_and_update_a_a_a_attribute_api(
            validator,
            add_and_update_a_a_a_attribute_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_a_a_attribute_api(json_schema_validate, obj):
    json_schema_validate('jsd_f20c99b436bd5be8bdb9094db3a47f01_v2_3_7_6').validate(obj)
    return True


def delete_a_a_a_attribute_api(api):
    endpoint_result = api.userand_roles.delete_a_a_a_attribute_api(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_delete_a_a_a_attribute_api(api, validator):
    try:
        assert is_valid_delete_a_a_a_attribute_api(
            validator,
            delete_a_a_a_attribute_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_a_a_attribute_api_default_val(api):
    endpoint_result = api.userand_roles.delete_a_a_a_attribute_api(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_delete_a_a_a_attribute_api_default_val(api, validator):
    try:
        assert is_valid_delete_a_a_a_attribute_api(
            validator,
            delete_a_a_a_attribute_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_a_a_a_attribute_api(json_schema_validate, obj):
    json_schema_validate('jsd_4bedf83096a45ad1beaaa1fc6c192103_v2_3_7_6').validate(obj)
    return True


def get_a_a_a_attribute_api(api):
    endpoint_result = api.userand_roles.get_a_a_a_attribute_api(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_a_a_a_attribute_api(api, validator):
    try:
        assert is_valid_get_a_a_a_attribute_api(
            validator,
            get_a_a_a_attribute_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_a_a_a_attribute_api_default_val(api):
    endpoint_result = api.userand_roles.get_a_a_a_attribute_api(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_a_a_a_attribute_api_default_val(api, validator):
    try:
        assert is_valid_get_a_a_a_attribute_api(
            validator,
            get_a_a_a_attribute_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.5.3', reason='version does not match')


def is_valid_get_permissions_ap_i(json_schema_validate, obj):
    json_schema_validate('jsd_9ec0b30eca9d540a845848cffd7c602a_v2_3_5_3').validate(obj)
    return True


def get_permissions_ap_i(api):
    endpoint_result = api.userand_roles.get_permissions_ap_i(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_permissions_ap_i(api, validator):
    try:
        assert is_valid_get_permissions_ap_i(
            validator,
            get_permissions_ap_i(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_permissions_ap_i_default_val(api):
    endpoint_result = api.userand_roles.get_permissions_ap_i(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_permissions_ap_i_default_val(api, validator):
    try:
        assert is_valid_get_permissions_ap_i(
            validator,
            get_permissions_ap_i_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_roles_ap_i(json_schema_validate, obj):
    json_schema_validate('jsd_bef02e8f6f8354dc99e375826a87c88c_v2_3_5_3').validate(obj)
    return True


def get_roles_ap_i(api):
    endpoint_result = api.userand_roles.get_roles_ap_i(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_roles_ap_i(api, validator):
    try:
        assert is_valid_get_roles_ap_i(
            validator,
            get_roles_ap_i(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_roles_ap_i_default_val(api):
    endpoint_result = api.userand_roles.get_roles_ap_i(

    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_roles_ap_i_default_val(api, validator):
    try:
        assert is_valid_get_roles_ap_i(
            validator,
            get_roles_ap_i_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_users_ap_i(json_schema_validate, obj):
    json_schema_validate('jsd_7fa405b6d1be56739f2dfeea63212015_v2_3_5_3').validate(obj)
    return True


def get_users_ap_i(api):
    endpoint_result = api.userand_roles.get_users_ap_i(
        invoke_source='string'
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_users_ap_i(api, validator):
    try:
        assert is_valid_get_users_ap_i(
            validator,
            get_users_ap_i(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_users_ap_i_default_val(api):
    endpoint_result = api.userand_roles.get_users_ap_i(
        invoke_source=None
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_users_ap_i_default_val(api, validator):
    try:
        assert is_valid_get_users_ap_i(
            validator,
            get_users_ap_i_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_user_ap_i(json_schema_validate, obj):
    json_schema_validate('jsd_6d82755e5e03510daf0951c1f42c2702_v2_3_5_3').validate(obj)
    return True


def add_user_ap_i(api):
    endpoint_result = api.userand_roles.add_user_ap_i(
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
def test_add_user_ap_i(api, validator):
    try:
        assert is_valid_add_user_ap_i(
            validator,
            add_user_ap_i(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_user_ap_i_default_val(api):
    endpoint_result = api.userand_roles.add_user_ap_i(
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
def test_add_user_ap_i_default_val(api, validator):
    try:
        assert is_valid_add_user_ap_i(
            validator,
            add_user_ap_i_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_user_ap_i(json_schema_validate, obj):
    json_schema_validate('jsd_34d2bd5f05bd535a89ebadb30e2ede9e_v2_3_5_3').validate(obj)
    return True


def update_user_ap_i(api):
    endpoint_result = api.userand_roles.update_user_ap_i(
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
def test_update_user_ap_i(api, validator):
    try:
        assert is_valid_update_user_ap_i(
            validator,
            update_user_ap_i(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_user_ap_i_default_val(api):
    endpoint_result = api.userand_roles.update_user_ap_i(
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
def test_update_user_ap_i_default_val(api, validator):
    try:
        assert is_valid_update_user_ap_i(
            validator,
            update_user_ap_i_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_external_authentication_servers_ap_i(json_schema_validate, obj):
    json_schema_validate('jsd_452738def9045d4d9c96bcd42172a79c_v2_3_5_3').validate(obj)
    return True


def get_external_authentication_servers_ap_i(api):
    endpoint_result = api.userand_roles.get_external_authentication_servers_ap_i(
        invoke_source='string'
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_external_authentication_servers_ap_i(api, validator):
    try:
        assert is_valid_get_external_authentication_servers_ap_i(
            validator,
            get_external_authentication_servers_ap_i(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_external_authentication_servers_ap_i_default_val(api):
    endpoint_result = api.userand_roles.get_external_authentication_servers_ap_i(
        invoke_source=None
    )
    return endpoint_result


@pytest.mark.userand_roles
def test_get_external_authentication_servers_ap_i_default_val(api, validator):
    try:
        assert is_valid_get_external_authentication_servers_ap_i(
            validator,
            get_external_authentication_servers_ap_i_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

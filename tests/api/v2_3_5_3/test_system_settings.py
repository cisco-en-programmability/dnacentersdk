# -*- coding: utf-8 -*-
"""DNACenterAPI system_settings API fixtures and tests.

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


def is_valid_get_authentication_and_policy_servers(json_schema_validate, obj):
    json_schema_validate("jsd_f7cc2592721f5b9b9f99795a26130147_v2_3_5_3").validate(obj)
    return True


def get_authentication_and_policy_servers(api):
    endpoint_result = api.system_settings.get_authentication_and_policy_servers(
        is_ise_enabled=True, role="string", state="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_get_authentication_and_policy_servers(api, validator):
    try:
        assert is_valid_get_authentication_and_policy_servers(
            validator, get_authentication_and_policy_servers(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_authentication_and_policy_servers_default_val(api):
    endpoint_result = api.system_settings.get_authentication_and_policy_servers(
        is_ise_enabled=None, role=None, state=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_get_authentication_and_policy_servers_default_val(api, validator):
    try:
        assert is_valid_get_authentication_and_policy_servers(
            validator, get_authentication_and_policy_servers_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_custom_prompt_support_get_api(json_schema_validate, obj):
    json_schema_validate("jsd_ada20dc4915d5901b50634628392e79f_v2_3_5_3").validate(obj)
    return True


def custom_prompt_support_get_api(api):
    endpoint_result = api.system_settings.custom_prompt_support_get_api()
    return endpoint_result


@pytest.mark.system_settings
def test_custom_prompt_support_get_api(api, validator):
    try:
        assert is_valid_custom_prompt_support_get_api(
            validator, custom_prompt_support_get_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def custom_prompt_support_get_api_default_val(api):
    endpoint_result = api.system_settings.custom_prompt_support_get_api()
    return endpoint_result


@pytest.mark.system_settings
def test_custom_prompt_support_get_api_default_val(api, validator):
    try:
        assert is_valid_custom_prompt_support_get_api(
            validator, custom_prompt_support_get_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_custom_prompt_post_api(json_schema_validate, obj):
    json_schema_validate("jsd_d2ea814bfae85da1b77872d095fc8221_v2_3_5_3").validate(obj)
    return True


def custom_prompt_post_api(api):
    endpoint_result = api.system_settings.custom_prompt_post_api(
        active_validation=True,
        passwordPrompt="string",
        payload=None,
        usernamePrompt="string",
    )
    return endpoint_result


@pytest.mark.system_settings
def test_custom_prompt_post_api(api, validator):
    try:
        assert is_valid_custom_prompt_post_api(validator, custom_prompt_post_api(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def custom_prompt_post_api_default_val(api):
    endpoint_result = api.system_settings.custom_prompt_post_api(
        active_validation=True, passwordPrompt=None, payload=None, usernamePrompt=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_custom_prompt_post_api_default_val(api, validator):
    try:
        assert is_valid_custom_prompt_post_api(
            validator, custom_prompt_post_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

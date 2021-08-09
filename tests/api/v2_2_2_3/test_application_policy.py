# -*- coding: utf-8 -*-
"""DNACenterAPI application_policy API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.2.3', reason='version does not match')


def is_valid_get_application_sets(json_schema_validate, obj):
    json_schema_validate('jsd_8b60dbd805b95030bc2caf345a44b504_v2_2_2_3').validate(obj)
    return True


def get_application_sets(api):
    endpoint_result = api.application_policy.get_application_sets(
        limit=0,
        name='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets(api, validator):
    try:
        assert is_valid_get_application_sets(
            validator,
            get_application_sets(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_sets_default(api):
    endpoint_result = api.application_policy.get_application_sets(
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_default(api, validator):
    try:
        assert is_valid_get_application_sets(
            validator,
            get_application_sets_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_application_set(json_schema_validate, obj):
    json_schema_validate('jsd_0a59a448c5c25f1e8246d6827e6e3215_v2_2_2_3').validate(obj)
    return True


def delete_application_set(api):
    endpoint_result = api.application_policy.delete_application_set(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_set(api, validator):
    try:
        assert is_valid_delete_application_set(
            validator,
            delete_application_set(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_application_set_default(api):
    endpoint_result = api.application_policy.delete_application_set(
        id=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_set_default(api, validator):
    try:
        assert is_valid_delete_application_set(
            validator,
            delete_application_set_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_application_set(json_schema_validate, obj):
    json_schema_validate('jsd_636cb7563a5058c4801eb842a74ff61c_v2_2_2_3').validate(obj)
    return True


def create_application_set(api):
    endpoint_result = api.application_policy.create_application_set(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_set(api, validator):
    try:
        assert is_valid_create_application_set(
            validator,
            create_application_set(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_application_set_default(api):
    endpoint_result = api.application_policy.create_application_set(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_set_default(api, validator):
    try:
        assert is_valid_create_application_set(
            validator,
            create_application_set_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_sets_count(json_schema_validate, obj):
    json_schema_validate('jsd_968ebc5880945305adb41253c6e4ffec_v2_2_2_3').validate(obj)
    return True


def get_application_sets_count(api):
    endpoint_result = api.application_policy.get_application_sets_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_count(api, validator):
    try:
        assert is_valid_get_application_sets_count(
            validator,
            get_application_sets_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_sets_count_default(api):
    endpoint_result = api.application_policy.get_application_sets_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_count_default(api, validator):
    try:
        assert is_valid_get_application_sets_count(
            validator,
            get_application_sets_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_application(json_schema_validate, obj):
    json_schema_validate('jsd_e1781a990c6b5a4b895d56bcfda2b7cb_v2_2_2_3').validate(obj)
    return True


def create_application(api):
    endpoint_result = api.application_policy.create_application(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application(api, validator):
    try:
        assert is_valid_create_application(
            validator,
            create_application(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_application_default(api):
    endpoint_result = api.application_policy.create_application(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_default(api, validator):
    try:
        assert is_valid_create_application(
            validator,
            create_application_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_edit_application(json_schema_validate, obj):
    json_schema_validate('jsd_a3b37dcbe2a150bea06d9dcde1837281_v2_2_2_3').validate(obj)
    return True


def edit_application(api):
    endpoint_result = api.application_policy.edit_application(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_edit_application(api, validator):
    try:
        assert is_valid_edit_application(
            validator,
            edit_application(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def edit_application_default(api):
    endpoint_result = api.application_policy.edit_application(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_edit_application_default(api, validator):
    try:
        assert is_valid_edit_application(
            validator,
            edit_application_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_application(json_schema_validate, obj):
    json_schema_validate('jsd_d11d35f3505652b68905ddf1ee2f7e66_v2_2_2_3').validate(obj)
    return True


def delete_application(api):
    endpoint_result = api.application_policy.delete_application(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application(api, validator):
    try:
        assert is_valid_delete_application(
            validator,
            delete_application(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_application_default(api):
    endpoint_result = api.application_policy.delete_application(
        id=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_default(api, validator):
    try:
        assert is_valid_delete_application(
            validator,
            delete_application_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_applications(json_schema_validate, obj):
    json_schema_validate('jsd_5b12cdd3a75c51258c9e051e84189f92_v2_2_2_3').validate(obj)
    return True


def get_applications(api):
    endpoint_result = api.application_policy.get_applications(
        limit=0,
        name='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications(api, validator):
    try:
        assert is_valid_get_applications(
            validator,
            get_applications(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_applications_default(api):
    endpoint_result = api.application_policy.get_applications(
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_default(api, validator):
    try:
        assert is_valid_get_applications(
            validator,
            get_applications_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_applications_count(json_schema_validate, obj):
    json_schema_validate('jsd_30af5f0aa1ed56ab9b98eb602dbd8366_v2_2_2_3').validate(obj)
    return True


def get_applications_count(api):
    endpoint_result = api.application_policy.get_applications_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_count(api, validator):
    try:
        assert is_valid_get_applications_count(
            validator,
            get_applications_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_applications_count_default(api):
    endpoint_result = api.application_policy.get_applications_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_count_default(api, validator):
    try:
        assert is_valid_get_applications_count(
            validator,
            get_applications_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI application_policy API fixtures and tests.

Copyright (c) 2019 Cisco and/or its affiliates.

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
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.1.1', reason='version does not match')


def is_valid_get_applications_count(obj):
    json_schema_validate('jsd_039de8b147a98690_v2_1_1').validate(obj)
    return True


def get_applications_count(api):
    endpoint_result = api.application_policy.get_applications_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_count(api):
    assert is_valid_get_applications_count(
        get_applications_count(api)
    )


def get_applications_count_default(api):
    endpoint_result = api.application_policy.get_applications_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_count_default(api):
    try:
        assert is_valid_get_applications_count(
            get_applications_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_application_set(obj):
    json_schema_validate('jsd_3e94cb1b485b8b0e_v2_1_1').validate(obj)
    return True


def create_application_set(api):
    endpoint_result = api.application_policy.create_application_set(
        active_validation=True,
        payload=[{'name': 'string'}]
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_set(api):
    assert is_valid_create_application_set(
        create_application_set(api)
    )


def create_application_set_default(api):
    endpoint_result = api.application_policy.create_application_set(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_set_default(api):
    try:
        assert is_valid_create_application_set(
            create_application_set_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_edit_application(obj):
    json_schema_validate('jsd_398668874439a41d_v2_1_1').validate(obj)
    return True


def edit_application(api):
    endpoint_result = api.application_policy.edit_application(
        active_validation=True,
        payload=[{'id': 'string', 'name': 'string', 'networkApplications': [{'id': 'string', 'appProtocol': 'string', 'applicationSubType': 'string', 'applicationType': 'string', 'categoryId': 'string', 'displayName': 'string', 'engineId': 'string', 'helpString': 'string', 'longDescription': 'string', 'name': 'string', 'popularity': 'string', 'rank': 'string', 'trafficClass': 'string', 'serverName': 'string', 'url': 'string', 'dscp': 'string', 'ignoreConflict': 'string'}], 'networkIdentity': [{'id': 'string', 'displayName': 'string', 'lowerPort': 'string', 'ports': 'string', 'protocol': 'string', 'upperPort': 'string'}], 'applicationSet': {'idRef': 'string'}}]
    )
    return endpoint_result


@pytest.mark.application_policy
def test_edit_application(api):
    assert is_valid_edit_application(
        edit_application(api)
    )


def edit_application_default(api):
    endpoint_result = api.application_policy.edit_application(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_edit_application_default(api):
    try:
        assert is_valid_edit_application(
            edit_application_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_application_set(obj):
    json_schema_validate('jsd_70b6f8e140b8b784_v2_1_1').validate(obj)
    return True


def delete_application_set(api):
    endpoint_result = api.application_policy.delete_application_set(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_set(api):
    assert is_valid_delete_application_set(
        delete_application_set(api)
    )


def delete_application_set_default(api):
    endpoint_result = api.application_policy.delete_application_set(
        id=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_set_default(api):
    try:
        assert is_valid_delete_application_set(
            delete_application_set_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_applications(obj):
    json_schema_validate('jsd_8893b834445bb29c_v2_1_1').validate(obj)
    return True


def get_applications(api):
    endpoint_result = api.application_policy.get_applications(
        limit=500,
        name='string',
        offset=1
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications(api):
    assert is_valid_get_applications(
        get_applications(api)
    )


def get_applications_default(api):
    endpoint_result = api.application_policy.get_applications(
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_default(api):
    try:
        assert is_valid_get_applications(
            get_applications_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_application_sets_count(obj):
    json_schema_validate('jsd_cfa049a644bb8a07_v2_1_1').validate(obj)
    return True


def get_application_sets_count(api):
    endpoint_result = api.application_policy.get_application_sets_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_count(api):
    assert is_valid_get_application_sets_count(
        get_application_sets_count(api)
    )


def get_application_sets_count_default(api):
    endpoint_result = api.application_policy.get_application_sets_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_count_default(api):
    try:
        assert is_valid_get_application_sets_count(
            get_application_sets_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_application_sets(obj):
    json_schema_validate('jsd_cb868b2142898159_v2_1_1').validate(obj)
    return True


def get_application_sets(api):
    endpoint_result = api.application_policy.get_application_sets(
        limit=500,
        name='string',
        offset=1
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets(api):
    assert is_valid_get_application_sets(
        get_application_sets(api)
    )


def get_application_sets_default(api):
    endpoint_result = api.application_policy.get_application_sets(
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_default(api):
    try:
        assert is_valid_get_application_sets(
            get_application_sets_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_application(obj):
    json_schema_validate('jsd_d49af9b84c6aa8ea_v2_1_1').validate(obj)
    return True


def delete_application(api):
    endpoint_result = api.application_policy.delete_application(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application(api):
    assert is_valid_delete_application(
        delete_application(api)
    )


def delete_application_default(api):
    endpoint_result = api.application_policy.delete_application(
        id=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_default(api):
    try:
        assert is_valid_delete_application(
            delete_application_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_application(obj):
    json_schema_validate('jsd_fb9bf80f491a9851_v2_1_1').validate(obj)
    return True


def create_application(api):
    endpoint_result = api.application_policy.create_application(
        active_validation=True,
        payload=[{'name': 'string', 'networkApplications': [{'appProtocol': 'string', 'applicationSubType': 'string', 'applicationType': 'string', 'categoryId': 'string', 'displayName': 'string', 'engineId': 'string', 'helpString': 'string', 'longDescription': 'string', 'name': 'string', 'popularity': 'string', 'rank': 'string', 'trafficClass': 'string', 'serverName': 'string', 'url': 'string', 'dscp': 'string', 'ignoreConflict': 'string'}], 'networkIdentity': [{'displayName': 'string', 'lowerPort': 'string', 'ports': 'string', 'protocol': 'string', 'upperPort': 'string'}], 'applicationSet': {'idRef': 'string'}}]
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application(api):
    assert is_valid_create_application(
        create_application(api)
    )


def create_application_default(api):
    endpoint_result = api.application_policy.create_application(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_default(api):
    try:
        assert is_valid_create_application(
            create_application_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

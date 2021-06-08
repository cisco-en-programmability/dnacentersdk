# -*- coding: utf-8 -*-
"""DNACenterAPI task API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.1', reason='version does not match')


def is_valid_get_task_count(json_schema_validate, obj):
    json_schema_validate('jsd_8d0586946be75e0f9f2c170217d45a28_v2_2_1').validate(obj)
    return True


def get_task_count(api):
    endpoint_result = api.task.get_task_count(
        data='string',
        end_time='string',
        error_code='string',
        failure_reason='string',
        is_error='string',
        parent_id='string',
        progress='string',
        service_type='string',
        start_time='string',
        username='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_count(api, validator):
    try:
        assert is_valid_get_task_count(
            validator,
            get_task_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_task_count_default(api):
    endpoint_result = api.task.get_task_count(
        data=None,
        end_time=None,
        error_code=None,
        failure_reason=None,
        is_error=None,
        parent_id=None,
        progress=None,
        service_type=None,
        start_time=None,
        username=None
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_count_default(api, validator):
    try:
        assert is_valid_get_task_count(
            validator,
            get_task_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_task_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_8009857899a75ba5a6bae1d568700bd3_v2_2_1').validate(obj)
    return True


def get_task_by_id(api):
    endpoint_result = api.task.get_task_by_id(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_by_id(api, validator):
    try:
        assert is_valid_get_task_by_id(
            validator,
            get_task_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_task_by_id_default(api):
    endpoint_result = api.task.get_task_by_id(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_by_id_default(api, validator):
    try:
        assert is_valid_get_task_by_id(
            validator,
            get_task_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_task_by_operationid(json_schema_validate, obj):
    json_schema_validate('jsd_d95c21e41dce5a9dbee07d33eefef2b2_v2_2_1').validate(obj)
    return True


def get_task_by_operationid(api):
    endpoint_result = api.task.get_task_by_operationid(
        limit=0,
        offset=0,
        operation_id='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_by_operationid(api, validator):
    try:
        assert is_valid_get_task_by_operationid(
            validator,
            get_task_by_operationid(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_task_by_operationid_default(api):
    endpoint_result = api.task.get_task_by_operationid(
        limit=0,
        offset=0,
        operation_id='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_by_operationid_default(api, validator):
    try:
        assert is_valid_get_task_by_operationid(
            validator,
            get_task_by_operationid_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tasks(json_schema_validate, obj):
    json_schema_validate('jsd_75ff485556f6504d8443789f42098be7_v2_2_1').validate(obj)
    return True


def get_tasks(api):
    endpoint_result = api.task.get_tasks(
        data='string',
        end_time='string',
        error_code='string',
        failure_reason='string',
        is_error='string',
        limit='string',
        offset='string',
        order='string',
        parent_id='string',
        progress='string',
        service_type='string',
        sort_by='string',
        start_time='string',
        username='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_tasks(api, validator):
    try:
        assert is_valid_get_tasks(
            validator,
            get_tasks(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tasks_default(api):
    endpoint_result = api.task.get_tasks(
        data=None,
        end_time=None,
        error_code=None,
        failure_reason=None,
        is_error=None,
        limit=None,
        offset=None,
        order=None,
        parent_id=None,
        progress=None,
        service_type=None,
        sort_by=None,
        start_time=None,
        username=None
    )
    return endpoint_result


@pytest.mark.task
def test_get_tasks_default(api, validator):
    try:
        assert is_valid_get_tasks(
            validator,
            get_tasks_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_task_tree(json_schema_validate, obj):
    json_schema_validate('jsd_8fa2865e229b536aacd59585a1d29704_v2_2_1').validate(obj)
    return True


def get_task_tree(api):
    endpoint_result = api.task.get_task_tree(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_tree(api, validator):
    try:
        assert is_valid_get_task_tree(
            validator,
            get_task_tree(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_task_tree_default(api):
    endpoint_result = api.task.get_task_tree(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_tree_default(api, validator):
    try:
        assert is_valid_get_task_tree(
            validator,
            get_task_tree_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

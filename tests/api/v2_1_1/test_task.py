# -*- coding: utf-8 -*-
"""DNACenterAPI task API fixtures and tests.

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


def is_valid_get_task_count(obj):
    json_schema_validate('jsd_26b44ab04649a183_v2_1_1').validate(obj)
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
def test_get_task_count(api):
    assert is_valid_get_task_count(
        get_task_count(api)
    )


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
def test_get_task_count_default(api):
    try:
        assert is_valid_get_task_count(
            get_task_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_task_by_id(obj):
    json_schema_validate('jsd_a1a9387346ba92b1_v2_1_1').validate(obj)
    return True


def get_task_by_id(api):
    endpoint_result = api.task.get_task_by_id(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_by_id(api):
    assert is_valid_get_task_by_id(
        get_task_by_id(api)
    )


def get_task_by_id_default(api):
    endpoint_result = api.task.get_task_by_id(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_by_id_default(api):
    try:
        assert is_valid_get_task_by_id(
            get_task_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_tasks(obj):
    json_schema_validate('jsd_e78bb8a2449b9eed_v2_1_1').validate(obj)
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
def test_get_tasks(api):
    assert is_valid_get_tasks(
        get_tasks(api)
    )


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
def test_get_tasks_default(api):
    try:
        assert is_valid_get_tasks(
            get_tasks_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_task_tree(obj):
    json_schema_validate('jsd_f5a269c44f2a95fa_v2_1_1').validate(obj)
    return True


def get_task_tree(api):
    endpoint_result = api.task.get_task_tree(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_tree(api):
    assert is_valid_get_task_tree(
        get_task_tree(api)
    )


def get_task_tree_default(api):
    endpoint_result = api.task.get_task_tree(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_tree_default(api):
    try:
        assert is_valid_get_task_tree(
            get_task_tree_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_task_by_operationid(obj):
    json_schema_validate('jsd_e487f8d3481b94f2_v2_1_1').validate(obj)
    return True


def get_task_by_operationid(api):
    endpoint_result = api.task.get_task_by_operationid(
        limit=0,
        offset=0,
        operation_id='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_by_operationid(api):
    assert is_valid_get_task_by_operationid(
        get_task_by_operationid(api)
    )


def get_task_by_operationid_default(api):
    endpoint_result = api.task.get_task_by_operationid(
        limit=0,
        offset=0,
        operation_id='string'
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_by_operationid_default(api):
    try:
        assert is_valid_get_task_by_operationid(
            get_task_by_operationid_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI pnp API fixtures and tests.

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
import dnacentersdk




# 3cb2-4acb-486b-89d2
def is_valid_get_smart_account_list(obj):
    return len(obj) > 0 and all([ item for item in obj ])


def get_smart_account_list(api):
    endpoint_result = api.pnp.get_smart_account_list( payload = '' )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_smart_account_list(api):
    assert is_valid_get_smart_account_list(get_smart_account_list(api))


# 70a4-79a6-462a-9496
def is_valid_get_virtual_account_list(obj):
    return len(obj) > 0 and all([ item for item in obj ])


def get_virtual_account_list(api):
    endpoint_result = api.pnp.get_virtual_account_list( path_param_domain = get_smart_account_list(api)[0], payload = '' )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_virtual_account_list(api):
    assert is_valid_get_virtual_account_list(get_virtual_account_list(api))


# 0a9c-9884-45cb-91c8
def is_valid_get_sync_result_for_virtual_account(obj):
    some_keys = [ 'virtualAccountId', 'autoSyncPeriod', 'syncResultStr', 'profile' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_sync_result_for_virtual_account(api):
    endpoint_result = api.pnp.get_sync_result_for_virtual_account( path_param_domain = get_smart_account_list(api)[0], path_param_name = get_virtual_account_list(api)[0], payload = '' )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_sync_result_for_virtual_account(api):
    assert is_valid_get_sync_result_for_virtual_account(get_sync_result_for_virtual_account(api))


# 7989-f868-46fa-af99
def is_valid_get_workflow_count(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_workflow_count(api):
    endpoint_result = api.pnp.get_workflow_count( param_name = None, payload = '' )
    return endpoint_result


def test_get_workflow_count(api):
    assert is_valid_get_workflow_count(get_workflow_count(api))


# aeb4-dad0-4a99-bbe3
def is_valid_get_workflows(obj):
    return len(obj) > 0 and all([ item for item in obj ])


def get_workflows(api):
    endpoint_result = api.pnp.get_workflows( param_limit = None, param_name = None, param_offset = None, param_sort = 'addedOn', param_sort_order = 'des', param_type = None, payload = '' )
    return endpoint_result


def test_get_workflows(api):
    assert is_valid_get_workflows(get_workflows(api))


# 80ac-b88e-4ac9-ac6d
def is_valid_get_workflow_by_id(obj):
    some_keys = [ '_id', 'state', 'type', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_workflow_by_id(api):
    endpoint_result = api.pnp.get_workflow_by_id( path_param_id = get_workflows(api)[0].id, payload = '' )
    return endpoint_result


def test_get_workflow_by_id(api):
    assert is_valid_get_workflow_by_id(get_workflow_by_id(api))


# 7e92-f9eb-46db-8320
def is_valid_get_pnp_global_settings(obj):
    some_keys = [ 'savaMappingList', 'taskTimeOuts', 'tenantId', 'aaaCredentials' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_pnp_global_settings(api):
    endpoint_result = api.pnp.get_pnp_global_settings( payload = '' )
    return endpoint_result


def test_get_pnp_global_settings(api):
    assert is_valid_get_pnp_global_settings(get_pnp_global_settings(api))


# e6b3-db80-46c9-9654
def is_valid_get_device_list(obj):
    some_keys = [ 'deviceInfo', 'systemResetWorkflow', 'systemWorkflow', 'workflow' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_list(api):
    endpoint_result = api.pnp.get_device_list( param_cm_state = None, param_last_contact = None, param_limit = 1, param_name = None, param_offset = None, param_onb_state = None, param_pid = None, param_project_id = None, param_project_name = None, param_serial_number = None, param_smart_account_id = None, param_sort = None, param_sort_order = None, param_source = None, param_state = None, param_virtual_account_id = None, param_workflow_id = None, param_workflow_name = None, payload = '' )
    return endpoint_result


def test_get_device_list(api):
    assert is_valid_get_device_list(get_device_list(api))


# bab6-c9e5-4408-85cc
def is_valid_get_device_by_id(obj):
    some_keys = [ '_id', 'deviceInfo', 'systemResetWorkflow', 'systemWorkflow' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_by_id(api):
    endpoint_result = api.pnp.get_device_by_id( path_param_id = get_device_list(api)[0].id, payload = '' )
    return endpoint_result


def test_get_device_by_id(api):
    assert is_valid_get_device_by_id(get_device_by_id(api))


# d9a1-fa9c-4068-b23c
def is_valid_get_device_count(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_count(api):
    endpoint_result = api.pnp.get_device_count( param_cm_state = None, param_last_contact = None, param_name = None, param_onb_state = None, param_pid = None, param_project_id = None, param_project_name = None, param_serial_number = None, param_smart_account_id = None, param_source = None, param_state = None, param_virtual_account_id = None, param_workflow_id = None, param_workflow_name = None, payload = '' )
    return endpoint_result


def test_get_device_count(api):
    assert is_valid_get_device_count(get_device_count(api))


# f093-1967-4049-a7d4
def is_valid_get_device_history(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_history(api):
    endpoint_result = api.pnp.get_device_history( param_serial_number = get_device_list(api)[0].deviceInfo.serialNumber, param_sort = None, param_sort_order = None, payload = '' )
    return endpoint_result


def test_get_device_history(api):
    assert is_valid_get_device_history(get_device_history(api))


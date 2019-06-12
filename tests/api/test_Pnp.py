# pnp

import pytest
import dnacentersdk


def is_valid_get_sync_result_for_virtual_account(obj):
    some_keys = [ 'virtualAccountId', 'autoSyncPeriod', 'syncResultStr', 'profile' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_sync_result_for_virtual_account(api):
    endpoint_result = api.pnp.get_sync_result_for_virtual_account( path_param_domain = '', path_param_name = '')
    assert is_valid_get_sync_result_for_virtual_account(endpoint_result)


def is_valid_import_devices_in_bulk(obj):
    some_keys = [ 'successList' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_import_devices_in_bulk(api):
    endpoint_result = api.pnp.import_devices_in_bulk( )
    assert is_valid_import_devices_in_bulk(endpoint_result)


def is_valid_update_workflow(obj):
    some_keys = [ '_id', 'state', 'type', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_workflow(api):
    endpoint_result = api.pnp.update_workflow( path_param_id = '', rq__id = None, rq_addToInventory = None, rq_addedOn = None, rq_configId = None, rq_currTaskIdx = None, rq_description = None, rq_endTime = None, rq_execTime = None, rq_imageId = None, rq_instanceType = None, rq_lastupdateOn = None, rq_name = None, rq_startTime = None, rq_state = None, rq_tasks = None, rq_tenantId = None, rq_type = None, rq_useState = None, rq_version = None)
    assert is_valid_update_workflow(endpoint_result)


def is_valid_un_claim_device(obj):
    some_keys = [ 'jsonArrayResponse', 'jsonResponse', 'message' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_un_claim_device(api):
    endpoint_result = api.pnp.un_claim_device( rq_deviceIdList = None)
    assert is_valid_un_claim_device(endpoint_result)


def is_valid_add_virtual_account(obj):
    some_keys = [ 'virtualAccountId', 'autoSyncPeriod', 'syncResultStr', 'profile' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_add_virtual_account(api):
    endpoint_result = api.pnp.add_virtual_account( rq_autoSyncPeriod = None, rq_ccoUser = None, rq_expiry = None, rq_lastSync = None, rq_profile = None, rq_smartAccountId = None, rq_syncResult = None, rq_syncResultStr = None, rq_syncStartTime = None, rq_syncStatus = None, rq_tenantId = None, rq_token = None, rq_virtualAccountId = None)
    assert is_valid_add_virtual_account(endpoint_result)


def is_valid_update_device(obj):
    some_keys = [ '_id', 'deviceInfo', 'systemResetWorkflow', 'systemWorkflow' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_device(api):
    endpoint_result = api.pnp.update_device( path_param_id = '', rq__id = None, rq_deviceInfo = None, rq_runSummaryList = None, rq_systemResetWorkflow = None, rq_systemWorkflow = None, rq_tenantId = None, rq_version = None, rq_workflow = None, rq_workflowParameters = None)
    assert is_valid_update_device(endpoint_result)


def is_valid_claim_a_device_to_a_site(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_claim_a_device_to_a_site(api):
    endpoint_result = api.pnp.claim_a_device_to_a_site( rq_deviceId = None, rq_siteId = None, rq_type = None)
    assert is_valid_claim_a_device_to_a_site(endpoint_result)


def is_valid_deregister_virtual_account(obj):
    some_keys = [ 'virtualAccountId', 'autoSyncPeriod', 'syncResultStr', 'profile' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_deregister_virtual_account(api):
    endpoint_result = api.pnp.deregister_virtual_account( param_domain = '', param_name = '')
    assert is_valid_deregister_virtual_account(endpoint_result)


def is_valid_get_smart_account_list(obj):
    return len(obj) > 0 and all([ item for item in obj ])

def test_get_smart_account_list(api):
    endpoint_result = api.pnp.get_smart_account_list( )
    assert is_valid_get_smart_account_list(endpoint_result)


def is_valid_get_workflow_by_id(obj):
    some_keys = [ '_id', 'state', 'type', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_workflow_by_id(api):
    endpoint_result = api.pnp.get_workflow_by_id( path_param_id = '')
    assert is_valid_get_workflow_by_id(endpoint_result)


def is_valid_update_pnp_server_profile(obj):
    some_keys = [ 'virtualAccountId', 'autoSyncPeriod', 'syncResultStr', 'profile' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_pnp_server_profile(api):
    endpoint_result = api.pnp.update_pnp_server_profile( rq_autoSyncPeriod = None, rq_ccoUser = None, rq_expiry = None, rq_lastSync = None, rq_profile = None, rq_smartAccountId = None, rq_syncResult = None, rq_syncResultStr = None, rq_syncStartTime = None, rq_syncStatus = None, rq_tenantId = None, rq_token = None, rq_virtualAccountId = None)
    assert is_valid_update_pnp_server_profile(endpoint_result)


def is_valid_get_workflow_count(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_workflow_count(api):
    endpoint_result = api.pnp.get_workflow_count( param_name = None)
    assert is_valid_get_workflow_count(endpoint_result)


def is_valid_update_pnp_global_settings(obj):
    some_keys = [ 'savaMappingList', 'taskTimeOuts', 'tenantId', 'aaaCredentials' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_pnp_global_settings(api):
    endpoint_result = api.pnp.update_pnp_global_settings( rq__id = None, rq_aaaCredentials = None, rq_acceptEula = None, rq_defaultProfile = None, rq_savaMappingList = None, rq_taskTimeOuts = None, rq_tenantId = None, rq_version = None)
    assert is_valid_update_pnp_global_settings(endpoint_result)


def is_valid_get_pnp_global_settings(obj):
    some_keys = [ 'savaMappingList', 'taskTimeOuts', 'tenantId', 'aaaCredentials' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_pnp_global_settings(api):
    endpoint_result = api.pnp.get_pnp_global_settings( )
    assert is_valid_get_pnp_global_settings(endpoint_result)


def is_valid_reset_device(obj):
    some_keys = [ 'jsonArrayResponse', 'jsonResponse', 'message' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_reset_device(api):
    endpoint_result = api.pnp.reset_device( rq_deviceResetList = None, rq_projectId = None, rq_workflowId = None)
    assert is_valid_reset_device(endpoint_result)


def is_valid_sync_virtual_account_devices(obj):
    some_keys = [ 'virtualAccountId', 'autoSyncPeriod', 'syncResultStr', 'profile' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_sync_virtual_account_devices(api):
    endpoint_result = api.pnp.sync_virtual_account_devices( rq_autoSyncPeriod = None, rq_ccoUser = None, rq_expiry = None, rq_lastSync = None, rq_profile = None, rq_smartAccountId = None, rq_syncResult = None, rq_syncResultStr = None, rq_syncStartTime = None, rq_syncStatus = None, rq_tenantId = None, rq_token = None, rq_virtualAccountId = None)
    assert is_valid_sync_virtual_account_devices(endpoint_result)


def is_valid_get_workflows(obj):
    return len(obj) > 0 and all([ item for item in obj ])

def test_get_workflows(api):
    endpoint_result = api.pnp.get_workflows( param_limit = None, param_name = None, param_offset = None, param_sort = None, param_sort_order = None, param_type = None)
    assert is_valid_get_workflows(endpoint_result)


def is_valid_delete_workflow_by_id(obj):
    some_keys = [ '_id', 'state', 'type', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_workflow_by_id(api):
    endpoint_result = api.pnp.delete_workflow_by_id( path_param_id = '')
    assert is_valid_delete_workflow_by_id(endpoint_result)


def is_valid_get_device_by_id(obj):
    some_keys = [ '_id', 'deviceInfo', 'systemResetWorkflow', 'systemWorkflow' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_by_id(api):
    endpoint_result = api.pnp.get_device_by_id( path_param_id = '')
    assert is_valid_get_device_by_id(endpoint_result)


def is_valid_get_virtual_account_list(obj):
    return len(obj) > 0 and all([ item for item in obj ])

def test_get_virtual_account_list(api):
    endpoint_result = api.pnp.get_virtual_account_list( path_param_domain = '')
    assert is_valid_get_virtual_account_list(endpoint_result)


def is_valid_preview_config(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_preview_config(api):
    endpoint_result = api.pnp.preview_config( rq_deviceId = None, rq_siteId = None, rq_type = None)
    assert is_valid_preview_config(endpoint_result)


def is_valid_claim_device(obj):
    some_keys = [ 'jsonArrayResponse', 'jsonResponse', 'message' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_claim_device(api):
    endpoint_result = api.pnp.claim_device( rq_configFileUrl = None, rq_configId = None, rq_deviceClaimList = None, rq_fileServiceId = None, rq_imageId = None, rq_imageUrl = None, rq_populateInventory = None, rq_projectId = None, rq_workflowId = None)
    assert is_valid_claim_device(endpoint_result)


def is_valid_get_device_list(obj):
    some_keys = [ 'deviceInfo', 'systemResetWorkflow', 'systemWorkflow', 'workflow' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_list(api):
    endpoint_result = api.pnp.get_device_list( param_cm_state = None, param_last_contact = None, param_limit = None, param_name = None, param_offset = None, param_onb_state = None, param_pid = None, param_project_id = None, param_project_name = None, param_serial_number = None, param_smart_account_id = None, param_sort = None, param_sort_order = None, param_source = None, param_state = None, param_virtual_account_id = None, param_workflow_id = None, param_workflow_name = None)
    assert is_valid_get_device_list(endpoint_result)


def is_valid_add_a_workflow(obj):
    some_keys = [ '_id', 'state', 'type', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_add_a_workflow(api):
    endpoint_result = api.pnp.add_a_workflow( rq__id = None, rq_addToInventory = None, rq_addedOn = None, rq_configId = None, rq_currTaskIdx = None, rq_description = None, rq_endTime = None, rq_execTime = None, rq_imageId = None, rq_instanceType = None, rq_lastupdateOn = None, rq_name = None, rq_startTime = None, rq_state = None, rq_tasks = None, rq_tenantId = None, rq_type = None, rq_useState = None, rq_version = None)
    assert is_valid_add_a_workflow(endpoint_result)


def is_valid_get_device_count(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_count(api):
    endpoint_result = api.pnp.get_device_count( param_cm_state = None, param_last_contact = None, param_name = None, param_onb_state = None, param_pid = None, param_project_id = None, param_project_name = None, param_serial_number = None, param_smart_account_id = None, param_source = None, param_state = None, param_virtual_account_id = None, param_workflow_id = None, param_workflow_name = None)
    assert is_valid_get_device_count(endpoint_result)


def is_valid_get_device_history(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_device_history(api):
    endpoint_result = api.pnp.get_device_history( param_serial_number = '', param_sort = None, param_sort_order = None)
    assert is_valid_get_device_history(endpoint_result)


def is_valid_delete_device_by_id_from_pnp(obj):
    some_keys = [ '_id', 'deviceInfo', 'systemResetWorkflow', 'systemWorkflow' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_device_by_id_from_pnp(api):
    endpoint_result = api.pnp.delete_device_by_id_from_pnp( path_param_id = '')
    assert is_valid_delete_device_by_id_from_pnp(endpoint_result)


def is_valid_add_device(obj):
    some_keys = [ '_id', 'deviceInfo', 'systemResetWorkflow', 'systemWorkflow' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_add_device(api):
    endpoint_result = api.pnp.add_device( rq__id = None, rq_deviceInfo = None, rq_runSummaryList = None, rq_systemResetWorkflow = None, rq_systemWorkflow = None, rq_tenantId = None, rq_version = None, rq_workflow = None, rq_workflowParameters = None)
    assert is_valid_add_device(endpoint_result)


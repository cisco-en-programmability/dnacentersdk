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
import calendar
import time
from tests.config import (NEW_VIRTUAL_ACCOUNT_PAYLOAD, SYNC_VIRTUAL_ACCOUNT_PAYLOAD,
                          DOMAIN_VIRTUAL_ACCOUNT, NAME_VIRTUAL_ACCOUNT)


def is_valid_get_smart_account_list(obj):
    return len(obj) >= 0 and all([item for item in obj])


def get_smart_account_list(api):
    endpoint_result = api.pnp.get_smart_account_list(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_smart_account_list(api):
    assert is_valid_get_smart_account_list(
        get_smart_account_list(api)
    )


def is_valid_get_virtual_account_list(obj):
    return len(obj) >= 0 and all([item for item in obj])


def get_virtual_account_list(api):
    endpoint_result = api.pnp.get_virtual_account_list(
        domain=get_smart_account_list(api)[0],
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_virtual_account_list(api):
    assert is_valid_get_virtual_account_list(
        get_virtual_account_list(api)
    )


def is_valid_get_sync_result_for_virtual_account(obj):
    some_keys = ['virtualAccountId', 'autoSyncPeriod', 'syncResultStr', 'profile', 'ccoUser']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_sync_result_for_virtual_account(api):
    endpoint_result = api.pnp.get_sync_result_for_virtual_account(
        domain=get_smart_account_list(api)[0],
        name=get_virtual_account_list(api)[0],
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_sync_result_for_virtual_account(api):
    assert is_valid_get_sync_result_for_virtual_account(
        get_sync_result_for_virtual_account(api)
    )


def is_valid_add_virtual_account(obj):
    some_keys = ['virtualAccountId', 'autoSyncPeriod', 'syncResultStr', 'profile', 'ccoUser']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def add_virtual_account(api):
    endpoint_result = api.pnp.add_virtual_account(
        autoSyncPeriod=None,
        ccoUser=None,
        expiry=None,
        lastSync=None,
        profile=None,
        smartAccountId=None,
        syncResult=None,
        syncResultStr=None,
        syncStartTime=None,
        syncStatus=None,
        tenantId=None,
        token=None,
        virtualAccountId=None,
        payload=NEW_VIRTUAL_ACCOUNT_PAYLOAD,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([NEW_VIRTUAL_ACCOUNT_PAYLOAD]) is True,
                    reason="tests.config values required not present")
def test_add_virtual_account(api):
    assert is_valid_add_virtual_account(
        add_virtual_account(api)
    )


def is_valid_sync_virtual_account_devices(obj):
    some_keys = ['virtualAccountId', 'autoSyncPeriod', 'syncResultStr', 'profile', 'ccoUser']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def sync_virtual_account_devices(api):
    endpoint_result = api.pnp.sync_virtual_account_devices(
        autoSyncPeriod=None,
        ccoUser=None,
        expiry=None,
        lastSync=None,
        profile=None,
        smartAccountId=None,
        syncResult=None,
        syncResultStr=None,
        syncStartTime=None,
        syncStatus=None,
        tenantId=None,
        token=None,
        virtualAccountId=None,
        payload=SYNC_VIRTUAL_ACCOUNT_PAYLOAD,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([SYNC_VIRTUAL_ACCOUNT_PAYLOAD]) is True,
                    reason="tests.config values required not present")
def test_sync_virtual_account_devices(api):
    assert is_valid_sync_virtual_account_devices(
        sync_virtual_account_devices(api)
    )


def is_valid_deregister_virtual_account(obj):
    some_keys = ['virtualAccountId', 'autoSyncPeriod', 'syncResultStr', 'profile', 'ccoUser']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def deregister_virtual_account(api):
    endpoint_result = api.pnp.deregister_virtual_account(
        domain=DOMAIN_VIRTUAL_ACCOUNT,
        name=NAME_VIRTUAL_ACCOUNT,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([DOMAIN_VIRTUAL_ACCOUNT, NAME_VIRTUAL_ACCOUNT]) is True,
                    reason="tests.config values required not present")
def test_deregister_virtual_account(api):
    assert is_valid_deregister_virtual_account(
        deregister_virtual_account(api)
    )


def is_valid_get_workflow_count(obj):
    some_keys = ['response']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_workflow_count(api):
    endpoint_result = api.pnp.get_workflow_count(
        name=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_get_workflow_count(api):
    assert is_valid_get_workflow_count(
        get_workflow_count(api)
    )


def is_valid_get_workflows(obj):
    return len(obj) >= 0 and all([item for item in obj])


def get_workflows(api):
    endpoint_result = api.pnp.get_workflows(
        limit=None,
        name=None,
        offset=None,
        sort='addedOn',
        sort_order='des',
        type=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_get_workflows(api):
    assert is_valid_get_workflows(
        get_workflows(api)
    )


def is_valid_get_pnp_global_settings(obj):
    some_keys = ['savaMappingList', 'taskTimeOuts', 'tenantId', 'aaaCredentials', 'defaultProfile']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_pnp_global_settings(api):
    endpoint_result = api.pnp.get_pnp_global_settings(
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_get_pnp_global_settings(api):
    assert is_valid_get_pnp_global_settings(
        get_pnp_global_settings(api)
    )


def is_valid_get_device_count(obj):
    some_keys = ['response']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_count(api):
    endpoint_result = api.pnp.get_device_count(
        cm_state=None,
        last_contact=None,
        name=None,
        onb_state=None,
        pid=None,
        project_id=None,
        project_name=None,
        serial_number=None,
        smart_account_id=None,
        source=None,
        state=None,
        virtual_account_id=None,
        workflow_id=None,
        workflow_name=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_get_device_count(api):
    assert is_valid_get_device_count(
        get_device_count(api)
    )


def is_valid_import_devices_in_bulk(obj):
    some_keys = ['successList', 'failureList']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def import_devices_in_bulk(api):
    endpoint_result = api.pnp.import_devices_in_bulk(
        payload=[{
            "deviceInfo": {
                "serialNumber": "c3160d2650",
                "name": "Test device c3160d2650"
            }
        }],
        active_validation=True
    )
    return endpoint_result


def test_import_devices_in_bulk(api):
    assert is_valid_import_devices_in_bulk(
        import_devices_in_bulk(api)
    )


def is_valid_get_device_list(obj):
    return len(obj) >= 0 and all([item for item in obj])


def get_device_list(api):
    endpoint_result = api.pnp.get_device_list(
        cm_state=None,
        last_contact=None,
        limit=1,
        name=None,
        offset=None,
        onb_state=None,
        pid=None,
        project_id=None,
        project_name=None,
        serial_number=None,
        smart_account_id=None,
        sort=None,
        sort_order=None,
        source=None,
        state=None,
        virtual_account_id=None,
        workflow_id=None,
        workflow_name=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_get_device_list(api):
    assert is_valid_get_device_list(
        get_device_list(api)
    )


def is_valid_get_device_by_id(obj):
    some_keys = ['_id', 'deviceInfo', 'systemResetWorkflow', 'systemWorkflow', 'workflow']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_by_id(api):
    endpoint_result = api.pnp.get_device_by_id(
        id=get_device_list(api)[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_get_device_by_id(api):
    assert is_valid_get_device_by_id(
        get_device_by_id(api)
    )


def is_valid_get_device_history(obj):
    some_keys = ['response', 'statusCode']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_history(api):
    endpoint_result = api.pnp.get_device_history(
        serial_number=get_device_list(api)[0].deviceInfo.serialNumber,
        sort=None,
        sort_order=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_get_device_history(api):
    assert is_valid_get_device_history(
        get_device_history(api)
    )


def is_valid_claim_a_device_to_a_site(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def claim_a_device_to_a_site(api):
    endpoint_result = api.pnp.claim_a_device_to_a_site(
        deviceId=api.pnp.get_device_list(name='Test device c3160d2650')[0].id,
        siteId='1',
        type='Default',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_claim_a_device_to_a_site(api):
    assert is_valid_claim_a_device_to_a_site(
        claim_a_device_to_a_site(api)
    )


def is_valid_preview_config(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def preview_config(api):
    endpoint_result = api.pnp.preview_config(
        deviceId=api.pnp.get_device_list(name='Test device c3160d2650')[0].id,
        siteId='1',
        type='Default',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_preview_config(api):
    assert is_valid_preview_config(
        preview_config(api)
    )


def is_valid_delete_device_by_id_from_pnp_imported(obj):
    some_keys = ['_id', 'deviceInfo', 'systemResetWorkflow', 'systemWorkflow', 'workflow']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_device_by_id_from_pnp_imported(api):
    endpoint_result = api.pnp.delete_device_by_id_from_pnp(
        id=api.pnp.get_device_list(name='Test device c3160d2650')[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_delete_device_by_id_from_pnp_imported(api):
    assert is_valid_delete_device_by_id_from_pnp_imported(
        delete_device_by_id_from_pnp_imported(api)
    )


def is_valid_add_device(obj):
    some_keys = ['_id', 'deviceInfo', 'systemResetWorkflow', 'systemWorkflow', 'workflow']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def add_device(api):
    endpoint_result = api.pnp.add_device(
        _id=None,
        deviceInfo={'serialNumber': 'd2650c3160', 'name': 'Test device d2650c3160'},
        runSummaryList=None,
        systemResetWorkflow=None,
        systemWorkflow=None,
        tenantId=None,
        version=None,
        workflow=None,
        workflowParameters=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_add_device(api):
    assert is_valid_add_device(
        add_device(api)
    )


def is_valid_update_device(obj):
    some_keys = ['_id', 'deviceInfo', 'systemResetWorkflow', 'systemWorkflow', 'workflow']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_device(api):
    endpoint_result = api.pnp.update_device(
        id=api.pnp.get_device_list(name='Test device d2650c3160')[0].id,
        _id=None,
        deviceInfo={'name': 'Test device d2650c3160-1'},
        runSummaryList=None,
        systemResetWorkflow=None,
        systemWorkflow=None,
        tenantId=None,
        version=None,
        workflow=None,
        workflowParameters=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_update_device(api):
    assert is_valid_update_device(
        update_device(api)
    )


def is_valid_add_a_workflow(obj):
    some_keys = ['_id', 'state', 'type', 'description', 'lastupdateOn']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def add_a_workflow(api):
    endpoint_result = api.pnp.add_a_workflow(
        _id=None,
        addToInventory=None,
        addedOn=None,
        configId=None,
        currTaskIdx=None,
        description='test_devnet',
        endTime=None,
        execTime=None,
        imageId=None,
        instanceType=None,
        lastupdateOn=None,
        name='test_devnet',
        startTime=None,
        state=None,
        tasks=api.pnp.get_workflows()[0].tasks[0:1],
        tenantId=None,
        type='Standard',
        useState='Available',
        version=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_add_a_workflow(api):
    assert is_valid_add_a_workflow(
        add_a_workflow(api)
    )


def is_valid_get_workflow_by_id(obj):
    some_keys = ['_id', 'state', 'type', 'description', 'lastupdateOn']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_workflow_by_id(api):
    endpoint_result = api.pnp.get_workflow_by_id(
        id=get_workflows(api)[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_get_workflow_by_id(api):
    assert is_valid_get_workflow_by_id(
        get_workflow_by_id(api)
    )


def is_valid_update_workflow(obj):
    some_keys = ['_id', 'state', 'type', 'description', 'lastupdateOn']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_workflow(api):
    endpoint_result = api.pnp.update_workflow(
        id=api.pnp.get_workflows(name='test_devnet')[0].id,
        _id=None,
        addToInventory=None,
        addedOn=None,
        configId=None,
        currTaskIdx=None,
        description='test_devnet workflow',
        endTime=None,
        execTime=None,
        imageId=None,
        instanceType=None,
        lastupdateOn=None,
        name='test_devnet',
        startTime=None,
        state=None,
        tasks=api.pnp.get_workflows(name='test_devnet')[0].tasks,
        tenantId=None,
        type='Standard',
        useState='Available',
        version=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_update_workflow(api):
    assert is_valid_update_workflow(
        update_workflow(api)
    )


def is_valid_claim_device(obj):
    some_keys = ['jsonArrayResponse', 'jsonResponse', 'message', 'statusCode']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def claim_device(api):
    endpoint_result = api.pnp.claim_device(
        configFileUrl=None,
        configId=None,
        deviceClaimList=[
            {
                "configList": [
                    api.pnp.get_workflows(name='test_devnet')[0].tasks[0].configInfo
                ],
                "deviceId": api.pnp.get_device_list(name='Test device d2650c3160-1')[0].id
            }
        ],
        fileServiceId=None,
        imageId=None,
        imageUrl=None,
        populateInventory=None,
        projectId=None,
        workflowId=api.pnp.get_workflows(name='test_devnet')[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_claim_device(api):
    assert is_valid_claim_device(
        claim_device(api)
    )


def is_valid_un_claim_device(obj):
    some_keys = ['jsonArrayResponse', 'jsonResponse', 'message', 'statusCode']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def un_claim_device(api):
    endpoint_result = api.pnp.un_claim_device(
        deviceIdList=[api.pnp.get_device_list(name='Test device d2650c3160-1')[0].id],
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_un_claim_device(api):
    assert is_valid_un_claim_device(
        un_claim_device(api)
    )


def is_valid_reset_device(obj):
    some_keys = ['jsonArrayResponse', 'jsonResponse', 'message', 'statusCode']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def reset_device(api):
    endpoint_result = api.pnp.reset_device(
        deviceResetList=[
            {
                "configList": [
                    api.pnp.get_workflows(name='test_devnet')[0].tasks[0].configInfo
                ],
                "deviceId": api.pnp.get_device_list(name='Test device d2650c3160-1')[0].id
            }
        ],
        projectId=None,
        workflowId=api.pnp.get_workflows(name='test_devnet')[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_reset_device(api):
    assert is_valid_reset_device(
        reset_device(api)
    )


def is_valid_delete_workflow_by_id(obj):
    some_keys = ['_id', 'state', 'type', 'description', 'lastupdateOn']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_workflow_by_id(api):
    endpoint_result = api.pnp.delete_workflow_by_id(
        id=api.pnp.get_workflows(name='test_devnet')[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_delete_workflow_by_id(api):
    assert is_valid_delete_workflow_by_id(
        delete_workflow_by_id(api)
    )


def is_valid_update_pnp_server_profile(obj):
    some_keys = ['virtualAccountId', 'autoSyncPeriod', 'syncResultStr', 'profile', 'ccoUser']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_pnp_server_profile(api):
    endpoint_result = api.pnp.update_pnp_server_profile(
        autoSyncPeriod=None,
        ccoUser=None,
        expiry=None,
        lastSync=None,
        profile={'addressFqdn': '', 'addressIpV4': '', 'name': ''},
        smartAccountId='',
        syncResult=None,
        syncResultStr=None,
        syncStartTime=None,
        syncStatus='SYNCING',
        tenantId=None,
        token=None,
        virtualAccountId='',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_update_pnp_server_profile(api):
    assert is_valid_update_pnp_server_profile(
        update_pnp_server_profile(api)
    )


def is_valid_update_pnp_global_settings(obj):
    some_keys = ['savaMappingList', 'taskTimeOuts', 'tenantId', 'aaaCredentials', 'defaultProfile']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_pnp_global_settings(api):
    endpoint_result = api.pnp.update_pnp_global_settings(
        _id=None,
        aaaCredentials=None,
        acceptEula=None,
        defaultProfile={
            "fqdnAddresses": "",
            "proxy": "",
            "cert": "",
            "ipAddresses": "",
            "port": "",
        },
        savaMappingList=[{
            "profile": {
                "addressFqdn": "",
                "addressIpV4": "",
                "name": ""
            },
            "smartAccountId": "",
            "syncStatus": "",
            "virtualAccountId": ""
        }],
        taskTimeOuts=None,
        tenantId=None,
        version=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_update_pnp_global_settings(api):
    assert is_valid_update_pnp_global_settings(
        update_pnp_global_settings(api)
    )


def is_valid_delete_device_by_id_from_pnp_added(obj):
    some_keys = ['_id', 'deviceInfo', 'systemResetWorkflow', 'systemWorkflow', 'workflow']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_device_by_id_from_pnp_added(api):
    endpoint_result = api.pnp.delete_device_by_id_from_pnp(
        id=api.pnp.get_device_list(name='Test device d2650c3160-1')[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


def test_delete_device_by_id_from_pnp_added(api):
    assert is_valid_delete_device_by_id_from_pnp_added(
        delete_device_by_id_from_pnp_added(api)
    )

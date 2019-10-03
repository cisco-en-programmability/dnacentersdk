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
import time
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate
from tests.config import (NEW_VIRTUAL_ACCOUNT_PAYLOAD)


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_get_smart_account_list(obj):
    json_schema_validate('jsd_3cb24acb486b89d2_v1_2_10').validate(obj)
    return True


def get_smart_account_list(api):
    endpoint_result = api.pnp.get_smart_account_list(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_get_smart_account_list(api):
    assert is_valid_get_smart_account_list(
        get_smart_account_list(api)
    )


def is_valid_get_virtual_account_list(obj):
    json_schema_validate('jsd_70a479a6462a9496_v1_2_10').validate(obj)
    return True


def get_virtual_account_list(api):
    endpoint_result = api.pnp.get_virtual_account_list(
        domain=get_smart_account_list(api)[0],
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_get_virtual_account_list(api):
    assert is_valid_get_virtual_account_list(
        get_virtual_account_list(api)
    )


def is_valid_add_virtual_account(obj):
    json_schema_validate('jsd_1e962af345b8b59f_v1_2_10').validate(obj)
    return True


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
        active_validation=False
    )
    return endpoint_result


@pytest.mark.skipif(not all([NEW_VIRTUAL_ACCOUNT_PAYLOAD]) is True,
                    reason="tests.config values required not present")
@pytest.mark.pnp
def test_add_virtual_account(api):
    assert is_valid_add_virtual_account(
        add_virtual_account(api)
    )


def is_valid_get_sync_result_for_virtual_account(obj):
    json_schema_validate('jsd_0a9c988445cb91c8_v1_2_10').validate(obj)
    return True


def get_sync_result_for_virtual_account(api):
    endpoint_result = api.pnp.get_sync_result_for_virtual_account(
        domain=get_smart_account_list(api)[0],
        name=get_virtual_account_list(api)[0],
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_get_sync_result_for_virtual_account(api):
    assert is_valid_get_sync_result_for_virtual_account(
        get_sync_result_for_virtual_account(api)
    )


def is_valid_update_pnp_server_profile(obj):
    json_schema_validate('jsd_6f9819e84178870c_v1_2_10').validate(obj)
    return True


def update_pnp_server_profile(api):
    endpoint_result = api.pnp.update_pnp_server_profile(
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
        payload=get_sync_result_for_virtual_account(api),
        active_validation=False
    )
    return endpoint_result


@pytest.mark.pnp
def test_update_pnp_server_profile(api):
    assert is_valid_update_pnp_server_profile(
        update_pnp_server_profile(api)
    )


def is_valid_sync_virtual_account_devices(obj):
    json_schema_validate('jsd_a4b6c87a4ffb9efa_v1_2_10').validate(obj)
    return True


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
        payload=get_sync_result_for_virtual_account(api),
        active_validation=False
    )
    return endpoint_result


@pytest.mark.pnp
def test_sync_virtual_account_devices(api):
    assert is_valid_sync_virtual_account_devices(
        sync_virtual_account_devices(api)
    )


def is_valid_deregister_virtual_account(obj):
    json_schema_validate('jsd_2499e9ad42e8ae5b_v1_2_10').validate(obj)
    return True


def deregister_virtual_account(api):
    time.sleep(10)
    endpoint_result = api.pnp.deregister_virtual_account(
        domain=get_smart_account_list(api)[0],
        name=get_virtual_account_list(api)[0],
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_deregister_virtual_account(api):
    assert is_valid_deregister_virtual_account(
        deregister_virtual_account(api)
    )


def is_valid_get_workflow_count(obj):
    json_schema_validate('jsd_7989f86846faaf99_v1_2_10').validate(obj)
    return True


def get_workflow_count(api):
    endpoint_result = api.pnp.get_workflow_count(
        name=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_get_workflow_count(api):
    assert is_valid_get_workflow_count(
        get_workflow_count(api)
    )


def is_valid_get_workflows(obj):
    json_schema_validate('jsd_aeb4dad04a99bbe3_v1_2_10').validate(obj)
    return True


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


@pytest.mark.pnp
def test_get_workflows(api):
    assert is_valid_get_workflows(
        get_workflows(api)
    )


def is_valid_get_pnp_global_settings(obj):
    json_schema_validate('jsd_7e92f9eb46db8320_v1_2_10').validate(obj)
    return True


def get_pnp_global_settings(api):
    endpoint_result = api.pnp.get_pnp_global_settings(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_get_pnp_global_settings(api):
    assert is_valid_get_pnp_global_settings(
        get_pnp_global_settings(api)
    )


def is_valid_update_pnp_global_settings(obj):
    json_schema_validate('jsd_8da0391947088a5a_v1_2_10').validate(obj)
    return True


def update_pnp_global_settings(api):
    endpoint_result = api.pnp.update_pnp_global_settings(
        _id=None,
        aaaCredentials=None,
        acceptEula=None,
        defaultProfile=None,
        savaMappingList=None,
        taskTimeOuts=None,
        tenantId=None,
        version=None,
        payload=get_pnp_global_settings(api),
        active_validation=False
    )
    return endpoint_result


@pytest.mark.pnp
def test_update_pnp_global_settings(api):
    assert is_valid_update_pnp_global_settings(
        update_pnp_global_settings(api)
    )


def is_valid_get_device_count(obj):
    json_schema_validate('jsd_d9a1fa9c4068b23c_v1_2_10').validate(obj)
    return True


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


@pytest.mark.pnp
def test_get_device_count(api):
    assert is_valid_get_device_count(
        get_device_count(api)
    )


def is_valid_import_devices_in_bulk(obj):
    json_schema_validate('jsd_21a6db2540298f55_v1_2_10').validate(obj)
    return True


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


@pytest.mark.pnp
def test_import_devices_in_bulk(api):
    assert is_valid_import_devices_in_bulk(
        import_devices_in_bulk(api)
    )


def is_valid_get_device_list(obj):
    json_schema_validate('jsd_e6b3db8046c99654_v1_2_10').validate(obj)
    return True


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


@pytest.mark.pnp
def test_get_device_list(api):
    assert is_valid_get_device_list(
        get_device_list(api)
    )


def is_valid_get_device_by_id(obj):
    json_schema_validate('jsd_bab6c9e5440885cc_v1_2_10').validate(obj)
    return True


def get_device_by_id(api):
    endpoint_result = api.pnp.get_device_by_id(
        id=get_device_list(api)[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_get_device_by_id(api):
    assert is_valid_get_device_by_id(
        get_device_by_id(api)
    )


def is_valid_get_device_history(obj):
    json_schema_validate('jsd_f09319674049a7d4_v1_2_10').validate(obj)
    return True


def get_device_history(api):
    endpoint_result = api.pnp.get_device_history(
        serial_number=get_device_list(api)[0].deviceInfo.serialNumber,
        sort=None,
        sort_order=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_get_device_history(api):
    assert is_valid_get_device_history(
        get_device_history(api)
    )


def is_valid_add_device_2(obj):
    json_schema_validate('jsd_f3b26b5544cabab9_v1_2_10').validate(obj)
    return True


def add_device_2(api):
    endpoint_result = api.pnp.add_device(
        _id=None,
        deviceInfo={'serialNumber': 'FJC2048D0HX', 'name': 'catalyst_ap_test', 'pid': 'ISR4431-SEC/K9'},
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


@pytest.mark.pnp
def test_add_device_2(api):
    assert is_valid_add_device_2(
        add_device_2(api)
    )


def is_valid_preview_config(obj):
    json_schema_validate('jsd_cf9418234d9ab37e_v1_2_10').validate(obj)
    return True


def preview_config(api):
    sites = api.sites.get_site_health(timestamp=None).response
    sites = list(filter(lambda x: x.siteType == 'building', sites))
    siteId = sites[-1].siteId if len(sites) > 0 else "1"
    endpoint_result = api.pnp.preview_config(
        deviceId=api.pnp.get_device_list(name='catalyst_ap_test')[0].id,
        siteId=siteId,
        type='Default',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_preview_config(api):
    assert is_valid_preview_config(
        preview_config(api)
    )


def is_valid_claim_a_device_to_a_site(obj):
    json_schema_validate('jsd_5889fb844939a13b_v1_2_10').validate(obj)
    return True


def claim_a_device_to_a_site(api):
    sites = api.sites.get_site_health(timestamp=None).response
    sites = list(filter(lambda x: x.siteType == 'building', sites))
    siteId = sites[-1].siteId if len(sites) > 0 else "1"
    deviceId = api.pnp.get_device_list(name='catalyst_ap_test')[0].id
    endpoint_result = api.pnp.claim_a_device_to_a_site(
        deviceId=None,
        siteId=None,
        type=None,
        payload={
            "siteId": siteId,
            "deviceId": deviceId,
            "type": "Default",
            "imageInfo": {"imageId": "", "skip": False},
            "configInfo": {"configId": "", "configParameters": []}
        },
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_claim_a_device_to_a_site(api):
    assert is_valid_claim_a_device_to_a_site(
        claim_a_device_to_a_site(api)
    )


def is_valid_delete_device_by_id_from_pnp_imported(obj):
    json_schema_validate('jsd_cdab9b474899ae06_v1_2_10').validate(obj)
    return True


def delete_device_by_id_from_pnp_imported(api):
    endpoint_result = api.pnp.delete_device_by_id_from_pnp(
        id=api.pnp.get_device_list(name='Test device c3160d2650')[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_delete_device_by_id_from_pnp_imported(api):
    assert is_valid_delete_device_by_id_from_pnp_imported(
        delete_device_by_id_from_pnp_imported(api)
    )


def is_valid_add_device(obj):
    json_schema_validate('jsd_f3b26b5544cabab9_v1_2_10').validate(obj)
    return True


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


@pytest.mark.pnp
def test_add_device(api):
    assert is_valid_add_device(
        add_device(api)
    )


def is_valid_update_device(obj):
    json_schema_validate('jsd_09b0f9ce4239ae10_v1_2_10').validate(obj)
    return True


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


@pytest.mark.pnp
def test_update_device(api):
    assert is_valid_update_device(
        update_device(api)
    )


def is_valid_add_a_workflow(obj):
    json_schema_validate('jsd_848b5a7b4f9b8c12_v1_2_10').validate(obj)
    return True


def add_a_workflow(api):
    projects = api.template_programmer.get_projects()
    filtered_project = list(filter(lambda x: x.name == 'Onboarding Configuration', projects))
    endpoint_result = api.template_programmer.create_template(
        project_id=filtered_project[0].id,
        composite=False,
        containingTemplates=[],
        deviceTypes=[
            {
                "productFamily": "Switches and Hubs",
            }
        ],
        name='test_template_05',
        rollbackTemplateContent='',
        rollbackTemplateParams=[],
        softwareType='IOS-XE',
        softwareVariant='XE',
        templateContent='show version\n',
        templateParams=[],
        active_validation=True
    )
    time.sleep(10)
    task = api.task.get_task_by_id(endpoint_result.response.taskId).response
    template = api.template_programmer.get_template_details(template_id=task.data)
    api.template_programmer.version_template(templateId=template.id)
    api.template_programmer.preview_template(templateId=template.id)
    endpoint_result = api.pnp.add_a_workflow(
        _id=None,
        addToInventory=None,
        addedOn=None,
        configId=None,
        currTaskIdx=None,
        description='test_devnet_1',
        endTime=None,
        execTime=None,
        imageId=None,
        instanceType=None,
        lastupdateOn=None,
        name='test_devnet_1',
        startTime=None,
        state=None,
        tasks=[{
            'taskSeqNo': 0,
            'name': 'Config Download',
            'type': 'Config',
            'startTime': 0,
            'endTime': 0,
            'timeTaken': 0,
            'currWorkItemIdx': 0,
            'configInfo': {
                'configId': template.id,
                'configFileUrl': None,
                'fileServiceId': None,
                'saveToStartUp': True,
                'connLossRollBack': True,
                'configParameters': None
            }
        }],
        tenantId=None,
        type='Standard',
        useState='Available',
        version=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_add_a_workflow(api):
    assert is_valid_add_a_workflow(
        add_a_workflow(api)
    )


def is_valid_get_workflow_by_id(obj):
    json_schema_validate('jsd_80acb88e4ac9ac6d_v1_2_10').validate(obj)
    return True


def get_workflow_by_id(api):
    endpoint_result = api.pnp.get_workflow_by_id(
        id=get_workflows(api)[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_get_workflow_by_id(api):
    assert is_valid_get_workflow_by_id(
        get_workflow_by_id(api)
    )


def is_valid_update_workflow(obj):
    json_schema_validate('jsd_3086c9624f498b85_v1_2_10').validate(obj)
    return True


def update_workflow(api):
    workflow = api.pnp.get_workflows(name='test_devnet_1')[0]
    endpoint_result = api.pnp.update_workflow(
        id=workflow.id,
        _id=None,
        addToInventory=None,
        addedOn=None,
        configId=None,
        currTaskIdx=None,
        description=workflow.description,
        endTime=None,
        execTime=None,
        imageId=None,
        instanceType=None,
        lastupdateOn=None,
        name=workflow.name,
        startTime=None,
        state=None,
        tasks=workflow.tasks,
        tenantId=None,
        type=workflow.type,
        useState=workflow.useState,
        version=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_update_workflow(api):
    assert is_valid_update_workflow(
        update_workflow(api)
    )


def is_valid_claim_device(obj):
    json_schema_validate('jsd_d8a619974a8a8c48_v1_2_10').validate(obj)
    return True


def claim_device(api):
    workflow = api.pnp.get_workflows(name='test_devnet_1')[0]
    configList = [workflow.tasks[0].configInfo]
    deviceId = api.pnp.get_device_list(name='catalyst_ap_test')[0].id
    endpoint_result = api.pnp.claim_device(
        configFileUrl=None,
        configId=None,
        deviceClaimList=[
            {
                "configList": configList,
                "deviceId": deviceId
            }
        ],
        fileServiceId=None,
        imageId=None,
        imageUrl=None,
        populateInventory=None,
        projectId=None,
        workflowId=workflow.id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_claim_device(api):
    assert is_valid_claim_device(
        claim_device(api)
    )


def is_valid_un_claim_device(obj):
    json_schema_validate('jsd_0b836b7b4b6a9fd5_v1_2_10').validate(obj)
    return True


def un_claim_device(api):
    deviceId = api.pnp.get_device_list(name='catalyst_ap_test')[0].id
    endpoint_result = api.pnp.un_claim_device(
        deviceIdList=[deviceId],
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_un_claim_device(api):
    assert is_valid_un_claim_device(
        un_claim_device(api)
    )


def is_valid_reset_device(obj):
    json_schema_validate('jsd_9e857b5a4a0bbcdb_v1_2_10').validate(obj)
    return True


def reset_device(api):
    workflow = api.pnp.get_workflows(name='test_devnet_1')[0]
    deviceId = api.pnp.get_device_list(name='catalyst_ap_test')[0].id
    try:
        endpoint_result = api.pnp.reset_device(
            deviceResetList=[{"deviceId": deviceId, "configList": [workflow.tasks[0].configInfo]}],
            projectId=None,
            workflowId=workflow.id,
            payload=None,
            active_validation=True
        )

    except Exception as e:
        assert(e.status_code == 400)
        assert('Invalid request for resetting' in e.message)
        endpoint_result = api.pnp._object_factory('', json_data={'message': e.message})
    return endpoint_result


@pytest.mark.pnp
def test_reset_device(api):
    assert is_valid_reset_device(
        reset_device(api)
    )


def is_valid_delete_workflow_by_id(obj):
    json_schema_validate('jsd_af8d7b0e470b8ae2_v1_2_10').validate(obj)
    return True


def delete_workflow_by_id(api):
    projects = api.template_programmer.get_projects()
    filtered_project = list(filter(lambda x: x.name == 'Onboarding Configuration', projects))
    templates = api.template_programmer.gets_the_templates_available(project_id=filtered_project[0].id)
    for template in templates:
        if 'test_template' in template.name:
            api.template_programmer.delete_template(template_id=template.templateId)
    endpoint_result = api.pnp.delete_workflow_by_id(
        id=api.pnp.get_workflows(name='test_devnet_1')[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_delete_workflow_by_id(api):
    assert is_valid_delete_workflow_by_id(
        delete_workflow_by_id(api)
    )


def is_valid_delete_device_by_id_from_pnp_added(obj):
    json_schema_validate('jsd_cdab9b474899ae06_v1_2_10').validate(obj)
    return True


def delete_device_by_id_from_pnp_added(api):
    endpoint_result = api.pnp.delete_device_by_id_from_pnp(
        id=api.pnp.get_device_list(name='Test device d2650c3160-1')[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_delete_device_by_id_from_pnp_added(api):
    assert is_valid_delete_device_by_id_from_pnp_added(
        delete_device_by_id_from_pnp_added(api)
    )


def is_valid_delete_device_by_id_from_pnp_added_2(obj):
    json_schema_validate('jsd_cdab9b474899ae06_v1_2_10').validate(obj)
    return True


def delete_device_by_id_from_pnp_added_2(api):
    endpoint_result = api.pnp.delete_device_by_id_from_pnp(
        id=api.pnp.get_device_list(name='catalyst_ap_test')[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.pnp
def test_delete_device_by_id_from_pnp_added_2(api):
    assert is_valid_delete_device_by_id_from_pnp_added_2(
        delete_device_by_id_from_pnp_added_2(api)
    )

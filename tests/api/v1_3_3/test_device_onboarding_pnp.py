# -*- coding: utf-8 -*-
"""DNACenterAPI device_onboarding_pnp API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.3', reason='version does not match')


def is_valid_get_sync_result_for_virtual_account(obj):
    json_schema_validate('jsd_0a9c988445cb91c8_v1_3_3').validate(obj)
    return True


def get_sync_result_for_virtual_account(api):
    endpoint_result = api.device_onboarding_pnp.get_sync_result_for_virtual_account(
        domain='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_sync_result_for_virtual_account(api):
    assert is_valid_get_sync_result_for_virtual_account(
        get_sync_result_for_virtual_account(api)
    )


def get_sync_result_for_virtual_account_default(api):
    endpoint_result = api.device_onboarding_pnp.get_sync_result_for_virtual_account(
        domain='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_sync_result_for_virtual_account_default(api):
    try:
        assert is_valid_get_sync_result_for_virtual_account(
            get_sync_result_for_virtual_account_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_un_claim_device(obj):
    json_schema_validate('jsd_0b836b7b4b6a9fd5_v1_3_3').validate(obj)
    return True


def un_claim_device(api):
    endpoint_result = api.device_onboarding_pnp.un_claim_device(
        active_validation=True,
        deviceIdList=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_un_claim_device(api):
    assert is_valid_un_claim_device(
        un_claim_device(api)
    )


def un_claim_device_default(api):
    endpoint_result = api.device_onboarding_pnp.un_claim_device(
        active_validation=True,
        deviceIdList=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_un_claim_device_default(api):
    try:
        assert is_valid_un_claim_device(
            un_claim_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_device(obj):
    json_schema_validate('jsd_09b0f9ce4239ae10_v1_3_3').validate(obj)
    return True


def update_device(api):
    endpoint_result = api.device_onboarding_pnp.update_device(
        _id='string',
        active_validation=True,
        deviceInfo={'aaaCredentials': {'password': 'string', 'username': 'string'}, 'addedOn': 0, 'addnMacAddrs': ['string'], 'agentType': 'POSIX', 'authStatus': 'string', 'authenticatedSudiSerialNo': 'string', 'capabilitiesSupported': ['string'], 'cmState': 'NotContacted', 'description': 'string', 'deviceSudiSerialNos': ['string'], 'deviceType': 'string', 'featuresSupported': ['string'], 'fileSystemList': [{'freespace': 0, 'name': 'string', 'readable': True, 'size': 0, 'type': 'string', 'writeable': True}], 'firstContact': 0, 'hostname': 'string', 'httpHeaders': [{'key': 'string', 'value': 'string'}], 'imageFile': 'string', 'imageVersion': 'string', 'ipInterfaces': [{'ipv4Address': {}, 'ipv6AddressList': [{}], 'macAddress': 'string', 'name': 'string', 'status': 'string'}], 'lastContact': 0, 'lastSyncTime': 0, 'lastUpdateOn': 0, 'location': {'address': 'string', 'altitude': 'string', 'latitude': 'string', 'longitude': 'string', 'siteId': 'string'}, 'macAddress': 'string', 'mode': 'string', 'name': 'string', 'neighborLinks': [{'localInterfaceName': 'string', 'localMacAddress': 'string', 'localShortInterfaceName': 'string', 'remoteDeviceName': 'string', 'remoteInterfaceName': 'string', 'remoteMacAddress': 'string', 'remotePlatform': 'string', 'remoteShortInterfaceName': 'string', 'remoteVersion': 'string'}], 'onbState': 'NotContacted', 'pid': 'string', 'pnpProfileList': [{'createdBy': 'string', 'discoveryCreated': True, 'primaryEndpoint': {'certificate': 'string', 'fqdn': 'string', 'ipv4Address': {}, 'ipv6Address': {}, 'port': 0, 'protocol': 'string'}, 'profileName': 'string', 'secondaryEndpoint': {'certificate': 'string', 'fqdn': 'string', 'ipv4Address': {}, 'ipv6Address': {}, 'port': 0, 'protocol': 'string'}}], 'populateInventory': True, 'preWorkflowCliOuputs': [{'cli': 'string', 'cliOutput': 'string'}], 'projectId': 'string', 'projectName': 'string', 'reloadRequested': True, 'serialNumber': 'string', 'smartAccountId': 'string', 'source': 'string', 'stack': True, 'stackInfo': {'isFullRing': True, 'stackMemberList': [{'hardwareVersion': 'string', 'licenseLevel': 'string', 'licenseType': 'string', 'macAddress': 'string', 'pid': 'string', 'priority': 0, 'role': 'string', 'serialNumber': 'string', 'softwareVersion': 'string', 'stackNumber': 0, 'state': 'string', 'sudiSerialNumber': 'string'}], 'stackRingProtocol': 'string', 'supportsStackWorkflows': True, 'totalMemberCount': 0, 'validLicenseLevels': ['string']}, 'state': 'Unclaimed', 'sudiRequired': True, 'tags': {}, 'userSudiSerialNos': ['string'], 'virtualAccountId': 'string', 'workflowId': 'string', 'workflowName': 'string'},
        id='string',
        payload=None,
        runSummaryList=[{'details': 'string', 'errorFlag': True, 'historyTaskInfo': {'addnDetails': [{'key': 'string', 'value': 'string'}], 'name': 'string', 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}, 'timestamp': 0}],
        systemResetWorkflow={'_id': 'string', 'addToInventory': True, 'addedOn': 0, 'configId': 'string', 'currTaskIdx': 0, 'description': 'string', 'endTime': 0, 'execTime': 0, 'imageId': 'string', 'instanceType': 'SystemWorkflow', 'lastupdateOn': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'tasks': [{'currWorkItemIdx': 0, 'endTime': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'taskSeqNo': 0, 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}], 'tenantId': 'string', 'type': 'string', 'useState': 'string', 'version': 0},
        systemWorkflow={'_id': 'string', 'addToInventory': True, 'addedOn': 0, 'configId': 'string', 'currTaskIdx': 0, 'description': 'string', 'endTime': 0, 'execTime': 0, 'imageId': 'string', 'instanceType': 'SystemWorkflow', 'lastupdateOn': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'tasks': [{'currWorkItemIdx': 0, 'endTime': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'taskSeqNo': 0, 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}], 'tenantId': 'string', 'type': 'string', 'useState': 'string', 'version': 0},
        tenantId='string',
        version=0,
        workflow={'_id': 'string', 'addToInventory': True, 'addedOn': 0, 'configId': 'string', 'currTaskIdx': 0, 'description': 'string', 'endTime': 0, 'execTime': 0, 'imageId': 'string', 'instanceType': 'SystemWorkflow', 'lastupdateOn': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'tasks': [{'currWorkItemIdx': 0, 'endTime': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'taskSeqNo': 0, 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}], 'tenantId': 'string', 'type': 'string', 'useState': 'string', 'version': 0},
        workflowParameters={'configList': [{'configId': 'string', 'configParameters': [{'key': 'string', 'value': 'string'}]}], 'licenseLevel': 'string', 'licenseType': 'string', 'topOfStackSerialNumber': 'string'}
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_update_device(api):
    assert is_valid_update_device(
        update_device(api)
    )


def update_device_default(api):
    endpoint_result = api.device_onboarding_pnp.update_device(
        _id=None,
        active_validation=True,
        deviceInfo=None,
        id='string',
        payload=None,
        runSummaryList=None,
        systemResetWorkflow=None,
        systemWorkflow=None,
        tenantId=None,
        version=None,
        workflow=None,
        workflowParameters=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_update_device_default(api):
    try:
        assert is_valid_update_device(
            update_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_import_devices_in_bulk(obj):
    json_schema_validate('jsd_21a6db2540298f55_v1_3_3').validate(obj)
    return True


def import_devices_in_bulk(api):
    endpoint_result = api.device_onboarding_pnp.import_devices_in_bulk(
        active_validation=True,
        payload=[{'_id': 'string', 'deviceInfo': {'aaaCredentials': {'password': 'string', 'username': 'string'}, 'addedOn': 0, 'addnMacAddrs': ['string'], 'agentType': 'POSIX', 'authStatus': 'string', 'authenticatedSudiSerialNo': 'string', 'capabilitiesSupported': ['string'], 'cmState': 'NotContacted', 'description': 'string', 'deviceSudiSerialNos': ['string'], 'deviceType': 'string', 'featuresSupported': ['string'], 'fileSystemList': [{'freespace': 0, 'name': 'string', 'readable': True, 'size': 0, 'type': 'string', 'writeable': True}], 'firstContact': 0, 'hostname': 'string', 'httpHeaders': [{'key': 'string', 'value': 'string'}], 'imageFile': 'string', 'imageVersion': 'string', 'ipInterfaces': [{'ipv4Address': {}, 'ipv6AddressList': [{}], 'macAddress': 'string', 'name': 'string', 'status': 'string'}], 'lastContact': 0, 'lastSyncTime': 0, 'lastUpdateOn': 0, 'location': {'address': 'string', 'altitude': 'string', 'latitude': 'string', 'longitude': 'string', 'siteId': 'string'}, 'macAddress': 'string', 'mode': 'string', 'name': 'string', 'neighborLinks': [{'localInterfaceName': 'string', 'localMacAddress': 'string', 'localShortInterfaceName': 'string', 'remoteDeviceName': 'string', 'remoteInterfaceName': 'string', 'remoteMacAddress': 'string', 'remotePlatform': 'string', 'remoteShortInterfaceName': 'string', 'remoteVersion': 'string'}], 'onbState': 'NotContacted', 'pid': 'string', 'pnpProfileList': [{'createdBy': 'string', 'discoveryCreated': True, 'primaryEndpoint': {'certificate': 'string', 'fqdn': 'string', 'ipv4Address': {}, 'ipv6Address': {}, 'port': 0, 'protocol': 'string'}, 'profileName': 'string', 'secondaryEndpoint': {'certificate': 'string', 'fqdn': 'string', 'ipv4Address': {}, 'ipv6Address': {}, 'port': 0, 'protocol': 'string'}}], 'populateInventory': True, 'preWorkflowCliOuputs': [{'cli': 'string', 'cliOutput': 'string'}], 'projectId': 'string', 'projectName': 'string', 'reloadRequested': True, 'serialNumber': 'string', 'smartAccountId': 'string', 'source': 'string', 'stack': True, 'stackInfo': {'isFullRing': True, 'stackMemberList': [{'hardwareVersion': 'string', 'licenseLevel': 'string', 'licenseType': 'string', 'macAddress': 'string', 'pid': 'string', 'priority': 0, 'role': 'string', 'serialNumber': 'string', 'softwareVersion': 'string', 'stackNumber': 0, 'state': 'string', 'sudiSerialNumber': 'string'}], 'stackRingProtocol': 'string', 'supportsStackWorkflows': True, 'totalMemberCount': 0, 'validLicenseLevels': ['string']}, 'state': 'Unclaimed', 'sudiRequired': True, 'tags': {}, 'userSudiSerialNos': ['string'], 'virtualAccountId': 'string', 'workflowId': 'string', 'workflowName': 'string'}, 'runSummaryList': [{'details': 'string', 'errorFlag': True, 'historyTaskInfo': {'addnDetails': [{'key': 'string', 'value': 'string'}], 'name': 'string', 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}, 'timestamp': 0}], 'systemResetWorkflow': {'_id': 'string', 'addToInventory': True, 'addedOn': 0, 'configId': 'string', 'currTaskIdx': 0, 'description': 'string', 'endTime': 0, 'execTime': 0, 'imageId': 'string', 'instanceType': 'SystemWorkflow', 'lastupdateOn': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'tasks': [{'currWorkItemIdx': 0, 'endTime': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'taskSeqNo': 0, 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}], 'tenantId': 'string', 'type': 'string', 'useState': 'string', 'version': 0}, 'systemWorkflow': {'_id': 'string', 'addToInventory': True, 'addedOn': 0, 'configId': 'string', 'currTaskIdx': 0, 'description': 'string', 'endTime': 0, 'execTime': 0, 'imageId': 'string', 'instanceType': 'SystemWorkflow', 'lastupdateOn': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'tasks': [{'currWorkItemIdx': 0, 'endTime': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'taskSeqNo': 0, 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}], 'tenantId': 'string', 'type': 'string', 'useState': 'string', 'version': 0}, 'tenantId': 'string', 'version': 0, 'workflow': {'_id': 'string', 'addToInventory': True, 'addedOn': 0, 'configId': 'string', 'currTaskIdx': 0, 'description': 'string', 'endTime': 0, 'execTime': 0, 'imageId': 'string', 'instanceType': 'SystemWorkflow', 'lastupdateOn': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'tasks': [{'currWorkItemIdx': 0, 'endTime': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'taskSeqNo': 0, 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}], 'tenantId': 'string', 'type': 'string', 'useState': 'string', 'version': 0}, 'workflowParameters': {'configList': [{'configId': 'string', 'configParameters': [{'key': 'string', 'value': 'string'}]}], 'licenseLevel': 'string', 'licenseType': 'string', 'topOfStackSerialNumber': 'string'}}]
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_import_devices_in_bulk(api):
    assert is_valid_import_devices_in_bulk(
        import_devices_in_bulk(api)
    )


def import_devices_in_bulk_default(api):
    endpoint_result = api.device_onboarding_pnp.import_devices_in_bulk(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_import_devices_in_bulk_default(api):
    try:
        assert is_valid_import_devices_in_bulk(
            import_devices_in_bulk_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_add_virtual_account(obj):
    json_schema_validate('jsd_1e962af345b8b59f_v1_3_3').validate(obj)
    return True


def add_virtual_account(api):
    endpoint_result = api.device_onboarding_pnp.add_virtual_account(
        active_validation=True,
        autoSyncPeriod=0,
        ccoUser='string',
        expiry=0,
        lastSync=0,
        payload=None,
        profile={'addressFqdn': 'string', 'addressIpV4': 'string', 'cert': 'string', 'makeDefault': True, 'name': 'string', 'port': 0, 'profileId': 'string', 'proxy': True},
        smartAccountId='string',
        syncResult={'syncList': [{'deviceSnList': ['string'], 'syncType': 'Add'}], 'syncMsg': 'string'},
        syncResultStr='string',
        syncStartTime=0,
        syncStatus='NOT_SYNCED',
        tenantId='string',
        token='string',
        virtualAccountId='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_add_virtual_account(api):
    assert is_valid_add_virtual_account(
        add_virtual_account(api)
    )


def add_virtual_account_default(api):
    endpoint_result = api.device_onboarding_pnp.add_virtual_account(
        active_validation=True,
        autoSyncPeriod=None,
        ccoUser=None,
        expiry=None,
        lastSync=None,
        payload=None,
        profile=None,
        smartAccountId=None,
        syncResult=None,
        syncResultStr=None,
        syncStartTime=None,
        syncStatus=None,
        tenantId=None,
        token=None,
        virtualAccountId=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_add_virtual_account_default(api):
    try:
        assert is_valid_add_virtual_account(
            add_virtual_account_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_workflow(obj):
    json_schema_validate('jsd_3086c9624f498b85_v1_3_3').validate(obj)
    return True


def update_workflow(api):
    endpoint_result = api.device_onboarding_pnp.update_workflow(
        _id='string',
        active_validation=True,
        addToInventory=True,
        addedOn=0,
        configId='string',
        currTaskIdx=0,
        description='string',
        endTime=0,
        execTime=0,
        id='string',
        imageId='string',
        instanceType='SystemWorkflow',
        lastupdateOn=0,
        name='string',
        payload=None,
        startTime=0,
        state='string',
        tasks=[{'currWorkItemIdx': 0, 'endTime': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'taskSeqNo': 0, 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}],
        tenantId='string',
        type='string',
        useState='string',
        version=0
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_update_workflow(api):
    assert is_valid_update_workflow(
        update_workflow(api)
    )


def update_workflow_default(api):
    endpoint_result = api.device_onboarding_pnp.update_workflow(
        _id=None,
        active_validation=True,
        addToInventory=None,
        addedOn=None,
        configId=None,
        currTaskIdx=None,
        description=None,
        endTime=None,
        execTime=None,
        id='string',
        imageId=None,
        instanceType=None,
        lastupdateOn=None,
        name=None,
        payload=None,
        startTime=None,
        state=None,
        tasks=None,
        tenantId=None,
        type=None,
        useState=None,
        version=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_update_workflow_default(api):
    try:
        assert is_valid_update_workflow(
            update_workflow_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_deregister_virtual_account(obj):
    json_schema_validate('jsd_2499e9ad42e8ae5b_v1_3_3').validate(obj)
    return True


def deregister_virtual_account(api):
    endpoint_result = api.device_onboarding_pnp.deregister_virtual_account(
        domain='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_deregister_virtual_account(api):
    assert is_valid_deregister_virtual_account(
        deregister_virtual_account(api)
    )


def deregister_virtual_account_default(api):
    endpoint_result = api.device_onboarding_pnp.deregister_virtual_account(
        domain=None,
        name=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_deregister_virtual_account_default(api):
    try:
        assert is_valid_deregister_virtual_account(
            deregister_virtual_account_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_smart_account_list(obj):
    json_schema_validate('jsd_3cb24acb486b89d2_v1_3_3').validate(obj)
    return True


def get_smart_account_list(api):
    endpoint_result = api.device_onboarding_pnp.get_smart_account_list(

    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_smart_account_list(api):
    assert is_valid_get_smart_account_list(
        get_smart_account_list(api)
    )


def get_smart_account_list_default(api):
    endpoint_result = api.device_onboarding_pnp.get_smart_account_list(

    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_smart_account_list_default(api):
    try:
        assert is_valid_get_smart_account_list(
            get_smart_account_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_claim_a_device_to_a_site(obj):
    return True if obj else False


def claim_a_device_to_a_site(api):
    endpoint_result = api.device_onboarding_pnp.claim_a_device_to_a_site(
        active_validation=True,
        deviceId='string',
        payload=None,
        siteId='string',
        type='Default'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_claim_a_device_to_a_site(api):
    assert is_valid_claim_a_device_to_a_site(
        claim_a_device_to_a_site(api)
    )


def claim_a_device_to_a_site_default(api):
    endpoint_result = api.device_onboarding_pnp.claim_a_device_to_a_site(
        active_validation=True,
        deviceId=None,
        payload=None,
        siteId=None,
        type=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_claim_a_device_to_a_site_default(api):
    try:
        assert is_valid_claim_a_device_to_a_site(
            claim_a_device_to_a_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_pnp_server_profile(obj):
    json_schema_validate('jsd_6f9819e84178870c_v1_3_3').validate(obj)
    return True


def update_pnp_server_profile(api):
    endpoint_result = api.device_onboarding_pnp.update_pnp_server_profile(
        active_validation=True,
        autoSyncPeriod=0,
        ccoUser='string',
        expiry=0,
        lastSync=0,
        payload=None,
        profile={'addressFqdn': 'string', 'addressIpV4': 'string', 'cert': 'string', 'makeDefault': True, 'name': 'string', 'port': 0, 'profileId': 'string', 'proxy': True},
        smartAccountId='string',
        syncResult={'syncList': [{'deviceSnList': ['string'], 'syncType': 'Add'}], 'syncMsg': 'string'},
        syncResultStr='string',
        syncStartTime=0,
        syncStatus='NOT_SYNCED',
        tenantId='string',
        token='string',
        virtualAccountId='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_update_pnp_server_profile(api):
    assert is_valid_update_pnp_server_profile(
        update_pnp_server_profile(api)
    )


def update_pnp_server_profile_default(api):
    endpoint_result = api.device_onboarding_pnp.update_pnp_server_profile(
        active_validation=True,
        autoSyncPeriod=None,
        ccoUser=None,
        expiry=None,
        lastSync=None,
        payload=None,
        profile=None,
        smartAccountId=None,
        syncResult=None,
        syncResultStr=None,
        syncStartTime=None,
        syncStatus=None,
        tenantId=None,
        token=None,
        virtualAccountId=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_update_pnp_server_profile_default(api):
    try:
        assert is_valid_update_pnp_server_profile(
            update_pnp_server_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_pnp_global_settings(obj):
    json_schema_validate('jsd_7e92f9eb46db8320_v1_3_3').validate(obj)
    return True


def get_pnp_global_settings(api):
    endpoint_result = api.device_onboarding_pnp.get_pnp_global_settings(

    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_pnp_global_settings(api):
    assert is_valid_get_pnp_global_settings(
        get_pnp_global_settings(api)
    )


def get_pnp_global_settings_default(api):
    endpoint_result = api.device_onboarding_pnp.get_pnp_global_settings(

    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_pnp_global_settings_default(api):
    try:
        assert is_valid_get_pnp_global_settings(
            get_pnp_global_settings_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_workflow_count(obj):
    json_schema_validate('jsd_7989f86846faaf99_v1_3_3').validate(obj)
    return True


def get_workflow_count(api):
    endpoint_result = api.device_onboarding_pnp.get_workflow_count(
        name='value1,value2'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_workflow_count(api):
    assert is_valid_get_workflow_count(
        get_workflow_count(api)
    )


def get_workflow_count_default(api):
    endpoint_result = api.device_onboarding_pnp.get_workflow_count(
        name=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_workflow_count_default(api):
    try:
        assert is_valid_get_workflow_count(
            get_workflow_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_virtual_account_list(obj):
    json_schema_validate('jsd_70a479a6462a9496_v1_3_3').validate(obj)
    return True


def get_virtual_account_list(api):
    endpoint_result = api.device_onboarding_pnp.get_virtual_account_list(
        domain='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_virtual_account_list(api):
    assert is_valid_get_virtual_account_list(
        get_virtual_account_list(api)
    )


def get_virtual_account_list_default(api):
    endpoint_result = api.device_onboarding_pnp.get_virtual_account_list(
        domain='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_virtual_account_list_default(api):
    try:
        assert is_valid_get_virtual_account_list(
            get_virtual_account_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_workflow_by_id(obj):
    json_schema_validate('jsd_80acb88e4ac9ac6d_v1_3_3').validate(obj)
    return True


def get_workflow_by_id(api):
    endpoint_result = api.device_onboarding_pnp.get_workflow_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_workflow_by_id(api):
    assert is_valid_get_workflow_by_id(
        get_workflow_by_id(api)
    )


def get_workflow_by_id_default(api):
    endpoint_result = api.device_onboarding_pnp.get_workflow_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_workflow_by_id_default(api):
    try:
        assert is_valid_get_workflow_by_id(
            get_workflow_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_add_a_workflow(obj):
    json_schema_validate('jsd_848b5a7b4f9b8c12_v1_3_3').validate(obj)
    return True


def add_a_workflow(api):
    endpoint_result = api.device_onboarding_pnp.add_a_workflow(
        _id='string',
        active_validation=True,
        addToInventory=True,
        addedOn=0,
        configId='string',
        currTaskIdx=0,
        description='string',
        endTime=0,
        execTime=0,
        imageId='string',
        instanceType='SystemWorkflow',
        lastupdateOn=0,
        name='string',
        payload=None,
        startTime=0,
        state='string',
        tasks=[{'currWorkItemIdx': 0, 'endTime': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'taskSeqNo': 0, 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}],
        tenantId='string',
        type='string',
        useState='string',
        version=0
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_add_a_workflow(api):
    assert is_valid_add_a_workflow(
        add_a_workflow(api)
    )


def add_a_workflow_default(api):
    endpoint_result = api.device_onboarding_pnp.add_a_workflow(
        _id=None,
        active_validation=True,
        addToInventory=None,
        addedOn=None,
        configId=None,
        currTaskIdx=None,
        description=None,
        endTime=None,
        execTime=None,
        imageId=None,
        instanceType=None,
        lastupdateOn=None,
        name=None,
        payload=None,
        startTime=None,
        state=None,
        tasks=None,
        tenantId=None,
        type=None,
        useState=None,
        version=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_add_a_workflow_default(api):
    try:
        assert is_valid_add_a_workflow(
            add_a_workflow_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_pnp_global_settings(obj):
    json_schema_validate('jsd_8da0391947088a5a_v1_3_3').validate(obj)
    return True


def update_pnp_global_settings(api):
    endpoint_result = api.device_onboarding_pnp.update_pnp_global_settings(
        _id='string',
        aaaCredentials={'password': 'string', 'username': 'string'},
        acceptEula=True,
        active_validation=True,
        defaultProfile={'cert': 'string', 'fqdnAddresses': ['string'], 'ipAddresses': ['string'], 'port': 0, 'proxy': True},
        payload=None,
        savaMappingList=[{'autoSyncPeriod': 0, 'ccoUser': 'string', 'expiry': 0, 'lastSync': 0, 'profile': {'addressFqdn': 'string', 'addressIpV4': 'string', 'cert': 'string', 'makeDefault': True, 'name': 'string', 'port': 0, 'profileId': 'string', 'proxy': True}, 'smartAccountId': 'string', 'syncResult': {'syncList': [{'deviceSnList': ['string'], 'syncType': 'Add'}], 'syncMsg': 'string'}, 'syncResultStr': 'string', 'syncStartTime': 0, 'syncStatus': 'NOT_SYNCED', 'tenantId': 'string', 'token': 'string', 'virtualAccountId': 'string'}],
        taskTimeOuts={'configTimeOut': 0, 'generalTimeOut': 0, 'imageDownloadTimeOut': 0},
        tenantId='string',
        version=0
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_update_pnp_global_settings(api):
    assert is_valid_update_pnp_global_settings(
        update_pnp_global_settings(api)
    )


def update_pnp_global_settings_default(api):
    endpoint_result = api.device_onboarding_pnp.update_pnp_global_settings(
        _id=None,
        aaaCredentials=None,
        acceptEula=None,
        active_validation=True,
        defaultProfile=None,
        payload=None,
        savaMappingList=None,
        taskTimeOuts=None,
        tenantId=None,
        version=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_update_pnp_global_settings_default(api):
    try:
        assert is_valid_update_pnp_global_settings(
            update_pnp_global_settings_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_reset_device(obj):
    json_schema_validate('jsd_9e857b5a4a0bbcdb_v1_3_3').validate(obj)
    return True


def reset_device(api):
    endpoint_result = api.device_onboarding_pnp.reset_device(
        active_validation=True,
        deviceResetList=[{'configList': [{'configId': 'string', 'configParameters': [{'key': 'string', 'value': 'string'}]}], 'deviceId': 'string', 'licenseLevel': 'string', 'licenseType': 'string', 'topOfStackSerialNumber': 'string'}],
        payload=None,
        projectId='string',
        workflowId='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_reset_device(api):
    assert is_valid_reset_device(
        reset_device(api)
    )


def reset_device_default(api):
    endpoint_result = api.device_onboarding_pnp.reset_device(
        active_validation=True,
        deviceResetList=None,
        payload=None,
        projectId=None,
        workflowId=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_reset_device_default(api):
    try:
        assert is_valid_reset_device(
            reset_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_sync_virtual_account_devices(obj):
    json_schema_validate('jsd_a4b6c87a4ffb9efa_v1_3_3').validate(obj)
    return True


def sync_virtual_account_devices(api):
    endpoint_result = api.device_onboarding_pnp.sync_virtual_account_devices(
        active_validation=True,
        autoSyncPeriod=0,
        ccoUser='string',
        expiry=0,
        lastSync=0,
        payload=None,
        profile={'addressFqdn': 'string', 'addressIpV4': 'string', 'cert': 'string', 'makeDefault': True, 'name': 'string', 'port': 0, 'profileId': 'string', 'proxy': True},
        smartAccountId='string',
        syncResult={'syncList': [{'deviceSnList': ['string'], 'syncType': 'Add'}], 'syncMsg': 'string'},
        syncResultStr='string',
        syncStartTime=0,
        syncStatus='NOT_SYNCED',
        tenantId='string',
        token='string',
        virtualAccountId='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_sync_virtual_account_devices(api):
    assert is_valid_sync_virtual_account_devices(
        sync_virtual_account_devices(api)
    )


def sync_virtual_account_devices_default(api):
    endpoint_result = api.device_onboarding_pnp.sync_virtual_account_devices(
        active_validation=True,
        autoSyncPeriod=None,
        ccoUser=None,
        expiry=None,
        lastSync=None,
        payload=None,
        profile=None,
        smartAccountId=None,
        syncResult=None,
        syncResultStr=None,
        syncStartTime=None,
        syncStatus=None,
        tenantId=None,
        token=None,
        virtualAccountId=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_sync_virtual_account_devices_default(api):
    try:
        assert is_valid_sync_virtual_account_devices(
            sync_virtual_account_devices_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_workflow_by_id(obj):
    json_schema_validate('jsd_af8d7b0e470b8ae2_v1_3_3').validate(obj)
    return True


def delete_workflow_by_id(api):
    endpoint_result = api.device_onboarding_pnp.delete_workflow_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_delete_workflow_by_id(api):
    assert is_valid_delete_workflow_by_id(
        delete_workflow_by_id(api)
    )


def delete_workflow_by_id_default(api):
    endpoint_result = api.device_onboarding_pnp.delete_workflow_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_delete_workflow_by_id_default(api):
    try:
        assert is_valid_delete_workflow_by_id(
            delete_workflow_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_workflows(obj):
    json_schema_validate('jsd_aeb4dad04a99bbe3_v1_3_3').validate(obj)
    return True


def get_workflows(api):
    endpoint_result = api.device_onboarding_pnp.get_workflows(
        limit=0,
        name='value1,value2',
        offset=0,
        sort='value1,value2',
        sort_order='string',
        type='value1,value2'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_workflows(api):
    assert is_valid_get_workflows(
        get_workflows(api)
    )


def get_workflows_default(api):
    endpoint_result = api.device_onboarding_pnp.get_workflows(
        limit=None,
        name=None,
        offset=None,
        sort=None,
        sort_order=None,
        type=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_workflows_default(api):
    try:
        assert is_valid_get_workflows(
            get_workflows_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_preview_config(obj):
    return True if obj else False


def preview_config(api):
    endpoint_result = api.device_onboarding_pnp.preview_config(
        active_validation=True,
        deviceId='string',
        payload=None,
        siteId='string',
        type='Default'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_preview_config(api):
    assert is_valid_preview_config(
        preview_config(api)
    )


def preview_config_default(api):
    endpoint_result = api.device_onboarding_pnp.preview_config(
        active_validation=True,
        deviceId=None,
        payload=None,
        siteId=None,
        type=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_preview_config_default(api):
    try:
        assert is_valid_preview_config(
            preview_config_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_device_by_id(obj):
    json_schema_validate('jsd_bab6c9e5440885cc_v1_3_3').validate(obj)
    return True


def get_device_by_id(api):
    endpoint_result = api.device_onboarding_pnp.get_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_device_by_id(api):
    assert is_valid_get_device_by_id(
        get_device_by_id(api)
    )


def get_device_by_id_default(api):
    endpoint_result = api.device_onboarding_pnp.get_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_device_by_id_default(api):
    try:
        assert is_valid_get_device_by_id(
            get_device_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_claim_device(obj):
    json_schema_validate('jsd_d8a619974a8a8c48_v1_3_3').validate(obj)
    return True


def claim_device(api):
    endpoint_result = api.device_onboarding_pnp.claim_device(
        active_validation=True,
        configFileUrl='string',
        configId='string',
        deviceClaimList=[{'configList': [{'configId': 'string', 'configParameters': [{'key': 'string', 'value': 'string'}]}], 'deviceId': 'string', 'licenseLevel': 'string', 'licenseType': 'string', 'topOfStackSerialNumber': 'string'}],
        fileServiceId='string',
        imageId='string',
        imageUrl='string',
        payload=None,
        populateInventory=True,
        projectId='string',
        workflowId='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_claim_device(api):
    assert is_valid_claim_device(
        claim_device(api)
    )


def claim_device_default(api):
    endpoint_result = api.device_onboarding_pnp.claim_device(
        active_validation=True,
        configFileUrl=None,
        configId=None,
        deviceClaimList=None,
        fileServiceId=None,
        imageId=None,
        imageUrl=None,
        payload=None,
        populateInventory=None,
        projectId=None,
        workflowId=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_claim_device_default(api):
    try:
        assert is_valid_claim_device(
            claim_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_device_by_id_from_pnp(obj):
    json_schema_validate('jsd_cdab9b474899ae06_v1_3_3').validate(obj)
    return True


def delete_device_by_id_from_pnp(api):
    endpoint_result = api.device_onboarding_pnp.delete_device_by_id_from_pnp(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_delete_device_by_id_from_pnp(api):
    assert is_valid_delete_device_by_id_from_pnp(
        delete_device_by_id_from_pnp(api)
    )


def delete_device_by_id_from_pnp_default(api):
    endpoint_result = api.device_onboarding_pnp.delete_device_by_id_from_pnp(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_delete_device_by_id_from_pnp_default(api):
    try:
        assert is_valid_delete_device_by_id_from_pnp(
            delete_device_by_id_from_pnp_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_device_list(obj):
    json_schema_validate('jsd_e6b3db8046c99654_v1_3_3').validate(obj)
    return True


def get_device_list(api):
    endpoint_result = api.device_onboarding_pnp.get_device_list(
        cm_state='value1,value2',
        last_contact=True,
        limit=0,
        name='value1,value2',
        offset=0,
        onb_state='value1,value2',
        pid='value1,value2',
        project_id='value1,value2',
        project_name='value1,value2',
        serial_number='value1,value2',
        smart_account_id='value1,value2',
        sort='value1,value2',
        sort_order='string',
        source='value1,value2',
        state='value1,value2',
        virtual_account_id='value1,value2',
        workflow_id='value1,value2',
        workflow_name='value1,value2'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_device_list(api):
    assert is_valid_get_device_list(
        get_device_list(api)
    )


def get_device_list_default(api):
    endpoint_result = api.device_onboarding_pnp.get_device_list(
        cm_state=None,
        last_contact=None,
        limit=None,
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
        workflow_name=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_device_list_default(api):
    try:
        assert is_valid_get_device_list(
            get_device_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_add_device(obj):
    json_schema_validate('jsd_f3b26b5544cabab9_v1_3_3').validate(obj)
    return True


def add_device(api):
    endpoint_result = api.device_onboarding_pnp.add_device(
        _id='string',
        active_validation=True,
        deviceInfo={'aaaCredentials': {'password': 'string', 'username': 'string'}, 'addedOn': 0, 'addnMacAddrs': ['string'], 'agentType': 'POSIX', 'authStatus': 'string', 'authenticatedSudiSerialNo': 'string', 'capabilitiesSupported': ['string'], 'cmState': 'NotContacted', 'description': 'string', 'deviceSudiSerialNos': ['string'], 'deviceType': 'string', 'featuresSupported': ['string'], 'fileSystemList': [{'freespace': 0, 'name': 'string', 'readable': True, 'size': 0, 'type': 'string', 'writeable': True}], 'firstContact': 0, 'hostname': 'string', 'httpHeaders': [{'key': 'string', 'value': 'string'}], 'imageFile': 'string', 'imageVersion': 'string', 'ipInterfaces': [{'ipv4Address': {}, 'ipv6AddressList': [{}], 'macAddress': 'string', 'name': 'string', 'status': 'string'}], 'lastContact': 0, 'lastSyncTime': 0, 'lastUpdateOn': 0, 'location': {'address': 'string', 'altitude': 'string', 'latitude': 'string', 'longitude': 'string', 'siteId': 'string'}, 'macAddress': 'string', 'mode': 'string', 'name': 'string', 'neighborLinks': [{'localInterfaceName': 'string', 'localMacAddress': 'string', 'localShortInterfaceName': 'string', 'remoteDeviceName': 'string', 'remoteInterfaceName': 'string', 'remoteMacAddress': 'string', 'remotePlatform': 'string', 'remoteShortInterfaceName': 'string', 'remoteVersion': 'string'}], 'onbState': 'NotContacted', 'pid': 'string', 'pnpProfileList': [{'createdBy': 'string', 'discoveryCreated': True, 'primaryEndpoint': {'certificate': 'string', 'fqdn': 'string', 'ipv4Address': {}, 'ipv6Address': {}, 'port': 0, 'protocol': 'string'}, 'profileName': 'string', 'secondaryEndpoint': {'certificate': 'string', 'fqdn': 'string', 'ipv4Address': {}, 'ipv6Address': {}, 'port': 0, 'protocol': 'string'}}], 'populateInventory': True, 'preWorkflowCliOuputs': [{'cli': 'string', 'cliOutput': 'string'}], 'projectId': 'string', 'projectName': 'string', 'reloadRequested': True, 'serialNumber': 'string', 'smartAccountId': 'string', 'source': 'string', 'stack': True, 'stackInfo': {'isFullRing': True, 'stackMemberList': [{'hardwareVersion': 'string', 'licenseLevel': 'string', 'licenseType': 'string', 'macAddress': 'string', 'pid': 'string', 'priority': 0, 'role': 'string', 'serialNumber': 'string', 'softwareVersion': 'string', 'stackNumber': 0, 'state': 'string', 'sudiSerialNumber': 'string'}], 'stackRingProtocol': 'string', 'supportsStackWorkflows': True, 'totalMemberCount': 0, 'validLicenseLevels': ['string']}, 'state': 'Unclaimed', 'sudiRequired': True, 'tags': {}, 'userSudiSerialNos': ['string'], 'virtualAccountId': 'string', 'workflowId': 'string', 'workflowName': 'string'},
        payload=None,
        runSummaryList=[{'details': 'string', 'errorFlag': True, 'historyTaskInfo': {'addnDetails': [{'key': 'string', 'value': 'string'}], 'name': 'string', 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}, 'timestamp': 0}],
        systemResetWorkflow={'_id': 'string', 'addToInventory': True, 'addedOn': 0, 'configId': 'string', 'currTaskIdx': 0, 'description': 'string', 'endTime': 0, 'execTime': 0, 'imageId': 'string', 'instanceType': 'SystemWorkflow', 'lastupdateOn': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'tasks': [{'currWorkItemIdx': 0, 'endTime': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'taskSeqNo': 0, 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}], 'tenantId': 'string', 'type': 'string', 'useState': 'string', 'version': 0},
        systemWorkflow={'_id': 'string', 'addToInventory': True, 'addedOn': 0, 'configId': 'string', 'currTaskIdx': 0, 'description': 'string', 'endTime': 0, 'execTime': 0, 'imageId': 'string', 'instanceType': 'SystemWorkflow', 'lastupdateOn': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'tasks': [{'currWorkItemIdx': 0, 'endTime': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'taskSeqNo': 0, 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}], 'tenantId': 'string', 'type': 'string', 'useState': 'string', 'version': 0},
        tenantId='string',
        version=0,
        workflow={'_id': 'string', 'addToInventory': True, 'addedOn': 0, 'configId': 'string', 'currTaskIdx': 0, 'description': 'string', 'endTime': 0, 'execTime': 0, 'imageId': 'string', 'instanceType': 'SystemWorkflow', 'lastupdateOn': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'tasks': [{'currWorkItemIdx': 0, 'endTime': 0, 'name': 'string', 'startTime': 0, 'state': 'string', 'taskSeqNo': 0, 'timeTaken': 0, 'type': 'string', 'workItemList': [{'command': 'string', 'endTime': 0, 'outputStr': 'string', 'startTime': 0, 'state': 'string', 'timeTaken': 0}]}], 'tenantId': 'string', 'type': 'string', 'useState': 'string', 'version': 0},
        workflowParameters={'configList': [{'configId': 'string', 'configParameters': [{'key': 'string', 'value': 'string'}]}], 'licenseLevel': 'string', 'licenseType': 'string', 'topOfStackSerialNumber': 'string'}
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_add_device(api):
    assert is_valid_add_device(
        add_device(api)
    )


def add_device_default(api):
    endpoint_result = api.device_onboarding_pnp.add_device(
        _id=None,
        active_validation=True,
        deviceInfo=None,
        payload=None,
        runSummaryList=None,
        systemResetWorkflow=None,
        systemWorkflow=None,
        tenantId=None,
        version=None,
        workflow=None,
        workflowParameters=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_add_device_default(api):
    try:
        assert is_valid_add_device(
            add_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_device_count(obj):
    json_schema_validate('jsd_d9a1fa9c4068b23c_v1_3_3').validate(obj)
    return True


def get_device_count(api):
    endpoint_result = api.device_onboarding_pnp.get_device_count(
        cm_state='value1,value2',
        last_contact=True,
        name='value1,value2',
        onb_state='value1,value2',
        pid='value1,value2',
        project_id='value1,value2',
        project_name='value1,value2',
        serial_number='value1,value2',
        smart_account_id='value1,value2',
        source='value1,value2',
        state='value1,value2',
        virtual_account_id='value1,value2',
        workflow_id='value1,value2',
        workflow_name='value1,value2'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_device_count(api):
    assert is_valid_get_device_count(
        get_device_count(api)
    )


def get_device_count_default(api):
    endpoint_result = api.device_onboarding_pnp.get_device_count(
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
        workflow_name=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_device_count_default(api):
    try:
        assert is_valid_get_device_count(
            get_device_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_device_history(obj):
    json_schema_validate('jsd_f09319674049a7d4_v1_3_3').validate(obj)
    return True


def get_device_history(api):
    endpoint_result = api.device_onboarding_pnp.get_device_history(
        serial_number='string',
        sort='value1,value2',
        sort_order='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_device_history(api):
    assert is_valid_get_device_history(
        get_device_history(api)
    )


def get_device_history_default(api):
    endpoint_result = api.device_onboarding_pnp.get_device_history(
        serial_number=None,
        sort=None,
        sort_order=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_device_history_default(api):
    try:
        assert is_valid_get_device_history(
            get_device_history_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

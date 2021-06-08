# -*- coding: utf-8 -*-
"""DNACenterAPI device_onboarding_pnp API fixtures and tests.

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


def is_valid_get_sync_result_for_virtual_account(json_schema_validate, obj):
    json_schema_validate('jsd_b34f9daa98735533a61287ce30d216b6_v2_2_1').validate(obj)
    return True


def get_sync_result_for_virtual_account(api):
    endpoint_result = api.device_onboarding_pnp.get_sync_result_for_virtual_account(
        domain='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_sync_result_for_virtual_account(api, validator):
    try:
        assert is_valid_get_sync_result_for_virtual_account(
            validator,
            get_sync_result_for_virtual_account(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sync_result_for_virtual_account_default(api):
    endpoint_result = api.device_onboarding_pnp.get_sync_result_for_virtual_account(
        domain='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_sync_result_for_virtual_account_default(api, validator):
    try:
        assert is_valid_get_sync_result_for_virtual_account(
            validator,
            get_sync_result_for_virtual_account_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_6d2ead8063ab552ea4abcb3e947a092a_v2_2_1').validate(obj)
    return True


def get_device_by_id(api):
    endpoint_result = api.device_onboarding_pnp.get_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_device_by_id(api, validator):
    try:
        assert is_valid_get_device_by_id(
            validator,
            get_device_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_by_id_default(api):
    endpoint_result = api.device_onboarding_pnp.get_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_device_by_id_default(api, validator):
    try:
        assert is_valid_get_device_by_id(
            validator,
            get_device_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device(json_schema_validate, obj):
    json_schema_validate('jsd_cec8139f6b1c5e5991d12197206029a0_v2_2_1').validate(obj)
    return True


def update_device(api):
    endpoint_result = api.device_onboarding_pnp.update_device(
        _id='string',
        active_validation=True,
        dayZeroConfig={'config': 'string'},
        dayZeroConfigPreview={},
        deviceInfo={'source': 'string', 'serialNumber': 'string', 'stack': True, 'mode': 'string', 'state': 'string', 'location': {'siteId': 'string', 'address': 'string', 'latitude': 'string', 'longitude': 'string', 'altitude': 'string'}, 'description': 'string', 'onbState': 'string', 'authenticatedMicNumber': 'string', 'authenticatedSudiSerialNo': 'string', 'capabilitiesSupported': ['string'], 'featuresSupported': ['string'], 'cmState': 'string', 'firstContact': 0, 'lastContact': 0, 'macAddress': 'string', 'pid': 'string', 'deviceSudiSerialNos': ['string'], 'lastUpdateOn': 0, 'workflowId': 'string', 'workflowName': 'string', 'projectId': 'string', 'projectName': 'string', 'deviceType': 'string', 'agentType': 'string', 'imageVersion': 'string', 'fileSystemList': [{'type': 'string', 'writeable': True, 'freespace': 0, 'name': 'string', 'readable': True, 'size': 0}], 'pnpProfileList': [{'profileName': 'string', 'discoveryCreated': True, 'createdBy': 'string', 'primaryEndpoint': {'port': 0, 'protocol': 'string', 'ipv4Address': {}, 'ipv6Address': {}, 'fqdn': 'string', 'certificate': 'string'}, 'secondaryEndpoint': {'port': 0, 'protocol': 'string', 'ipv4Address': {}, 'ipv6Address': {}, 'fqdn': 'string', 'certificate': 'string'}}], 'imageFile': 'string', 'httpHeaders': [{'key': 'string', 'value': 'string'}], 'neighborLinks': [{'localInterfaceName': 'string', 'localShortInterfaceName': 'string', 'localMacAddress': 'string', 'remoteInterfaceName': 'string', 'remoteShortInterfaceName': 'string', 'remoteMacAddress': 'string', 'remoteDeviceName': 'string', 'remotePlatform': 'string', 'remoteVersion': 'string'}], 'lastSyncTime': 0, 'ipInterfaces': [{'status': 'string', 'macAddress': 'string', 'ipv4Address': {}, 'ipv6AddressList': [{}], 'name': 'string'}], 'hostname': 'string', 'authStatus': 'string', 'stackInfo': {'supportsStackWorkflows': True, 'isFullRing': True, 'stackMemberList': [{'serialNumber': 'string', 'state': 'string', 'role': 'string', 'macAddress': 'string', 'pid': 'string', 'licenseLevel': 'string', 'licenseType': 'string', 'sudiSerialNumber': 'string', 'hardwareVersion': 'string', 'stackNumber': 0, 'softwareVersion': 'string', 'priority': 0}], 'stackRingProtocol': 'string', 'validLicenseLevels': ['string'], 'totalMemberCount': 0}, 'reloadRequested': True, 'addedOn': 0, 'siteId': 'string', 'aaaCredentials': {'password': 'string', 'username': 'string'}, 'userMicNumbers': ['string'], 'userSudiSerialNos': ['string'], 'addnMacAddrs': ['string'], 'preWorkflowCliOuputs': [{'cli': 'string', 'cliOutput': 'string'}], 'tags': {}, 'sudiRequired': True, 'smartAccountId': 'string', 'virtualAccountId': 'string', 'populateInventory': True, 'siteName': 'string', 'name': 'string'},
        id='string',
        payload=None,
        runSummaryList=[{'details': 'string', 'historyTaskInfo': {'type': 'string', 'workItemList': [{'state': 'string', 'command': 'string', 'outputStr': 'string', 'endTime': 0, 'startTime': 0, 'timeTaken': 0}], 'timeTaken': 0, 'addnDetails': [{'key': 'string', 'value': 'string'}], 'name': 'string'}, 'errorFlag': True, 'timestamp': 0}],
        systemResetWorkflow={'_id': 'string', 'state': 'string', 'type': 'string', 'description': 'string', 'lastupdateOn': 0, 'imageId': 'string', 'currTaskIdx': 0, 'addedOn': 0, 'tasks': [{'state': 'string', 'type': 'string', 'currWorkItemIdx': 0, 'taskSeqNo': 0, 'endTime': 0, 'startTime': 0, 'workItemList': [{'state': 'string', 'command': 'string', 'outputStr': 'string', 'endTime': 0, 'startTime': 0, 'timeTaken': 0}], 'timeTaken': 0, 'name': 'string'}], 'addToInventory': True, 'instanceType': 'string', 'endTime': 0, 'execTime': 0, 'startTime': 0, 'useState': 'string', 'configId': 'string', 'name': 'string', 'version': 0, 'tenantId': 'string'},
        systemWorkflow={'_id': 'string', 'state': 'string', 'type': 'string', 'description': 'string', 'lastupdateOn': 0, 'imageId': 'string', 'currTaskIdx': 0, 'addedOn': 0, 'tasks': [{'state': 'string', 'type': 'string', 'currWorkItemIdx': 0, 'taskSeqNo': 0, 'endTime': 0, 'startTime': 0, 'workItemList': [{'state': 'string', 'command': 'string', 'outputStr': 'string', 'endTime': 0, 'startTime': 0, 'timeTaken': 0}], 'timeTaken': 0, 'name': 'string'}], 'addToInventory': True, 'instanceType': 'string', 'endTime': 0, 'execTime': 0, 'startTime': 0, 'useState': 'string', 'configId': 'string', 'name': 'string', 'version': 0, 'tenantId': 'string'},
        tenantId='string',
        version=0,
        workflow={'_id': 'string', 'state': 'string', 'type': 'string', 'description': 'string', 'lastupdateOn': 0, 'imageId': 'string', 'currTaskIdx': 0, 'addedOn': 0, 'tasks': [{'state': 'string', 'type': 'string', 'currWorkItemIdx': 0, 'taskSeqNo': 0, 'endTime': 0, 'startTime': 0, 'workItemList': [{'state': 'string', 'command': 'string', 'outputStr': 'string', 'endTime': 0, 'startTime': 0, 'timeTaken': 0}], 'timeTaken': 0, 'name': 'string'}], 'addToInventory': True, 'instanceType': 'string', 'endTime': 0, 'execTime': 0, 'startTime': 0, 'useState': 'string', 'configId': 'string', 'name': 'string', 'version': 0, 'tenantId': 'string'},
        workflowParameters={'topOfStackSerialNumber': 'string', 'licenseLevel': 'string', 'licenseType': 'string', 'configList': [{'configParameters': [{'key': 'string', 'value': 'string'}], 'configId': 'string'}]}
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_update_device(api, validator):
    try:
        assert is_valid_update_device(
            validator,
            update_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_default(api):
    endpoint_result = api.device_onboarding_pnp.update_device(
        _id=None,
        active_validation=True,
        dayZeroConfig=None,
        dayZeroConfigPreview=None,
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
def test_update_device_default(api, validator):
    try:
        assert is_valid_update_device(
            validator,
            update_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_by_id_from_pnp(json_schema_validate, obj):
    json_schema_validate('jsd_5cfec9657be95cac9679e5a808e95124_v2_2_1').validate(obj)
    return True


def delete_device_by_id_from_pnp(api):
    endpoint_result = api.device_onboarding_pnp.delete_device_by_id_from_pnp(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_delete_device_by_id_from_pnp(api, validator):
    try:
        assert is_valid_delete_device_by_id_from_pnp(
            validator,
            delete_device_by_id_from_pnp(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_by_id_from_pnp_default(api):
    endpoint_result = api.device_onboarding_pnp.delete_device_by_id_from_pnp(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_delete_device_by_id_from_pnp_default(api, validator):
    try:
        assert is_valid_delete_device_by_id_from_pnp(
            validator,
            delete_device_by_id_from_pnp_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_un_claim_device(json_schema_validate, obj):
    json_schema_validate('jsd_0768898397e350a7a690cdfeffa5eaca_v2_2_1').validate(obj)
    return True


def un_claim_device(api):
    endpoint_result = api.device_onboarding_pnp.un_claim_device(
        active_validation=True,
        deviceIdList=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_un_claim_device(api, validator):
    try:
        assert is_valid_un_claim_device(
            validator,
            un_claim_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def un_claim_device_default(api):
    endpoint_result = api.device_onboarding_pnp.un_claim_device(
        active_validation=True,
        deviceIdList=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_un_claim_device_default(api, validator):
    try:
        assert is_valid_un_claim_device(
            validator,
            un_claim_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_pnp_server_profile(json_schema_validate, obj):
    json_schema_validate('jsd_bc3cb471beaf5bfeb47201993c023068_v2_2_1').validate(obj)
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
        syncResult={'syncList': [{'deviceSnList': ['string'], 'syncType': 'string'}], 'syncMsg': 'string'},
        syncResultStr='string',
        syncStartTime=0,
        syncStatus='string',
        tenantId='string',
        token='string',
        virtualAccountId='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_update_pnp_server_profile(api, validator):
    try:
        assert is_valid_update_pnp_server_profile(
            validator,
            update_pnp_server_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


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
def test_update_pnp_server_profile_default(api, validator):
    try:
        assert is_valid_update_pnp_server_profile(
            validator,
            update_pnp_server_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_virtual_account(json_schema_validate, obj):
    json_schema_validate('jsd_c6774ff9549a53d4b41fdd2d88f1d0f5_v2_2_1').validate(obj)
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
        syncResult={'syncList': [{'deviceSnList': ['string'], 'syncType': 'string'}], 'syncMsg': 'string'},
        syncResultStr='string',
        syncStartTime=0,
        syncStatus='string',
        tenantId='string',
        token='string',
        virtualAccountId='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_add_virtual_account(api, validator):
    try:
        assert is_valid_add_virtual_account(
            validator,
            add_virtual_account(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


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
def test_add_virtual_account_default(api, validator):
    try:
        assert is_valid_add_virtual_account(
            validator,
            add_virtual_account_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_devices_in_bulk(json_schema_validate, obj):
    json_schema_validate('jsd_a7d6d604f38f5f849af79d8768bddfc1_v2_2_1').validate(obj)
    return True


def import_devices_in_bulk(api):
    endpoint_result = api.device_onboarding_pnp.import_devices_in_bulk(
        _id='string',
        active_validation=True,
        dayZeroConfig={'config': 'string'},
        dayZeroConfigPreview={},
        deviceInfo={'source': 'string', 'serialNumber': 'string', 'stack': True, 'mode': 'string', 'state': 'string', 'location': {'siteId': 'string', 'address': 'string', 'latitude': 'string', 'longitude': 'string', 'altitude': 'string'}, 'description': 'string', 'onbState': 'string', 'authenticatedMicNumber': 'string', 'authenticatedSudiSerialNo': 'string', 'capabilitiesSupported': ['string'], 'featuresSupported': ['string'], 'cmState': 'string', 'firstContact': 0, 'lastContact': 0, 'macAddress': 'string', 'pid': 'string', 'deviceSudiSerialNos': ['string'], 'lastUpdateOn': 0, 'workflowId': 'string', 'workflowName': 'string', 'projectId': 'string', 'projectName': 'string', 'deviceType': 'string', 'agentType': 'string', 'imageVersion': 'string', 'fileSystemList': [{'type': 'string', 'writeable': True, 'freespace': 0, 'name': 'string', 'readable': True, 'size': 0}], 'pnpProfileList': [{'profileName': 'string', 'discoveryCreated': True, 'createdBy': 'string', 'primaryEndpoint': {'port': 0, 'protocol': 'string', 'ipv4Address': {}, 'ipv6Address': {}, 'fqdn': 'string', 'certificate': 'string'}, 'secondaryEndpoint': {'port': 0, 'protocol': 'string', 'ipv4Address': {}, 'ipv6Address': {}, 'fqdn': 'string', 'certificate': 'string'}}], 'imageFile': 'string', 'httpHeaders': [{'key': 'string', 'value': 'string'}], 'neighborLinks': [{'localInterfaceName': 'string', 'localShortInterfaceName': 'string', 'localMacAddress': 'string', 'remoteInterfaceName': 'string', 'remoteShortInterfaceName': 'string', 'remoteMacAddress': 'string', 'remoteDeviceName': 'string', 'remotePlatform': 'string', 'remoteVersion': 'string'}], 'lastSyncTime': 0, 'ipInterfaces': [{'status': 'string', 'macAddress': 'string', 'ipv4Address': {}, 'ipv6AddressList': [{}], 'name': 'string'}], 'hostname': 'string', 'authStatus': 'string', 'stackInfo': {'supportsStackWorkflows': True, 'isFullRing': True, 'stackMemberList': [{'serialNumber': 'string', 'state': 'string', 'role': 'string', 'macAddress': 'string', 'pid': 'string', 'licenseLevel': 'string', 'licenseType': 'string', 'sudiSerialNumber': 'string', 'hardwareVersion': 'string', 'stackNumber': 0, 'softwareVersion': 'string', 'priority': 0}], 'stackRingProtocol': 'string', 'validLicenseLevels': ['string'], 'totalMemberCount': 0}, 'reloadRequested': True, 'addedOn': 0, 'siteId': 'string', 'aaaCredentials': {'password': 'string', 'username': 'string'}, 'userMicNumbers': ['string'], 'userSudiSerialNos': ['string'], 'addnMacAddrs': ['string'], 'preWorkflowCliOuputs': [{'cli': 'string', 'cliOutput': 'string'}], 'tags': {}, 'sudiRequired': True, 'smartAccountId': 'string', 'virtualAccountId': 'string', 'populateInventory': True, 'siteName': 'string', 'name': 'string'},
        payload=None,
        runSummaryList=[{'details': 'string', 'historyTaskInfo': {'type': 'string', 'workItemList': [{'state': 'string', 'command': 'string', 'outputStr': 'string', 'endTime': 0, 'startTime': 0, 'timeTaken': 0}], 'timeTaken': 0, 'addnDetails': [{'key': 'string', 'value': 'string'}], 'name': 'string'}, 'errorFlag': True, 'timestamp': 0}],
        systemResetWorkflow={'_id': 'string', 'state': 'string', 'type': 'string', 'description': 'string', 'lastupdateOn': 0, 'imageId': 'string', 'currTaskIdx': 0, 'addedOn': 0, 'tasks': [{'state': 'string', 'type': 'string', 'currWorkItemIdx': 0, 'taskSeqNo': 0, 'endTime': 0, 'startTime': 0, 'workItemList': [{'state': 'string', 'command': 'string', 'outputStr': 'string', 'endTime': 0, 'startTime': 0, 'timeTaken': 0}], 'timeTaken': 0, 'name': 'string'}], 'addToInventory': True, 'instanceType': 'string', 'endTime': 0, 'execTime': 0, 'startTime': 0, 'useState': 'string', 'configId': 'string', 'name': 'string', 'version': 0, 'tenantId': 'string'},
        systemWorkflow={'_id': 'string', 'state': 'string', 'type': 'string', 'description': 'string', 'lastupdateOn': 0, 'imageId': 'string', 'currTaskIdx': 0, 'addedOn': 0, 'tasks': [{'state': 'string', 'type': 'string', 'currWorkItemIdx': 0, 'taskSeqNo': 0, 'endTime': 0, 'startTime': 0, 'workItemList': [{'state': 'string', 'command': 'string', 'outputStr': 'string', 'endTime': 0, 'startTime': 0, 'timeTaken': 0}], 'timeTaken': 0, 'name': 'string'}], 'addToInventory': True, 'instanceType': 'string', 'endTime': 0, 'execTime': 0, 'startTime': 0, 'useState': 'string', 'configId': 'string', 'name': 'string', 'version': 0, 'tenantId': 'string'},
        tenantId='string',
        version=0,
        workflow={'_id': 'string', 'state': 'string', 'type': 'string', 'description': 'string', 'lastupdateOn': 0, 'imageId': 'string', 'currTaskIdx': 0, 'addedOn': 0, 'tasks': [{'state': 'string', 'type': 'string', 'currWorkItemIdx': 0, 'taskSeqNo': 0, 'endTime': 0, 'startTime': 0, 'workItemList': [{'state': 'string', 'command': 'string', 'outputStr': 'string', 'endTime': 0, 'startTime': 0, 'timeTaken': 0}], 'timeTaken': 0, 'name': 'string'}], 'addToInventory': True, 'instanceType': 'string', 'endTime': 0, 'execTime': 0, 'startTime': 0, 'useState': 'string', 'configId': 'string', 'name': 'string', 'version': 0, 'tenantId': 'string'},
        workflowParameters={'topOfStackSerialNumber': 'string', 'licenseLevel': 'string', 'licenseType': 'string', 'configList': [{'configParameters': [{'key': 'string', 'value': 'string'}], 'configId': 'string'}]}
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_import_devices_in_bulk(api, validator):
    try:
        assert is_valid_import_devices_in_bulk(
            validator,
            import_devices_in_bulk(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_devices_in_bulk_default(api):
    endpoint_result = api.device_onboarding_pnp.import_devices_in_bulk(
        _id=None,
        active_validation=True,
        dayZeroConfig=None,
        dayZeroConfigPreview=None,
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
def test_import_devices_in_bulk_default(api, validator):
    try:
        assert is_valid_import_devices_in_bulk(
            validator,
            import_devices_in_bulk_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deregister_virtual_account(json_schema_validate, obj):
    json_schema_validate('jsd_8f785e5c9b1c5690b29a65d96f6a601a_v2_2_1').validate(obj)
    return True


def deregister_virtual_account(api):
    endpoint_result = api.device_onboarding_pnp.deregister_virtual_account(
        domain='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_deregister_virtual_account(api, validator):
    try:
        assert is_valid_deregister_virtual_account(
            validator,
            deregister_virtual_account(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deregister_virtual_account_default(api):
    endpoint_result = api.device_onboarding_pnp.deregister_virtual_account(
        domain=None,
        name=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_deregister_virtual_account_default(api, validator):
    try:
        assert is_valid_deregister_virtual_account(
            validator,
            deregister_virtual_account_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_workflow_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_56a2b8f2239f5ef5b2e749f1b85d6508_v2_2_1').validate(obj)
    return True


def get_workflow_by_id(api):
    endpoint_result = api.device_onboarding_pnp.get_workflow_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_workflow_by_id(api, validator):
    try:
        assert is_valid_get_workflow_by_id(
            validator,
            get_workflow_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_workflow_by_id_default(api):
    endpoint_result = api.device_onboarding_pnp.get_workflow_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_workflow_by_id_default(api, validator):
    try:
        assert is_valid_get_workflow_by_id(
            validator,
            get_workflow_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_workflow(json_schema_validate, obj):
    json_schema_validate('jsd_4550fdd2af215b9b8327a3e24a3dea89_v2_2_1').validate(obj)
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
        instanceType='string',
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
def test_update_workflow(api, validator):
    try:
        assert is_valid_update_workflow(
            validator,
            update_workflow(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


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
def test_update_workflow_default(api, validator):
    try:
        assert is_valid_update_workflow(
            validator,
            update_workflow_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_workflow_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_820ccaae97d6564e9a29fa5170ccd2a3_v2_2_1').validate(obj)
    return True


def delete_workflow_by_id(api):
    endpoint_result = api.device_onboarding_pnp.delete_workflow_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_delete_workflow_by_id(api, validator):
    try:
        assert is_valid_delete_workflow_by_id(
            validator,
            delete_workflow_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_workflow_by_id_default(api):
    endpoint_result = api.device_onboarding_pnp.delete_workflow_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_delete_workflow_by_id_default(api, validator):
    try:
        assert is_valid_delete_workflow_by_id(
            validator,
            delete_workflow_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_smart_account_list(json_schema_validate, obj):
    json_schema_validate('jsd_6e433c01ec815f18af40dcf05481ef52_v2_2_1').validate(obj)
    return True


def get_smart_account_list(api):
    endpoint_result = api.device_onboarding_pnp.get_smart_account_list(

    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_smart_account_list(api, validator):
    try:
        assert is_valid_get_smart_account_list(
            validator,
            get_smart_account_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_smart_account_list_default(api):
    endpoint_result = api.device_onboarding_pnp.get_smart_account_list(

    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_smart_account_list_default(api, validator):
    try:
        assert is_valid_get_smart_account_list(
            validator,
            get_smart_account_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_claim_a_device_to_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_e11daa984f535a08bc1eb01bc84bc399_v2_2_1').validate(obj)
    return True


def claim_a_device_to_a_site(api):
    endpoint_result = api.device_onboarding_pnp.claim_a_device_to_a_site(
        active_validation=True,
        deviceId='string',
        payload=None,
        siteId='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_claim_a_device_to_a_site(api, validator):
    try:
        assert is_valid_claim_a_device_to_a_site(
            validator,
            claim_a_device_to_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


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
def test_claim_a_device_to_a_site_default(api, validator):
    try:
        assert is_valid_claim_a_device_to_a_site(
            validator,
            claim_a_device_to_a_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_virtual_account_list(json_schema_validate, obj):
    json_schema_validate('jsd_c1a9d2c14ac255fd812d6e7aa20a57cc_v2_2_1').validate(obj)
    return True


def get_virtual_account_list(api):
    endpoint_result = api.device_onboarding_pnp.get_virtual_account_list(
        domain='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_virtual_account_list(api, validator):
    try:
        assert is_valid_get_virtual_account_list(
            validator,
            get_virtual_account_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_virtual_account_list_default(api):
    endpoint_result = api.device_onboarding_pnp.get_virtual_account_list(
        domain='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_virtual_account_list_default(api, validator):
    try:
        assert is_valid_get_virtual_account_list(
            validator,
            get_virtual_account_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_workflow_count(json_schema_validate, obj):
    json_schema_validate('jsd_da8a788940fe59519facc6327e988922_v2_2_1').validate(obj)
    return True


def get_workflow_count(api):
    endpoint_result = api.device_onboarding_pnp.get_workflow_count(
        name='value1,value2'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_workflow_count(api, validator):
    try:
        assert is_valid_get_workflow_count(
            validator,
            get_workflow_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_workflow_count_default(api):
    endpoint_result = api.device_onboarding_pnp.get_workflow_count(
        name=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_workflow_count_default(api, validator):
    try:
        assert is_valid_get_workflow_count(
            validator,
            get_workflow_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_pnp_global_settings(json_schema_validate, obj):
    json_schema_validate('jsd_b37eb826a4ad5283ae85dc4628045b40_v2_2_1').validate(obj)
    return True


def get_pnp_global_settings(api):
    endpoint_result = api.device_onboarding_pnp.get_pnp_global_settings(

    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_pnp_global_settings(api, validator):
    try:
        assert is_valid_get_pnp_global_settings(
            validator,
            get_pnp_global_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_pnp_global_settings_default(api):
    endpoint_result = api.device_onboarding_pnp.get_pnp_global_settings(

    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_pnp_global_settings_default(api, validator):
    try:
        assert is_valid_get_pnp_global_settings(
            validator,
            get_pnp_global_settings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_pnp_global_settings(json_schema_validate, obj):
    json_schema_validate('jsd_fc8410781af357b6be17a2104ce5efb1_v2_2_1').validate(obj)
    return True


def update_pnp_global_settings(api):
    endpoint_result = api.device_onboarding_pnp.update_pnp_global_settings(
        _id='string',
        aaaCredentials={'password': 'string', 'username': 'string'},
        acceptEula=True,
        active_validation=True,
        defaultProfile={'cert': 'string', 'fqdnAddresses': ['string'], 'ipAddresses': ['string'], 'port': 0, 'proxy': True},
        payload=None,
        savaMappingList=[{'autoSyncPeriod': 0, 'ccoUser': 'string', 'expiry': 0, 'lastSync': 0, 'profile': {'addressFqdn': 'string', 'addressIpV4': 'string', 'cert': 'string', 'makeDefault': True, 'name': 'string', 'port': 0, 'profileId': 'string', 'proxy': True}, 'smartAccountId': 'string', 'syncResult': {'syncList': [{'deviceSnList': ['string'], 'syncType': 'string'}], 'syncMsg': 'string'}, 'syncResultStr': 'string', 'syncStartTime': 0, 'syncStatus': 'string', 'tenantId': 'string', 'token': 'string', 'virtualAccountId': 'string'}],
        taskTimeOuts={'configTimeOut': 0, 'generalTimeOut': 0, 'imageDownloadTimeOut': 0},
        tenantId='string',
        version=0
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_update_pnp_global_settings(api, validator):
    try:
        assert is_valid_update_pnp_global_settings(
            validator,
            update_pnp_global_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


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
def test_update_pnp_global_settings_default(api, validator):
    try:
        assert is_valid_update_pnp_global_settings(
            validator,
            update_pnp_global_settings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_workflows(json_schema_validate, obj):
    json_schema_validate('jsd_1df400c60659589599f2a0e3e1171985_v2_2_1').validate(obj)
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
def test_get_workflows(api, validator):
    try:
        assert is_valid_get_workflows(
            validator,
            get_workflows(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


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
def test_get_workflows_default(api, validator):
    try:
        assert is_valid_get_workflows(
            validator,
            get_workflows_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_a_workflow(json_schema_validate, obj):
    json_schema_validate('jsd_d967a378b43457ad8c6a6de7bc1845d1_v2_2_1').validate(obj)
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
        instanceType='string',
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
def test_add_a_workflow(api, validator):
    try:
        assert is_valid_add_a_workflow(
            validator,
            add_a_workflow(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


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
def test_add_a_workflow_default(api, validator):
    try:
        assert is_valid_add_a_workflow(
            validator,
            add_a_workflow_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reset_device(json_schema_validate, obj):
    json_schema_validate('jsd_15226f5a13405ba69f3957b98db8663a_v2_2_1').validate(obj)
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
def test_reset_device(api, validator):
    try:
        assert is_valid_reset_device(
            validator,
            reset_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


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
def test_reset_device_default(api, validator):
    try:
        assert is_valid_reset_device(
            validator,
            reset_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sync_virtual_account_devices(json_schema_validate, obj):
    json_schema_validate('jsd_97591ad0cce45817862bebfc839bf5ae_v2_2_1').validate(obj)
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
        syncResult={'syncList': [{'deviceSnList': ['string'], 'syncType': 'string'}], 'syncMsg': 'string'},
        syncResultStr='string',
        syncStartTime=0,
        syncStatus='string',
        tenantId='string',
        token='string',
        virtualAccountId='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_sync_virtual_account_devices(api, validator):
    try:
        assert is_valid_sync_virtual_account_devices(
            validator,
            sync_virtual_account_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


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
def test_sync_virtual_account_devices_default(api, validator):
    try:
        assert is_valid_sync_virtual_account_devices(
            validator,
            sync_virtual_account_devices_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_preview_config(json_schema_validate, obj):
    json_schema_validate('jsd_fc416739f3c655ed911884aec0130e83_v2_2_1').validate(obj)
    return True


def preview_config(api):
    endpoint_result = api.device_onboarding_pnp.preview_config(
        active_validation=True,
        deviceId='string',
        payload=None,
        siteId='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_preview_config(api, validator):
    try:
        assert is_valid_preview_config(
            validator,
            preview_config(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


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
def test_preview_config_default(api, validator):
    try:
        assert is_valid_preview_config(
            validator,
            preview_config_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_claim_device(json_schema_validate, obj):
    json_schema_validate('jsd_2e722e05046d5262b55c125237e9b67d_v2_2_1').validate(obj)
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
def test_claim_device(api, validator):
    try:
        assert is_valid_claim_device(
            validator,
            claim_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


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
def test_claim_device_default(api, validator):
    try:
        assert is_valid_claim_device(
            validator,
            claim_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_count(json_schema_validate, obj):
    json_schema_validate('jsd_17ce6d91900556839c09184d8a11c04d_v2_2_1').validate(obj)
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
def test_get_device_count(api, validator):
    try:
        assert is_valid_get_device_count(
            validator,
            get_device_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


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
def test_get_device_count_default(api, validator):
    try:
        assert is_valid_get_device_count(
            validator,
            get_device_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_list(json_schema_validate, obj):
    json_schema_validate('jsd_24c033291ec4591886bd6ed25f900c1b_v2_2_1').validate(obj)
    return True


def get_device_list(api):
    endpoint_result = api.device_onboarding_pnp.get_device_list(
        cm_state='value1,value2',
        hostname='string',
        last_contact=True,
        limit=0,
        mac_address='string',
        name='value1,value2',
        offset=0,
        onb_state='value1,value2',
        pid='value1,value2',
        project_id='value1,value2',
        project_name='value1,value2',
        serial_number='value1,value2',
        site_name='string',
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
def test_get_device_list(api, validator):
    try:
        assert is_valid_get_device_list(
            validator,
            get_device_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_list_default(api):
    endpoint_result = api.device_onboarding_pnp.get_device_list(
        cm_state=None,
        hostname=None,
        last_contact=None,
        limit=None,
        mac_address=None,
        name=None,
        offset=None,
        onb_state=None,
        pid=None,
        project_id=None,
        project_name=None,
        serial_number=None,
        site_name=None,
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
def test_get_device_list_default(api, validator):
    try:
        assert is_valid_get_device_list(
            validator,
            get_device_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_device(json_schema_validate, obj):
    json_schema_validate('jsd_734f04b76067507b9384e409e9431ef3_v2_2_1').validate(obj)
    return True


def add_device(api):
    endpoint_result = api.device_onboarding_pnp.add_device(
        _id='string',
        active_validation=True,
        dayZeroConfig={'config': 'string'},
        dayZeroConfigPreview={},
        deviceInfo={'source': 'string', 'serialNumber': 'string', 'stack': True, 'mode': 'string', 'state': 'string', 'location': {'siteId': 'string', 'address': 'string', 'latitude': 'string', 'longitude': 'string', 'altitude': 'string'}, 'description': 'string', 'onbState': 'string', 'authenticatedMicNumber': 'string', 'authenticatedSudiSerialNo': 'string', 'capabilitiesSupported': ['string'], 'featuresSupported': ['string'], 'cmState': 'string', 'firstContact': 0, 'lastContact': 0, 'macAddress': 'string', 'pid': 'string', 'deviceSudiSerialNos': ['string'], 'lastUpdateOn': 0, 'workflowId': 'string', 'workflowName': 'string', 'projectId': 'string', 'projectName': 'string', 'deviceType': 'string', 'agentType': 'string', 'imageVersion': 'string', 'fileSystemList': [{'type': 'string', 'writeable': True, 'freespace': 0, 'name': 'string', 'readable': True, 'size': 0}], 'pnpProfileList': [{'profileName': 'string', 'discoveryCreated': True, 'createdBy': 'string', 'primaryEndpoint': {'port': 0, 'protocol': 'string', 'ipv4Address': {}, 'ipv6Address': {}, 'fqdn': 'string', 'certificate': 'string'}, 'secondaryEndpoint': {'port': 0, 'protocol': 'string', 'ipv4Address': {}, 'ipv6Address': {}, 'fqdn': 'string', 'certificate': 'string'}}], 'imageFile': 'string', 'httpHeaders': [{'key': 'string', 'value': 'string'}], 'neighborLinks': [{'localInterfaceName': 'string', 'localShortInterfaceName': 'string', 'localMacAddress': 'string', 'remoteInterfaceName': 'string', 'remoteShortInterfaceName': 'string', 'remoteMacAddress': 'string', 'remoteDeviceName': 'string', 'remotePlatform': 'string', 'remoteVersion': 'string'}], 'lastSyncTime': 0, 'ipInterfaces': [{'status': 'string', 'macAddress': 'string', 'ipv4Address': {}, 'ipv6AddressList': [{}], 'name': 'string'}], 'hostname': 'string', 'authStatus': 'string', 'stackInfo': {'supportsStackWorkflows': True, 'isFullRing': True, 'stackMemberList': [{'serialNumber': 'string', 'state': 'string', 'role': 'string', 'macAddress': 'string', 'pid': 'string', 'licenseLevel': 'string', 'licenseType': 'string', 'sudiSerialNumber': 'string', 'hardwareVersion': 'string', 'stackNumber': 0, 'softwareVersion': 'string', 'priority': 0}], 'stackRingProtocol': 'string', 'validLicenseLevels': ['string'], 'totalMemberCount': 0}, 'reloadRequested': True, 'addedOn': 0, 'siteId': 'string', 'aaaCredentials': {'password': 'string', 'username': 'string'}, 'userMicNumbers': ['string'], 'userSudiSerialNos': ['string'], 'addnMacAddrs': ['string'], 'preWorkflowCliOuputs': [{'cli': 'string', 'cliOutput': 'string'}], 'tags': {}, 'sudiRequired': True, 'smartAccountId': 'string', 'virtualAccountId': 'string', 'populateInventory': True, 'siteName': 'string', 'name': 'string'},
        payload=None,
        runSummaryList=[{'details': 'string', 'historyTaskInfo': {'type': 'string', 'workItemList': [{'state': 'string', 'command': 'string', 'outputStr': 'string', 'endTime': 0, 'startTime': 0, 'timeTaken': 0}], 'timeTaken': 0, 'addnDetails': [{'key': 'string', 'value': 'string'}], 'name': 'string'}, 'errorFlag': True, 'timestamp': 0}],
        systemResetWorkflow={'_id': 'string', 'state': 'string', 'type': 'string', 'description': 'string', 'lastupdateOn': 0, 'imageId': 'string', 'currTaskIdx': 0, 'addedOn': 0, 'tasks': [{'state': 'string', 'type': 'string', 'currWorkItemIdx': 0, 'taskSeqNo': 0, 'endTime': 0, 'startTime': 0, 'workItemList': [{'state': 'string', 'command': 'string', 'outputStr': 'string', 'endTime': 0, 'startTime': 0, 'timeTaken': 0}], 'timeTaken': 0, 'name': 'string'}], 'addToInventory': True, 'instanceType': 'string', 'endTime': 0, 'execTime': 0, 'startTime': 0, 'useState': 'string', 'configId': 'string', 'name': 'string', 'version': 0, 'tenantId': 'string'},
        systemWorkflow={'_id': 'string', 'state': 'string', 'type': 'string', 'description': 'string', 'lastupdateOn': 0, 'imageId': 'string', 'currTaskIdx': 0, 'addedOn': 0, 'tasks': [{'state': 'string', 'type': 'string', 'currWorkItemIdx': 0, 'taskSeqNo': 0, 'endTime': 0, 'startTime': 0, 'workItemList': [{'state': 'string', 'command': 'string', 'outputStr': 'string', 'endTime': 0, 'startTime': 0, 'timeTaken': 0}], 'timeTaken': 0, 'name': 'string'}], 'addToInventory': True, 'instanceType': 'string', 'endTime': 0, 'execTime': 0, 'startTime': 0, 'useState': 'string', 'configId': 'string', 'name': 'string', 'version': 0, 'tenantId': 'string'},
        tenantId='string',
        version=0,
        workflow={'_id': 'string', 'state': 'string', 'type': 'string', 'description': 'string', 'lastupdateOn': 0, 'imageId': 'string', 'currTaskIdx': 0, 'addedOn': 0, 'tasks': [{'state': 'string', 'type': 'string', 'currWorkItemIdx': 0, 'taskSeqNo': 0, 'endTime': 0, 'startTime': 0, 'workItemList': [{'state': 'string', 'command': 'string', 'outputStr': 'string', 'endTime': 0, 'startTime': 0, 'timeTaken': 0}], 'timeTaken': 0, 'name': 'string'}], 'addToInventory': True, 'instanceType': 'string', 'endTime': 0, 'execTime': 0, 'startTime': 0, 'useState': 'string', 'configId': 'string', 'name': 'string', 'version': 0, 'tenantId': 'string'},
        workflowParameters={'topOfStackSerialNumber': 'string', 'licenseLevel': 'string', 'licenseType': 'string', 'configList': [{'configParameters': [{'key': 'string', 'value': 'string'}], 'configId': 'string'}]}
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_add_device(api, validator):
    try:
        assert is_valid_add_device(
            validator,
            add_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_device_default(api):
    endpoint_result = api.device_onboarding_pnp.add_device(
        _id=None,
        active_validation=True,
        dayZeroConfig=None,
        dayZeroConfigPreview=None,
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
def test_add_device_default(api, validator):
    try:
        assert is_valid_add_device(
            validator,
            add_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_history(json_schema_validate, obj):
    json_schema_validate('jsd_f03966978a7f5cd4b3228dcae71373fe_v2_2_1').validate(obj)
    return True


def get_device_history(api):
    endpoint_result = api.device_onboarding_pnp.get_device_history(
        serial_number='string',
        sort='value1,value2',
        sort_order='string'
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_device_history(api, validator):
    try:
        assert is_valid_get_device_history(
            validator,
            get_device_history(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_history_default(api):
    endpoint_result = api.device_onboarding_pnp.get_device_history(
        serial_number=None,
        sort=None,
        sort_order=None
    )
    return endpoint_result


@pytest.mark.device_onboarding_pnp
def test_get_device_history_default(api, validator):
    try:
        assert is_valid_get_device_history(
            validator,
            get_device_history_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

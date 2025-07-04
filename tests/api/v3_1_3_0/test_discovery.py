# -*- coding: utf-8 -*-
"""CatalystCenterAPI discovery API fixtures and tests.

Copyright (c) 2025 Cisco Systems.

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

pytestmark = pytest.mark.skipif(
    DNA_CENTER_VERSION != "3.1.3.0", reason="version does not match"
)


def is_valid_delete_all_discovery(json_schema_validate, obj):
    json_schema_validate("jsd_a1d007749a7e5b99aabddf1543714a9a_v3_1_3_0").validate(obj)
    return True


def delete_all_discovery(api):
    endpoint_result = api.discovery.delete_all_discovery()
    return endpoint_result


@pytest.mark.discovery
def test_delete_all_discovery(api, validator):
    try:
        assert is_valid_delete_all_discovery(validator, delete_all_discovery(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_all_discovery_default_val(api):
    endpoint_result = api.discovery.delete_all_discovery()
    return endpoint_result


@pytest.mark.discovery
def test_delete_all_discovery_default_val(api, validator):
    try:
        assert is_valid_delete_all_discovery(
            validator, delete_all_discovery_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_discovery_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_f325b2c7e429566ba5ed9ae8253b5bef_v3_1_3_0").validate(obj)
    return True


def updates_discovery_by_id(api):
    endpoint_result = api.discovery.updates_discovery_by_id(
        active_validation=True,
        attributeInfo={},
        cdpLevel=0,
        deviceIds="string",
        discoveryCondition="string",
        discoveryStatus="string",
        discoveryType="string",
        enablePasswordList="string",
        globalCredentialIdList=["string"],
        httpReadCredential={
            "comments": "string",
            "credentialType": "string",
            "description": "string",
            "id": "string",
            "instanceTenantId": "string",
            "instanceUuid": "string",
            "password": "string",
            "port": 0,
            "secure": True,
            "username": "string",
        },
        httpWriteCredential={
            "comments": "string",
            "credentialType": "string",
            "description": "string",
            "id": "string",
            "instanceTenantId": "string",
            "instanceUuid": "string",
            "password": "string",
            "port": 0,
            "secure": True,
            "username": "string",
        },
        id="string",
        ipAddressList="string",
        ipFilterList="string",
        isAutoCdp=True,
        lldpLevel=0,
        name="string",
        netconfPort="string",
        numDevices=0,
        parentDiscoveryId="string",
        passwordList="string",
        payload=None,
        preferredMgmtIPMethod="string",
        protocolOrder="string",
        retryCount=0,
        snmpAuthPassphrase="string",
        snmpAuthProtocol="string",
        snmpMode="string",
        snmpPrivPassphrase="string",
        snmpPrivProtocol="string",
        snmpRoCommunity="string",
        snmpRoCommunityDesc="string",
        snmpRwCommunity="string",
        snmpRwCommunityDesc="string",
        snmpUserName="string",
        timeOut=0,
        updateMgmtIp=True,
        userNameList="string",
    )
    return endpoint_result


@pytest.mark.discovery
def test_updates_discovery_by_id(api, validator):
    try:
        assert is_valid_updates_discovery_by_id(validator, updates_discovery_by_id(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_discovery_by_id_default_val(api):
    endpoint_result = api.discovery.updates_discovery_by_id(
        active_validation=True,
        attributeInfo=None,
        cdpLevel=None,
        deviceIds=None,
        discoveryCondition=None,
        discoveryStatus=None,
        discoveryType=None,
        enablePasswordList=None,
        globalCredentialIdList=None,
        httpReadCredential=None,
        httpWriteCredential=None,
        id=None,
        ipAddressList=None,
        ipFilterList=None,
        isAutoCdp=None,
        lldpLevel=None,
        name=None,
        netconfPort=None,
        numDevices=None,
        parentDiscoveryId=None,
        passwordList=None,
        payload=None,
        preferredMgmtIPMethod=None,
        protocolOrder=None,
        retryCount=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpRoCommunity=None,
        snmpRoCommunityDesc=None,
        snmpRwCommunity=None,
        snmpRwCommunityDesc=None,
        snmpUserName=None,
        timeOut=None,
        updateMgmtIp=None,
        userNameList=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_updates_discovery_by_id_default_val(api, validator):
    try:
        assert is_valid_updates_discovery_by_id(
            validator, updates_discovery_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_start_discovery(json_schema_validate, obj):
    json_schema_validate("jsd_fdbe4ec3e9f252a988404dc94250b80d_v3_1_3_0").validate(obj)
    return True


def start_discovery(api):
    endpoint_result = api.discovery.start_discovery(
        active_validation=True,
        cdpLevel=0,
        discoveryType="string",
        enablePasswordList=["string"],
        globalCredentialIdList=["string"],
        httpReadCredential={
            "password": "string",
            "port": 0,
            "secure": True,
            "username": "string",
        },
        httpWriteCredential={
            "password": "string",
            "port": 0,
            "secure": True,
            "username": "string",
        },
        ipAddressList="string",
        ipFilterList=["string"],
        lldpLevel=0,
        name="string",
        netconfPort="string",
        passwordList=["string"],
        payload=None,
        preferredMgmtIPMethod="string",
        protocolOrder="string",
        retry=0,
        snmpAuthPassphrase="string",
        snmpAuthProtocol="string",
        snmpMode="string",
        snmpPrivPassphrase="string",
        snmpPrivProtocol="string",
        snmpROCommunity="string",
        snmpROCommunityDesc="string",
        snmpRWCommunity="string",
        snmpRWCommunityDesc="string",
        snmpUserName="string",
        snmpVersion="string",
        timeout=0,
        userNameList=["string"],
    )
    return endpoint_result


@pytest.mark.discovery
def test_start_discovery(api, validator):
    try:
        assert is_valid_start_discovery(validator, start_discovery(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def start_discovery_default_val(api):
    endpoint_result = api.discovery.start_discovery(
        active_validation=True,
        cdpLevel=None,
        discoveryType=None,
        enablePasswordList=None,
        globalCredentialIdList=None,
        httpReadCredential=None,
        httpWriteCredential=None,
        ipAddressList=None,
        ipFilterList=None,
        lldpLevel=None,
        name=None,
        netconfPort=None,
        passwordList=None,
        payload=None,
        preferredMgmtIPMethod=None,
        protocolOrder=None,
        retry=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpROCommunityDesc=None,
        snmpRWCommunity=None,
        snmpRWCommunityDesc=None,
        snmpUserName=None,
        snmpVersion=None,
        timeout=None,
        userNameList=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_start_discovery_default_val(api, validator):
    try:
        assert is_valid_start_discovery(validator, start_discovery_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_all_discovery_jobs(json_schema_validate, obj):
    json_schema_validate("jsd_95e37fcf36e3539492dfb9cd21e49620_v3_1_3_0").validate(obj)
    return True


def get_count_of_all_discovery_jobs(api):
    endpoint_result = api.discovery.get_count_of_all_discovery_jobs()
    return endpoint_result


@pytest.mark.discovery
def test_get_count_of_all_discovery_jobs(api, validator):
    try:
        assert is_valid_get_count_of_all_discovery_jobs(
            validator, get_count_of_all_discovery_jobs(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_all_discovery_jobs_default_val(api):
    endpoint_result = api.discovery.get_count_of_all_discovery_jobs()
    return endpoint_result


@pytest.mark.discovery
def test_get_count_of_all_discovery_jobs_default_val(api, validator):
    try:
        assert is_valid_get_count_of_all_discovery_jobs(
            validator, get_count_of_all_discovery_jobs_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_discovery_jobs_by_ip(json_schema_validate, obj):
    json_schema_validate("jsd_bde1ca5763fc552ab78cd3b2ecf119b1_v3_1_3_0").validate(obj)
    return True


def get_discovery_jobs_by_ip(api):
    endpoint_result = api.discovery.get_discovery_jobs_by_ip(
        ip_address="string", limit=0, name="string", offset=0
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovery_jobs_by_ip(api, validator):
    try:
        assert is_valid_get_discovery_jobs_by_ip(
            validator, get_discovery_jobs_by_ip(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_discovery_jobs_by_ip_default_val(api):
    endpoint_result = api.discovery.get_discovery_jobs_by_ip(
        ip_address=None, limit=None, name=None, offset=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovery_jobs_by_ip_default_val(api, validator):
    try:
        assert is_valid_get_discovery_jobs_by_ip(
            validator, get_discovery_jobs_by_ip_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_discovery_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_1bb187b0c0a55e7e8089ac78eb29d8a2_v3_1_3_0").validate(obj)
    return True


def delete_discovery_by_id(api):
    endpoint_result = api.discovery.delete_discovery_by_id(id="string")
    return endpoint_result


@pytest.mark.discovery
def test_delete_discovery_by_id(api, validator):
    try:
        assert is_valid_delete_discovery_by_id(validator, delete_discovery_by_id(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_discovery_by_id_default_val(api):
    endpoint_result = api.discovery.delete_discovery_by_id(id="string")
    return endpoint_result


@pytest.mark.discovery
def test_delete_discovery_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_discovery_by_id(
            validator, delete_discovery_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_discovery_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_c4370f0a57d85355a7061d7671f1b613_v3_1_3_0").validate(obj)
    return True


def get_discovery_by_id(api):
    endpoint_result = api.discovery.get_discovery_by_id(id="string")
    return endpoint_result


@pytest.mark.discovery
def test_get_discovery_by_id(api, validator):
    try:
        assert is_valid_get_discovery_by_id(validator, get_discovery_by_id(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_discovery_by_id_default_val(api):
    endpoint_result = api.discovery.get_discovery_by_id(id="string")
    return endpoint_result


@pytest.mark.discovery
def test_get_discovery_by_id_default_val(api, validator):
    try:
        assert is_valid_get_discovery_by_id(
            validator, get_discovery_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_list_of_discoveries_by_discovery_id(json_schema_validate, obj):
    json_schema_validate("jsd_e369e19c1a835567855984d9f2c628ef_v3_1_3_0").validate(obj)
    return True


def get_list_of_discoveries_by_discovery_id(api):
    endpoint_result = api.discovery.get_list_of_discoveries_by_discovery_id(
        id="string", ip_address="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_list_of_discoveries_by_discovery_id(api, validator):
    try:
        assert is_valid_get_list_of_discoveries_by_discovery_id(
            validator, get_list_of_discoveries_by_discovery_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_list_of_discoveries_by_discovery_id_default_val(api):
    endpoint_result = api.discovery.get_list_of_discoveries_by_discovery_id(
        id="string", ip_address=None, limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_list_of_discoveries_by_discovery_id_default_val(api, validator):
    try:
        assert is_valid_get_list_of_discoveries_by_discovery_id(
            validator, get_list_of_discoveries_by_discovery_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_discovered_network_devices_by_discovery_id(json_schema_validate, obj):
    json_schema_validate("jsd_f478b876b38a5cf094d80eced531b1a0_v3_1_3_0").validate(obj)
    return True


def get_discovered_network_devices_by_discovery_id(api):
    endpoint_result = api.discovery.get_discovered_network_devices_by_discovery_id(
        id="string", task_id="string"
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovered_network_devices_by_discovery_id(api, validator):
    try:
        assert is_valid_get_discovered_network_devices_by_discovery_id(
            validator, get_discovered_network_devices_by_discovery_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_discovered_network_devices_by_discovery_id_default_val(api):
    endpoint_result = api.discovery.get_discovered_network_devices_by_discovery_id(
        id="string", task_id=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovered_network_devices_by_discovery_id_default_val(api, validator):
    try:
        assert is_valid_get_discovered_network_devices_by_discovery_id(
            validator, get_discovered_network_devices_by_discovery_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_devices_discovered_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_a2f0cb47996d5bf7a3d5de89e2a002bb_v3_1_3_0").validate(obj)
    return True


def get_devices_discovered_by_id(api):
    endpoint_result = api.discovery.get_devices_discovered_by_id(
        id="string", task_id="string"
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_devices_discovered_by_id(api, validator):
    try:
        assert is_valid_get_devices_discovered_by_id(
            validator, get_devices_discovered_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_devices_discovered_by_id_default_val(api):
    endpoint_result = api.discovery.get_devices_discovered_by_id(
        id="string", task_id=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_devices_discovered_by_id_default_val(api, validator):
    try:
        assert is_valid_get_devices_discovered_by_id(
            validator, get_devices_discovered_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_discovered_devices_by_range(json_schema_validate, obj):
    json_schema_validate("jsd_7fd0ae0041dc59fb8aae545a8199d7b4_v3_1_3_0").validate(obj)
    return True


def get_discovered_devices_by_range(api):
    endpoint_result = api.discovery.get_discovered_devices_by_range(
        id="string", records_to_return=0, start_index=0, task_id="string"
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovered_devices_by_range(api, validator):
    try:
        assert is_valid_get_discovered_devices_by_range(
            validator, get_discovered_devices_by_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_discovered_devices_by_range_default_val(api):
    endpoint_result = api.discovery.get_discovered_devices_by_range(
        id="string", records_to_return=0, start_index=0, task_id=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovered_devices_by_range_default_val(api, validator):
    try:
        assert is_valid_get_discovered_devices_by_range(
            validator, get_discovered_devices_by_range_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_devices_from_discovery(json_schema_validate, obj):
    json_schema_validate("jsd_98155b212632561f886c01676b12a2b1_v3_1_3_0").validate(obj)
    return True


def get_network_devices_from_discovery(api):
    endpoint_result = api.discovery.get_network_devices_from_discovery(
        clistatus="value1,value2",
        http_status="value1,value2",
        id="string",
        ip_address="value1,value2",
        netconf_status="value1,value2",
        ping_status="value1,value2",
        snmp_status="value1,value2",
        sort_by="string",
        sort_order="string",
        task_id="string",
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_network_devices_from_discovery(api, validator):
    try:
        assert is_valid_get_network_devices_from_discovery(
            validator, get_network_devices_from_discovery(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_devices_from_discovery_default_val(api):
    endpoint_result = api.discovery.get_network_devices_from_discovery(
        clistatus=None,
        http_status=None,
        id="string",
        ip_address=None,
        netconf_status=None,
        ping_status=None,
        snmp_status=None,
        sort_by=None,
        sort_order=None,
        task_id=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_network_devices_from_discovery_default_val(api, validator):
    try:
        assert is_valid_get_network_devices_from_discovery(
            validator, get_network_devices_from_discovery_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_discovery_by_specified_range(json_schema_validate, obj):
    json_schema_validate("jsd_6cba543cfb0957e9bc38d8c7f49f3e47_v3_1_3_0").validate(obj)
    return True


def delete_discovery_by_specified_range(api):
    endpoint_result = api.discovery.delete_discovery_by_specified_range(
        records_to_delete=0, start_index=0
    )
    return endpoint_result


@pytest.mark.discovery
def test_delete_discovery_by_specified_range(api, validator):
    try:
        assert is_valid_delete_discovery_by_specified_range(
            validator, delete_discovery_by_specified_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_discovery_by_specified_range_default_val(api):
    endpoint_result = api.discovery.delete_discovery_by_specified_range(
        records_to_delete=0, start_index=0
    )
    return endpoint_result


@pytest.mark.discovery
def test_delete_discovery_by_specified_range_default_val(api, validator):
    try:
        assert is_valid_delete_discovery_by_specified_range(
            validator, delete_discovery_by_specified_range_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_discoveries_by_range(json_schema_validate, obj):
    json_schema_validate("jsd_e847420499a7592d993b7c7dff809f0d_v3_1_3_0").validate(obj)
    return True


def get_discoveries_by_range(api):
    endpoint_result = api.discovery.get_discoveries_by_range(
        records_to_return=0, start_index=0
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discoveries_by_range(api, validator):
    try:
        assert is_valid_get_discoveries_by_range(
            validator, get_discoveries_by_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_discoveries_by_range_default_val(api):
    endpoint_result = api.discovery.get_discoveries_by_range(
        records_to_return=0, start_index=0
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discoveries_by_range_default_val(api, validator):
    try:
        assert is_valid_get_discoveries_by_range(
            validator, get_discoveries_by_range_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_global_credentials(json_schema_validate, obj):
    json_schema_validate("jsd_3ce4a30581da554591309dd423a91e7a_v3_1_3_0").validate(obj)
    return True


def get_global_credentials(api):
    endpoint_result = api.discovery.get_global_credentials(
        credential_sub_type="string", order="string", sort_by="string"
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_global_credentials(api, validator):
    try:
        assert is_valid_get_global_credentials(validator, get_global_credentials(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_global_credentials_default_val(api):
    endpoint_result = api.discovery.get_global_credentials(
        credential_sub_type=None, order=None, sort_by=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_global_credentials_default_val(api, validator):
    try:
        assert is_valid_get_global_credentials(
            validator, get_global_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_cli_credentials(json_schema_validate, obj):
    json_schema_validate("jsd_678669d39d23589e85db0a63c414057c_v3_1_3_0").validate(obj)
    return True


def update_cli_credentials(api):
    endpoint_result = api.discovery.update_cli_credentials(
        active_validation=True,
        comments="string",
        credentialType="string",
        description="string",
        enablePassword="string",
        id="string",
        instanceTenantId="string",
        instanceUuid="string",
        password="string",
        payload=None,
        username="string",
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_cli_credentials(api, validator):
    try:
        assert is_valid_update_cli_credentials(validator, update_cli_credentials(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_cli_credentials_default_val(api):
    endpoint_result = api.discovery.update_cli_credentials(
        active_validation=True,
        comments=None,
        credentialType=None,
        description=None,
        enablePassword=None,
        id=None,
        instanceTenantId=None,
        instanceUuid=None,
        password=None,
        payload=None,
        username=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_cli_credentials_default_val(api, validator):
    try:
        assert is_valid_update_cli_credentials(
            validator, update_cli_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_cli_credentials(json_schema_validate, obj):
    json_schema_validate("jsd_c524f0ec199e5435bcaee56b423532e7_v3_1_3_0").validate(obj)
    return True


def create_cli_credentials(api):
    endpoint_result = api.discovery.create_cli_credentials(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_cli_credentials(api, validator):
    try:
        assert is_valid_create_cli_credentials(validator, create_cli_credentials(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_cli_credentials_default_val(api):
    endpoint_result = api.discovery.create_cli_credentials(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_cli_credentials_default_val(api, validator):
    try:
        assert is_valid_create_cli_credentials(
            validator, create_cli_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_http_read_credentials(json_schema_validate, obj):
    json_schema_validate("jsd_1ffcaccdd9f2530abf66adc98c3f0201_v3_1_3_0").validate(obj)
    return True


def create_http_read_credentials(api):
    endpoint_result = api.discovery.create_http_read_credentials(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_http_read_credentials(api, validator):
    try:
        assert is_valid_create_http_read_credentials(
            validator, create_http_read_credentials(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_http_read_credentials_default_val(api):
    endpoint_result = api.discovery.create_http_read_credentials(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_http_read_credentials_default_val(api, validator):
    try:
        assert is_valid_create_http_read_credentials(
            validator, create_http_read_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_http_read_credential(json_schema_validate, obj):
    json_schema_validate("jsd_1d1845268faf55f98bc952872259f16f_v3_1_3_0").validate(obj)
    return True


def update_http_read_credential(api):
    endpoint_result = api.discovery.update_http_read_credential(
        active_validation=True,
        comments="string",
        credentialType="string",
        description="string",
        id="string",
        instanceTenantId="string",
        instanceUuid="string",
        password="string",
        payload=None,
        port=0,
        secure=True,
        username="string",
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_http_read_credential(api, validator):
    try:
        assert is_valid_update_http_read_credential(
            validator, update_http_read_credential(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_http_read_credential_default_val(api):
    endpoint_result = api.discovery.update_http_read_credential(
        active_validation=True,
        comments=None,
        credentialType=None,
        description=None,
        id=None,
        instanceTenantId=None,
        instanceUuid=None,
        password=None,
        payload=None,
        port=None,
        secure=None,
        username=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_http_read_credential_default_val(api, validator):
    try:
        assert is_valid_update_http_read_credential(
            validator, update_http_read_credential_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_http_write_credentials(json_schema_validate, obj):
    json_schema_validate("jsd_6f6536a8f01d5863856a0a8308198e15_v3_1_3_0").validate(obj)
    return True


def update_http_write_credentials(api):
    endpoint_result = api.discovery.update_http_write_credentials(
        active_validation=True,
        comments="string",
        credentialType="string",
        description="string",
        id="string",
        instanceTenantId="string",
        instanceUuid="string",
        password="string",
        payload=None,
        port=0,
        secure=True,
        username="string",
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_http_write_credentials(api, validator):
    try:
        assert is_valid_update_http_write_credentials(
            validator, update_http_write_credentials(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_http_write_credentials_default_val(api):
    endpoint_result = api.discovery.update_http_write_credentials(
        active_validation=True,
        comments=None,
        credentialType=None,
        description=None,
        id=None,
        instanceTenantId=None,
        instanceUuid=None,
        password=None,
        payload=None,
        port=None,
        secure=None,
        username=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_http_write_credentials_default_val(api, validator):
    try:
        assert is_valid_update_http_write_credentials(
            validator, update_http_write_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_http_write_credentials(json_schema_validate, obj):
    json_schema_validate("jsd_1f77386a48895fa59dcddcc7dd4addb5_v3_1_3_0").validate(obj)
    return True


def create_http_write_credentials(api):
    endpoint_result = api.discovery.create_http_write_credentials(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_http_write_credentials(api, validator):
    try:
        assert is_valid_create_http_write_credentials(
            validator, create_http_write_credentials(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_http_write_credentials_default_val(api):
    endpoint_result = api.discovery.create_http_write_credentials(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_http_write_credentials_default_val(api, validator):
    try:
        assert is_valid_create_http_write_credentials(
            validator, create_http_write_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_netconf_credentials(json_schema_validate, obj):
    json_schema_validate("jsd_702f7cf4f24d54c6944a31ed308f8361_v3_1_3_0").validate(obj)
    return True


def update_netconf_credentials(api):
    endpoint_result = api.discovery.update_netconf_credentials(
        active_validation=True,
        comments="string",
        credentialType="string",
        description="string",
        id="string",
        instanceTenantId="string",
        instanceUuid="string",
        netconfPort="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_netconf_credentials(api, validator):
    try:
        assert is_valid_update_netconf_credentials(
            validator, update_netconf_credentials(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_netconf_credentials_default_val(api):
    endpoint_result = api.discovery.update_netconf_credentials(
        active_validation=True,
        comments=None,
        credentialType=None,
        description=None,
        id=None,
        instanceTenantId=None,
        instanceUuid=None,
        netconfPort=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_netconf_credentials_default_val(api, validator):
    try:
        assert is_valid_update_netconf_credentials(
            validator, update_netconf_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_netconf_credentials(json_schema_validate, obj):
    json_schema_validate("jsd_7f5645e6e819558fa08761dee45ca406_v3_1_3_0").validate(obj)
    return True


def create_netconf_credentials(api):
    endpoint_result = api.discovery.create_netconf_credentials(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_netconf_credentials(api, validator):
    try:
        assert is_valid_create_netconf_credentials(
            validator, create_netconf_credentials(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_netconf_credentials_default_val(api):
    endpoint_result = api.discovery.create_netconf_credentials(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_netconf_credentials_default_val(api, validator):
    try:
        assert is_valid_create_netconf_credentials(
            validator, create_netconf_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_snmp_read_community(json_schema_validate, obj):
    json_schema_validate("jsd_e3d7ad943d3a50fb8c3be7327669e557_v3_1_3_0").validate(obj)
    return True


def update_snmp_read_community(api):
    endpoint_result = api.discovery.update_snmp_read_community(
        active_validation=True,
        comments="string",
        credentialType="string",
        description="string",
        instanceUuid="string",
        payload=None,
        readCommunity="string",
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_snmp_read_community(api, validator):
    try:
        assert is_valid_update_snmp_read_community(
            validator, update_snmp_read_community(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_snmp_read_community_default_val(api):
    endpoint_result = api.discovery.update_snmp_read_community(
        active_validation=True,
        comments=None,
        credentialType=None,
        description=None,
        instanceUuid=None,
        payload=None,
        readCommunity=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_snmp_read_community_default_val(api, validator):
    try:
        assert is_valid_update_snmp_read_community(
            validator, update_snmp_read_community_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_snmp_read_community(json_schema_validate, obj):
    json_schema_validate("jsd_8d16471a58805b4aa2c757209d188aed_v3_1_3_0").validate(obj)
    return True


def create_snmp_read_community(api):
    endpoint_result = api.discovery.create_snmp_read_community(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_snmp_read_community(api, validator):
    try:
        assert is_valid_create_snmp_read_community(
            validator, create_snmp_read_community(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_snmp_read_community_default_val(api):
    endpoint_result = api.discovery.create_snmp_read_community(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_snmp_read_community_default_val(api, validator):
    try:
        assert is_valid_create_snmp_read_community(
            validator, create_snmp_read_community_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_snmp_write_community(json_schema_validate, obj):
    json_schema_validate("jsd_2a3a1bf404bf5772828f66f1e10f074d_v3_1_3_0").validate(obj)
    return True


def create_snmp_write_community(api):
    endpoint_result = api.discovery.create_snmp_write_community(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_snmp_write_community(api, validator):
    try:
        assert is_valid_create_snmp_write_community(
            validator, create_snmp_write_community(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_snmp_write_community_default_val(api):
    endpoint_result = api.discovery.create_snmp_write_community(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_snmp_write_community_default_val(api, validator):
    try:
        assert is_valid_create_snmp_write_community(
            validator, create_snmp_write_community_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_snmp_write_community(json_schema_validate, obj):
    json_schema_validate("jsd_92179760c9ea5c02b2b7368cac785f30_v3_1_3_0").validate(obj)
    return True


def update_snmp_write_community(api):
    endpoint_result = api.discovery.update_snmp_write_community(
        active_validation=True,
        comments="string",
        credentialType="string",
        description="string",
        instanceUuid="string",
        payload=None,
        writeCommunity="string",
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_snmp_write_community(api, validator):
    try:
        assert is_valid_update_snmp_write_community(
            validator, update_snmp_write_community(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_snmp_write_community_default_val(api):
    endpoint_result = api.discovery.update_snmp_write_community(
        active_validation=True,
        comments=None,
        credentialType=None,
        description=None,
        instanceUuid=None,
        payload=None,
        writeCommunity=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_snmp_write_community_default_val(api, validator):
    try:
        assert is_valid_update_snmp_write_community(
            validator, update_snmp_write_community_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_snmpv3_credentials(json_schema_validate, obj):
    json_schema_validate("jsd_2782bdc981805b5fad0a038966d52558_v3_1_3_0").validate(obj)
    return True


def update_snmpv3_credentials(api):
    endpoint_result = api.discovery.update_snmpv3_credentials(
        active_validation=True,
        authPassword="string",
        authType="string",
        comments="string",
        credentialType="string",
        description="string",
        id="string",
        instanceTenantId="string",
        instanceUuid="string",
        payload=None,
        privacyPassword="string",
        privacyType="string",
        snmpMode="string",
        username="string",
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_snmpv3_credentials(api, validator):
    try:
        assert is_valid_update_snmpv3_credentials(
            validator, update_snmpv3_credentials(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_snmpv3_credentials_default_val(api):
    endpoint_result = api.discovery.update_snmpv3_credentials(
        active_validation=True,
        authPassword=None,
        authType=None,
        comments=None,
        credentialType=None,
        description=None,
        id=None,
        instanceTenantId=None,
        instanceUuid=None,
        payload=None,
        privacyPassword=None,
        privacyType=None,
        snmpMode=None,
        username=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_snmpv3_credentials_default_val(api, validator):
    try:
        assert is_valid_update_snmpv3_credentials(
            validator, update_snmpv3_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_snmpv3_credentials(json_schema_validate, obj):
    json_schema_validate("jsd_ecdb2d14c29b5bf3ad79ed2e3cc70715_v3_1_3_0").validate(obj)
    return True


def create_snmpv3_credentials(api):
    endpoint_result = api.discovery.create_snmpv3_credentials(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_snmpv3_credentials(api, validator):
    try:
        assert is_valid_create_snmpv3_credentials(
            validator, create_snmpv3_credentials(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_snmpv3_credentials_default_val(api):
    endpoint_result = api.discovery.create_snmpv3_credentials(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_snmpv3_credentials_default_val(api, validator):
    try:
        assert is_valid_create_snmpv3_credentials(
            validator, create_snmpv3_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_global_credentials_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_a82cc61ddeae50969464f7b5d7d6bbf1_v3_1_3_0").validate(obj)
    return True


def delete_global_credentials_by_id(api):
    endpoint_result = api.discovery.delete_global_credentials_by_id(
        global_credential_id="string"
    )
    return endpoint_result


@pytest.mark.discovery
def test_delete_global_credentials_by_id(api, validator):
    try:
        assert is_valid_delete_global_credentials_by_id(
            validator, delete_global_credentials_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_global_credentials_by_id_default_val(api):
    endpoint_result = api.discovery.delete_global_credentials_by_id(
        global_credential_id="string"
    )
    return endpoint_result


@pytest.mark.discovery
def test_delete_global_credentials_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_global_credentials_by_id(
            validator, delete_global_credentials_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_global_credentials(json_schema_validate, obj):
    json_schema_validate("jsd_4f5d13316c8f53a0b78d881c738a15c6_v3_1_3_0").validate(obj)
    return True


def update_global_credentials(api):
    endpoint_result = api.discovery.update_global_credentials(
        active_validation=True,
        global_credential_id="string",
        payload=None,
        siteUuids=["string"],
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_global_credentials(api, validator):
    try:
        assert is_valid_update_global_credentials(
            validator, update_global_credentials(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_global_credentials_default_val(api):
    endpoint_result = api.discovery.update_global_credentials(
        active_validation=True,
        global_credential_id="string",
        payload=None,
        siteUuids=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_global_credentials_default_val(api, validator):
    try:
        assert is_valid_update_global_credentials(
            validator, update_global_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_credential_sub_type_by_credential_id(json_schema_validate, obj):
    json_schema_validate("jsd_659a37de9e4e5fab8c65b0701b074fd2_v3_1_3_0").validate(obj)
    return True


def get_credential_sub_type_by_credential_id(api):
    endpoint_result = api.discovery.get_credential_sub_type_by_credential_id(
        id="string"
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_credential_sub_type_by_credential_id(api, validator):
    try:
        assert is_valid_get_credential_sub_type_by_credential_id(
            validator, get_credential_sub_type_by_credential_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_credential_sub_type_by_credential_id_default_val(api):
    endpoint_result = api.discovery.get_credential_sub_type_by_credential_id(
        id="string"
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_credential_sub_type_by_credential_id_default_val(api, validator):
    try:
        assert is_valid_get_credential_sub_type_by_credential_id(
            validator, get_credential_sub_type_by_credential_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_snmp_properties(json_schema_validate, obj):
    json_schema_validate("jsd_9031dfb02d27503fab05602db7311e90_v3_1_3_0").validate(obj)
    return True


def get_snmp_properties(api):
    endpoint_result = api.discovery.get_snmp_properties()
    return endpoint_result


@pytest.mark.discovery
def test_get_snmp_properties(api, validator):
    try:
        assert is_valid_get_snmp_properties(validator, get_snmp_properties(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_snmp_properties_default_val(api):
    endpoint_result = api.discovery.get_snmp_properties()
    return endpoint_result


@pytest.mark.discovery
def test_get_snmp_properties_default_val(api, validator):
    try:
        assert is_valid_get_snmp_properties(
            validator, get_snmp_properties_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_update_snmp_properties(json_schema_validate, obj):
    json_schema_validate("jsd_da593242978c5047bb6b62b7f9475326_v3_1_3_0").validate(obj)
    return True


def create_update_snmp_properties(api):
    endpoint_result = api.discovery.create_update_snmp_properties(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_update_snmp_properties(api, validator):
    try:
        assert is_valid_create_update_snmp_properties(
            validator, create_update_snmp_properties(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_update_snmp_properties_default_val(api):
    endpoint_result = api.discovery.create_update_snmp_properties(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_update_snmp_properties_default_val(api, validator):
    try:
        assert is_valid_create_update_snmp_properties(
            validator, create_update_snmp_properties_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_global_credentials_v2(json_schema_validate, obj):
    json_schema_validate("jsd_1b3323a24b275402b97c7e9ccfd78c91_v3_1_3_0").validate(obj)
    return True


def update_global_credentials_v2(api):
    endpoint_result = api.discovery.update_global_credentials_v2(
        active_validation=True,
        cliCredential={
            "description": "string",
            "username": "string",
            "password": "string",
            "enablePassword": "string",
            "id": "string",
        },
        httpsRead={
            "description": "string",
            "username": "string",
            "password": "string",
            "port": 0,
            "id": "string",
        },
        httpsWrite={
            "description": "string",
            "username": "string",
            "password": "string",
            "port": 0,
            "id": "string",
        },
        payload=None,
        snmpV2cRead={
            "description": "string",
            "readCommunity": "string",
            "id": "string",
        },
        snmpV2cWrite={
            "description": "string",
            "writeCommunity": "string",
            "id": "string",
        },
        snmpV3={
            "authPassword": "string",
            "authType": "string",
            "snmpMode": "string",
            "privacyPassword": "string",
            "privacyType": "string",
            "username": "string",
            "description": "string",
            "id": "string",
        },
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_global_credentials_v2(api, validator):
    try:
        assert is_valid_update_global_credentials_v2(
            validator, update_global_credentials_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_global_credentials_v2_default_val(api):
    endpoint_result = api.discovery.update_global_credentials_v2(
        active_validation=True,
        cliCredential=None,
        httpsRead=None,
        httpsWrite=None,
        payload=None,
        snmpV2cRead=None,
        snmpV2cWrite=None,
        snmpV3=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_global_credentials_v2_default_val(api, validator):
    try:
        assert is_valid_update_global_credentials_v2(
            validator, update_global_credentials_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_global_credentials_v2(json_schema_validate, obj):
    json_schema_validate("jsd_3573d2ece28b509b8ef80b2b8c5c5f36_v3_1_3_0").validate(obj)
    return True


def create_global_credentials_v2(api):
    endpoint_result = api.discovery.create_global_credentials_v2(
        active_validation=True,
        cliCredential=[
            {
                "description": "string",
                "username": "string",
                "password": "string",
                "enablePassword": "string",
            }
        ],
        httpsRead=[
            {
                "description": "string",
                "username": "string",
                "password": "string",
                "port": 0,
            }
        ],
        httpsWrite=[
            {
                "description": "string",
                "username": "string",
                "password": "string",
                "port": 0,
            }
        ],
        payload=None,
        snmpV2cRead=[{"description": "string", "readCommunity": "string"}],
        snmpV2cWrite=[{"description": "string", "writeCommunity": "string"}],
        snmpV3=[
            {
                "description": "string",
                "username": "string",
                "privacyType": "string",
                "privacyPassword": "string",
                "authType": "string",
                "authPassword": "string",
                "snmpMode": "string",
            }
        ],
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_global_credentials_v2(api, validator):
    try:
        assert is_valid_create_global_credentials_v2(
            validator, create_global_credentials_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_global_credentials_v2_default_val(api):
    endpoint_result = api.discovery.create_global_credentials_v2(
        active_validation=True,
        cliCredential=None,
        httpsRead=None,
        httpsWrite=None,
        payload=None,
        snmpV2cRead=None,
        snmpV2cWrite=None,
        snmpV3=None,
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_global_credentials_v2_default_val(api, validator):
    try:
        assert is_valid_create_global_credentials_v2(
            validator, create_global_credentials_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_global_credentials_v2(json_schema_validate, obj):
    json_schema_validate("jsd_8a473a278a325c67abd310df49bae1bb_v3_1_3_0").validate(obj)
    return True


def get_all_global_credentials_v2(api):
    endpoint_result = api.discovery.get_all_global_credentials_v2()
    return endpoint_result


@pytest.mark.discovery
def test_get_all_global_credentials_v2(api, validator):
    try:
        assert is_valid_get_all_global_credentials_v2(
            validator, get_all_global_credentials_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_global_credentials_v2_default_val(api):
    endpoint_result = api.discovery.get_all_global_credentials_v2()
    return endpoint_result


@pytest.mark.discovery
def test_get_all_global_credentials_v2_default_val(api, validator):
    try:
        assert is_valid_get_all_global_credentials_v2(
            validator, get_all_global_credentials_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_global_credential_v2(json_schema_validate, obj):
    json_schema_validate("jsd_caa7cd8d7a3550cfb102cd3498494d04_v3_1_3_0").validate(obj)
    return True


def delete_global_credential_v2(api):
    endpoint_result = api.discovery.delete_global_credential_v2(id="string")
    return endpoint_result


@pytest.mark.discovery
def test_delete_global_credential_v2(api, validator):
    try:
        assert is_valid_delete_global_credential_v2(
            validator, delete_global_credential_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_global_credential_v2_default_val(api):
    endpoint_result = api.discovery.delete_global_credential_v2(id="string")
    return endpoint_result


@pytest.mark.discovery
def test_delete_global_credential_v2_default_val(api, validator):
    try:
        assert is_valid_delete_global_credential_v2(
            validator, delete_global_credential_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

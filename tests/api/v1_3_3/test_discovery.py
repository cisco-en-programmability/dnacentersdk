# -*- coding: utf-8 -*-
"""DNACenterAPI discovery API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.3', reason='version does not match')


def is_valid_get_count_of_all_discovery_jobs(json_schema_validate, obj):
    json_schema_validate('jsd_069d9823451b892d_v1_3_3').validate(obj)
    return True


def get_count_of_all_discovery_jobs(api):
    endpoint_result = api.discovery.get_count_of_all_discovery_jobs(

    )
    return endpoint_result


@pytest.mark.discovery
def test_get_count_of_all_discovery_jobs(api, validator):
    assert is_valid_get_count_of_all_discovery_jobs(
        validator,
        get_count_of_all_discovery_jobs(api)
    )


def get_count_of_all_discovery_jobs_default(api):
    endpoint_result = api.discovery.get_count_of_all_discovery_jobs(

    )
    return endpoint_result


@pytest.mark.discovery
def test_get_count_of_all_discovery_jobs_default(api, validator):
    try:
        assert is_valid_get_count_of_all_discovery_jobs(
            validator,
            get_count_of_all_discovery_jobs_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_netconf_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_17929bc7465bb564_v1_3_3').validate(obj)
    return True


def create_netconf_credentials(api):
    endpoint_result = api.discovery.create_netconf_credentials(
        active_validation=True,
        payload=[{'comments': 'string', 'credentialType': 'GLOBAL', 'description': 'string', 'id': 'string', 'instanceTenantId': 'string', 'instanceUuid': 'string', 'netconfPort': 'string'}]
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_netconf_credentials(api, validator):
    assert is_valid_create_netconf_credentials(
        validator,
        create_netconf_credentials(api)
    )


def create_netconf_credentials_default(api):
    endpoint_result = api.discovery.create_netconf_credentials(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_netconf_credentials_default(api, validator):
    try:
        assert is_valid_create_netconf_credentials(
            validator,
            create_netconf_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_snmp_write_community(json_schema_validate, obj):
    json_schema_validate('jsd_10b06a6a4f7bb3cb_v1_3_3').validate(obj)
    return True


def update_snmp_write_community(api):
    endpoint_result = api.discovery.update_snmp_write_community(
        active_validation=True,
        comments='string',
        credentialType='GLOBAL',
        description='string',
        id='string',
        instanceTenantId='string',
        instanceUuid='string',
        payload=None,
        writeCommunity='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_snmp_write_community(api, validator):
    assert is_valid_update_snmp_write_community(
        validator,
        update_snmp_write_community(api)
    )


def update_snmp_write_community_default(api):
    endpoint_result = api.discovery.update_snmp_write_community(
        active_validation=True,
        comments=None,
        credentialType=None,
        description=None,
        id=None,
        instanceTenantId=None,
        instanceUuid=None,
        payload=None,
        writeCommunity=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_snmp_write_community_default(api, validator):
    try:
        assert is_valid_update_snmp_write_community(
            validator,
            update_snmp_write_community_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_snmpv3_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_1da5ebdd434aacfe_v1_3_3').validate(obj)
    return True


def update_snmpv3_credentials(api):
    endpoint_result = api.discovery.update_snmpv3_credentials(
        active_validation=True,
        authPassword='string',
        authType='SHA',
        comments='string',
        credentialType='GLOBAL',
        description='string',
        id='string',
        instanceTenantId='string',
        instanceUuid='string',
        payload=None,
        privacyPassword='string',
        privacyType='DES',
        snmpMode='AUTHPRIV',
        username='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_snmpv3_credentials(api, validator):
    assert is_valid_update_snmpv3_credentials(
        validator,
        update_snmpv3_credentials(api)
    )


def update_snmpv3_credentials_default(api):
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
        username=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_snmpv3_credentials_default(api, validator):
    try:
        assert is_valid_update_snmpv3_credentials(
            validator,
            update_snmpv3_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_discoveries_by_range(json_schema_validate, obj):
    json_schema_validate('jsd_33b799d04d0a8907_v1_3_3').validate(obj)
    return True


def get_discoveries_by_range(api):
    endpoint_result = api.discovery.get_discoveries_by_range(
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discoveries_by_range(api, validator):
    assert is_valid_get_discoveries_by_range(
        validator,
        get_discoveries_by_range(api)
    )


def get_discoveries_by_range_default(api):
    endpoint_result = api.discovery.get_discoveries_by_range(
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discoveries_by_range_default(api, validator):
    try:
        assert is_valid_get_discoveries_by_range(
            validator,
            get_discoveries_by_range_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_network_devices_from_discovery(json_schema_validate, obj):
    json_schema_validate('jsd_3d9b99c343398a27_v1_3_3').validate(obj)
    return True


def get_network_devices_from_discovery(api):
    endpoint_result = api.discovery.get_network_devices_from_discovery(
        cli_status='value1,value2',
        http_status='value1,value2',
        id='string',
        ip_address='value1,value2',
        netconf_status='value1,value2',
        ping_status='value1,value2',
        snmp_status='value1,value2',
        sort_by='string',
        sort_order='string',
        task_id='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_network_devices_from_discovery(api, validator):
    assert is_valid_get_network_devices_from_discovery(
        validator,
        get_network_devices_from_discovery(api)
    )


def get_network_devices_from_discovery_default(api):
    endpoint_result = api.discovery.get_network_devices_from_discovery(
        cli_status=None,
        http_status=None,
        id='string',
        ip_address=None,
        netconf_status=None,
        ping_status=None,
        snmp_status=None,
        sort_by=None,
        sort_order=None,
        task_id=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_network_devices_from_discovery_default(api, validator):
    try:
        assert is_valid_get_network_devices_from_discovery(
            validator,
            get_network_devices_from_discovery_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_snmp_properties(json_schema_validate, obj):
    json_schema_validate('jsd_44974ba5435a801d_v1_3_3').validate(obj)
    return True


def get_snmp_properties(api):
    endpoint_result = api.discovery.get_snmp_properties(

    )
    return endpoint_result


@pytest.mark.discovery
def test_get_snmp_properties(api, validator):
    assert is_valid_get_snmp_properties(
        validator,
        get_snmp_properties(api)
    )


def get_snmp_properties_default(api):
    endpoint_result = api.discovery.get_snmp_properties(

    )
    return endpoint_result


@pytest.mark.discovery
def test_get_snmp_properties_default(api, validator):
    try:
        assert is_valid_get_snmp_properties(
            validator,
            get_snmp_properties_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_discovery_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_4c8cab5f435a80f4_v1_3_3').validate(obj)
    return True


def delete_discovery_by_id(api):
    endpoint_result = api.discovery.delete_discovery_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_delete_discovery_by_id(api, validator):
    assert is_valid_delete_discovery_by_id(
        validator,
        delete_discovery_by_id(api)
    )


def delete_discovery_by_id_default(api):
    endpoint_result = api.discovery.delete_discovery_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_delete_discovery_by_id_default(api, validator):
    try:
        assert is_valid_delete_discovery_by_id(
            validator,
            delete_discovery_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_snmp_read_community(json_schema_validate, obj):
    json_schema_validate('jsd_47a1b84b4e1b8044_v1_3_3').validate(obj)
    return True


def update_snmp_read_community(api):
    endpoint_result = api.discovery.update_snmp_read_community(
        active_validation=True,
        comments='string',
        credentialType='GLOBAL',
        description='string',
        id='string',
        instanceTenantId='string',
        instanceUuid='string',
        payload=None,
        readCommunity='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_snmp_read_community(api, validator):
    assert is_valid_update_snmp_read_community(
        validator,
        update_snmp_read_community(api)
    )


def update_snmp_read_community_default(api):
    endpoint_result = api.discovery.update_snmp_read_community(
        active_validation=True,
        comments=None,
        credentialType=None,
        description=None,
        id=None,
        instanceTenantId=None,
        instanceUuid=None,
        payload=None,
        readCommunity=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_snmp_read_community_default(api, validator):
    try:
        assert is_valid_update_snmp_read_community(
            validator,
            update_snmp_read_community_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_http_write_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_4d9ca8e2431a8a24_v1_3_3').validate(obj)
    return True


def create_http_write_credentials(api):
    endpoint_result = api.discovery.create_http_write_credentials(
        active_validation=True,
        payload=[{'comments': 'string', 'credentialType': 'GLOBAL', 'description': 'string', 'id': 'string', 'instanceTenantId': 'string', 'instanceUuid': 'string', 'password': 'string', 'port': 0, 'secure': True, 'username': 'string'}]
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_http_write_credentials(api, validator):
    assert is_valid_create_http_write_credentials(
        validator,
        create_http_write_credentials(api)
    )


def create_http_write_credentials_default(api):
    endpoint_result = api.discovery.create_http_write_credentials(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_http_write_credentials_default(api, validator):
    try:
        assert is_valid_create_http_write_credentials(
            validator,
            create_http_write_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_credential_sub_type_by_credential_id(json_schema_validate, obj):
    json_schema_validate('jsd_58a3699e489b9529_v1_3_3').validate(obj)
    return True


def get_credential_sub_type_by_credential_id(api):
    endpoint_result = api.discovery.get_credential_sub_type_by_credential_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_credential_sub_type_by_credential_id(api, validator):
    assert is_valid_get_credential_sub_type_by_credential_id(
        validator,
        get_credential_sub_type_by_credential_id(api)
    )


def get_credential_sub_type_by_credential_id_default(api):
    endpoint_result = api.discovery.get_credential_sub_type_by_credential_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_credential_sub_type_by_credential_id_default(api, validator):
    try:
        assert is_valid_get_credential_sub_type_by_credential_id(
            validator,
            get_credential_sub_type_by_credential_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_start_discovery(json_schema_validate, obj):
    json_schema_validate('jsd_55b439dc4239b140_v1_3_3').validate(obj)
    return True


def start_discovery(api):
    endpoint_result = api.discovery.start_discovery(
        active_validation=True,
        cdpLevel=0,
        discoveryType='string',
        enablePasswordList=['string'],
        globalCredentialIdList=['string'],
        httpReadCredential={'comments': 'string', 'credentialType': 'GLOBAL', 'description': 'string', 'id': 'string', 'instanceTenantId': 'string', 'instanceUuid': 'string', 'password': 'string', 'port': 0, 'secure': True, 'username': 'string'},
        httpWriteCredential={'comments': 'string', 'credentialType': 'GLOBAL', 'description': 'string', 'id': 'string', 'instanceTenantId': 'string', 'instanceUuid': 'string', 'password': 'string', 'port': 0, 'secure': True, 'username': 'string'},
        ipAddressList='string',
        ipFilterList=['string'],
        lldpLevel=0,
        name='string',
        netconfPort='string',
        noAddNewDevice=True,
        parentDiscoveryId='string',
        passwordList=['string'],
        payload=None,
        preferredMgmtIPMethod='string',
        protocolOrder='string',
        reDiscovery=True,
        retry=0,
        snmpAuthPassphrase='string',
        snmpAuthProtocol='string',
        snmpMode='string',
        snmpPrivPassphrase='string',
        snmpPrivProtocol='string',
        snmpROCommunity='string',
        snmpROCommunityDesc='string',
        snmpRWCommunity='string',
        snmpRWCommunityDesc='string',
        snmpUserName='string',
        snmpVersion='string',
        timeout=0,
        updateMgmtIp=True,
        userNameList=['string']
    )
    return endpoint_result


@pytest.mark.discovery
def test_start_discovery(api, validator):
    assert is_valid_start_discovery(
        validator,
        start_discovery(api)
    )


def start_discovery_default(api):
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
        noAddNewDevice=None,
        parentDiscoveryId=None,
        passwordList=None,
        payload=None,
        preferredMgmtIPMethod=None,
        protocolOrder=None,
        reDiscovery=None,
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
        updateMgmtIp=None,
        userNameList=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_start_discovery_default(api, validator):
    try:
        assert is_valid_start_discovery(
            validator,
            start_discovery_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_global_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_709fda3c42b8877a_v1_3_3').validate(obj)
    return True


def update_global_credentials(api):
    endpoint_result = api.discovery.update_global_credentials(
        active_validation=True,
        global_credential_id='string',
        payload=None,
        siteUuids=['string']
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_global_credentials(api, validator):
    assert is_valid_update_global_credentials(
        validator,
        update_global_credentials(api)
    )


def update_global_credentials_default(api):
    endpoint_result = api.discovery.update_global_credentials(
        active_validation=True,
        global_credential_id='string',
        payload=None,
        siteUuids=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_global_credentials_default(api, validator):
    try:
        assert is_valid_update_global_credentials(
            validator,
            update_global_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_snmp_write_community(json_schema_validate, obj):
    json_schema_validate('jsd_6bacb8d14639bdc7_v1_3_3').validate(obj)
    return True


def create_snmp_write_community(api):
    endpoint_result = api.discovery.create_snmp_write_community(
        active_validation=True,
        payload=[{'comments': 'string', 'credentialType': 'GLOBAL', 'description': 'string', 'id': 'string', 'instanceTenantId': 'string', 'instanceUuid': 'string', 'writeCommunity': 'string'}]
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_snmp_write_community(api, validator):
    assert is_valid_create_snmp_write_community(
        validator,
        create_snmp_write_community(api)
    )


def create_snmp_write_community_default(api):
    endpoint_result = api.discovery.create_snmp_write_community(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_snmp_write_community_default(api, validator):
    try:
        assert is_valid_create_snmp_write_community(
            validator,
            create_snmp_write_community_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_snmp_read_community(json_schema_validate, obj):
    json_schema_validate('jsd_7aa3da9d4e098ef2_v1_3_3').validate(obj)
    return True


def create_snmp_read_community(api):
    endpoint_result = api.discovery.create_snmp_read_community(
        active_validation=True,
        payload=[{'comments': 'string', 'credentialType': 'GLOBAL', 'description': 'string', 'id': 'string', 'instanceTenantId': 'string', 'instanceUuid': 'string', 'readCommunity': 'string'}]
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_snmp_read_community(api, validator):
    assert is_valid_create_snmp_read_community(
        validator,
        create_snmp_read_community(api)
    )


def create_snmp_read_community_default(api):
    endpoint_result = api.discovery.create_snmp_read_community(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_snmp_read_community_default(api, validator):
    try:
        assert is_valid_create_snmp_read_community(
            validator,
            create_snmp_read_community_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_discovery_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_63bb88b74f59aa17_v1_3_3').validate(obj)
    return True


def get_discovery_by_id(api):
    endpoint_result = api.discovery.get_discovery_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovery_by_id(api, validator):
    assert is_valid_get_discovery_by_id(
        validator,
        get_discovery_by_id(api)
    )


def get_discovery_by_id_default(api):
    endpoint_result = api.discovery.get_discovery_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovery_by_id_default(api, validator):
    try:
        assert is_valid_get_discovery_by_id(
            validator,
            get_discovery_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_http_read_credential(json_schema_validate, obj):
    json_schema_validate('jsd_89b36b4649999d81_v1_3_3').validate(obj)
    return True


def update_http_read_credential(api):
    endpoint_result = api.discovery.update_http_read_credential(
        active_validation=True,
        comments='string',
        credentialType='GLOBAL',
        description='string',
        id='string',
        instanceTenantId='string',
        instanceUuid='string',
        password='string',
        payload=None,
        port=0,
        secure=True,
        username='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_http_read_credential(api, validator):
    assert is_valid_update_http_read_credential(
        validator,
        update_http_read_credential(api)
    )


def update_http_read_credential_default(api):
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
        username=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_http_read_credential_default(api, validator):
    try:
        assert is_valid_update_http_read_credential(
            validator,
            update_http_read_credential_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_list_of_discoveries_by_discovery_id(json_schema_validate, obj):
    json_schema_validate('jsd_99872a134d0a9fb4_v1_3_3').validate(obj)
    return True


def get_list_of_discoveries_by_discovery_id(api):
    endpoint_result = api.discovery.get_list_of_discoveries_by_discovery_id(
        id='string',
        ip_address='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_list_of_discoveries_by_discovery_id(api, validator):
    assert is_valid_get_list_of_discoveries_by_discovery_id(
        validator,
        get_list_of_discoveries_by_discovery_id(api)
    )


def get_list_of_discoveries_by_discovery_id_default(api):
    endpoint_result = api.discovery.get_list_of_discoveries_by_discovery_id(
        id='string',
        ip_address=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_list_of_discoveries_by_discovery_id_default(api, validator):
    try:
        assert is_valid_get_list_of_discoveries_by_discovery_id(
            validator,
            get_list_of_discoveries_by_discovery_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_updates_discovery_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_9788b8fc4418831d_v1_3_3').validate(obj)
    return True


def updates_discovery_by_id(api):
    endpoint_result = api.discovery.updates_discovery_by_id(
        active_validation=True,
        attributeInfo={},
        cdpLevel=0,
        deviceIds='string',
        discoveryCondition='string',
        discoveryStatus='string',
        discoveryType='string',
        enablePasswordList='string',
        globalCredentialIdList=['string'],
        httpReadCredential={'comments': 'string', 'credentialType': 'GLOBAL', 'description': 'string', 'id': 'string', 'instanceTenantId': 'string', 'instanceUuid': 'string', 'password': 'string', 'port': 0, 'secure': True, 'username': 'string'},
        httpWriteCredential={'comments': 'string', 'credentialType': 'GLOBAL', 'description': 'string', 'id': 'string', 'instanceTenantId': 'string', 'instanceUuid': 'string', 'password': 'string', 'port': 0, 'secure': True, 'username': 'string'},
        id='string',
        ipAddressList='string',
        ipFilterList='string',
        isAutoCdp=True,
        lldpLevel=0,
        name='string',
        netconfPort='string',
        numDevices=0,
        parentDiscoveryId='string',
        passwordList='string',
        payload=None,
        preferredMgmtIPMethod='string',
        protocolOrder='string',
        retryCount=0,
        snmpAuthPassphrase='string',
        snmpAuthProtocol='string',
        snmpMode='string',
        snmpPrivPassphrase='string',
        snmpPrivProtocol='string',
        snmpRoCommunity='string',
        snmpRoCommunityDesc='string',
        snmpRwCommunity='string',
        snmpRwCommunityDesc='string',
        snmpUserName='string',
        timeOut=0,
        updateMgmtIp=True,
        userNameList='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_updates_discovery_by_id(api, validator):
    assert is_valid_updates_discovery_by_id(
        validator,
        updates_discovery_by_id(api)
    )


def updates_discovery_by_id_default(api):
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
        userNameList=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_updates_discovery_by_id_default(api, validator):
    try:
        assert is_valid_updates_discovery_by_id(
            validator,
            updates_discovery_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_cli_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_948ea8194348bc0b_v1_3_3').validate(obj)
    return True


def create_cli_credentials(api):
    endpoint_result = api.discovery.create_cli_credentials(
        active_validation=True,
        payload=[{'comments': 'string', 'credentialType': 'GLOBAL', 'description': 'string', 'enablePassword': 'string', 'id': 'string', 'instanceTenantId': 'string', 'instanceUuid': 'string', 'password': 'string', 'username': 'string'}]
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_cli_credentials(api, validator):
    assert is_valid_create_cli_credentials(
        validator,
        create_cli_credentials(api)
    )


def create_cli_credentials_default(api):
    endpoint_result = api.discovery.create_cli_credentials(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_cli_credentials_default(api, validator):
    try:
        assert is_valid_create_cli_credentials(
            validator,
            create_cli_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_discovered_devices_by_range(json_schema_validate, obj):
    json_schema_validate('jsd_a6b798ab4acaa34e_v1_3_3').validate(obj)
    return True


def get_discovered_devices_by_range(api):
    endpoint_result = api.discovery.get_discovered_devices_by_range(
        id='string',
        records_to_return=0,
        start_index=0,
        task_id='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovered_devices_by_range(api, validator):
    assert is_valid_get_discovered_devices_by_range(
        validator,
        get_discovered_devices_by_range(api)
    )


def get_discovered_devices_by_range_default(api):
    endpoint_result = api.discovery.get_discovered_devices_by_range(
        id='string',
        records_to_return=0,
        start_index=0,
        task_id=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovered_devices_by_range_default(api, validator):
    try:
        assert is_valid_get_discovered_devices_by_range(
            validator,
            get_discovered_devices_by_range_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_discovery_jobs_by_ip(json_schema_validate, obj):
    json_schema_validate('jsd_a4967be64dfaaa1a_v1_3_3').validate(obj)
    return True


def get_discovery_jobs_by_ip(api):
    endpoint_result = api.discovery.get_discovery_jobs_by_ip(
        ip_address='string',
        limit=0,
        name='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovery_jobs_by_ip(api, validator):
    assert is_valid_get_discovery_jobs_by_ip(
        validator,
        get_discovery_jobs_by_ip(api)
    )


def get_discovery_jobs_by_ip_default(api):
    endpoint_result = api.discovery.get_discovery_jobs_by_ip(
        ip_address=None,
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovery_jobs_by_ip_default(api, validator):
    try:
        assert is_valid_get_discovery_jobs_by_ip(
            validator,
            get_discovery_jobs_by_ip_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_update_snmp_properties(json_schema_validate, obj):
    json_schema_validate('jsd_a5ac99774c6bb541_v1_3_3').validate(obj)
    return True


def create_update_snmp_properties(api):
    endpoint_result = api.discovery.create_update_snmp_properties(
        active_validation=True,
        payload=[{'id': 'string', 'instanceTenantId': 'string', 'instanceUuid': 'string', 'intValue': 0, 'systemPropertyName': 'string'}]
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_update_snmp_properties(api, validator):
    assert is_valid_create_update_snmp_properties(
        validator,
        create_update_snmp_properties(api)
    )


def create_update_snmp_properties_default(api):
    endpoint_result = api.discovery.create_update_snmp_properties(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_update_snmp_properties_default(api, validator):
    try:
        assert is_valid_create_update_snmp_properties(
            validator,
            create_update_snmp_properties_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_snmpv3_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_979688084b7ba60d_v1_3_3').validate(obj)
    return True


def create_snmpv3_credentials(api):
    endpoint_result = api.discovery.create_snmpv3_credentials(
        active_validation=True,
        payload=[{'authPassword': 'string', 'authType': 'SHA', 'comments': 'string', 'credentialType': 'GLOBAL', 'description': 'string', 'id': 'string', 'instanceTenantId': 'string', 'instanceUuid': 'string', 'privacyPassword': 'string', 'privacyType': 'DES', 'snmpMode': 'AUTHPRIV', 'username': 'string'}]
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_snmpv3_credentials(api, validator):
    assert is_valid_create_snmpv3_credentials(
        validator,
        create_snmpv3_credentials(api)
    )


def create_snmpv3_credentials_default(api):
    endpoint_result = api.discovery.create_snmpv3_credentials(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_snmpv3_credentials_default(api, validator):
    try:
        assert is_valid_create_snmpv3_credentials(
            validator,
            create_snmpv3_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_http_write_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_b68a6bd8473a9a25_v1_3_3').validate(obj)
    return True


def update_http_write_credentials(api):
    endpoint_result = api.discovery.update_http_write_credentials(
        active_validation=True,
        comments='string',
        credentialType='GLOBAL',
        description='string',
        id='string',
        instanceTenantId='string',
        instanceUuid='string',
        password='string',
        payload=None,
        port=0,
        secure=True,
        username='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_http_write_credentials(api, validator):
    assert is_valid_update_http_write_credentials(
        validator,
        update_http_write_credentials(api)
    )


def update_http_write_credentials_default(api):
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
        username=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_http_write_credentials_default(api, validator):
    try:
        assert is_valid_update_http_write_credentials(
            validator,
            update_http_write_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_http_read_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_bf859ac64a0ba19c_v1_3_3').validate(obj)
    return True


def create_http_read_credentials(api):
    endpoint_result = api.discovery.create_http_read_credentials(
        active_validation=True,
        payload=[{'comments': 'string', 'credentialType': 'GLOBAL', 'description': 'string', 'id': 'string', 'instanceTenantId': 'string', 'instanceUuid': 'string', 'password': 'string', 'port': 0, 'secure': True, 'username': 'string'}]
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_http_read_credentials(api, validator):
    assert is_valid_create_http_read_credentials(
        validator,
        create_http_read_credentials(api)
    )


def create_http_read_credentials_default(api):
    endpoint_result = api.discovery.create_http_read_credentials(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_create_http_read_credentials_default(api, validator):
    try:
        assert is_valid_create_http_read_credentials(
            validator,
            create_http_read_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_netconf_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_c5acd9fa4c1a8abc_v1_3_3').validate(obj)
    return True


def update_netconf_credentials(api):
    endpoint_result = api.discovery.update_netconf_credentials(
        active_validation=True,
        comments='string',
        credentialType='GLOBAL',
        description='string',
        id='string',
        instanceTenantId='string',
        instanceUuid='string',
        netconfPort='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_netconf_credentials(api, validator):
    assert is_valid_update_netconf_credentials(
        validator,
        update_netconf_credentials(api)
    )


def update_netconf_credentials_default(api):
    endpoint_result = api.discovery.update_netconf_credentials(
        active_validation=True,
        comments=None,
        credentialType=None,
        description=None,
        id=None,
        instanceTenantId=None,
        instanceUuid=None,
        netconfPort=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_netconf_credentials_default(api, validator):
    try:
        assert is_valid_update_netconf_credentials(
            validator,
            update_netconf_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_discovery_by_specified_range(json_schema_validate, obj):
    json_schema_validate('jsd_c1ba9a424c08a01b_v1_3_3').validate(obj)
    return True


def delete_discovery_by_specified_range(api):
    endpoint_result = api.discovery.delete_discovery_by_specified_range(
        records_to_delete=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.discovery
def test_delete_discovery_by_specified_range(api, validator):
    assert is_valid_delete_discovery_by_specified_range(
        validator,
        delete_discovery_by_specified_range(api)
    )


def delete_discovery_by_specified_range_default(api):
    endpoint_result = api.discovery.delete_discovery_by_specified_range(
        records_to_delete=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.discovery
def test_delete_discovery_by_specified_range_default(api, validator):
    try:
        assert is_valid_delete_discovery_by_specified_range(
            validator,
            delete_discovery_by_specified_range_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_devices_discovered_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_a6965b454c9a8663_v1_3_3').validate(obj)
    return True


def get_devices_discovered_by_id(api):
    endpoint_result = api.discovery.get_devices_discovered_by_id(
        id='string',
        task_id='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_devices_discovered_by_id(api, validator):
    assert is_valid_get_devices_discovered_by_id(
        validator,
        get_devices_discovered_by_id(api)
    )


def get_devices_discovered_by_id_default(api):
    endpoint_result = api.discovery.get_devices_discovered_by_id(
        id='string',
        task_id=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_devices_discovered_by_id_default(api, validator):
    try:
        assert is_valid_get_devices_discovered_by_id(
            validator,
            get_devices_discovered_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_all_discovery(json_schema_validate, obj):
    json_schema_validate('jsd_db8e09234a988bab_v1_3_3').validate(obj)
    return True


def delete_all_discovery(api):
    endpoint_result = api.discovery.delete_all_discovery(

    )
    return endpoint_result


@pytest.mark.discovery
def test_delete_all_discovery(api, validator):
    assert is_valid_delete_all_discovery(
        validator,
        delete_all_discovery(api)
    )


def delete_all_discovery_default(api):
    endpoint_result = api.discovery.delete_all_discovery(

    )
    return endpoint_result


@pytest.mark.discovery
def test_delete_all_discovery_default(api, validator):
    try:
        assert is_valid_delete_all_discovery(
            validator,
            delete_all_discovery_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_global_credentials_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_f5ac590c4ca9975a_v1_3_3').validate(obj)
    return True


def delete_global_credentials_by_id(api):
    endpoint_result = api.discovery.delete_global_credentials_by_id(
        global_credential_id='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_delete_global_credentials_by_id(api, validator):
    assert is_valid_delete_global_credentials_by_id(
        validator,
        delete_global_credentials_by_id(api)
    )


def delete_global_credentials_by_id_default(api):
    endpoint_result = api.discovery.delete_global_credentials_by_id(
        global_credential_id='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_delete_global_credentials_by_id_default(api, validator):
    try:
        assert is_valid_delete_global_credentials_by_id(
            validator,
            delete_global_credentials_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_discovered_network_devices_by_discovery_id(json_schema_validate, obj):
    json_schema_validate('jsd_f6ac994f451ba011_v1_3_3').validate(obj)
    return True


def get_discovered_network_devices_by_discovery_id(api):
    endpoint_result = api.discovery.get_discovered_network_devices_by_discovery_id(
        id='string',
        task_id='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovered_network_devices_by_discovery_id(api, validator):
    assert is_valid_get_discovered_network_devices_by_discovery_id(
        validator,
        get_discovered_network_devices_by_discovery_id(api)
    )


def get_discovered_network_devices_by_discovery_id_default(api):
    endpoint_result = api.discovery.get_discovered_network_devices_by_discovery_id(
        id='string',
        task_id=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_discovered_network_devices_by_discovery_id_default(api, validator):
    try:
        assert is_valid_get_discovered_network_devices_by_discovery_id(
            validator,
            get_discovered_network_devices_by_discovery_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_global_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_ff816b8e435897eb_v1_3_3').validate(obj)
    return True


def get_global_credentials(api):
    endpoint_result = api.discovery.get_global_credentials(
        credential_sub_type='string',
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_global_credentials(api, validator):
    assert is_valid_get_global_credentials(
        validator,
        get_global_credentials(api)
    )


def get_global_credentials_default(api):
    endpoint_result = api.discovery.get_global_credentials(
        credential_sub_type=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_get_global_credentials_default(api, validator):
    try:
        assert is_valid_get_global_credentials(
            validator,
            get_global_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_cli_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_fba0d80747eb82e8_v1_3_3').validate(obj)
    return True


def update_cli_credentials(api):
    endpoint_result = api.discovery.update_cli_credentials(
        active_validation=True,
        comments='string',
        credentialType='GLOBAL',
        description='string',
        enablePassword='string',
        id='string',
        instanceTenantId='string',
        instanceUuid='string',
        password='string',
        payload=None,
        username='string'
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_cli_credentials(api, validator):
    assert is_valid_update_cli_credentials(
        validator,
        update_cli_credentials(api)
    )


def update_cli_credentials_default(api):
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
        username=None
    )
    return endpoint_result


@pytest.mark.discovery
def test_update_cli_credentials_default(api, validator):
    try:
        assert is_valid_update_cli_credentials(
            validator,
            update_cli_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

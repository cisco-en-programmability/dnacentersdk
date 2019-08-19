# -*- coding: utf-8 -*-
"""DNACenterAPI network_discovery API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_delete_all_discovery(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_all_discovery(api):
    endpoint_result = api.network_discovery.delete_all_discovery(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_delete_all_discovery(api):
    assert is_valid_delete_all_discovery(
        delete_all_discovery(api)
    )


def is_valid_create_cli_credentials(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def create_cli_credentials(api):
    endpoint_result = api.network_discovery.create_cli_credentials(
        payload=[{
            "username": "test_user_devnet",
            "password": "NO!$DATA!$"
        }],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_create_cli_credentials(api):
    assert is_valid_create_cli_credentials(
        create_cli_credentials(api)
    )


def is_valid_create_netconf_credentials(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def create_netconf_credentials(api):
    endpoint_result = api.network_discovery.create_netconf_credentials(
        payload=[{
            "netconfPort": '65533'  # range of 1 to 65535
        }],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_create_netconf_credentials(api):
    assert is_valid_create_netconf_credentials(
        create_netconf_credentials(api)
    )


def is_valid_create_snmp_write_community(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def create_snmp_write_community(api):
    endpoint_result = api.network_discovery.create_snmp_write_community(
        payload=[{
            "writeCommunity": "NO!$DATA!$",
            "description": "created snmpv2"
        }],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_create_snmp_write_community(api):
    assert is_valid_create_snmp_write_community(
        create_snmp_write_community(api)
    )


def is_valid_create_snmp_read_community(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def create_snmp_read_community(api):
    endpoint_result = api.network_discovery.create_snmp_read_community(
        payload=[{
            "readCommunity": "NO!$DATA!$",
            "description": "created snmpv2"
        }],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_create_snmp_read_community(api):
    assert is_valid_create_snmp_read_community(
        create_snmp_read_community(api)
    )


def is_valid_create_http_write_credentials(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def create_http_write_credentials(api):
    endpoint_result = api.network_discovery.create_http_write_credentials(
        payload=[{
            "username": "test_user_devnet",
            "password": "W.~&KV9ha",
            "port": 8080
        }],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_create_http_write_credentials(api):
    assert is_valid_create_http_write_credentials(
        create_http_write_credentials(api)
    )


def is_valid_create_http_read_credentials(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def create_http_read_credentials(api):
    endpoint_result = api.network_discovery.create_http_read_credentials(
        payload=[{
            "username": "test_user_devnet",
            "password": "W.~&KV9ha",
            "port": 8080
        }],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_create_http_read_credentials(api):
    assert is_valid_create_http_read_credentials(
        create_http_read_credentials(api)
    )


def is_valid_create_update_snmp_properties(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def create_update_snmp_properties(api):
    endpoint_result = api.network_discovery.create_update_snmp_properties(
        payload=[{
            "intValue": 1,
            "systemPropertyName": "version"
        }],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_create_update_snmp_properties(api):
    assert is_valid_create_update_snmp_properties(
        create_update_snmp_properties(api)
    )


def is_valid_create_snmpv3_credentials(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def create_snmpv3_credentials(api):
    endpoint_result = api.network_discovery.create_snmpv3_credentials(
        payload=[{
            "snmpMode": "NOAUTHNOPRIV",
            "username": "test_user_devnet"
        }],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_create_snmpv3_credentials(api):
    assert is_valid_create_snmpv3_credentials(
        create_snmpv3_credentials(api)
    )


def is_valid_get_credential_sub_type_by_credential_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_credential_sub_type_by_credential_id(api):
    endpoint_result = api.network_discovery.get_credential_sub_type_by_credential_id(
        id=get_global_credentials(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_get_credential_sub_type_by_credential_id(api):
    assert is_valid_get_credential_sub_type_by_credential_id(
        get_credential_sub_type_by_credential_id(api)
    )


def is_valid_get_snmp_properties(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_snmp_properties(api):
    endpoint_result = api.network_discovery.get_snmp_properties(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_get_snmp_properties(api):
    assert is_valid_get_snmp_properties(
        get_snmp_properties(api)
    )


def is_valid_start_discovery(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def start_discovery(api):
    credentials = api.network_discovery.get_global_credentials(credential_sub_type='CLI').response
    credentialIdList = [x.id for x in credentials]
    endpoint_result = api.network_discovery.start_discovery(
        cdpLevel=16,
        discoveryType='CDP',
        enablePasswordList=None,
        globalCredentialIdList=credentialIdList[0:5],
        httpReadCredential=None,
        httpWriteCredential=None,
        ipAddressList='10.10.22.22',
        ipFilterList=None,
        lldpLevel=None,
        name='start_discovery_test',
        netconfPort='65535',
        noAddNewDevice=None,
        parentDiscoveryId=None,
        passwordList=None,
        preferredMgmtIPMethod=None,
        protocolOrder='ssh',
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
        userNameList=None,
        payload=None,
        active_validation=True
    )
    time.sleep(10)
    return endpoint_result


@pytest.mark.network_discovery
def test_start_discovery(api):
    assert is_valid_start_discovery(
        start_discovery(api)
    )


def is_valid_get_count_of_all_discovery_jobs(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_count_of_all_discovery_jobs(api):
    endpoint_result = api.network_discovery.get_count_of_all_discovery_jobs(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_get_count_of_all_discovery_jobs(api):
    assert is_valid_get_count_of_all_discovery_jobs(
        get_count_of_all_discovery_jobs(api)
    )


def is_valid_get_discoveries_by_range(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_discoveries_by_range(api):
    endpoint_result = api.network_discovery.get_discoveries_by_range(
        records_to_return=10,
        start_index=1,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_get_discoveries_by_range(api):
    assert is_valid_get_discoveries_by_range(
        get_discoveries_by_range(api)
    )


def is_valid_get_network_devices_from_discovery(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_network_devices_from_discovery(api):
    endpoint_result = api.network_discovery.get_network_devices_from_discovery(
        id=get_discoveries_by_range(api).response[0].id,
        cli_status=None,
        http_status=None,
        ip_address=None,
        netconf_status=None,
        ping_status=None,
        snmp_status=None,
        sort_by=None,
        sort_order=None,
        task_id=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_get_network_devices_from_discovery(api):
    assert is_valid_get_network_devices_from_discovery(
        get_network_devices_from_discovery(api)
    )


def is_valid_get_discovery_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_discovery_by_id(api):
    endpoint_result = api.network_discovery.get_discovery_by_id(
        id=get_discoveries_by_range(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_get_discovery_by_id(api):
    assert is_valid_get_discovery_by_id(
        get_discovery_by_id(api)
    )


def is_valid_get_list_of_discoveries_by_discovery_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_list_of_discoveries_by_discovery_id(api):
    endpoint_result = api.network_discovery.get_list_of_discoveries_by_discovery_id(
        id=get_discoveries_by_range(api).response[0].id,
        ip_address=None,
        limit=None,
        offset=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_get_list_of_discoveries_by_discovery_id(api):
    assert is_valid_get_list_of_discoveries_by_discovery_id(
        get_list_of_discoveries_by_discovery_id(api)
    )


def is_valid_get_discovery_jobs_by_ip(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_discovery_jobs_by_ip(api):
    endpoint_result = api.network_discovery.get_discovery_jobs_by_ip(
        ip_address=get_discoveries_by_range(api).response[0].ipAddressList.split('-')[0],
        limit=None,
        name=None,
        offset=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_get_discovery_jobs_by_ip(api):
    assert is_valid_get_discovery_jobs_by_ip(
        get_discovery_jobs_by_ip(api)
    )


def is_valid_get_discovered_devices_by_range(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_discovered_devices_by_range(api):
    discoveries = get_discoveries_by_range(api).response
    filtered_discoveries = discoveries
    # list(filter(lambda x: x.numDevices and x.numDevices > 0, discoveries))
    endpoint_result = api.network_discovery.get_discovered_devices_by_range(
        id=filtered_discoveries[0].id,
        records_to_return=3,
        start_index=1,
        task_id=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_get_discovered_devices_by_range(api):
    assert is_valid_get_discovered_devices_by_range(
        get_discovered_devices_by_range(api)
    )


def is_valid_get_devices_discovered_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_devices_discovered_by_id(api):
    endpoint_result = api.network_discovery.get_devices_discovered_by_id(
        id=get_discoveries_by_range(api).response[0].id,
        task_id=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_get_devices_discovered_by_id(api):
    assert is_valid_get_devices_discovered_by_id(
        get_devices_discovered_by_id(api)
    )


def is_valid_get_global_credentials(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_global_credentials(api):
    endpoint_result = api.network_discovery.get_global_credentials(
        credential_sub_type='CLI',
        order=None,
        sort_by=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_get_global_credentials(api):
    assert is_valid_get_global_credentials(
        get_global_credentials(api)
    )


def is_valid_get_discovered_network_devices_by_discovery_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_discovered_network_devices_by_discovery_id(api):
    endpoint_result = api.network_discovery.get_discovered_network_devices_by_discovery_id(
        id=get_discoveries_by_range(api).response[0].id,
        task_id=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_get_discovered_network_devices_by_discovery_id(api):
    assert is_valid_get_discovered_network_devices_by_discovery_id(
        get_discovered_network_devices_by_discovery_id(api)
    )


def is_valid_delete_discovery_by_specified_range(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_discovery_by_specified_range(api):
    endpoint_result = api.network_discovery.delete_discovery_by_specified_range(
        records_to_delete=3,
        start_index=800,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_delete_discovery_by_specified_range(api):
    assert is_valid_delete_discovery_by_specified_range(
        delete_discovery_by_specified_range(api)
    )


def is_valid_update_netconf_credentials(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_netconf_credentials(api):
    credentials = api.network_discovery.get_global_credentials(credential_sub_type="NETCONF").response
    endpoint_result = api.network_discovery.update_netconf_credentials(
        comments=None,
        credentialType=None,
        description=None,
        id=list(filter(lambda x: x.netconfPort == '65533', credentials))[0].id,
        instanceTenantId=None,
        instanceUuid=None,
        netconfPort='65532',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_update_netconf_credentials(api):
    assert is_valid_update_netconf_credentials(
        update_netconf_credentials(api)
    )


def is_valid_update_global_credentials(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_global_credentials(api):
    credentials = api.network_discovery.get_global_credentials(credential_sub_type="NETCONF").response
    endpoint_result = api.network_discovery.update_global_credentials(
        global_credential_id=list(filter(lambda x: x.netconfPort == '65532', credentials))[0].id,
        siteUuids=[],
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_update_global_credentials(api):
    assert is_valid_update_global_credentials(
        update_global_credentials(api)
    )


def is_valid_delete_global_credentials_by_id_netconf(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_global_credentials_by_id_netconf(api):
    credentials = api.network_discovery.get_global_credentials(credential_sub_type="NETCONF").response
    endpoint_result = api.network_discovery.delete_global_credentials_by_id(
        global_credential_id=list(filter(lambda x: x.netconfPort == '65532', credentials))[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_netconf(api):
    assert is_valid_delete_global_credentials_by_id_netconf(
        delete_global_credentials_by_id_netconf(api)
    )


def is_valid_update_snmp_write_community(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_snmp_write_community(api):
    time.sleep(10)
    sub_type = "SNMPV2_WRITE_COMMUNITY"
    credentials = api.network_discovery.get_global_credentials(credential_sub_type=sub_type).response
    endpoint_result = api.network_discovery.update_snmp_write_community(
        comments=None,
        credentialType=None,
        description='created snmpv2_write',
        id=list(filter(lambda x: x.description == 'created snmpv2', credentials))[0].id,
        instanceTenantId=None,
        instanceUuid=None,
        writeCommunity='NO!$DATA!$',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_update_snmp_write_community(api):
    assert is_valid_update_snmp_write_community(
        update_snmp_write_community(api)
    )


def is_valid_update_snmp_read_community(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_snmp_read_community(api):
    time.sleep(10)
    sub_type = "SNMPV2_READ_COMMUNITY"
    credentials = api.network_discovery.get_global_credentials(credential_sub_type=sub_type).response
    endpoint_result = api.network_discovery.update_snmp_read_community(
        comments=None,
        credentialType=None,
        description='created snmpv2_read',
        id=list(filter(lambda x: x.description == 'created snmpv2', credentials))[0].id,
        instanceTenantId=None,
        instanceUuid=None,
        readCommunity='NO!$DATA!$',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_update_snmp_read_community(api):
    assert is_valid_update_snmp_read_community(
        update_snmp_read_community(api)
    )


def is_valid_update_cli_credentials(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_cli_credentials(api):
    time.sleep(10)
    credentials = api.network_discovery.get_global_credentials(credential_sub_type="CLI").response
    endpoint_result = api.network_discovery.update_cli_credentials(
        comments=None,
        credentialType=None,
        description='test: user devnet credentials',
        enablePassword=None,
        id=list(filter(lambda x: x.username == 'test_user_devnet', credentials))[0].id,
        instanceTenantId=None,
        instanceUuid=None,
        password='NO!$DATA!$',
        username='test_user_devnet',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_update_cli_credentials(api):
    assert is_valid_update_cli_credentials(
        update_cli_credentials(api)
    )


def is_valid_delete_global_credentials_by_id_snmp_write(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_global_credentials_by_id_snmp_write(api):
    time.sleep(10)
    sub_type = "SNMPV2_WRITE_COMMUNITY"
    credentials = api.network_discovery.get_global_credentials(credential_sub_type=sub_type).response
    endpoint_result = api.network_discovery.delete_global_credentials_by_id(
        global_credential_id=list(filter(lambda x: x.description == 'created snmpv2_write', credentials))[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_snmp_write(api):
    assert is_valid_delete_global_credentials_by_id_snmp_write(
        delete_global_credentials_by_id_snmp_write(api)
    )


def is_valid_delete_global_credentials_by_id_snmp_read(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_global_credentials_by_id_snmp_read(api):
    time.sleep(10)
    sub_type = "SNMPV2_READ_COMMUNITY"
    credentials = api.network_discovery.get_global_credentials(credential_sub_type=sub_type).response
    endpoint_result = api.network_discovery.delete_global_credentials_by_id(
        global_credential_id=list(filter(lambda x: x.description == 'created snmpv2_read', credentials))[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_snmp_read(api):
    assert is_valid_delete_global_credentials_by_id_snmp_read(
        delete_global_credentials_by_id_snmp_read(api)
    )


def is_valid_delete_global_credentials_by_id_cli(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_global_credentials_by_id_cli(api):
    time.sleep(10)
    credentials = api.network_discovery.get_global_credentials(credential_sub_type="CLI").response
    endpoint_result = api.network_discovery.delete_global_credentials_by_id(
        global_credential_id=list(filter(lambda x: x.username == 'test_user_devnet', credentials))[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_cli(api):
    assert is_valid_delete_global_credentials_by_id_cli(
        delete_global_credentials_by_id_cli(api)
    )


def is_valid_update_http_write_credentials(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_http_write_credentials(api):
    time.sleep(10)
    credentials = api.network_discovery.get_global_credentials(credential_sub_type="HTTP_WRITE").response
    endpoint_result = api.network_discovery.update_http_write_credentials(
        comments=None,
        credentialType=None,
        description='created http_write',
        id=list(filter(lambda x: x.username == 'test_user_devnet', credentials))[0].id,
        instanceTenantId=None,
        instanceUuid=None,
        password='W.~&KV9ha',
        port=8080,
        secure=None,
        username='test_user_devnet',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_update_http_write_credentials(api):
    assert is_valid_update_http_write_credentials(
        update_http_write_credentials(api)
    )


def is_valid_update_http_read_credential(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_http_read_credential(api):
    time.sleep(10)
    credentials = api.network_discovery.get_global_credentials(credential_sub_type="HTTP_READ").response
    endpoint_result = api.network_discovery.update_http_read_credential(
        comments=None,
        credentialType=None,
        description='created http_write',
        id=list(filter(lambda x: x.username == 'test_user_devnet', credentials))[0].id,
        instanceTenantId=None,
        instanceUuid=None,
        password='W.~&KV9ha',
        port=8080,
        secure=None,
        username='test_user_devnet',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_update_http_read_credential(api):
    assert is_valid_update_http_read_credential(
        update_http_read_credential(api)
    )


def is_valid_update_snmpv3_credentials(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def update_snmpv3_credentials(api):
    credentials = api.network_discovery.get_global_credentials(credential_sub_type="SNMPV3").response
    endpoint_result = api.network_discovery.update_snmpv3_credentials(
        authPassword=None,
        authType=None,
        comments=None,
        credentialType=None,
        description='created snmpv3',
        id=list(filter(lambda x: x.username == 'test_user_devnet', credentials))[0].id,
        instanceTenantId=None,
        instanceUuid=None,
        privacyPassword=None,
        privacyType=None,
        snmpMode='NOAUTHNOPRIV',
        username='test_user_devnet',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_update_snmpv3_credentials(api):
    assert is_valid_update_snmpv3_credentials(
        update_snmpv3_credentials(api)
    )


def is_valid_delete_global_credentials_by_id_http_write(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_global_credentials_by_id_http_write(api):
    credentials = api.network_discovery.get_global_credentials(credential_sub_type="HTTP_WRITE").response
    endpoint_result = api.network_discovery.delete_global_credentials_by_id(
        global_credential_id=list(filter(lambda x: x.username == 'test_user_devnet', credentials))[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_http_write(api):
    assert is_valid_delete_global_credentials_by_id_http_write(
        delete_global_credentials_by_id_http_write(api)
    )


def is_valid_delete_global_credentials_by_id_http_read(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_global_credentials_by_id_http_read(api):
    credentials = api.network_discovery.get_global_credentials(credential_sub_type="HTTP_READ").response
    endpoint_result = api.network_discovery.delete_global_credentials_by_id(
        global_credential_id=list(filter(lambda x: x.username == 'test_user_devnet', credentials))[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_http_read(api):
    assert is_valid_delete_global_credentials_by_id_http_read(
        delete_global_credentials_by_id_http_read(api)
    )


def is_valid_delete_global_credentials_by_id_snmpv3(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_global_credentials_by_id_snmpv3(api):
    credentials = api.network_discovery.get_global_credentials(credential_sub_type="SNMPV3").response
    endpoint_result = api.network_discovery.delete_global_credentials_by_id(
        global_credential_id=list(filter(lambda x: x.username == 'test_user_devnet', credentials))[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id_snmpv3(api):
    assert is_valid_delete_global_credentials_by_id_snmpv3(
        delete_global_credentials_by_id_snmpv3(api)
    )


def is_valid_updates_discovery_by_id_active(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def updates_discovery_by_id_active(api):
    discovery = get_discoveries_by_range(api).response[0]
    endpoint_result = api.network_discovery.updates_discovery_by_id(
        attributeInfo=None,
        cdpLevel=None,
        deviceIds=None,
        discoveryCondition=None,
        discoveryStatus=discovery.discoveryStatus,
        discoveryType=None,
        enablePasswordList=None,
        globalCredentialIdList=None,
        httpReadCredential=None,
        httpWriteCredential=None,
        id=discovery.id,
        ipAddressList=None,
        ipFilterList=None,
        isAutoCdp=None,
        lldpLevel=None,
        name=None,
        netconfPort=None,
        numDevices=None,
        parentDiscoveryId=None,
        passwordList=None,
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
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_updates_discovery_by_id_active(api):
    assert is_valid_updates_discovery_by_id_active(
        updates_discovery_by_id_active(api)
    )


def is_valid_updates_discovery_by_id_inactive(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def updates_discovery_by_id_inactive(api):
    discovery = get_discoveries_by_range(api).response[0]
    endpoint_result = api.network_discovery.updates_discovery_by_id(
        attributeInfo=None,
        cdpLevel=None,
        deviceIds=None,
        discoveryCondition=None,
        discoveryStatus=discovery.discoveryStatus,
        discoveryType=None,
        enablePasswordList=None,
        globalCredentialIdList=None,
        httpReadCredential=None,
        httpWriteCredential=None,
        id=discovery.id,
        ipAddressList=None,
        ipFilterList=None,
        isAutoCdp=None,
        lldpLevel=None,
        name=None,
        netconfPort=None,
        numDevices=None,
        parentDiscoveryId=None,
        passwordList=None,
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
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_updates_discovery_by_id_inactive(api):
    assert is_valid_updates_discovery_by_id_inactive(
        updates_discovery_by_id_inactive(api)
    )


def is_valid_delete_discovery_by_id(obj):
    some_keys = ['response', 'version']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def delete_discovery_by_id(api):
    time.sleep(10)
    discoveries = api.network_discovery.get_discoveries_by_range(
        records_to_return=500,
        start_index=1,
        payload=None
    ).response
    discovery_to_delete = list(filter(
        lambda x: x.ipAddressList == '10.10.22.22' and x.name == 'start_discovery_test', discoveries
    ))
    endpoint_result = api.network_discovery.delete_discovery_by_id(
        id=discovery_to_delete[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.network_discovery
def test_delete_discovery_by_id(api):
    assert is_valid_delete_discovery_by_id(
        delete_discovery_by_id(api)
    )

# -*- coding: utf-8 -*-
"""DNACenterAPI network_settings API fixtures and tests.

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


def is_valid_update_global_pool(obj):
    json_schema_validate('jsd_03b4c8b44919b964_v2_1_1').validate(obj)
    return True


def update_global_pool(api):
    endpoint_result = api.network_settings.update_global_pool(
        active_validation=True,
        payload=None,
        settings={'ippool': [{'ipPoolName': 'string', 'gateway': 'string', 'dhcpServerIps': ['string'], 'dnsServerIps': ['string'], 'id': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_global_pool(api):
    assert is_valid_update_global_pool(
        update_global_pool(api)
    )


def update_global_pool_default(api):
    endpoint_result = api.network_settings.update_global_pool(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_global_pool_default(api):
    try:
        assert is_valid_update_global_pool(
            update_global_pool_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_network(obj):
    json_schema_validate('jsd_38b7eb13449b9471_v2_1_1').validate(obj)
    return True


def get_network(api):
    endpoint_result = api.network_settings.get_network(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_network(api):
    assert is_valid_get_network(
        get_network(api)
    )


def get_network_default(api):
    endpoint_result = api.network_settings.get_network(
        site_id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_default(api):
    try:
        assert is_valid_get_network(
            get_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_sp_profile(obj):
    json_schema_validate('jsd_4ca2db1143ebb5d7_v2_1_1').validate(obj)
    return True


def delete_sp_profile(api):
    endpoint_result = api.network_settings.delete_sp_profile(
        sp_profile_name='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile(api):
    assert is_valid_delete_sp_profile(
        delete_sp_profile(api)
    )


def delete_sp_profile_default(api):
    endpoint_result = api.network_settings.delete_sp_profile(
        sp_profile_name='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile_default(api):
    try:
        assert is_valid_delete_sp_profile(
            delete_sp_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_global_ip_pool(obj):
    json_schema_validate('jsd_1eaa8b2148ab81de_v2_1_1').validate(obj)
    return True


def delete_global_ip_pool(api):
    endpoint_result = api.network_settings.delete_global_ip_pool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_global_ip_pool(api):
    assert is_valid_delete_global_ip_pool(
        delete_global_ip_pool(api)
    )


def delete_global_ip_pool_default(api):
    endpoint_result = api.network_settings.delete_global_ip_pool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_global_ip_pool_default(api):
    try:
        assert is_valid_delete_global_ip_pool(
            delete_global_ip_pool_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_sp_profile(obj):
    json_schema_validate('jsd_5087daae4cc98566_v2_1_1').validate(obj)
    return True


def update_sp_profile(api):
    endpoint_result = api.network_settings.update_sp_profile(
        active_validation=True,
        payload=None,
        settings={'qos': [{'profileName': 'string', 'model': 'string', 'wanProvider': 'string', 'oldProfileName': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_sp_profile(api):
    assert is_valid_update_sp_profile(
        update_sp_profile(api)
    )


def update_sp_profile_default(api):
    endpoint_result = api.network_settings.update_sp_profile(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_sp_profile_default(api):
    try:
        assert is_valid_update_sp_profile(
            update_sp_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_device_credential(obj):
    json_schema_validate('jsd_259eab3045988958_v2_1_1').validate(obj)
    return True


def delete_device_credential(api):
    endpoint_result = api.network_settings.delete_device_credential(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_device_credential(api):
    assert is_valid_delete_device_credential(
        delete_device_credential(api)
    )


def delete_device_credential_default(api):
    endpoint_result = api.network_settings.delete_device_credential(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_device_credential_default(api):
    try:
        assert is_valid_delete_device_credential(
            delete_device_credential_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_assign_credential_to_site(obj):
    json_schema_validate('jsd_4da91a544e29842d_v2_1_1').validate(obj)
    return True


def assign_credential_to_site(api):
    endpoint_result = api.network_settings.assign_credential_to_site(
        active_validation=True,
        cliId='string',
        httpRead='string',
        httpWrite='string',
        payload=None,
        site_id='string',
        snmpV2ReadId='string',
        snmpV2WriteId='string',
        snmpV3Id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_assign_credential_to_site(api):
    assert is_valid_assign_credential_to_site(
        assign_credential_to_site(api)
    )


def assign_credential_to_site_default(api):
    endpoint_result = api.network_settings.assign_credential_to_site(
        active_validation=True,
        cliId=None,
        httpRead=None,
        httpWrite=None,
        payload=None,
        site_id='string',
        snmpV2ReadId=None,
        snmpV2WriteId=None,
        snmpV3Id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_assign_credential_to_site_default(api):
    try:
        assert is_valid_assign_credential_to_site(
            assign_credential_to_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_network(obj):
    json_schema_validate('jsd_698bfbb44dcb9fca_v2_1_1').validate(obj)
    return True


def update_network(api):
    endpoint_result = api.network_settings.update_network(
        active_validation=True,
        payload=None,
        settings={'dhcpServer': ['string'], 'dnsServer': {'domainName': 'can only contain alphanumeric characters or hyphen', 'primaryIpAddress': 'valid range : 1.0.0.0 - 223.255.255.255', 'secondaryIpAddress': 'valid range : 1.0.0.0 - 223.255.255.255'}, 'syslogServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'snmpServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'netflowcollector': {'ipAddress': 'string', 'port': 0}, 'ntpServer': ['string'], 'timezone': 'string', 'messageOfTheday': {'bannerMessage': 'string', 'retainExistingBanner': True}, 'network_aaa': {'servers': 'Server type supported by ISE and AAA', 'ipAddress': 'Mandatory for ISE servers and for AAA consider this as additional Ip.', 'network': 'For AAA server consider it as primary IP and For ISE consider as Network', 'protocol': 'string', 'sharedSecret': 'Supported only by ISE servers'}, 'clientAndEndpoint_aaa': {'servers': 'string', 'ipAddress': 'Mandatory for ISE servers.', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'Supported only by ISE servers'}},
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_network(api):
    assert is_valid_update_network(
        update_network(api)
    )


def update_network_default(api):
    endpoint_result = api.network_settings.update_network(
        active_validation=True,
        payload=None,
        settings=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_network_default(api):
    try:
        assert is_valid_update_network(
            update_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_device_credentials(obj):
    json_schema_validate('jsd_4f947a1c4fc884f6_v2_1_1').validate(obj)
    return True


def update_device_credentials(api):
    endpoint_result = api.network_settings.update_device_credentials(
        active_validation=True,
        payload=None,
        settings={'cliCredential': {'description': 'string', 'username': 'string', 'password': 'string', 'enablePassword': 'string', 'id': 'string'}, 'snmpV2cRead': {'description': 'string', 'readCommunity': 'string', 'id': 'string'}, 'snmpV2cWrite': {'description': 'string', 'writeCommunity': 'string', 'id': 'string'}, 'snmpV3': {'authPassword': 'string', 'authType': 'string', 'snmpMode': 'string', 'privacyPassword': 'string', 'privacyType': 'string', 'username': 'string', 'description': 'string', 'id': 'string'}, 'httpsRead': {'name': 'string', 'username': 'string', 'password': 'string', 'port': 'string', 'id': 'string'}, 'httpsWrite': {'name': 'string', 'username': 'string', 'password': 'string', 'port': 'string', 'id': 'string'}}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_device_credentials(api):
    assert is_valid_update_device_credentials(
        update_device_credentials(api)
    )


def update_device_credentials_default(api):
    endpoint_result = api.network_settings.update_device_credentials(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_device_credentials_default(api):
    try:
        assert is_valid_update_device_credentials(
            update_device_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_service_provider_details(obj):
    json_schema_validate('jsd_70847bdc4d89a437_v2_1_1').validate(obj)
    return True


def get_service_provider_details(api):
    endpoint_result = api.network_settings.get_service_provider_details(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details(api):
    assert is_valid_get_service_provider_details(
        get_service_provider_details(api)
    )


def get_service_provider_details_default(api):
    endpoint_result = api.network_settings.get_service_provider_details(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details_default(api):
    try:
        assert is_valid_get_service_provider_details(
            get_service_provider_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_device_credential_details(obj):
    json_schema_validate('jsd_899f08e7401b82dd_v2_1_1').validate(obj)
    return True


def get_device_credential_details(api):
    endpoint_result = api.network_settings.get_device_credential_details(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_details(api):
    assert is_valid_get_device_credential_details(
        get_device_credential_details(api)
    )


def get_device_credential_details_default(api):
    endpoint_result = api.network_settings.get_device_credential_details(
        site_id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_details_default(api):
    try:
        assert is_valid_get_device_credential_details(
            get_device_credential_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_sp_profile(obj):
    json_schema_validate('jsd_a39a1a214debb781_v2_1_1').validate(obj)
    return True


def create_sp_profile(api):
    endpoint_result = api.network_settings.create_sp_profile(
        active_validation=True,
        payload=None,
        settings={'qos': [{'profileName': 'string', 'model': 'string', 'wanProvider': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_sp_profile(api):
    assert is_valid_create_sp_profile(
        create_sp_profile(api)
    )


def create_sp_profile_default(api):
    endpoint_result = api.network_settings.create_sp_profile(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_sp_profile_default(api):
    try:
        assert is_valid_create_sp_profile(
            create_sp_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_global_pool(obj):
    json_schema_validate('jsd_c0bca85643c8b58d_v2_1_1').validate(obj)
    return True


def get_global_pool(api):
    endpoint_result = api.network_settings.get_global_pool(
        limit='string',
        offset='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_global_pool(api):
    assert is_valid_get_global_pool(
        get_global_pool(api)
    )


def get_global_pool_default(api):
    endpoint_result = api.network_settings.get_global_pool(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_global_pool_default(api):
    try:
        assert is_valid_get_global_pool(
            get_global_pool_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_network(obj):
    json_schema_validate('jsd_be892bd84a78865a_v2_1_1').validate(obj)
    return True


def create_network(api):
    endpoint_result = api.network_settings.create_network(
        active_validation=True,
        payload=None,
        settings={'dhcpServer': ['string'], 'dnsServer': {'domainName': 'can only contain alphanumeric characters or hyphen', 'primaryIpAddress': 'valid range : 1.0.0.0 - 223.255.255.255', 'secondaryIpAddress': 'valid range : 1.0.0.0 - 223.255.255.255'}, 'syslogServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'snmpServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'netflowcollector': {'ipAddress': 'string', 'port': 0}, 'ntpServer': ['string'], 'timezone': 'string', 'messageOfTheday': {'bannerMessage': 'string', 'retainExistingBanner': True}, 'network_aaa': {'servers': 'Server type supported by ISE and AAA', 'ipAddress': 'Mandatory for ISE servers and for AAA consider this as additional Ip.', 'network': 'For AAA server consider it as primary IP and For ISE consider as Network', 'protocol': 'string', 'sharedSecret': 'Supported only by ISE servers'}, 'clientAndEndpoint_aaa': {'servers': 'string', 'ipAddress': 'Mandatory for ISE servers.', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'Supported only by ISE servers'}},
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_network(api):
    assert is_valid_create_network(
        create_network(api)
    )


def create_network_default(api):
    endpoint_result = api.network_settings.create_network(
        active_validation=True,
        payload=None,
        settings=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_network_default(api):
    try:
        assert is_valid_create_network(
            create_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_device_credentials(obj):
    json_schema_validate('jsd_fbb95b37484a9fce_v2_1_1').validate(obj)
    return True


def create_device_credentials(api):
    endpoint_result = api.network_settings.create_device_credentials(
        active_validation=True,
        payload=None,
        settings={'cliCredential': [{'description': 'string', 'username': 'string', 'password': 'string', 'enablePassword': 'string'}], 'snmpV2cRead': [{'description': 'string', 'readCommunity': 'string'}], 'snmpV2cWrite': [{'description': 'string', 'writeCommunity': 'string'}], 'snmpV3': [{'description': 'string', 'username': 'string', 'privacyType': 'AES128', 'privacyPassword': 'string', 'authType': 'SHA', 'authPassword': 'string', 'snmpMode': 'AUTHPRIV'}], 'httpsRead': [{'name': 'string', 'username': 'string', 'password': 'string', 'port': 0}], 'httpsWrite': [{'name': 'string', 'username': 'string', 'password': 'string', 'port': 0}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_device_credentials(api):
    assert is_valid_create_device_credentials(
        create_device_credentials(api)
    )


def create_device_credentials_default(api):
    endpoint_result = api.network_settings.create_device_credentials(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_device_credentials_default(api):
    try:
        assert is_valid_create_device_credentials(
            create_device_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_global_pool(obj):
    json_schema_validate('jsd_f793192a43dabed9_v2_1_1').validate(obj)
    return True


def create_global_pool(api):
    endpoint_result = api.network_settings.create_global_pool(
        active_validation=True,
        payload=None,
        settings={'ippool': [{'ipPoolName': 'string', 'type': 'Generic', 'ipPoolCidr': 'string', 'gateway': 'string', 'dhcpServerIps': ['string'], 'dnsServerIps': ['string'], 'IpAddressSpace': 'IPv6 or IPv4'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_global_pool(api):
    assert is_valid_create_global_pool(
        create_global_pool(api)
    )


def create_global_pool_default(api):
    endpoint_result = api.network_settings.create_global_pool(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_global_pool_default(api):
    try:
        assert is_valid_create_global_pool(
            create_global_pool_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

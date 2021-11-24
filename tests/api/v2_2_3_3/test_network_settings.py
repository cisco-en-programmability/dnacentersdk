# -*- coding: utf-8 -*-
"""DNACenterAPI network_settings API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.3.3', reason='version does not match')


def is_valid_assign_credential_to_site(json_schema_validate, obj):
    json_schema_validate('jsd_4e4f91ea42515ccdbc24549b84ca1e90_v2_2_3_3').validate(obj)
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
def test_assign_credential_to_site(api, validator):
    try:
        assert is_valid_assign_credential_to_site(
            validator,
            assign_credential_to_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_credential_to_site_default_val(api):
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
def test_assign_credential_to_site_default_val(api, validator):
    try:
        assert is_valid_assign_credential_to_site(
            validator,
            assign_credential_to_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_device_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_903cf2cac6f150c9bee9ade37921b162_v2_2_3_3').validate(obj)
    return True


def create_device_credentials(api):
    endpoint_result = api.network_settings.create_device_credentials(
        active_validation=True,
        payload=None,
        settings={'cliCredential': [{'description': 'string', 'username': 'string', 'password': 'string', 'enablePassword': 'string'}], 'snmpV2cRead': [{'description': 'string', 'readCommunity': 'string'}], 'snmpV2cWrite': [{'description': 'string', 'writeCommunity': 'string'}], 'snmpV3': [{'description': 'string', 'username': 'string', 'privacyType': 'string', 'privacyPassword': 'string', 'authType': 'string', 'authPassword': 'string', 'snmpMode': 'string'}], 'httpsRead': [{'name': 'string', 'username': 'string', 'password': 'string', 'port': 0}], 'httpsWrite': [{'name': 'string', 'username': 'string', 'password': 'string', 'port': 0}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_device_credentials(api, validator):
    try:
        assert is_valid_create_device_credentials(
            validator,
            create_device_credentials(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_device_credentials_default_val(api):
    endpoint_result = api.network_settings.create_device_credentials(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_device_credentials_default_val(api, validator):
    try:
        assert is_valid_create_device_credentials(
            validator,
            create_device_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_722d7161b33157dba957ba18eda440c2_v2_2_3_3').validate(obj)
    return True


def update_device_credentials(api):
    endpoint_result = api.network_settings.update_device_credentials(
        active_validation=True,
        payload=None,
        settings={'cliCredential': {'description': 'string', 'username': 'string', 'password': 'string', 'enablePassword': 'string', 'id': 'string'}, 'snmpV2cRead': {'description': 'string', 'readCommunity': 'string', 'id': 'string'}, 'snmpV2cWrite': {'description': 'string', 'writeCommunity': 'string', 'id': 'string'}, 'snmpV3': {'authPassword': 'string', 'authType': 'string', 'snmpMode': 'string', 'privacyPassword': 'string', 'privacyType': 'string', 'username': 'string', 'description': 'string', 'id': 'string'}, 'httpsRead': {'name': 'string', 'username': 'string', 'password': 'string', 'port': 'string', 'id': 'string'}, 'httpsWrite': {'name': 'string', 'username': 'string', 'password': 'string', 'port': 'string', 'id': 'string'}}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_device_credentials(api, validator):
    try:
        assert is_valid_update_device_credentials(
            validator,
            update_device_credentials(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_credentials_default_val(api):
    endpoint_result = api.network_settings.update_device_credentials(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_device_credentials_default_val(api, validator):
    try:
        assert is_valid_update_device_credentials(
            validator,
            update_device_credentials_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_credential_details(json_schema_validate, obj):
    json_schema_validate('jsd_403067d8cf995d9d99bdc31707817456_v2_2_3_3').validate(obj)
    return True


def get_device_credential_details(api):
    endpoint_result = api.network_settings.get_device_credential_details(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_details(api, validator):
    try:
        assert is_valid_get_device_credential_details(
            validator,
            get_device_credential_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_credential_details_default_val(api):
    endpoint_result = api.network_settings.get_device_credential_details(
        site_id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_details_default_val(api, validator):
    try:
        assert is_valid_get_device_credential_details(
            validator,
            get_device_credential_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_credential(json_schema_validate, obj):
    json_schema_validate('jsd_598e8e021f1c51eeaf0d102084481486_v2_2_3_3').validate(obj)
    return True


def delete_device_credential(api):
    endpoint_result = api.network_settings.delete_device_credential(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_device_credential(api, validator):
    try:
        assert is_valid_delete_device_credential(
            validator,
            delete_device_credential(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_credential_default_val(api):
    endpoint_result = api.network_settings.delete_device_credential(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_device_credential_default_val(api, validator):
    try:
        assert is_valid_delete_device_credential(
            validator,
            delete_device_credential_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_global_pool(json_schema_validate, obj):
    json_schema_validate('jsd_ebdcd84fc41754a69eaeacf7c0b0731c_v2_2_3_3').validate(obj)
    return True


def get_global_pool(api):
    endpoint_result = api.network_settings.get_global_pool(
        limit='string',
        offset='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_global_pool(api, validator):
    try:
        assert is_valid_get_global_pool(
            validator,
            get_global_pool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_global_pool_default_val(api):
    endpoint_result = api.network_settings.get_global_pool(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_global_pool_default_val(api, validator):
    try:
        assert is_valid_get_global_pool(
            validator,
            get_global_pool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_global_pool(json_schema_validate, obj):
    json_schema_validate('jsd_5c380301e3e05423bdc1857ff00ae77a_v2_2_3_3').validate(obj)
    return True


def update_global_pool(api):
    endpoint_result = api.network_settings.update_global_pool(
        active_validation=True,
        payload=None,
        settings={'ippool': [{'ipPoolName': 'string', 'gateway': 'string', 'dhcpServerIps': ['string'], 'dnsServerIps': ['string'], 'id': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_global_pool(api, validator):
    try:
        assert is_valid_update_global_pool(
            validator,
            update_global_pool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_global_pool_default_val(api):
    endpoint_result = api.network_settings.update_global_pool(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_global_pool_default_val(api, validator):
    try:
        assert is_valid_update_global_pool(
            validator,
            update_global_pool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_global_pool(json_schema_validate, obj):
    json_schema_validate('jsd_eecf4323cb285985be72a7e061891059_v2_2_3_3').validate(obj)
    return True


def create_global_pool(api):
    endpoint_result = api.network_settings.create_global_pool(
        active_validation=True,
        payload=None,
        settings={'ippool': [{'ipPoolName': 'string', 'type': 'string', 'ipPoolCidr': 'string', 'gateway': 'string', 'dhcpServerIps': ['string'], 'dnsServerIps': ['string'], 'IpAddressSpace': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_global_pool(api, validator):
    try:
        assert is_valid_create_global_pool(
            validator,
            create_global_pool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_global_pool_default_val(api):
    endpoint_result = api.network_settings.create_global_pool(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_global_pool_default_val(api, validator):
    try:
        assert is_valid_create_global_pool(
            validator,
            create_global_pool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_global_ip_pool(json_schema_validate, obj):
    json_schema_validate('jsd_61f9079863c95acd945c51f728cbf81f_v2_2_3_3').validate(obj)
    return True


def delete_global_ip_pool(api):
    endpoint_result = api.network_settings.delete_global_ip_pool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_global_ip_pool(api, validator):
    try:
        assert is_valid_delete_global_ip_pool(
            validator,
            delete_global_ip_pool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_global_ip_pool_default_val(api):
    endpoint_result = api.network_settings.delete_global_ip_pool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_global_ip_pool_default_val(api, validator):
    try:
        assert is_valid_delete_global_ip_pool(
            validator,
            delete_global_ip_pool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network(json_schema_validate, obj):
    json_schema_validate('jsd_40397b199c175281977a7e9e6bd9255b_v2_2_3_3').validate(obj)
    return True


def get_network(api):
    endpoint_result = api.network_settings.get_network(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_network(api, validator):
    try:
        assert is_valid_get_network(
            validator,
            get_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_default_val(api):
    endpoint_result = api.network_settings.get_network(
        site_id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_default_val(api, validator):
    try:
        assert is_valid_get_network(
            validator,
            get_network_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network(json_schema_validate, obj):
    json_schema_validate('jsd_6eca62ef076b5627a85b2a5959613fb8_v2_2_3_3').validate(obj)
    return True


def create_network(api):
    endpoint_result = api.network_settings.create_network(
        active_validation=True,
        payload=None,
        settings={'dhcpServer': ['string'], 'dnsServer': {'domainName': 'string', 'primaryIpAddress': 'string', 'secondaryIpAddress': 'string'}, 'syslogServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'snmpServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'netflowcollector': {'ipAddress': 'string', 'port': 0}, 'ntpServer': ['string'], 'timezone': 'string', 'messageOfTheday': {'bannerMessage': 'string', 'retainExistingBanner': 'string'}, 'network_aaa': {'servers': 'string', 'ipAddress': 'string', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'string'}, 'clientAndEndpoint_aaa': {'servers': 'string', 'ipAddress': 'string', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'string'}},
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_network(api, validator):
    try:
        assert is_valid_create_network(
            validator,
            create_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_network_default_val(api):
    endpoint_result = api.network_settings.create_network(
        active_validation=True,
        payload=None,
        settings=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_network_default_val(api, validator):
    try:
        assert is_valid_create_network(
            validator,
            create_network_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network(json_schema_validate, obj):
    json_schema_validate('jsd_e1b8c435195d56368c24a54dcce007d0_v2_2_3_3').validate(obj)
    return True


def update_network(api):
    endpoint_result = api.network_settings.update_network(
        active_validation=True,
        payload=None,
        settings={'dhcpServer': ['string'], 'dnsServer': {'domainName': 'string', 'primaryIpAddress': 'string', 'secondaryIpAddress': 'string'}, 'syslogServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'snmpServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'netflowcollector': {'ipAddress': 'string', 'port': 0}, 'ntpServer': ['string'], 'timezone': 'string', 'messageOfTheday': {'bannerMessage': 'string', 'retainExistingBanner': 'string'}, 'network_aaa': {'servers': 'string', 'ipAddress': 'string', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'string'}, 'clientAndEndpoint_aaa': {'servers': 'string', 'ipAddress': 'string', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'string'}},
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_network(api, validator):
    try:
        assert is_valid_update_network(
            validator,
            update_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_default_val(api):
    endpoint_result = api.network_settings.update_network(
        active_validation=True,
        payload=None,
        settings=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_network_default_val(api, validator):
    try:
        assert is_valid_update_network(
            validator,
            update_network_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_reserve_ip_subpool(json_schema_validate, obj):
    json_schema_validate('jsd_274851d84253559e9d3e81881a4bd2fc_v2_2_3_3').validate(obj)
    return True


def get_reserve_ip_subpool(api):
    endpoint_result = api.network_settings.get_reserve_ip_subpool(
        limit='string',
        offset='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_reserve_ip_subpool(api, validator):
    try:
        assert is_valid_get_reserve_ip_subpool(
            validator,
            get_reserve_ip_subpool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_reserve_ip_subpool_default_val(api):
    endpoint_result = api.network_settings.get_reserve_ip_subpool(
        limit=None,
        offset=None,
        site_id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_reserve_ip_subpool_default_val(api, validator):
    try:
        assert is_valid_get_reserve_ip_subpool(
            validator,
            get_reserve_ip_subpool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_release_reserve_ip_subpool(json_schema_validate, obj):
    json_schema_validate('jsd_eabbb425255a57578e9db00cda1f303a_v2_2_3_3').validate(obj)
    return True


def release_reserve_ip_subpool(api):
    endpoint_result = api.network_settings.release_reserve_ip_subpool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_release_reserve_ip_subpool(api, validator):
    try:
        assert is_valid_release_reserve_ip_subpool(
            validator,
            release_reserve_ip_subpool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def release_reserve_ip_subpool_default_val(api):
    endpoint_result = api.network_settings.release_reserve_ip_subpool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_release_reserve_ip_subpool_default_val(api, validator):
    try:
        assert is_valid_release_reserve_ip_subpool(
            validator,
            release_reserve_ip_subpool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reserve_ip_subpool(json_schema_validate, obj):
    json_schema_validate('jsd_700808cec6c85d9bb4bcc8f61f31296b_v2_2_3_3').validate(obj)
    return True


def reserve_ip_subpool(api):
    endpoint_result = api.network_settings.reserve_ip_subpool(
        active_validation=True,
        ipv4DhcpServers=['string'],
        ipv4DnsServers=['string'],
        ipv4GateWay='string',
        ipv4GlobalPool='string',
        ipv4Prefix=True,
        ipv4PrefixLength=0,
        ipv4Subnet='string',
        ipv4TotalHost=0,
        ipv6AddressSpace=True,
        ipv6DhcpServers=['string'],
        ipv6DnsServers=['string'],
        ipv6GateWay='string',
        ipv6GlobalPool='string',
        ipv6Prefix=True,
        ipv6PrefixLength=0,
        ipv6Subnet='string',
        ipv6TotalHost=0,
        name='string',
        payload=None,
        site_id='string',
        slaacSupport=True,
        type='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_reserve_ip_subpool(api, validator):
    try:
        assert is_valid_reserve_ip_subpool(
            validator,
            reserve_ip_subpool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def reserve_ip_subpool_default_val(api):
    endpoint_result = api.network_settings.reserve_ip_subpool(
        active_validation=True,
        ipv4DhcpServers=None,
        ipv4DnsServers=None,
        ipv4GateWay=None,
        ipv4GlobalPool=None,
        ipv4Prefix=None,
        ipv4PrefixLength=None,
        ipv4Subnet=None,
        ipv4TotalHost=None,
        ipv6AddressSpace=None,
        ipv6DhcpServers=None,
        ipv6DnsServers=None,
        ipv6GateWay=None,
        ipv6GlobalPool=None,
        ipv6Prefix=None,
        ipv6PrefixLength=None,
        ipv6Subnet=None,
        ipv6TotalHost=None,
        name=None,
        payload=None,
        site_id='string',
        slaacSupport=None,
        type=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_reserve_ip_subpool_default_val(api, validator):
    try:
        assert is_valid_reserve_ip_subpool(
            validator,
            reserve_ip_subpool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_reserve_ip_subpool(json_schema_validate, obj):
    json_schema_validate('jsd_07fd6083b0c65d03b2d53f10b3ece59d_v2_2_3_3').validate(obj)
    return True


def update_reserve_ip_subpool(api):
    endpoint_result = api.network_settings.update_reserve_ip_subpool(
        active_validation=True,
        id='string',
        ipv4DhcpServers=['string'],
        ipv4DnsServers=['string'],
        ipv4GateWay='string',
        ipv6AddressSpace=True,
        ipv6DhcpServers=['string'],
        ipv6DnsServers=['string'],
        ipv6GateWay='string',
        ipv6GlobalPool='string',
        ipv6Prefix=True,
        ipv6PrefixLength=0,
        ipv6Subnet='string',
        ipv6TotalHost=0,
        name='string',
        payload=None,
        site_id='string',
        slaacSupport=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_reserve_ip_subpool(api, validator):
    try:
        assert is_valid_update_reserve_ip_subpool(
            validator,
            update_reserve_ip_subpool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_reserve_ip_subpool_default_val(api):
    endpoint_result = api.network_settings.update_reserve_ip_subpool(
        active_validation=True,
        id=None,
        ipv4DhcpServers=None,
        ipv4DnsServers=None,
        ipv4GateWay=None,
        ipv6AddressSpace=None,
        ipv6DhcpServers=None,
        ipv6DnsServers=None,
        ipv6GateWay=None,
        ipv6GlobalPool=None,
        ipv6Prefix=None,
        ipv6PrefixLength=None,
        ipv6Subnet=None,
        ipv6TotalHost=None,
        name=None,
        payload=None,
        site_id='string',
        slaacSupport=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_reserve_ip_subpool_default_val(api, validator):
    try:
        assert is_valid_update_reserve_ip_subpool(
            validator,
            update_reserve_ip_subpool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_service_provider_details(json_schema_validate, obj):
    json_schema_validate('jsd_69dda850a0675b888048adf8d488aec1_v2_2_3_3').validate(obj)
    return True


def get_service_provider_details(api):
    endpoint_result = api.network_settings.get_service_provider_details(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details(api, validator):
    try:
        assert is_valid_get_service_provider_details(
            validator,
            get_service_provider_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_service_provider_details_default_val(api):
    endpoint_result = api.network_settings.get_service_provider_details(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details_default_val(api, validator):
    try:
        assert is_valid_get_service_provider_details(
            validator,
            get_service_provider_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sp_profile(json_schema_validate, obj):
    json_schema_validate('jsd_1ffa347eb411567a9c793696795250a5_v2_2_3_3').validate(obj)
    return True


def create_sp_profile(api):
    endpoint_result = api.network_settings.create_sp_profile(
        active_validation=True,
        payload=None,
        settings={'qos': [{'profileName': 'string', 'model': 'string', 'wanProvider': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_sp_profile(api, validator):
    try:
        assert is_valid_create_sp_profile(
            validator,
            create_sp_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_sp_profile_default_val(api):
    endpoint_result = api.network_settings.create_sp_profile(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_sp_profile_default_val(api, validator):
    try:
        assert is_valid_create_sp_profile(
            validator,
            create_sp_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_sp_profile(json_schema_validate, obj):
    json_schema_validate('jsd_03e22c99a82f5764828810acb45e7a9e_v2_2_3_3').validate(obj)
    return True


def update_sp_profile(api):
    endpoint_result = api.network_settings.update_sp_profile(
        active_validation=True,
        payload=None,
        settings={'qos': [{'profileName': 'string', 'model': 'string', 'wanProvider': 'string', 'oldProfileName': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_sp_profile(api, validator):
    try:
        assert is_valid_update_sp_profile(
            validator,
            update_sp_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_sp_profile_default_val(api):
    endpoint_result = api.network_settings.update_sp_profile(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_sp_profile_default_val(api, validator):
    try:
        assert is_valid_update_sp_profile(
            validator,
            update_sp_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sp_profile(json_schema_validate, obj):
    json_schema_validate('jsd_35598a1d68f15e02adc37239b3fcbbb6_v2_2_3_3').validate(obj)
    return True


def delete_sp_profile(api):
    endpoint_result = api.network_settings.delete_sp_profile(
        sp_profile_name='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile(api, validator):
    try:
        assert is_valid_delete_sp_profile(
            validator,
            delete_sp_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_sp_profile_default_val(api):
    endpoint_result = api.network_settings.delete_sp_profile(
        sp_profile_name='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile_default_val(api, validator):
    try:
        assert is_valid_delete_sp_profile(
            validator,
            delete_sp_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

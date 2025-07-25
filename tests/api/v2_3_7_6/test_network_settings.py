# -*- coding: utf-8 -*-
"""DNACenterAPI network_settings API fixtures and tests.

Copyright (c) 2024 Cisco Systems.

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
    DNA_CENTER_VERSION != "2.3.7.6", reason="version does not match"
)


def is_valid_assign_device_credential_to_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_4e4f91ea42515ccdbc24549b84ca1e90_v2_3_7_6").validate(obj)
    return True


def assign_device_credential_to_site_v1(api):
    endpoint_result = api.network_settings.assign_device_credential_to_site_v1(
        active_validation=True,
        cliId="string",
        httpRead="string",
        httpWrite="string",
        payload=None,
        site_id="string",
        snmpV2ReadId="string",
        snmpV2WriteId="string",
        snmpV3Id="string",
    )
    return endpoint_result


@pytest.mark.network_settings
def test_assign_device_credential_to_site_v1(api, validator):
    try:
        assert is_valid_assign_device_credential_to_site_v1(
            validator, assign_device_credential_to_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_device_credential_to_site_v1_default_val(api):
    endpoint_result = api.network_settings.assign_device_credential_to_site_v1(
        active_validation=True,
        cliId=None,
        httpRead=None,
        httpWrite=None,
        payload=None,
        site_id="string",
        snmpV2ReadId=None,
        snmpV2WriteId=None,
        snmpV3Id=None,
    )
    return endpoint_result


@pytest.mark.network_settings
def test_assign_device_credential_to_site_v1_default_val(api, validator):
    try:
        assert is_valid_assign_device_credential_to_site_v1(
            validator, assign_device_credential_to_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_device_credentials_v1(json_schema_validate, obj):
    json_schema_validate("jsd_903cf2cac6f150c9bee9ade37921b162_v2_3_7_6").validate(obj)
    return True


def create_device_credentials_v1(api):
    endpoint_result = api.network_settings.create_device_credentials_v1(
        active_validation=True,
        payload=None,
        settings={
            "cliCredential": [
                {
                    "description": "string",
                    "username": "string",
                    "password": "string",
                    "enablePassword": "string",
                }
            ],
            "snmpV2cRead": [{"description": "string", "readCommunity": "string"}],
            "snmpV2cWrite": [{"description": "string", "writeCommunity": "string"}],
            "snmpV3": [
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
            "httpsRead": [
                {
                    "name": "string",
                    "username": "string",
                    "password": "string",
                    "port": 0,
                }
            ],
            "httpsWrite": [
                {
                    "name": "string",
                    "username": "string",
                    "password": "string",
                    "port": 0,
                }
            ],
        },
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_device_credentials_v1(api, validator):
    try:
        assert is_valid_create_device_credentials_v1(
            validator, create_device_credentials_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_device_credentials_v1_default_val(api):
    endpoint_result = api.network_settings.create_device_credentials_v1(
        active_validation=True, payload=None, settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_device_credentials_v1_default_val(api, validator):
    try:
        assert is_valid_create_device_credentials_v1(
            validator, create_device_credentials_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_credentials_v1(json_schema_validate, obj):
    json_schema_validate("jsd_722d7161b33157dba957ba18eda440c2_v2_3_7_6").validate(obj)
    return True


def update_device_credentials_v1(api):
    endpoint_result = api.network_settings.update_device_credentials_v1(
        active_validation=True,
        payload=None,
        settings={
            "cliCredential": {
                "description": "string",
                "username": "string",
                "password": "string",
                "enablePassword": "string",
                "id": "string",
            },
            "snmpV2cRead": {
                "description": "string",
                "readCommunity": "string",
                "id": "string",
            },
            "snmpV2cWrite": {
                "description": "string",
                "writeCommunity": "string",
                "id": "string",
            },
            "snmpV3": {
                "authPassword": "string",
                "authType": "string",
                "snmpMode": "string",
                "privacyPassword": "string",
                "privacyType": "string",
                "username": "string",
                "description": "string",
                "id": "string",
            },
            "httpsRead": {
                "name": "string",
                "username": "string",
                "password": "string",
                "port": "string",
                "id": "string",
            },
            "httpsWrite": {
                "name": "string",
                "username": "string",
                "password": "string",
                "port": "string",
                "id": "string",
            },
        },
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_device_credentials_v1(api, validator):
    try:
        assert is_valid_update_device_credentials_v1(
            validator, update_device_credentials_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_credentials_v1_default_val(api):
    endpoint_result = api.network_settings.update_device_credentials_v1(
        active_validation=True, payload=None, settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_device_credentials_v1_default_val(api, validator):
    try:
        assert is_valid_update_device_credentials_v1(
            validator, update_device_credentials_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_credential_details_v1(json_schema_validate, obj):
    json_schema_validate("jsd_403067d8cf995d9d99bdc31707817456_v2_3_7_6").validate(obj)
    return True


def get_device_credential_details_v1(api):
    endpoint_result = api.network_settings.get_device_credential_details_v1(
        site_id="string"
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_details_v1(api, validator):
    try:
        assert is_valid_get_device_credential_details_v1(
            validator, get_device_credential_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_credential_details_v1_default_val(api):
    endpoint_result = api.network_settings.get_device_credential_details_v1(
        site_id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_credential_details_v1(
            validator, get_device_credential_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_credential_v1(json_schema_validate, obj):
    json_schema_validate("jsd_598e8e021f1c51eeaf0d102084481486_v2_3_7_6").validate(obj)
    return True


def delete_device_credential_v1(api):
    endpoint_result = api.network_settings.delete_device_credential_v1(id="string")
    return endpoint_result


@pytest.mark.network_settings
def test_delete_device_credential_v1(api, validator):
    try:
        assert is_valid_delete_device_credential_v1(
            validator, delete_device_credential_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_credential_v1_default_val(api):
    endpoint_result = api.network_settings.delete_device_credential_v1(id="string")
    return endpoint_result


@pytest.mark.network_settings
def test_delete_device_credential_v1_default_val(api, validator):
    try:
        assert is_valid_delete_device_credential_v1(
            validator, delete_device_credential_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_global_pool_v1(json_schema_validate, obj):
    json_schema_validate("jsd_ebdcd84fc41754a69eaeacf7c0b0731c_v2_3_7_6").validate(obj)
    return True


def get_global_pool_v1(api):
    endpoint_result = api.network_settings.get_global_pool_v1(limit=0, offset=0)
    return endpoint_result


@pytest.mark.network_settings
def test_get_global_pool_v1(api, validator):
    try:
        assert is_valid_get_global_pool_v1(validator, get_global_pool_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_global_pool_v1_default_val(api):
    endpoint_result = api.network_settings.get_global_pool_v1(limit=None, offset=None)
    return endpoint_result


@pytest.mark.network_settings
def test_get_global_pool_v1_default_val(api, validator):
    try:
        assert is_valid_get_global_pool_v1(
            validator, get_global_pool_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_global_pool_v1(json_schema_validate, obj):
    json_schema_validate("jsd_5c380301e3e05423bdc1857ff00ae77a_v2_3_7_6").validate(obj)
    return True


def update_global_pool_v1(api):
    endpoint_result = api.network_settings.update_global_pool_v1(
        active_validation=True,
        payload=None,
        settings={
            "ippool": [
                {
                    "ipPoolName": "string",
                    "gateway": "string",
                    "dhcpServerIps": ["string"],
                    "dnsServerIps": ["string"],
                    "id": "string",
                }
            ]
        },
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_global_pool_v1(api, validator):
    try:
        assert is_valid_update_global_pool_v1(validator, update_global_pool_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_global_pool_v1_default_val(api):
    endpoint_result = api.network_settings.update_global_pool_v1(
        active_validation=True, payload=None, settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_global_pool_v1_default_val(api, validator):
    try:
        assert is_valid_update_global_pool_v1(
            validator, update_global_pool_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_global_pool_v1(json_schema_validate, obj):
    json_schema_validate("jsd_eecf4323cb285985be72a7e061891059_v2_3_7_6").validate(obj)
    return True


def create_global_pool_v1(api):
    endpoint_result = api.network_settings.create_global_pool_v1(
        active_validation=True,
        payload=None,
        settings={
            "ippool": [
                {
                    "ipPoolName": "string",
                    "type": "string",
                    "ipPoolCidr": "string",
                    "gateway": "string",
                    "dhcpServerIps": ["string"],
                    "dnsServerIps": ["string"],
                    "IpAddressSpace": "string",
                }
            ]
        },
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_global_pool_v1(api, validator):
    try:
        assert is_valid_create_global_pool_v1(validator, create_global_pool_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_global_pool_v1_default_val(api):
    endpoint_result = api.network_settings.create_global_pool_v1(
        active_validation=True, payload=None, settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_global_pool_v1_default_val(api, validator):
    try:
        assert is_valid_create_global_pool_v1(
            validator, create_global_pool_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_global_ip_pool_v1(json_schema_validate, obj):
    json_schema_validate("jsd_61f9079863c95acd945c51f728cbf81f_v2_3_7_6").validate(obj)
    return True


def delete_global_ip_pool_v1(api):
    endpoint_result = api.network_settings.delete_global_ip_pool_v1(id="string")
    return endpoint_result


@pytest.mark.network_settings
def test_delete_global_ip_pool_v1(api, validator):
    try:
        assert is_valid_delete_global_ip_pool_v1(
            validator, delete_global_ip_pool_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_global_ip_pool_v1_default_val(api):
    endpoint_result = api.network_settings.delete_global_ip_pool_v1(id="string")
    return endpoint_result


@pytest.mark.network_settings
def test_delete_global_ip_pool_v1_default_val(api, validator):
    try:
        assert is_valid_delete_global_ip_pool_v1(
            validator, delete_global_ip_pool_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_v1(json_schema_validate, obj):
    json_schema_validate("jsd_40397b199c175281977a7e9e6bd9255b_v2_3_7_6").validate(obj)
    return True


def get_network_v1(api):
    endpoint_result = api.network_settings.get_network_v1(site_id="string")
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_v1(api, validator):
    try:
        assert is_valid_get_network_v1(validator, get_network_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_v1_default_val(api):
    endpoint_result = api.network_settings.get_network_v1(site_id=None)
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_v1_default_val(api, validator):
    try:
        assert is_valid_get_network_v1(validator, get_network_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_v1(json_schema_validate, obj):
    json_schema_validate("jsd_6eca62ef076b5627a85b2a5959613fb8_v2_3_7_6").validate(obj)
    return True


def create_network_v1(api):
    endpoint_result = api.network_settings.create_network_v1(
        active_validation=True,
        payload=None,
        settings={
            "dhcpServer": ["string"],
            "dnsServer": {
                "domainName": "string",
                "primaryIpAddress": "string",
                "secondaryIpAddress": "string",
            },
            "syslogServer": {"ipAddresses": ["string"], "configureDnacIP": True},
            "snmpServer": {"ipAddresses": ["string"], "configureDnacIP": True},
            "netflowcollector": {"ipAddress": "string", "port": 0},
            "ntpServer": ["string"],
            "timezone": "string",
            "messageOfTheday": {
                "bannerMessage": "string",
                "retainExistingBanner": "string",
            },
            "network_aaa": {
                "servers": "string",
                "ipAddress": "string",
                "network": "string",
                "protocol": "string",
                "sharedSecret": "string",
            },
            "clientAndEndpoint_aaa": {
                "servers": "string",
                "ipAddress": "string",
                "network": "string",
                "protocol": "string",
                "sharedSecret": "string",
            },
        },
        site_id="string",
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_network_v1(api, validator):
    try:
        assert is_valid_create_network_v1(validator, create_network_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_network_v1_default_val(api):
    endpoint_result = api.network_settings.create_network_v1(
        active_validation=True, payload=None, settings=None, site_id="string"
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_network_v1_default_val(api, validator):
    try:
        assert is_valid_create_network_v1(validator, create_network_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_v1(json_schema_validate, obj):
    json_schema_validate("jsd_e1b8c435195d56368c24a54dcce007d0_v2_3_7_6").validate(obj)
    return True


def update_network_v1(api):
    endpoint_result = api.network_settings.update_network_v1(
        active_validation=True,
        payload=None,
        settings={
            "dhcpServer": ["string"],
            "dnsServer": {
                "domainName": "string",
                "primaryIpAddress": "string",
                "secondaryIpAddress": "string",
            },
            "syslogServer": {"ipAddresses": ["string"], "configureDnacIP": True},
            "snmpServer": {"ipAddresses": ["string"], "configureDnacIP": True},
            "netflowcollector": {"ipAddress": "string", "port": 0},
            "ntpServer": ["string"],
            "timezone": "string",
            "messageOfTheday": {
                "bannerMessage": "string",
                "retainExistingBanner": "string",
            },
            "network_aaa": {
                "servers": "string",
                "ipAddress": "string",
                "network": "string",
                "protocol": "string",
                "sharedSecret": "string",
            },
            "clientAndEndpoint_aaa": {
                "servers": "string",
                "ipAddress": "string",
                "network": "string",
                "protocol": "string",
                "sharedSecret": "string",
            },
        },
        site_id="string",
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_network_v1(api, validator):
    try:
        assert is_valid_update_network_v1(validator, update_network_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_v1_default_val(api):
    endpoint_result = api.network_settings.update_network_v1(
        active_validation=True, payload=None, settings=None, site_id="string"
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_network_v1_default_val(api, validator):
    try:
        assert is_valid_update_network_v1(validator, update_network_v1_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_reserve_ip_subpool_v1(json_schema_validate, obj):
    json_schema_validate("jsd_274851d84253559e9d3e81881a4bd2fc_v2_3_7_6").validate(obj)
    return True


def get_reserve_ip_subpool_v1(api):
    endpoint_result = api.network_settings.get_reserve_ip_subpool_v1(
        group_name="string",
        ignore_inherited_groups="string",
        limit=0,
        offset=0,
        pool_usage="string",
        site_id="string",
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_reserve_ip_subpool_v1(api, validator):
    try:
        assert is_valid_get_reserve_ip_subpool_v1(
            validator, get_reserve_ip_subpool_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_reserve_ip_subpool_v1_default_val(api):
    endpoint_result = api.network_settings.get_reserve_ip_subpool_v1(
        group_name=None,
        ignore_inherited_groups=None,
        limit=None,
        offset=None,
        pool_usage=None,
        site_id=None,
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_reserve_ip_subpool_v1_default_val(api, validator):
    try:
        assert is_valid_get_reserve_ip_subpool_v1(
            validator, get_reserve_ip_subpool_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_release_reserve_ip_subpool_v1(json_schema_validate, obj):
    json_schema_validate("jsd_eabbb425255a57578e9db00cda1f303a_v2_3_7_6").validate(obj)
    return True


def release_reserve_ip_subpool_v1(api):
    endpoint_result = api.network_settings.release_reserve_ip_subpool_v1(id="string")
    return endpoint_result


@pytest.mark.network_settings
def test_release_reserve_ip_subpool_v1(api, validator):
    try:
        assert is_valid_release_reserve_ip_subpool_v1(
            validator, release_reserve_ip_subpool_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def release_reserve_ip_subpool_v1_default_val(api):
    endpoint_result = api.network_settings.release_reserve_ip_subpool_v1(id="string")
    return endpoint_result


@pytest.mark.network_settings
def test_release_reserve_ip_subpool_v1_default_val(api, validator):
    try:
        assert is_valid_release_reserve_ip_subpool_v1(
            validator, release_reserve_ip_subpool_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reserve_ip_subpool_v1(json_schema_validate, obj):
    json_schema_validate("jsd_700808cec6c85d9bb4bcc8f61f31296b_v2_3_7_6").validate(obj)
    return True


def reserve_ip_subpool_v1(api):
    endpoint_result = api.network_settings.reserve_ip_subpool_v1(
        active_validation=True,
        ipv4DhcpServers=["string"],
        ipv4DnsServers=["string"],
        ipv4GateWay="string",
        ipv4GlobalPool="string",
        ipv4Prefix=True,
        ipv4PrefixLength=0,
        ipv4Subnet="string",
        ipv4TotalHost=0,
        ipv6AddressSpace=True,
        ipv6DhcpServers=["string"],
        ipv6DnsServers=["string"],
        ipv6GateWay="string",
        ipv6GlobalPool="string",
        ipv6Prefix=True,
        ipv6PrefixLength=0,
        ipv6Subnet="string",
        ipv6TotalHost=0,
        name="string",
        payload=None,
        site_id="string",
        slaacSupport=True,
        type="string",
    )
    return endpoint_result


@pytest.mark.network_settings
def test_reserve_ip_subpool_v1(api, validator):
    try:
        assert is_valid_reserve_ip_subpool_v1(validator, reserve_ip_subpool_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def reserve_ip_subpool_v1_default_val(api):
    endpoint_result = api.network_settings.reserve_ip_subpool_v1(
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
        site_id="string",
        slaacSupport=None,
        type=None,
    )
    return endpoint_result


@pytest.mark.network_settings
def test_reserve_ip_subpool_v1_default_val(api, validator):
    try:
        assert is_valid_reserve_ip_subpool_v1(
            validator, reserve_ip_subpool_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_reserve_ip_subpool_v1(json_schema_validate, obj):
    json_schema_validate("jsd_07fd6083b0c65d03b2d53f10b3ece59d_v2_3_7_6").validate(obj)
    return True


def update_reserve_ip_subpool_v1(api):
    endpoint_result = api.network_settings.update_reserve_ip_subpool_v1(
        active_validation=True,
        id="string",
        ipv4DhcpServers=["string"],
        ipv4DnsServers=["string"],
        ipv4GateWay="string",
        ipv6AddressSpace=True,
        ipv6DhcpServers=["string"],
        ipv6DnsServers=["string"],
        ipv6GateWay="string",
        ipv6GlobalPool="string",
        ipv6Prefix=True,
        ipv6PrefixLength=0,
        ipv6Subnet="string",
        ipv6TotalHost=0,
        name="string",
        payload=None,
        site_id="string",
        slaacSupport=True,
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_reserve_ip_subpool_v1(api, validator):
    try:
        assert is_valid_update_reserve_ip_subpool_v1(
            validator, update_reserve_ip_subpool_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_reserve_ip_subpool_v1_default_val(api):
    endpoint_result = api.network_settings.update_reserve_ip_subpool_v1(
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
        site_id="string",
        slaacSupport=None,
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_reserve_ip_subpool_v1_default_val(api, validator):
    try:
        assert is_valid_update_reserve_ip_subpool_v1(
            validator, update_reserve_ip_subpool_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_service_provider_details_v1(json_schema_validate, obj):
    json_schema_validate("jsd_69dda850a0675b888048adf8d488aec1_v2_3_7_6").validate(obj)
    return True


def get_service_provider_details_v1(api):
    endpoint_result = api.network_settings.get_service_provider_details_v1()
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details_v1(api, validator):
    try:
        assert is_valid_get_service_provider_details_v1(
            validator, get_service_provider_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_service_provider_details_v1_default_val(api):
    endpoint_result = api.network_settings.get_service_provider_details_v1()
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_service_provider_details_v1(
            validator, get_service_provider_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sp_profile_v1(json_schema_validate, obj):
    json_schema_validate("jsd_1ffa347eb411567a9c793696795250a5_v2_3_7_6").validate(obj)
    return True


def create_sp_profile_v1(api):
    endpoint_result = api.network_settings.create_sp_profile_v1(
        active_validation=True,
        payload=None,
        settings={
            "qos": [
                {"profileName": "string", "model": "string", "wanProvider": "string"}
            ]
        },
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_sp_profile_v1(api, validator):
    try:
        assert is_valid_create_sp_profile_v1(validator, create_sp_profile_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_sp_profile_v1_default_val(api):
    endpoint_result = api.network_settings.create_sp_profile_v1(
        active_validation=True, payload=None, settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_sp_profile_v1_default_val(api, validator):
    try:
        assert is_valid_create_sp_profile_v1(
            validator, create_sp_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_sp_profile_v1(json_schema_validate, obj):
    json_schema_validate("jsd_03e22c99a82f5764828810acb45e7a9e_v2_3_7_6").validate(obj)
    return True


def update_sp_profile_v1(api):
    endpoint_result = api.network_settings.update_sp_profile_v1(
        active_validation=True,
        payload=None,
        settings={
            "qos": [
                {
                    "profileName": "string",
                    "model": "string",
                    "wanProvider": "string",
                    "oldProfileName": "string",
                }
            ]
        },
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_sp_profile_v1(api, validator):
    try:
        assert is_valid_update_sp_profile_v1(validator, update_sp_profile_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_sp_profile_v1_default_val(api):
    endpoint_result = api.network_settings.update_sp_profile_v1(
        active_validation=True, payload=None, settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_sp_profile_v1_default_val(api, validator):
    try:
        assert is_valid_update_sp_profile_v1(
            validator, update_sp_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sync_network_devices_credential_v1(json_schema_validate, obj):
    json_schema_validate("jsd_79e73b352ff2573aab906c2ad75c5a71_v2_3_7_6").validate(obj)
    return True


def sync_network_devices_credential_v1(api):
    endpoint_result = api.network_settings.sync_network_devices_credential_v1(
        active_validation=True,
        deviceCredentialId="string",
        payload=None,
        siteId="string",
    )
    return endpoint_result


@pytest.mark.network_settings
def test_sync_network_devices_credential_v1(api, validator):
    try:
        assert is_valid_sync_network_devices_credential_v1(
            validator, sync_network_devices_credential_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def sync_network_devices_credential_v1_default_val(api):
    endpoint_result = api.network_settings.sync_network_devices_credential_v1(
        active_validation=True, deviceCredentialId=None, payload=None, siteId=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_sync_network_devices_credential_v1_default_val(api, validator):
    try:
        assert is_valid_sync_network_devices_credential_v1(
            validator, sync_network_devices_credential_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_aaa_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_953292cd2e825a78b6de087e991f6fe0_v2_3_7_6").validate(obj)
    return True


def set_aaa_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.set_aaa_settings_for_a_site_v1(
        aaaClient={
            "serverType": "string",
            "protocol": "string",
            "pan": "string",
            "primaryServerIp": "string",
            "secondaryServerIp": "string",
            "sharedSecret": "string",
        },
        aaaNetwork={
            "serverType": "string",
            "protocol": "string",
            "pan": "string",
            "primaryServerIp": "string",
            "secondaryServerIp": "string",
            "sharedSecret": "string",
        },
        active_validation=True,
        id="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_aaa_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_set_aaa_settings_for_a_site_v1(
            validator, set_aaa_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_aaa_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.set_aaa_settings_for_a_site_v1(
        aaaClient=None,
        aaaNetwork=None,
        active_validation=True,
        id="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_aaa_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_set_aaa_settings_for_a_site_v1(
            validator, set_aaa_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_aaa_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_4c13899171d45b4f828423c6feaa1e46_v2_3_7_6").validate(obj)
    return True


def retrieve_aaa_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.retrieve_aaa_settings_for_a_site_v1(
        id="string", inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_aaa_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_retrieve_aaa_settings_for_a_site_v1(
            validator, retrieve_aaa_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_aaa_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.retrieve_aaa_settings_for_a_site_v1(
        id="string", inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_aaa_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_aaa_settings_for_a_site_v1(
            validator, retrieve_aaa_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_banner_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_9b29d90ce0125ad898bc06bbceb07403_v2_3_7_6").validate(obj)
    return True


def retrieve_banner_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.retrieve_banner_settings_for_a_site_v1(
        id="string", inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_banner_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_retrieve_banner_settings_for_a_site_v1(
            validator, retrieve_banner_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_banner_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.retrieve_banner_settings_for_a_site_v1(
        id="string", inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_banner_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_banner_settings_for_a_site_v1(
            validator, retrieve_banner_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_banner_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_b3c4383ecc13514c85c6f3d8484f6d68_v2_3_7_6").validate(obj)
    return True


def set_banner_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.set_banner_settings_for_a_site_v1(
        active_validation=True,
        banner={"type": "string", "message": "string"},
        id="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_banner_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_set_banner_settings_for_a_site_v1(
            validator, set_banner_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_banner_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.set_banner_settings_for_a_site_v1(
        active_validation=True, banner=None, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_banner_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_set_banner_settings_for_a_site_v1(
            validator, set_banner_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_credential_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_e4e92f7adc845290b11168e59ab4c88b_v2_3_7_6").validate(obj)
    return True


def get_device_credential_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.get_device_credential_settings_for_a_site_v1(
        id="string", inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_get_device_credential_settings_for_a_site_v1(
            validator, get_device_credential_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_credential_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.get_device_credential_settings_for_a_site_v1(
        id="string", inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_credential_settings_for_a_site_v1(
            validator, get_device_credential_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_credential_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_8e481654675355408be8daff9a82f9a0_v2_3_7_6").validate(obj)
    return True


def update_device_credential_settings_for_a_site_v1(api):
    endpoint_result = (
        api.network_settings.update_device_credential_settings_for_a_site_v1(
            active_validation=True,
            cliCredentialsId={"credentialsId": "string"},
            httpReadCredentialsId={"credentialsId": "string"},
            httpWriteCredentialsId={"credentialsId": "string"},
            id="string",
            payload=None,
            snmpv2cReadCredentialsId={"credentialsId": "string"},
            snmpv2cWriteCredentialsId={"credentialsId": "string"},
            snmpv3CredentialsId={"credentialsId": "string"},
        )
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_device_credential_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_update_device_credential_settings_for_a_site_v1(
            validator, update_device_credential_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_credential_settings_for_a_site_v1_default_val(api):
    endpoint_result = (
        api.network_settings.update_device_credential_settings_for_a_site_v1(
            active_validation=True,
            cliCredentialsId=None,
            httpReadCredentialsId=None,
            httpWriteCredentialsId=None,
            id="string",
            payload=None,
            snmpv2cReadCredentialsId=None,
            snmpv2cWriteCredentialsId=None,
            snmpv3CredentialsId=None,
        )
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_device_credential_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_update_device_credential_settings_for_a_site_v1(
            validator, update_device_credential_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_devices_credentials_sync_status_v1(json_schema_validate, obj):
    json_schema_validate("jsd_be59a332e9e45f6991e96111743fd775_v2_3_7_6").validate(obj)
    return True


def get_network_devices_credentials_sync_status_v1(api):
    endpoint_result = (
        api.network_settings.get_network_devices_credentials_sync_status_v1(id="string")
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_devices_credentials_sync_status_v1(api, validator):
    try:
        assert is_valid_get_network_devices_credentials_sync_status_v1(
            validator, get_network_devices_credentials_sync_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_devices_credentials_sync_status_v1_default_val(api):
    endpoint_result = (
        api.network_settings.get_network_devices_credentials_sync_status_v1(id="string")
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_devices_credentials_sync_status_v1_default_val(api, validator):
    try:
        assert is_valid_get_network_devices_credentials_sync_status_v1(
            validator, get_network_devices_credentials_sync_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_dhcp_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_2a15a2f83f975a6a9964e7da79a605de_v2_3_7_6").validate(obj)
    return True


def set_dhcp_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.set_dhcp_settings_for_a_site_v1(
        active_validation=True, dhcp={"servers": ["string"]}, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_dhcp_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_set_dhcp_settings_for_a_site_v1(
            validator, set_dhcp_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_dhcp_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.set_dhcp_settings_for_a_site_v1(
        active_validation=True, dhcp=None, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_dhcp_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_set_dhcp_settings_for_a_site_v1(
            validator, set_dhcp_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_d_h_c_p_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_5fe723d00fce5700b8abe2a43b82f035_v2_3_7_6").validate(obj)
    return True


def retrieve_d_h_c_p_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.retrieve_d_h_c_p_settings_for_a_site_v1(
        id="string", inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_d_h_c_p_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_retrieve_d_h_c_p_settings_for_a_site_v1(
            validator, retrieve_d_h_c_p_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_d_h_c_p_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.retrieve_d_h_c_p_settings_for_a_site_v1(
        id="string", inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_d_h_c_p_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_d_h_c_p_settings_for_a_site_v1(
            validator, retrieve_d_h_c_p_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_d_n_s_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_0f32e172f454564ba92d7a410c63c164_v2_3_7_6").validate(obj)
    return True


def retrieve_d_n_s_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.retrieve_d_n_s_settings_for_a_site_v1(
        id="string", inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_d_n_s_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_retrieve_d_n_s_settings_for_a_site_v1(
            validator, retrieve_d_n_s_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_d_n_s_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.retrieve_d_n_s_settings_for_a_site_v1(
        id="string", inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_d_n_s_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_d_n_s_settings_for_a_site_v1(
            validator, retrieve_d_n_s_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_d_n_s_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_6eb3b18894545315b25b94d0c0e2ec67_v2_3_7_6").validate(obj)
    return True


def set_d_n_s_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.set_d_n_s_settings_for_a_site_v1(
        active_validation=True,
        dns={"domainName": "string", "dnsServers": ["string"]},
        id="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_d_n_s_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_set_d_n_s_settings_for_a_site_v1(
            validator, set_d_n_s_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_d_n_s_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.set_d_n_s_settings_for_a_site_v1(
        active_validation=True, dns=None, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_d_n_s_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_set_d_n_s_settings_for_a_site_v1(
            validator, set_d_n_s_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_image_distribution_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_d02614492a2251c18de2e36c097e40ff_v2_3_7_6").validate(obj)
    return True


def set_image_distribution_settings_for_a_site_v1(api):
    endpoint_result = (
        api.network_settings.set_image_distribution_settings_for_a_site_v1(
            active_validation=True,
            id="string",
            imageDistribution={"servers": ["string"]},
            payload=None,
        )
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_image_distribution_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_set_image_distribution_settings_for_a_site_v1(
            validator, set_image_distribution_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_image_distribution_settings_for_a_site_v1_default_val(api):
    endpoint_result = (
        api.network_settings.set_image_distribution_settings_for_a_site_v1(
            active_validation=True, id="string", imageDistribution=None, payload=None
        )
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_image_distribution_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_set_image_distribution_settings_for_a_site_v1(
            validator, set_image_distribution_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_image_distribution_settings_for_a_site_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_d0c5259b59bd5751994e2aa77a15f70e_v2_3_7_6").validate(obj)
    return True


def retrieve_image_distribution_settings_for_a_site_v1(api):
    endpoint_result = (
        api.network_settings.retrieve_image_distribution_settings_for_a_site_v1(
            id="string", inherited=True
        )
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_image_distribution_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_retrieve_image_distribution_settings_for_a_site_v1(
            validator, retrieve_image_distribution_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_image_distribution_settings_for_a_site_v1_default_val(api):
    endpoint_result = (
        api.network_settings.retrieve_image_distribution_settings_for_a_site_v1(
            id="string", inherited=None
        )
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_image_distribution_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_image_distribution_settings_for_a_site_v1(
            validator,
            retrieve_image_distribution_settings_for_a_site_v1_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_n_t_p_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_df9ec5aa58815a849b4853b223343e5e_v2_3_7_6").validate(obj)
    return True


def set_n_t_p_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.set_n_t_p_settings_for_a_site_v1(
        active_validation=True, id="string", ntp={"servers": ["string"]}, payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_n_t_p_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_set_n_t_p_settings_for_a_site_v1(
            validator, set_n_t_p_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_n_t_p_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.set_n_t_p_settings_for_a_site_v1(
        active_validation=True, id="string", ntp=None, payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_n_t_p_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_set_n_t_p_settings_for_a_site_v1(
            validator, set_n_t_p_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_n_t_p_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_c49b666d3a305b509d0d3b356e912ab4_v2_3_7_6").validate(obj)
    return True


def retrieve_n_t_p_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.retrieve_n_t_p_settings_for_a_site_v1(
        id="string", inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_n_t_p_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_retrieve_n_t_p_settings_for_a_site_v1(
            validator, retrieve_n_t_p_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_n_t_p_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.retrieve_n_t_p_settings_for_a_site_v1(
        id="string", inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_n_t_p_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_n_t_p_settings_for_a_site_v1(
            validator, retrieve_n_t_p_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_telemetry_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_af4b3c5d1dc6505cadd13bf41c894700_v2_3_7_6").validate(obj)
    return True


def retrieve_telemetry_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.retrieve_telemetry_settings_for_a_site_v1(
        id="string", inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_telemetry_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_retrieve_telemetry_settings_for_a_site_v1(
            validator, retrieve_telemetry_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_telemetry_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.retrieve_telemetry_settings_for_a_site_v1(
        id="string", inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_telemetry_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_telemetry_settings_for_a_site_v1(
            validator, retrieve_telemetry_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_telemetry_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_bac0c488707959c182dfef18681bceda_v2_3_7_6").validate(obj)
    return True


def set_telemetry_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.set_telemetry_settings_for_a_site_v1(
        active_validation=True,
        applicationVisibility={
            "collector": {"collectorType": "string", "address": "string", "port": 0},
            "enableOnWiredAccessDevices": True,
        },
        id="string",
        payload=None,
        snmpTraps={"useBuiltinTrapServer": True, "externalTrapServers": ["string"]},
        syslogs={"useBuiltinSyslogServer": True, "externalSyslogServers": ["string"]},
        wiredDataCollection={"enableWiredDataCollectio": True},
        wirelessTelemetry={"enableWirelessTelemetry": True},
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_telemetry_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_set_telemetry_settings_for_a_site_v1(
            validator, set_telemetry_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_telemetry_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.set_telemetry_settings_for_a_site_v1(
        active_validation=True,
        applicationVisibility=None,
        id="string",
        payload=None,
        snmpTraps=None,
        syslogs=None,
        wiredDataCollection=None,
        wirelessTelemetry=None,
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_telemetry_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_set_telemetry_settings_for_a_site_v1(
            validator, set_telemetry_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_time_zone_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_c17432d928f755f8bb9f4edb83089d3e_v2_3_7_6").validate(obj)
    return True


def set_time_zone_for_a_site_v1(api):
    endpoint_result = api.network_settings.set_time_zone_for_a_site_v1(
        active_validation=True,
        id="string",
        payload=None,
        timeZone={"identifier": "string"},
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_time_zone_for_a_site_v1(api, validator):
    try:
        assert is_valid_set_time_zone_for_a_site_v1(
            validator, set_time_zone_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_time_zone_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.set_time_zone_for_a_site_v1(
        active_validation=True, id="string", payload=None, timeZone=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_time_zone_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_set_time_zone_for_a_site_v1(
            validator, set_time_zone_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_time_zone_settings_for_a_site_v1(json_schema_validate, obj):
    json_schema_validate("jsd_10a03efc6bba51eeabcde938f0856074_v2_3_7_6").validate(obj)
    return True


def retrieve_time_zone_settings_for_a_site_v1(api):
    endpoint_result = api.network_settings.retrieve_time_zone_settings_for_a_site_v1(
        id="string", inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_time_zone_settings_for_a_site_v1(api, validator):
    try:
        assert is_valid_retrieve_time_zone_settings_for_a_site_v1(
            validator, retrieve_time_zone_settings_for_a_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_time_zone_settings_for_a_site_v1_default_val(api):
    endpoint_result = api.network_settings.retrieve_time_zone_settings_for_a_site_v1(
        id="string", inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_time_zone_settings_for_a_site_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_time_zone_settings_for_a_site_v1(
            validator, retrieve_time_zone_settings_for_a_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sp_profile_v1(json_schema_validate, obj):
    json_schema_validate("jsd_35598a1d68f15e02adc37239b3fcbbb6_v2_3_7_6").validate(obj)
    return True


def delete_sp_profile_v1(api):
    endpoint_result = api.network_settings.delete_sp_profile_v1(
        sp_profile_name="string"
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile_v1(api, validator):
    try:
        assert is_valid_delete_sp_profile_v1(validator, delete_sp_profile_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_sp_profile_v1_default_val(api):
    endpoint_result = api.network_settings.delete_sp_profile_v1(
        sp_profile_name="string"
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile_v1_default_val(api, validator):
    try:
        assert is_valid_delete_sp_profile_v1(
            validator, delete_sp_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_54266de1b75d59b083df0ece12259ecd_v2_3_7_6").validate(obj)
    return True


def update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1(
    api,
):
    endpoint_result = api.network_settings.update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1(
        active_validation=True, deviceIds=["string"], payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1(
    api, validator
):
    try:
        assert is_valid_update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1(
            validator,
            update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1_default_val(
    api,
):
    endpoint_result = api.network_settings.update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1(
        active_validation=True, deviceIds=None, payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1_default_val(
    api, validator
):
    try:
        assert is_valid_update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1(
            validator,
            update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_device_credential_to_site_v2(json_schema_validate, obj):
    json_schema_validate("jsd_156a3954b27e5eeb82789ed231e0557f_v2_3_7_6").validate(obj)
    return True


def assign_device_credential_to_site_v2(api):
    endpoint_result = api.network_settings.assign_device_credential_to_site_v2(
        active_validation=True,
        cliId="string",
        httpRead="string",
        httpWrite="string",
        payload=None,
        site_id="string",
        snmpV2ReadId="string",
        snmpV2WriteId="string",
        snmpV3Id="string",
    )
    return endpoint_result


@pytest.mark.network_settings
def test_assign_device_credential_to_site_v2(api, validator):
    try:
        assert is_valid_assign_device_credential_to_site_v2(
            validator, assign_device_credential_to_site_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_device_credential_to_site_v2_default_val(api):
    endpoint_result = api.network_settings.assign_device_credential_to_site_v2(
        active_validation=True,
        cliId=None,
        httpRead=None,
        httpWrite=None,
        payload=None,
        site_id="string",
        snmpV2ReadId=None,
        snmpV2WriteId=None,
        snmpV3Id=None,
    )
    return endpoint_result


@pytest.mark.network_settings
def test_assign_device_credential_to_site_v2_default_val(api, validator):
    try:
        assert is_valid_assign_device_credential_to_site_v2(
            validator, assign_device_credential_to_site_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_v2(json_schema_validate, obj):
    json_schema_validate("jsd_d0b7bffe821755dab4e2a2df8ea79404_v2_3_7_6").validate(obj)
    return True


def get_network_v2(api):
    endpoint_result = api.network_settings.get_network_v2(site_id="string")
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_v2(api, validator):
    try:
        assert is_valid_get_network_v2(validator, get_network_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_v2_default_val(api):
    endpoint_result = api.network_settings.get_network_v2(site_id=None)
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_v2_default_val(api, validator):
    try:
        assert is_valid_get_network_v2(validator, get_network_v2_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_v2(json_schema_validate, obj):
    json_schema_validate("jsd_c5f97865727857d5b1eeaedee3dcccd2_v2_3_7_6").validate(obj)
    return True


def create_network_v2(api):
    endpoint_result = api.network_settings.create_network_v2(
        active_validation=True,
        payload=None,
        settings={
            "dhcpServer": ["string"],
            "dnsServer": {
                "domainName": "string",
                "primaryIpAddress": "string",
                "secondaryIpAddress": "string",
            },
            "syslogServer": {"ipAddresses": ["string"], "configureDnacIP": True},
            "snmpServer": {"ipAddresses": ["string"], "configureDnacIP": True},
            "netflowcollector": {"ipAddress": "string", "port": 0},
            "ntpServer": ["string"],
            "timezone": "string",
            "messageOfTheday": {
                "bannerMessage": "string",
                "retainExistingBanner": "string",
            },
            "network_aaa": {
                "servers": "string",
                "ipAddress": "string",
                "network": "string",
                "protocol": "string",
                "sharedSecret": "string",
            },
            "clientAndEndpoint_aaa": {
                "servers": "string",
                "ipAddress": "string",
                "network": "string",
                "protocol": "string",
                "sharedSecret": "string",
            },
        },
        site_id="string",
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_network_v2(api, validator):
    try:
        assert is_valid_create_network_v2(validator, create_network_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_network_v2_default_val(api):
    endpoint_result = api.network_settings.create_network_v2(
        active_validation=True, payload=None, settings=None, site_id="string"
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_network_v2_default_val(api, validator):
    try:
        assert is_valid_create_network_v2(validator, create_network_v2_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_v2(json_schema_validate, obj):
    json_schema_validate("jsd_a7935eedd53a5b8c84668c903cc1c705_v2_3_7_6").validate(obj)
    return True


def update_network_v2(api):
    endpoint_result = api.network_settings.update_network_v2(
        active_validation=True,
        payload=None,
        settings={
            "dhcpServer": ["string"],
            "dnsServer": {
                "domainName": "string",
                "primaryIpAddress": "string",
                "secondaryIpAddress": "string",
            },
            "syslogServer": {"ipAddresses": ["string"], "configureDnacIP": True},
            "snmpServer": {"ipAddresses": ["string"], "configureDnacIP": True},
            "netflowcollector": {"ipAddress": "string", "port": 0},
            "ntpServer": ["string"],
            "timezone": "string",
            "messageOfTheday": {
                "bannerMessage": "string",
                "retainExistingBanner": "string",
            },
            "network_aaa": {
                "servers": "string",
                "ipAddress": "string",
                "network": "string",
                "protocol": "string",
                "sharedSecret": "string",
            },
            "clientAndEndpoint_aaa": {
                "servers": "string",
                "ipAddress": "string",
                "network": "string",
                "protocol": "string",
                "sharedSecret": "string",
            },
        },
        site_id="string",
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_network_v2(api, validator):
    try:
        assert is_valid_update_network_v2(validator, update_network_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_v2_default_val(api):
    endpoint_result = api.network_settings.update_network_v2(
        active_validation=True, payload=None, settings=None, site_id="string"
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_network_v2_default_val(api, validator):
    try:
        assert is_valid_update_network_v2(validator, update_network_v2_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sp_profile_v2(json_schema_validate, obj):
    json_schema_validate("jsd_a66db26df529597c84c2a15ea2d632ce_v2_3_7_6").validate(obj)
    return True


def create_sp_profile_v2(api):
    endpoint_result = api.network_settings.create_sp_profile_v2(
        active_validation=True,
        payload=None,
        settings={
            "qos": [
                {"profileName": "string", "model": "string", "wanProvider": "string"}
            ]
        },
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_sp_profile_v2(api, validator):
    try:
        assert is_valid_create_sp_profile_v2(validator, create_sp_profile_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_sp_profile_v2_default_val(api):
    endpoint_result = api.network_settings.create_sp_profile_v2(
        active_validation=True, payload=None, settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_sp_profile_v2_default_val(api, validator):
    try:
        assert is_valid_create_sp_profile_v2(
            validator, create_sp_profile_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_sp_profile_v2(json_schema_validate, obj):
    json_schema_validate("jsd_53680237e0b654c39dc6e19cd6f5194d_v2_3_7_6").validate(obj)
    return True


def update_sp_profile_v2(api):
    endpoint_result = api.network_settings.update_sp_profile_v2(
        active_validation=True,
        payload=None,
        settings={
            "qos": [
                {
                    "profileName": "string",
                    "model": "string",
                    "wanProvider": "string",
                    "oldProfileName": "string",
                }
            ]
        },
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_sp_profile_v2(api, validator):
    try:
        assert is_valid_update_sp_profile_v2(validator, update_sp_profile_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_sp_profile_v2_default_val(api):
    endpoint_result = api.network_settings.update_sp_profile_v2(
        active_validation=True, payload=None, settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_sp_profile_v2_default_val(api, validator):
    try:
        assert is_valid_update_sp_profile_v2(
            validator, update_sp_profile_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_service_provider_details_v2(json_schema_validate, obj):
    json_schema_validate("jsd_3907f01025635a52bdfdac7226911b31_v2_3_7_6").validate(obj)
    return True


def get_service_provider_details_v2(api):
    endpoint_result = api.network_settings.get_service_provider_details_v2()
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details_v2(api, validator):
    try:
        assert is_valid_get_service_provider_details_v2(
            validator, get_service_provider_details_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_service_provider_details_v2_default_val(api):
    endpoint_result = api.network_settings.get_service_provider_details_v2()
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details_v2_default_val(api, validator):
    try:
        assert is_valid_get_service_provider_details_v2(
            validator, get_service_provider_details_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sp_profile_v2(json_schema_validate, obj):
    json_schema_validate("jsd_a9bbbce953615baeb0a324c61753139d_v2_3_7_6").validate(obj)
    return True


def delete_sp_profile_v2(api):
    endpoint_result = api.network_settings.delete_sp_profile_v2(
        sp_profile_name="string"
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile_v2(api, validator):
    try:
        assert is_valid_delete_sp_profile_v2(validator, delete_sp_profile_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_sp_profile_v2_default_val(api):
    endpoint_result = api.network_settings.delete_sp_profile_v2(
        sp_profile_name="string"
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile_v2_default_val(api, validator):
    try:
        assert is_valid_delete_sp_profile_v2(
            validator, delete_sp_profile_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

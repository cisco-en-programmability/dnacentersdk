# -*- coding: utf-8 -*-
"""CatalystCenterAPI network_settings API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.9', reason='version does not match')


def is_valid_assign_device_credential_to_site(json_schema_validate, obj):
    json_schema_validate('jsd_4e4f91ea42515ccdbc24549b84ca1e90_v2_3_7_9').validate(obj)
    return True


def assign_device_credential_to_site(api):
    endpoint_result = api.network_settings.assign_device_credential_to_site(
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
def test_assign_device_credential_to_site(api, validator):
    try:
        assert is_valid_assign_device_credential_to_site(
            validator,
            assign_device_credential_to_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_device_credential_to_site_default_val(api):
    endpoint_result = api.network_settings.assign_device_credential_to_site(
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
def test_assign_device_credential_to_site_default_val(api, validator):
    try:
        assert is_valid_assign_device_credential_to_site(
            validator,
            assign_device_credential_to_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_device_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_903cf2cac6f150c9bee9ade37921b162_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_722d7161b33157dba957ba18eda440c2_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_403067d8cf995d9d99bdc31707817456_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_598e8e021f1c51eeaf0d102084481486_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_ebdcd84fc41754a69eaeacf7c0b0731c_v2_3_7_9').validate(obj)
    return True


def get_global_pool(api):
    endpoint_result = api.network_settings.get_global_pool(
        limit=0,
        offset=0
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
    json_schema_validate('jsd_5c380301e3e05423bdc1857ff00ae77a_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_eecf4323cb285985be72a7e061891059_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_61f9079863c95acd945c51f728cbf81f_v2_3_7_9').validate(obj)
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


def is_valid_create_a_global_ip_address_pool(json_schema_validate, obj):
    json_schema_validate('jsd_21d833c51c4f5cd2879d3e69f773295c_v2_3_7_9').validate(obj)
    return True


def create_a_global_ip_address_pool(api):
    endpoint_result = api.network_settings.create_a_global_ip_address_pool(
        active_validation=True,
        addressSpace={'subnet': 'string', 'prefixLength': 0, 'gatewayIpAddress': 'string', 'dhcpServers': ['string'], 'dnsServers': ['string']},
        name='string',
        payload=None,
        poolType='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_a_global_ip_address_pool(api, validator):
    try:
        assert is_valid_create_a_global_ip_address_pool(
            validator,
            create_a_global_ip_address_pool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_a_global_ip_address_pool_default_val(api):
    endpoint_result = api.network_settings.create_a_global_ip_address_pool(
        active_validation=True,
        addressSpace=None,
        name=None,
        payload=None,
        poolType=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_a_global_ip_address_pool_default_val(api, validator):
    try:
        assert is_valid_create_a_global_ip_address_pool(
            validator,
            create_a_global_ip_address_pool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_global_ip_address_pools(json_schema_validate, obj):
    json_schema_validate('jsd_4615c6b166895678be157ab0d389c0c6_v2_3_7_9').validate(obj)
    return True


def retrieves_global_ip_address_pools(api):
    endpoint_result = api.network_settings.retrieves_global_ip_address_pools(
        limit=0,
        offset=0,
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieves_global_ip_address_pools(api, validator):
    try:
        assert is_valid_retrieves_global_ip_address_pools(
            validator,
            retrieves_global_ip_address_pools(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_global_ip_address_pools_default_val(api):
    endpoint_result = api.network_settings.retrieves_global_ip_address_pools(
        limit=None,
        offset=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieves_global_ip_address_pools_default_val(api, validator):
    try:
        assert is_valid_retrieves_global_ip_address_pools(
            validator,
            retrieves_global_ip_address_pools_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_counts_global_ip_address_pools(json_schema_validate, obj):
    json_schema_validate('jsd_6ab655674f4156dc92f7ba1ed3a0de68_v2_3_7_9').validate(obj)
    return True


def counts_global_ip_address_pools(api):
    endpoint_result = api.network_settings.counts_global_ip_address_pools(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_counts_global_ip_address_pools(api, validator):
    try:
        assert is_valid_counts_global_ip_address_pools(
            validator,
            counts_global_ip_address_pools(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def counts_global_ip_address_pools_default_val(api):
    endpoint_result = api.network_settings.counts_global_ip_address_pools(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_counts_global_ip_address_pools_default_val(api, validator):
    try:
        assert is_valid_counts_global_ip_address_pools(
            validator,
            counts_global_ip_address_pools_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_subpools_ids_of_a_global_ip_address_pool(json_schema_validate, obj):
    json_schema_validate('jsd_75e3d5e2a49655fa8fa7a0257a0fcd35_v2_3_7_9').validate(obj)
    return True


def retrieves_subpools_ids_of_a_global_ip_address_pool(api):
    endpoint_result = api.network_settings.retrieves_subpools_ids_of_a_global_ip_address_pool(
        global_ip_address_pool_id='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieves_subpools_ids_of_a_global_ip_address_pool(api, validator):
    try:
        assert is_valid_retrieves_subpools_ids_of_a_global_ip_address_pool(
            validator,
            retrieves_subpools_ids_of_a_global_ip_address_pool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_subpools_ids_of_a_global_ip_address_pool_default_val(api):
    endpoint_result = api.network_settings.retrieves_subpools_ids_of_a_global_ip_address_pool(
        global_ip_address_pool_id='string',
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieves_subpools_ids_of_a_global_ip_address_pool_default_val(api, validator):
    try:
        assert is_valid_retrieves_subpools_ids_of_a_global_ip_address_pool(
            validator,
            retrieves_subpools_ids_of_a_global_ip_address_pool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_counts_subpools_of_a_global_ip_address_pool(json_schema_validate, obj):
    json_schema_validate('jsd_4cdc0978bfef5699abbfabf52ecd5fa8_v2_3_7_9').validate(obj)
    return True


def counts_subpools_of_a_global_ip_address_pool(api):
    endpoint_result = api.network_settings.counts_subpools_of_a_global_ip_address_pool(
        global_ip_address_pool_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_counts_subpools_of_a_global_ip_address_pool(api, validator):
    try:
        assert is_valid_counts_subpools_of_a_global_ip_address_pool(
            validator,
            counts_subpools_of_a_global_ip_address_pool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def counts_subpools_of_a_global_ip_address_pool_default_val(api):
    endpoint_result = api.network_settings.counts_subpools_of_a_global_ip_address_pool(
        global_ip_address_pool_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_counts_subpools_of_a_global_ip_address_pool_default_val(api, validator):
    try:
        assert is_valid_counts_subpools_of_a_global_ip_address_pool(
            validator,
            counts_subpools_of_a_global_ip_address_pool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_a_global_ip_address_pool(json_schema_validate, obj):
    json_schema_validate('jsd_1fe2440acbc059fb866295bb4d4eeb38_v2_3_7_9').validate(obj)
    return True


def retrieves_a_global_ip_address_pool(api):
    endpoint_result = api.network_settings.retrieves_a_global_ip_address_pool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieves_a_global_ip_address_pool(api, validator):
    try:
        assert is_valid_retrieves_a_global_ip_address_pool(
            validator,
            retrieves_a_global_ip_address_pool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_a_global_ip_address_pool_default_val(api):
    endpoint_result = api.network_settings.retrieves_a_global_ip_address_pool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieves_a_global_ip_address_pool_default_val(api, validator):
    try:
        assert is_valid_retrieves_a_global_ip_address_pool(
            validator,
            retrieves_a_global_ip_address_pool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_a_global_ip_address_pool(json_schema_validate, obj):
    json_schema_validate('jsd_4e235d44e4485bafa4499f5a8e53bcd3_v2_3_7_9').validate(obj)
    return True


def updates_a_global_ip_address_pool(api):
    endpoint_result = api.network_settings.updates_a_global_ip_address_pool(
        active_validation=True,
        addressSpace={'subnet': 'string', 'prefixLength': 0, 'gatewayIpAddress': 'string', 'dhcpServers': ['string'], 'dnsServers': ['string']},
        id='string',
        name='string',
        payload=None,
        poolType='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_updates_a_global_ip_address_pool(api, validator):
    try:
        assert is_valid_updates_a_global_ip_address_pool(
            validator,
            updates_a_global_ip_address_pool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_a_global_ip_address_pool_default_val(api):
    endpoint_result = api.network_settings.updates_a_global_ip_address_pool(
        active_validation=True,
        addressSpace=None,
        id='string',
        name=None,
        payload=None,
        poolType=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_updates_a_global_ip_address_pool_default_val(api, validator):
    try:
        assert is_valid_updates_a_global_ip_address_pool(
            validator,
            updates_a_global_ip_address_pool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_global_ip_address_pool(json_schema_validate, obj):
    json_schema_validate('jsd_1ca56aef75ed559f821e14d17e289d7b_v2_3_7_9').validate(obj)
    return True


def delete_a_global_ip_address_pool(api):
    endpoint_result = api.network_settings.delete_a_global_ip_address_pool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_a_global_ip_address_pool(api, validator):
    try:
        assert is_valid_delete_a_global_ip_address_pool(
            validator,
            delete_a_global_ip_address_pool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_global_ip_address_pool_default_val(api):
    endpoint_result = api.network_settings.delete_a_global_ip_address_pool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_a_global_ip_address_pool_default_val(api, validator):
    try:
        assert is_valid_delete_a_global_ip_address_pool(
            validator,
            delete_a_global_ip_address_pool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reservecreate_ip_address_subpools(json_schema_validate, obj):
    json_schema_validate('jsd_31970086c7315d78a2ddda76b62777e8_v2_3_7_9').validate(obj)
    return True


def reservecreate_ip_address_subpools(api):
    endpoint_result = api.network_settings.reservecreate_ip_address_subpools(
        active_validation=True,
        ipV4AddressSpace={'subnet': 'string', 'prefixLength': 0, 'gatewayIpAddress': 'string', 'dhcpServers': ['string'], 'dnsServers': ['string'], 'totalAddresses': 'string', 'unassignableAddresses': 'string', 'assignedAddresses': 'string', 'defaultAssignedAddresses': 'string', 'slaacSupport': True, 'globalPoolId': 'string'},
        ipV6AddressSpace={'subnet': 'string', 'prefixLength': 0, 'gatewayIpAddress': 'string', 'dhcpServers': ['string'], 'dnsServers': ['string'], 'totalAddresses': 'string', 'unassignableAddresses': 'string', 'assignedAddresses': 'string', 'defaultAssignedAddresses': 'string', 'slaacSupport': True, 'globalPoolId': 'string'},
        name='string',
        payload=None,
        poolType='string',
        siteId='string',
        siteName='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_reservecreate_ip_address_subpools(api, validator):
    try:
        assert is_valid_reservecreate_ip_address_subpools(
            validator,
            reservecreate_ip_address_subpools(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def reservecreate_ip_address_subpools_default_val(api):
    endpoint_result = api.network_settings.reservecreate_ip_address_subpools(
        active_validation=True,
        ipV4AddressSpace=None,
        ipV6AddressSpace=None,
        name=None,
        payload=None,
        poolType=None,
        siteId=None,
        siteName=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_reservecreate_ip_address_subpools_default_val(api, validator):
    try:
        assert is_valid_reservecreate_ip_address_subpools(
            validator,
            reservecreate_ip_address_subpools_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_ip_address_subpools(json_schema_validate, obj):
    json_schema_validate('jsd_865ebda74d4458fc9d197089571726d5_v2_3_7_9').validate(obj)
    return True


def retrieves_ip_address_subpools(api):
    endpoint_result = api.network_settings.retrieves_ip_address_subpools(
        limit=0,
        offset=0,
        order='string',
        site_id='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieves_ip_address_subpools(api, validator):
    try:
        assert is_valid_retrieves_ip_address_subpools(
            validator,
            retrieves_ip_address_subpools(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_ip_address_subpools_default_val(api):
    endpoint_result = api.network_settings.retrieves_ip_address_subpools(
        limit=None,
        offset=None,
        order=None,
        site_id=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieves_ip_address_subpools_default_val(api, validator):
    try:
        assert is_valid_retrieves_ip_address_subpools(
            validator,
            retrieves_ip_address_subpools_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_counts_ip_address_subpools(json_schema_validate, obj):
    json_schema_validate('jsd_0e192825119d5baaa2edd636e7c4d12d_v2_3_7_9').validate(obj)
    return True


def counts_ip_address_subpools(api):
    endpoint_result = api.network_settings.counts_ip_address_subpools(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_counts_ip_address_subpools(api, validator):
    try:
        assert is_valid_counts_ip_address_subpools(
            validator,
            counts_ip_address_subpools(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def counts_ip_address_subpools_default_val(api):
    endpoint_result = api.network_settings.counts_ip_address_subpools(
        site_id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_counts_ip_address_subpools_default_val(api, validator):
    try:
        assert is_valid_counts_ip_address_subpools(
            validator,
            counts_ip_address_subpools_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_release_an_ip_address_subpool(json_schema_validate, obj):
    json_schema_validate('jsd_f3a0040b7a89523f8d95ff69fb620047_v2_3_7_9').validate(obj)
    return True


def release_an_ip_address_subpool(api):
    endpoint_result = api.network_settings.release_an_ip_address_subpool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_release_an_ip_address_subpool(api, validator):
    try:
        assert is_valid_release_an_ip_address_subpool(
            validator,
            release_an_ip_address_subpool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def release_an_ip_address_subpool_default_val(api):
    endpoint_result = api.network_settings.release_an_ip_address_subpool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_release_an_ip_address_subpool_default_val(api, validator):
    try:
        assert is_valid_release_an_ip_address_subpool(
            validator,
            release_an_ip_address_subpool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_an_ip_address_subpool(json_schema_validate, obj):
    json_schema_validate('jsd_e328f7d015535897877f3ecb0c927453_v2_3_7_9').validate(obj)
    return True


def updates_an_ip_address_subpool(api):
    endpoint_result = api.network_settings.updates_an_ip_address_subpool(
        active_validation=True,
        id='string',
        ipV4AddressSpace={'subnet': 'string', 'prefixLength': 0, 'gatewayIpAddress': 'string', 'dhcpServers': ['string'], 'dnsServers': ['string'], 'slaacSupport': True, 'globalPoolId': 'string'},
        ipV6AddressSpace={'subnet': 'string', 'prefixLength': 0, 'gatewayIpAddress': 'string', 'dhcpServers': ['string'], 'dnsServers': ['string'], 'slaacSupport': True, 'globalPoolId': 'string'},
        name='string',
        payload=None,
        poolType='string',
        siteId='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_updates_an_ip_address_subpool(api, validator):
    try:
        assert is_valid_updates_an_ip_address_subpool(
            validator,
            updates_an_ip_address_subpool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_an_ip_address_subpool_default_val(api):
    endpoint_result = api.network_settings.updates_an_ip_address_subpool(
        active_validation=True,
        id='string',
        ipV4AddressSpace=None,
        ipV6AddressSpace=None,
        name=None,
        payload=None,
        poolType=None,
        siteId=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_updates_an_ip_address_subpool_default_val(api, validator):
    try:
        assert is_valid_updates_an_ip_address_subpool(
            validator,
            updates_an_ip_address_subpool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_an_ip_address_subpool(json_schema_validate, obj):
    json_schema_validate('jsd_f88725b8419857269dcb0d735af3e828_v2_3_7_9').validate(obj)
    return True


def retrieves_an_ip_address_subpool(api):
    endpoint_result = api.network_settings.retrieves_an_ip_address_subpool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieves_an_ip_address_subpool(api, validator):
    try:
        assert is_valid_retrieves_an_ip_address_subpool(
            validator,
            retrieves_an_ip_address_subpool(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_an_ip_address_subpool_default_val(api):
    endpoint_result = api.network_settings.retrieves_an_ip_address_subpool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieves_an_ip_address_subpool_default_val(api, validator):
    try:
        assert is_valid_retrieves_an_ip_address_subpool(
            validator,
            retrieves_an_ip_address_subpool_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network(json_schema_validate, obj):
    json_schema_validate('jsd_40397b199c175281977a7e9e6bd9255b_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_6eca62ef076b5627a85b2a5959613fb8_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_e1b8c435195d56368c24a54dcce007d0_v2_3_7_9').validate(obj)
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


def is_valid_retrieve_cli_templates_attached_to_a_network_profile(json_schema_validate, obj):
    json_schema_validate('jsd_05d743268b5b5705a00e002a4484b003_v2_3_7_9').validate(obj)
    return True


def retrieve_cli_templates_attached_to_a_network_profile(api):
    endpoint_result = api.network_settings.retrieve_cli_templates_attached_to_a_network_profile(
        profile_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_cli_templates_attached_to_a_network_profile(api, validator):
    try:
        assert is_valid_retrieve_cli_templates_attached_to_a_network_profile(
            validator,
            retrieve_cli_templates_attached_to_a_network_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_cli_templates_attached_to_a_network_profile_default_val(api):
    endpoint_result = api.network_settings.retrieve_cli_templates_attached_to_a_network_profile(
        profile_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_cli_templates_attached_to_a_network_profile_default_val(api, validator):
    try:
        assert is_valid_retrieve_cli_templates_attached_to_a_network_profile(
            validator,
            retrieve_cli_templates_attached_to_a_network_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_count_of_cli_templates_attached_to_a_network_profile(json_schema_validate, obj):
    json_schema_validate('jsd_b8047373040656b29dc1306cad58366b_v2_3_7_9').validate(obj)
    return True


def retrieve_count_of_cli_templates_attached_to_a_network_profile(api):
    endpoint_result = api.network_settings.retrieve_count_of_cli_templates_attached_to_a_network_profile(
        profile_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_count_of_cli_templates_attached_to_a_network_profile(api, validator):
    try:
        assert is_valid_retrieve_count_of_cli_templates_attached_to_a_network_profile(
            validator,
            retrieve_count_of_cli_templates_attached_to_a_network_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_count_of_cli_templates_attached_to_a_network_profile_default_val(api):
    endpoint_result = api.network_settings.retrieve_count_of_cli_templates_attached_to_a_network_profile(
        profile_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_count_of_cli_templates_attached_to_a_network_profile_default_val(api, validator):
    try:
        assert is_valid_retrieve_count_of_cli_templates_attached_to_a_network_profile(
            validator,
            retrieve_count_of_cli_templates_attached_to_a_network_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_reserve_ip_subpool(json_schema_validate, obj):
    json_schema_validate('jsd_274851d84253559e9d3e81881a4bd2fc_v2_3_7_9').validate(obj)
    return True


def get_reserve_ip_subpool(api):
    endpoint_result = api.network_settings.get_reserve_ip_subpool(
        group_name='string',
        ignore_inherited_groups=True,
        limit=0,
        offset=0,
        pool_usage='string',
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
        group_name=None,
        ignore_inherited_groups=None,
        limit=None,
        offset=None,
        pool_usage=None,
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
    json_schema_validate('jsd_eabbb425255a57578e9db00cda1f303a_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_700808cec6c85d9bb4bcc8f61f31296b_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_07fd6083b0c65d03b2d53f10b3ece59d_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_69dda850a0675b888048adf8d488aec1_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_1ffa347eb411567a9c793696795250a5_v2_3_7_9').validate(obj)
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
    json_schema_validate('jsd_03e22c99a82f5764828810acb45e7a9e_v2_3_7_9').validate(obj)
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


def is_valid_sync_network_devices_credential(json_schema_validate, obj):
    json_schema_validate('jsd_79e73b352ff2573aab906c2ad75c5a71_v2_3_7_9').validate(obj)
    return True


def sync_network_devices_credential(api):
    endpoint_result = api.network_settings.sync_network_devices_credential(
        active_validation=True,
        deviceCredentialId='string',
        payload=None,
        siteId='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_sync_network_devices_credential(api, validator):
    try:
        assert is_valid_sync_network_devices_credential(
            validator,
            sync_network_devices_credential(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def sync_network_devices_credential_default_val(api):
    endpoint_result = api.network_settings.sync_network_devices_credential(
        active_validation=True,
        deviceCredentialId=None,
        payload=None,
        siteId=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_sync_network_devices_credential_default_val(api, validator):
    try:
        assert is_valid_sync_network_devices_credential(
            validator,
            sync_network_devices_credential_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_aaa_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_953292cd2e825a78b6de087e991f6fe0_v2_3_7_9').validate(obj)
    return True


def set_aaa_settings_for_a_site(api):
    endpoint_result = api.network_settings.set_aaa_settings_for_a_site(
        aaaClient={'serverType': 'string', 'protocol': 'string', 'pan': 'string', 'primaryServerIp': 'string', 'secondaryServerIp': 'string', 'sharedSecret': 'string'},
        aaaNetwork={'serverType': 'string', 'protocol': 'string', 'pan': 'string', 'primaryServerIp': 'string', 'secondaryServerIp': 'string', 'sharedSecret': 'string'},
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_aaa_settings_for_a_site(api, validator):
    try:
        assert is_valid_set_aaa_settings_for_a_site(
            validator,
            set_aaa_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_aaa_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.set_aaa_settings_for_a_site(
        aaaClient=None,
        aaaNetwork=None,
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_aaa_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_set_aaa_settings_for_a_site(
            validator,
            set_aaa_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_aaa_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_4c13899171d45b4f828423c6feaa1e46_v2_3_7_9').validate(obj)
    return True


def retrieve_aaa_settings_for_a_site(api):
    endpoint_result = api.network_settings.retrieve_aaa_settings_for_a_site(
        id='string',
        inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_aaa_settings_for_a_site(api, validator):
    try:
        assert is_valid_retrieve_aaa_settings_for_a_site(
            validator,
            retrieve_aaa_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_aaa_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.retrieve_aaa_settings_for_a_site(
        id='string',
        inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_aaa_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_retrieve_aaa_settings_for_a_site(
            validator,
            retrieve_aaa_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_banner_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_9b29d90ce0125ad898bc06bbceb07403_v2_3_7_9').validate(obj)
    return True


def retrieve_banner_settings_for_a_site(api):
    endpoint_result = api.network_settings.retrieve_banner_settings_for_a_site(
        id='string',
        inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_banner_settings_for_a_site(api, validator):
    try:
        assert is_valid_retrieve_banner_settings_for_a_site(
            validator,
            retrieve_banner_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_banner_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.retrieve_banner_settings_for_a_site(
        id='string',
        inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_banner_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_retrieve_banner_settings_for_a_site(
            validator,
            retrieve_banner_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_banner_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_b3c4383ecc13514c85c6f3d8484f6d68_v2_3_7_9').validate(obj)
    return True


def set_banner_settings_for_a_site(api):
    endpoint_result = api.network_settings.set_banner_settings_for_a_site(
        active_validation=True,
        banner={'type': 'string', 'message': 'string'},
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_banner_settings_for_a_site(api, validator):
    try:
        assert is_valid_set_banner_settings_for_a_site(
            validator,
            set_banner_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_banner_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.set_banner_settings_for_a_site(
        active_validation=True,
        banner=None,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_banner_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_set_banner_settings_for_a_site(
            validator,
            set_banner_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_credential_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_e4e92f7adc845290b11168e59ab4c88b_v2_3_7_9').validate(obj)
    return True


def get_device_credential_settings_for_a_site(api):
    endpoint_result = api.network_settings.get_device_credential_settings_for_a_site(
        id='string',
        inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_settings_for_a_site(api, validator):
    try:
        assert is_valid_get_device_credential_settings_for_a_site(
            validator,
            get_device_credential_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_credential_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.get_device_credential_settings_for_a_site(
        id='string',
        inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_get_device_credential_settings_for_a_site(
            validator,
            get_device_credential_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_credential_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_8e481654675355408be8daff9a82f9a0_v2_3_7_9').validate(obj)
    return True


def update_device_credential_settings_for_a_site(api):
    endpoint_result = api.network_settings.update_device_credential_settings_for_a_site(
        active_validation=True,
        cliCredentialsId={'credentialsId': 'string'},
        httpReadCredentialsId={'credentialsId': 'string'},
        httpWriteCredentialsId={'credentialsId': 'string'},
        id='string',
        payload=None,
        snmpv2cReadCredentialsId={'credentialsId': 'string'},
        snmpv2cWriteCredentialsId={'credentialsId': 'string'},
        snmpv3CredentialsId={'credentialsId': 'string'}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_device_credential_settings_for_a_site(api, validator):
    try:
        assert is_valid_update_device_credential_settings_for_a_site(
            validator,
            update_device_credential_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_credential_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.update_device_credential_settings_for_a_site(
        active_validation=True,
        cliCredentialsId=None,
        httpReadCredentialsId=None,
        httpWriteCredentialsId=None,
        id='string',
        payload=None,
        snmpv2cReadCredentialsId=None,
        snmpv2cWriteCredentialsId=None,
        snmpv3CredentialsId=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_device_credential_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_update_device_credential_settings_for_a_site(
            validator,
            update_device_credential_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_devices_credentials_sync_status(json_schema_validate, obj):
    json_schema_validate('jsd_be59a332e9e45f6991e96111743fd775_v2_3_7_9').validate(obj)
    return True


def get_network_devices_credentials_sync_status(api):
    endpoint_result = api.network_settings.get_network_devices_credentials_sync_status(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_devices_credentials_sync_status(api, validator):
    try:
        assert is_valid_get_network_devices_credentials_sync_status(
            validator,
            get_network_devices_credentials_sync_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_devices_credentials_sync_status_default_val(api):
    endpoint_result = api.network_settings.get_network_devices_credentials_sync_status(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_devices_credentials_sync_status_default_val(api, validator):
    try:
        assert is_valid_get_network_devices_credentials_sync_status(
            validator,
            get_network_devices_credentials_sync_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_dhcp_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_2a15a2f83f975a6a9964e7da79a605de_v2_3_7_9').validate(obj)
    return True


def set_dhcp_settings_for_a_site(api):
    endpoint_result = api.network_settings.set_dhcp_settings_for_a_site(
        active_validation=True,
        dhcp={'servers': ['string']},
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_dhcp_settings_for_a_site(api, validator):
    try:
        assert is_valid_set_dhcp_settings_for_a_site(
            validator,
            set_dhcp_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_dhcp_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.set_dhcp_settings_for_a_site(
        active_validation=True,
        dhcp=None,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_dhcp_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_set_dhcp_settings_for_a_site(
            validator,
            set_dhcp_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_d_h_c_p_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_5fe723d00fce5700b8abe2a43b82f035_v2_3_7_9').validate(obj)
    return True


def retrieve_d_h_c_p_settings_for_a_site(api):
    endpoint_result = api.network_settings.retrieve_d_h_c_p_settings_for_a_site(
        id='string',
        inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_d_h_c_p_settings_for_a_site(api, validator):
    try:
        assert is_valid_retrieve_d_h_c_p_settings_for_a_site(
            validator,
            retrieve_d_h_c_p_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_d_h_c_p_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.retrieve_d_h_c_p_settings_for_a_site(
        id='string',
        inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_d_h_c_p_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_retrieve_d_h_c_p_settings_for_a_site(
            validator,
            retrieve_d_h_c_p_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_d_n_s_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_0f32e172f454564ba92d7a410c63c164_v2_3_7_9').validate(obj)
    return True


def retrieve_d_n_s_settings_for_a_site(api):
    endpoint_result = api.network_settings.retrieve_d_n_s_settings_for_a_site(
        id='string',
        inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_d_n_s_settings_for_a_site(api, validator):
    try:
        assert is_valid_retrieve_d_n_s_settings_for_a_site(
            validator,
            retrieve_d_n_s_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_d_n_s_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.retrieve_d_n_s_settings_for_a_site(
        id='string',
        inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_d_n_s_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_retrieve_d_n_s_settings_for_a_site(
            validator,
            retrieve_d_n_s_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_d_n_s_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_6eb3b18894545315b25b94d0c0e2ec67_v2_3_7_9').validate(obj)
    return True


def set_d_n_s_settings_for_a_site(api):
    endpoint_result = api.network_settings.set_d_n_s_settings_for_a_site(
        active_validation=True,
        dns={'domainName': 'string', 'dnsServers': ['string']},
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_d_n_s_settings_for_a_site(api, validator):
    try:
        assert is_valid_set_d_n_s_settings_for_a_site(
            validator,
            set_d_n_s_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_d_n_s_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.set_d_n_s_settings_for_a_site(
        active_validation=True,
        dns=None,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_d_n_s_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_set_d_n_s_settings_for_a_site(
            validator,
            set_d_n_s_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_image_distribution_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_d02614492a2251c18de2e36c097e40ff_v2_3_7_9').validate(obj)
    return True


def set_image_distribution_settings_for_a_site(api):
    endpoint_result = api.network_settings.set_image_distribution_settings_for_a_site(
        active_validation=True,
        id='string',
        imageDistribution={'servers': ['string']},
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_image_distribution_settings_for_a_site(api, validator):
    try:
        assert is_valid_set_image_distribution_settings_for_a_site(
            validator,
            set_image_distribution_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_image_distribution_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.set_image_distribution_settings_for_a_site(
        active_validation=True,
        id='string',
        imageDistribution=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_image_distribution_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_set_image_distribution_settings_for_a_site(
            validator,
            set_image_distribution_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_image_distribution_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_d0c5259b59bd5751994e2aa77a15f70e_v2_3_7_9').validate(obj)
    return True


def retrieve_image_distribution_settings_for_a_site(api):
    endpoint_result = api.network_settings.retrieve_image_distribution_settings_for_a_site(
        id='string',
        inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_image_distribution_settings_for_a_site(api, validator):
    try:
        assert is_valid_retrieve_image_distribution_settings_for_a_site(
            validator,
            retrieve_image_distribution_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_image_distribution_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.retrieve_image_distribution_settings_for_a_site(
        id='string',
        inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_image_distribution_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_retrieve_image_distribution_settings_for_a_site(
            validator,
            retrieve_image_distribution_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_n_t_p_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_df9ec5aa58815a849b4853b223343e5e_v2_3_7_9').validate(obj)
    return True


def set_n_t_p_settings_for_a_site(api):
    endpoint_result = api.network_settings.set_n_t_p_settings_for_a_site(
        active_validation=True,
        id='string',
        ntp={'servers': ['string']},
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_n_t_p_settings_for_a_site(api, validator):
    try:
        assert is_valid_set_n_t_p_settings_for_a_site(
            validator,
            set_n_t_p_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_n_t_p_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.set_n_t_p_settings_for_a_site(
        active_validation=True,
        id='string',
        ntp=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_n_t_p_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_set_n_t_p_settings_for_a_site(
            validator,
            set_n_t_p_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_n_t_p_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_c49b666d3a305b509d0d3b356e912ab4_v2_3_7_9').validate(obj)
    return True


def retrieve_n_t_p_settings_for_a_site(api):
    endpoint_result = api.network_settings.retrieve_n_t_p_settings_for_a_site(
        id='string',
        inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_n_t_p_settings_for_a_site(api, validator):
    try:
        assert is_valid_retrieve_n_t_p_settings_for_a_site(
            validator,
            retrieve_n_t_p_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_n_t_p_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.retrieve_n_t_p_settings_for_a_site(
        id='string',
        inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_n_t_p_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_retrieve_n_t_p_settings_for_a_site(
            validator,
            retrieve_n_t_p_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_telemetry_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_af4b3c5d1dc6505cadd13bf41c894700_v2_3_7_9').validate(obj)
    return True


def retrieve_telemetry_settings_for_a_site(api):
    endpoint_result = api.network_settings.retrieve_telemetry_settings_for_a_site(
        id='string',
        inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_telemetry_settings_for_a_site(api, validator):
    try:
        assert is_valid_retrieve_telemetry_settings_for_a_site(
            validator,
            retrieve_telemetry_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_telemetry_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.retrieve_telemetry_settings_for_a_site(
        id='string',
        inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_telemetry_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_retrieve_telemetry_settings_for_a_site(
            validator,
            retrieve_telemetry_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_telemetry_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_bac0c488707959c182dfef18681bceda_v2_3_7_9').validate(obj)
    return True


def set_telemetry_settings_for_a_site(api):
    endpoint_result = api.network_settings.set_telemetry_settings_for_a_site(
        active_validation=True,
        applicationVisibility={'collector': {'collectorType': 'string', 'address': 'string', 'port': 0}, 'enableOnWiredAccessDevices': True},
        id='string',
        payload=None,
        snmpTraps={'useBuiltinTrapServer': True, 'externalTrapServers': ['string']},
        syslogs={'useBuiltinSyslogServer': True, 'externalSyslogServers': ['string']},
        wiredDataCollection={'enableWiredDataCollectio': True},
        wirelessTelemetry={'enableWirelessTelemetry': True}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_telemetry_settings_for_a_site(api, validator):
    try:
        assert is_valid_set_telemetry_settings_for_a_site(
            validator,
            set_telemetry_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_telemetry_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.set_telemetry_settings_for_a_site(
        active_validation=True,
        applicationVisibility=None,
        id='string',
        payload=None,
        snmpTraps=None,
        syslogs=None,
        wiredDataCollection=None,
        wirelessTelemetry=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_telemetry_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_set_telemetry_settings_for_a_site(
            validator,
            set_telemetry_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_time_zone_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_c17432d928f755f8bb9f4edb83089d3e_v2_3_7_9').validate(obj)
    return True


def set_time_zone_for_a_site(api):
    endpoint_result = api.network_settings.set_time_zone_for_a_site(
        active_validation=True,
        id='string',
        payload=None,
        timeZone={'identifier': 'string'}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_time_zone_for_a_site(api, validator):
    try:
        assert is_valid_set_time_zone_for_a_site(
            validator,
            set_time_zone_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_time_zone_for_a_site_default_val(api):
    endpoint_result = api.network_settings.set_time_zone_for_a_site(
        active_validation=True,
        id='string',
        payload=None,
        timeZone=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_set_time_zone_for_a_site_default_val(api, validator):
    try:
        assert is_valid_set_time_zone_for_a_site(
            validator,
            set_time_zone_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_time_zone_settings_for_a_site(json_schema_validate, obj):
    json_schema_validate('jsd_10a03efc6bba51eeabcde938f0856074_v2_3_7_9').validate(obj)
    return True


def retrieve_time_zone_settings_for_a_site(api):
    endpoint_result = api.network_settings.retrieve_time_zone_settings_for_a_site(
        id='string',
        inherited=True
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_time_zone_settings_for_a_site(api, validator):
    try:
        assert is_valid_retrieve_time_zone_settings_for_a_site(
            validator,
            retrieve_time_zone_settings_for_a_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_time_zone_settings_for_a_site_default_val(api):
    endpoint_result = api.network_settings.retrieve_time_zone_settings_for_a_site(
        id='string',
        inherited=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_retrieve_time_zone_settings_for_a_site_default_val(api, validator):
    try:
        assert is_valid_retrieve_time_zone_settings_for_a_site(
            validator,
            retrieve_time_zone_settings_for_a_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sp_profile(json_schema_validate, obj):
    json_schema_validate('jsd_35598a1d68f15e02adc37239b3fcbbb6_v2_3_7_9').validate(obj)
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


def is_valid_update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site(json_schema_validate, obj):
    json_schema_validate('jsd_54266de1b75d59b083df0ece12259ecd_v2_3_7_9').validate(obj)
    return True


def update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site(api):
    endpoint_result = api.network_settings.update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site(
        active_validation=True,
        deviceIds=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site(api, validator):
    try:
        assert is_valid_update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site(
            validator,
            update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_default_val(api):
    endpoint_result = api.network_settings.update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site(
        active_validation=True,
        deviceIds=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_default_val(api, validator):
    try:
        assert is_valid_update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site(
            validator,
            update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_device_credential_to_site_v2(json_schema_validate, obj):
    json_schema_validate('jsd_156a3954b27e5eeb82789ed231e0557f_v2_3_7_9').validate(obj)
    return True


def assign_device_credential_to_site_v2(api):
    endpoint_result = api.network_settings.assign_device_credential_to_site_v2(
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
def test_assign_device_credential_to_site_v2(api, validator):
    try:
        assert is_valid_assign_device_credential_to_site_v2(
            validator,
            assign_device_credential_to_site_v2(api)
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
        site_id='string',
        snmpV2ReadId=None,
        snmpV2WriteId=None,
        snmpV3Id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_assign_device_credential_to_site_v2_default_val(api, validator):
    try:
        assert is_valid_assign_device_credential_to_site_v2(
            validator,
            assign_device_credential_to_site_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_v2(json_schema_validate, obj):
    json_schema_validate('jsd_d0b7bffe821755dab4e2a2df8ea79404_v2_3_7_9').validate(obj)
    return True


def get_network_v2(api):
    endpoint_result = api.network_settings.get_network_v2(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_v2(api, validator):
    try:
        assert is_valid_get_network_v2(
            validator,
            get_network_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_v2_default_val(api):
    endpoint_result = api.network_settings.get_network_v2(
        site_id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_v2_default_val(api, validator):
    try:
        assert is_valid_get_network_v2(
            validator,
            get_network_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_v2(json_schema_validate, obj):
    json_schema_validate('jsd_c5f97865727857d5b1eeaedee3dcccd2_v2_3_7_9').validate(obj)
    return True


def create_network_v2(api):
    endpoint_result = api.network_settings.create_network_v2(
        active_validation=True,
        payload=None,
        settings={'dhcpServer': ['string'], 'dnsServer': {'domainName': 'string', 'primaryIpAddress': 'string', 'secondaryIpAddress': 'string'}, 'syslogServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'snmpServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'netflowcollector': {'ipAddress': 'string', 'port': 0}, 'ntpServer': ['string'], 'timezone': 'string', 'messageOfTheday': {'bannerMessage': 'string', 'retainExistingBanner': 'string'}, 'network_aaa': {'servers': 'string', 'ipAddress': 'string', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'string'}, 'clientAndEndpoint_aaa': {'servers': 'string', 'ipAddress': 'string', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'string'}},
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_network_v2(api, validator):
    try:
        assert is_valid_create_network_v2(
            validator,
            create_network_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_network_v2_default_val(api):
    endpoint_result = api.network_settings.create_network_v2(
        active_validation=True,
        payload=None,
        settings=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_network_v2_default_val(api, validator):
    try:
        assert is_valid_create_network_v2(
            validator,
            create_network_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_v2(json_schema_validate, obj):
    json_schema_validate('jsd_a7935eedd53a5b8c84668c903cc1c705_v2_3_7_9').validate(obj)
    return True


def update_network_v2(api):
    endpoint_result = api.network_settings.update_network_v2(
        active_validation=True,
        payload=None,
        settings={'dhcpServer': ['string'], 'dnsServer': {'domainName': 'string', 'primaryIpAddress': 'string', 'secondaryIpAddress': 'string'}, 'syslogServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'snmpServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'netflowcollector': {'ipAddress': 'string', 'port': 0}, 'ntpServer': ['string'], 'timezone': 'string', 'messageOfTheday': {'bannerMessage': 'string', 'retainExistingBanner': 'string'}, 'network_aaa': {'servers': 'string', 'ipAddress': 'string', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'string'}, 'clientAndEndpoint_aaa': {'servers': 'string', 'ipAddress': 'string', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'string'}},
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_network_v2(api, validator):
    try:
        assert is_valid_update_network_v2(
            validator,
            update_network_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_v2_default_val(api):
    endpoint_result = api.network_settings.update_network_v2(
        active_validation=True,
        payload=None,
        settings=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_network_v2_default_val(api, validator):
    try:
        assert is_valid_update_network_v2(
            validator,
            update_network_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sp_profile_v2(json_schema_validate, obj):
    json_schema_validate('jsd_a66db26df529597c84c2a15ea2d632ce_v2_3_7_9').validate(obj)
    return True


def create_sp_profile_v2(api):
    endpoint_result = api.network_settings.create_sp_profile_v2(
        active_validation=True,
        payload=None,
        settings={'qos': [{'profileName': 'string', 'model': 'string', 'wanProvider': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_sp_profile_v2(api, validator):
    try:
        assert is_valid_create_sp_profile_v2(
            validator,
            create_sp_profile_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_sp_profile_v2_default_val(api):
    endpoint_result = api.network_settings.create_sp_profile_v2(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_sp_profile_v2_default_val(api, validator):
    try:
        assert is_valid_create_sp_profile_v2(
            validator,
            create_sp_profile_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_sp_profile_v2(json_schema_validate, obj):
    json_schema_validate('jsd_53680237e0b654c39dc6e19cd6f5194d_v2_3_7_9').validate(obj)
    return True


def update_sp_profile_v2(api):
    endpoint_result = api.network_settings.update_sp_profile_v2(
        active_validation=True,
        payload=None,
        settings={'qos': [{'profileName': 'string', 'model': 'string', 'wanProvider': 'string', 'oldProfileName': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_sp_profile_v2(api, validator):
    try:
        assert is_valid_update_sp_profile_v2(
            validator,
            update_sp_profile_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_sp_profile_v2_default_val(api):
    endpoint_result = api.network_settings.update_sp_profile_v2(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_sp_profile_v2_default_val(api, validator):
    try:
        assert is_valid_update_sp_profile_v2(
            validator,
            update_sp_profile_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_service_provider_details_v2(json_schema_validate, obj):
    json_schema_validate('jsd_3907f01025635a52bdfdac7226911b31_v2_3_7_9').validate(obj)
    return True


def get_service_provider_details_v2(api):
    endpoint_result = api.network_settings.get_service_provider_details_v2(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details_v2(api, validator):
    try:
        assert is_valid_get_service_provider_details_v2(
            validator,
            get_service_provider_details_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_service_provider_details_v2_default_val(api):
    endpoint_result = api.network_settings.get_service_provider_details_v2(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details_v2_default_val(api, validator):
    try:
        assert is_valid_get_service_provider_details_v2(
            validator,
            get_service_provider_details_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sp_profile_v2(json_schema_validate, obj):
    json_schema_validate('jsd_a9bbbce953615baeb0a324c61753139d_v2_3_7_9').validate(obj)
    return True


def delete_sp_profile_v2(api):
    endpoint_result = api.network_settings.delete_sp_profile_v2(
        sp_profile_name='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile_v2(api, validator):
    try:
        assert is_valid_delete_sp_profile_v2(
            validator,
            delete_sp_profile_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_sp_profile_v2_default_val(api):
    endpoint_result = api.network_settings.delete_sp_profile_v2(
        sp_profile_name='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile_v2_default_val(api, validator):
    try:
        assert is_valid_delete_sp_profile_v2(
            validator,
            delete_sp_profile_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI system_settings API fixtures and tests.

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


def is_valid_add_authentication_and_policy_server_access_configuration_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_fa3975be5af25501abb40339d96917eb_v2_3_7_6").validate(obj)
    return True


def add_authentication_and_policy_server_access_configuration_v1(api):
    endpoint_result = api.system_settings.add_authentication_and_policy_server_access_configuration_v1(
        accountingPort=0,
        active_validation=True,
        authenticationPort=0,
        ciscoIseDtos=[
            {
                "description": "string",
                "fqdn": "string",
                "password": "string",
                "sshkey": "string",
                "ipAddress": "string",
                "subscriberName": "string",
                "userName": "string",
            }
        ],
        encryptionKey="string",
        encryptionScheme="string",
        externalCiscoIseIpAddrDtos=[
            {
                "externalCiscoIseIpAddresses": [{"externalIpAddress": "string"}],
                "type": "string",
            }
        ],
        ipAddress="string",
        isIseEnabled=True,
        messageKey="string",
        payload=None,
        port=0,
        protocol="string",
        pxgridEnabled=True,
        retries="string",
        role="string",
        sharedSecret="string",
        timeoutSeconds="string",
        useDnacCertForPxgrid=True,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_add_authentication_and_policy_server_access_configuration_v1(api, validator):
    try:
        assert is_valid_add_authentication_and_policy_server_access_configuration_v1(
            validator, add_authentication_and_policy_server_access_configuration_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_authentication_and_policy_server_access_configuration_v1_default_val(api):
    endpoint_result = api.system_settings.add_authentication_and_policy_server_access_configuration_v1(
        accountingPort=None,
        active_validation=True,
        authenticationPort=None,
        ciscoIseDtos=None,
        encryptionKey=None,
        encryptionScheme=None,
        externalCiscoIseIpAddrDtos=None,
        ipAddress=None,
        isIseEnabled=None,
        messageKey=None,
        payload=None,
        port=None,
        protocol=None,
        pxgridEnabled=None,
        retries=None,
        role=None,
        sharedSecret=None,
        timeoutSeconds=None,
        useDnacCertForPxgrid=None,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_add_authentication_and_policy_server_access_configuration_v1_default_val(
    api, validator
):
    try:
        assert is_valid_add_authentication_and_policy_server_access_configuration_v1(
            validator,
            add_authentication_and_policy_server_access_configuration_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_authentication_and_policy_servers_v1(json_schema_validate, obj):
    json_schema_validate("jsd_f7cc2592721f5b9b9f99795a26130147_v2_3_7_6").validate(obj)
    return True


def get_authentication_and_policy_servers_v1(api):
    endpoint_result = api.system_settings.get_authentication_and_policy_servers_v1(
        is_ise_enabled=True, role="string", state="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_get_authentication_and_policy_servers_v1(api, validator):
    try:
        assert is_valid_get_authentication_and_policy_servers_v1(
            validator, get_authentication_and_policy_servers_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_authentication_and_policy_servers_v1_default_val(api):
    endpoint_result = api.system_settings.get_authentication_and_policy_servers_v1(
        is_ise_enabled=None, role=None, state=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_get_authentication_and_policy_servers_v1_default_val(api, validator):
    try:
        assert is_valid_get_authentication_and_policy_servers_v1(
            validator, get_authentication_and_policy_servers_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_authentication_and_policy_server_access_configuration_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_3b5ce4c02a525aa98e49940d5aa006a7_v2_3_7_6").validate(obj)
    return True


def delete_authentication_and_policy_server_access_configuration_v1(api):
    endpoint_result = api.system_settings.delete_authentication_and_policy_server_access_configuration_v1(
        id="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_delete_authentication_and_policy_server_access_configuration_v1(
    api, validator
):
    try:
        assert is_valid_delete_authentication_and_policy_server_access_configuration_v1(
            validator,
            delete_authentication_and_policy_server_access_configuration_v1(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_authentication_and_policy_server_access_configuration_v1_default_val(api):
    endpoint_result = api.system_settings.delete_authentication_and_policy_server_access_configuration_v1(
        id="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_delete_authentication_and_policy_server_access_configuration_v1_default_val(
    api, validator
):
    try:
        assert is_valid_delete_authentication_and_policy_server_access_configuration_v1(
            validator,
            delete_authentication_and_policy_server_access_configuration_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_edit_authentication_and_policy_server_access_configuration_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_fbdd94fbecd256c08e1d9f6e1a7657ac_v2_3_7_6").validate(obj)
    return True


def edit_authentication_and_policy_server_access_configuration_v1(api):
    endpoint_result = api.system_settings.edit_authentication_and_policy_server_access_configuration_v1(
        accountingPort=0,
        active_validation=True,
        authenticationPort=0,
        ciscoIseDtos=[
            {
                "description": "string",
                "fqdn": "string",
                "password": "string",
                "sshkey": "string",
                "ipAddress": "string",
                "subscriberName": "string",
                "userName": "string",
            }
        ],
        encryptionKey="string",
        encryptionScheme="string",
        externalCiscoIseIpAddrDtos=[
            {
                "externalCiscoIseIpAddresses": [{"externalIpAddress": "string"}],
                "type": "string",
            }
        ],
        id="string",
        ipAddress="string",
        isIseEnabled=True,
        messageKey="string",
        payload=None,
        port=0,
        protocol="string",
        pxgridEnabled=True,
        retries="string",
        role="string",
        sharedSecret="string",
        timeoutSeconds="string",
        useDnacCertForPxgrid=True,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_edit_authentication_and_policy_server_access_configuration_v1(api, validator):
    try:
        assert is_valid_edit_authentication_and_policy_server_access_configuration_v1(
            validator,
            edit_authentication_and_policy_server_access_configuration_v1(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def edit_authentication_and_policy_server_access_configuration_v1_default_val(api):
    endpoint_result = api.system_settings.edit_authentication_and_policy_server_access_configuration_v1(
        accountingPort=None,
        active_validation=True,
        authenticationPort=None,
        ciscoIseDtos=None,
        encryptionKey=None,
        encryptionScheme=None,
        externalCiscoIseIpAddrDtos=None,
        id="string",
        ipAddress=None,
        isIseEnabled=None,
        messageKey=None,
        payload=None,
        port=None,
        protocol=None,
        pxgridEnabled=None,
        retries=None,
        role=None,
        sharedSecret=None,
        timeoutSeconds=None,
        useDnacCertForPxgrid=None,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_edit_authentication_and_policy_server_access_configuration_v1_default_val(
    api, validator
):
    try:
        assert is_valid_edit_authentication_and_policy_server_access_configuration_v1(
            validator,
            edit_authentication_and_policy_server_access_configuration_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_4121e0ed6b9a530ea05d77a199ded4e3_v2_3_7_6").validate(obj)
    return True


def accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_v1(api):
    endpoint_result = api.system_settings.accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_v1(
        active_validation=True, id="string", isCertAcceptedByUser=True, payload=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_v1(
    api, validator
):
    try:
        assert is_valid_accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_v1(
            validator,
            accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_v1(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_v1_default_val(
    api,
):
    endpoint_result = api.system_settings.accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_v1(
        active_validation=True, id="string", isCertAcceptedByUser=None, payload=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_v1_default_val(
    api, validator
):
    try:
        assert is_valid_accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_v1(
            validator,
            accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_configuration_details_of_the_external_ip_a_m_server_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_9838825d6d7d5c8983c1d3c9815bfd35_v2_3_7_6").validate(obj)
    return True


def creates_configuration_details_of_the_external_ip_a_m_server_v1(api):
    endpoint_result = api.system_settings.creates_configuration_details_of_the_external_ip_a_m_server_v1(
        active_validation=True,
        password="string",
        payload=None,
        provider="string",
        serverName="string",
        serverUrl="string",
        syncView=True,
        userName="string",
        view="string",
    )
    return endpoint_result


@pytest.mark.system_settings
def test_creates_configuration_details_of_the_external_ip_a_m_server_v1(api, validator):
    try:
        assert is_valid_creates_configuration_details_of_the_external_ip_a_m_server_v1(
            validator,
            creates_configuration_details_of_the_external_ip_a_m_server_v1(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_configuration_details_of_the_external_ip_a_m_server_v1_default_val(api):
    endpoint_result = api.system_settings.creates_configuration_details_of_the_external_ip_a_m_server_v1(
        active_validation=True,
        password=None,
        payload=None,
        provider=None,
        serverName=None,
        serverUrl=None,
        syncView=None,
        userName=None,
        view=None,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_creates_configuration_details_of_the_external_ip_a_m_server_v1_default_val(
    api, validator
):
    try:
        assert is_valid_creates_configuration_details_of_the_external_ip_a_m_server_v1(
            validator,
            creates_configuration_details_of_the_external_ip_a_m_server_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_configuration_details_of_the_external_ip_a_m_server_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_88f06b38c5915162acc31afbf33b843e_v2_3_7_6").validate(obj)
    return True


def retrieves_configuration_details_of_the_external_ip_a_m_server_v1(api):
    endpoint_result = (
        api.system_settings.retrieves_configuration_details_of_the_external_ip_a_m_server_v1()
    )
    return endpoint_result


@pytest.mark.system_settings
def test_retrieves_configuration_details_of_the_external_ip_a_m_server_v1(
    api, validator
):
    try:
        assert (
            is_valid_retrieves_configuration_details_of_the_external_ip_a_m_server_v1(
                validator,
                retrieves_configuration_details_of_the_external_ip_a_m_server_v1(api),
            )
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_configuration_details_of_the_external_ip_a_m_server_v1_default_val(api):
    endpoint_result = (
        api.system_settings.retrieves_configuration_details_of_the_external_ip_a_m_server_v1()
    )
    return endpoint_result


@pytest.mark.system_settings
def test_retrieves_configuration_details_of_the_external_ip_a_m_server_v1_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_configuration_details_of_the_external_ip_a_m_server_v1(
            validator,
            retrieves_configuration_details_of_the_external_ip_a_m_server_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_configuration_details_of_the_external_ip_a_m_server_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_28f47e2181ce5957818a97f135a5eb9f_v2_3_7_6").validate(obj)
    return True


def deletes_configuration_details_of_the_external_ip_a_m_server_v1(api):
    endpoint_result = (
        api.system_settings.deletes_configuration_details_of_the_external_ip_a_m_server_v1()
    )
    return endpoint_result


@pytest.mark.system_settings
def test_deletes_configuration_details_of_the_external_ip_a_m_server_v1(api, validator):
    try:
        assert is_valid_deletes_configuration_details_of_the_external_ip_a_m_server_v1(
            validator,
            deletes_configuration_details_of_the_external_ip_a_m_server_v1(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_configuration_details_of_the_external_ip_a_m_server_v1_default_val(api):
    endpoint_result = (
        api.system_settings.deletes_configuration_details_of_the_external_ip_a_m_server_v1()
    )
    return endpoint_result


@pytest.mark.system_settings
def test_deletes_configuration_details_of_the_external_ip_a_m_server_v1_default_val(
    api, validator
):
    try:
        assert is_valid_deletes_configuration_details_of_the_external_ip_a_m_server_v1(
            validator,
            deletes_configuration_details_of_the_external_ip_a_m_server_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_configuration_details_of_the_external_ip_a_m_server_v1(
    json_schema_validate, obj
):
    json_schema_validate("jsd_88ba98ed72975099b39dd2dc4cb65ed8_v2_3_7_6").validate(obj)
    return True


def updates_configuration_details_of_the_external_ip_a_m_server_v1(api):
    endpoint_result = api.system_settings.updates_configuration_details_of_the_external_ip_a_m_server_v1(
        active_validation=True,
        password="string",
        payload=None,
        serverName="string",
        serverUrl="string",
        syncView=True,
        userName="string",
        view="string",
    )
    return endpoint_result


@pytest.mark.system_settings
def test_updates_configuration_details_of_the_external_ip_a_m_server_v1(api, validator):
    try:
        assert is_valid_updates_configuration_details_of_the_external_ip_a_m_server_v1(
            validator,
            updates_configuration_details_of_the_external_ip_a_m_server_v1(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_configuration_details_of_the_external_ip_a_m_server_v1_default_val(api):
    endpoint_result = api.system_settings.updates_configuration_details_of_the_external_ip_a_m_server_v1(
        active_validation=True,
        password=None,
        payload=None,
        serverName=None,
        serverUrl=None,
        syncView=None,
        userName=None,
        view=None,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_updates_configuration_details_of_the_external_ip_a_m_server_v1_default_val(
    api, validator
):
    try:
        assert is_valid_updates_configuration_details_of_the_external_ip_a_m_server_v1(
            validator,
            updates_configuration_details_of_the_external_ip_a_m_server_v1_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_cisco_ise_server_integration_status_v1(json_schema_validate, obj):
    json_schema_validate("jsd_a1bc4f82533a5d909ed345b4703cff8a_v2_3_7_6").validate(obj)
    return True


def cisco_ise_server_integration_status_v1(api):
    endpoint_result = api.system_settings.cisco_ise_server_integration_status_v1()
    return endpoint_result


@pytest.mark.system_settings
def test_cisco_ise_server_integration_status_v1(api, validator):
    try:
        assert is_valid_cisco_ise_server_integration_status_v1(
            validator, cisco_ise_server_integration_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def cisco_ise_server_integration_status_v1_default_val(api):
    endpoint_result = api.system_settings.cisco_ise_server_integration_status_v1()
    return endpoint_result


@pytest.mark.system_settings
def test_cisco_ise_server_integration_status_v1_default_val(api, validator):
    try:
        assert is_valid_cisco_ise_server_integration_status_v1(
            validator, cisco_ise_server_integration_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_custom_prompt_support_get_api_v1(json_schema_validate, obj):
    json_schema_validate("jsd_ada20dc4915d5901b50634628392e79f_v2_3_7_6").validate(obj)
    return True


def custom_prompt_support_get_api_v1(api):
    endpoint_result = api.system_settings.custom_prompt_support_get_api_v1()
    return endpoint_result


@pytest.mark.system_settings
def test_custom_prompt_support_get_api_v1(api, validator):
    try:
        assert is_valid_custom_prompt_support_get_api_v1(
            validator, custom_prompt_support_get_api_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def custom_prompt_support_get_api_v1_default_val(api):
    endpoint_result = api.system_settings.custom_prompt_support_get_api_v1()
    return endpoint_result


@pytest.mark.system_settings
def test_custom_prompt_support_get_api_v1_default_val(api, validator):
    try:
        assert is_valid_custom_prompt_support_get_api_v1(
            validator, custom_prompt_support_get_api_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_custom_prompt_post_api_v1(json_schema_validate, obj):
    json_schema_validate("jsd_d2ea814bfae85da1b77872d095fc8221_v2_3_7_6").validate(obj)
    return True


def custom_prompt_post_api_v1(api):
    endpoint_result = api.system_settings.custom_prompt_post_api_v1(
        active_validation=True,
        passwordPrompt="string",
        payload=None,
        usernamePrompt="string",
    )
    return endpoint_result


@pytest.mark.system_settings
def test_custom_prompt_post_api_v1(api, validator):
    try:
        assert is_valid_custom_prompt_post_api_v1(
            validator, custom_prompt_post_api_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def custom_prompt_post_api_v1_default_val(api):
    endpoint_result = api.system_settings.custom_prompt_post_api_v1(
        active_validation=True, passwordPrompt=None, payload=None, usernamePrompt=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_custom_prompt_post_api_v1_default_val(api, validator):
    try:
        assert is_valid_custom_prompt_post_api_v1(
            validator, custom_prompt_post_api_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_provisioning_settings_v1(json_schema_validate, obj):
    json_schema_validate("jsd_b3ab480a3f485ecc9fef1bd2f8c9d109_v2_3_7_6").validate(obj)
    return True


def set_provisioning_settings_v1(api):
    endpoint_result = api.system_settings.set_provisioning_settings_v1(
        active_validation=True,
        payload=None,
        requireItsmApproval=True,
        requirePreview=True,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_set_provisioning_settings_v1(api, validator):
    try:
        assert is_valid_set_provisioning_settings_v1(
            validator, set_provisioning_settings_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_provisioning_settings_v1_default_val(api):
    endpoint_result = api.system_settings.set_provisioning_settings_v1(
        active_validation=True,
        payload=None,
        requireItsmApproval=None,
        requirePreview=None,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_set_provisioning_settings_v1_default_val(api, validator):
    try:
        assert is_valid_set_provisioning_settings_v1(
            validator, set_provisioning_settings_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_provisioning_settings_v1(json_schema_validate, obj):
    json_schema_validate("jsd_b2e5d0e7f80b555f865bb1f72c4d7bdd_v2_3_7_6").validate(obj)
    return True


def get_provisioning_settings_v1(api):
    endpoint_result = api.system_settings.get_provisioning_settings_v1()
    return endpoint_result


@pytest.mark.system_settings
def test_get_provisioning_settings_v1(api, validator):
    try:
        assert is_valid_get_provisioning_settings_v1(
            validator, get_provisioning_settings_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_provisioning_settings_v1_default_val(api):
    endpoint_result = api.system_settings.get_provisioning_settings_v1()
    return endpoint_result


@pytest.mark.system_settings
def test_get_provisioning_settings_v1_default_val(api, validator):
    try:
        assert is_valid_get_provisioning_settings_v1(
            validator, get_provisioning_settings_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

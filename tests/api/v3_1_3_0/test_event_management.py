# -*- coding: utf-8 -*-
"""CatalystCenterAPI event_management API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '3.1.3.0', reason='version does not match')


def is_valid_get_auditlog_parent_records(json_schema_validate, obj):
    json_schema_validate('jsd_9f8e3a0674c15fd58cd78f42dca37c7c_v3_1_3_0').validate(obj)
    return True


def get_auditlog_parent_records(api):
    endpoint_result = api.event_management.get_auditlog_parent_records(
        category='string',
        context='string',
        description='string',
        device_id='string',
        domain='string',
        end_time=0,
        event_hierarchy='string',
        event_id='string',
        instance_id='string',
        is_system_events=True,
        limit=0,
        name='string',
        offset=0,
        order='string',
        severity='string',
        site_id='string',
        sort_by='string',
        source='string',
        start_time=0,
        sub_domain='string',
        user_id='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_auditlog_parent_records(api, validator):
    try:
        assert is_valid_get_auditlog_parent_records(
            validator,
            get_auditlog_parent_records(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_auditlog_parent_records_default_val(api):
    endpoint_result = api.event_management.get_auditlog_parent_records(
        category=None,
        context=None,
        description=None,
        device_id=None,
        domain=None,
        end_time=None,
        event_hierarchy=None,
        event_id=None,
        instance_id=None,
        is_system_events=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        severity=None,
        site_id=None,
        sort_by=None,
        source=None,
        start_time=None,
        sub_domain=None,
        user_id=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_auditlog_parent_records_default_val(api, validator):
    try:
        assert is_valid_get_auditlog_parent_records(
            validator,
            get_auditlog_parent_records_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_auditlog_summary(json_schema_validate, obj):
    json_schema_validate('jsd_894ea7c0220d55ae9e1a51d6823ce862_v3_1_3_0').validate(obj)
    return True


def get_auditlog_summary(api):
    endpoint_result = api.event_management.get_auditlog_summary(
        category='string',
        context='string',
        description='string',
        device_id='string',
        domain='string',
        end_time=0,
        event_hierarchy='string',
        event_id='string',
        instance_id='string',
        is_parent_only=True,
        is_system_events=True,
        name='string',
        parent_instance_id='string',
        severity='string',
        site_id='string',
        source='string',
        start_time=0,
        sub_domain='string',
        user_id='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_auditlog_summary(api, validator):
    try:
        assert is_valid_get_auditlog_summary(
            validator,
            get_auditlog_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_auditlog_summary_default_val(api):
    endpoint_result = api.event_management.get_auditlog_summary(
        category=None,
        context=None,
        description=None,
        device_id=None,
        domain=None,
        end_time=None,
        event_hierarchy=None,
        event_id=None,
        instance_id=None,
        is_parent_only=None,
        is_system_events=None,
        name=None,
        parent_instance_id=None,
        severity=None,
        site_id=None,
        source=None,
        start_time=None,
        sub_domain=None,
        user_id=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_auditlog_summary_default_val(api, validator):
    try:
        assert is_valid_get_auditlog_summary(
            validator,
            get_auditlog_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_auditlog_records(json_schema_validate, obj):
    json_schema_validate('jsd_b0aa5a61f64a5da997dfe05bc8a4a64f_v3_1_3_0').validate(obj)
    return True


def get_auditlog_records(api):
    endpoint_result = api.event_management.get_auditlog_records(
        category='string',
        context='string',
        description='string',
        device_id='string',
        domain='string',
        end_time=0,
        event_hierarchy='string',
        event_id='string',
        instance_id='string',
        is_system_events=True,
        limit=0,
        name='string',
        offset=0,
        order='string',
        parent_instance_id='string',
        severity='string',
        site_id='string',
        sort_by='string',
        source='string',
        start_time=0,
        sub_domain='string',
        user_id='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_auditlog_records(api, validator):
    try:
        assert is_valid_get_auditlog_records(
            validator,
            get_auditlog_records(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_auditlog_records_default_val(api):
    endpoint_result = api.event_management.get_auditlog_records(
        category=None,
        context=None,
        description=None,
        device_id=None,
        domain=None,
        end_time=None,
        event_hierarchy=None,
        event_id=None,
        instance_id=None,
        is_system_events=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        parent_instance_id=None,
        severity=None,
        site_id=None,
        sort_by=None,
        source=None,
        start_time=None,
        sub_domain=None,
        user_id=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_auditlog_records_default_val(api, validator):
    try:
        assert is_valid_get_auditlog_records(
            validator,
            get_auditlog_records_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_snmp_destination_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e6effbb4a8555f669395009245149ba7_v3_1_3_0').validate(obj)
    return True


def get_snmp_destination_v1(api):
    endpoint_result = api.event_management.get_snmp_destination_v1(
        config_id='string',
        limit=0,
        offset=0,
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_snmp_destination_v1(api, validator):
    try:
        assert is_valid_get_snmp_destination_v1(
            validator,
            get_snmp_destination_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_snmp_destination_v1_default_val(api):
    endpoint_result = api.event_management.get_snmp_destination_v1(
        config_id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_snmp_destination_v1_default_val(api, validator):
    try:
        assert is_valid_get_snmp_destination_v1(
            validator,
            get_snmp_destination_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_status_api_for_events_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e1bd67a1a0225713ab23f0d0d3ceb4f6_v3_1_3_0').validate(obj)
    return True


def get_status_api_for_events_v1(api):
    endpoint_result = api.event_management.get_status_api_for_events_v1(
        execution_id='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_status_api_for_events_v1(api, validator):
    try:
        assert is_valid_get_status_api_for_events_v1(
            validator,
            get_status_api_for_events_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_status_api_for_events_v1_default_val(api):
    endpoint_result = api.event_management.get_status_api_for_events_v1(
        execution_id='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_status_api_for_events_v1_default_val(api, validator):
    try:
        assert is_valid_get_status_api_for_events_v1(
            validator,
            get_status_api_for_events_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_email_destination_v1(json_schema_validate, obj):
    json_schema_validate('jsd_96aaebb912125213b350d7423b4f01a4_v3_1_3_0').validate(obj)
    return True


def update_email_destination_v1(api):
    endpoint_result = api.event_management.update_email_destination_v1(
        active_validation=True,
        emailConfigId='string',
        fromEmail='string',
        payload=None,
        primarySMTPConfig={'hostName': 'string', 'port': 'string', 'userName': 'string', 'password': 'string', 'smtpType': 'string'},
        secondarySMTPConfig={'hostName': 'string', 'port': 'string', 'userName': 'string', 'password': 'string', 'smtpType': 'string'},
        subject='string',
        toEmail='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_email_destination_v1(api, validator):
    try:
        assert is_valid_update_email_destination_v1(
            validator,
            update_email_destination_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_email_destination_v1_default_val(api):
    endpoint_result = api.event_management.update_email_destination_v1(
        active_validation=True,
        emailConfigId=None,
        fromEmail=None,
        payload=None,
        primarySMTPConfig=None,
        secondarySMTPConfig=None,
        subject=None,
        toEmail=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_email_destination_v1_default_val(api, validator):
    try:
        assert is_valid_update_email_destination_v1(
            validator,
            update_email_destination_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_email_destination_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d5f08e8ff59e51d1a9ae56c3e20eae3c_v3_1_3_0').validate(obj)
    return True


def get_email_destination_v1(api):
    endpoint_result = api.event_management.get_email_destination_v1(

    )
    return endpoint_result


@pytest.mark.event_management
def test_get_email_destination_v1(api, validator):
    try:
        assert is_valid_get_email_destination_v1(
            validator,
            get_email_destination_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_email_destination_v1_default_val(api):
    endpoint_result = api.event_management.get_email_destination_v1(

    )
    return endpoint_result


@pytest.mark.event_management
def test_get_email_destination_v1_default_val(api, validator):
    try:
        assert is_valid_get_email_destination_v1(
            validator,
            get_email_destination_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_email_destination_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9c991ce0b0f058a08c863a4abdfc70a6_v3_1_3_0').validate(obj)
    return True


def create_email_destination_v1(api):
    endpoint_result = api.event_management.create_email_destination_v1(
        active_validation=True,
        emailConfigId='string',
        fromEmail='string',
        payload=None,
        primarySMTPConfig={'hostName': 'string', 'port': 'string', 'userName': 'string', 'password': 'string', 'smtpType': 'string'},
        secondarySMTPConfig={'hostName': 'string', 'port': 'string', 'userName': 'string', 'password': 'string', 'smtpType': 'string'},
        subject='string',
        toEmail='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_email_destination_v1(api, validator):
    try:
        assert is_valid_create_email_destination_v1(
            validator,
            create_email_destination_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_email_destination_v1_default_val(api):
    endpoint_result = api.event_management.create_email_destination_v1(
        active_validation=True,
        emailConfigId=None,
        fromEmail=None,
        payload=None,
        primarySMTPConfig=None,
        secondarySMTPConfig=None,
        subject=None,
        toEmail=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_email_destination_v1_default_val(api, validator):
    try:
        assert is_valid_create_email_destination_v1(
            validator,
            create_email_destination_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_notifications_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c641f481dd285301861010da8d6fbf9f_v3_1_3_0').validate(obj)
    return True


def get_notifications_v1(api):
    endpoint_result = api.event_management.get_notifications_v1(
        category='string',
        domain='string',
        end_time=0,
        event_ids='string',
        limit=0,
        namespace='string',
        offset=0,
        order='string',
        severity='string',
        site_id='string',
        sort_by='string',
        source='string',
        start_time=0,
        sub_domain='string',
        tags='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_notifications_v1(api, validator):
    try:
        assert is_valid_get_notifications_v1(
            validator,
            get_notifications_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_notifications_v1_default_val(api):
    endpoint_result = api.event_management.get_notifications_v1(
        category=None,
        domain=None,
        end_time=None,
        event_ids=None,
        limit=None,
        namespace=None,
        offset=None,
        order=None,
        severity=None,
        site_id=None,
        sort_by=None,
        source=None,
        start_time=None,
        sub_domain=None,
        tags=None,
        type=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_notifications_v1_default_val(api, validator):
    try:
        assert is_valid_get_notifications_v1(
            validator,
            get_notifications_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_of_notifications_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4431fd269fe156e4b5ad3f4210b7b168_v3_1_3_0').validate(obj)
    return True


def count_of_notifications_v1(api):
    endpoint_result = api.event_management.count_of_notifications_v1(
        category='string',
        domain='string',
        end_time=0,
        event_ids='string',
        severity='string',
        source='string',
        start_time=0,
        sub_domain='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_notifications_v1(api, validator):
    try:
        assert is_valid_count_of_notifications_v1(
            validator,
            count_of_notifications_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_of_notifications_v1_default_val(api):
    endpoint_result = api.event_management.count_of_notifications_v1(
        category=None,
        domain=None,
        end_time=None,
        event_ids=None,
        severity=None,
        source=None,
        start_time=None,
        sub_domain=None,
        type=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_notifications_v1_default_val(api, validator):
    try:
        assert is_valid_count_of_notifications_v1(
            validator,
            count_of_notifications_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_snmp_destination_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d69b1cfffdda5bd1828a5a89a262cbdd_v3_1_3_0').validate(obj)
    return True


def create_snmp_destination_v1(api):
    endpoint_result = api.event_management.create_snmp_destination_v1(
        active_validation=True,
        authPassword='string',
        community='string',
        description='string',
        ipAddress='string',
        name='string',
        payload=None,
        port='string',
        privacyPassword='string',
        snmpAuthType='string',
        snmpMode='string',
        snmpPrivacyType='string',
        snmpVersion='string',
        userName='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_snmp_destination_v1(api, validator):
    try:
        assert is_valid_create_snmp_destination_v1(
            validator,
            create_snmp_destination_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_snmp_destination_v1_default_val(api):
    endpoint_result = api.event_management.create_snmp_destination_v1(
        active_validation=True,
        authPassword=None,
        community=None,
        description=None,
        ipAddress=None,
        name=None,
        payload=None,
        port=None,
        privacyPassword=None,
        snmpAuthType=None,
        snmpMode=None,
        snmpPrivacyType=None,
        snmpVersion=None,
        userName=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_snmp_destination_v1_default_val(api, validator):
    try:
        assert is_valid_create_snmp_destination_v1(
            validator,
            create_snmp_destination_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_snmp_destination_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1ccbaf226c685cacac29eb345955f3ad_v3_1_3_0').validate(obj)
    return True


def update_snmp_destination_v1(api):
    endpoint_result = api.event_management.update_snmp_destination_v1(
        active_validation=True,
        authPassword='string',
        community='string',
        configId='string',
        description='string',
        ipAddress='string',
        name='string',
        payload=None,
        port='string',
        privacyPassword='string',
        snmpAuthType='string',
        snmpMode='string',
        snmpPrivacyType='string',
        snmpVersion='string',
        userName='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_snmp_destination_v1(api, validator):
    try:
        assert is_valid_update_snmp_destination_v1(
            validator,
            update_snmp_destination_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_snmp_destination_v1_default_val(api):
    endpoint_result = api.event_management.update_snmp_destination_v1(
        active_validation=True,
        authPassword=None,
        community=None,
        configId=None,
        description=None,
        ipAddress=None,
        name=None,
        payload=None,
        port=None,
        privacyPassword=None,
        snmpAuthType=None,
        snmpMode=None,
        snmpPrivacyType=None,
        snmpVersion=None,
        userName=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_snmp_destination_v1_default_val(api, validator):
    try:
        assert is_valid_update_snmp_destination_v1(
            validator,
            update_snmp_destination_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_event_subscriptions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_343538d7d4e55d6bbb21c34ce863a131_v3_1_3_0').validate(obj)
    return True


def get_event_subscriptions_v1(api):
    endpoint_result = api.event_management.get_event_subscriptions_v1(
        event_ids='string',
        limit=0,
        offset=0,
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_event_subscriptions_v1(api, validator):
    try:
        assert is_valid_get_event_subscriptions_v1(
            validator,
            get_event_subscriptions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_event_subscriptions_v1_default_val(api):
    endpoint_result = api.event_management.get_event_subscriptions_v1(
        event_ids=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_event_subscriptions_v1_default_val(api, validator):
    try:
        assert is_valid_get_event_subscriptions_v1(
            validator,
            get_event_subscriptions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_event_subscriptions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a0e0b1772dfc5a02a96a9f6ee6e2579b_v3_1_3_0').validate(obj)
    return True


def delete_event_subscriptions_v1(api):
    endpoint_result = api.event_management.delete_event_subscriptions_v1(
        subscriptions='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_delete_event_subscriptions_v1(api, validator):
    try:
        assert is_valid_delete_event_subscriptions_v1(
            validator,
            delete_event_subscriptions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_event_subscriptions_v1_default_val(api):
    endpoint_result = api.event_management.delete_event_subscriptions_v1(
        subscriptions=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_delete_event_subscriptions_v1_default_val(api, validator):
    try:
        assert is_valid_delete_event_subscriptions_v1(
            validator,
            delete_event_subscriptions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_event_subscriptions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_dfda5beca4cc5437876bff366493ebf0_v3_1_3_0').validate(obj)
    return True


def update_event_subscriptions_v1(api):
    endpoint_result = api.event_management.update_event_subscriptions_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_event_subscriptions_v1(api, validator):
    try:
        assert is_valid_update_event_subscriptions_v1(
            validator,
            update_event_subscriptions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_event_subscriptions_v1_default_val(api):
    endpoint_result = api.event_management.update_event_subscriptions_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_event_subscriptions_v1_default_val(api, validator):
    try:
        assert is_valid_update_event_subscriptions_v1(
            validator,
            update_event_subscriptions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_event_subscriptions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5fcc151af7615a84adf48b714d146192_v3_1_3_0').validate(obj)
    return True


def create_event_subscriptions_v1(api):
    endpoint_result = api.event_management.create_event_subscriptions_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_event_subscriptions_v1(api, validator):
    try:
        assert is_valid_create_event_subscriptions_v1(
            validator,
            create_event_subscriptions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_event_subscriptions_v1_default_val(api):
    endpoint_result = api.event_management.create_event_subscriptions_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_event_subscriptions_v1_default_val(api, validator):
    try:
        assert is_valid_create_event_subscriptions_v1(
            validator,
            create_event_subscriptions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_email_subscription_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_403889d420225889bb16f99ec7ba099a_v3_1_3_0').validate(obj)
    return True


def get_email_subscription_details_v1(api):
    endpoint_result = api.event_management.get_email_subscription_details_v1(
        instance_id='string',
        limit=0,
        name='string',
        offset=0,
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_email_subscription_details_v1(api, validator):
    try:
        assert is_valid_get_email_subscription_details_v1(
            validator,
            get_email_subscription_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_email_subscription_details_v1_default_val(api):
    endpoint_result = api.event_management.get_email_subscription_details_v1(
        instance_id=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_email_subscription_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_email_subscription_details_v1(
            validator,
            get_email_subscription_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_rest_webhook_subscription_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_86272f278c72555e9a56f554b2a21c85_v3_1_3_0').validate(obj)
    return True


def get_rest_webhook_subscription_details_v1(api):
    endpoint_result = api.event_management.get_rest_webhook_subscription_details_v1(
        instance_id='string',
        limit=0,
        name='string',
        offset=0,
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_rest_webhook_subscription_details_v1(api, validator):
    try:
        assert is_valid_get_rest_webhook_subscription_details_v1(
            validator,
            get_rest_webhook_subscription_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_rest_webhook_subscription_details_v1_default_val(api):
    endpoint_result = api.event_management.get_rest_webhook_subscription_details_v1(
        instance_id=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_rest_webhook_subscription_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_rest_webhook_subscription_details_v1(
            validator,
            get_rest_webhook_subscription_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_syslog_subscription_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c0dcb335458a58fa8bc5a485b174427d_v3_1_3_0').validate(obj)
    return True


def get_syslog_subscription_details_v1(api):
    endpoint_result = api.event_management.get_syslog_subscription_details_v1(
        instance_id='string',
        limit=0,
        name='string',
        offset=0,
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_syslog_subscription_details_v1(api, validator):
    try:
        assert is_valid_get_syslog_subscription_details_v1(
            validator,
            get_syslog_subscription_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_syslog_subscription_details_v1_default_val(api):
    endpoint_result = api.event_management.get_syslog_subscription_details_v1(
        instance_id=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_syslog_subscription_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_syslog_subscription_details_v1(
            validator,
            get_syslog_subscription_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_of_event_subscriptions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c538dc50a4555b5fba17b672a89ee1b8_v3_1_3_0').validate(obj)
    return True


def count_of_event_subscriptions_v1(api):
    endpoint_result = api.event_management.count_of_event_subscriptions_v1(
        event_ids='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_event_subscriptions_v1(api, validator):
    try:
        assert is_valid_count_of_event_subscriptions_v1(
            validator,
            count_of_event_subscriptions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_of_event_subscriptions_v1_default_val(api):
    endpoint_result = api.event_management.count_of_event_subscriptions_v1(
        event_ids=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_event_subscriptions_v1_default_val(api, validator):
    try:
        assert is_valid_count_of_event_subscriptions_v1(
            validator,
            count_of_event_subscriptions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_email_event_subscription_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2e69d02d71905aecbd10b782469efbda_v3_1_3_0').validate(obj)
    return True


def create_email_event_subscription_v1(api):
    endpoint_result = api.event_management.create_email_event_subscription_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_email_event_subscription_v1(api, validator):
    try:
        assert is_valid_create_email_event_subscription_v1(
            validator,
            create_email_event_subscription_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_email_event_subscription_v1_default_val(api):
    endpoint_result = api.event_management.create_email_event_subscription_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_email_event_subscription_v1_default_val(api, validator):
    try:
        assert is_valid_create_email_event_subscription_v1(
            validator,
            create_email_event_subscription_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_email_event_subscription_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f8b4842604b65658afb34b4f124db469_v3_1_3_0').validate(obj)
    return True


def update_email_event_subscription_v1(api):
    endpoint_result = api.event_management.update_email_event_subscription_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_email_event_subscription_v1(api, validator):
    try:
        assert is_valid_update_email_event_subscription_v1(
            validator,
            update_email_event_subscription_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_email_event_subscription_v1_default_val(api):
    endpoint_result = api.event_management.update_email_event_subscription_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_email_event_subscription_v1_default_val(api, validator):
    try:
        assert is_valid_update_email_event_subscription_v1(
            validator,
            update_email_event_subscription_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_email_event_subscriptions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bc212b5ee1f252479f35e8dd58319f17_v3_1_3_0').validate(obj)
    return True


def get_email_event_subscriptions_v1(api):
    endpoint_result = api.event_management.get_email_event_subscriptions_v1(
        category='string',
        domain='string',
        event_ids='string',
        limit=0,
        name='string',
        offset=0,
        order='string',
        sort_by='string',
        sub_domain='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_email_event_subscriptions_v1(api, validator):
    try:
        assert is_valid_get_email_event_subscriptions_v1(
            validator,
            get_email_event_subscriptions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_email_event_subscriptions_v1_default_val(api):
    endpoint_result = api.event_management.get_email_event_subscriptions_v1(
        category=None,
        domain=None,
        event_ids=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        sort_by=None,
        sub_domain=None,
        type=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_email_event_subscriptions_v1_default_val(api, validator):
    try:
        assert is_valid_get_email_event_subscriptions_v1(
            validator,
            get_email_event_subscriptions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_rest_webhook_event_subscription_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9f41eb48a0da56949cfaddeecb51ab66_v3_1_3_0').validate(obj)
    return True


def create_rest_webhook_event_subscription_v1(api):
    endpoint_result = api.event_management.create_rest_webhook_event_subscription_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_rest_webhook_event_subscription_v1(api, validator):
    try:
        assert is_valid_create_rest_webhook_event_subscription_v1(
            validator,
            create_rest_webhook_event_subscription_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_rest_webhook_event_subscription_v1_default_val(api):
    endpoint_result = api.event_management.create_rest_webhook_event_subscription_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_rest_webhook_event_subscription_v1_default_val(api, validator):
    try:
        assert is_valid_create_rest_webhook_event_subscription_v1(
            validator,
            create_rest_webhook_event_subscription_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_rest_webhook_event_subscriptions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1ee2008494d158e7bff7f106519a64c5_v3_1_3_0').validate(obj)
    return True


def get_rest_webhook_event_subscriptions_v1(api):
    endpoint_result = api.event_management.get_rest_webhook_event_subscriptions_v1(
        category='string',
        domain='string',
        event_ids='string',
        limit=0,
        name='string',
        offset=0,
        order='string',
        sort_by='string',
        sub_domain='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_rest_webhook_event_subscriptions_v1(api, validator):
    try:
        assert is_valid_get_rest_webhook_event_subscriptions_v1(
            validator,
            get_rest_webhook_event_subscriptions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_rest_webhook_event_subscriptions_v1_default_val(api):
    endpoint_result = api.event_management.get_rest_webhook_event_subscriptions_v1(
        category=None,
        domain=None,
        event_ids=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        sort_by=None,
        sub_domain=None,
        type=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_rest_webhook_event_subscriptions_v1_default_val(api, validator):
    try:
        assert is_valid_get_rest_webhook_event_subscriptions_v1(
            validator,
            get_rest_webhook_event_subscriptions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_rest_webhook_event_subscription_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7474456b6581534bb321eaea272365b7_v3_1_3_0').validate(obj)
    return True


def update_rest_webhook_event_subscription_v1(api):
    endpoint_result = api.event_management.update_rest_webhook_event_subscription_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_rest_webhook_event_subscription_v1(api, validator):
    try:
        assert is_valid_update_rest_webhook_event_subscription_v1(
            validator,
            update_rest_webhook_event_subscription_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_rest_webhook_event_subscription_v1_default_val(api):
    endpoint_result = api.event_management.update_rest_webhook_event_subscription_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_rest_webhook_event_subscription_v1_default_val(api, validator):
    try:
        assert is_valid_update_rest_webhook_event_subscription_v1(
            validator,
            update_rest_webhook_event_subscription_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_syslog_event_subscription_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8d8fc92ddeab597ebb50ea003a6d46bd_v3_1_3_0').validate(obj)
    return True


def update_syslog_event_subscription_v1(api):
    endpoint_result = api.event_management.update_syslog_event_subscription_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_syslog_event_subscription_v1(api, validator):
    try:
        assert is_valid_update_syslog_event_subscription_v1(
            validator,
            update_syslog_event_subscription_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_syslog_event_subscription_v1_default_val(api):
    endpoint_result = api.event_management.update_syslog_event_subscription_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_syslog_event_subscription_v1_default_val(api, validator):
    try:
        assert is_valid_update_syslog_event_subscription_v1(
            validator,
            update_syslog_event_subscription_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_syslog_event_subscription_v1(json_schema_validate, obj):
    json_schema_validate('jsd_99fb5a8c0075563491622171958074bf_v3_1_3_0').validate(obj)
    return True


def create_syslog_event_subscription_v1(api):
    endpoint_result = api.event_management.create_syslog_event_subscription_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_syslog_event_subscription_v1(api, validator):
    try:
        assert is_valid_create_syslog_event_subscription_v1(
            validator,
            create_syslog_event_subscription_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_syslog_event_subscription_v1_default_val(api):
    endpoint_result = api.event_management.create_syslog_event_subscription_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_syslog_event_subscription_v1_default_val(api, validator):
    try:
        assert is_valid_create_syslog_event_subscription_v1(
            validator,
            create_syslog_event_subscription_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_syslog_event_subscriptions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c7bed4b4148753e6bc9912e3be135217_v3_1_3_0').validate(obj)
    return True


def get_syslog_event_subscriptions_v1(api):
    endpoint_result = api.event_management.get_syslog_event_subscriptions_v1(
        category='string',
        domain='string',
        event_ids='string',
        limit=0,
        name='string',
        offset=0,
        order='string',
        sort_by='string',
        sub_domain='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_syslog_event_subscriptions_v1(api, validator):
    try:
        assert is_valid_get_syslog_event_subscriptions_v1(
            validator,
            get_syslog_event_subscriptions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_syslog_event_subscriptions_v1_default_val(api):
    endpoint_result = api.event_management.get_syslog_event_subscriptions_v1(
        category=None,
        domain=None,
        event_ids=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        sort_by=None,
        sub_domain=None,
        type=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_syslog_event_subscriptions_v1_default_val(api, validator):
    try:
        assert is_valid_get_syslog_event_subscriptions_v1(
            validator,
            get_syslog_event_subscriptions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_syslog_destination_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6a9f5796226051218eac559ab5211384_v3_1_3_0').validate(obj)
    return True


def update_syslog_destination_v1(api):
    endpoint_result = api.event_management.update_syslog_destination_v1(
        active_validation=True,
        configId='string',
        description='string',
        host='string',
        name='string',
        payload=None,
        port=0,
        protocol='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_syslog_destination_v1(api, validator):
    try:
        assert is_valid_update_syslog_destination_v1(
            validator,
            update_syslog_destination_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_syslog_destination_v1_default_val(api):
    endpoint_result = api.event_management.update_syslog_destination_v1(
        active_validation=True,
        configId=None,
        description=None,
        host=None,
        name=None,
        payload=None,
        port=None,
        protocol=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_syslog_destination_v1_default_val(api, validator):
    try:
        assert is_valid_update_syslog_destination_v1(
            validator,
            update_syslog_destination_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_syslog_destination_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a170168de2ac55cc93571af1fbc02894_v3_1_3_0').validate(obj)
    return True


def get_syslog_destination_v1(api):
    endpoint_result = api.event_management.get_syslog_destination_v1(
        config_id='string',
        limit=0,
        name='string',
        offset=0,
        order='string',
        protocol='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_syslog_destination_v1(api, validator):
    try:
        assert is_valid_get_syslog_destination_v1(
            validator,
            get_syslog_destination_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_syslog_destination_v1_default_val(api):
    endpoint_result = api.event_management.get_syslog_destination_v1(
        config_id=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        protocol=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_syslog_destination_v1_default_val(api, validator):
    try:
        assert is_valid_get_syslog_destination_v1(
            validator,
            get_syslog_destination_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_syslog_destination_v1(json_schema_validate, obj):
    json_schema_validate('jsd_919dece7a9b353b49084a8ffa4f18c91_v3_1_3_0').validate(obj)
    return True


def create_syslog_destination_v1(api):
    endpoint_result = api.event_management.create_syslog_destination_v1(
        active_validation=True,
        configId='string',
        description='string',
        host='string',
        name='string',
        payload=None,
        port=0,
        protocol='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_syslog_destination_v1(api, validator):
    try:
        assert is_valid_create_syslog_destination_v1(
            validator,
            create_syslog_destination_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_syslog_destination_v1_default_val(api):
    endpoint_result = api.event_management.create_syslog_destination_v1(
        active_validation=True,
        configId=None,
        description=None,
        host=None,
        name=None,
        payload=None,
        port=None,
        protocol=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_syslog_destination_v1_default_val(api, validator):
    try:
        assert is_valid_create_syslog_destination_v1(
            validator,
            create_syslog_destination_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_webhook_destination_v1(json_schema_validate, obj):
    json_schema_validate('jsd_36b8699619f95a24bd2d81f12f048235_v3_1_3_0').validate(obj)
    return True


def create_webhook_destination_v1(api):
    endpoint_result = api.event_management.create_webhook_destination_v1(
        active_validation=True,
        description='string',
        headers=[{'name': 'string', 'value': 'string', 'defaultValue': 'string', 'encrypt': True}],
        isProxyRoute=True,
        method='string',
        name='string',
        payload=None,
        trustCert=True,
        url='string',
        webhookId='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_webhook_destination_v1(api, validator):
    try:
        assert is_valid_create_webhook_destination_v1(
            validator,
            create_webhook_destination_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_webhook_destination_v1_default_val(api):
    endpoint_result = api.event_management.create_webhook_destination_v1(
        active_validation=True,
        description=None,
        headers=None,
        isProxyRoute=None,
        method=None,
        name=None,
        payload=None,
        trustCert=None,
        url=None,
        webhookId=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_webhook_destination_v1_default_val(api, validator):
    try:
        assert is_valid_create_webhook_destination_v1(
            validator,
            create_webhook_destination_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_webhook_destination_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d5c229546dc755f796dfcf34f1c2e290_v3_1_3_0').validate(obj)
    return True


def update_webhook_destination_v1(api):
    endpoint_result = api.event_management.update_webhook_destination_v1(
        active_validation=True,
        description='string',
        headers=[{'name': 'string', 'value': 'string', 'defaultValue': 'string', 'encrypt': True}],
        isProxyRoute=True,
        method='string',
        name='string',
        payload=None,
        trustCert=True,
        url='string',
        webhookId='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_webhook_destination_v1(api, validator):
    try:
        assert is_valid_update_webhook_destination_v1(
            validator,
            update_webhook_destination_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_webhook_destination_v1_default_val(api):
    endpoint_result = api.event_management.update_webhook_destination_v1(
        active_validation=True,
        description=None,
        headers=None,
        isProxyRoute=None,
        method=None,
        name=None,
        payload=None,
        trustCert=None,
        url=None,
        webhookId=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_webhook_destination_v1_default_val(api, validator):
    try:
        assert is_valid_update_webhook_destination_v1(
            validator,
            update_webhook_destination_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_webhook_destination_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ddecdd64b34c5fdc910296fce09b2828_v3_1_3_0').validate(obj)
    return True


def get_webhook_destination_v1(api):
    endpoint_result = api.event_management.get_webhook_destination_v1(
        limit=0,
        offset=0,
        order='string',
        sort_by='string',
        webhook_ids='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_webhook_destination_v1(api, validator):
    try:
        assert is_valid_get_webhook_destination_v1(
            validator,
            get_webhook_destination_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_webhook_destination_v1_default_val(api):
    endpoint_result = api.event_management.get_webhook_destination_v1(
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        webhook_ids=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_webhook_destination_v1_default_val(api, validator):
    try:
        assert is_valid_get_webhook_destination_v1(
            validator,
            get_webhook_destination_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_events_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bf36f1819e61575189c0709efab6e48a_v3_1_3_0').validate(obj)
    return True


def get_events_v1(api):
    endpoint_result = api.event_management.get_events_v1(
        event_id='string',
        limit=0,
        offset=0,
        order='string',
        sort_by='string',
        tags='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_events_v1(api, validator):
    try:
        assert is_valid_get_events_v1(
            validator,
            get_events_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_events_v1_default_val(api):
    endpoint_result = api.event_management.get_events_v1(
        event_id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        tags=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_events_v1_default_val(api, validator):
    try:
        assert is_valid_get_events_v1(
            validator,
            get_events_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_of_events_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3b21d2947d715c198f5e62ba3149839a_v3_1_3_0').validate(obj)
    return True


def count_of_events_v1(api):
    endpoint_result = api.event_management.count_of_events_v1(
        event_id='string',
        tags='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_events_v1(api, validator):
    try:
        assert is_valid_count_of_events_v1(
            validator,
            count_of_events_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_of_events_v1_default_val(api):
    endpoint_result = api.event_management.count_of_events_v1(
        event_id=None,
        tags=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_events_v1_default_val(api, validator):
    try:
        assert is_valid_count_of_events_v1(
            validator,
            count_of_events_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_eventartifacts(json_schema_validate, obj):
    json_schema_validate('jsd_584c0e0d76b2561b8f2efd0220f02267_v3_1_3_0').validate(obj)
    return True


def get_eventartifacts(api):
    endpoint_result = api.event_management.get_eventartifacts(
        event_ids='string',
        limit=0,
        offset=0,
        order='string',
        search='string',
        sort_by='string',
        tags='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_eventartifacts(api, validator):
    try:
        assert is_valid_get_eventartifacts(
            validator,
            get_eventartifacts(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_eventartifacts_default_val(api):
    endpoint_result = api.event_management.get_eventartifacts(
        event_ids=None,
        limit=None,
        offset=None,
        order=None,
        search=None,
        sort_by=None,
        tags=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_eventartifacts_default_val(api, validator):
    try:
        assert is_valid_get_eventartifacts(
            validator,
            get_eventartifacts_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_eventartifact_count(json_schema_validate, obj):
    json_schema_validate('jsd_a137e0b583c85ffe80fbbd85b480bf15_v3_1_3_0').validate(obj)
    return True


def eventartifact_count(api):
    endpoint_result = api.event_management.eventartifact_count(

    )
    return endpoint_result


@pytest.mark.event_management
def test_eventartifact_count(api, validator):
    try:
        assert is_valid_eventartifact_count(
            validator,
            eventartifact_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def eventartifact_count_default_val(api):
    endpoint_result = api.event_management.eventartifact_count(

    )
    return endpoint_result


@pytest.mark.event_management
def test_eventartifact_count_default_val(api, validator):
    try:
        assert is_valid_eventartifact_count(
            validator,
            eventartifact_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_connector_types_v1(json_schema_validate, obj):
    json_schema_validate('jsd_632352b94cfb5af084c1a65d8e51df71_v3_1_3_0').validate(obj)
    return True


def get_connector_types_v1(api):
    endpoint_result = api.event_management.get_connector_types_v1(

    )
    return endpoint_result


@pytest.mark.event_management
def test_get_connector_types_v1(api, validator):
    try:
        assert is_valid_get_connector_types_v1(
            validator,
            get_connector_types_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_connector_types_v1_default_val(api):
    endpoint_result = api.event_management.get_connector_types_v1(

    )
    return endpoint_result


@pytest.mark.event_management
def test_get_connector_types_v1_default_val(api, validator):
    try:
        assert is_valid_get_connector_types_v1(
            validator,
            get_connector_types_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

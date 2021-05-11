# -*- coding: utf-8 -*-
"""DNACenterAPI event_management API fixtures and tests.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.1', reason='version does not match')


def is_valid_count_of_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_149b7ba04e5890b2_v2_2_1').validate(obj)
    return True


def count_of_event_subscriptions(api):
    endpoint_result = api.event_management.count_of_event_subscriptions(
        event_ids='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_event_subscriptions(api, validator):
    assert is_valid_count_of_event_subscriptions(
        validator,
        count_of_event_subscriptions(api)
    )


def count_of_event_subscriptions_default(api):
    endpoint_result = api.event_management.count_of_event_subscriptions(
        event_ids=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_event_subscriptions_default(api, validator):
    try:
        assert is_valid_count_of_event_subscriptions(
            validator,
            count_of_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_count_of_notifications(json_schema_validate, obj):
    json_schema_validate('jsd_0eb8faf742aaabb7_v2_2_1').validate(obj)
    return True


def count_of_notifications(api):
    endpoint_result = api.event_management.count_of_notifications(
        category='string',
        domain='string',
        end_time=0,
        event_ids=' ',
        severity='string',
        source='string',
        start_time=0,
        sub_domain='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_notifications(api, validator):
    assert is_valid_count_of_notifications(
        validator,
        count_of_notifications(api)
    )


def count_of_notifications_default(api):
    endpoint_result = api.event_management.count_of_notifications(
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
def test_count_of_notifications_default(api, validator):
    try:
        assert is_valid_count_of_notifications(
            validator,
            count_of_notifications_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_syslog_subscription_details(json_schema_validate, obj):
    json_schema_validate('jsd_17855b4e4e69a497_v2_2_1').validate(obj)
    return True


def get_syslog_subscription_details(api):
    endpoint_result = api.event_management.get_syslog_subscription_details(
        connector_type=' SYSLOG',
        instance_id='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_syslog_subscription_details(api, validator):
    assert is_valid_get_syslog_subscription_details(
        validator,
        get_syslog_subscription_details(api)
    )


def get_syslog_subscription_details_default(api):
    endpoint_result = api.event_management.get_syslog_subscription_details(
        connector_type=None,
        instance_id=None,
        name=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_syslog_subscription_details_default(api, validator):
    try:
        assert is_valid_get_syslog_subscription_details(
            validator,
            get_syslog_subscription_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_email_subscription_details(json_schema_validate, obj):
    json_schema_validate('jsd_339fd9f54719a410_v2_2_1').validate(obj)
    return True


def get_email_subscription_details(api):
    endpoint_result = api.event_management.get_email_subscription_details(
        connector_type=' EMAIL',
        instance_id='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_email_subscription_details(api, validator):
    assert is_valid_get_email_subscription_details(
        validator,
        get_email_subscription_details(api)
    )


def get_email_subscription_details_default(api):
    endpoint_result = api.event_management.get_email_subscription_details(
        connector_type=None,
        instance_id=None,
        name=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_email_subscription_details_default(api, validator):
    try:
        assert is_valid_get_email_subscription_details(
            validator,
            get_email_subscription_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_email_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_39b208514b39837e_v2_2_1').validate(obj)
    return True


def get_email_event_subscriptions(api):
    endpoint_result = api.event_management.get_email_event_subscriptions(
        event_ids='string',
        limit=10,
        offset=0,
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_email_event_subscriptions(api, validator):
    assert is_valid_get_email_event_subscriptions(
        validator,
        get_email_event_subscriptions(api)
    )


def get_email_event_subscriptions_default(api):
    endpoint_result = api.event_management.get_email_event_subscriptions(
        event_ids=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_email_event_subscriptions_default(api, validator):
    try:
        assert is_valid_get_email_event_subscriptions(
            validator,
            get_email_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_events(json_schema_validate, obj):
    json_schema_validate('jsd_44a39a074a6a82a2_v2_2_1').validate(obj)
    return True


def get_events(api):
    endpoint_result = api.event_management.get_events(
        event_id=' ',
        limit=10,
        offset=0,
        order='string',
        sort_by='string',
        tags='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_events(api, validator):
    assert is_valid_get_events(
        validator,
        get_events(api)
    )


def get_events_default(api):
    endpoint_result = api.event_management.get_events(
        event_id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        tags=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_events_default(api, validator):
    try:
        assert is_valid_get_events(
            validator,
            get_events_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_auditlog_summary(json_schema_validate, obj):
    json_schema_validate('jsd_4a87484a4df9819e_v2_2_1').validate(obj)
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
        is_parent_only=False,
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
    assert is_valid_get_auditlog_summary(
        validator,
        get_auditlog_summary(api)
    )


def get_auditlog_summary_default(api):
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
def test_get_auditlog_summary_default(api, validator):
    try:
        assert is_valid_get_auditlog_summary(
            validator,
            get_auditlog_summary_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_4f9f7a7b40f990de_v2_2_1').validate(obj)
    return True


def create_event_subscriptions(api):
    endpoint_result = api.event_management.create_event_subscriptions(
        active_validation=True,
        payload=[{'subscriptionId': 'string', 'version': 'string', 'name': 'string', 'description': 'string', 'subscriptionEndpoints': [{'instanceId': 'string', 'subscriptionDetails': {'name': 'string', 'url': 'string', 'method': 'string', 'connectorType': 'string'}}], 'filter': {'eventIds': ['string']}}]
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_event_subscriptions(api, validator):
    assert is_valid_create_event_subscriptions(
        validator,
        create_event_subscriptions(api)
    )


def create_event_subscriptions_default(api):
    endpoint_result = api.event_management.create_event_subscriptions(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_event_subscriptions_default(api, validator):
    try:
        assert is_valid_create_event_subscriptions(
            validator,
            create_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_579a6a7248cb94cf_v2_2_1').validate(obj)
    return True


def update_event_subscriptions(api):
    endpoint_result = api.event_management.update_event_subscriptions(
        active_validation=True,
        payload=[{'subscriptionId': 'string', 'version': 'string', 'name': 'string', 'description': 'string', 'subscriptionEndpoints': [{'instanceId': 'string', 'subscriptionDetails': {'name': 'string', 'url': 'string', 'method': 'string', 'connectorType': 'string'}}], 'filter': {'eventIds': ['string']}}]
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_event_subscriptions(api, validator):
    assert is_valid_update_event_subscriptions(
        validator,
        update_event_subscriptions(api)
    )


def update_event_subscriptions_default(api):
    endpoint_result = api.event_management.update_event_subscriptions(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_event_subscriptions_default(api, validator):
    try:
        assert is_valid_update_event_subscriptions(
            validator,
            update_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_syslog_event_subscription(json_schema_validate, obj):
    json_schema_validate('jsd_6285cbc140399ace_v2_2_1').validate(obj)
    return True


def update_syslog_event_subscription(api):
    endpoint_result = api.event_management.update_syslog_event_subscription(
        active_validation=True,
        payload=[{'subscriptionId': 'string', 'version': 'string', 'name': 'string', 'description': 'string', 'subscriptionEndpoints': [{'instanceId': 'string', 'subscriptionDetails': {'connectorType': 'string'}}], 'filter': {'eventIds': ['string']}}]
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_syslog_event_subscription(api, validator):
    assert is_valid_update_syslog_event_subscription(
        validator,
        update_syslog_event_subscription(api)
    )


def update_syslog_event_subscription_default(api):
    endpoint_result = api.event_management.update_syslog_event_subscription(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_syslog_event_subscription_default(api, validator):
    try:
        assert is_valid_update_syslog_event_subscription(
            validator,
            update_syslog_event_subscription_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_count_of_events(json_schema_validate, obj):
    json_schema_validate('jsd_6a9edac149ba86cf_v2_2_1').validate(obj)
    return True


def count_of_events(api):
    endpoint_result = api.event_management.count_of_events(
        event_id='string',
        tags='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_events(api, validator):
    assert is_valid_count_of_events(
        validator,
        count_of_events(api)
    )


def count_of_events_default(api):
    endpoint_result = api.event_management.count_of_events(
        event_id=None,
        tags=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_events_default(api, validator):
    try:
        assert is_valid_count_of_events(
            validator,
            count_of_events_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_eventartifacts(json_schema_validate, obj):
    json_schema_validate('jsd_73b1d8324c98bc22_v2_2_1').validate(obj)
    return True


def get_eventartifacts(api):
    endpoint_result = api.event_management.get_eventartifacts(
        event_ids='string',
        limit=10,
        offset=0,
        order='string',
        search='string',
        sort_by='string',
        tags='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_eventartifacts(api, validator):
    assert is_valid_get_eventartifacts(
        validator,
        get_eventartifacts(api)
    )


def get_eventartifacts_default(api):
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
def test_get_eventartifacts_default(api, validator):
    try:
        assert is_valid_get_eventartifacts(
            validator,
            get_eventartifacts_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_email_event_subscription(json_schema_validate, obj):
    json_schema_validate('jsd_7bbc88c8424a840f_v2_2_1').validate(obj)
    return True


def create_email_event_subscription(api):
    endpoint_result = api.event_management.create_email_event_subscription(
        active_validation=True,
        payload=[{'subscriptionId': 'string', 'version': 'string', 'name': 'string', 'description': 'string', 'subscriptionEndpoints': [{'instanceId': 'string', 'subscriptionDetails': {'connectorType': 'string', 'fromEmailAddress': 'string', 'toEmailAddresses': ['string'], 'subject': 'string'}}], 'filter': {'eventIds': ['string']}}]
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_email_event_subscription(api, validator):
    assert is_valid_create_email_event_subscription(
        validator,
        create_email_event_subscription(api)
    )


def create_email_event_subscription_default(api):
    endpoint_result = api.event_management.create_email_event_subscription(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_email_event_subscription_default(api, validator):
    try:
        assert is_valid_create_email_event_subscription(
            validator,
            create_email_event_subscription_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_notifications(json_schema_validate, obj):
    json_schema_validate('jsd_84999b564afb8657_v2_2_1').validate(obj)
    return True


def get_notifications(api):
    endpoint_result = api.event_management.get_notifications(
        category='string',
        domain='string',
        end_time=0,
        event_ids=' ',
        limit=10,
        offset=0,
        order='string',
        severity='string',
        sort_by='string',
        source='string',
        start_time=0,
        sub_domain='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_notifications(api, validator):
    assert is_valid_get_notifications(
        validator,
        get_notifications(api)
    )


def get_notifications_default(api):
    endpoint_result = api.event_management.get_notifications(
        category=None,
        domain=None,
        end_time=None,
        event_ids=None,
        limit=None,
        offset=None,
        order=None,
        severity=None,
        sort_by=None,
        source=None,
        start_time=None,
        sub_domain=None,
        type=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_notifications_default(api, validator):
    try:
        assert is_valid_get_notifications(
            validator,
            get_notifications_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_auditlog_records(json_schema_validate, obj):
    json_schema_validate('jsd_89a9fafb4d49bd86_v2_2_1').validate(obj)
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
        limit=25,
        name='string',
        offset=0,
        order='desc',
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
    assert is_valid_get_auditlog_records(
        validator,
        get_auditlog_records(api)
    )


def get_auditlog_records_default(api):
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
def test_get_auditlog_records_default(api, validator):
    try:
        assert is_valid_get_auditlog_records(
            validator,
            get_auditlog_records_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_syslog_event_subscription(json_schema_validate, obj):
    json_schema_validate('jsd_919a8bb7445a88fe_v2_2_1').validate(obj)
    return True


def create_syslog_event_subscription(api):
    endpoint_result = api.event_management.create_syslog_event_subscription(
        active_validation=True,
        payload=[{'subscriptionId': 'string', 'version': 'string', 'name': 'string', 'description': 'string', 'subscriptionEndpoints': [{'instanceId': 'string', 'subscriptionDetails': {'connectorType': 'string'}}], 'filter': {'eventIds': ['string']}}]
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_syslog_event_subscription(api, validator):
    assert is_valid_create_syslog_event_subscription(
        validator,
        create_syslog_event_subscription(api)
    )


def create_syslog_event_subscription_default(api):
    endpoint_result = api.event_management.create_syslog_event_subscription(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_syslog_event_subscription_default(api, validator):
    try:
        assert is_valid_create_syslog_event_subscription(
            validator,
            create_syslog_event_subscription_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_email_event_subscription(json_schema_validate, obj):
    json_schema_validate('jsd_87b22b8346bb8983_v2_2_1').validate(obj)
    return True


def update_email_event_subscription(api):
    endpoint_result = api.event_management.update_email_event_subscription(
        active_validation=True,
        payload=[{'subscriptionId': 'string', 'version': 'string', 'name': 'string', 'description': 'string', 'subscriptionEndpoints': [{'instanceId': 'string', 'subscriptionDetails': {'connectorType': 'string', 'fromEmailAddress': 'string', 'toEmailAddresses': ['string'], 'subject': 'string'}}], 'filter': {'eventIds': ['string']}}]
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_email_event_subscription(api, validator):
    assert is_valid_update_email_event_subscription(
        validator,
        update_email_event_subscription(api)
    )


def update_email_event_subscription_default(api):
    endpoint_result = api.event_management.update_email_event_subscription(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_email_event_subscription_default(api, validator):
    try:
        assert is_valid_update_email_event_subscription(
            validator,
            update_email_event_subscription_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_rest_webhook_event_subscription(json_schema_validate, obj):
    json_schema_validate('jsd_9584d98845ebb4b0_v2_2_1').validate(obj)
    return True


def create_rest_webhook_event_subscription(api):
    endpoint_result = api.event_management.create_rest_webhook_event_subscription(
        active_validation=True,
        payload=[{'subscriptionId': 'string', 'version': 'string', 'name': 'string', 'description': 'string', 'subscriptionEndpoints': [{'instanceId': 'string', 'subscriptionDetails': {'connectorType': 'string'}}], 'filter': {'eventIds': ['string']}}]
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_rest_webhook_event_subscription(api, validator):
    assert is_valid_create_rest_webhook_event_subscription(
        validator,
        create_rest_webhook_event_subscription(api)
    )


def create_rest_webhook_event_subscription_default(api):
    endpoint_result = api.event_management.create_rest_webhook_event_subscription(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_rest_webhook_event_subscription_default(api, validator):
    try:
        assert is_valid_create_rest_webhook_event_subscription(
            validator,
            create_rest_webhook_event_subscription_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_93981baa40799483_v2_2_1').validate(obj)
    return True


def delete_event_subscriptions(api):
    endpoint_result = api.event_management.delete_event_subscriptions(
        subscriptions='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_delete_event_subscriptions(api, validator):
    assert is_valid_delete_event_subscriptions(
        validator,
        delete_event_subscriptions(api)
    )


def delete_event_subscriptions_default(api):
    endpoint_result = api.event_management.delete_event_subscriptions(
        subscriptions=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_delete_event_subscriptions_default(api, validator):
    try:
        assert is_valid_delete_event_subscriptions(
            validator,
            delete_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_auditlog_parent_records(json_schema_validate, obj):
    json_schema_validate('jsd_95907ae946eab1c6_v2_2_1').validate(obj)
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
        limit=25,
        name='string',
        offset=0,
        order='desc',
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
    assert is_valid_get_auditlog_parent_records(
        validator,
        get_auditlog_parent_records(api)
    )


def get_auditlog_parent_records_default(api):
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
def test_get_auditlog_parent_records_default(api, validator):
    try:
        assert is_valid_get_auditlog_parent_records(
            validator,
            get_auditlog_parent_records_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_eventartifact_count(json_schema_validate, obj):
    json_schema_validate('jsd_b78e9bf74f8a8321_v2_2_1').validate(obj)
    return True


def eventartifact_count(api):
    endpoint_result = api.event_management.eventartifact_count(

    )
    return endpoint_result


@pytest.mark.event_management
def test_eventartifact_count(api, validator):
    assert is_valid_eventartifact_count(
        validator,
        eventartifact_count(api)
    )


def eventartifact_count_default(api):
    endpoint_result = api.event_management.eventartifact_count(

    )
    return endpoint_result


@pytest.mark.event_management
def test_eventartifact_count_default(api, validator):
    try:
        assert is_valid_eventartifact_count(
            validator,
            eventartifact_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_rest_webhook_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_dcaa6bde4feb9153_v2_2_1').validate(obj)
    return True


def get_rest_webhook_event_subscriptions(api):
    endpoint_result = api.event_management.get_rest_webhook_event_subscriptions(
        event_ids='string',
        limit=10,
        offset=0,
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_rest_webhook_event_subscriptions(api, validator):
    assert is_valid_get_rest_webhook_event_subscriptions(
        validator,
        get_rest_webhook_event_subscriptions(api)
    )


def get_rest_webhook_event_subscriptions_default(api):
    endpoint_result = api.event_management.get_rest_webhook_event_subscriptions(
        event_ids=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_rest_webhook_event_subscriptions_default(api, validator):
    try:
        assert is_valid_get_rest_webhook_event_subscriptions(
            validator,
            get_rest_webhook_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_syslog_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_c5a92a5b4e6a852e_v2_2_1').validate(obj)
    return True


def get_syslog_event_subscriptions(api):
    endpoint_result = api.event_management.get_syslog_event_subscriptions(
        event_ids='string',
        limit=10,
        offset=0,
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_syslog_event_subscriptions(api, validator):
    assert is_valid_get_syslog_event_subscriptions(
        validator,
        get_syslog_event_subscriptions(api)
    )


def get_syslog_event_subscriptions_default(api):
    endpoint_result = api.event_management.get_syslog_event_subscriptions(
        event_ids=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_syslog_event_subscriptions_default(api, validator):
    try:
        assert is_valid_get_syslog_event_subscriptions(
            validator,
            get_syslog_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_rest_webhook_subscription_details(json_schema_validate, obj):
    json_schema_validate('jsd_eeb68baf4338bb23_v2_2_1').validate(obj)
    return True


def get_rest_webhook_subscription_details(api):
    endpoint_result = api.event_management.get_rest_webhook_subscription_details(
        connector_type=' REST',
        instance_id='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_rest_webhook_subscription_details(api, validator):
    assert is_valid_get_rest_webhook_subscription_details(
        validator,
        get_rest_webhook_subscription_details(api)
    )


def get_rest_webhook_subscription_details_default(api):
    endpoint_result = api.event_management.get_rest_webhook_subscription_details(
        connector_type=None,
        instance_id=None,
        name=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_rest_webhook_subscription_details_default(api, validator):
    try:
        assert is_valid_get_rest_webhook_subscription_details(
            validator,
            get_rest_webhook_subscription_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_rest_webhook_event_subscription(json_schema_validate, obj):
    json_schema_validate('jsd_ce81f9c54fc8b576_v2_2_1').validate(obj)
    return True


def update_rest_webhook_event_subscription(api):
    endpoint_result = api.event_management.update_rest_webhook_event_subscription(
        active_validation=True,
        payload=[{'subscriptionId': 'string', 'version': 'string', 'name': 'string', 'description': 'string', 'subscriptionEndpoints': [{'instanceId': 'string', 'subscriptionDetails': {'connectorType': 'string'}}], 'filter': {'eventIds': ['string']}}]
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_rest_webhook_event_subscription(api, validator):
    assert is_valid_update_rest_webhook_event_subscription(
        validator,
        update_rest_webhook_event_subscription(api)
    )


def update_rest_webhook_event_subscription_default(api):
    endpoint_result = api.event_management.update_rest_webhook_event_subscription(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_rest_webhook_event_subscription_default(api, validator):
    try:
        assert is_valid_update_rest_webhook_event_subscription(
            validator,
            update_rest_webhook_event_subscription_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_dcaa6bde4feb9152_v2_2_1').validate(obj)
    return True


def get_event_subscriptions(api):
    endpoint_result = api.event_management.get_event_subscriptions(
        event_ids='string',
        limit=10,
        offset=0,
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_event_subscriptions(api, validator):
    assert is_valid_get_event_subscriptions(
        validator,
        get_event_subscriptions(api)
    )


def get_event_subscriptions_default(api):
    endpoint_result = api.event_management.get_event_subscriptions(
        event_ids=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_event_subscriptions_default(api, validator):
    try:
        assert is_valid_get_event_subscriptions(
            validator,
            get_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_status_api_for_events(json_schema_validate, obj):
    json_schema_validate('jsd_f9bd99c74bba8832_v2_2_1').validate(obj)
    return True


def get_status_api_for_events(api):
    endpoint_result = api.event_management.get_status_api_for_events(
        execution_id='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_status_api_for_events(api, validator):
    assert is_valid_get_status_api_for_events(
        validator,
        get_status_api_for_events(api)
    )


def get_status_api_for_events_default(api):
    endpoint_result = api.event_management.get_status_api_for_events(
        execution_id='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_status_api_for_events_default(api, validator):
    try:
        assert is_valid_get_status_api_for_events(
            validator,
            get_status_api_for_events_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

# -*- coding: utf-8 -*-
"""CatalystCenterAPI application_policy API fixtures and tests.

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


def is_valid_get_application_policy(json_schema_validate, obj):
    json_schema_validate('jsd_fae4378ef4e2503f9fef4f3a4ddd4de4_v2_3_7_9').validate(obj)
    return True


def get_application_policy(api):
    endpoint_result = api.application_policy.get_application_policy(
        policy_scope='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy(api, validator):
    try:
        assert is_valid_get_application_policy(
            validator,
            get_application_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_policy_default_val(api):
    endpoint_result = api.application_policy.get_application_policy(
        policy_scope=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_default_val(api, validator):
    try:
        assert is_valid_get_application_policy(
            validator,
            get_application_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_policy_default(json_schema_validate, obj):
    json_schema_validate('jsd_9d1b2e541bb85dea8192cd474be4e3ad_v2_3_7_9').validate(obj)
    return True


def get_application_policy_default(api):
    endpoint_result = api.application_policy.get_application_policy_default(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_default(api, validator):
    try:
        assert is_valid_get_application_policy_default(
            validator,
            get_application_policy_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_policy_default_default_val(api):
    endpoint_result = api.application_policy.get_application_policy_default(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_default_default_val(api, validator):
    try:
        assert is_valid_get_application_policy_default(
            validator,
            get_application_policy_default_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_application_policy_intent(json_schema_validate, obj):
    json_schema_validate('jsd_72fa27ccbaf55711849381a707e1edfa_v2_3_7_9').validate(obj)
    return True


def application_policy_intent(api):
    endpoint_result = api.application_policy.application_policy_intent(
        active_validation=True,
        createList=[{'name': 'string', 'deletePolicyStatus': 'string', 'policyScope': 'string', 'priority': 'string', 'advancedPolicyScope': {'name': 'string', 'advancedPolicyScopeElement': [{'groupId': ['string'], 'ssid': ['string']}]}, 'exclusiveContract': {'clause': [{'type': 'string', 'relevanceLevel': 'string', 'deviceRemovalBehavior': 'string', 'hostTrackingEnabled': True}]}, 'contract': {'idRef': 'string'}, 'producer': {'scalableGroup': [{'idRef': 'string'}]}, 'consumer': {'scalableGroup': [{'idRef': 'string'}]}}],
        deleteList=['string'],
        payload=None,
        updateList=[{'id': 'string', 'name': 'string', 'deletePolicyStatus': 'string', 'policyScope': 'string', 'priority': 'string', 'advancedPolicyScope': {'id': 'string', 'name': 'string', 'advancedPolicyScopeElement': [{'id': 'string', 'groupId': ['string'], 'ssid': ['string']}]}, 'exclusiveContract': {'id': 'string', 'clause': [{'id': 'string', 'type': 'string', 'relevanceLevel': 'string', 'deviceRemovalBehavior': 'string', 'hostTrackingEnabled': True}]}, 'contract': {'idRef': 'string'}, 'producer': {'id': 'string', 'scalableGroup': [{'idRef': 'string'}]}, 'consumer': {'id': 'string', 'scalableGroup': [{'idRef': 'string'}]}}]
    )
    return endpoint_result


@pytest.mark.application_policy
def test_application_policy_intent(api, validator):
    try:
        assert is_valid_application_policy_intent(
            validator,
            application_policy_intent(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def application_policy_intent_default_val(api):
    endpoint_result = api.application_policy.application_policy_intent(
        active_validation=True,
        createList=None,
        deleteList=None,
        payload=None,
        updateList=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_application_policy_intent_default_val(api, validator):
    try:
        assert is_valid_application_policy_intent(
            validator,
            application_policy_intent_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_policy_queuing_profile(json_schema_validate, obj):
    json_schema_validate('jsd_d47102747c9e50ed9e365b1297e4188d_v2_3_7_9').validate(obj)
    return True


def get_application_policy_queuing_profile(api):
    endpoint_result = api.application_policy.get_application_policy_queuing_profile(
        name='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_queuing_profile(api, validator):
    try:
        assert is_valid_get_application_policy_queuing_profile(
            validator,
            get_application_policy_queuing_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_policy_queuing_profile_default_val(api):
    endpoint_result = api.application_policy.get_application_policy_queuing_profile(
        name=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_queuing_profile_default_val(api, validator):
    try:
        assert is_valid_get_application_policy_queuing_profile(
            validator,
            get_application_policy_queuing_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_application_policy_queuing_profile(json_schema_validate, obj):
    json_schema_validate('jsd_b11aa4de387251c794665e030fa815da_v2_3_7_9').validate(obj)
    return True


def update_application_policy_queuing_profile(api):
    endpoint_result = api.application_policy.update_application_policy_queuing_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_update_application_policy_queuing_profile(api, validator):
    try:
        assert is_valid_update_application_policy_queuing_profile(
            validator,
            update_application_policy_queuing_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_application_policy_queuing_profile_default_val(api):
    endpoint_result = api.application_policy.update_application_policy_queuing_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_update_application_policy_queuing_profile_default_val(api, validator):
    try:
        assert is_valid_update_application_policy_queuing_profile(
            validator,
            update_application_policy_queuing_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_application_policy_queuing_profile(json_schema_validate, obj):
    json_schema_validate('jsd_bd31fcbd1ecd5a2c8b812088b27bfcea_v2_3_7_9').validate(obj)
    return True


def create_application_policy_queuing_profile(api):
    endpoint_result = api.application_policy.create_application_policy_queuing_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_policy_queuing_profile(api, validator):
    try:
        assert is_valid_create_application_policy_queuing_profile(
            validator,
            create_application_policy_queuing_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_application_policy_queuing_profile_default_val(api):
    endpoint_result = api.application_policy.create_application_policy_queuing_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_policy_queuing_profile_default_val(api, validator):
    try:
        assert is_valid_create_application_policy_queuing_profile(
            validator,
            create_application_policy_queuing_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_policy_queuing_profile_count(json_schema_validate, obj):
    json_schema_validate('jsd_a22faef865d55fe48dd2467bee214518_v2_3_7_9').validate(obj)
    return True


def get_application_policy_queuing_profile_count(api):
    endpoint_result = api.application_policy.get_application_policy_queuing_profile_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_queuing_profile_count(api, validator):
    try:
        assert is_valid_get_application_policy_queuing_profile_count(
            validator,
            get_application_policy_queuing_profile_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_policy_queuing_profile_count_default_val(api):
    endpoint_result = api.application_policy.get_application_policy_queuing_profile_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_queuing_profile_count_default_val(api, validator):
    try:
        assert is_valid_get_application_policy_queuing_profile_count(
            validator,
            get_application_policy_queuing_profile_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_application_policy_queuing_profile(json_schema_validate, obj):
    json_schema_validate('jsd_ac547ee07c2c5aff983d90cf4306619d_v2_3_7_9').validate(obj)
    return True


def delete_application_policy_queuing_profile(api):
    endpoint_result = api.application_policy.delete_application_policy_queuing_profile(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_policy_queuing_profile(api, validator):
    try:
        assert is_valid_delete_application_policy_queuing_profile(
            validator,
            delete_application_policy_queuing_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_application_policy_queuing_profile_default_val(api):
    endpoint_result = api.application_policy.delete_application_policy_queuing_profile(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_policy_queuing_profile_default_val(api, validator):
    try:
        assert is_valid_delete_application_policy_queuing_profile(
            validator,
            delete_application_policy_queuing_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_sets(json_schema_validate, obj):
    json_schema_validate('jsd_8b60dbd805b95030bc2caf345a44b504_v2_3_7_9').validate(obj)
    return True


def get_application_sets(api):
    endpoint_result = api.application_policy.get_application_sets(
        limit=0,
        name='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets(api, validator):
    try:
        assert is_valid_get_application_sets(
            validator,
            get_application_sets(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_sets_default_val(api):
    endpoint_result = api.application_policy.get_application_sets(
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_default_val(api, validator):
    try:
        assert is_valid_get_application_sets(
            validator,
            get_application_sets_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_application_set(json_schema_validate, obj):
    json_schema_validate('jsd_0a59a448c5c25f1e8246d6827e6e3215_v2_3_7_9').validate(obj)
    return True


def delete_application_set(api):
    endpoint_result = api.application_policy.delete_application_set(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_set(api, validator):
    try:
        assert is_valid_delete_application_set(
            validator,
            delete_application_set(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_application_set_default_val(api):
    endpoint_result = api.application_policy.delete_application_set(
        id=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_set_default_val(api, validator):
    try:
        assert is_valid_delete_application_set(
            validator,
            delete_application_set_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_application_set(json_schema_validate, obj):
    json_schema_validate('jsd_636cb7563a5058c4801eb842a74ff61c_v2_3_7_9').validate(obj)
    return True


def create_application_set(api):
    endpoint_result = api.application_policy.create_application_set(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_set(api, validator):
    try:
        assert is_valid_create_application_set(
            validator,
            create_application_set(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_application_set_default_val(api):
    endpoint_result = api.application_policy.create_application_set(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_set_default_val(api, validator):
    try:
        assert is_valid_create_application_set(
            validator,
            create_application_set_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_sets_count(json_schema_validate, obj):
    json_schema_validate('jsd_968ebc5880945305adb41253c6e4ffec_v2_3_7_9').validate(obj)
    return True


def get_application_sets_count(api):
    endpoint_result = api.application_policy.get_application_sets_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_count(api, validator):
    try:
        assert is_valid_get_application_sets_count(
            validator,
            get_application_sets_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_sets_count_default_val(api):
    endpoint_result = api.application_policy.get_application_sets_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_count_default_val(api, validator):
    try:
        assert is_valid_get_application_sets_count(
            validator,
            get_application_sets_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_list_of_network_devices_with_their_application_visibility_status(json_schema_validate, obj):
    json_schema_validate('jsd_6899256a5b7b549ba686b2c5c1091157_v2_3_7_9').validate(obj)
    return True


def retrieve_the_list_of_network_devices_with_their_application_visibility_status(api):
    endpoint_result = api.application_policy.retrieve_the_list_of_network_devices_with_their_application_visibility_status(
        app_telemetry_deployment_status='string',
        app_telemetry_readiness_status='string',
        application_registry_sync_status='string',
        cbar_deployment_status='string',
        cbar_readiness_status='string',
        hostname='string',
        ids='string',
        limit='string',
        management_address='string',
        offset='string',
        order='string',
        protocol_pack_status='string',
        protocol_pack_update_status='string',
        site_id='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_retrieve_the_list_of_network_devices_with_their_application_visibility_status(api, validator):
    try:
        assert is_valid_retrieve_the_list_of_network_devices_with_their_application_visibility_status(
            validator,
            retrieve_the_list_of_network_devices_with_their_application_visibility_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_list_of_network_devices_with_their_application_visibility_status_default_val(api):
    endpoint_result = api.application_policy.retrieve_the_list_of_network_devices_with_their_application_visibility_status(
        app_telemetry_deployment_status=None,
        app_telemetry_readiness_status=None,
        application_registry_sync_status=None,
        cbar_deployment_status=None,
        cbar_readiness_status=None,
        hostname=None,
        ids=None,
        limit=None,
        management_address=None,
        offset=None,
        order=None,
        protocol_pack_status=None,
        protocol_pack_update_status=None,
        site_id=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_retrieve_the_list_of_network_devices_with_their_application_visibility_status_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_list_of_network_devices_with_their_application_visibility_status(
            validator,
            retrieve_the_list_of_network_devices_with_their_application_visibility_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_network_devices_for_the_given_application_visibility_status_filters(json_schema_validate, obj):
    json_schema_validate('jsd_c378266e951b51b6b15818086b9ea97a_v2_3_7_9').validate(obj)
    return True


def retrieve_the_count_of_network_devices_for_the_given_application_visibility_status_filters(api):
    endpoint_result = api.application_policy.retrieve_the_count_of_network_devices_for_the_given_application_visibility_status_filters(
        app_telemetry_deployment_status='string',
        app_telemetry_readiness_status='string',
        application_registry_sync_status='string',
        cbar_deployment_status='string',
        cbar_readiness_status='string',
        hostname='string',
        ids='string',
        management_address='string',
        protocol_pack_status='string',
        protocol_pack_update_status='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_retrieve_the_count_of_network_devices_for_the_given_application_visibility_status_filters(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_network_devices_for_the_given_application_visibility_status_filters(
            validator,
            retrieve_the_count_of_network_devices_for_the_given_application_visibility_status_filters(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_network_devices_for_the_given_application_visibility_status_filters_default_val(api):
    endpoint_result = api.application_policy.retrieve_the_count_of_network_devices_for_the_given_application_visibility_status_filters(
        app_telemetry_deployment_status=None,
        app_telemetry_readiness_status=None,
        application_registry_sync_status=None,
        cbar_deployment_status=None,
        cbar_readiness_status=None,
        hostname=None,
        ids=None,
        management_address=None,
        protocol_pack_status=None,
        protocol_pack_update_status=None,
        site_id=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_retrieve_the_count_of_network_devices_for_the_given_application_visibility_status_filters_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_network_devices_for_the_given_application_visibility_status_filters(
            validator,
            retrieve_the_count_of_network_devices_for_the_given_application_visibility_status_filters_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_disable_application_telemetry_feature_on_multiple_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_dda852745acd5ce5a97b0cfdf0de2fd2_v2_3_7_9').validate(obj)
    return True


def disable_application_telemetry_feature_on_multiple_network_devices(api):
    endpoint_result = api.application_policy.disable_application_telemetry_feature_on_multiple_network_devices(
        active_validation=True,
        networkDeviceIds=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_disable_application_telemetry_feature_on_multiple_network_devices(api, validator):
    try:
        assert is_valid_disable_application_telemetry_feature_on_multiple_network_devices(
            validator,
            disable_application_telemetry_feature_on_multiple_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def disable_application_telemetry_feature_on_multiple_network_devices_default_val(api):
    endpoint_result = api.application_policy.disable_application_telemetry_feature_on_multiple_network_devices(
        active_validation=True,
        networkDeviceIds=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_disable_application_telemetry_feature_on_multiple_network_devices_default_val(api, validator):
    try:
        assert is_valid_disable_application_telemetry_feature_on_multiple_network_devices(
            validator,
            disable_application_telemetry_feature_on_multiple_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_disable_c_b_a_r_feature_on_multiple_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_2b4635c45c3b5e44a30d84daa1d5fb69_v2_3_7_9').validate(obj)
    return True


def disable_c_b_a_r_feature_on_multiple_network_devices(api):
    endpoint_result = api.application_policy.disable_c_b_a_r_feature_on_multiple_network_devices(
        active_validation=True,
        networkDeviceIds=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_disable_c_b_a_r_feature_on_multiple_network_devices(api, validator):
    try:
        assert is_valid_disable_c_b_a_r_feature_on_multiple_network_devices(
            validator,
            disable_c_b_a_r_feature_on_multiple_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def disable_c_b_a_r_feature_on_multiple_network_devices_default_val(api):
    endpoint_result = api.application_policy.disable_c_b_a_r_feature_on_multiple_network_devices(
        active_validation=True,
        networkDeviceIds=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_disable_c_b_a_r_feature_on_multiple_network_devices_default_val(api, validator):
    try:
        assert is_valid_disable_c_b_a_r_feature_on_multiple_network_devices(
            validator,
            disable_c_b_a_r_feature_on_multiple_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_enable_application_telemetry_feature_on_multiple_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_7048648d73cd5be487a36d0a01d6cdc3_v2_3_7_9').validate(obj)
    return True


def enable_application_telemetry_feature_on_multiple_network_devices(api):
    endpoint_result = api.application_policy.enable_application_telemetry_feature_on_multiple_network_devices(
        active_validation=True,
        networkDevices=[{'id': 'string', 'includeWlanModes': ['string'], 'includeGuestSsids': True}],
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_enable_application_telemetry_feature_on_multiple_network_devices(api, validator):
    try:
        assert is_valid_enable_application_telemetry_feature_on_multiple_network_devices(
            validator,
            enable_application_telemetry_feature_on_multiple_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def enable_application_telemetry_feature_on_multiple_network_devices_default_val(api):
    endpoint_result = api.application_policy.enable_application_telemetry_feature_on_multiple_network_devices(
        active_validation=True,
        networkDevices=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_enable_application_telemetry_feature_on_multiple_network_devices_default_val(api, validator):
    try:
        assert is_valid_enable_application_telemetry_feature_on_multiple_network_devices(
            validator,
            enable_application_telemetry_feature_on_multiple_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_enable_c_b_a_r_feature_on_multiple_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_94e62749061c5aae8ecd1ccc2d315153_v2_3_7_9').validate(obj)
    return True


def enable_c_b_a_r_feature_on_multiple_network_devices(api):
    endpoint_result = api.application_policy.enable_c_b_a_r_feature_on_multiple_network_devices(
        active_validation=True,
        networkDevices=[{'id': 'string', 'excludeInterfaceIds': ['string'], 'excludeWlanModes': ['string']}],
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_enable_c_b_a_r_feature_on_multiple_network_devices(api, validator):
    try:
        assert is_valid_enable_c_b_a_r_feature_on_multiple_network_devices(
            validator,
            enable_c_b_a_r_feature_on_multiple_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def enable_c_b_a_r_feature_on_multiple_network_devices_default_val(api):
    endpoint_result = api.application_policy.enable_c_b_a_r_feature_on_multiple_network_devices(
        active_validation=True,
        networkDevices=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_enable_c_b_a_r_feature_on_multiple_network_devices_default_val(api, validator):
    try:
        assert is_valid_enable_c_b_a_r_feature_on_multiple_network_devices(
            validator,
            enable_c_b_a_r_feature_on_multiple_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_application(json_schema_validate, obj):
    json_schema_validate('jsd_e1781a990c6b5a4b895d56bcfda2b7cb_v2_3_7_9').validate(obj)
    return True


def create_application(api):
    endpoint_result = api.application_policy.create_application(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application(api, validator):
    try:
        assert is_valid_create_application(
            validator,
            create_application(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_application_default_val(api):
    endpoint_result = api.application_policy.create_application(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_default_val(api, validator):
    try:
        assert is_valid_create_application(
            validator,
            create_application_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_edit_application(json_schema_validate, obj):
    json_schema_validate('jsd_a3b37dcbe2a150bea06d9dcde1837281_v2_3_7_9').validate(obj)
    return True


def edit_application(api):
    endpoint_result = api.application_policy.edit_application(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_edit_application(api, validator):
    try:
        assert is_valid_edit_application(
            validator,
            edit_application(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def edit_application_default_val(api):
    endpoint_result = api.application_policy.edit_application(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_edit_application_default_val(api, validator):
    try:
        assert is_valid_edit_application(
            validator,
            edit_application_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_application(json_schema_validate, obj):
    json_schema_validate('jsd_d11d35f3505652b68905ddf1ee2f7e66_v2_3_7_9').validate(obj)
    return True


def delete_application(api):
    endpoint_result = api.application_policy.delete_application(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application(api, validator):
    try:
        assert is_valid_delete_application(
            validator,
            delete_application(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_application_default_val(api):
    endpoint_result = api.application_policy.delete_application(
        id=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_default_val(api, validator):
    try:
        assert is_valid_delete_application(
            validator,
            delete_application_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_applications(json_schema_validate, obj):
    json_schema_validate('jsd_5b12cdd3a75c51258c9e051e84189f92_v2_3_7_9').validate(obj)
    return True


def get_applications(api):
    endpoint_result = api.application_policy.get_applications(
        limit=0,
        name='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications(api, validator):
    try:
        assert is_valid_get_applications(
            validator,
            get_applications(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_applications_default_val(api):
    endpoint_result = api.application_policy.get_applications(
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_default_val(api, validator):
    try:
        assert is_valid_get_applications(
            validator,
            get_applications_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_applications_count(json_schema_validate, obj):
    json_schema_validate('jsd_30af5f0aa1ed56ab9b98eb602dbd8366_v2_3_7_9').validate(obj)
    return True


def get_applications_count(api):
    endpoint_result = api.application_policy.get_applications_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_count(api, validator):
    try:
        assert is_valid_get_applications_count(
            validator,
            get_applications_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_applications_count_default_val(api):
    endpoint_result = api.application_policy.get_applications_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_count_default_val(api, validator):
    try:
        assert is_valid_get_applications_count(
            validator,
            get_applications_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_qos_device_interface_info(json_schema_validate, obj):
    json_schema_validate('jsd_56001c37a46857f0bee5eba0a514091c_v2_3_7_9').validate(obj)
    return True


def get_qos_device_interface_info(api):
    endpoint_result = api.application_policy.get_qos_device_interface_info(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_qos_device_interface_info(api, validator):
    try:
        assert is_valid_get_qos_device_interface_info(
            validator,
            get_qos_device_interface_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_qos_device_interface_info_default_val(api):
    endpoint_result = api.application_policy.get_qos_device_interface_info(
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_qos_device_interface_info_default_val(api, validator):
    try:
        assert is_valid_get_qos_device_interface_info(
            validator,
            get_qos_device_interface_info_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_qos_device_interface_info(json_schema_validate, obj):
    json_schema_validate('jsd_ea59df3daf2a57a0b48044cc49c8a1ca_v2_3_7_9').validate(obj)
    return True


def update_qos_device_interface_info(api):
    endpoint_result = api.application_policy.update_qos_device_interface_info(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_update_qos_device_interface_info(api, validator):
    try:
        assert is_valid_update_qos_device_interface_info(
            validator,
            update_qos_device_interface_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_qos_device_interface_info_default_val(api):
    endpoint_result = api.application_policy.update_qos_device_interface_info(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_update_qos_device_interface_info_default_val(api, validator):
    try:
        assert is_valid_update_qos_device_interface_info(
            validator,
            update_qos_device_interface_info_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_qos_device_interface_info(json_schema_validate, obj):
    json_schema_validate('jsd_d045d18062ad5ae59c6f446beb17d675_v2_3_7_9').validate(obj)
    return True


def create_qos_device_interface_info(api):
    endpoint_result = api.application_policy.create_qos_device_interface_info(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_qos_device_interface_info(api, validator):
    try:
        assert is_valid_create_qos_device_interface_info(
            validator,
            create_qos_device_interface_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_qos_device_interface_info_default_val(api):
    endpoint_result = api.application_policy.create_qos_device_interface_info(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_qos_device_interface_info_default_val(api, validator):
    try:
        assert is_valid_create_qos_device_interface_info(
            validator,
            create_qos_device_interface_info_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_qos_device_interface_info_count(json_schema_validate, obj):
    json_schema_validate('jsd_6349b98fe15b531dbb7e20c0f5fa61ab_v2_3_7_9').validate(obj)
    return True


def get_qos_device_interface_info_count(api):
    endpoint_result = api.application_policy.get_qos_device_interface_info_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_qos_device_interface_info_count(api, validator):
    try:
        assert is_valid_get_qos_device_interface_info_count(
            validator,
            get_qos_device_interface_info_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_qos_device_interface_info_count_default_val(api):
    endpoint_result = api.application_policy.get_qos_device_interface_info_count(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_qos_device_interface_info_count_default_val(api, validator):
    try:
        assert is_valid_get_qos_device_interface_info_count(
            validator,
            get_qos_device_interface_info_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_qos_device_interface_info(json_schema_validate, obj):
    json_schema_validate('jsd_629a6a5bb5935709b03d0fc37a1d47d4_v2_3_7_9').validate(obj)
    return True


def delete_qos_device_interface_info(api):
    endpoint_result = api.application_policy.delete_qos_device_interface_info(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_qos_device_interface_info(api, validator):
    try:
        assert is_valid_delete_qos_device_interface_info(
            validator,
            delete_qos_device_interface_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_qos_device_interface_info_default_val(api):
    endpoint_result = api.application_policy.delete_qos_device_interface_info(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_qos_device_interface_info_default_val(api, validator):
    try:
        assert is_valid_delete_qos_device_interface_info(
            validator,
            delete_qos_device_interface_info_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_application_qo_s_policy_setting(json_schema_validate, obj):
    json_schema_validate('jsd_428094d3c8a459b787b55338701d8b33_v2_3_7_9').validate(obj)
    return True


def retrieves_the_application_qo_s_policy_setting(api):
    endpoint_result = api.application_policy.retrieves_the_application_qo_s_policy_setting(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_retrieves_the_application_qo_s_policy_setting(api, validator):
    try:
        assert is_valid_retrieves_the_application_qo_s_policy_setting(
            validator,
            retrieves_the_application_qo_s_policy_setting(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_application_qo_s_policy_setting_default_val(api):
    endpoint_result = api.application_policy.retrieves_the_application_qo_s_policy_setting(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_retrieves_the_application_qo_s_policy_setting_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_application_qo_s_policy_setting(
            validator,
            retrieves_the_application_qo_s_policy_setting_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_the_application_qo_s_policy_setting(json_schema_validate, obj):
    json_schema_validate('jsd_3bc9716ed6eb5c6e9ecb0380501d6138_v2_3_7_9').validate(obj)
    return True


def updates_the_application_qo_s_policy_setting(api):
    endpoint_result = api.application_policy.updates_the_application_qo_s_policy_setting(
        active_validation=True,
        deployByDefaultOnWiredDevices=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_updates_the_application_qo_s_policy_setting(api, validator):
    try:
        assert is_valid_updates_the_application_qo_s_policy_setting(
            validator,
            updates_the_application_qo_s_policy_setting(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_the_application_qo_s_policy_setting_default_val(api):
    endpoint_result = api.application_policy.updates_the_application_qo_s_policy_setting(
        active_validation=True,
        deployByDefaultOnWiredDevices=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_updates_the_application_qo_s_policy_setting_default_val(api, validator):
    try:
        assert is_valid_updates_the_application_qo_s_policy_setting(
            validator,
            updates_the_application_qo_s_policy_setting_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_application_sets_v2(json_schema_validate, obj):
    json_schema_validate('jsd_01e4d208b5545f66bf0f94a155c81f46_v2_3_7_9').validate(obj)
    return True


def create_application_sets_v2(api):
    endpoint_result = api.application_policy.create_application_sets_v2(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_sets_v2(api, validator):
    try:
        assert is_valid_create_application_sets_v2(
            validator,
            create_application_sets_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_application_sets_v2_default_val(api):
    endpoint_result = api.application_policy.create_application_sets_v2(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_sets_v2_default_val(api, validator):
    try:
        assert is_valid_create_application_sets_v2(
            validator,
            create_application_sets_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_sets_v2(json_schema_validate, obj):
    json_schema_validate('jsd_b399a8f895b65f3d91926da8508a9295_v2_3_7_9').validate(obj)
    return True


def get_application_sets_v2(api):
    endpoint_result = api.application_policy.get_application_sets_v2(
        attributes='string',
        limit=0,
        name='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_v2(api, validator):
    try:
        assert is_valid_get_application_sets_v2(
            validator,
            get_application_sets_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_sets_v2_default_val(api):
    endpoint_result = api.application_policy.get_application_sets_v2(
        attributes=None,
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_v2_default_val(api, validator):
    try:
        assert is_valid_get_application_sets_v2(
            validator,
            get_application_sets_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_set_count_v2(json_schema_validate, obj):
    json_schema_validate('jsd_8c3f0e5c233a5cc39969fdcff6e0288e_v2_3_7_9').validate(obj)
    return True


def get_application_set_count_v2(api):
    endpoint_result = api.application_policy.get_application_set_count_v2(
        scalable_group_type='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_set_count_v2(api, validator):
    try:
        assert is_valid_get_application_set_count_v2(
            validator,
            get_application_set_count_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_set_count_v2_default_val(api):
    endpoint_result = api.application_policy.get_application_set_count_v2(
        scalable_group_type=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_set_count_v2_default_val(api, validator):
    try:
        assert is_valid_get_application_set_count_v2(
            validator,
            get_application_set_count_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_application_set_v2(json_schema_validate, obj):
    json_schema_validate('jsd_1fbef625d3225c1eb6db93289a11a33e_v2_3_7_9').validate(obj)
    return True


def delete_application_set_v2(api):
    endpoint_result = api.application_policy.delete_application_set_v2(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_set_v2(api, validator):
    try:
        assert is_valid_delete_application_set_v2(
            validator,
            delete_application_set_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_application_set_v2_default_val(api):
    endpoint_result = api.application_policy.delete_application_set_v2(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_set_v2_default_val(api, validator):
    try:
        assert is_valid_delete_application_set_v2(
            validator,
            delete_application_set_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_edit_applications_v2(json_schema_validate, obj):
    json_schema_validate('jsd_3662b46a141650debf5946262e8a0961_v2_3_7_9').validate(obj)
    return True


def edit_applications_v2(api):
    endpoint_result = api.application_policy.edit_applications_v2(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_edit_applications_v2(api, validator):
    try:
        assert is_valid_edit_applications_v2(
            validator,
            edit_applications_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def edit_applications_v2_default_val(api):
    endpoint_result = api.application_policy.edit_applications_v2(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_edit_applications_v2_default_val(api, validator):
    try:
        assert is_valid_edit_applications_v2(
            validator,
            edit_applications_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_applications_v2(json_schema_validate, obj):
    json_schema_validate('jsd_a14e71c1b98e51eea41255720025b519_v2_3_7_9').validate(obj)
    return True


def create_applications_v2(api):
    endpoint_result = api.application_policy.create_applications_v2(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_applications_v2(api, validator):
    try:
        assert is_valid_create_applications_v2(
            validator,
            create_applications_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_applications_v2_default_val(api):
    endpoint_result = api.application_policy.create_applications_v2(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_applications_v2_default_val(api, validator):
    try:
        assert is_valid_create_applications_v2(
            validator,
            create_applications_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_applications_v2(json_schema_validate, obj):
    json_schema_validate('jsd_645981f8a81055328e2c77f0dcb60a68_v2_3_7_9').validate(obj)
    return True


def get_applications_v2(api):
    endpoint_result = api.application_policy.get_applications_v2(
        attributes='string',
        limit=0,
        name='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_v2(api, validator):
    try:
        assert is_valid_get_applications_v2(
            validator,
            get_applications_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_applications_v2_default_val(api):
    endpoint_result = api.application_policy.get_applications_v2(
        attributes=None,
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_v2_default_val(api, validator):
    try:
        assert is_valid_get_applications_v2(
            validator,
            get_applications_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_count_v2(json_schema_validate, obj):
    json_schema_validate('jsd_d4d0a63b02ed518a95fe297b2a566f1d_v2_3_7_9').validate(obj)
    return True


def get_application_count_v2(api):
    endpoint_result = api.application_policy.get_application_count_v2(
        scalable_group_type='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_count_v2(api, validator):
    try:
        assert is_valid_get_application_count_v2(
            validator,
            get_application_count_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_count_v2_default_val(api):
    endpoint_result = api.application_policy.get_application_count_v2(
        scalable_group_type=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_count_v2_default_val(api, validator):
    try:
        assert is_valid_get_application_count_v2(
            validator,
            get_application_count_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_application_v2(json_schema_validate, obj):
    json_schema_validate('jsd_ef849b2f5415501086635693a458e69b_v2_3_7_9').validate(obj)
    return True


def delete_application_v2(api):
    endpoint_result = api.application_policy.delete_application_v2(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_v2(api, validator):
    try:
        assert is_valid_delete_application_v2(
            validator,
            delete_application_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_application_v2_default_val(api):
    endpoint_result = api.application_policy.delete_application_v2(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_v2_default_val(api, validator):
    try:
        assert is_valid_delete_application_v2(
            validator,
            delete_application_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

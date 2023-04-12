# -*- coding: utf-8 -*-
"""DNACenterAPI application_policy API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.5.3', reason='version does not match')


def is_valid_get_application_policy(json_schema_validate, obj):
    json_schema_validate('jsd_fae4378ef4e2503f9fef4f3a4ddd4de4_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_9d1b2e541bb85dea8192cd474be4e3ad_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_72fa27ccbaf55711849381a707e1edfa_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_d47102747c9e50ed9e365b1297e4188d_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_b11aa4de387251c794665e030fa815da_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_bd31fcbd1ecd5a2c8b812088b27bfcea_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_a22faef865d55fe48dd2467bee214518_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_ac547ee07c2c5aff983d90cf4306619d_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_8b60dbd805b95030bc2caf345a44b504_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_0a59a448c5c25f1e8246d6827e6e3215_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_636cb7563a5058c4801eb842a74ff61c_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_968ebc5880945305adb41253c6e4ffec_v2_3_5_3').validate(obj)
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


def is_valid_create_application(json_schema_validate, obj):
    json_schema_validate('jsd_e1781a990c6b5a4b895d56bcfda2b7cb_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_a3b37dcbe2a150bea06d9dcde1837281_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_d11d35f3505652b68905ddf1ee2f7e66_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_5b12cdd3a75c51258c9e051e84189f92_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_30af5f0aa1ed56ab9b98eb602dbd8366_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_56001c37a46857f0bee5eba0a514091c_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_ea59df3daf2a57a0b48044cc49c8a1ca_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_d045d18062ad5ae59c6f446beb17d675_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_6349b98fe15b531dbb7e20c0f5fa61ab_v2_3_5_3').validate(obj)
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
    json_schema_validate('jsd_629a6a5bb5935709b03d0fc37a1d47d4_v2_3_5_3').validate(obj)
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

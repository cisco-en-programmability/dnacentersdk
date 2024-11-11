# -*- coding: utf-8 -*-
"""DNACenterAPI application_policy API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.6', reason='version does not match')


def is_valid_get_application_policy_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fae4378ef4e2503f9fef4f3a4ddd4de4_v2_3_7_6').validate(obj)
    return True


def get_application_policy_v1(api):
    endpoint_result = api.application_policy.get_application_policy_v1(
        policy_scope='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_v1(api, validator):
    try:
        assert is_valid_get_application_policy_v1(
            validator,
            get_application_policy_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_policy_v1_default_val(api):
    endpoint_result = api.application_policy.get_application_policy_v1(
        policy_scope=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_v1_default_val(api, validator):
    try:
        assert is_valid_get_application_policy_v1(
            validator,
            get_application_policy_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_policy_default_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9d1b2e541bb85dea8192cd474be4e3ad_v2_3_7_6').validate(obj)
    return True


def get_application_policy_default_v1(api):
    endpoint_result = api.application_policy.get_application_policy_default_v1(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_default_v1(api, validator):
    try:
        assert is_valid_get_application_policy_default_v1(
            validator,
            get_application_policy_default_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_policy_default_v1_default_val(api):
    endpoint_result = api.application_policy.get_application_policy_default_v1(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_default_v1_default_val(api, validator):
    try:
        assert is_valid_get_application_policy_default_v1(
            validator,
            get_application_policy_default_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_application_policy_intent_v1(json_schema_validate, obj):
    json_schema_validate('jsd_72fa27ccbaf55711849381a707e1edfa_v2_3_7_6').validate(obj)
    return True


def application_policy_intent_v1(api):
    endpoint_result = api.application_policy.application_policy_intent_v1(
        active_validation=True,
        createList=[{'name': 'string', 'deletePolicyStatus': 'string', 'policyScope': 'string', 'priority': 'string', 'advancedPolicyScope': {'name': 'string', 'advancedPolicyScopeElement': [{'groupId': ['string'], 'ssid': ['string']}]}, 'exclusiveContract': {'clause': [{'type': 'string', 'relevanceLevel': 'string', 'deviceRemovalBehavior': 'string', 'hostTrackingEnabled': True}]}, 'contract': {'idRef': 'string'}, 'producer': {'scalableGroup': [{'idRef': 'string'}]}, 'consumer': {'scalableGroup': [{'idRef': 'string'}]}}],
        deleteList=['string'],
        payload=None,
        updateList=[{'id': 'string', 'name': 'string', 'deletePolicyStatus': 'string', 'policyScope': 'string', 'priority': 'string', 'advancedPolicyScope': {'id': 'string', 'name': 'string', 'advancedPolicyScopeElement': [{'id': 'string', 'groupId': ['string'], 'ssid': ['string']}]}, 'exclusiveContract': {'id': 'string', 'clause': [{'id': 'string', 'type': 'string', 'relevanceLevel': 'string', 'deviceRemovalBehavior': 'string', 'hostTrackingEnabled': True}]}, 'contract': {'idRef': 'string'}, 'producer': {'id': 'string', 'scalableGroup': [{'idRef': 'string'}]}, 'consumer': {'id': 'string', 'scalableGroup': [{'idRef': 'string'}]}}]
    )
    return endpoint_result


@pytest.mark.application_policy
def test_application_policy_intent_v1(api, validator):
    try:
        assert is_valid_application_policy_intent_v1(
            validator,
            application_policy_intent_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def application_policy_intent_v1_default_val(api):
    endpoint_result = api.application_policy.application_policy_intent_v1(
        active_validation=True,
        createList=None,
        deleteList=None,
        payload=None,
        updateList=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_application_policy_intent_v1_default_val(api, validator):
    try:
        assert is_valid_application_policy_intent_v1(
            validator,
            application_policy_intent_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_policy_queuing_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d47102747c9e50ed9e365b1297e4188d_v2_3_7_6').validate(obj)
    return True


def get_application_policy_queuing_profile_v1(api):
    endpoint_result = api.application_policy.get_application_policy_queuing_profile_v1(
        name='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_queuing_profile_v1(api, validator):
    try:
        assert is_valid_get_application_policy_queuing_profile_v1(
            validator,
            get_application_policy_queuing_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_policy_queuing_profile_v1_default_val(api):
    endpoint_result = api.application_policy.get_application_policy_queuing_profile_v1(
        name=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_queuing_profile_v1_default_val(api, validator):
    try:
        assert is_valid_get_application_policy_queuing_profile_v1(
            validator,
            get_application_policy_queuing_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_application_policy_queuing_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b11aa4de387251c794665e030fa815da_v2_3_7_6').validate(obj)
    return True


def update_application_policy_queuing_profile_v1(api):
    endpoint_result = api.application_policy.update_application_policy_queuing_profile_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_update_application_policy_queuing_profile_v1(api, validator):
    try:
        assert is_valid_update_application_policy_queuing_profile_v1(
            validator,
            update_application_policy_queuing_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_application_policy_queuing_profile_v1_default_val(api):
    endpoint_result = api.application_policy.update_application_policy_queuing_profile_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_update_application_policy_queuing_profile_v1_default_val(api, validator):
    try:
        assert is_valid_update_application_policy_queuing_profile_v1(
            validator,
            update_application_policy_queuing_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_application_policy_queuing_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bd31fcbd1ecd5a2c8b812088b27bfcea_v2_3_7_6').validate(obj)
    return True


def create_application_policy_queuing_profile_v1(api):
    endpoint_result = api.application_policy.create_application_policy_queuing_profile_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_policy_queuing_profile_v1(api, validator):
    try:
        assert is_valid_create_application_policy_queuing_profile_v1(
            validator,
            create_application_policy_queuing_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_application_policy_queuing_profile_v1_default_val(api):
    endpoint_result = api.application_policy.create_application_policy_queuing_profile_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_policy_queuing_profile_v1_default_val(api, validator):
    try:
        assert is_valid_create_application_policy_queuing_profile_v1(
            validator,
            create_application_policy_queuing_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_policy_queuing_profile_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a22faef865d55fe48dd2467bee214518_v2_3_7_6').validate(obj)
    return True


def get_application_policy_queuing_profile_count_v1(api):
    endpoint_result = api.application_policy.get_application_policy_queuing_profile_count_v1(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_queuing_profile_count_v1(api, validator):
    try:
        assert is_valid_get_application_policy_queuing_profile_count_v1(
            validator,
            get_application_policy_queuing_profile_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_policy_queuing_profile_count_v1_default_val(api):
    endpoint_result = api.application_policy.get_application_policy_queuing_profile_count_v1(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_policy_queuing_profile_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_application_policy_queuing_profile_count_v1(
            validator,
            get_application_policy_queuing_profile_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_application_policy_queuing_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ac547ee07c2c5aff983d90cf4306619d_v2_3_7_6').validate(obj)
    return True


def delete_application_policy_queuing_profile_v1(api):
    endpoint_result = api.application_policy.delete_application_policy_queuing_profile_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_policy_queuing_profile_v1(api, validator):
    try:
        assert is_valid_delete_application_policy_queuing_profile_v1(
            validator,
            delete_application_policy_queuing_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_application_policy_queuing_profile_v1_default_val(api):
    endpoint_result = api.application_policy.delete_application_policy_queuing_profile_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_policy_queuing_profile_v1_default_val(api, validator):
    try:
        assert is_valid_delete_application_policy_queuing_profile_v1(
            validator,
            delete_application_policy_queuing_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_sets_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8b60dbd805b95030bc2caf345a44b504_v2_3_7_6').validate(obj)
    return True


def get_application_sets_v1(api):
    endpoint_result = api.application_policy.get_application_sets_v1(
        limit=0,
        name='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_v1(api, validator):
    try:
        assert is_valid_get_application_sets_v1(
            validator,
            get_application_sets_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_sets_v1_default_val(api):
    endpoint_result = api.application_policy.get_application_sets_v1(
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_v1_default_val(api, validator):
    try:
        assert is_valid_get_application_sets_v1(
            validator,
            get_application_sets_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_application_set_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0a59a448c5c25f1e8246d6827e6e3215_v2_3_7_6').validate(obj)
    return True


def delete_application_set_v1(api):
    endpoint_result = api.application_policy.delete_application_set_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_set_v1(api, validator):
    try:
        assert is_valid_delete_application_set_v1(
            validator,
            delete_application_set_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_application_set_v1_default_val(api):
    endpoint_result = api.application_policy.delete_application_set_v1(
        id=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_set_v1_default_val(api, validator):
    try:
        assert is_valid_delete_application_set_v1(
            validator,
            delete_application_set_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_application_set_v1(json_schema_validate, obj):
    json_schema_validate('jsd_636cb7563a5058c4801eb842a74ff61c_v2_3_7_6').validate(obj)
    return True


def create_application_set_v1(api):
    endpoint_result = api.application_policy.create_application_set_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_set_v1(api, validator):
    try:
        assert is_valid_create_application_set_v1(
            validator,
            create_application_set_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_application_set_v1_default_val(api):
    endpoint_result = api.application_policy.create_application_set_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_set_v1_default_val(api, validator):
    try:
        assert is_valid_create_application_set_v1(
            validator,
            create_application_set_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_sets_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_968ebc5880945305adb41253c6e4ffec_v2_3_7_6').validate(obj)
    return True


def get_application_sets_count_v1(api):
    endpoint_result = api.application_policy.get_application_sets_count_v1(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_count_v1(api, validator):
    try:
        assert is_valid_get_application_sets_count_v1(
            validator,
            get_application_sets_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_sets_count_v1_default_val(api):
    endpoint_result = api.application_policy.get_application_sets_count_v1(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_application_sets_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_application_sets_count_v1(
            validator,
            get_application_sets_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_application_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e1781a990c6b5a4b895d56bcfda2b7cb_v2_3_7_6').validate(obj)
    return True


def create_application_v1(api):
    endpoint_result = api.application_policy.create_application_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_v1(api, validator):
    try:
        assert is_valid_create_application_v1(
            validator,
            create_application_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_application_v1_default_val(api):
    endpoint_result = api.application_policy.create_application_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_application_v1_default_val(api, validator):
    try:
        assert is_valid_create_application_v1(
            validator,
            create_application_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_edit_application_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a3b37dcbe2a150bea06d9dcde1837281_v2_3_7_6').validate(obj)
    return True


def edit_application_v1(api):
    endpoint_result = api.application_policy.edit_application_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_edit_application_v1(api, validator):
    try:
        assert is_valid_edit_application_v1(
            validator,
            edit_application_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def edit_application_v1_default_val(api):
    endpoint_result = api.application_policy.edit_application_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_edit_application_v1_default_val(api, validator):
    try:
        assert is_valid_edit_application_v1(
            validator,
            edit_application_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_application_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d11d35f3505652b68905ddf1ee2f7e66_v2_3_7_6').validate(obj)
    return True


def delete_application_v1(api):
    endpoint_result = api.application_policy.delete_application_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_v1(api, validator):
    try:
        assert is_valid_delete_application_v1(
            validator,
            delete_application_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_application_v1_default_val(api):
    endpoint_result = api.application_policy.delete_application_v1(
        id=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_application_v1_default_val(api, validator):
    try:
        assert is_valid_delete_application_v1(
            validator,
            delete_application_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_applications_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5b12cdd3a75c51258c9e051e84189f92_v2_3_7_6').validate(obj)
    return True


def get_applications_v1(api):
    endpoint_result = api.application_policy.get_applications_v1(
        limit=0,
        name='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_v1(api, validator):
    try:
        assert is_valid_get_applications_v1(
            validator,
            get_applications_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_applications_v1_default_val(api):
    endpoint_result = api.application_policy.get_applications_v1(
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_v1_default_val(api, validator):
    try:
        assert is_valid_get_applications_v1(
            validator,
            get_applications_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_applications_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_30af5f0aa1ed56ab9b98eb602dbd8366_v2_3_7_6').validate(obj)
    return True


def get_applications_count_v1(api):
    endpoint_result = api.application_policy.get_applications_count_v1(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_count_v1(api, validator):
    try:
        assert is_valid_get_applications_count_v1(
            validator,
            get_applications_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_applications_count_v1_default_val(api):
    endpoint_result = api.application_policy.get_applications_count_v1(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_applications_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_applications_count_v1(
            validator,
            get_applications_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_qos_device_interface_info_v1(json_schema_validate, obj):
    json_schema_validate('jsd_56001c37a46857f0bee5eba0a514091c_v2_3_7_6').validate(obj)
    return True


def get_qos_device_interface_info_v1(api):
    endpoint_result = api.application_policy.get_qos_device_interface_info_v1(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_qos_device_interface_info_v1(api, validator):
    try:
        assert is_valid_get_qos_device_interface_info_v1(
            validator,
            get_qos_device_interface_info_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_qos_device_interface_info_v1_default_val(api):
    endpoint_result = api.application_policy.get_qos_device_interface_info_v1(
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_qos_device_interface_info_v1_default_val(api, validator):
    try:
        assert is_valid_get_qos_device_interface_info_v1(
            validator,
            get_qos_device_interface_info_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_qos_device_interface_info_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ea59df3daf2a57a0b48044cc49c8a1ca_v2_3_7_6').validate(obj)
    return True


def update_qos_device_interface_info_v1(api):
    endpoint_result = api.application_policy.update_qos_device_interface_info_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_update_qos_device_interface_info_v1(api, validator):
    try:
        assert is_valid_update_qos_device_interface_info_v1(
            validator,
            update_qos_device_interface_info_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_qos_device_interface_info_v1_default_val(api):
    endpoint_result = api.application_policy.update_qos_device_interface_info_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_update_qos_device_interface_info_v1_default_val(api, validator):
    try:
        assert is_valid_update_qos_device_interface_info_v1(
            validator,
            update_qos_device_interface_info_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_qos_device_interface_info_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d045d18062ad5ae59c6f446beb17d675_v2_3_7_6').validate(obj)
    return True


def create_qos_device_interface_info_v1(api):
    endpoint_result = api.application_policy.create_qos_device_interface_info_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_qos_device_interface_info_v1(api, validator):
    try:
        assert is_valid_create_qos_device_interface_info_v1(
            validator,
            create_qos_device_interface_info_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_qos_device_interface_info_v1_default_val(api):
    endpoint_result = api.application_policy.create_qos_device_interface_info_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.application_policy
def test_create_qos_device_interface_info_v1_default_val(api, validator):
    try:
        assert is_valid_create_qos_device_interface_info_v1(
            validator,
            create_qos_device_interface_info_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_qos_device_interface_info_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6349b98fe15b531dbb7e20c0f5fa61ab_v2_3_7_6').validate(obj)
    return True


def get_qos_device_interface_info_count_v1(api):
    endpoint_result = api.application_policy.get_qos_device_interface_info_count_v1(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_qos_device_interface_info_count_v1(api, validator):
    try:
        assert is_valid_get_qos_device_interface_info_count_v1(
            validator,
            get_qos_device_interface_info_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_qos_device_interface_info_count_v1_default_val(api):
    endpoint_result = api.application_policy.get_qos_device_interface_info_count_v1(

    )
    return endpoint_result


@pytest.mark.application_policy
def test_get_qos_device_interface_info_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_qos_device_interface_info_count_v1(
            validator,
            get_qos_device_interface_info_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_qos_device_interface_info_v1(json_schema_validate, obj):
    json_schema_validate('jsd_629a6a5bb5935709b03d0fc37a1d47d4_v2_3_7_6').validate(obj)
    return True


def delete_qos_device_interface_info_v1(api):
    endpoint_result = api.application_policy.delete_qos_device_interface_info_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_qos_device_interface_info_v1(api, validator):
    try:
        assert is_valid_delete_qos_device_interface_info_v1(
            validator,
            delete_qos_device_interface_info_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_qos_device_interface_info_v1_default_val(api):
    endpoint_result = api.application_policy.delete_qos_device_interface_info_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.application_policy
def test_delete_qos_device_interface_info_v1_default_val(api, validator):
    try:
        assert is_valid_delete_qos_device_interface_info_v1(
            validator,
            delete_qos_device_interface_info_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_application_sets_v2(json_schema_validate, obj):
    json_schema_validate('jsd_01e4d208b5545f66bf0f94a155c81f46_v2_3_7_6').validate(obj)
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
    json_schema_validate('jsd_b399a8f895b65f3d91926da8508a9295_v2_3_7_6').validate(obj)
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
    json_schema_validate('jsd_8c3f0e5c233a5cc39969fdcff6e0288e_v2_3_7_6').validate(obj)
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
    json_schema_validate('jsdfbef625d3225c1eb6db93289a11a33e_v2_3_7_6').validate(obj)
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
    json_schema_validate('jsd_3662b46a141650debf5946262e8a0961_v2_3_7_6').validate(obj)
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
    json_schema_validate('jsd_a14e71c1b98e51eea41255720025b519_v2_3_7_6').validate(obj)
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
    json_schema_validate('jsd_645981f8a81055328e2c77f0dcb60a68_v2_3_7_6').validate(obj)
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
    json_schema_validate('jsd_d4d0a63b02ed518a95fe297b2a566f1d_v2_3_7_6').validate(obj)
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
    json_schema_validate('jsd_ef849b2f5415501086635693a458e69b_v2_3_7_6').validate(obj)
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

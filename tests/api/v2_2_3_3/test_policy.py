# -*- coding: utf-8 -*-
"""DNACenterAPI policy API fixtures and tests.

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


def is_valid_create_a_profiling_rule(json_schema_validate, obj):
    json_schema_validate('jsd_2194bf80823752baba63a8849fd521cd_v2_2_3_3').validate(obj)
    return True


def create_a_profiling_rule(api):
    endpoint_result = api.policy.create_a_profiling_rule(
        active_validation=True,
        clusterId='string',
        conditionGroups={'type': 'string', 'condition': {'attribute': 'string', 'operator': 'string', 'value': 'string', 'attributeDictionary': 'string'}, 'operator': 'string', 'conditionGroup': [{}]},
        isDeleted=True,
        lastModifiedBy='string',
        lastModifiedOn=0,
        payload=None,
        pluginId='string',
        rejected=True,
        result={'deviceType': ['string'], 'hardwareManufacturer': ['string'], 'hardwareModel': ['string'], 'operatingSystem': ['string']},
        ruleId='string',
        ruleName='string',
        rulePriority=0,
        ruleType='string',
        ruleVersion=0,
        sourcePriority=0,
        usedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.policy
def test_create_a_profiling_rule(api, validator):
    try:
        assert is_valid_create_a_profiling_rule(
            validator,
            create_a_profiling_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_a_profiling_rule_default_val(api):
    endpoint_result = api.policy.create_a_profiling_rule(
        active_validation=True,
        clusterId=None,
        conditionGroups=None,
        isDeleted=None,
        lastModifiedBy=None,
        lastModifiedOn=None,
        payload=None,
        pluginId=None,
        rejected=None,
        result=None,
        ruleId=None,
        ruleName=None,
        rulePriority=None,
        ruleType=None,
        ruleVersion=None,
        sourcePriority=None,
        usedAttributes=None
    )
    return endpoint_result


@pytest.mark.policy
def test_create_a_profiling_rule_default_val(api, validator):
    try:
        assert is_valid_create_a_profiling_rule(
            validator,
            create_a_profiling_rule_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_list_of_profiling_rules(json_schema_validate, obj):
    json_schema_validate('jsd_a4571194a9e05664ad348f72d7651bb0_v2_2_3_3').validate(obj)
    return True


def get_list_of_profiling_rules(api):
    endpoint_result = api.policy.get_list_of_profiling_rules(
        include_deleted=True,
        limit=0,
        offset=0,
        order='string',
        rule_type='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.policy
def test_get_list_of_profiling_rules(api, validator):
    try:
        assert is_valid_get_list_of_profiling_rules(
            validator,
            get_list_of_profiling_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_list_of_profiling_rules_default_val(api):
    endpoint_result = api.policy.get_list_of_profiling_rules(
        include_deleted=None,
        limit=None,
        offset=None,
        order=None,
        rule_type=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.policy
def test_get_list_of_profiling_rules_default_val(api, validator):
    try:
        assert is_valid_get_list_of_profiling_rules(
            validator,
            get_list_of_profiling_rules_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_profiling_rules_in_bulk(json_schema_validate, obj):
    json_schema_validate('jsd_90347931b4155d6f885a53ad0e47b1a4_v2_2_3_3').validate(obj)
    return True


def import_profiling_rules_in_bulk(api):
    endpoint_result = api.policy.import_profiling_rules_in_bulk(
        active_validation=True,
        payload=None,
        profilingRules=[{'ruleId': 'string', 'ruleName': 'string', 'ruleType': 'string', 'ruleVersion': 0, 'rulePriority': 0, 'sourcePriority': 0, 'isDeleted': True, 'lastModifiedBy': 'string', 'lastModifiedOn': 0, 'pluginId': 'string', 'clusterId': 'string', 'rejected': True, 'result': {'deviceType': ['string'], 'hardwareManufacturer': ['string'], 'hardwareModel': ['string'], 'operatingSystem': ['string']}, 'conditionGroups': {'type': 'string', 'condition': {'attribute': 'string', 'operator': 'string', 'value': 'string', 'attributeDictionary': 'string'}, 'operator': 'string', 'conditionGroup': [{}]}, 'usedAttributes': ['string']}]
    )
    return endpoint_result


@pytest.mark.policy
def test_import_profiling_rules_in_bulk(api, validator):
    try:
        assert is_valid_import_profiling_rules_in_bulk(
            validator,
            import_profiling_rules_in_bulk(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_profiling_rules_in_bulk_default_val(api):
    endpoint_result = api.policy.import_profiling_rules_in_bulk(
        active_validation=True,
        payload=None,
        profilingRules=None
    )
    return endpoint_result


@pytest.mark.policy
def test_import_profiling_rules_in_bulk_default_val(api, validator):
    try:
        assert is_valid_import_profiling_rules_in_bulk(
            validator,
            import_profiling_rules_in_bulk_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_profiling_rules(json_schema_validate, obj):
    json_schema_validate('jsd_2ec43ed2e44c5f3ea7a904d39af66899_v2_2_3_3').validate(obj)
    return True


def get_count_of_profiling_rules(api):
    endpoint_result = api.policy.get_count_of_profiling_rules(
        include_deleted=True,
        rule_type='string'
    )
    return endpoint_result


@pytest.mark.policy
def test_get_count_of_profiling_rules(api, validator):
    try:
        assert is_valid_get_count_of_profiling_rules(
            validator,
            get_count_of_profiling_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_profiling_rules_default_val(api):
    endpoint_result = api.policy.get_count_of_profiling_rules(
        include_deleted=None,
        rule_type=None
    )
    return endpoint_result


@pytest.mark.policy
def test_get_count_of_profiling_rules_default_val(api, validator):
    try:
        assert is_valid_get_count_of_profiling_rules(
            validator,
            get_count_of_profiling_rules_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_an_existing_profiling_rule(json_schema_validate, obj):
    json_schema_validate('jsd_1508a4dab79d54829548004029a91ba1_v2_2_3_3').validate(obj)
    return True


def update_an_existing_profiling_rule(api):
    endpoint_result = api.policy.update_an_existing_profiling_rule(
        active_validation=True,
        clusterId='string',
        conditionGroups={'type': 'string', 'condition': {'attribute': 'string', 'operator': 'string', 'value': 'string', 'attributeDictionary': 'string'}, 'operator': 'string', 'conditionGroup': [{}]},
        isDeleted=True,
        lastModifiedBy='string',
        lastModifiedOn=0,
        payload=None,
        pluginId='string',
        rejected=True,
        result={'deviceType': ['string'], 'hardwareManufacturer': ['string'], 'hardwareModel': ['string'], 'operatingSystem': ['string']},
        ruleId='string',
        ruleName='string',
        rulePriority=0,
        ruleType='string',
        ruleVersion=0,
        rule_id='string',
        sourcePriority=0,
        usedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.policy
def test_update_an_existing_profiling_rule(api, validator):
    try:
        assert is_valid_update_an_existing_profiling_rule(
            validator,
            update_an_existing_profiling_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_an_existing_profiling_rule_default_val(api):
    endpoint_result = api.policy.update_an_existing_profiling_rule(
        active_validation=True,
        clusterId=None,
        conditionGroups=None,
        isDeleted=None,
        lastModifiedBy=None,
        lastModifiedOn=None,
        payload=None,
        pluginId=None,
        rejected=None,
        result=None,
        ruleId=None,
        ruleName=None,
        rulePriority=None,
        ruleType=None,
        ruleVersion=None,
        rule_id='string',
        sourcePriority=None,
        usedAttributes=None
    )
    return endpoint_result


@pytest.mark.policy
def test_update_an_existing_profiling_rule_default_val(api, validator):
    try:
        assert is_valid_update_an_existing_profiling_rule(
            validator,
            update_an_existing_profiling_rule_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_details_of_a_single_profiling_rule(json_schema_validate, obj):
    json_schema_validate('jsd_fbea90831e6e57e79062edab0c76f8a1_v2_2_3_3').validate(obj)
    return True


def get_details_of_a_single_profiling_rule(api):
    endpoint_result = api.policy.get_details_of_a_single_profiling_rule(
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.policy
def test_get_details_of_a_single_profiling_rule(api, validator):
    try:
        assert is_valid_get_details_of_a_single_profiling_rule(
            validator,
            get_details_of_a_single_profiling_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_details_of_a_single_profiling_rule_default_val(api):
    endpoint_result = api.policy.get_details_of_a_single_profiling_rule(
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.policy
def test_get_details_of_a_single_profiling_rule_default_val(api, validator):
    try:
        assert is_valid_get_details_of_a_single_profiling_rule(
            validator,
            get_details_of_a_single_profiling_rule_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_an_existing_profiling_rule(json_schema_validate, obj):
    json_schema_validate('jsd_3a3f7b6780725e83beed53d6ce2256e4_v2_2_3_3').validate(obj)
    return True


def delete_an_existing_profiling_rule(api):
    endpoint_result = api.policy.delete_an_existing_profiling_rule(
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.policy
def test_delete_an_existing_profiling_rule(api, validator):
    try:
        assert is_valid_delete_an_existing_profiling_rule(
            validator,
            delete_an_existing_profiling_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_an_existing_profiling_rule_default_val(api):
    endpoint_result = api.policy.delete_an_existing_profiling_rule(
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.policy
def test_delete_an_existing_profiling_rule_default_val(api, validator):
    try:
        assert is_valid_delete_an_existing_profiling_rule(
            validator,
            delete_an_existing_profiling_rule_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

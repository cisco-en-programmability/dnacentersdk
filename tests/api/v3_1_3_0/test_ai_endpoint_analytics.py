# -*- coding: utf-8 -*-
"""CatalystCenterAPI ai_endpoint_analytics API fixtures and tests.

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

pytestmark = pytest.mark.skipif(
    DNA_CENTER_VERSION != "3.1.3.0", reason="version does not match"
)


def is_valid_get_anc_policies(json_schema_validate, obj):
    json_schema_validate("jsd_c888e4f05d80571483ebe5793f6c44c1_v3_1_3_0").validate(obj)
    return True


def get_anc_policies(api):
    endpoint_result = api.ai_endpoint_analytics.get_anc_policies()
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_anc_policies(api, validator):
    try:
        assert is_valid_get_anc_policies(validator, get_anc_policies(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_anc_policies_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.get_anc_policies()
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_anc_policies_default_val(api, validator):
    try:
        assert is_valid_get_anc_policies(validator, get_anc_policies_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_process_cmdb_endpoints(json_schema_validate, obj):
    json_schema_validate("jsd_72aba18f6e605ce28a112b34dcb4fe82_v3_1_3_0").validate(obj)
    return True


def process_cmdb_endpoints(api):
    endpoint_result = api.ai_endpoint_analytics.process_cmdb_endpoints(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_process_cmdb_endpoints(api, validator):
    try:
        assert is_valid_process_cmdb_endpoints(validator, process_cmdb_endpoints(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def process_cmdb_endpoints_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.process_cmdb_endpoints(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_process_cmdb_endpoints_default_val(api, validator):
    try:
        assert is_valid_process_cmdb_endpoints(
            validator, process_cmdb_endpoints_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ai_endpoint_analytics_attribute_dictionaries(
    json_schema_validate, obj
):
    json_schema_validate("jsd_b12a3ca89c475179b182da81bdb64a8a_v3_1_3_0").validate(obj)
    return True


def get_ai_endpoint_analytics_attribute_dictionaries(api):
    endpoint_result = (
        api.ai_endpoint_analytics.get_ai_endpoint_analytics_attribute_dictionaries(
            include_attributes=True
        )
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_ai_endpoint_analytics_attribute_dictionaries(api, validator):
    try:
        assert is_valid_get_ai_endpoint_analytics_attribute_dictionaries(
            validator, get_ai_endpoint_analytics_attribute_dictionaries(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ai_endpoint_analytics_attribute_dictionaries_default_val(api):
    endpoint_result = (
        api.ai_endpoint_analytics.get_ai_endpoint_analytics_attribute_dictionaries(
            include_attributes=None
        )
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_ai_endpoint_analytics_attribute_dictionaries_default_val(api, validator):
    try:
        assert is_valid_get_ai_endpoint_analytics_attribute_dictionaries(
            validator, get_ai_endpoint_analytics_attribute_dictionaries_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_register_an_endpoint(json_schema_validate, obj):
    json_schema_validate("jsd_73b7ae9494b05a57bf6393eaf308b1e7_v3_1_3_0").validate(obj)
    return True


def register_an_endpoint(api):
    endpoint_result = api.ai_endpoint_analytics.register_an_endpoint(
        active_validation=True,
        deviceType="string",
        hardwareManufacturer="string",
        hardwareModel="string",
        macAddress="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_register_an_endpoint(api, validator):
    try:
        assert is_valid_register_an_endpoint(validator, register_an_endpoint(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def register_an_endpoint_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.register_an_endpoint(
        active_validation=True,
        deviceType=None,
        hardwareManufacturer=None,
        hardwareModel=None,
        macAddress=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_register_an_endpoint_default_val(api, validator):
    try:
        assert is_valid_register_an_endpoint(
            validator, register_an_endpoint_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_the_endpoints(json_schema_validate, obj):
    json_schema_validate("jsd_b4f18988d61253bd8565ce2a22a909ae_v3_1_3_0").validate(obj)
    return True


def query_the_endpoints(api):
    endpoint_result = api.ai_endpoint_analytics.query_the_endpoints(
        ai_spoofing_trust_level="string",
        anc_policy="string",
        auth_method="string",
        changed_profile_trust_level="string",
        concurrent_mac_trust_level="string",
        device_type="string",
        hardware_manufacturer="string",
        hardware_model="string",
        include="string",
        ip="string",
        ip_blocklist_detected=True,
        limit=0,
        mac_address="string",
        mac_addresses="value1,value2",
        nat_trust_level="string",
        offset=0,
        operating_system="string",
        order="string",
        posture_status="string",
        profiling_status="string",
        random_mac=True,
        registered=True,
        sort_by="string",
        trust_score="string",
        unauth_port_detected=True,
        weak_cred_detected=True,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_query_the_endpoints(api, validator):
    try:
        assert is_valid_query_the_endpoints(validator, query_the_endpoints(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def query_the_endpoints_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.query_the_endpoints(
        ai_spoofing_trust_level=None,
        anc_policy=None,
        auth_method=None,
        changed_profile_trust_level=None,
        concurrent_mac_trust_level=None,
        device_type=None,
        hardware_manufacturer=None,
        hardware_model=None,
        include=None,
        ip=None,
        ip_blocklist_detected=None,
        limit=None,
        mac_address=None,
        mac_addresses=None,
        nat_trust_level=None,
        offset=None,
        operating_system=None,
        order=None,
        posture_status=None,
        profiling_status=None,
        random_mac=None,
        registered=None,
        sort_by=None,
        trust_score=None,
        unauth_port_detected=None,
        weak_cred_detected=None,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_query_the_endpoints_default_val(api, validator):
    try:
        assert is_valid_query_the_endpoints(
            validator, query_the_endpoints_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_fetch_the_count_of_endpoints(json_schema_validate, obj):
    json_schema_validate("jsd_1fab7e4bf248589894a0ad79c4f0940f_v3_1_3_0").validate(obj)
    return True


def fetch_the_count_of_endpoints(api):
    endpoint_result = api.ai_endpoint_analytics.fetch_the_count_of_endpoints(
        ai_spoofing_trust_level="string",
        anc_policy="string",
        auth_method="string",
        changed_profile_trust_level="string",
        concurrent_mac_trust_level="string",
        device_type="string",
        hardware_manufacturer="string",
        hardware_model="string",
        ip="string",
        ip_blocklist_detected=True,
        mac_address="string",
        mac_addresses="value1,value2",
        nat_trust_level="string",
        operating_system="string",
        posture_status="string",
        profiling_status="string",
        random_mac=True,
        registered=True,
        trust_score="string",
        unauth_port_detected=True,
        weak_cred_detected=True,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_fetch_the_count_of_endpoints(api, validator):
    try:
        assert is_valid_fetch_the_count_of_endpoints(
            validator, fetch_the_count_of_endpoints(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def fetch_the_count_of_endpoints_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.fetch_the_count_of_endpoints(
        ai_spoofing_trust_level=None,
        anc_policy=None,
        auth_method=None,
        changed_profile_trust_level=None,
        concurrent_mac_trust_level=None,
        device_type=None,
        hardware_manufacturer=None,
        hardware_model=None,
        ip=None,
        ip_blocklist_detected=None,
        mac_address=None,
        mac_addresses=None,
        nat_trust_level=None,
        operating_system=None,
        posture_status=None,
        profiling_status=None,
        random_mac=None,
        registered=None,
        trust_score=None,
        unauth_port_detected=None,
        weak_cred_detected=None,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_fetch_the_count_of_endpoints_default_val(api, validator):
    try:
        assert is_valid_fetch_the_count_of_endpoints(
            validator, fetch_the_count_of_endpoints_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_a_registered_endpoint(json_schema_validate, obj):
    json_schema_validate("jsd_15645b107800544384c1ddad7b60c237_v3_1_3_0").validate(obj)
    return True


def update_a_registered_endpoint(api):
    endpoint_result = api.ai_endpoint_analytics.update_a_registered_endpoint(
        active_validation=True,
        deviceType="string",
        ep_id="string",
        hardwareManufacturer="string",
        hardwareModel="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_update_a_registered_endpoint(api, validator):
    try:
        assert is_valid_update_a_registered_endpoint(
            validator, update_a_registered_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_a_registered_endpoint_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.update_a_registered_endpoint(
        active_validation=True,
        deviceType=None,
        ep_id="string",
        hardwareManufacturer=None,
        hardwareModel=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_update_a_registered_endpoint_default_val(api, validator):
    try:
        assert is_valid_update_a_registered_endpoint(
            validator, update_a_registered_endpoint_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_endpoint_details(json_schema_validate, obj):
    json_schema_validate("jsd_cde73293a8235ed8ae4cfe5f6717bff1_v3_1_3_0").validate(obj)
    return True


def get_endpoint_details(api):
    endpoint_result = api.ai_endpoint_analytics.get_endpoint_details(
        ep_id="string", include="string"
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_endpoint_details(api, validator):
    try:
        assert is_valid_get_endpoint_details(validator, get_endpoint_details(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_endpoint_details_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.get_endpoint_details(
        ep_id="string", include=None
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_endpoint_details_default_val(api, validator):
    try:
        assert is_valid_get_endpoint_details(
            validator, get_endpoint_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_an_endpoint(json_schema_validate, obj):
    json_schema_validate("jsd_d82c78cf10395b2baba3b51fd8370a14_v3_1_3_0").validate(obj)
    return True


def delete_an_endpoint(api):
    endpoint_result = api.ai_endpoint_analytics.delete_an_endpoint(ep_id="string")
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_delete_an_endpoint(api, validator):
    try:
        assert is_valid_delete_an_endpoint(validator, delete_an_endpoint(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_an_endpoint_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.delete_an_endpoint(ep_id="string")
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_delete_an_endpoint_default_val(api, validator):
    try:
        assert is_valid_delete_an_endpoint(
            validator, delete_an_endpoint_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_apply_anc_policy(json_schema_validate, obj):
    json_schema_validate("jsd_3de92f8ae3c15ea0bad5562452eb5c40_v3_1_3_0").validate(obj)
    return True


def apply_anc_policy(api):
    endpoint_result = api.ai_endpoint_analytics.apply_anc_policy(
        active_validation=True,
        ancPolicy="string",
        ep_id="string",
        granularAncPolicy=[{"name": "string", "nasIpAddress": "string"}],
        payload=None,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_apply_anc_policy(api, validator):
    try:
        assert is_valid_apply_anc_policy(validator, apply_anc_policy(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def apply_anc_policy_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.apply_anc_policy(
        active_validation=True,
        ancPolicy=None,
        ep_id="string",
        granularAncPolicy=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_apply_anc_policy_default_val(api, validator):
    try:
        assert is_valid_apply_anc_policy(validator, apply_anc_policy_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_revoke_anc_policy(json_schema_validate, obj):
    json_schema_validate("jsd_f136ac6d3b145d35922c4ba15ccb941a_v3_1_3_0").validate(obj)
    return True


def revoke_anc_policy(api):
    endpoint_result = api.ai_endpoint_analytics.revoke_anc_policy(ep_id="string")
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_revoke_anc_policy(api, validator):
    try:
        assert is_valid_revoke_anc_policy(validator, revoke_anc_policy(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def revoke_anc_policy_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.revoke_anc_policy(ep_id="string")
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_revoke_anc_policy_default_val(api, validator):
    try:
        assert is_valid_revoke_anc_policy(validator, revoke_anc_policy_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_a_profiling_rule(json_schema_validate, obj):
    json_schema_validate("jsd_2194bf80823752baba63a8849fd521cd_v3_1_3_0").validate(obj)
    return True


def create_a_profiling_rule(api):
    endpoint_result = api.ai_endpoint_analytics.create_a_profiling_rule(
        active_validation=True,
        clusterId="string",
        conditionGroups={
            "type": "string",
            "condition": {
                "attribute": "string",
                "operator": "string",
                "value": "string",
                "attributeDictionary": "string",
            },
            "operator": "string",
            "conditionGroup": [{}],
        },
        isDeleted=True,
        lastModifiedBy="string",
        lastModifiedOn=0,
        payload=None,
        pluginId="string",
        rejected=True,
        result={
            "deviceType": ["string"],
            "hardwareManufacturer": ["string"],
            "hardwareModel": ["string"],
            "operatingSystem": ["string"],
        },
        ruleId="string",
        ruleName="string",
        rulePriority=0,
        ruleType="string",
        ruleVersion=0,
        sourcePriority=0,
        usedAttributes=["string"],
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_create_a_profiling_rule(api, validator):
    try:
        assert is_valid_create_a_profiling_rule(validator, create_a_profiling_rule(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_a_profiling_rule_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.create_a_profiling_rule(
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
        usedAttributes=None,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_create_a_profiling_rule_default_val(api, validator):
    try:
        assert is_valid_create_a_profiling_rule(
            validator, create_a_profiling_rule_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_list_of_profiling_rules(json_schema_validate, obj):
    json_schema_validate("jsd_a4571194a9e05664ad348f72d7651bb0_v3_1_3_0").validate(obj)
    return True


def get_list_of_profiling_rules(api):
    endpoint_result = api.ai_endpoint_analytics.get_list_of_profiling_rules(
        include_deleted=True,
        limit=0,
        offset=0,
        order="string",
        rule_type="string",
        sort_by="string",
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_list_of_profiling_rules(api, validator):
    try:
        assert is_valid_get_list_of_profiling_rules(
            validator, get_list_of_profiling_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_list_of_profiling_rules_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.get_list_of_profiling_rules(
        include_deleted=None,
        limit=None,
        offset=None,
        order=None,
        rule_type=None,
        sort_by=None,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_list_of_profiling_rules_default_val(api, validator):
    try:
        assert is_valid_get_list_of_profiling_rules(
            validator, get_list_of_profiling_rules_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_profiling_rules_in_bulk(json_schema_validate, obj):
    json_schema_validate("jsd_90347931b4155d6f885a53ad0e47b1a4_v3_1_3_0").validate(obj)
    return True


def import_profiling_rules_in_bulk(api):
    endpoint_result = api.ai_endpoint_analytics.import_profiling_rules_in_bulk(
        active_validation=True,
        payload=None,
        profilingRules=[
            {
                "ruleId": "string",
                "ruleName": "string",
                "ruleType": "string",
                "ruleVersion": 0,
                "rulePriority": 0,
                "sourcePriority": 0,
                "isDeleted": True,
                "lastModifiedBy": "string",
                "lastModifiedOn": 0,
                "pluginId": "string",
                "clusterId": "string",
                "rejected": True,
                "result": {
                    "deviceType": ["string"],
                    "hardwareManufacturer": ["string"],
                    "hardwareModel": ["string"],
                    "operatingSystem": ["string"],
                },
                "conditionGroups": {
                    "type": "string",
                    "condition": {
                        "attribute": "string",
                        "operator": "string",
                        "value": "string",
                        "attributeDictionary": "string",
                    },
                    "operator": "string",
                    "conditionGroup": [{}],
                },
                "usedAttributes": ["string"],
            }
        ],
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_import_profiling_rules_in_bulk(api, validator):
    try:
        assert is_valid_import_profiling_rules_in_bulk(
            validator, import_profiling_rules_in_bulk(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_profiling_rules_in_bulk_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.import_profiling_rules_in_bulk(
        active_validation=True, payload=None, profilingRules=None
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_import_profiling_rules_in_bulk_default_val(api, validator):
    try:
        assert is_valid_import_profiling_rules_in_bulk(
            validator, import_profiling_rules_in_bulk_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_profiling_rules(json_schema_validate, obj):
    json_schema_validate("jsd_2ec43ed2e44c5f3ea7a904d39af66899_v3_1_3_0").validate(obj)
    return True


def get_count_of_profiling_rules(api):
    endpoint_result = api.ai_endpoint_analytics.get_count_of_profiling_rules(
        include_deleted=True, rule_type="string"
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_count_of_profiling_rules(api, validator):
    try:
        assert is_valid_get_count_of_profiling_rules(
            validator, get_count_of_profiling_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_profiling_rules_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.get_count_of_profiling_rules(
        include_deleted=None, rule_type=None
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_count_of_profiling_rules_default_val(api, validator):
    try:
        assert is_valid_get_count_of_profiling_rules(
            validator, get_count_of_profiling_rules_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_an_existing_profiling_rule(json_schema_validate, obj):
    json_schema_validate("jsd_1508a4dab79d54829548004029a91ba1_v3_1_3_0").validate(obj)
    return True


def update_an_existing_profiling_rule(api):
    endpoint_result = api.ai_endpoint_analytics.update_an_existing_profiling_rule(
        active_validation=True,
        clusterId="string",
        conditionGroups={
            "type": "string",
            "condition": {
                "attribute": "string",
                "operator": "string",
                "value": "string",
                "attributeDictionary": "string",
            },
            "operator": "string",
            "conditionGroup": [{}],
        },
        isDeleted=True,
        lastModifiedBy="string",
        lastModifiedOn=0,
        payload=None,
        pluginId="string",
        rejected=True,
        result={
            "deviceType": ["string"],
            "hardwareManufacturer": ["string"],
            "hardwareModel": ["string"],
            "operatingSystem": ["string"],
        },
        ruleId="string",
        ruleName="string",
        rulePriority=0,
        ruleType="string",
        ruleVersion=0,
        rule_id="string",
        sourcePriority=0,
        usedAttributes=["string"],
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_update_an_existing_profiling_rule(api, validator):
    try:
        assert is_valid_update_an_existing_profiling_rule(
            validator, update_an_existing_profiling_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_an_existing_profiling_rule_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.update_an_existing_profiling_rule(
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
        rule_id="string",
        sourcePriority=None,
        usedAttributes=None,
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_update_an_existing_profiling_rule_default_val(api, validator):
    try:
        assert is_valid_update_an_existing_profiling_rule(
            validator, update_an_existing_profiling_rule_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_details_of_a_single_profiling_rule(json_schema_validate, obj):
    json_schema_validate("jsd_fbea90831e6e57e79062edab0c76f8a1_v3_1_3_0").validate(obj)
    return True


def get_details_of_a_single_profiling_rule(api):
    endpoint_result = api.ai_endpoint_analytics.get_details_of_a_single_profiling_rule(
        rule_id="string"
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_details_of_a_single_profiling_rule(api, validator):
    try:
        assert is_valid_get_details_of_a_single_profiling_rule(
            validator, get_details_of_a_single_profiling_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_details_of_a_single_profiling_rule_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.get_details_of_a_single_profiling_rule(
        rule_id="string"
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_details_of_a_single_profiling_rule_default_val(api, validator):
    try:
        assert is_valid_get_details_of_a_single_profiling_rule(
            validator, get_details_of_a_single_profiling_rule_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_an_existing_profiling_rule(json_schema_validate, obj):
    json_schema_validate("jsd_3a3f7b6780725e83beed53d6ce2256e4_v3_1_3_0").validate(obj)
    return True


def delete_an_existing_profiling_rule(api):
    endpoint_result = api.ai_endpoint_analytics.delete_an_existing_profiling_rule(
        rule_id="string"
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_delete_an_existing_profiling_rule(api, validator):
    try:
        assert is_valid_delete_an_existing_profiling_rule(
            validator, delete_an_existing_profiling_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_an_existing_profiling_rule_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.delete_an_existing_profiling_rule(
        rule_id="string"
    )
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_delete_an_existing_profiling_rule_default_val(api, validator):
    try:
        assert is_valid_delete_an_existing_profiling_rule(
            validator, delete_an_existing_profiling_rule_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_task_details(json_schema_validate, obj):
    json_schema_validate("jsd_682a0d1d05fe582aa287acb470e3af1d_v3_1_3_0").validate(obj)
    return True


def get_task_details(api):
    endpoint_result = api.ai_endpoint_analytics.get_task_details(task_id="string")
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_task_details(api, validator):
    try:
        assert is_valid_get_task_details(validator, get_task_details(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_task_details_default_val(api):
    endpoint_result = api.ai_endpoint_analytics.get_task_details(task_id="string")
    return endpoint_result


@pytest.mark.ai_endpoint_analytics
def test_get_task_details_default_val(api, validator):
    try:
        assert is_valid_get_task_details(validator, get_task_details_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

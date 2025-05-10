# -*- coding: utf-8 -*-
"""CatalystCenterAPI health_and_performance API fixtures and tests.

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


def is_valid_retrieves_diagnostic_task_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_84f1144e25e659d1aedcfe02afca97cc_v3_1_3_0').validate(obj)
    return True


def retrieves_diagnostic_task_by_id_v1(api):
    endpoint_result = api.health_and_performance.retrieves_diagnostic_task_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_diagnostic_task_by_id_v1(api, validator):
    try:
        assert is_valid_retrieves_diagnostic_task_by_id_v1(
            validator,
            retrieves_diagnostic_task_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_diagnostic_task_by_id_v1_default_val(api):
    endpoint_result = api.health_and_performance.retrieves_diagnostic_task_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_diagnostic_task_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_diagnostic_task_by_id_v1(
            validator,
            retrieves_diagnostic_task_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_diagnostic_task_details_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a656639f78625002805a9ad1257f9cde_v3_1_3_0').validate(obj)
    return True


def retrieves_diagnostic_task_details_by_id_v1(api):
    endpoint_result = api.health_and_performance.retrieves_diagnostic_task_details_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_diagnostic_task_details_by_id_v1(api, validator):
    try:
        assert is_valid_retrieves_diagnostic_task_details_by_id_v1(
            validator,
            retrieves_diagnostic_task_details_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_diagnostic_task_details_by_id_v1_default_val(api):
    endpoint_result = api.health_and_performance.retrieves_diagnostic_task_details_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_diagnostic_task_details_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_diagnostic_task_details_by_id_v1(
            validator,
            retrieves_diagnostic_task_details_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_all_the_validation_sets_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d6fc1397d48d52449923716aff009d3c_v3_1_3_0').validate(obj)
    return True


def retrieves_all_the_validation_sets_v1(api):
    endpoint_result = api.health_and_performance.retrieves_all_the_validation_sets_v1(
        view='string'
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_all_the_validation_sets_v1(api, validator):
    try:
        assert is_valid_retrieves_all_the_validation_sets_v1(
            validator,
            retrieves_all_the_validation_sets_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_all_the_validation_sets_v1_default_val(api):
    endpoint_result = api.health_and_performance.retrieves_all_the_validation_sets_v1(
        view=None
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_all_the_validation_sets_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_all_the_validation_sets_v1(
            validator,
            retrieves_all_the_validation_sets_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_validation_details_for_a_validation_set_v1(json_schema_validate, obj):
    json_schema_validate('jsd_99d95307fdbf5b169d9d05e3151f61ac_v3_1_3_0').validate(obj)
    return True


def retrieves_validation_details_for_a_validation_set_v1(api):
    endpoint_result = api.health_and_performance.retrieves_validation_details_for_a_validation_set_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_validation_details_for_a_validation_set_v1(api, validator):
    try:
        assert is_valid_retrieves_validation_details_for_a_validation_set_v1(
            validator,
            retrieves_validation_details_for_a_validation_set_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_validation_details_for_a_validation_set_v1_default_val(api):
    endpoint_result = api.health_and_performance.retrieves_validation_details_for_a_validation_set_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_validation_details_for_a_validation_set_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_validation_details_for_a_validation_set_v1(
            validator,
            retrieves_validation_details_for_a_validation_set_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_validation_workflows_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2a53d325f85e5549b7c5957c6ecbd891_v3_1_3_0').validate(obj)
    return True


def retrieves_the_list_of_validation_workflows_v1(api):
    endpoint_result = api.health_and_performance.retrieves_the_list_of_validation_workflows_v1(
        end_time=0,
        limit=0,
        offset=0,
        run_status='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_the_list_of_validation_workflows_v1(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_validation_workflows_v1(
            validator,
            retrieves_the_list_of_validation_workflows_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_validation_workflows_v1_default_val(api):
    endpoint_result = api.health_and_performance.retrieves_the_list_of_validation_workflows_v1(
        end_time=None,
        limit=None,
        offset=None,
        run_status=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_the_list_of_validation_workflows_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_validation_workflows_v1(
            validator,
            retrieves_the_list_of_validation_workflows_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_submits_the_workflow_for_executing_validations_v1(json_schema_validate, obj):
    json_schema_validate('jsd_cf9d39cef5e95bb9bd48d5f86e094c99_v3_1_3_0').validate(obj)
    return True


def submits_the_workflow_for_executing_validations_v1(api):
    endpoint_result = api.health_and_performance.submits_the_workflow_for_executing_validations_v1(
        active_validation=True,
        description='string',
        name='string',
        payload=None,
        validationSetIds=['string']
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_submits_the_workflow_for_executing_validations_v1(api, validator):
    try:
        assert is_valid_submits_the_workflow_for_executing_validations_v1(
            validator,
            submits_the_workflow_for_executing_validations_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def submits_the_workflow_for_executing_validations_v1_default_val(api):
    endpoint_result = api.health_and_performance.submits_the_workflow_for_executing_validations_v1(
        active_validation=True,
        description=None,
        name=None,
        payload=None,
        validationSetIds=None
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_submits_the_workflow_for_executing_validations_v1_default_val(api, validator):
    try:
        assert is_valid_submits_the_workflow_for_executing_validations_v1(
            validator,
            submits_the_workflow_for_executing_validations_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_validation_workflows_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b174a2fc5171520d9423c9a50f7394e7_v3_1_3_0').validate(obj)
    return True


def retrieves_the_count_of_validation_workflows_v1(api):
    endpoint_result = api.health_and_performance.retrieves_the_count_of_validation_workflows_v1(
        end_time=0,
        run_status='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_the_count_of_validation_workflows_v1(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_validation_workflows_v1(
            validator,
            retrieves_the_count_of_validation_workflows_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_validation_workflows_v1_default_val(api):
    endpoint_result = api.health_and_performance.retrieves_the_count_of_validation_workflows_v1(
        end_time=None,
        run_status=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_the_count_of_validation_workflows_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_validation_workflows_v1(
            validator,
            retrieves_the_count_of_validation_workflows_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_a_validation_workflow_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b3ab76a74dae51fabf39b2ad85c3c58f_v3_1_3_0').validate(obj)
    return True


def deletes_a_validation_workflow_v1(api):
    endpoint_result = api.health_and_performance.deletes_a_validation_workflow_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_deletes_a_validation_workflow_v1(api, validator):
    try:
        assert is_valid_deletes_a_validation_workflow_v1(
            validator,
            deletes_a_validation_workflow_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_a_validation_workflow_v1_default_val(api):
    endpoint_result = api.health_and_performance.deletes_a_validation_workflow_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_deletes_a_validation_workflow_v1_default_val(api, validator):
    try:
        assert is_valid_deletes_a_validation_workflow_v1(
            validator,
            deletes_a_validation_workflow_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_validation_workflow_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_221c36c30b8c5ddfbf9ccf36db5dd68a_v3_1_3_0').validate(obj)
    return True


def retrieves_validation_workflow_details_v1(api):
    endpoint_result = api.health_and_performance.retrieves_validation_workflow_details_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_validation_workflow_details_v1(api, validator):
    try:
        assert is_valid_retrieves_validation_workflow_details_v1(
            validator,
            retrieves_validation_workflow_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_validation_workflow_details_v1_default_val(api):
    endpoint_result = api.health_and_performance.retrieves_validation_workflow_details_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_retrieves_validation_workflow_details_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_validation_workflow_details_v1(
            validator,
            retrieves_validation_workflow_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_system_health(json_schema_validate, obj):
    json_schema_validate('jsd_d0acccfae6885bc28f8f39c67f4acfc1_v3_1_3_0').validate(obj)
    return True


def system_health(api):
    endpoint_result = api.health_and_performance.system_health(
        domain='string',
        limit=0,
        offset=0,
        subdomain='string',
        summary=True
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_system_health(api, validator):
    try:
        assert is_valid_system_health(
            validator,
            system_health(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def system_health_default_val(api):
    endpoint_result = api.health_and_performance.system_health(
        domain=None,
        limit=None,
        offset=None,
        subdomain=None,
        summary=None
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_system_health_default_val(api, validator):
    try:
        assert is_valid_system_health(
            validator,
            system_health_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_system_health_count(json_schema_validate, obj):
    json_schema_validate('jsd_96f6dd603bc35db1948f31c782a37647_v3_1_3_0').validate(obj)
    return True


def system_health_count(api):
    endpoint_result = api.health_and_performance.system_health_count(
        domain='string',
        subdomain='string'
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_system_health_count(api, validator):
    try:
        assert is_valid_system_health_count(
            validator,
            system_health_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def system_health_count_default_val(api):
    endpoint_result = api.health_and_performance.system_health_count(
        domain=None,
        subdomain=None
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_system_health_count_default_val(api, validator):
    try:
        assert is_valid_system_health_count(
            validator,
            system_health_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_system_performance(json_schema_validate, obj):
    json_schema_validate('jsd_cfcb7a875f215cb4ba59be38abb871e6_v3_1_3_0').validate(obj)
    return True


def system_performance(api):
    endpoint_result = api.health_and_performance.system_performance(
        end_time=0,
        function='string',
        kpi='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_system_performance(api, validator):
    try:
        assert is_valid_system_performance(
            validator,
            system_performance(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def system_performance_default_val(api):
    endpoint_result = api.health_and_performance.system_performance(
        end_time=None,
        function=None,
        kpi=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_system_performance_default_val(api, validator):
    try:
        assert is_valid_system_performance(
            validator,
            system_performance_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_system_performance_historical(json_schema_validate, obj):
    json_schema_validate('jsd_0f131d712dc253dca528c0298b3e41c6_v3_1_3_0').validate(obj)
    return True


def system_performance_historical(api):
    endpoint_result = api.health_and_performance.system_performance_historical(
        end_time=0,
        kpi='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_system_performance_historical(api, validator):
    try:
        assert is_valid_system_performance_historical(
            validator,
            system_performance_historical(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def system_performance_historical_default_val(api):
    endpoint_result = api.health_and_performance.system_performance_historical(
        end_time=None,
        kpi=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.health_and_performance
def test_system_performance_historical_default_val(api, validator):
    try:
        assert is_valid_system_performance_historical(
            validator,
            system_performance_historical_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

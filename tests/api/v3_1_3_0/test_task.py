# -*- coding: utf-8 -*-
"""CatalystCenterAPI task API fixtures and tests.

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


def is_valid_retrieve_a_list_of_assurance_tasks(json_schema_validate, obj):
    json_schema_validate("jsd_8134704449d65b4492fff74d2a84d710_v3_1_3_0").validate(obj)
    return True


def retrieve_a_list_of_assurance_tasks(api):
    endpoint_result = api.task.retrieve_a_list_of_assurance_tasks(
        limit=0, offset=0, order="string", sort_by="string", status="string"
    )
    return endpoint_result


@pytest.mark.task
def test_retrieve_a_list_of_assurance_tasks(api, validator):
    try:
        assert is_valid_retrieve_a_list_of_assurance_tasks(
            validator, retrieve_a_list_of_assurance_tasks(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_list_of_assurance_tasks_default_val(api):
    endpoint_result = api.task.retrieve_a_list_of_assurance_tasks(
        limit=None, offset=None, order=None, sort_by=None, status=None
    )
    return endpoint_result


@pytest.mark.task
def test_retrieve_a_list_of_assurance_tasks_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_list_of_assurance_tasks(
            validator, retrieve_a_list_of_assurance_tasks_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist(
    json_schema_validate, obj
):
    json_schema_validate("jsd_14cb42937f005b9980039bb76b1b04bc_v3_1_3_0").validate(obj)
    return True


def retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist(api):
    endpoint_result = (
        api.task.retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist(
            status="string"
        )
    )
    return endpoint_result


@pytest.mark.task
def test_retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist(
    api, validator
):
    try:
        assert is_valid_retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist(
            validator,
            retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist_default_val(
    api,
):
    endpoint_result = (
        api.task.retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist(
            status=None
        )
    )
    return endpoint_result


@pytest.mark.task
def test_retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist_default_val(
    api, validator
):
    try:
        assert is_valid_retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist(
            validator,
            retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_specific_assurance_task_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_f8a9bff28df85f64bdf060731d66dc7c_v3_1_3_0").validate(obj)
    return True


def retrieve_a_specific_assurance_task_by_id(api):
    endpoint_result = api.task.retrieve_a_specific_assurance_task_by_id(id="string")
    return endpoint_result


@pytest.mark.task
def test_retrieve_a_specific_assurance_task_by_id(api, validator):
    try:
        assert is_valid_retrieve_a_specific_assurance_task_by_id(
            validator, retrieve_a_specific_assurance_task_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_specific_assurance_task_by_id_default_val(api):
    endpoint_result = api.task.retrieve_a_specific_assurance_task_by_id(id="string")
    return endpoint_result


@pytest.mark.task
def test_retrieve_a_specific_assurance_task_by_id_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_specific_assurance_task_by_id(
            validator, retrieve_a_specific_assurance_task_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_activities(json_schema_validate, obj):
    json_schema_validate("jsd_c6a291ea9c5d5423af5ac96894c7f8b0_v3_1_3_0").validate(obj)
    return True


def get_activities(api):
    endpoint_result = api.task.get_activities(
        description="string",
        end_time="string",
        limit=0,
        offset=0,
        order="string",
        recurring=True,
        sort_by="string",
        start_time="string",
        status="string",
        type="string",
    )
    return endpoint_result


@pytest.mark.task
def test_get_activities(api, validator):
    try:
        assert is_valid_get_activities(validator, get_activities(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_activities_default_val(api):
    endpoint_result = api.task.get_activities(
        description=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        recurring=None,
        sort_by=None,
        start_time=None,
        status=None,
        type=None,
    )
    return endpoint_result


@pytest.mark.task
def test_get_activities_default_val(api, validator):
    try:
        assert is_valid_get_activities(validator, get_activities_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_activities(json_schema_validate, obj):
    json_schema_validate("jsd_eab67fb962e55baea864b1bb17fd78e3_v3_1_3_0").validate(obj)
    return True


def retrieves_the_count_of_activities(api):
    endpoint_result = api.task.retrieves_the_count_of_activities(
        description="string",
        end_time="string",
        recurring=True,
        start_time="string",
        status="string",
        type="string",
    )
    return endpoint_result


@pytest.mark.task
def test_retrieves_the_count_of_activities(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_activities(
            validator, retrieves_the_count_of_activities(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_activities_default_val(api):
    endpoint_result = api.task.retrieves_the_count_of_activities(
        description=None,
        end_time=None,
        recurring=None,
        start_time=None,
        status=None,
        type=None,
    )
    return endpoint_result


@pytest.mark.task
def test_retrieves_the_count_of_activities_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_activities(
            validator, retrieves_the_count_of_activities_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_triggered_jobs_by_activity_id(json_schema_validate, obj):
    json_schema_validate("jsd_6affaf286eb455fc8869939066990765_v3_1_3_0").validate(obj)
    return True


def get_triggered_jobs_by_activity_id(api):
    endpoint_result = api.task.get_triggered_jobs_by_activity_id(
        activity_id="string", limit=0, offset=0, order="string", sort_by="string"
    )
    return endpoint_result


@pytest.mark.task
def test_get_triggered_jobs_by_activity_id(api, validator):
    try:
        assert is_valid_get_triggered_jobs_by_activity_id(
            validator, get_triggered_jobs_by_activity_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_triggered_jobs_by_activity_id_default_val(api):
    endpoint_result = api.task.get_triggered_jobs_by_activity_id(
        activity_id="string", limit=None, offset=None, order=None, sort_by=None
    )
    return endpoint_result


@pytest.mark.task
def test_get_triggered_jobs_by_activity_id_default_val(api, validator):
    try:
        assert is_valid_get_triggered_jobs_by_activity_id(
            validator, get_triggered_jobs_by_activity_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_triggered_jobs_by_activity_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_d235a8436ddd5bb1add2c7bf04940a99_v3_1_3_0").validate(obj)
    return True


def retrieves_the_count_of_triggered_jobs_by_activity_id(api):
    endpoint_result = api.task.retrieves_the_count_of_triggered_jobs_by_activity_id(
        activity_id="string"
    )
    return endpoint_result


@pytest.mark.task
def test_retrieves_the_count_of_triggered_jobs_by_activity_id(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_triggered_jobs_by_activity_id(
            validator, retrieves_the_count_of_triggered_jobs_by_activity_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_triggered_jobs_by_activity_id_default_val(api):
    endpoint_result = api.task.retrieves_the_count_of_triggered_jobs_by_activity_id(
        activity_id="string"
    )
    return endpoint_result


@pytest.mark.task
def test_retrieves_the_count_of_triggered_jobs_by_activity_id_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_count_of_triggered_jobs_by_activity_id(
            validator,
            retrieves_the_count_of_triggered_jobs_by_activity_id_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_business_api_execution_details(json_schema_validate, obj):
    json_schema_validate("jsd_0ffc19ddea705526b7d9db01baf4997e_v3_1_3_0").validate(obj)
    return True


def get_business_api_execution_details(api):
    endpoint_result = api.task.get_business_api_execution_details(execution_id="string")
    return endpoint_result


@pytest.mark.task
def test_get_business_api_execution_details(api, validator):
    try:
        assert is_valid_get_business_api_execution_details(
            validator, get_business_api_execution_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_business_api_execution_details_default_val(api):
    endpoint_result = api.task.get_business_api_execution_details(execution_id="string")
    return endpoint_result


@pytest.mark.task
def test_get_business_api_execution_details_default_val(api, validator):
    try:
        assert is_valid_get_business_api_execution_details(
            validator, get_business_api_execution_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tasks_operational_tasks(json_schema_validate, obj):
    json_schema_validate("jsd_75ff485556f6504d8443789f42098be7_v3_1_3_0").validate(obj)
    return True


def get_tasks_operational_tasks(api):
    endpoint_result = api.task.get_tasks_operational_tasks(
        data="string",
        end_time="string",
        error_code="string",
        failure_reason="string",
        is_error="string",
        limit=0,
        offset=0,
        order="string",
        parent_id="string",
        progress="string",
        service_type="string",
        sort_by="string",
        start_time="string",
        username="string",
    )
    return endpoint_result


@pytest.mark.task
def test_get_tasks_operational_tasks(api, validator):
    try:
        assert is_valid_get_tasks_operational_tasks(
            validator, get_tasks_operational_tasks(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tasks_operational_tasks_default_val(api):
    endpoint_result = api.task.get_tasks_operational_tasks(
        data=None,
        end_time=None,
        error_code=None,
        failure_reason=None,
        is_error=None,
        limit=None,
        offset=None,
        order=None,
        parent_id=None,
        progress=None,
        service_type=None,
        sort_by=None,
        start_time=None,
        username=None,
    )
    return endpoint_result


@pytest.mark.task
def test_get_tasks_operational_tasks_default_val(api, validator):
    try:
        assert is_valid_get_tasks_operational_tasks(
            validator, get_tasks_operational_tasks_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_task_count(json_schema_validate, obj):
    json_schema_validate("jsd_8d0586946be75e0f9f2c170217d45a28_v3_1_3_0").validate(obj)
    return True


def get_task_count(api):
    endpoint_result = api.task.get_task_count(
        data="string",
        end_time="string",
        error_code="string",
        failure_reason="string",
        is_error="string",
        parent_id="string",
        progress="string",
        service_type="string",
        start_time="string",
        username="string",
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_count(api, validator):
    try:
        assert is_valid_get_task_count(validator, get_task_count(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_task_count_default_val(api):
    endpoint_result = api.task.get_task_count(
        data=None,
        end_time=None,
        error_code=None,
        failure_reason=None,
        is_error=None,
        parent_id=None,
        progress=None,
        service_type=None,
        start_time=None,
        username=None,
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_count_default_val(api, validator):
    try:
        assert is_valid_get_task_count(validator, get_task_count_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_task_by_operationid(json_schema_validate, obj):
    json_schema_validate("jsd_d95c21e41dce5a9dbee07d33eefef2b2_v3_1_3_0").validate(obj)
    return True


def get_task_by_operationid(api):
    endpoint_result = api.task.get_task_by_operationid(
        limit=0, offset=0, operation_id="string"
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_by_operationid(api, validator):
    try:
        assert is_valid_get_task_by_operationid(validator, get_task_by_operationid(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_task_by_operationid_default_val(api):
    endpoint_result = api.task.get_task_by_operationid(
        limit=0, offset=0, operation_id="string"
    )
    return endpoint_result


@pytest.mark.task
def test_get_task_by_operationid_default_val(api, validator):
    try:
        assert is_valid_get_task_by_operationid(
            validator, get_task_by_operationid_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_task_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_8009857899a75ba5a6bae1d568700bd3_v3_1_3_0").validate(obj)
    return True


def get_task_by_id(api):
    endpoint_result = api.task.get_task_by_id(task_id="string")
    return endpoint_result


@pytest.mark.task
def test_get_task_by_id(api, validator):
    try:
        assert is_valid_get_task_by_id(validator, get_task_by_id(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_task_by_id_default_val(api):
    endpoint_result = api.task.get_task_by_id(task_id="string")
    return endpoint_result


@pytest.mark.task
def test_get_task_by_id_default_val(api, validator):
    try:
        assert is_valid_get_task_by_id(validator, get_task_by_id_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_task_tree(json_schema_validate, obj):
    json_schema_validate("jsd_8fa2865e229b536aacd59585a1d29704_v3_1_3_0").validate(obj)
    return True


def get_task_tree(api):
    endpoint_result = api.task.get_task_tree(task_id="string")
    return endpoint_result


@pytest.mark.task
def test_get_task_tree(api, validator):
    try:
        assert is_valid_get_task_tree(validator, get_task_tree(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_task_tree_default_val(api):
    endpoint_result = api.task.get_task_tree(task_id="string")
    return endpoint_result


@pytest.mark.task
def test_get_task_tree_default_val(api, validator):
    try:
        assert is_valid_get_task_tree(validator, get_task_tree_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tasks(json_schema_validate, obj):
    json_schema_validate("jsd_b485e8aa7d9150ddb5048aa3b0617866_v3_1_3_0").validate(obj)
    return True


def get_tasks(api):
    endpoint_result = api.task.get_tasks(
        end_time=0,
        limit=0,
        offset=0,
        order="string",
        parent_id="string",
        root_id="string",
        sort_by="string",
        start_time=0,
        status="string",
    )
    return endpoint_result


@pytest.mark.task
def test_get_tasks(api, validator):
    try:
        assert is_valid_get_tasks(validator, get_tasks(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tasks_default_val(api):
    endpoint_result = api.task.get_tasks(
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        parent_id=None,
        root_id=None,
        sort_by=None,
        start_time=None,
        status=None,
    )
    return endpoint_result


@pytest.mark.task
def test_get_tasks_default_val(api, validator):
    try:
        assert is_valid_get_tasks(validator, get_tasks_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tasks_count(json_schema_validate, obj):
    json_schema_validate("jsd_90ff937b756f5eec9f5cd519ea6e9fec_v3_1_3_0").validate(obj)
    return True


def get_tasks_count(api):
    endpoint_result = api.task.get_tasks_count(
        end_time=0, parent_id="string", root_id="string", start_time=0, status="string"
    )
    return endpoint_result


@pytest.mark.task
def test_get_tasks_count(api, validator):
    try:
        assert is_valid_get_tasks_count(validator, get_tasks_count(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tasks_count_default_val(api):
    endpoint_result = api.task.get_tasks_count(
        end_time=None, parent_id=None, root_id=None, start_time=None, status=None
    )
    return endpoint_result


@pytest.mark.task
def test_get_tasks_count_default_val(api, validator):
    try:
        assert is_valid_get_tasks_count(validator, get_tasks_count_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tasks_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_ffc437c17db355ae92597ce411cec6c8_v3_1_3_0").validate(obj)
    return True


def get_tasks_by_id(api):
    endpoint_result = api.task.get_tasks_by_id(id="string")
    return endpoint_result


@pytest.mark.task
def test_get_tasks_by_id(api, validator):
    try:
        assert is_valid_get_tasks_by_id(validator, get_tasks_by_id(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tasks_by_id_default_val(api):
    endpoint_result = api.task.get_tasks_by_id(id="string")
    return endpoint_result


@pytest.mark.task
def test_get_tasks_by_id_default_val(api, validator):
    try:
        assert is_valid_get_tasks_by_id(validator, get_tasks_by_id_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_task_details_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_a48eee2b20065722ba9688176af178c1_v3_1_3_0").validate(obj)
    return True


def get_task_details_by_id(api):
    endpoint_result = api.task.get_task_details_by_id(id="string")
    return endpoint_result


@pytest.mark.task
def test_get_task_details_by_id(api, validator):
    try:
        assert is_valid_get_task_details_by_id(validator, get_task_details_by_id(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_task_details_by_id_default_val(api):
    endpoint_result = api.task.get_task_details_by_id(id="string")
    return endpoint_result


@pytest.mark.task
def test_get_task_details_by_id_default_val(api, validator):
    try:
        assert is_valid_get_task_details_by_id(
            validator, get_task_details_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_activity_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_88c8c7108e4f52c783a2703cf19e6c8c_v3_1_3_0").validate(obj)
    return True


def get_activity_by_id(api):
    endpoint_result = api.task.get_activity_by_id(id="string")
    return endpoint_result


@pytest.mark.task
def test_get_activity_by_id(api, validator):
    try:
        assert is_valid_get_activity_by_id(validator, get_activity_by_id(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_activity_by_id_default_val(api):
    endpoint_result = api.task.get_activity_by_id(id="string")
    return endpoint_result


@pytest.mark.task
def test_get_activity_by_id_default_val(api, validator):
    try:
        assert is_valid_get_activity_by_id(
            validator, get_activity_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

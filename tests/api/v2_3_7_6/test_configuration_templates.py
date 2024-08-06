# -*- coding: utf-8 -*-
"""DNACenterAPI configuration_templates API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.6', reason='version does not match')


def is_valid_clone_given_template(json_schema_validate, obj):
    json_schema_validate('jsd_feb800c6888f5b13972467f0e3416ec2_v2_3_7_6').validate(obj)
    return True


def clone_given_template(api):
    endpoint_result = api.configuration_templates.clone_given_template(
        active_validation=True,
        name='string',
        payload=None,
        project_id='string',
        template_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_clone_given_template(api, validator):
    try:
        assert is_valid_clone_given_template(
            validator,
            clone_given_template(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def clone_given_template_default_val(api):
    endpoint_result = api.configuration_templates.clone_given_template(
        active_validation=True,
        name='string',
        payload=None,
        project_id='string',
        project_id=None,
        template_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_clone_given_template_default_val(api, validator):
    try:
        assert is_valid_clone_given_template(
            validator,
            clone_given_template_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_project(json_schema_validate, obj):
    json_schema_validate('jsd_8548ecc3258a5c5b8f2267a512820a59_v2_3_7_6').validate(obj)
    return True


def create_project(api):
    endpoint_result = api.configuration_templates.create_project(
        active_validation=True,
        createTime=0,
        description='string',
        id='string',
        lastUpdateTime=0,
        name='string',
        payload=None,
        tags=[{'id': 'string', 'name': 'string'}],
        templates=[{}]
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_create_project(api, validator):
    try:
        assert is_valid_create_project(
            validator,
            create_project(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_project_default_val(api):
    endpoint_result = api.configuration_templates.create_project(
        active_validation=True,
        createTime=None,
        description=None,
        id=None,
        lastUpdateTime=None,
        name=None,
        payload=None,
        tags=None,
        templates=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_create_project_default_val(api, validator):
    try:
        assert is_valid_create_project(
            validator,
            create_project_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_project(json_schema_validate, obj):
    json_schema_validate('jsd_cc19241fd92f586c8986d4d5c99c3a88_v2_3_7_6').validate(obj)
    return True


def update_project(api):
    endpoint_result = api.configuration_templates.update_project(
        active_validation=True,
        createTime=0,
        description='string',
        id='string',
        lastUpdateTime=0,
        name='string',
        payload=None,
        tags=[{'id': 'string', 'name': 'string'}],
        templates={}
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_update_project(api, validator):
    try:
        assert is_valid_update_project(
            validator,
            update_project(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_project_default_val(api):
    endpoint_result = api.configuration_templates.update_project(
        active_validation=True,
        createTime=None,
        description=None,
        id=None,
        lastUpdateTime=None,
        name=None,
        payload=None,
        tags=None,
        templates=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_update_project_default_val(api, validator):
    try:
        assert is_valid_update_project(
            validator,
            update_project_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_projects(json_schema_validate, obj):
    json_schema_validate('jsd_56b942797fc158e3a0fbb5ffb1347962_v2_3_7_6').validate(obj)
    return True


def get_projects(api):
    endpoint_result = api.configuration_templates.get_projects(
        name='string',
        sort_order='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_projects(api, validator):
    try:
        assert is_valid_get_projects(
            validator,
            get_projects(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_projects_default_val(api):
    endpoint_result = api.configuration_templates.get_projects(
        name=None,
        sort_order=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_projects_default_val(api, validator):
    try:
        assert is_valid_get_projects(
            validator,
            get_projects_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_imports_the_projects_provided(json_schema_validate, obj):
    json_schema_validate('jsd_dec1857f1585557eb39e12a9c93ef985_v2_3_7_6').validate(obj)
    return True


def imports_the_projects_provided(api):
    endpoint_result = api.configuration_templates.imports_the_projects_provided(
        active_validation=True,
        do_version=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_imports_the_projects_provided(api, validator):
    try:
        assert is_valid_imports_the_projects_provided(
            validator,
            imports_the_projects_provided(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def imports_the_projects_provided_default_val(api):
    endpoint_result = api.configuration_templates.imports_the_projects_provided(
        active_validation=True,
        do_version=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_imports_the_projects_provided_default_val(api, validator):
    try:
        assert is_valid_imports_the_projects_provided(
            validator,
            imports_the_projects_provided_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_export_projects(json_schema_validate, obj):
    json_schema_validate('jsd_49e6ea8c5d425cf9ac77006f5593725f_v2_3_7_6').validate(obj)
    return True


def export_projects(api):
    endpoint_result = api.configuration_templates.export_projects(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_export_projects(api, validator):
    try:
        assert is_valid_export_projects(
            validator,
            export_projects(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def export_projects_default_val(api):
    endpoint_result = api.configuration_templates.export_projects(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_export_projects_default_val(api, validator):
    try:
        assert is_valid_export_projects(
            validator,
            export_projects_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_imports_the_templates_provided(json_schema_validate, obj):
    json_schema_validate('jsd_706db7b6c4f0542aab9fe7cf5c995f83_v2_3_7_6').validate(obj)
    return True


def imports_the_templates_provided(api):
    endpoint_result = api.configuration_templates.imports_the_templates_provided(
        active_validation=True,
        do_version=True,
        payload=None,
        project_name='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_imports_the_templates_provided(api, validator):
    try:
        assert is_valid_imports_the_templates_provided(
            validator,
            imports_the_templates_provided(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def imports_the_templates_provided_default_val(api):
    endpoint_result = api.configuration_templates.imports_the_templates_provided(
        active_validation=True,
        do_version=None,
        payload=None,
        project_name='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_imports_the_templates_provided_default_val(api, validator):
    try:
        assert is_valid_imports_the_templates_provided(
            validator,
            imports_the_templates_provided_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_project_details(json_schema_validate, obj):
    json_schema_validate('jsd_c1b2c35764f2518182b3f271a29a574c_v2_3_7_6').validate(obj)
    return True


def get_project_details(api):
    endpoint_result = api.configuration_templates.get_project_details(
        project_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_project_details(api, validator):
    try:
        assert is_valid_get_project_details(
            validator,
            get_project_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_project_details_default_val(api):
    endpoint_result = api.configuration_templates.get_project_details(
        project_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_project_details_default_val(api, validator):
    try:
        assert is_valid_get_project_details(
            validator,
            get_project_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_the_project(json_schema_validate, obj):
    json_schema_validate('jsd_a3e0588fa1ac56d4947ae5cfc2e16a8f_v2_3_7_6').validate(obj)
    return True


def deletes_the_project(api):
    endpoint_result = api.configuration_templates.deletes_the_project(
        project_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_deletes_the_project(api, validator):
    try:
        assert is_valid_deletes_the_project(
            validator,
            deletes_the_project(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_the_project_default_val(api):
    endpoint_result = api.configuration_templates.deletes_the_project(
        project_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_deletes_the_project_default_val(api, validator):
    try:
        assert is_valid_deletes_the_project(
            validator,
            deletes_the_project_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_template(json_schema_validate, obj):
    json_schema_validate('jsd_e3e170003d865b9a8d76cbe1d2f268be_v2_3_7_6').validate(obj)
    return True


def create_template(api):
    endpoint_result = api.configuration_templates.create_template(
        active_validation=True,
        author='string',
        composite=True,
        containingTemplates=[{'tags': [{'id': 'string', 'name': 'string'}], 'composite': True, 'description': 'string', 'deviceTypes': [{'productFamily': 'string', 'productSeries': 'string', 'productType': 'string'}], 'id': 'string', 'language': 'string', 'name': 'string', 'projectName': 'string', 'rollbackTemplateParams': [{'binding': 'string', 'customOrder': 0, 'dataType': 'string', 'defaultValue': 'string', 'description': 'string', 'displayName': 'string', 'group': 'string', 'id': 'string', 'instructionText': 'string', 'key': 'string', 'notParam': True, 'order': 0, 'paramArray': True, 'parameterName': 'string', 'provider': 'string', 'range': [{'id': 'string', 'maxValue': 0, 'minValue': 0}], 'required': True, 'selection': {'defaultSelectedValues': ['string'], 'id': 'string', 'selectionType': 'string', 'selectionValues': {}}}], 'templateContent': 'string', 'templateParams': [{'binding': 'string', 'customOrder': 0, 'dataType': 'string', 'defaultValue': 'string', 'description': 'string', 'displayName': 'string', 'group': 'string', 'id': 'string', 'instructionText': 'string', 'key': 'string', 'notParam': True, 'order': 0, 'paramArray': True, 'parameterName': 'string', 'provider': 'string', 'range': [{'id': 'string', 'maxValue': 0, 'minValue': 0}], 'required': True, 'selection': {'defaultSelectedValues': ['string'], 'id': 'string', 'selectionType': 'string', 'selectionValues': {}}}], 'version': 'string'}],
        createTime=0,
        customParamsOrder=True,
        description='string',
        deviceTypes=[{'productFamily': 'string', 'productSeries': 'string', 'productType': 'string'}],
        failurePolicy='string',
        id='string',
        language='string',
        lastUpdateTime=0,
        latestVersionTime=0,
        name='string',
        parentTemplateId='string',
        payload=None,
        projectId='string',
        projectName='string',
        project_id='string',
        rollbackTemplateContent='string',
        rollbackTemplateParams=[{'binding': 'string', 'customOrder': 0, 'dataType': 'string', 'defaultValue': 'string', 'description': 'string', 'displayName': 'string', 'group': 'string', 'id': 'string', 'instructionText': 'string', 'key': 'string', 'notParam': True, 'order': 0, 'paramArray': True, 'parameterName': 'string', 'provider': 'string', 'range': [{'id': 'string', 'maxValue': 0, 'minValue': 0}], 'required': True, 'selection': {'defaultSelectedValues': ['string'], 'id': 'string', 'selectionType': 'string', 'selectionValues': {}}}],
        softwareType='string',
        softwareVariant='string',
        softwareVersion='string',
        tags=[{'id': 'string', 'name': 'string'}],
        templateContent='string',
        templateParams=[{'binding': 'string', 'customOrder': 0, 'dataType': 'string', 'defaultValue': 'string', 'description': 'string', 'displayName': 'string', 'group': 'string', 'id': 'string', 'instructionText': 'string', 'key': 'string', 'notParam': True, 'order': 0, 'paramArray': True, 'parameterName': 'string', 'provider': 'string', 'range': [{'id': 'string', 'maxValue': 0, 'minValue': 0}], 'required': True, 'selection': {'defaultSelectedValues': ['string'], 'id': 'string', 'selectionType': 'string', 'selectionValues': {}}}],
        validationErrors={'rollbackTemplateErrors': {}, 'templateErrors': {}, 'templateId': 'string', 'templateVersion': 'string'},
        version='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_create_template(api, validator):
    try:
        assert is_valid_create_template(
            validator,
            create_template(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_template_default_val(api):
    endpoint_result = api.configuration_templates.create_template(
        active_validation=True,
        author=None,
        composite=None,
        containingTemplates=None,
        createTime=None,
        customParamsOrder=None,
        description=None,
        deviceTypes=None,
        failurePolicy=None,
        id=None,
        language=None,
        lastUpdateTime=None,
        latestVersionTime=None,
        name=None,
        parentTemplateId=None,
        payload=None,
        projectId=None,
        projectName=None,
        project_id='string',
        rollbackTemplateContent=None,
        rollbackTemplateParams=None,
        softwareType=None,
        softwareVariant=None,
        softwareVersion=None,
        tags=None,
        templateContent=None,
        templateParams=None,
        validationErrors=None,
        version=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_create_template_default_val(api, validator):
    try:
        assert is_valid_create_template(
            validator,
            create_template_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_templates_available(json_schema_validate, obj):
    json_schema_validate('jsd_027bdc3bc8a35908aba5858e78805d22_v2_3_7_6').validate(obj)
    return True


def gets_the_templates_available(api):
    endpoint_result = api.configuration_templates.gets_the_templates_available(
        filter_conflicting_templates=True,
        product_family='string',
        product_series='string',
        product_type='string',
        project_id='string',
        project_names='value1,value2',
        software_type='string',
        software_version='string',
        sort_order='string',
        tags='value1,value2',
        un_committed=True
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_gets_the_templates_available(api, validator):
    try:
        assert is_valid_gets_the_templates_available(
            validator,
            gets_the_templates_available(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_templates_available_default_val(api):
    endpoint_result = api.configuration_templates.gets_the_templates_available(
        filter_conflicting_templates=None,
        product_family=None,
        product_series=None,
        product_type=None,
        project_id=None,
        project_names=None,
        software_type=None,
        software_version=None,
        sort_order=None,
        tags=None,
        un_committed=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_gets_the_templates_available_default_val(api, validator):
    try:
        assert is_valid_gets_the_templates_available(
            validator,
            gets_the_templates_available_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_template(json_schema_validate, obj):
    json_schema_validate('jsd_7dbea7d7de125cf6b840d5032d3a5c59_v2_3_7_6').validate(obj)
    return True


def update_template(api):
    endpoint_result = api.configuration_templates.update_template(
        active_validation=True,
        author='string',
        composite=True,
        containingTemplates=[{'tags': [{'id': 'string', 'name': 'string'}], 'composite': True, 'description': 'string', 'deviceTypes': [{'productFamily': 'string', 'productSeries': 'string', 'productType': 'string'}], 'id': 'string', 'language': 'string', 'name': 'string', 'projectName': 'string', 'rollbackTemplateParams': [{'binding': 'string', 'customOrder': 0, 'dataType': 'string', 'defaultValue': 'string', 'description': 'string', 'displayName': 'string', 'group': 'string', 'id': 'string', 'instructionText': 'string', 'key': 'string', 'notParam': True, 'order': 0, 'paramArray': True, 'parameterName': 'string', 'provider': 'string', 'range': [{'id': 'string', 'maxValue': 0, 'minValue': 0}], 'required': True, 'selection': {'defaultSelectedValues': ['string'], 'id': 'string', 'selectionType': 'string', 'selectionValues': {}}}], 'templateContent': 'string', 'templateParams': [{'binding': 'string', 'customOrder': 0, 'dataType': 'string', 'defaultValue': 'string', 'description': 'string', 'displayName': 'string', 'group': 'string', 'id': 'string', 'instructionText': 'string', 'key': 'string', 'notParam': True, 'order': 0, 'paramArray': True, 'parameterName': 'string', 'provider': 'string', 'range': [{'id': 'string', 'maxValue': 0, 'minValue': 0}], 'required': True, 'selection': {'defaultSelectedValues': ['string'], 'id': 'string', 'selectionType': 'string', 'selectionValues': {}}}], 'version': 'string'}],
        createTime=0,
        customParamsOrder=True,
        description='string',
        deviceTypes=[{'productFamily': 'string', 'productSeries': 'string', 'productType': 'string'}],
        failurePolicy='string',
        id='string',
        language='string',
        lastUpdateTime=0,
        latestVersionTime=0,
        name='string',
        parentTemplateId='string',
        payload=None,
        projectId='string',
        projectName='string',
        rollbackTemplateContent='string',
        rollbackTemplateParams=[{'binding': 'string', 'customOrder': 0, 'dataType': 'string', 'defaultValue': 'string', 'description': 'string', 'displayName': 'string', 'group': 'string', 'id': 'string', 'instructionText': 'string', 'key': 'string', 'notParam': True, 'order': 0, 'paramArray': True, 'parameterName': 'string', 'provider': 'string', 'range': [{'id': 'string', 'maxValue': 0, 'minValue': 0}], 'required': True, 'selection': {'defaultSelectedValues': ['string'], 'id': 'string', 'selectionType': 'string', 'selectionValues': {}}}],
        softwareType='string',
        softwareVariant='string',
        softwareVersion='string',
        tags=[{'id': 'string', 'name': 'string'}],
        templateContent='string',
        templateParams=[{'binding': 'string', 'customOrder': 0, 'dataType': 'string', 'defaultValue': 'string', 'description': 'string', 'displayName': 'string', 'group': 'string', 'id': 'string', 'instructionText': 'string', 'key': 'string', 'notParam': True, 'order': 0, 'paramArray': True, 'parameterName': 'string', 'provider': 'string', 'range': [{'id': 'string', 'maxValue': 0, 'minValue': 0}], 'required': True, 'selection': {'defaultSelectedValues': ['string'], 'id': 'string', 'selectionType': 'string', 'selectionValues': {}}}],
        validationErrors={'rollbackTemplateErrors': {}, 'templateErrors': {}, 'templateId': 'string', 'templateVersion': 'string'},
        version='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_update_template(api, validator):
    try:
        assert is_valid_update_template(
            validator,
            update_template(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_template_default_val(api):
    endpoint_result = api.configuration_templates.update_template(
        active_validation=True,
        author=None,
        composite=None,
        containingTemplates=None,
        createTime=None,
        customParamsOrder=None,
        description=None,
        deviceTypes=None,
        failurePolicy=None,
        id=None,
        language=None,
        lastUpdateTime=None,
        latestVersionTime=None,
        name=None,
        parentTemplateId=None,
        payload=None,
        projectId=None,
        projectName=None,
        rollbackTemplateContent=None,
        rollbackTemplateParams=None,
        softwareType=None,
        softwareVariant=None,
        softwareVersion=None,
        tags=None,
        templateContent=None,
        templateParams=None,
        validationErrors=None,
        version=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_update_template_default_val(api, validator):
    try:
        assert is_valid_update_template(
            validator,
            update_template_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_template(json_schema_validate, obj):
    json_schema_validate('jsd_847875efa92557c9a6c8af0a71829c7e_v2_3_7_6').validate(obj)
    return True


def deploy_template(api):
    endpoint_result = api.configuration_templates.deploy_template(
        active_validation=True,
        forcePushTemplate=True,
        isComposite=True,
        mainTemplateId='string',
        memberTemplateDeploymentInfo=[{}],
        payload=None,
        targetInfo=[{'hostName': 'string', 'id': 'string', 'params': {}, 'resourceParams': ['string'], 'type': 'string', 'versionedTemplateId': 'string'}],
        templateId='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_deploy_template(api, validator):
    try:
        assert is_valid_deploy_template(
            validator,
            deploy_template(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_template_default_val(api):
    endpoint_result = api.configuration_templates.deploy_template(
        active_validation=True,
        forcePushTemplate=None,
        isComposite=None,
        mainTemplateId=None,
        memberTemplateDeploymentInfo=None,
        payload=None,
        targetInfo=None,
        templateId=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_deploy_template_default_val(api, validator):
    try:
        assert is_valid_deploy_template(
            validator,
            deploy_template_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_template_deployment_status(json_schema_validate, obj):
    json_schema_validate('jsd_6e1f17b174e955dea2ae9d98264de307_v2_3_7_6').validate(obj)
    return True


def get_template_deployment_status(api):
    endpoint_result = api.configuration_templates.get_template_deployment_status(
        deployment_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_template_deployment_status(api, validator):
    try:
        assert is_valid_get_template_deployment_status(
            validator,
            get_template_deployment_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_template_deployment_status_default_val(api):
    endpoint_result = api.configuration_templates.get_template_deployment_status(
        deployment_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_template_deployment_status_default_val(api, validator):
    try:
        assert is_valid_get_template_deployment_status(
            validator,
            get_template_deployment_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_export_templates(json_schema_validate, obj):
    json_schema_validate('jsd_dc254215fdf25cd5b7ba797e8f8faebf_v2_3_7_6').validate(obj)
    return True


def export_templates(api):
    endpoint_result = api.configuration_templates.export_templates(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_export_templates(api, validator):
    try:
        assert is_valid_export_templates(
            validator,
            export_templates(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def export_templates_default_val(api):
    endpoint_result = api.configuration_templates.export_templates(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_export_templates_default_val(api, validator):
    try:
        assert is_valid_export_templates(
            validator,
            export_templates_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_preview_template(json_schema_validate, obj):
    json_schema_validate('jsd_ccbf614b4b355cac929f12cc61272c1c_v2_3_7_6').validate(obj)
    return True


def preview_template(api):
    endpoint_result = api.configuration_templates.preview_template(
        active_validation=True,
        deviceId='string',
        params={},
        payload=None,
        resourceParams={},
        templateId='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_preview_template(api, validator):
    try:
        assert is_valid_preview_template(
            validator,
            preview_template(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def preview_template_default_val(api):
    endpoint_result = api.configuration_templates.preview_template(
        active_validation=True,
        deviceId=None,
        params=None,
        payload=None,
        resourceParams=None,
        templateId=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_preview_template_default_val(api, validator):
    try:
        assert is_valid_preview_template(
            validator,
            preview_template_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_version_template(json_schema_validate, obj):
    json_schema_validate('jsd_13e1a76c121857a085149e62e56caadd_v2_3_7_6').validate(obj)
    return True


def version_template(api):
    endpoint_result = api.configuration_templates.version_template(
        active_validation=True,
        comments='string',
        payload=None,
        templateId='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_version_template(api, validator):
    try:
        assert is_valid_version_template(
            validator,
            version_template(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def version_template_default_val(api):
    endpoint_result = api.configuration_templates.version_template(
        active_validation=True,
        comments=None,
        payload=None,
        templateId=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_version_template_default_val(api, validator):
    try:
        assert is_valid_version_template(
            validator,
            version_template_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_template_versions(json_schema_validate, obj):
    return True if obj else False


def get_template_versions(api):
    endpoint_result = api.configuration_templates.get_template_versions(
        template_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_template_versions(api, validator):
    try:
        assert is_valid_get_template_versions(
            validator,
            get_template_versions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_template_versions_default_val(api):
    endpoint_result = api.configuration_templates.get_template_versions(
        template_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_template_versions_default_val(api, validator):
    try:
        assert is_valid_get_template_versions(
            validator,
            get_template_versions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_the_template(json_schema_validate, obj):
    json_schema_validate('jsd_c311bd3d952757b2a7b98a5bc5aa6137_v2_3_7_6').validate(obj)
    return True


def deletes_the_template(api):
    endpoint_result = api.configuration_templates.deletes_the_template(
        template_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_deletes_the_template(api, validator):
    try:
        assert is_valid_deletes_the_template(
            validator,
            deletes_the_template(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_the_template_default_val(api):
    endpoint_result = api.configuration_templates.deletes_the_template(
        template_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_deletes_the_template_default_val(api, validator):
    try:
        assert is_valid_deletes_the_template(
            validator,
            deletes_the_template_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_template_details(json_schema_validate, obj):
    json_schema_validate('jsd_d6dbb8874d3150858c1ca6feb7e09edf_v2_3_7_6').validate(obj)
    return True


def get_template_details(api):
    endpoint_result = api.configuration_templates.get_template_details(
        latest_version=True,
        template_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_template_details(api, validator):
    try:
        assert is_valid_get_template_details(
            validator,
            get_template_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_template_details_default_val(api):
    endpoint_result = api.configuration_templates.get_template_details(
        latest_version=None,
        template_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_template_details_default_val(api, validator):
    try:
        assert is_valid_get_template_details(
            validator,
            get_template_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_projects_details(json_schema_validate, obj):
    json_schema_validate('jsd_2074b1fbcb8a5286936915883ec1a0cc_v2_3_7_6').validate(obj)
    return True


def get_projects_details(api):
    endpoint_result = api.configuration_templates.get_projects_details(
        id='string',
        limit=0,
        name='string',
        offset=0,
        sort_order='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_projects_details(api, validator):
    try:
        assert is_valid_get_projects_details(
            validator,
            get_projects_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_projects_details_default_val(api):
    endpoint_result = api.configuration_templates.get_projects_details(
        id=None,
        limit=None,
        name=None,
        offset=None,
        sort_order=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_projects_details_default_val(api, validator):
    try:
        assert is_valid_get_projects_details(
            validator,
            get_projects_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_templates_details(json_schema_validate, obj):
    json_schema_validate('jsd_8915c55b3c31568294840b4b6fd8bc0a_v2_3_7_6').validate(obj)
    return True


def get_templates_details(api):
    endpoint_result = api.configuration_templates.get_templates_details(
        all_template_attributes=True,
        filter_conflicting_templates=True,
        id='string',
        include_version_details=True,
        limit=0,
        name='string',
        offset=0,
        product_family='string',
        product_series='string',
        product_type='string',
        project_id='string',
        project_name='string',
        software_type='string',
        software_version='string',
        sort_order='string',
        tags='value1,value2',
        un_committed=True
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_templates_details(api, validator):
    try:
        assert is_valid_get_templates_details(
            validator,
            get_templates_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_templates_details_default_val(api):
    endpoint_result = api.configuration_templates.get_templates_details(
        all_template_attributes=None,
        filter_conflicting_templates=None,
        id=None,
        include_version_details=None,
        limit=None,
        name=None,
        offset=None,
        product_family=None,
        product_series=None,
        product_type=None,
        project_id=None,
        project_name=None,
        software_type=None,
        software_version=None,
        sort_order=None,
        tags=None,
        un_committed=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_get_templates_details_default_val(api, validator):
    try:
        assert is_valid_get_templates_details(
            validator,
            get_templates_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_template_v2(json_schema_validate, obj):
    json_schema_validate('jsd_bf40cea4982c54278a52ac2e7b0c458a_v2_3_7_6').validate(obj)
    return True


def deploy_template_v2(api):
    endpoint_result = api.configuration_templates.deploy_template_v2(
        active_validation=True,
        forcePushTemplate=True,
        isComposite=True,
        mainTemplateId='string',
        memberTemplateDeploymentInfo=[{}],
        payload=None,
        targetInfo=[{'hostName': 'string', 'id': 'string', 'params': {}, 'resourceParams': [{}], 'type': 'string', 'versionedTemplateId': 'string'}],
        templateId='string'
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_deploy_template_v2(api, validator):
    try:
        assert is_valid_deploy_template_v2(
            validator,
            deploy_template_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_template_v2_default_val(api):
    endpoint_result = api.configuration_templates.deploy_template_v2(
        active_validation=True,
        forcePushTemplate=None,
        isComposite=None,
        mainTemplateId=None,
        memberTemplateDeploymentInfo=None,
        payload=None,
        targetInfo=None,
        templateId=None
    )
    return endpoint_result


@pytest.mark.configuration_templates
def test_deploy_template_v2_default_val(api, validator):
    try:
        assert is_valid_deploy_template_v2(
            validator,
            deploy_template_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

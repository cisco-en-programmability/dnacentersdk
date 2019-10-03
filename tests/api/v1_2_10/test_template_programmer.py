# -*- coding: utf-8 -*-
"""DNACenterAPI template_programmer API fixtures and tests.

Copyright (c) 2019 Cisco and/or its affiliates.

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
import dnacentersdk
import time
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_gets_the_templates_available(obj):
    json_schema_validate('jsd_01b09a254b9ab259_v1_2_10').validate(obj)
    return True


def gets_the_templates_available(api):
    endpoint_result = api.template_programmer.gets_the_templates_available(
        filter_conflicting_templates=None,
        product_family=None,
        product_series=None,
        product_type=None,
        project_id=None,
        software_type=None,
        software_version=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_gets_the_templates_available(api):
    assert is_valid_gets_the_templates_available(
        gets_the_templates_available(api)
    )


def is_valid_get_projects(obj):
    json_schema_validate('jsd_109d1b4f4289aecd_v1_2_10').validate(obj)
    return True


def get_projects(api):
    endpoint_result = api.template_programmer.get_projects(
        name=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_get_projects(api):
    assert is_valid_get_projects(
        get_projects(api)
    )


def is_valid_get_template_details(obj):
    json_schema_validate('jsd_83a3b9404cb88787_v1_2_10').validate(obj)
    return True


def get_template_details(api):
    templates_available = gets_the_templates_available(api)
    projects = get_projects(api)
    if len(projects) > 0 and len(projects[0].templates) > 0:
        templateID = projects[0].templates[0].id
    if len(templates_available) > 0:
        templateID = templates_available[0].templateId
    endpoint_result = api.template_programmer.get_template_details(
        template_id=templateID,
        latest_version=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_get_template_details(api):
    assert is_valid_get_template_details(
        get_template_details(api)
    )


def is_valid_get_template_versions(obj):
    json_schema_validate('jsd_c8bf6b65414a9bc7_v1_2_10').validate(obj)
    return True


def get_template_versions(api):
    templates_available = gets_the_templates_available(api)
    projects = get_projects(api)
    if len(projects) > 0 and len(projects[0].templates) > 0:
        templateID = projects[0].templates[0].id
    if len(templates_available) > 0:
        templateID = templates_available[0].templateId
    endpoint_result = api.template_programmer.get_template_versions(
        template_id=templateID,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_get_template_versions(api):
    assert is_valid_get_template_versions(
        get_template_versions(api)
    )


def is_valid_create_project(obj):
    json_schema_validate('jsd_00aec9b1422ab27e_v1_2_10').validate(obj)
    return True


def create_project(api):
    endpoint_result = api.template_programmer.create_project(
        createTime=None,
        description=None,
        id=None,
        lastUpdateTime=None,
        name='test_project',
        tags=None,
        templates=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_create_project(api):
    assert is_valid_create_project(
        create_project(api)
    )


def is_valid_create_template(obj):
    json_schema_validate('jsd_f6b119ad4d4aaf16_v1_2_10').validate(obj)
    return True


def create_template(api):
    projects = api.template_programmer.get_projects()
    filtered_project = list(filter(lambda x: x.name == 'test_project', projects))
    endpoint_result = api.template_programmer.create_template(
        project_id=filtered_project[0].id,
        author=None,
        composite=False,
        containingTemplates=[],
        createTime=None,
        description=None,
        deviceTypes=[
            {
                "productFamily": "Switches and Hubs",
                # "productSeries": "Cisco Catalyst 9300 Series Switches",
                # "productType": "Cisco Catalyst 9300 Switch"
            }
        ],
        failurePolicy=None,
        id=None,
        lastUpdateTime=None,
        name='test_template',
        parentTemplateId=None,
        projectId=None,
        projectName=None,
        rollbackTemplateContent='',
        rollbackTemplateParams=[],
        softwareType='IOS-XE',
        softwareVariant='XE',
        softwareVersion=None,
        tags=None,
        templateContent='show version\n',
        templateParams=[],
        version=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_create_template(api):
    assert is_valid_create_template(
        create_template(api)
    )


def is_valid_update_template(obj):
    json_schema_validate('jsd_7781fa0548a98342_v1_2_10').validate(obj)
    return True


def update_template(api):
    projects = api.template_programmer.get_projects()
    filtered_project = list(filter(lambda x: x.name == 'test_project', projects))
    template = api.template_programmer.get_template_details(template_id=filtered_project[0].templates[0].id)
    endpoint_result = api.template_programmer.update_template(
        author=None,
        composite=template.composite,
        containingTemplates=template.containingTemplates,
        createTime=None,
        description=None,
        deviceTypes=template.deviceTypes,
        failurePolicy=None,
        id=template.id,
        lastUpdateTime=None,
        name=template.name + '_updated',
        parentTemplateId=None,
        projectId=template.projectId,
        projectName=None,
        rollbackTemplateContent=template.rollbackTemplateContent,
        rollbackTemplateParams=template.rollbackTemplateParams,
        softwareType=template.softwareType,
        softwareVariant=template.softwareVariant,
        softwareVersion=None,
        tags=None,
        templateContent=template.templateContent,
        templateParams=template.templateParams,
        version=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_update_template(api):
    assert is_valid_update_template(
        update_template(api)
    )


def is_valid_update_project(obj):
    json_schema_validate('jsd_9480fa1f47ca9254_v1_2_10').validate(obj)
    return True


def update_project(api):
    projects = api.template_programmer.get_projects()
    filtered_project = list(filter(lambda x: x.name == 'test_project', projects))
    endpoint_result = api.template_programmer.update_project(
        createTime=None,
        description=None,
        id=filtered_project[0].id,
        lastUpdateTime=None,
        name=filtered_project[0].name + '_updated',
        tags=None,
        templates=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_update_project(api):
    assert is_valid_update_project(
        update_project(api)
    )


def is_valid_version_template(obj):
    json_schema_validate('jsd_62b05b2c40a9b216_v1_2_10').validate(obj)
    return True


def version_template(api):
    projects = api.template_programmer.get_projects()
    filtered_project = list(filter(lambda x: x.name == 'test_project_updated', projects))
    template = api.template_programmer.get_template_details(template_id=filtered_project[0].templates[0].id)
    endpoint_result = api.template_programmer.version_template(
        comments=None,
        templateId=template.id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_version_template(api):
    assert is_valid_version_template(
        version_template(api)
    )


def is_valid_preview_template(obj):
    json_schema_validate('jsd_f393abe84989bb48_v1_2_10').validate(obj)
    return True


def preview_template(api):
    projects = api.template_programmer.get_projects()
    filtered_project = list(filter(lambda x: x.name == 'test_project_updated', projects))
    template = api.template_programmer.get_template_details(template_id=filtered_project[0].templates[0].id)
    endpoint_result = api.template_programmer.preview_template(
        params=None,
        templateId=template.id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_preview_template(api):
    assert is_valid_preview_template(
        preview_template(api)
    )


def is_valid_deploy_template(obj):
    json_schema_validate('jsd_6099da82477b858a_v1_2_10').validate(obj)
    return True


def deploy_template(api):
    projects = api.template_programmer.get_projects()
    filtered_project = list(filter(lambda x: x.name == 'test_project_updated', projects))
    template = api.template_programmer.get_template_details(template_id=filtered_project[0].templates[0].id)
    target = api.devices.get_device_list(family=template.deviceTypes[0].productFamily,
                                         software_type=template.softwareType).response
    # versions = api.template_programmer.get_template_versions(template.id)[0].versionsInfo
    # versions = sorted(versions, key=lambda version: str(version.get('version', -1)), reverse=True)
    endpoint_result = api.template_programmer.deploy_template(
        forcePushTemplate=True,
        isComposite=template.composite,
        mainTemplateId=template.parentTemplateId,
        memberTemplateDeploymentInfo=None,
        targetInfo=[{'id': t.managementIpAddress,
                    'type': 'MANAGED_DEVICE_IP', 'params': {}} for t in target],
        templateId=template.id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_deploy_template(api):
    assert is_valid_deploy_template(
        deploy_template(api)
    )


def is_valid_get_template_deployment_status(obj):
    json_schema_validate('jsd_9c9a785741cbb41f_v1_2_10').validate(obj)
    return True


def get_template_deployment_status(api):
    time.sleep(10)
    deploymentID = deploy_template(api).deploymentId.split(" ")[-1]
    endpoint_result = api.template_programmer.get_template_deployment_status(
        deployment_id=deploymentID,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_get_template_deployment_status(api):
    assert is_valid_get_template_deployment_status(
        get_template_deployment_status(api)
    )


def is_valid_delete_template(obj):
    json_schema_validate('jsd_a7b42836408a8e74_v1_2_10').validate(obj)
    return True


def delete_template(api):
    projects = api.template_programmer.get_projects()
    filtered_project = list(filter(lambda x: x.name == 'test_project_updated', projects))
    template = api.template_programmer.get_template_details(template_id=filtered_project[0].templates[0].id)
    endpoint_result = api.template_programmer.delete_template(
        template_id=template.id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_delete_template(api):
    assert is_valid_delete_template(
        delete_template(api)
    )


def is_valid_delete_project(obj):
    json_schema_validate('jsd_d0a1abfa435b841d_v1_2_10').validate(obj)
    return True


def delete_project(api):
    projects = api.template_programmer.get_projects()
    filtered_project = list(filter(lambda x: x.name == 'test_project_updated', projects))
    endpoint_result = api.template_programmer.delete_project(
        project_id=filtered_project[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_delete_project(api):
    assert is_valid_delete_project(
        delete_project(api)
    )

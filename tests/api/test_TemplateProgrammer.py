# template_programmer

import pytest
import dnacentersdk


def is_valid_gets_the_templates_available(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_gets_the_templates_available(api):
    endpoint_result = api.template_programmer.gets_the_templates_available( param_filter_conflicting_templates = None, param_product_family = None, param_product_series = None, param_product_type = None, param_project_id = None, param_software_type = None, param_software_version = None)
    assert is_valid_gets_the_templates_available(endpoint_result)


def is_valid_create_project(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_project(api):
    endpoint_result = api.template_programmer.create_project( rq_createTime = None, rq_description = None, rq_id = None, rq_lastUpdateTime = None, rq_name = None, rq_tags = None, rq_templates = None)
    assert is_valid_create_project(endpoint_result)


def is_valid_update_template(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_template(api):
    endpoint_result = api.template_programmer.update_template( rq_author = None, rq_composite = None, rq_containingTemplates = None, rq_createTime = None, rq_description = None, rq_deviceTypes = None, rq_failurePolicy = None, rq_id = None, rq_lastUpdateTime = None, rq_name = None, rq_parentTemplateId = None, rq_projectId = None, rq_projectName = None, rq_rollbackTemplateContent = None, rq_rollbackTemplateParams = None, rq_softwareType = None, rq_softwareVariant = None, rq_softwareVersion = None, rq_tags = None, rq_templateContent = None, rq_templateParams = None, rq_version = None)
    assert is_valid_update_template(endpoint_result)


def is_valid_get_projects(obj):
    return len(obj) > 0 and all([ item for item in obj ])

def test_get_projects(api):
    endpoint_result = api.template_programmer.get_projects( param_name = None)
    assert is_valid_get_projects(endpoint_result)


def is_valid_deploy_template(obj):
    some_keys = [ 'deploymentId', 'deploymentName', 'devices', 'duration' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_deploy_template(api):
    endpoint_result = api.template_programmer.deploy_template( rq_forcePushTemplate = None, rq_isComposite = None, rq_mainTemplateId = None, rq_memberTemplateDeploymentInfo = None, rq_targetInfo = None, rq_templateId = None)
    assert is_valid_deploy_template(endpoint_result)


def is_valid_get_template_details(obj):
    some_keys = [ 'author', 'composite', 'containingTemplates', 'createTime' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_template_details(api):
    endpoint_result = api.template_programmer.get_template_details( path_param_template_id = '', param_latest_version = None)
    assert is_valid_get_template_details(endpoint_result)


def is_valid_update_project(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_project(api):
    endpoint_result = api.template_programmer.update_project( rq_createTime = None, rq_description = None, rq_id = None, rq_lastUpdateTime = None, rq_name = None, rq_tags = None, rq_templates = None)
    assert is_valid_update_project(endpoint_result)


def is_valid_get_template_deployment_status(obj):
    some_keys = [ 'deploymentId', 'deploymentName', 'devices', 'duration' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_template_deployment_status(api):
    endpoint_result = api.template_programmer.get_template_deployment_status( path_param_deployment_id = '')
    assert is_valid_get_template_deployment_status(endpoint_result)


def is_valid_delete_template(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_template(api):
    endpoint_result = api.template_programmer.delete_template( path_param_template_id = '')
    assert is_valid_delete_template(endpoint_result)


def is_valid_version_template(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_version_template(api):
    endpoint_result = api.template_programmer.version_template( rq_comments = None, rq_templateId = None)
    assert is_valid_version_template(endpoint_result)


def is_valid_preview_template(obj):
    some_keys = [ 'cliPreview', 'templateId' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_preview_template(api):
    endpoint_result = api.template_programmer.preview_template( rq_params = None, rq_templateId = None)
    assert is_valid_preview_template(endpoint_result)


def is_valid_delete_project(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_project(api):
    endpoint_result = api.template_programmer.delete_project( path_param_project_id = '')
    assert is_valid_delete_project(endpoint_result)


def is_valid_create_template(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_template(api):
    endpoint_result = api.template_programmer.create_template( path_param_project_id = '', rq_author = None, rq_composite = None, rq_containingTemplates = None, rq_createTime = None, rq_description = None, rq_deviceTypes = None, rq_failurePolicy = None, rq_id = None, rq_lastUpdateTime = None, rq_name = None, rq_parentTemplateId = None, rq_projectId = None, rq_projectName = None, rq_rollbackTemplateContent = None, rq_rollbackTemplateParams = None, rq_softwareType = None, rq_softwareVariant = None, rq_softwareVersion = None, rq_tags = None, rq_templateContent = None, rq_templateParams = None, rq_version = None)
    assert is_valid_create_template(endpoint_result)


def is_valid_get_template_versions(obj):
    return len(obj) > 0 and all([ item for item in obj ])

def test_get_template_versions(api):
    endpoint_result = api.template_programmer.get_template_versions( path_param_template_id = '')
    assert is_valid_get_template_versions(endpoint_result)


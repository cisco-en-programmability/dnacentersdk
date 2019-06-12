# -*- coding: utf-8 -*-
"""DNA Center Template Programmer API wrapper.

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


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ..generator_containers import generator_container
from ..restsession import RestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_filt,
)

class TemplateProgrammer( object ):
    """DNA Center Template Programmer API.

    Wraps the DNA Center Template Programmer API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new TemplateProgrammer object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(TemplateProgrammer, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator


    # Gets the templates available
    def gets_the_templates_available(self, param_filter_conflicting_templates = None, param_product_family = None, param_product_series = None, param_product_type = None, param_project_id = None, param_software_type = None, param_software_version = None, headers=None,payload=None,**request_parameters):
        check_type( param_project_id, basestring)
        check_type( param_software_type, basestring)
        check_type( param_software_version, basestring)
        check_type( param_product_family, basestring)
        check_type( param_product_series, basestring)
        check_type( param_product_type, basestring)
        check_type( param_filter_conflicting_templates, bool)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'projectId': param_project_id,
            'softwareType': param_software_type,
            'softwareVersion': param_software_version,
            'productFamily': param_product_family,
            'productSeries': param_product_series,
            'productType': param_product_type,
            'filterConflictingTemplates': param_filter_conflicting_templates,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_01b09a254b9ab259').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/template-programmer/template', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/template-programmer/template', path_params), params=params, json=payload)

        return self._object_factory('bpm_01b09a254b9ab259', json_data)


    # Create Project
    def create_project(self, rq_createTime = None, rq_description = None, rq_id = None, rq_lastUpdateTime = None, rq_name = None, rq_tags = None, rq_templates = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_createTime is not None: payload.update( { 'createTime':  rq_createTime })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_lastUpdateTime is not None: payload.update( { 'lastUpdateTime':  rq_lastUpdateTime })
        if rq_name is not None: payload.update( { 'name':  rq_name })
        if rq_tags is not None: payload.update( { 'tags':  rq_tags })
        if rq_templates is not None: payload.update( { 'templates':  rq_templates })
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_00aec9b1422ab27e').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/template-programmer/project', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/template-programmer/project', path_params), params=params, json=payload)

        return self._object_factory('bpm_00aec9b1422ab27e', json_data)


    # Update Template
    def update_template(self, rq_author = None, rq_composite = None, rq_containingTemplates = None, rq_createTime = None, rq_description = None, rq_deviceTypes = None, rq_failurePolicy = None, rq_id = None, rq_lastUpdateTime = None, rq_name = None, rq_parentTemplateId = None, rq_projectId = None, rq_projectName = None, rq_rollbackTemplateContent = None, rq_rollbackTemplateParams = None, rq_softwareType = None, rq_softwareVariant = None, rq_softwareVersion = None, rq_tags = None, rq_templateContent = None, rq_templateParams = None, rq_version = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_author is not None: payload.update( { 'author':  rq_author })
        if rq_composite is not None: payload.update( { 'composite':  rq_composite })
        if rq_containingTemplates is not None: payload.update( { 'containingTemplates':  rq_containingTemplates })
        if rq_createTime is not None: payload.update( { 'createTime':  rq_createTime })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_deviceTypes is not None: payload.update( { 'deviceTypes':  rq_deviceTypes })
        if rq_failurePolicy is not None: payload.update( { 'failurePolicy':  rq_failurePolicy })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_lastUpdateTime is not None: payload.update( { 'lastUpdateTime':  rq_lastUpdateTime })
        if rq_name is not None: payload.update( { 'name':  rq_name })
        if rq_parentTemplateId is not None: payload.update( { 'parentTemplateId':  rq_parentTemplateId })
        if rq_projectId is not None: payload.update( { 'projectId':  rq_projectId })
        if rq_projectName is not None: payload.update( { 'projectName':  rq_projectName })
        if rq_rollbackTemplateContent is not None: payload.update( { 'rollbackTemplateContent':  rq_rollbackTemplateContent })
        if rq_rollbackTemplateParams is not None: payload.update( { 'rollbackTemplateParams':  rq_rollbackTemplateParams })
        if rq_softwareType is not None: payload.update( { 'softwareType':  rq_softwareType })
        if rq_softwareVariant is not None: payload.update( { 'softwareVariant':  rq_softwareVariant })
        if rq_softwareVersion is not None: payload.update( { 'softwareVersion':  rq_softwareVersion })
        if rq_tags is not None: payload.update( { 'tags':  rq_tags })
        if rq_templateContent is not None: payload.update( { 'templateContent':  rq_templateContent })
        if rq_templateParams is not None: payload.update( { 'templateParams':  rq_templateParams })
        if rq_version is not None: payload.update( { 'version':  rq_version })
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_7781fa0548a98342').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/template-programmer/template', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/template-programmer/template', path_params), params=params, json=payload)

        return self._object_factory('bpm_7781fa0548a98342', json_data)


    # Get Projects
    def get_projects(self, param_name = None, headers=None,payload=None,**request_parameters):
        check_type( param_name, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'name': param_name,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_109d1b4f4289aecd').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/template-programmer/project', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/template-programmer/project', path_params), params=params, json=payload)

        return self._object_factory('bpm_109d1b4f4289aecd', json_data)


    # Deploy Template
    def deploy_template(self, rq_forcePushTemplate = None, rq_isComposite = None, rq_mainTemplateId = None, rq_memberTemplateDeploymentInfo = None, rq_targetInfo = None, rq_templateId = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_forcePushTemplate is not None: payload.update( { 'forcePushTemplate':  rq_forcePushTemplate })
        if rq_isComposite is not None: payload.update( { 'isComposite':  rq_isComposite })
        if rq_mainTemplateId is not None: payload.update( { 'mainTemplateId':  rq_mainTemplateId })
        if rq_memberTemplateDeploymentInfo is not None: payload.update( { 'memberTemplateDeploymentInfo':  rq_memberTemplateDeploymentInfo })
        if rq_targetInfo is not None: payload.update( { 'targetInfo':  rq_targetInfo })
        if rq_templateId is not None: payload.update( { 'templateId':  rq_templateId })
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_6099da82477b858a').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/template-programmer/template/deploy', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/template-programmer/template/deploy', path_params), params=params, json=payload)

        return self._object_factory('bpm_6099da82477b858a', json_data)


    # Get Template Details
    def get_template_details(self, path_param_template_id, param_latest_version = None, headers=None,payload=None,**request_parameters):
        check_type( param_latest_version, bool)
        check_type( path_param_template_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'latestVersion': param_latest_version,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'templateId': path_param_template_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_83a3b9404cb88787').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/template-programmer/template/${templateId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/template-programmer/template/${templateId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_83a3b9404cb88787', json_data)


    # Update Project
    def update_project(self, rq_createTime = None, rq_description = None, rq_id = None, rq_lastUpdateTime = None, rq_name = None, rq_tags = None, rq_templates = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_createTime is not None: payload.update( { 'createTime':  rq_createTime })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_lastUpdateTime is not None: payload.update( { 'lastUpdateTime':  rq_lastUpdateTime })
        if rq_name is not None: payload.update( { 'name':  rq_name })
        if rq_tags is not None: payload.update( { 'tags':  rq_tags })
        if rq_templates is not None: payload.update( { 'templates':  rq_templates })
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_9480fa1f47ca9254').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/template-programmer/project', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/template-programmer/project', path_params), params=params, json=payload)

        return self._object_factory('bpm_9480fa1f47ca9254', json_data)


    # Get Template deployment status
    def get_template_deployment_status(self, path_param_deployment_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_deployment_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'deploymentId': path_param_deployment_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_9c9a785741cbb41f').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/template-programmer/template/deploy/status/${deploymentId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/template-programmer/template/deploy/status/${deploymentId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_9c9a785741cbb41f', json_data)


    # Delete Template
    def delete_template(self, path_param_template_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_template_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'templateId': path_param_template_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_a7b42836408a8e74').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/template-programmer/template/${templateId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/template-programmer/template/${templateId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_a7b42836408a8e74', json_data)


    # Version Template
    def version_template(self, rq_comments = None, rq_templateId = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_comments is not None: payload.update( { 'comments':  rq_comments })
        if rq_templateId is not None: payload.update( { 'templateId':  rq_templateId })
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_62b05b2c40a9b216').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/template-programmer/template/version', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/template-programmer/template/version', path_params), params=params, json=payload)

        return self._object_factory('bpm_62b05b2c40a9b216', json_data)


    # Preview Template
    def preview_template(self, rq_params = None, rq_templateId = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_params is not None: payload.update( { 'params':  rq_params })
        if rq_templateId is not None: payload.update( { 'templateId':  rq_templateId })
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_f393abe84989bb48').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/template-programmer/template/preview', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/template-programmer/template/preview', path_params), params=params, json=payload)

        return self._object_factory('bpm_f393abe84989bb48', json_data)


    # Delete Project
    def delete_project(self, path_param_project_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_project_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'projectId': path_param_project_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_d0a1abfa435b841d').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/template-programmer/project/${projectId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/template-programmer/project/${projectId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_d0a1abfa435b841d', json_data)


    # Create Template
    def create_template(self, path_param_project_id, rq_author = None, rq_composite = None, rq_containingTemplates = None, rq_createTime = None, rq_description = None, rq_deviceTypes = None, rq_failurePolicy = None, rq_id = None, rq_lastUpdateTime = None, rq_name = None, rq_parentTemplateId = None, rq_projectId = None, rq_projectName = None, rq_rollbackTemplateContent = None, rq_rollbackTemplateParams = None, rq_softwareType = None, rq_softwareVariant = None, rq_softwareVersion = None, rq_tags = None, rq_templateContent = None, rq_templateParams = None, rq_version = None, headers=None,payload=None,**request_parameters):
        check_type( path_param_project_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'projectId': path_param_project_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_author is not None: payload.update( { 'author':  rq_author })
        if rq_composite is not None: payload.update( { 'composite':  rq_composite })
        if rq_containingTemplates is not None: payload.update( { 'containingTemplates':  rq_containingTemplates })
        if rq_createTime is not None: payload.update( { 'createTime':  rq_createTime })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_deviceTypes is not None: payload.update( { 'deviceTypes':  rq_deviceTypes })
        if rq_failurePolicy is not None: payload.update( { 'failurePolicy':  rq_failurePolicy })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_lastUpdateTime is not None: payload.update( { 'lastUpdateTime':  rq_lastUpdateTime })
        if rq_name is not None: payload.update( { 'name':  rq_name })
        if rq_parentTemplateId is not None: payload.update( { 'parentTemplateId':  rq_parentTemplateId })
        if rq_projectId is not None: payload.update( { 'projectId':  rq_projectId })
        if rq_projectName is not None: payload.update( { 'projectName':  rq_projectName })
        if rq_rollbackTemplateContent is not None: payload.update( { 'rollbackTemplateContent':  rq_rollbackTemplateContent })
        if rq_rollbackTemplateParams is not None: payload.update( { 'rollbackTemplateParams':  rq_rollbackTemplateParams })
        if rq_softwareType is not None: payload.update( { 'softwareType':  rq_softwareType })
        if rq_softwareVariant is not None: payload.update( { 'softwareVariant':  rq_softwareVariant })
        if rq_softwareVersion is not None: payload.update( { 'softwareVersion':  rq_softwareVersion })
        if rq_tags is not None: payload.update( { 'tags':  rq_tags })
        if rq_templateContent is not None: payload.update( { 'templateContent':  rq_templateContent })
        if rq_templateParams is not None: payload.update( { 'templateParams':  rq_templateParams })
        if rq_version is not None: payload.update( { 'version':  rq_version })
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_f6b119ad4d4aaf16').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/template-programmer/project/${projectId}/template', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/template-programmer/project/${projectId}/template', path_params), params=params, json=payload)

        return self._object_factory('bpm_f6b119ad4d4aaf16', json_data)


    # Get Template Versions
    def get_template_versions(self, path_param_template_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_template_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'templateId': path_param_template_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_c8bf6b65414a9bc7').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/template-programmer/template/version/${templateId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/template-programmer/template/version/${templateId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_c8bf6b65414a9bc7', json_data)



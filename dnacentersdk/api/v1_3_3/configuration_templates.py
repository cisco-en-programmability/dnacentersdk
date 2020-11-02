# -*- coding: utf-8 -*-
"""DNA Center Configuration Templates API wrapper.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_of_str,
)


class ConfigurationTemplates(object):
    """DNA Center Configuration Templates API (version: 1.3.3).

    Wraps the DNA Center Configuration Templates
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new ConfigurationTemplates
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(ConfigurationTemplates, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def create_project(self,
                       createTime=None,
                       description=None,
                       id=None,
                       lastUpdateTime=None,
                       name=None,
                       tags=None,
                       templates=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """Creates a new project.

        Args:
            createTime(number): ProjectDTO's createTime.
            description(string): ProjectDTO's description.
            id(string): ProjectDTO's id.
            lastUpdateTime(number): ProjectDTO's lastUpdateTime.
            name(string): ProjectDTO's name.
            tags(list): ProjectDTO's tags (list of string, objects).
            templates: Part of the JSON serializable Python object
                to send in the body of the Request.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
            'createTime':
                createTime,
            'description':
                description,
            'id':
                id,
            'lastUpdateTime':
                lastUpdateTime,
            'name':
                name,
            'tags':
                tags,
            'templates':
                templates,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_00aec9b1422ab27e_v1_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/project')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload)

        return self._object_factory('bpm_00aec9b1422ab27e_v1_3_3', json_data)

    def gets_the_templates_available(self,
                                     filter_conflicting_templates=None,
                                     product_family=None,
                                     product_series=None,
                                     product_type=None,
                                     project_id=None,
                                     software_type=None,
                                     software_version=None,
                                     headers=None,
                                     **request_parameters):
        """List the templates available.

        Args:
            project_id(basestring): projectId query parameter.
            software_type(basestring): softwareType query parameter.
            software_version(basestring): softwareVersion query
                parameter.
            product_family(basestring): productFamily query
                parameter.
            product_series(basestring): productSeries query
                parameter.
            product_type(basestring): productType query parameter.
            filter_conflicting_templates(bool):
                filterConflictingTemplates query
                parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(project_id, basestring)
        check_type(software_type, basestring)
        check_type(software_version, basestring)
        check_type(product_family, basestring)
        check_type(product_series, basestring)
        check_type(product_type, basestring)
        check_type(filter_conflicting_templates, bool)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'projectId':
                project_id,
            'softwareType':
                software_type,
            'softwareVersion':
                software_version,
            'productFamily':
                product_family,
            'productSeries':
                product_series,
            'productType':
                product_type,
            'filterConflictingTemplates':
                filter_conflicting_templates,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/template')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_01b09a254b9ab259_v1_3_3', json_data)

    def get_projects(self,
                     name=None,
                     headers=None,
                     **request_parameters):
        """Returns the projects in the system.

        Args:
            name(basestring): Name of project to be searched.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(name, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'name':
                name,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/project')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_109d1b4f4289aecd_v1_3_3', json_data)

    def version_template(self,
                         comments=None,
                         templateId=None,
                         headers=None,
                         payload=None,
                         active_validation=True,
                         **request_parameters):
        """Creates Versioning for the current contents of the template.

        Args:
            comments(string): TemplateVersionRequestDTO's comments.
            templateId(string): TemplateVersionRequestDTO's
                templateId.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
            'comments':
                comments,
            'templateId':
                templateId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_62b05b2c40a9b216_v1_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/template/version')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload)

        return self._object_factory('bpm_62b05b2c40a9b216_v1_3_3', json_data)

    def deploy_template(self,
                        forcePushTemplate=None,
                        isComposite=None,
                        mainTemplateId=None,
                        memberTemplateDeploymentInfo=None,
                        targetInfo=None,
                        templateId=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Deploys a template.

        Args:
            forcePushTemplate(boolean): TemplateDeploymentInfo's
                forcePushTemplate.
            isComposite(boolean): TemplateDeploymentInfo's
                isComposite.
            mainTemplateId(string): TemplateDeploymentInfo's
                mainTemplateId.
            memberTemplateDeploymentInfo(list):
                TemplateDeploymentInfo's
                memberTemplateDeploymentInfo (list of
                any objects).
            targetInfo(list): TemplateDeploymentInfo's targetInfo
                (list of objects).
            templateId(string): TemplateDeploymentInfo's templateId.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
            'forcePushTemplate':
                forcePushTemplate,
            'isComposite':
                isComposite,
            'mainTemplateId':
                mainTemplateId,
            'memberTemplateDeploymentInfo':
                memberTemplateDeploymentInfo,
            'targetInfo':
                targetInfo,
            'templateId':
                templateId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_6099da82477b858a_v1_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/template/deploy')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload)

        return self._object_factory('bpm_6099da82477b858a_v1_3_3', json_data)

    def update_template(self,
                        author=None,
                        composite=None,
                        containingTemplates=None,
                        createTime=None,
                        description=None,
                        deviceTypes=None,
                        failurePolicy=None,
                        id=None,
                        lastUpdateTime=None,
                        name=None,
                        parentTemplateId=None,
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
                        version=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Updates an existing template.

        Args:
            author(string): TemplateDTO's author.
            composite(boolean): TemplateDTO's composite.
            containingTemplates(list): TemplateDTO's
                containingTemplates (list of objects).
            createTime(number): TemplateDTO's createTime.
            description(string): TemplateDTO's description.
            deviceTypes(list): TemplateDTO's deviceTypes (list of
                objects).
            failurePolicy(string): TemplateDTO's failurePolicy.
                Available values are 'ABORT_ON_ERROR',
                'CONTINUE_ON_ERROR',
                'ROLLBACK_ON_ERROR',
                'ROLLBACK_TARGET_ON_ERROR' and
                'ABORT_TARGET_ON_ERROR'.
            id(string): TemplateDTO's id.
            lastUpdateTime(number): TemplateDTO's lastUpdateTime.
            name(string): TemplateDTO's name.
            parentTemplateId(string): TemplateDTO's
                parentTemplateId.
            projectId(string): TemplateDTO's projectId.
            projectName(string): TemplateDTO's projectName.
            rollbackTemplateContent(string): TemplateDTO's
                rollbackTemplateContent.
            rollbackTemplateParams(list): TemplateDTO's
                rollbackTemplateParams (list of
                objects).
            softwareType(string): TemplateDTO's softwareType.
            softwareVariant(string): TemplateDTO's softwareVariant.
            softwareVersion(string): TemplateDTO's softwareVersion.
            tags(list): TemplateDTO's tags (list of string,
                objects).
            templateContent(string): TemplateDTO's templateContent.
            templateParams(list): TemplateDTO's templateParams (list
                of objects).
            version(string): TemplateDTO's version.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
            'author':
                author,
            'composite':
                composite,
            'containingTemplates':
                containingTemplates,
            'createTime':
                createTime,
            'description':
                description,
            'deviceTypes':
                deviceTypes,
            'failurePolicy':
                failurePolicy,
            'id':
                id,
            'lastUpdateTime':
                lastUpdateTime,
            'name':
                name,
            'parentTemplateId':
                parentTemplateId,
            'projectId':
                projectId,
            'projectName':
                projectName,
            'rollbackTemplateContent':
                rollbackTemplateContent,
            'rollbackTemplateParams':
                rollbackTemplateParams,
            'softwareType':
                softwareType,
            'softwareVariant':
                softwareVariant,
            'softwareVersion':
                softwareVersion,
            'tags':
                tags,
            'templateContent':
                templateContent,
            'templateParams':
                templateParams,
            'version':
                version,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_7781fa0548a98342_v1_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/template')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_7781fa0548a98342_v1_3_3', json_data)

    def get_template_details(self,
                             template_id,
                             latest_version=None,
                             headers=None,
                             **request_parameters):
        """Returns details of the specified template.

        Args:
            template_id(basestring): templateId path parameter.
            latest_version(bool): latestVersion query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(latest_version, bool)
        check_type(template_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'latestVersion':
                latest_version,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'templateId': template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-'
                 + 'programmer/template/${templateId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_83a3b9404cb88787_v1_3_3', json_data)

    def update_project(self,
                       createTime=None,
                       description=None,
                       id=None,
                       lastUpdateTime=None,
                       name=None,
                       tags=None,
                       templates=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """Updates an existing project.

        Args:
            createTime(number): ProjectDTO's createTime.
            description(string): ProjectDTO's description.
            id(string): ProjectDTO's id.
            lastUpdateTime(number): ProjectDTO's lastUpdateTime.
            name(string): ProjectDTO's name.
            tags(list): ProjectDTO's tags (list of string, objects).
            templates: Part of the JSON serializable Python object
                to send in the body of the Request.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
            'createTime':
                createTime,
            'description':
                description,
            'id':
                id,
            'lastUpdateTime':
                lastUpdateTime,
            'name':
                name,
            'tags':
                tags,
            'templates':
                templates,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_9480fa1f47ca9254_v1_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/project')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_9480fa1f47ca9254_v1_3_3', json_data)

    def get_template_deployment_status(self,
                                       deployment_id,
                                       headers=None,
                                       **request_parameters):
        """Returns the status of a deployed template.

        Args:
            deployment_id(basestring): deploymentId path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(deployment_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'deploymentId': deployment_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-'
                 + 'programmer/template/deploy/status/${deploymentId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_9c9a785741cbb41f_v1_3_3', json_data)

    def delete_template(self,
                        template_id,
                        headers=None,
                        **request_parameters):
        """Deletes an existing template.

        Args:
            template_id(basestring): templateId path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(template_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'templateId': template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-'
                 + 'programmer/template/${templateId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=params)

        return self._object_factory('bpm_a7b42836408a8e74_v1_3_3', json_data)

    def get_template_versions(self,
                              template_id,
                              headers=None,
                              **request_parameters):
        """Returns the versions of a specified template.

        Args:
            template_id(basestring): templateId path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(template_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'templateId': template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-'
                 + 'programmer/template/version/${templateId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_c8bf6b65414a9bc7_v1_3_3', json_data)

    def delete_project(self,
                       project_id,
                       headers=None,
                       **request_parameters):
        """Deletes an existing Project.

        Args:
            project_id(basestring): projectId path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(project_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'projectId': project_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-'
                 + 'programmer/project/${projectId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=params)

        return self._object_factory('bpm_d0a1abfa435b841d_v1_3_3', json_data)

    def preview_template(self,
                         params=None,
                         templateId=None,
                         headers=None,
                         payload=None,
                         active_validation=True,
                         **request_parameters):
        """Previews an existing template.

        Args:
            params(object): TemplatePreviewRequestDTO's params.
            templateId(string): TemplatePreviewRequestDTO's
                templateId.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
            'params':
                params,
            'templateId':
                templateId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f393abe84989bb48_v1_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/template/preview')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_f393abe84989bb48_v1_3_3', json_data)

    def create_template(self,
                        project_id,
                        author=None,
                        composite=None,
                        containingTemplates=None,
                        createTime=None,
                        description=None,
                        deviceTypes=None,
                        failurePolicy=None,
                        id=None,
                        lastUpdateTime=None,
                        name=None,
                        parentTemplateId=None,
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
                        version=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Creates a new template.

        Args:
            author(string): TemplateDTO's author.
            composite(boolean): TemplateDTO's composite.
            containingTemplates(list): TemplateDTO's
                containingTemplates (list of objects).
            createTime(number): TemplateDTO's createTime.
            description(string): TemplateDTO's description.
            deviceTypes(list): TemplateDTO's deviceTypes (list of
                objects).
            failurePolicy(string): TemplateDTO's failurePolicy.
                Available values are 'ABORT_ON_ERROR',
                'CONTINUE_ON_ERROR',
                'ROLLBACK_ON_ERROR',
                'ROLLBACK_TARGET_ON_ERROR' and
                'ABORT_TARGET_ON_ERROR'.
            id(string): TemplateDTO's id.
            lastUpdateTime(number): TemplateDTO's lastUpdateTime.
            name(string): TemplateDTO's name.
            parentTemplateId(string): TemplateDTO's
                parentTemplateId.
            projectId(string): TemplateDTO's projectId.
            projectName(string): TemplateDTO's projectName.
            rollbackTemplateContent(string): TemplateDTO's
                rollbackTemplateContent.
            rollbackTemplateParams(list): TemplateDTO's
                rollbackTemplateParams (list of
                objects).
            softwareType(string): TemplateDTO's softwareType.
            softwareVariant(string): TemplateDTO's softwareVariant.
            softwareVersion(string): TemplateDTO's softwareVersion.
            tags(list): TemplateDTO's tags (list of string,
                objects).
            templateContent(string): TemplateDTO's templateContent.
            templateParams(list): TemplateDTO's templateParams (list
                of objects).
            version(string): TemplateDTO's version.
            project_id(basestring): projectId path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(project_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'projectId': project_id,
        }

        _payload = {
            'author':
                author,
            'composite':
                composite,
            'containingTemplates':
                containingTemplates,
            'createTime':
                createTime,
            'description':
                description,
            'deviceTypes':
                deviceTypes,
            'failurePolicy':
                failurePolicy,
            'id':
                id,
            'lastUpdateTime':
                lastUpdateTime,
            'name':
                name,
            'parentTemplateId':
                parentTemplateId,
            'projectId':
                projectId,
            'projectName':
                projectName,
            'rollbackTemplateContent':
                rollbackTemplateContent,
            'rollbackTemplateParams':
                rollbackTemplateParams,
            'softwareType':
                softwareType,
            'softwareVariant':
                softwareVariant,
            'softwareVersion':
                softwareVersion,
            'tags':
                tags,
            'templateContent':
                templateContent,
            'templateParams':
                templateParams,
            'version':
                version,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f6b119ad4d4aaf16_v1_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-'
                 + 'programmer/project/${projectId}/template')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload)

        return self._object_factory('bpm_f6b119ad4d4aaf16_v1_3_3', json_data)

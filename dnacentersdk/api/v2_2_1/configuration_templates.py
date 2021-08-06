# -*- coding: utf-8 -*-
"""Cisco DNA Center Configuration Templates API wrapper.

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
    """Cisco DNA Center Configuration Templates API (version: 2.2.1).

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

    def get_projects(self,
                     name=None,
                     headers=None,
                     **request_parameters):
        """Returns the projects in the system.

        Args:
            name(basestring): name query parameter. Name of project to be searched.
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

        _params = {
            'name':
                name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

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
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b942797fc158e3a0fbb5ffb1347962_v2_2_1', json_data)

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
            createTime(integer): Configuration Templates's createTime.
            description(string): Configuration Templates's description.
            id(string): Configuration Templates's id.
            lastUpdateTime(integer): Configuration Templates's lastUpdateTime.
            name(string): Configuration Templates's name.
            tags(list): Configuration Templates's tags (list of strings).
            templates(object): Configuration Templates's templates.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

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
            self._request_validator('jsd_cc19241fd92f586c8986d4d5c99c3a88_v2_2_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/project')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_cc19241fd92f586c8986d4d5c99c3a88_v2_2_1', json_data)

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
            createTime(integer): Configuration Templates's createTime.
            description(string): Configuration Templates's description.
            id(string): Configuration Templates's id.
            lastUpdateTime(integer): Configuration Templates's lastUpdateTime.
            name(string): Configuration Templates's name.
            tags(list): Configuration Templates's tags (list of strings).
            templates(object): Configuration Templates's templates.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

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
            self._request_validator('jsd_ecc3258a5c5b8f2267a512820a59_v2_2_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/project')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_ecc3258a5c5b8f2267a512820a59_v2_2_1', json_data)

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
            software_version(basestring): softwareVersion query parameter.
            product_family(basestring): productFamily query parameter.
            product_series(basestring): productSeries query parameter.
            product_type(basestring): productType query parameter.
            filter_conflicting_templates(bool): filterConflictingTemplates query parameter.
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

        _params = {
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
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

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
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bdc3bc8a35908aba5858e78805d22_v2_2_1', json_data)

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
            author(string): Configuration Templates's author.
            composite(boolean): Configuration Templates's composite.
            containingTemplates(list): Configuration Templates's containingTemplates (list of objects).
            createTime(integer): Configuration Templates's createTime.
            description(string): Configuration Templates's description.
            deviceTypes(list): Configuration Templates's deviceTypes (list of objects).
            failurePolicy(string): Configuration Templates's failurePolicy. Available values are 'ABORT_ON_ERROR',
                'CONTINUE_ON_ERROR', 'ROLLBACK_ON_ERROR', 'ROLLBACK_TARGET_ON_ERROR' and
                'ABORT_TARGET_ON_ERROR'.
            id(string): Configuration Templates's id.
            lastUpdateTime(integer): Configuration Templates's lastUpdateTime.
            name(string): Configuration Templates's name.
            parentTemplateId(string): Configuration Templates's parentTemplateId.
            projectId(string): Configuration Templates's projectId.
            projectName(string): Configuration Templates's projectName.
            rollbackTemplateContent(string): Configuration Templates's rollbackTemplateContent.
            rollbackTemplateParams(list): Configuration Templates's rollbackTemplateParams (list of objects).
            softwareType(string): Configuration Templates's softwareType.
            softwareVariant(string): Configuration Templates's softwareVariant.
            softwareVersion(string): Configuration Templates's softwareVersion.
            tags(list): Configuration Templates's tags (list of strings).
            templateContent(string): Configuration Templates's templateContent.
            templateParams(list): Configuration Templates's templateParams (list of objects).
            version(string): Configuration Templates's version.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

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
            self._request_validator('jsd_dbea7d7de125cf6b840d5032d3a5c59_v2_2_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/template')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_dbea7d7de125cf6b840d5032d3a5c59_v2_2_1', json_data)

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
            forcePushTemplate(boolean): Configuration Templates's forcePushTemplate.
            isComposite(boolean): Configuration Templates's isComposite.
            mainTemplateId(string): Configuration Templates's mainTemplateId.
            memberTemplateDeploymentInfo(list): Configuration Templates's memberTemplateDeploymentInfo (list of
                strings).
            targetInfo(list): Configuration Templates's targetInfo (list of objects).
            templateId(string): Configuration Templates's templateId.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

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
            self._request_validator('jsd_efa92557c9a6c8af0a71829c7e_v2_2_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/template/deploy')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_efa92557c9a6c8af0a71829c7e_v2_2_1', json_data)

    def version_template(self,
                         comments=None,
                         templateId=None,
                         headers=None,
                         payload=None,
                         active_validation=True,
                         **request_parameters):
        """Creates Versioning for the current contents of the template.

        Args:
            comments(string): Configuration Templates's comments.
            templateId(string): Configuration Templates's templateId.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

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
            self._request_validator('jsd_e1a76c121857a085149e62e56caadd_v2_2_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/template/version')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e1a76c121857a085149e62e56caadd_v2_2_1', json_data)

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

        _params = {
            'latestVersion':
                latest_version,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'templateId': template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-'
                 + 'programmer/template/{templateId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d6dbb8874d3150858c1ca6feb7e09edf_v2_2_1', json_data)

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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'templateId': template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-'
                 + 'programmer/template/{templateId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c311bd3d952757b2a7b98a5bc5aa6137_v2_2_1', json_data)

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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'deploymentId': deployment_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-'
                 + 'programmer/template/deploy/status/{deploymentId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e1f17b174e955dea2ae9d98264de307_v2_2_1', json_data)

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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'templateId': template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-'
                 + 'programmer/template/version/{templateId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d49f82923bc5dfda63adfd224e1a22f_v2_2_1', json_data)

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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'projectId': project_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-'
                 + 'programmer/project/{projectId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a3e0588fa1ac56d4947ae5cfc2e16a8f_v2_2_1', json_data)

    def preview_template(self,
                         params=None,
                         templateId=None,
                         headers=None,
                         payload=None,
                         active_validation=True,
                         **request_parameters):
        """Previews an existing template.

        Args:
            params(object): Configuration Templates's params.
            templateId(string): Configuration Templates's templateId.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

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
            self._request_validator('jsd_ccbf614b4b355cac929f12cc61272c1c_v2_2_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-programmer/template/preview')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_ccbf614b4b355cac929f12cc61272c1c_v2_2_1', json_data)

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
            author(string): Configuration Templates's author.
            composite(boolean): Configuration Templates's composite.
            containingTemplates(list): Configuration Templates's containingTemplates (list of objects).
            createTime(integer): Configuration Templates's createTime.
            description(string): Configuration Templates's description.
            deviceTypes(list): Configuration Templates's deviceTypes (list of objects).
            failurePolicy(string): Configuration Templates's failurePolicy. Available values are 'ABORT_ON_ERROR',
                'CONTINUE_ON_ERROR', 'ROLLBACK_ON_ERROR', 'ROLLBACK_TARGET_ON_ERROR' and
                'ABORT_TARGET_ON_ERROR'.
            id(string): Configuration Templates's id.
            lastUpdateTime(integer): Configuration Templates's lastUpdateTime.
            name(string): Configuration Templates's name.
            parentTemplateId(string): Configuration Templates's parentTemplateId.
            projectId(string): Configuration Templates's projectId.
            projectName(string): Configuration Templates's projectName.
            rollbackTemplateContent(string): Configuration Templates's rollbackTemplateContent.
            rollbackTemplateParams(list): Configuration Templates's rollbackTemplateParams (list of objects).
            softwareType(string): Configuration Templates's softwareType.
            softwareVariant(string): Configuration Templates's softwareVariant.
            softwareVersion(string): Configuration Templates's softwareVersion.
            tags(list): Configuration Templates's tags (list of strings).
            templateContent(string): Configuration Templates's templateContent.
            templateParams(list): Configuration Templates's templateParams (list of objects).
            version(string): Configuration Templates's version.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

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
            self._request_validator('jsd_e3e170003d865b9a8d76cbe1d2f268be_v2_2_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/template-'
                 + 'programmer/project/{projectId}/template')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e3e170003d865b9a8d76cbe1d2f268be_v2_2_1', json_data)

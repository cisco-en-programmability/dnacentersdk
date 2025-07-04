# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Configuration Templates API wrapper.

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


from builtins import *


from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class ConfigurationTemplates(object):
    """Cisco Catalyst Center Configuration Templates API (version: 3.1.3.0).

    Wraps the Catalyst Center Configuration Templates
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new ConfigurationTemplates
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(ConfigurationTemplates, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def create_template_project(
        self,
        description=None,
        name=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Create a template project. .

        Args:
            description(string): Configuration Templates's Description of the project .
            name(string): Configuration Templates's Name of the project .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-template-project
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "name": name,
            "description": description,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e37e7d81575d35a974df797e0a2268_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/projects"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_e37e7d81575d35a974df797e0a2268_v3_1_3_0", json_data
        )

    def get_template_projects(
        self, limit=None, name=None, offset=None, headers=None, **request_parameters
    ):
        """Get all matching template projects based on the filters selected. .

        Args:
            name(str): name query parameter. Name of project to be searched .
            limit(int): limit query parameter. The number of records to show for this page;The minimum is 1, and the
                maximum is 500. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-template-projects
        """
        check_type(headers, dict)
        check_type(name, str)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
            "limit": limit,
            "offset": offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/projects"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d74ea4c307a5ee9a0a97143f62a74e4_v3_1_3_0", json_data
        )

    def get_template_project_count(self, name=None, headers=None, **request_parameters):
        """Get the count of all template projects. .

        Args:
            name(str): name query parameter. Name of project to be searched .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-template-project-count
        """
        check_type(headers, dict)
        check_type(name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/projects/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ed5b154779c554408832f9ddfb65db89_v3_1_3_0", json_data
        )

    def get_template_project(self, project_id, headers=None, **request_parameters):
        """Get a template project by the project's ID. .

        Args:
            project_id(str): projectId path parameter. The id of the project to get, retrieveable from `GET
                /dna/intent/api/v1/projects` .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-template-project
        """
        check_type(headers, dict)
        check_type(project_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "projectId": project_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/projects/{projectId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bf7a624855fa9f08a3d2cafcbce7_v3_1_3_0", json_data
        )

    def update_template_project(
        self,
        project_id,
        description=None,
        name=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update a template project by the project's ID. .

        Args:
            description(string): Configuration Templates's Description of the project .
            name(string): Configuration Templates's Name of the project .
            project_id(str): projectId path parameter. The id of the project to update, retrieveable from `GET
                /dna/intent/api/v1/projects` .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-template-project
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(project_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "projectId": project_id,
        }
        _payload = {
            "name": name,
            "description": description,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_fb8fee52fcb7577206a3fcac8c_v3_1_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/projects/{projectId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_fb8fee52fcb7577206a3fcac8c_v3_1_3_0", json_data
        )

    def delete_template_project(self, project_id, headers=None, **request_parameters):
        """Delete a template project by the project's ID. .

        Args:
            project_id(str): projectId path parameter. the id of the project to delete, retrieveable from `GET
                /dna/intent/api/v1/projects` .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-template-project
        """
        check_type(headers, dict)
        check_type(project_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "projectId": project_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/projects/{projectId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f3a0f150bc9cb9759496f6029c_v3_1_3_0", json_data
        )

    def clone_given_template(
        self, name, project_id, template_id, headers=None, **request_parameters
    ):
        """API to clone template .

        Args:
            name(str): name path parameter. Template name to clone template(Name should be different than existing
                template name within same project) .
            template_id(str): templateId path parameter. UUID of the template to clone it .
            project_id(str): projectId path parameter.
            project_id(str): projectId query parameter. UUID of the project in which the template needs to be
                created .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!creates-a-clone-of-the-given-template
        """
        check_type(headers, dict)
        check_type(project_id, str)
        check_type(name, str, may_be_none=False)
        check_type(template_id, str, may_be_none=False)
        check_type(project_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "projectId": project_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "name": name,
            "templateId": template_id,
            "projectId": project_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/template-programmer/clone/name/{name}"
            + "/project/{projectId}/template/{templateId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_feb800c6888f5b13972467f0e3416ec2_v3_1_3_0", json_data
        )

    def create_project(
        self,
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
        **request_parameters
    ):
        """This API is used to create a new project. .

        Args:
            createTime(integer): Configuration Templates's Create time of project .
            description(string): Configuration Templates's Description of project .
            id(string): Configuration Templates's UUID of project .
            lastUpdateTime(integer): Configuration Templates's Update time of project .
            name(string): Configuration Templates's Name of project .
            tags(list): Configuration Templates's tags (list of objects).
            templates(list): Configuration Templates's List of templates within the project  (list of objects).
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-project
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "tags": tags,
            "createTime": createTime,
            "description": description,
            "id": id,
            "lastUpdateTime": lastUpdateTime,
            "name": name,
            "templates": templates,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ecc3258a5c5b8f2267a512820a59_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-programmer/project"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_ecc3258a5c5b8f2267a512820a59_v3_1_3_0", json_data
        )

    def update_project(
        self,
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
        **request_parameters
    ):
        """This API is used to update an existing project. .

        Args:
            createTime(integer): Configuration Templates's Create time of project .
            description(string): Configuration Templates's Description of project .
            id(string): Configuration Templates's UUID of project .
            lastUpdateTime(integer): Configuration Templates's Update time of project .
            name(string): Configuration Templates's Name of project .
            tags(list): Configuration Templates's tags (list of objects).
            templates(object): Configuration Templates's List of templates within the project .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-project
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "tags": tags,
            "createTime": createTime,
            "description": description,
            "id": id,
            "lastUpdateTime": lastUpdateTime,
            "name": name,
            "templates": templates,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cc19241fd92f586c8986d4d5c99c3a88_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-programmer/project"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_cc19241fd92f586c8986d4d5c99c3a88_v3_1_3_0", json_data
        )

    def get_projects(
        self, name=None, sort_order=None, headers=None, **request_parameters
    ):
        """List the projects .

        Args:
            name(str): name query parameter. Name of project to be searched .
            sort_order(str): sortOrder query parameter. Sort Order Ascending (asc) or Descending (des) .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!gets-a-list-of-projects
        """
        check_type(headers, dict)
        check_type(name, str)
        check_type(sort_order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
            "sortOrder": sort_order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-programmer/project"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b942797fc158e3a0fbb5ffb1347962_v3_1_3_0", json_data
        )

    def imports_the_projects_provided(
        self,
        do_version=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Imports the Projects provided in the DTO .

        Args:
            do_version(bool): doVersion query parameter. If this flag is true then it creates a new version of the
                template with the imported contents in case if the templates already exists. " If this
                flag is false and if template already exists, then operation fails with 'Template
                already exists' error .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload((list, dict)): A JSON serializable Python object to send in the
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!imports-the-projects-provided
        """
        check_type(headers, dict)
        check_type(payload, (list, dict))
        check_type(do_version, bool)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "doVersion": do_version,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or {}
        if active_validation:
            self._request_validator(
                "jsd_dec1857f1585557eb39e12a9c93ef985_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-" + "programmer/project/importprojects"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_dec1857f1585557eb39e12a9c93ef985_v3_1_3_0", json_data
        )

    def export_projects(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Exports the projects for given projectNames. .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!exports-the-projects-for-a-given-criteria
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_e6ea8c5d425cf9ac77006f5593725f_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/template-" + "programmer/project/name/exportprojects"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_e6ea8c5d425cf9ac77006f5593725f_v3_1_3_0", json_data
        )

    def imports_the_templates_provided(
        self,
        project_name,
        do_version=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Imports the templates provided in the DTO by project Name .

        Args:
            project_name(str): projectName path parameter. Project name to create template under the project .
            do_version(bool): doVersion query parameter. If this flag is true then it creates a new version of the
                template with the imported contents in case if the templates already exists. " If this
                flag is false and if template already exists, then operation fails with 'Template
                already exists' error .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!imports-the-templates-provided
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(do_version, bool)
        check_type(project_name, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "doVersion": do_version,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "projectName": project_name,
        }
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_db7b6c4f0542aab9fe7cf5c995f83_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/template-programmer/project/name/{pro"
            + "jectName}/template/importtemplates"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_db7b6c4f0542aab9fe7cf5c995f83_v3_1_3_0", json_data
        )

    def get_project_details(self, project_id, headers=None, **request_parameters):
        """Get the details of the given project by its id. .

        Args:
            project_id(str): projectId path parameter. projectId(UUID) of project to get project details .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!gets-the-details-of-a-given-project
        """
        check_type(headers, dict)
        check_type(project_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "projectId": project_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-" + "programmer/project/{projectId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c1b2c35764f2518182b3f271a29a574c_v3_1_3_0", json_data
        )

    def deletes_the_project(self, project_id, headers=None, **request_parameters):
        """Deletes the project by its id .

        Args:
            project_id(str): projectId path parameter. projectId(UUID) of project to be deleted .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!deletes-the-project
        """
        check_type(headers, dict)
        check_type(project_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "projectId": project_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-" + "programmer/project/{projectId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a3e0588fa1ac56d4947ae5cfc2e16a8f_v3_1_3_0", json_data
        )

    def create_template(
        self,
        project_id,
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
        version=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to create a template by project id. .

        Args:
            author(string): Configuration Templates's Author of template .
            composite(boolean): Configuration Templates's Is it composite template .
            containingTemplates(list): Configuration Templates's containingTemplates (list of objects).
            createTime(integer): Configuration Templates's Create time of template .
            customParamsOrder(boolean): Configuration Templates's Custom Params Order .
            description(string): Configuration Templates's Description of template .
            deviceTypes(list): Configuration Templates's deviceTypes (list of objects).
            failurePolicy(string): Configuration Templates's Define failure policy if template provisioning fails .
                Available values are 'ABORT_ON_ERROR', 'CONTINUE_ON_ERROR', 'ROLLBACK_ON_ERROR',
                'ROLLBACK_TARGET_ON_ERROR' and 'ABORT_TARGET_ON_ERROR'.
            id(string): Configuration Templates's UUID of template .
            language(string): Configuration Templates's Template language (JINJA or VELOCITY) .
            lastUpdateTime(integer): Configuration Templates's Update time of template .
            latestVersionTime(integer): Configuration Templates's Latest versioned template time .
            name(string): Configuration Templates's Name of template .
            parentTemplateId(string): Configuration Templates's Parent templateID .
            projectId(string): Configuration Templates's Project UUID .
            projectName(string): Configuration Templates's Project name .
            rollbackTemplateContent(string): Configuration Templates's Rollback template content .
            rollbackTemplateParams(list): Configuration Templates's rollbackTemplateParams (list of objects).
            softwareType(string): Configuration Templates's Applicable device software type .
            softwareVariant(string): Configuration Templates's Applicable device software variant .
            softwareVersion(string): Configuration Templates's Applicable device software version .
            tags(list): Configuration Templates's tags (list of objects).
            templateContent(string): Configuration Templates's Template content .
            templateParams(list): Configuration Templates's templateParams (list of objects).
            validationErrors(object): Configuration Templates's validationErrors.
            version(string): Configuration Templates's Current version of template .
            project_id(str): projectId path parameter. UUID of the project in which the template needs to be created
                .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(project_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "projectId": project_id,
        }
        _payload = {
            "tags": tags,
            "author": author,
            "composite": composite,
            "containingTemplates": containingTemplates,
            "createTime": createTime,
            "customParamsOrder": customParamsOrder,
            "description": description,
            "deviceTypes": deviceTypes,
            "failurePolicy": failurePolicy,
            "id": id,
            "language": language,
            "lastUpdateTime": lastUpdateTime,
            "latestVersionTime": latestVersionTime,
            "name": name,
            "parentTemplateId": parentTemplateId,
            "projectId": projectId,
            "projectName": projectName,
            "rollbackTemplateContent": rollbackTemplateContent,
            "rollbackTemplateParams": rollbackTemplateParams,
            "softwareType": softwareType,
            "softwareVariant": softwareVariant,
            "softwareVersion": softwareVersion,
            "templateContent": templateContent,
            "templateParams": templateParams,
            "validationErrors": validationErrors,
            "version": version,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e3e170003d865b9a8d76cbe1d2f268be_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/template-" + "programmer/project/{projectId}/template"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_e3e170003d865b9a8d76cbe1d2f268be_v3_1_3_0", json_data
        )

    def gets_the_templates_available(
        self,
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
        un_committed=None,
        headers=None,
        **request_parameters
    ):
        """List the templates available .

        Args:
            project_id(str): projectId query parameter. Filter template(s) based on project UUID .
            software_type(str): softwareType query parameter. Filter template(s) based software type .
            software_version(str): softwareVersion query parameter. Filter template(s) based softwareVersion .
            product_family(str): productFamily query parameter. Filter template(s) based on device family .
            product_series(str): productSeries query parameter. Filter template(s) based on device series .
            product_type(str): productType query parameter. Filter template(s) based on device type .
            filter_conflicting_templates(bool): filterConflictingTemplates query parameter. Filter template(s) based
                on confliting templates .
            tags(list, set, str, tuple): tags query parameter. Filter template(s) based on tags .
            project_names(list, set, str, tuple): projectNames query parameter. Filter template(s) based on project
                names .
            un_committed(bool): unCommitted query parameter. Filter template(s) based on template commited or not .
            sort_order(str): sortOrder query parameter. Sort Order Ascending (asc) or Descending (des) .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!gets-the-templates-available
        """
        check_type(headers, dict)
        check_type(project_id, str)
        check_type(software_type, str)
        check_type(software_version, str)
        check_type(product_family, str)
        check_type(product_series, str)
        check_type(product_type, str)
        check_type(filter_conflicting_templates, bool)
        check_type(tags, (list, set, str, tuple))
        check_type(project_names, (list, set, str, tuple))
        check_type(un_committed, bool)
        check_type(sort_order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "projectId": project_id,
            "softwareType": software_type,
            "softwareVersion": software_version,
            "productFamily": product_family,
            "productSeries": product_series,
            "productType": product_type,
            "filterConflictingTemplates": filter_conflicting_templates,
            "tags": tags,
            "projectNames": project_names,
            "unCommitted": un_committed,
            "sortOrder": sort_order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-programmer/template"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bdc3bc8a35908aba5858e78805d22_v3_1_3_0", json_data
        )

    def update_template(
        self,
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
        version=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to update a template. .

        Args:
            author(string): Configuration Templates's Author of template .
            composite(boolean): Configuration Templates's Is it composite template .
            containingTemplates(list): Configuration Templates's containingTemplates (list of objects).
            createTime(integer): Configuration Templates's Create time of template .
            customParamsOrder(boolean): Configuration Templates's Custom Params Order .
            description(string): Configuration Templates's Description of template .
            deviceTypes(list): Configuration Templates's deviceTypes (list of objects).
            failurePolicy(string): Configuration Templates's Define failure policy if template provisioning fails .
                Available values are 'ABORT_ON_ERROR', 'CONTINUE_ON_ERROR', 'ROLLBACK_ON_ERROR',
                'ROLLBACK_TARGET_ON_ERROR' and 'ABORT_TARGET_ON_ERROR'.
            id(string): Configuration Templates's UUID of template .
            language(string): Configuration Templates's Template language (JINJA or VELOCITY) .
            lastUpdateTime(integer): Configuration Templates's Update time of template .
            latestVersionTime(integer): Configuration Templates's Latest versioned template time .
            name(string): Configuration Templates's Name of template .
            parentTemplateId(string): Configuration Templates's Parent templateID .
            projectId(string): Configuration Templates's Project UUID .
            projectName(string): Configuration Templates's Project name .
            rollbackTemplateContent(string): Configuration Templates's Rollback template content .
            rollbackTemplateParams(list): Configuration Templates's rollbackTemplateParams (list of objects).
            softwareType(string): Configuration Templates's Applicable device software type .
            softwareVariant(string): Configuration Templates's Applicable device software variant .
            softwareVersion(string): Configuration Templates's Applicable device software version .
            tags(list): Configuration Templates's tags (list of objects).
            templateContent(string): Configuration Templates's Template content .
            templateParams(list): Configuration Templates's templateParams (list of objects).
            validationErrors(object): Configuration Templates's validationErrors.
            version(string): Configuration Templates's Current version of template .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "tags": tags,
            "author": author,
            "composite": composite,
            "containingTemplates": containingTemplates,
            "createTime": createTime,
            "customParamsOrder": customParamsOrder,
            "description": description,
            "deviceTypes": deviceTypes,
            "failurePolicy": failurePolicy,
            "id": id,
            "language": language,
            "lastUpdateTime": lastUpdateTime,
            "latestVersionTime": latestVersionTime,
            "name": name,
            "parentTemplateId": parentTemplateId,
            "projectId": projectId,
            "projectName": projectName,
            "rollbackTemplateContent": rollbackTemplateContent,
            "rollbackTemplateParams": rollbackTemplateParams,
            "softwareType": softwareType,
            "softwareVariant": softwareVariant,
            "softwareVersion": softwareVersion,
            "templateContent": templateContent,
            "templateParams": templateParams,
            "validationErrors": validationErrors,
            "version": version,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_dbea7d7de125cf6b840d5032d3a5c59_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-programmer/template"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_dbea7d7de125cf6b840d5032d3a5c59_v3_1_3_0", json_data
        )

    def deploy_template(
        self,
        forcePushTemplate=None,
        isComposite=None,
        mainTemplateId=None,
        memberTemplateDeploymentInfo=None,
        targetInfo=None,
        templateId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to deploy a template. .

        Args:
            forcePushTemplate(boolean): Configuration Templates's forcePushTemplate.
            isComposite(boolean): Configuration Templates's Composite template flag .
            mainTemplateId(string): Configuration Templates's Main template UUID of versioned template .
            memberTemplateDeploymentInfo(list): Configuration Templates's memberTemplateDeploymentInfo  (list of
                objects).
            targetInfo(list): Configuration Templates's targetInfo (list of objects).
            templateId(string): Configuration Templates's UUID of template to be provisioned .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!deploy-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "forcePushTemplate": forcePushTemplate,
            "isComposite": isComposite,
            "mainTemplateId": mainTemplateId,
            "memberTemplateDeploymentInfo": memberTemplateDeploymentInfo,
            "targetInfo": targetInfo,
            "templateId": templateId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_efa92557c9a6c8af0a71829c7e_v3_1_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-programmer/template/deploy"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_efa92557c9a6c8af0a71829c7e_v3_1_3_0", json_data
        )

    def get_template_deployment_status(
        self, deployment_id, headers=None, **request_parameters
    ):
        """API to retrieve the status of template deployment. .

        Args:
            deployment_id(str): deploymentId path parameter. UUID of deployment to retrieve template deployment
                status .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!status-of-template-deployment
        """
        check_type(headers, dict)
        check_type(deployment_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deploymentId": deployment_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/template-"
            + "programmer/template/deploy/status/{deploymentId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e1f17b174e955dea2ae9d98264de307_v3_1_3_0", json_data
        )

    def export_templates(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Exports the templates for given templateIds. .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!exports-the-templates-for-a-given-criteria
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_dc254215fdf25cd5b7ba797e8f8faebf_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-" + "programmer/template/exporttemplates"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_dc254215fdf25cd5b7ba797e8f8faebf_v3_1_3_0", json_data
        )

    def preview_template(
        self,
        deviceId=None,
        params=None,
        resourceParams=None,
        templateId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to preview a template. .

        Args:
            deviceId(string): Configuration Templates's UUID of device to get template preview .
            params(object): Configuration Templates's Params to render preview .
            resourceParams(object): Configuration Templates's Resource params to render preview .
            templateId(string): Configuration Templates's UUID of template to get template preview .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!preview-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "deviceId": deviceId,
            "params": params,
            "resourceParams": resourceParams,
            "templateId": templateId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ccbf614b4b355cac929f12cc61272c1c_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-programmer/template/preview"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_ccbf614b4b355cac929f12cc61272c1c_v3_1_3_0", json_data
        )

    def version_template(
        self,
        comments=None,
        templateId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to version the current contents of the template. .

        Args:
            comments(string): Configuration Templates's Template version comments .
            templateId(string): Configuration Templates's UUID of template .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!version-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "comments": comments,
            "templateId": templateId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e1a76c121857a085149e62e56caadd_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-programmer/template/version"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_e1a76c121857a085149e62e56caadd_v3_1_3_0", json_data
        )

    def get_template_versions(self, template_id, headers=None, **request_parameters):
        """Get all the versions of template by its id .

        Args:
            template_id(str): templateId path parameter. templateId(UUID) to get list of versioned templates .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!gets-all-the-versions-of-a-given-template
        """
        check_type(headers, dict)
        check_type(template_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/template-" + "programmer/template/version/{templateId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d49f82923bc5dfda63adfd224e1a22f_v3_1_3_0", json_data
        )

    def deletes_the_template(self, template_id, headers=None, **request_parameters):
        """Deletes the template by its id .

        Args:
            template_id(str): templateId path parameter. templateId(UUID) of template to be deleted .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!deletes-the-template
        """
        check_type(headers, dict)
        check_type(template_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-" + "programmer/template/{templateId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c311bd3d952757b2a7b98a5bc5aa6137_v3_1_3_0", json_data
        )

    def get_template_details(
        self, template_id, latest_version=None, headers=None, **request_parameters
    ):
        """Details of the template by its id .

        Args:
            template_id(str): templateId path parameter. TemplateId(UUID) to get details of the template .
            latest_version(bool): latestVersion query parameter. latestVersion flag to get the latest versioned
                template .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!gets-details-of-a-given-template
        """
        check_type(headers, dict)
        check_type(latest_version, bool)
        check_type(template_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "latestVersion": latest_version,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/template-" + "programmer/template/{templateId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d6dbb8874d3150858c1ca6feb7e09edf_v3_1_3_0", json_data
        )

    def retrieve_the_network_profiles_attached_to_acl_i_template(
        self, template_id, headers=None, **request_parameters
    ):
        """Retrieves the list of network profiles that a CLI template is currently attached to by the template ID. .

        Args:
            template_id(str): templateId path parameter. The `id` of the template, retrievable from `GET
                /intent/api/v1/templates` .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-network-profiles-attached-to-a-c-l-i-template
        """
        check_type(headers, dict)
        check_type(template_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/templates/{templateId}/networkProfile" + "sForSites"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b082bd5ba905dde83e3ec96da5ab2e6_v3_1_3_0", json_data
        )

    def attach_network_profile_to_a_day_n_cli_template(
        self,
        template_id,
        profileId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Attaches a network profile to a Day-N CLI template by passing the profile ID and template ID. .

        Args:
            profileId(string): Configuration Templates's The id of the network profile, retrievable from
                `/intent/api/v1/networkProfilesForSites` .
            template_id(str): templateId path parameter. The `id` of the template, retrievable from `GET
                /intent/api/v1/templates` .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!attach-network-profile-to-a-day-n-c-l-i-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(template_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
        }
        _payload = {
            "profileId": profileId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a31cc19195d43ba695f4b7494b559_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/templates/{templateId}/networkProfile" + "sForSites"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_a31cc19195d43ba695f4b7494b559_v3_1_3_0", json_data
        )

    def detach_a_list_of_network_profiles_from_a_day_n_cli_template(
        self, profile_id, template_id, headers=None, **request_parameters
    ):
        """Detach a list of network profiles from a Day-N CLI template with a list of profile IDs along with the template
        ID. .

        Args:
            template_id(str): templateId path parameter. The `id` of the template, retrievable from `GET
                /intent/api/v1/templates` .
            profile_id(str): profileId query parameter. The id or ids of the network profile, retrievable from
                /dna/intent/api/v1/networkProfilesForSites. The maximum number of profile Ids allowed is
                20.  A list of profile ids can be passed as a queryParameter in two ways:   a comma-
                separated string ( profileId=388a23e9-4739-4be7-a0aa-
                cc5a95d158dd,2726dc60-3a12-451e-947a-d972ebf58743), or...  as separate query parameters
                with the same name ( profileId=388a23e9-4739-4be7-a0aa-
                cc5a95d158dd&profileId=2726dc60-3a12-451e-947a-d972ebf58743 .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!detach-a-list-of-network-profiles-from-a-day-n-c-l-i-template
        """
        check_type(headers, dict)
        check_type(profile_id, str, may_be_none=False)
        check_type(template_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "profileId": profile_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/templates/{templateId}/networkProfile"
            + "sForSites/bulk"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ec48554347c9598da26f9865e844ca59_v3_1_3_0", json_data
        )

    def attach_a_list_of_network_profiles_to_a_day_n_cli_template(
        self,
        template_id,
        items=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Attaches a list of network profiles to the Day-N CLI template by passing the profile IDs and template ID. .

        Args:
            items(list): Configuration Templates's items (list of arrays).
            template_id(str): templateId path parameter. The `id` of the template, retrievable from `GET
                /intent/api/v1/templates` .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!attach-a-list-of-network-profiles-to-a-day-n-c-l-i-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(template_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
        }
        _payload = {
            "items": items,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d0f4d6b5909b5ecaa29e854e919b4221_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/templates/{templateId}/networkProfile"
            + "sForSites/bulk"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_d0f4d6b5909b5ecaa29e854e919b4221_v3_1_3_0", json_data
        )

    def retrieve_count_of_network_profiles_attached_to_acl_i_template(
        self, template_id, headers=None, **request_parameters
    ):
        """Retrieves the count of network profiles that a CLI template has been attached to by the template ID. .

        Args:
            template_id(str): templateId path parameter. The `id` of the template, retrievable from `GET
                /intent/api/v1/templates` .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieve-count-of-network-profiles-attached-to-a-c-l-i-template
        """
        check_type(headers, dict)
        check_type(template_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/templates/{templateId}/networkProfile"
            + "sForSites/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c758ee742a598ba1093c626658efaf_v3_1_3_0", json_data
        )

    def detach_a_network_profile_from_a_day_n_cli_template(
        self, profile_id, template_id, headers=None, **request_parameters
    ):
        """Detach a network profile from a Day-N CLI template by the profile ID and template ID. .

        Args:
            template_id(str): templateId path parameter. The `id` of the template, retrievable from `GET
                /intent/api/v1/templates` .
            profile_id(str): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!detach-a-network-profile-from-a-day-n-c-l-i-template
        """
        check_type(headers, dict)
        check_type(template_id, str, may_be_none=False)
        check_type(profile_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
            "profileId": profile_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/templates/{templateId}/networkProfile"
            + "sForSites/{profileId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e57a51a4a73a5f6d966981c25e2bc2b2_v3_1_3_0", json_data
        )

    def get_template_versions(
        self,
        template_id,
        latest_version=None,
        limit=None,
        offset=None,
        order=None,
        version_number=None,
        headers=None,
        **request_parameters
    ):
        """Get a template's version information. .

        Args:
            template_id(str): templateId path parameter. The id of the template to get versions of, retrieveable
                from `GET /dna/intent/api/v1/templates` .
            version_number(int): versionNumber query parameter. Filter response to only get the template version
                that matches this version number .
            latest_version(bool): latestVersion query parameter. Filter response to only include the latest version
                of a template .
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. .
            limit(int): limit query parameter. The number of records to show for this page;The minimum is 1, and the
                maximum is 500. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-template-versions
        """
        check_type(headers, dict)
        check_type(version_number, int)
        check_type(latest_version, bool)
        check_type(order, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(template_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "versionNumber": version_number,
            "latestVersion": latest_version,
            "order": order,
            "limit": limit,
            "offset": offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/templates/{templateId}/versions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b2b1616094b5091812b0e412b8982e7_v3_1_3_0", json_data
        )

    def commit_template_for_a_new_version(
        self,
        template_id,
        commitNote=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Transitions the current draft of a template to a new committed version with a higher version number. .

        Args:
            commitNote(string): Configuration Templates's A message to leave as a note with the commit of a
                template. The maximum length allowed is 255 characters. .
            template_id(str): templateId path parameter. The id of the template to commit a new version for,
                retrieveable from `GET /dna/intent/api/v1/templates` .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!commit-template-for-a-new-version
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(template_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
        }
        _payload = {
            "commitNote": commitNote,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bb1653037ca558a8c6097e20b99b4b1_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/templates/{templateId}/versions/commi" + "t"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_bb1653037ca558a8c6097e20b99b4b1_v3_1_3_0", json_data
        )

    def get_template_versions_count(
        self,
        template_id,
        latest_version=None,
        version_number=None,
        headers=None,
        **request_parameters
    ):
        """Get the count of a template's version information. .

        Args:
            template_id(str): templateId path parameter. The id of the template to get versions of, retrieveable
                from `GET /dna/intent/api/v1/templates` .
            version_number(int): versionNumber query parameter. Filter response to only get the template version
                that matches this version number .
            latest_version(bool): latestVersion query parameter. Filter response to only include the latest version
                of a template .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-template-versions-count
        """
        check_type(headers, dict)
        check_type(version_number, int)
        check_type(latest_version, bool)
        check_type(template_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "versionNumber": version_number,
            "latestVersion": latest_version,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/templates/{templateId}/versions/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c8590f2e6c3e5294919edafe8219c083_v3_1_3_0", json_data
        )

    def get_template_version(
        self, template_id, version_id, headers=None, **request_parameters
    ):
        """Get a template's version by the version ID. .

        Args:
            template_id(str): templateId path parameter. The id of the template to get versions of, retrieveable
                from `GET /dna/intent/api/v1/templates` .
            version_id(str): versionId path parameter. The id of the versioned template to get versions of,
                retrieveable from `GET /dna/intent/api/v1/templates/{id}/versions` .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-template-version
        """
        check_type(headers, dict)
        check_type(template_id, str, may_be_none=False)
        check_type(version_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "templateId": template_id,
            "versionId": version_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/templates/{templateId}/versions/{vers" + "ionId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bcb01a2f9225afe97043d9f5a904290_v3_1_3_0", json_data
        )

    def get_projects_details(
        self,
        id=None,
        limit=None,
        name=None,
        offset=None,
        sort_order=None,
        headers=None,
        **request_parameters
    ):
        """Get project(s) details .

        Args:
            id(str): id query parameter. Id of project to be searched .
            name(str): name query parameter. Name of project to be searched .
            offset(int): offset query parameter. Index of first result .
            limit(int): limit query parameter. The number of records to show for this page;The minimum is 1, and the
                maximum is 500. .
            sort_order(str): sortOrder query parameter. Sort Order Ascending (asc) or Descending (dsc) .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-projects-details
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(name, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "name": name,
            "offset": offset,
            "limit": limit,
            "sortOrder": sort_order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/template-programmer/project"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b1fbcb8a5286936915883ec1a0cc_v3_1_3_0", json_data
        )

    def get_templates_details(
        self,
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
        un_committed=None,
        headers=None,
        **request_parameters
    ):
        """Get template(s) details .

        Args:
            id(str): id query parameter. Id of template to be searched .
            name(str): name query parameter. Name of template to be searched .
            project_id(str): projectId query parameter. Filter template(s) based on project id .
            project_name(str): projectName query parameter. Filter template(s) based on project name .
            software_type(str): softwareType query parameter. Filter template(s) based software type .
            software_version(str): softwareVersion query parameter. Filter template(s) based softwareVersion .
            product_family(str): productFamily query parameter. Filter template(s) based on device family .
            product_series(str): productSeries query parameter. Filter template(s) based on device series .
            product_type(str): productType query parameter. Filter template(s) based on device type .
            filter_conflicting_templates(bool): filterConflictingTemplates query parameter. Filter template(s) based
                on confliting templates .
            tags(list, set, str, tuple): tags query parameter. Filter template(s) based on tags .
            un_committed(bool): unCommitted query parameter. Return uncommitted template .
            sort_order(str): sortOrder query parameter. Sort Order Ascending (asc) or Descending (dsc) .
            all_template_attributes(bool): allTemplateAttributes query parameter. Return all template attributes .
            include_version_details(bool): includeVersionDetails query parameter. Include template version details .
            offset(int): offset query parameter. Index of first result .
            limit(int): limit query parameter. The number of records to show for this page;The minimum is 1, and the
                maximum is 500. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-templates-details
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(name, str)
        check_type(project_id, str)
        check_type(project_name, str)
        check_type(software_type, str)
        check_type(software_version, str)
        check_type(product_family, str)
        check_type(product_series, str)
        check_type(product_type, str)
        check_type(filter_conflicting_templates, bool)
        check_type(tags, (list, set, str, tuple))
        check_type(un_committed, bool)
        check_type(sort_order, str)
        check_type(all_template_attributes, bool)
        check_type(include_version_details, bool)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "name": name,
            "projectId": project_id,
            "projectName": project_name,
            "softwareType": software_type,
            "softwareVersion": software_version,
            "productFamily": product_family,
            "productSeries": product_series,
            "productType": product_type,
            "filterConflictingTemplates": filter_conflicting_templates,
            "tags": tags,
            "unCommitted": un_committed,
            "sortOrder": sort_order,
            "allTemplateAttributes": all_template_attributes,
            "includeVersionDetails": include_version_details,
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/template-programmer/template"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c55b3c31568294840b4b6fd8bc0a_v3_1_3_0", json_data
        )

    def deploy_template_v2(
        self,
        forcePushTemplate=None,
        isComposite=None,
        mainTemplateId=None,
        memberTemplateDeploymentInfo=None,
        targetInfo=None,
        templateId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """V2 API to deploy a template. .

        Args:
            forcePushTemplate(boolean): Configuration Templates's forcePushTemplate.
            isComposite(boolean): Configuration Templates's Composite template flag .
            mainTemplateId(string): Configuration Templates's Main template UUID of versioned template .
            memberTemplateDeploymentInfo(list): Configuration Templates's memberTemplateDeploymentInfo  (list of
                objects).
            targetInfo(list): Configuration Templates's targetInfo (list of objects).
            templateId(string): Configuration Templates's UUID of template to be provisioned .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!deploy-template-v2
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "forcePushTemplate": forcePushTemplate,
            "isComposite": isComposite,
            "mainTemplateId": mainTemplateId,
            "memberTemplateDeploymentInfo": memberTemplateDeploymentInfo,
            "targetInfo": targetInfo,
            "templateId": templateId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bf40cea4982c54278a52ac2e7b0c458a_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/template-programmer/template/deploy"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_bf40cea4982c54278a52ac2e7b0c458a_v3_1_3_0", json_data
        )


# Alias Functions

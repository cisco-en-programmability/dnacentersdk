# -*- coding: utf-8 -*-
"""Cisco Catalyst Center User and Roles API wrapper.

Copyright (c) 2024 Cisco Systems.

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


class UserandRoles(object):
    """Cisco Catalyst Center User and Roles API (version: 2.3.7.9).

    Wraps the Catalyst Center User and Roles
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new UserandRoles
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(UserandRoles, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def add_role_api_v1(self,
                        description=None,
                        resourceTypes=None,
                        role=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Add a new role in the system .

        Args:
            description(string): User and Roles's Description of role .
            resourceTypes(list): User and Roles's resourceTypes (list of objects).
            role(string): User and Roles's Name of the role .
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
            https://developer.cisco.com/docs/dna-center/#!add-role-a-p-i
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'role':
                role,
            'description':
                description,
            'resourceTypes':
                resourceTypes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a88c7510a15578b8eb2df183a92d5d_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/system/api/v1/role')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a88c7510a15578b8eb2df183a92d5d_v2_3_7_9', json_data)

    def update_role_api_v1(self,
                           description=None,
                           resourceTypes=None,
                           roleId=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """Update a role in the system .

        Args:
            description(string): User and Roles's Description of the role .
            resourceTypes(list): User and Roles's resourceTypes (list of objects).
            roleId(string): User and Roles's Id of the role .
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
            https://developer.cisco.com/docs/dna-center/#!update-role-a-p-i
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'roleId':
                roleId,
            'description':
                description,
            'resourceTypes':
                resourceTypes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_ff5bf5a67c6c5c0aa9e7ba84c088e1a6_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/system/api/v1/role')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_ff5bf5a67c6c5c0aa9e7ba84c088e1a6_v2_3_7_9', json_data)

    def get_permissions_api_v1(self,
                               headers=None,
                               **request_parameters):
        """Get permissions for a role in the system. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!get-permissions-a-p-i
        """
        check_type(headers, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
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

        e_url = ('/dna/system/api/v1/role/permissions')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ec0b30eca9d540a845848cffd7c602a_v2_3_7_9', json_data)

    def delete_role_api_v1(self,
                           role_id,
                           headers=None,
                           **request_parameters):
        """Delete a role in the system .

        Args:
            role_id(str): roleId path parameter. The Id of the role to be deleted .
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
            https://developer.cisco.com/docs/dna-center/#!delete-role-a-p-i
        """
        check_type(headers, dict)
        check_type(role_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'roleId': role_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/system/api/v1/role/{roleId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_da9e850c44d353f78ab002a640e5604f_v2_3_7_9', json_data)

    def get_roles_api_v1(self,
                         headers=None,
                         **request_parameters):
        """Get all roles in the system .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!get-roles-a-p-i
        """
        check_type(headers, dict)
        if headers is not None:
            if 'invokeSource' in headers:
                check_type(headers.get('invokeSource'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
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

        e_url = ('/dna/system/api/v1/roles')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bef02e8f6f8354dc99e375826a87c88c_v2_3_7_9', json_data)

    def get_users_api_v1(self,
                         invoke_source,
                         auth_source=None,
                         headers=None,
                         **request_parameters):
        """Get all users in the system .

        Args:
            invoke_source(str): invokeSource query parameter. The source that invokes this API. The value of
                this query parameter must be set to "external". .
            auth_source(str): authSource query parameter. The source that authenticates the user. The value
                of this query parameter can be set to "internal" or "external". If not provided, then
                all users will be returned in the response. .
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
            https://developer.cisco.com/docs/dna-center/#!get-users-a-p-i
        """
        check_type(headers, dict)
        check_type(invoke_source, str,
                   may_be_none=False)
        check_type(auth_source, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'invokeSource':
                invoke_source,
            'authSource':
                auth_source,
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

        e_url = ('/dna/system/api/v1/user')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fa405b6d1be56739f2dfeea63212015_v2_3_7_9', json_data)

    def add_user_api_v1(self,
                        email=None,
                        firstName=None,
                        lastName=None,
                        password=None,
                        roleList=None,
                        username=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Add a new user in the system .

        Args:
            email(string): User and Roles's Email.
            firstName(string): User and Roles's First Name.
            lastName(string): User and Roles's Last Name.
            password(string): User and Roles's Password.
            roleList(list): User and Roles's Role id list  (list of strings).
            username(string): User and Roles's Username.
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
            https://developer.cisco.com/docs/dna-center/#!add-user-a-p-i
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'firstName':
                firstName,
            'lastName':
                lastName,
            'username':
                username,
            'password':
                password,
            'email':
                email,
            'roleList':
                roleList,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d82755e5e03510daf0951c1f42c2702_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/system/api/v1/user')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d82755e5e03510daf0951c1f42c2702_v2_3_7_9', json_data)

    def update_user_api_v1(self,
                           email=None,
                           firstName=None,
                           lastName=None,
                           roleList=None,
                           userId=None,
                           username=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """Update a user in the system .

        Args:
            email(string): User and Roles's email should be set if the original value is not empty .
            firstName(string): User and Roles's firstName should be set if the original value is not empty .
            lastName(string): User and Roles's lastName should be set if the original value is not empty .
            roleList(list): User and Roles's Role id list  (list of strings).
            userId(string): User and Roles's User Id.
            username(string): User and Roles's Username.
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
            https://developer.cisco.com/docs/dna-center/#!update-user-a-p-i
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'firstName':
                firstName,
            'lastName':
                lastName,
            'email':
                email,
            'username':
                username,
            'userId':
                userId,
            'roleList':
                roleList,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d2bd5f05bd535a89ebadb30e2ede9e_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/system/api/v1/user')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_d2bd5f05bd535a89ebadb30e2ede9e_v2_3_7_9', json_data)

    def delete_user_api_v1(self,
                           user_id,
                           headers=None,
                           **request_parameters):
        """Delete a user in the system .

        Args:
            user_id(str): userId path parameter. The id of the user to be deleted .
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
            https://developer.cisco.com/docs/dna-center/#!delete-user-a-p-i
        """
        check_type(headers, dict)
        check_type(user_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'userId': user_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/system/api/v1/user/{userId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c65c6cc65f068766cbb8a42ad387_v2_3_7_9', json_data)

    def get_external_authentication_setting_api_v1(self,
                                                   headers=None,
                                                   **request_parameters):
        """Get the External Authentication setting. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!get-external-authentication-setting-a-p-i
        """
        check_type(headers, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
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

        e_url = ('/dna/system/api/v1/users/external-authentication')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ac03ba045f60925fd7843bf9e279_v2_3_7_9', json_data)

    def manage_external_authentication_setting_api_v1(self,
                                                      enable=None,
                                                      headers=None,
                                                      payload=None,
                                                      active_validation=True,
                                                      **request_parameters):
        """Enable or disable external authentication in the System. Please find the Administrator Guide for your particular
        release from the list linked below and follow the steps required to enable external authentication
        before trying to do so from this API. https://www.cisco.com/c/en/us/support/cloud-systems-
        management/dna-center/products-maintenance-guides-list.html .

        Args:
            enable(boolean): User and Roles's Enable/disable External Authentication. .
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
            https://developer.cisco.com/docs/dna-center/#!manage-external-authentication-setting-a-p-i
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'enable':
                enable,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e4f57e8f06856ee9a7e490d01f7f692_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/system/api/v1/users/external-authentication')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e4f57e8f06856ee9a7e490d01f7f692_v2_3_7_9', json_data)

    def get_external_authentication_servers_api_v1(self,
                                                   invoke_source,
                                                   headers=None,
                                                   **request_parameters):
        """Get external users authentication servers. .

        Args:
            invoke_source(str): invokeSource query parameter. The source that invokes this API. The value of
                this query parameter must be set to "external". .
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
            https://developer.cisco.com/docs/dna-center/#!get-external-authentication-servers-a-p-i
        """
        check_type(headers, dict)
        check_type(invoke_source, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'invokeSource':
                invoke_source,
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

        e_url = ('/dna/system/api/v1/users/external-servers')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_def9045d4d9c96bcd42172a79c_v2_3_7_9', json_data)

    def add_and_update_aaa_attribute_api_v1(self,
                                              attributeName=None,
                                              headers=None,
                                              payload=None,
                                              active_validation=True,
                                              **request_parameters):
        """Add or update the custom AAA attribute for external authentication. Note that if you decide not to set the
        custom AAA attribute, a default AAA attribute will be used for authentication based on the protocol
        supported by your server. For TACACS servers it will be "cisco-av-pair" and for RADIUS servers it will
        be "Cisco-AVPair". .

        Args:
            attributeName(string): User and Roles's name of the custom AAA attribute. .
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
            https://developer.cisco.com/docs/dna-center/#!add-and-update-a-a-a-attribute-a-p-i
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'attributeName':
                attributeName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f5bfccc7e30550baa7046f74daa1ef2_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/system/api/v1/users/external-servers/aaa-attribute')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f5bfccc7e30550baa7046f74daa1ef2_v2_3_7_9', json_data)

    def delete_aaa_attribute_api_v1(self,
                                      headers=None,
                                      **request_parameters):
        """Delete the custom AAA attribute that was added. Note that by deleting the AAA attribute, a default AAA attribute
        will be used for authentication based on the protocol supported by your server. For TACACS servers it
        will be "cisco-av-pair" and for RADIUS servers it will be "Cisco-AVPair". .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-a-a-attribute-a-p-i
        """
        check_type(headers, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
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

        e_url = ('/dna/system/api/v1/users/external-servers/aaa-attribute')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f20c99b436bd5be8bdb9094db3a47f01_v2_3_7_9', json_data)

    def get_aaa_attribute_api_v1(self,
                                   headers=None,
                                   **request_parameters):
        """Get the current value of the custom AAA attribute. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!get-a-a-a-attribute-a-p-i
        """
        check_type(headers, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
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

        e_url = ('/dna/system/api/v1/users/external-servers/aaa-attribute')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bedf83096a45ad1beaaa1fc6c192103_v2_3_7_9', json_data)



    # Alias Function
    def add_and_update_aaa_attribute_api(self,
                                              attributeName=None,
                                              headers=None,
                                              payload=None,
                                              active_validation=True,
                                              **request_parameters):
        """ This function is an alias of add_and_update_aaa_attribute_api_v1 .
        Args:
            attributeName(string): User and Roles's name of the custom AAA attribute. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of add_and_update_aaa_attribute_api_v1 .
        """
        return self.add_and_update_aaa_attribute_api_v1(
                    attributeName=attributeName,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def get_users_api(self,
                         invoke_source,
                         auth_source=None,
                         headers=None,
                         **request_parameters):
        """ This function is an alias of get_users_api_v1 .
        Args:
            invoke_source(str): invokeSource query parameter. The source that invokes this API. The value of
                this query parameter must be set to "external". .
            auth_source(str): authSource query parameter. The source that authenticates the user. The value
                of this query parameter can be set to "internal" or "external". If not provided, then
                all users will be returned in the response. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_users_api_v1 .
        """
        return self.get_users_api_v1(
                    invoke_source=invoke_source,
                    auth_source=auth_source,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_external_authentication_servers_api(self,
                                                   invoke_source,
                                                   headers=None,
                                                   **request_parameters):
        """ This function is an alias of get_external_authentication_servers_api_v1 .
        Args:
            invoke_source(str): invokeSource query parameter. The source that invokes this API. The value of
                this query parameter must be set to "external". .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_external_authentication_servers_api_v1 .
        """
        return self.get_external_authentication_servers_api_v1(
                    invoke_source=invoke_source,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def add_user_api(self,
                        email=None,
                        firstName=None,
                        lastName=None,
                        password=None,
                        roleList=None,
                        username=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """ This function is an alias of add_user_api_v1 .
        Args:
            email(string): User and Roles's Email.
            firstName(string): User and Roles's First Name.
            lastName(string): User and Roles's Last Name.
            password(string): User and Roles's Password.
            roleList(list): User and Roles's Role id list  (list of strings).
            username(string): User and Roles's Username.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of add_user_api_v1 .
        """
        return self.add_user_api_v1(
                    email=email,
                    firstName=firstName,
                    lastName=lastName,
                    password=password,
                    roleList=roleList,
                    username=username,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def delete_aaa_attribute_api(self,
                                      headers=None,
                                      **request_parameters):
        """ This function is an alias of delete_aaa_attribute_api_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_aaa_attribute_api_v1 .
        """
        return self.delete_aaa_attribute_api_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def delete_user_api(self,
                           user_id,
                           headers=None,
                           **request_parameters):
        """ This function is an alias of delete_user_api_v1 .
        Args:
            user_id(str): userId path parameter. The id of the user to be deleted .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_user_api_v1 .
        """
        return self.delete_user_api_v1(
                    user_id=user_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_external_authentication_setting_api(self,
                                                   headers=None,
                                                   **request_parameters):
        """ This function is an alias of get_external_authentication_setting_api_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_external_authentication_setting_api_v1 .
        """
        return self.get_external_authentication_setting_api_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_roles_api(self,
                         headers=None,
                         **request_parameters):
        """ This function is an alias of get_roles_api_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_roles_api_v1 .
        """
        return self.get_roles_api_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def add_role_api(self,
                        description=None,
                        resourceTypes=None,
                        role=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """ This function is an alias of add_role_api_v1 .
        Args:
            description(string): User and Roles's Description of role .
            resourceTypes(list): User and Roles's resourceTypes (list of objects).
            role(string): User and Roles's Name of the role .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of add_role_api_v1 .
        """
        return self.add_role_api_v1(
                    description=description,
                    resourceTypes=resourceTypes,
                    role=role,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def update_user_api(self,
                           email=None,
                           firstName=None,
                           lastName=None,
                           roleList=None,
                           userId=None,
                           username=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """ This function is an alias of update_user_api_v1 .
        Args:
            email(string): User and Roles's email should be set if the original value is not empty .
            firstName(string): User and Roles's firstName should be set if the original value is not empty .
            lastName(string): User and Roles's lastName should be set if the original value is not empty .
            roleList(list): User and Roles's Role id list  (list of strings).
            userId(string): User and Roles's User Id.
            username(string): User and Roles's Username.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_user_api_v1 .
        """
        return self.update_user_api_v1(
                    email=email,
                    firstName=firstName,
                    lastName=lastName,
                    roleList=roleList,
                    userId=userId,
                    username=username,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def get_permissions_api(self,
                               headers=None,
                               **request_parameters):
        """ This function is an alias of get_permissions_api_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_permissions_api_v1 .
        """
        return self.get_permissions_api_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_aaa_attribute_api(self,
                                   headers=None,
                                   **request_parameters):
        """ This function is an alias of get_aaa_attribute_api_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_aaa_attribute_api_v1 .
        """
        return self.get_aaa_attribute_api_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def manage_external_authentication_setting_api(self,
                                                      enable=None,
                                                      headers=None,
                                                      payload=None,
                                                      active_validation=True,
                                                      **request_parameters):
        """ This function is an alias of manage_external_authentication_setting_api_v1 .
        Args:
            enable(boolean): User and Roles's Enable/disable External Authentication. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of manage_external_authentication_setting_api_v1 .
        """
        return self.manage_external_authentication_setting_api_v1(
                    enable=enable,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def delete_role_api(self,
                           role_id,
                           headers=None,
                           **request_parameters):
        """ This function is an alias of delete_role_api_v1 .
        Args:
            role_id(str): roleId path parameter. The Id of the role to be deleted .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_role_api_v1 .
        """
        return self.delete_role_api_v1(
                    role_id=role_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def update_role_api(self,
                           description=None,
                           resourceTypes=None,
                           roleId=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """ This function is an alias of update_role_api_v1 .
        Args:
            description(string): User and Roles's Description of the role .
            resourceTypes(list): User and Roles's resourceTypes (list of objects).
            roleId(string): User and Roles's Id of the role .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_role_api_v1 .
        """
        return self.update_role_api_v1(
                    description=description,
                    resourceTypes=resourceTypes,
                    roleId=roleId,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )



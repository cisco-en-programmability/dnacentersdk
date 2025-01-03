# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Authentication Management API wrapper.

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


class AuthenticationManagement(object):
    """Cisco Catalyst Center Authentication Management API (version: 2.3.7.9).

    Wraps the Catalyst Center Authentication Management
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new AuthenticationManagement
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(AuthenticationManagement, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def import_certificate_v1(self,
                              list_of_users=None,
                              pk_password=None,
                              headers=None,
                              **request_parameters):
        """This API enables a user to import a PEM certificate and its key for the controller and/or disaster recovery. .

        Args:
            pk_password(str): pkPassword query parameter. Password for encrypted private key .
            list_of_users(str, list, set, tuple): listOfUsers query parameter. Specify whether the
                certificate will be used for controller ("server"), disaster recovery ("ipsec") or both
                ("server, ipsec"). If no value is provided, the default value taken will be "server" .
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
            https://developer.cisco.com/docs/dna-center/#!import-certificate
        """
        check_type(headers, dict)
        check_type(pk_password, str)
        check_type(list_of_users, (str, list, set, tuple))
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'pkPassword':
                pk_password,
            'listOfUsers':
                list_of_users,
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

        e_url = ('/dna/intent/api/v1/certificate')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b19d7e8de2ca5329930d06f041a4a173_v2_3_7_9', json_data)

    def import_certificate_p12_v1(self,
                                  p12_password,
                                  list_of_users=None,
                                  pk_password=None,
                                  headers=None,
                                  **request_parameters):
        """This API enables a user to import a PKCS12 certificate bundle for the controller and/or disaster recovery. .

        Args:
            p12_password(str): p12Password query parameter. The password for PKCS12 certificate bundle .
            pk_password(str): pkPassword query parameter. Password for encrypted private key .
            list_of_users(str, list, set, tuple): listOfUsers query parameter. Specify whether the
                certificate will be used for controller ("server"), disaster recovery ("ipsec") or both
                ("server, ipsec"). If no value is provided, the default value taken will be "server" .
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
            https://developer.cisco.com/docs/dna-center/#!import-certificate-p12
        """
        check_type(headers, dict)
        check_type(p12_password, str,
                   may_be_none=False)
        check_type(pk_password, str)
        check_type(list_of_users, (str, list, set, tuple))
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'p12Password':
                p12_password,
            'pkPassword':
                pk_password,
            'listOfUsers':
                list_of_users,
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

        e_url = ('/dna/intent/api/v1/certificate-p12')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c80e660c2e36582f939a7403ef15de22_v2_3_7_9', json_data)

    def authentication_api_v1(self,
                              headers=None,
                              **request_parameters):
        """API to obtain an access token, which remains valid for 1 hour. The token obtained using this API is required to
        be set as value to the X-Auth-Token HTTP Header for all API calls to Cisco DNA Center. .

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
            https://developer.cisco.com/docs/dna-center/#!authentication-a-p-i
        """
        check_type(headers, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'Authorization' in headers:
                check_type(headers.get('Authorization'),
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

        e_url = ('/dna/system/api/v1/auth/token')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a6bfcd88e22c5c138657b340870b4ebb_v2_3_7_9', json_data)



    # Alias Function
    def authentication_api(self,
                              headers=None,
                              **request_parameters):
        """ This function is an alias of authentication_api_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of authentication_api_v1 .
        """
        return self.authentication_api_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def import_certificate_p12(self,
                                  p12_password,
                                  list_of_users=None,
                                  pk_password=None,
                                  headers=None,
                                  **request_parameters):
        """ This function is an alias of import_certificate_p12_v1 .
        Args:
            p12_password(str): p12Password query parameter. The password for PKCS12 certificate bundle .
            pk_password(str): pkPassword query parameter. Password for encrypted private key .
            list_of_users(str, list, set, tuple): listOfUsers query parameter. Specify whether the
                certificate will be used for controller ("server"), disaster recovery ("ipsec") or both
                ("server, ipsec"). If no value is provided, the default value taken will be "server" .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of import_certificate_p12_v1 .
        """
        return self.import_certificate_p12_v1(
                    p12_password=p12_password,
                    list_of_users=list_of_users,
                    pk_password=pk_password,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def import_certificate(self,
                              list_of_users=None,
                              pk_password=None,
                              headers=None,
                              **request_parameters):
        """ This function is an alias of import_certificate_v1 .
        Args:
            pk_password(str): pkPassword query parameter. Password for encrypted private key .
            list_of_users(str, list, set, tuple): listOfUsers query parameter. Specify whether the
                certificate will be used for controller ("server"), disaster recovery ("ipsec") or both
                ("server, ipsec"). If no value is provided, the default value taken will be "server" .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of import_certificate_v1 .
        """
        return self.import_certificate_v1(
                    list_of_users=list_of_users,
                    pk_password=pk_password,
                    headers=headers,
                    **request_parameters
        )



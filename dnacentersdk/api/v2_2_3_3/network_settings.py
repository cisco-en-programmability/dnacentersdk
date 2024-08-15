# -*- coding: utf-8 -*-
"""Cisco DNA Center Network Settings API wrapper.

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


from builtins import *


from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class NetworkSettings(object):
    """Cisco DNA Center Network Settings API (version: 2.2.3.3).

    Wraps the DNA Center Network Settings
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkSettings
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkSettings, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def assign_credential_to_site(self,
                                  site_id,
                                  cliId=None,
                                  httpRead=None,
                                  httpWrite=None,
                                  snmpV2ReadId=None,
                                  snmpV2WriteId=None,
                                  snmpV3Id=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Assign Device Credential To Site  .

        Args:
            cliId(string): Network Settings's Cli Id.
            httpRead(string): Network Settings's Http Read.
            httpWrite(string): Network Settings's Http Write.
            snmpV2ReadId(string): Network Settings's Snmp V2 Read Id.
            snmpV2WriteId(string): Network Settings's Snmp V2 Write Id.
            snmpV3Id(string): Network Settings's Snmp V3 Id.
            site_id(str): siteId path parameter. site id to assign credential. .
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
        check_type(site_id, str,
                   may_be_none=False)
        if headers is not None:
            if '__persistbapioutput' in headers:
                check_type(headers.get('__persistbapioutput'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'siteId': site_id,
        }
        _payload = {
            'cliId':
                cliId,
            'snmpV2ReadId':
                snmpV2ReadId,
            'snmpV2WriteId':
                snmpV2WriteId,
            'httpRead':
                httpRead,
            'httpWrite':
                httpWrite,
            'snmpV3Id':
                snmpV3Id,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e4f91ea42515ccdbc24549b84ca1e90_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/credential-to-site/{siteId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e4f91ea42515ccdbc24549b84ca1e90_v2_2_3_3', json_data)

    def create_device_credentials(self,
                                  settings=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """API to create device credentials. .

        Args:
            settings(object): Network Settings's settings.
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
            'settings':
                settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_cf2cac6f150c9bee9ade37921b162_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/device-credential')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_cf2cac6f150c9bee9ade37921b162_v2_2_3_3', json_data)

    def update_device_credentials(self,
                                  settings=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """API to update device credentials. .

        Args:
            settings(object): Network Settings's settings.
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
            'settings':
                settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d7161b33157dba957ba18eda440c2_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/device-credential')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_d7161b33157dba957ba18eda440c2_v2_2_3_3', json_data)

    def get_device_credential_details(self,
                                      site_id=None,
                                      headers=None,
                                      **request_parameters):
        """API to get device credential details. .

        Args:
            site_id(str): siteId query parameter. Site id to retrieve the credential details associated with
                the site. .
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
        check_type(site_id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteId':
                site_id,
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

        e_url = ('/dna/intent/api/v1/device-credential')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d8cf995d9d99bdc31707817456_v2_2_3_3', json_data)

    def delete_device_credential(self,
                                 id,
                                 headers=None,
                                 **request_parameters):
        """Delete device credential. .

        Args:
            id(str): id path parameter. global credential id .
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
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/device-credential/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e8e021f1c51eeaf0d102084481486_v2_2_3_3', json_data)

    def get_global_pool(self,
                        limit=None,
                        offset=None,
                        headers=None,
                        **request_parameters):
        """API to get global pool. .

        Args:
            offset(str,int): offset query parameter. offset/starting row .
            limit(str,int): limit query parameter. No of Global Pools to be retrieved .
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
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
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

        e_url = ('/dna/intent/api/v1/global-pool')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ebdcd84fc41754a69eaeacf7c0b0731c_v2_2_3_3', json_data)

    def update_global_pool(self,
                           settings=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """API to update global pool .

        Args:
            settings(object): Network Settings's settings.
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
            'settings':
                settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_c380301e3e05423bdc1857ff00ae77a_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-pool')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_c380301e3e05423bdc1857ff00ae77a_v2_2_3_3', json_data)

    def create_global_pool(self,
                           settings=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """API to create global pool. .

        Args:
            settings(object): Network Settings's settings.
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
            'settings':
                settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_eecf4323cb285985be72a7e061891059_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-pool')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_eecf4323cb285985be72a7e061891059_v2_2_3_3', json_data)

    def delete_global_ip_pool(self,
                              id,
                              headers=None,
                              **request_parameters):
        """API to delete global IP pool. .

        Args:
            id(str): id path parameter. global pool id .
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
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-pool/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f9079863c95acd945c51f728cbf81f_v2_2_3_3', json_data)

    def get_network(self,
                    site_id=None,
                    headers=None,
                    **request_parameters):
        """API to get  DHCP and DNS center server details. .

        Args:
            site_id(str): siteId query parameter. Site id to get the network settings associated with the
                site. .
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
        check_type(site_id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteId':
                site_id,
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

        e_url = ('/dna/intent/api/v1/network')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b199c175281977a7e9e6bd9255b_v2_2_3_3', json_data)

    def create_network(self,
                       site_id,
                       settings=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """API to create a network for DHCP and DNS center server settings. .

        Args:
            settings(object): Network Settings's settings.
            site_id(str): siteId path parameter. Site id to which site details to associate with the network
                settings. .
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
        check_type(site_id, str,
                   may_be_none=False)
        if headers is not None:
            if '__persistbapioutput' in headers:
                check_type(headers.get('__persistbapioutput'),
                           bool)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'siteId': site_id,
        }
        _payload = {
            'settings':
                settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_eca62ef076b5627a85b2a5959613fb8_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network/{siteId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_eca62ef076b5627a85b2a5959613fb8_v2_2_3_3', json_data)

    def update_network(self,
                       site_id,
                       settings=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """API to update network for DHCP and DNS center server settings. .

        Args:
            settings(object): Network Settings's settings.
            site_id(str): siteId path parameter. Site id to update the network settings which is associated
                with the site .
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
        check_type(site_id, str,
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
            'siteId': site_id,
        }
        _payload = {
            'settings':
                settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e1b8c435195d56368c24a54dcce007d0_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network/{siteId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_e1b8c435195d56368c24a54dcce007d0_v2_2_3_3', json_data)

    def get_reserve_ip_subpool(self,
                               limit=None,
                               offset=None,
                               site_id=None,
                               headers=None,
                               **request_parameters):
        """API to get the ip subpool info. .

        Args:
            site_id(str): siteId query parameter. site id to get the reserve ip associated with the site .
            offset(str,int): offset query parameter. offset/starting row .
            limit(str,int): limit query parameter. No of Global Pools to be retrieved .
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
        check_type(site_id, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteId':
                site_id,
            'offset':
                offset,
            'limit':
                limit,
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

        e_url = ('/dna/intent/api/v1/reserve-ip-subpool')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d84253559e9d3e81881a4bd2fc_v2_2_3_3', json_data)

    def release_reserve_ip_subpool(self,
                                   id,
                                   headers=None,
                                   **request_parameters):
        """API to delete the reserved ip subpool .

        Args:
            id(str): id path parameter. Id of reserve ip subpool to be deleted. .
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
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/reserve-ip-subpool/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_eabbb425255a57578e9db00cda1f303a_v2_2_3_3', json_data)

    def reserve_ip_subpool(self,
                           site_id,
                           ipv4DhcpServers=None,
                           ipv4DnsServers=None,
                           ipv4GateWay=None,
                           ipv4GlobalPool=None,
                           ipv4Prefix=None,
                           ipv4PrefixLength=None,
                           ipv4Subnet=None,
                           ipv4TotalHost=None,
                           ipv6AddressSpace=None,
                           ipv6DhcpServers=None,
                           ipv6DnsServers=None,
                           ipv6GateWay=None,
                           ipv6GlobalPool=None,
                           ipv6Prefix=None,
                           ipv6PrefixLength=None,
                           ipv6Subnet=None,
                           ipv6TotalHost=None,
                           name=None,
                           slaacSupport=None,
                           type=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """API to reserve an ip subpool from the global pool .

        Args:
            ipv4DhcpServers(list): Network Settings's IPv4 input for dhcp server ip example: 1.1.1.1  (list of
                strings).
            ipv4DnsServers(list): Network Settings's IPv4 input for dns server ip example: 4.4.4.4  (list of
                strings).
            ipv4GateWay(string): Network Settings's Gateway ip address details, example: 175.175.0.1 .
            ipv4GlobalPool(string): Network Settings's IP v4 Global pool address with cidr, example: 175.175.0.0/16
                .
            ipv4Prefix(boolean): Network Settings's IPv4 prefix value is true, the ip4 prefix length input field is
                enabled , if it is false ipv4 total Host input is enable .
            ipv4PrefixLength(integer): Network Settings's The ipv4 prefix length is required when ipv4prefix value
                is true. .
            ipv4Subnet(string): Network Settings's IPv4 Subnet address, example: 175.175.0.0 .
            ipv4TotalHost(integer): Network Settings's IPv4 total host is required when ipv4prefix value is false. .
            ipv6AddressSpace(boolean): Network Settings's If the value is false only ipv4 input are required,
                otherwise both ipv6 and ipv4 are required .
            ipv6DhcpServers(list): Network Settings's IPv6 format dhcp server as input example : 2001:db8::1234
                (list of strings).
            ipv6DnsServers(list): Network Settings's IPv6 format dns server input example: 2001:db8::1234  (list of
                strings).
            ipv6GateWay(string): Network Settings's Gateway ip address details, example: 2001:db8:85a3:0:100::1 .
            ipv6GlobalPool(string): Network Settings's IPv6 Global pool address with cidr this is required when
                Ipv6AddressSpace value is true, example: 2001:db8:85a3::/64 .
            ipv6Prefix(boolean): Network Settings's Ipv6 prefix value is true, the ip6 prefix length input field is
                enabled , if it is false ipv6 total Host input is enable .
            ipv6PrefixLength(integer): Network Settings's IPv6 prefix length is required when the ipv6prefix value
                is true .
            ipv6Subnet(string): Network Settings's IPv6 Subnet address, example :2001:db8:85a3:0:100:: .
            ipv6TotalHost(integer): Network Settings's IPv6 total host is required when ipv6prefix value is false. .
            name(string): Network Settings's Name of the reserve ip sub pool .
            slaacSupport(boolean): Network Settings's Slaac Support.
            type(string): Network Settings's Type of the reserve ip sub pool . Available values are 'Generic',
                'LAN', 'WAN', 'management' and 'service'.
            site_id(str): siteId path parameter. Site id to reserve the ip sub pool. .
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
        check_type(site_id, str,
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
            'siteId': site_id,
        }
        _payload = {
            'name':
                name,
            'type':
                type,
            'ipv6AddressSpace':
                ipv6AddressSpace,
            'ipv4GlobalPool':
                ipv4GlobalPool,
            'ipv4Prefix':
                ipv4Prefix,
            'ipv4PrefixLength':
                ipv4PrefixLength,
            'ipv4Subnet':
                ipv4Subnet,
            'ipv4GateWay':
                ipv4GateWay,
            'ipv4DhcpServers':
                ipv4DhcpServers,
            'ipv4DnsServers':
                ipv4DnsServers,
            'ipv6GlobalPool':
                ipv6GlobalPool,
            'ipv6Prefix':
                ipv6Prefix,
            'ipv6PrefixLength':
                ipv6PrefixLength,
            'ipv6Subnet':
                ipv6Subnet,
            'ipv6GateWay':
                ipv6GateWay,
            'ipv6DhcpServers':
                ipv6DhcpServers,
            'ipv6DnsServers':
                ipv6DnsServers,
            'ipv4TotalHost':
                ipv4TotalHost,
            'ipv6TotalHost':
                ipv6TotalHost,
            'slaacSupport':
                slaacSupport,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_cec6c85d9bb4bcc8f61f31296b_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/reserve-ip-subpool/{siteId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_cec6c85d9bb4bcc8f61f31296b_v2_2_3_3', json_data)

    def update_reserve_ip_subpool(self,
                                  id,
                                  site_id,
                                  ipv4DhcpServers=None,
                                  ipv4DnsServers=None,
                                  ipv4GateWay=None,
                                  ipv6AddressSpace=None,
                                  ipv6DhcpServers=None,
                                  ipv6DnsServers=None,
                                  ipv6GateWay=None,
                                  ipv6GlobalPool=None,
                                  ipv6Prefix=None,
                                  ipv6PrefixLength=None,
                                  ipv6Subnet=None,
                                  ipv6TotalHost=None,
                                  name=None,
                                  slaacSupport=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """API to update ip subpool from the global pool .

        Args:
            ipv4DhcpServers(list): Network Settings's IPv4 input for dhcp server ip example: 1.1.1.1  (list of
                strings).
            ipv4DnsServers(list): Network Settings's IPv4 input for dns server ip  example: 4.4.4.4  (list of
                strings).
            ipv4GateWay(string): Network Settings's Ipv4 Gate Way.
            ipv6AddressSpace(boolean): Network Settings's If the value is false only ipv4 input are required,
                otherwise both ipv6 and ipv4 are required .
            ipv6DhcpServers(list): Network Settings's IPv6 format dhcp server as input example : 2001:db8::1234
                (list of strings).
            ipv6DnsServers(list): Network Settings's IPv6 format dns server input example: 2001:db8::1234  (list of
                strings).
            ipv6GateWay(string): Network Settings's Gateway ip address details, example: 2001:db8:85a3:0:100::1 .
            ipv6GlobalPool(string): Network Settings's IP v6 Global pool address with cidr this is required when
                Ipv6AddressSpace value is true, example: 2001:db8:85a3::/64 .
            ipv6Prefix(boolean): Network Settings's IPv6 prefix value is true, the ip6 prefix length input field is
                enabled , if it is false  ipv6 total Host input is enable .
            ipv6PrefixLength(integer): Network Settings's IPv6 prefix length is required when the ipv6prefix value
                is true .
            ipv6Subnet(string): Network Settings's IPv6 Subnet address, example :2001:db8:85a3:0:100:: .
            ipv6TotalHost(integer): Network Settings's IPv6 total host is required when ipv6prefix value is false. .
            name(string): Network Settings's Name of the reserve ip sub pool .
            slaacSupport(boolean): Network Settings's Slaac Support.
            site_id(str): siteId path parameter. Site id of site to update sub pool. .
            id(str): id query parameter. Id of subpool to be associated with the site .
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
        check_type(id, str,
                   may_be_none=False)
        check_type(site_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'id':
                id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'siteId': site_id,
        }
        _payload = {
            'name':
                name,
            'ipv6AddressSpace':
                ipv6AddressSpace,
            'ipv4DhcpServers':
                ipv4DhcpServers,
            'ipv4DnsServers':
                ipv4DnsServers,
            'ipv6GlobalPool':
                ipv6GlobalPool,
            'ipv6Prefix':
                ipv6Prefix,
            'ipv6PrefixLength':
                ipv6PrefixLength,
            'ipv6Subnet':
                ipv6Subnet,
            'ipv6GateWay':
                ipv6GateWay,
            'ipv6DhcpServers':
                ipv6DhcpServers,
            'ipv6DnsServers':
                ipv6DnsServers,
            'ipv6TotalHost':
                ipv6TotalHost,
            'slaacSupport':
                slaacSupport,
            'ipv4GateWay':
                ipv4GateWay,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_fd6083b0c65d03b2d53f10b3ece59d_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/reserve-ip-subpool/{siteId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_fd6083b0c65d03b2d53f10b3ece59d_v2_2_3_3', json_data)

    def get_service_provider_details(self,
                                     headers=None,
                                     **request_parameters):
        """API to get service provider details (QoS). .

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
            ApiError: If the DNA Center cloud returns an error.
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

        e_url = ('/dna/intent/api/v1/service-provider')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dda850a0675b888048adf8d488aec1_v2_2_3_3', json_data)

    def create_sp_profile(self,
                          settings=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **request_parameters):
        """API to create service provider profile(QOS). .

        Args:
            settings(object): Network Settings's settings.
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
            'settings':
                settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_ffa347eb411567a9c793696795250a5_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/service-provider')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_ffa347eb411567a9c793696795250a5_v2_2_3_3', json_data)

    def update_sp_profile(self,
                          settings=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **request_parameters):
        """API to update SP profile .

        Args:
            settings(object): Network Settings's settings.
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
            'settings':
                settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e22c99a82f5764828810acb45e7a9e_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/service-provider')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_e22c99a82f5764828810acb45e7a9e_v2_2_3_3', json_data)

    def delete_sp_profile(self,
                          sp_profile_name,
                          headers=None,
                          **request_parameters):
        """API to delete Service Provider profile (QoS). .

        Args:
            sp_profile_name(str): spProfileName path parameter. sp profile name .
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
        check_type(sp_profile_name, str,
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
            'spProfileName': sp_profile_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sp-profile/{spProfileName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a1d68f15e02adc37239b3fcbbb6_v2_2_3_3', json_data)

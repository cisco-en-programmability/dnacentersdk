# -*- coding: utf-8 -*-
"""Cisco DNA Center SDA API wrapper.

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


class Sda(object):
    """Cisco DNA Center SDA API (version: 2.3.7.6).

    Wraps the DNA Center SDA
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Sda
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Sda, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_default_authentication_profile(self,
                                           site_name_hierarchy,
                                           authenticate_template_name=None,
                                           headers=None,
                                           **request_parameters):
        """Get default authentication profile from SDA Fabric .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter.
            authenticate_template_name(str): authenticateTemplateName query parameter.
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
        check_type(site_name_hierarchy, str,
                   may_be_none=False)
        check_type(authenticate_template_name, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteNameHierarchy':
                site_name_hierarchy,
            'authenticateTemplateName':
                authenticate_template_name,
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

        e_url = ('/dna/intent/api/v1/business/sda/authentication-profile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e414dcbeeabd5a359352a0e2ad5ec3f5_v2_3_7_6', json_data)

    def add_default_authentication_profile(self,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **request_parameters):
        """Add default authentication template in SDA Fabric .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_d1d42ef2f1895a82a2830bf1353e6baa_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/authentication-profile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d1d42ef2f1895a82a2830bf1353e6baa_v2_3_7_6', json_data)

    def update_default_authentication_profile(self,
                                              headers=None,
                                              payload=None,
                                              active_validation=True,
                                              **request_parameters):
        """Update default authentication profile in SDA Fabric .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_d999a1d36ee52babb6b619877dad734_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/authentication-profile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_d999a1d36ee52babb6b619877dad734_v2_3_7_6', json_data)

    def delete_default_authentication_profile(self,
                                              site_name_hierarchy,
                                              headers=None,
                                              **request_parameters):
        """Delete default authentication profile in SDA Fabric .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter.
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
        check_type(site_name_hierarchy, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteNameHierarchy':
                site_name_hierarchy,
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

        e_url = ('/dna/intent/api/v1/business/sda/authentication-profile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b2be8b5dda8b81620b903afe9f_v2_3_7_6', json_data)

    def adds_border_device(self,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """Add border device in SDA Fabric .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_b6f2d8e46cdd5f05bb06f52cd1b26fb2_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/border-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_b6f2d8e46cdd5f05bb06f52cd1b26fb2_v2_3_7_6', json_data)

    def gets_border_device_detail(self,
                                  device_management_ip_address,
                                  headers=None,
                                  **request_parameters):
        """Get border device detail from SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
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

        e_url = ('/dna/intent/api/v1/business/sda/border-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_aae881ff75d5488a5325ea949be4c5b_v2_3_7_6', json_data)

    def deletes_border_device(self,
                              device_management_ip_address,
                              headers=None,
                              **request_parameters):
        """Delete border device from SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
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

        e_url = ('/dna/intent/api/v1/business/sda/border-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a102ba155e35f84b7af3396aa407d02_v2_3_7_6', json_data)

    def delete_control_plane_device(self,
                                    device_management_ip_address,
                                    headers=None,
                                    **request_parameters):
        """Delete control plane device in SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
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

        e_url = ('/dna/intent/api/v1/business/sda/control-plane-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c05702ed7075a2f9ab14c051f1ac883_v2_3_7_6', json_data)

    def get_control_plane_device(self,
                                 device_management_ip_address,
                                 headers=None,
                                 **request_parameters):
        """Get control plane device from SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
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

        e_url = ('/dna/intent/api/v1/business/sda/control-plane-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c1a89e4a8ff15608bc6c10d7ef7389d7_v2_3_7_6', json_data)

    def add_control_plane_device(self,
                                 deviceManagementIpAddress=None,
                                 routeDistributionProtocol=None,
                                 siteNameHierarchy=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **request_parameters):
        """Add control plane device in SDA Fabric .

        Args:
            deviceManagementIpAddress(string): SDA's Management Ip Address of the Device which is provisioned
                successfully .
            routeDistributionProtocol(string): SDA's Route Distribution Protocol for Control Plane Device. Allowed
                values are "LISP_BGP" or "LISP_PUB_SUB". Default value is "LISP_BGP" .
            siteNameHierarchy(string): SDA's siteNameHierarchy of the Provisioned Device(site should be part of
                Fabric Site) .
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
            'deviceManagementIpAddress':
                deviceManagementIpAddress,
            'siteNameHierarchy':
                siteNameHierarchy,
            'routeDistributionProtocol':
                routeDistributionProtocol,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_ae7f02a3d051f2baf7cc087990d658_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/control-plane-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_ae7f02a3d051f2baf7cc087990d658_v2_3_7_6', json_data)

    def get_device_info(self,
                        device_management_ip_address,
                        headers=None,
                        **request_parameters):
        """Get device info from SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
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

        e_url = ('/dna/intent/api/v1/business/sda/device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d12790f461c553a08142ec740db5efbf_v2_3_7_6', json_data)

    def get_device_role_in_sda_fabric(self,
                                      device_management_ip_address,
                                      headers=None,
                                      **request_parameters):
        """Get device role in SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter. Device Management
                IP Address .
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
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

        e_url = ('/dna/intent/api/v1/business/sda/device/role')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea24b22ce355a229b7fd067401ddf3a_v2_3_7_6', json_data)

    def add_edge_device(self,
                        deviceManagementIpAddress=None,
                        siteNameHierarchy=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Add edge device in SDA Fabric .

        Args:
            deviceManagementIpAddress(string): SDA's Management Ip Address of the Device which is provisioned
                successfully .
            siteNameHierarchy(string): SDA's siteNameHierarchy of the Provisioned Device(site should be part of
                Fabric Site) .
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
            'deviceManagementIpAddress':
                deviceManagementIpAddress,
            'siteNameHierarchy':
                siteNameHierarchy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e0c7b28d55c85d49a84c1403ca14bd5f_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/edge-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e0c7b28d55c85d49a84c1403ca14bd5f_v2_3_7_6', json_data)

    def delete_edge_device(self,
                           device_management_ip_address,
                           headers=None,
                           **request_parameters):
        """Delete edge device from SDA Fabric. .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
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

        e_url = ('/dna/intent/api/v1/business/sda/edge-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b70d8c6f85254a053ab281fd9e8fc_v2_3_7_6', json_data)

    def get_edge_device(self,
                        device_management_ip_address,
                        headers=None,
                        **request_parameters):
        """Get edge device from SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
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

        e_url = ('/dna/intent/api/v1/business/sda/edge-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a2ee396d6595001acfbbcdfa25093ff_v2_3_7_6', json_data)

    def get_site(self,
                 site_name_hierarchy,
                 headers=None,
                 **request_parameters):
        """Get Site info from SDA Fabric .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter. Site Name Hierarchy .
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
        check_type(site_name_hierarchy, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteNameHierarchy':
                site_name_hierarchy,
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

        e_url = ('/dna/intent/api/v1/business/sda/fabric-site')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d23f3e54f8c59caac3ca905f7bf543a_v2_3_7_6', json_data)

    def delete_site(self,
                    site_name_hierarchy,
                    headers=None,
                    **request_parameters):
        """Delete Site from SDA Fabric .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter. Site Name Hierarchy .
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
        check_type(site_name_hierarchy, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteNameHierarchy':
                site_name_hierarchy,
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

        e_url = ('/dna/intent/api/v1/business/sda/fabric-site')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f9db3b115f0b8c8b3ce14bc5f975_v2_3_7_6', json_data)

    def add_site(self,
                 fabricName=None,
                 fabricType=None,
                 siteNameHierarchy=None,
                 headers=None,
                 payload=None,
                 active_validation=True,
                 **request_parameters):
        """Add Site in SDA Fabric .

        Args:
            fabricName(string): SDA's Warning Starting DNA Center 2.2.3.5 release, this field has been deprecated.
                SD-Access Fabric does not need it anymore.  It will be removed in future DNA Center
                releases. .
            fabricType(string): SDA's Type of SD-Access Fabric. Allowed values are "FABRIC_SITE" or "FABRIC_ZONE".
                Default value is "FABRIC_SITE". .
            siteNameHierarchy(string): SDA's Existing site name hierarchy available at global level. For Example
                "Global/Chicago/Building21/Floor1" .
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
            'fabricName':
                fabricName,
            'siteNameHierarchy':
                siteNameHierarchy,
            'fabricType':
                fabricType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a764c85d8df5c30b9143619d4f9cde9_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/fabric-site')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a764c85d8df5c30b9143619d4f9cde9_v2_3_7_6', json_data)

    def add_port_assignment_for_access_point(self,
                                             authenticateTemplateName=None,
                                             dataIpAddressPoolName=None,
                                             deviceManagementIpAddress=None,
                                             interfaceDescription=None,
                                             interfaceName=None,
                                             siteNameHierarchy=None,
                                             headers=None,
                                             payload=None,
                                             active_validation=True,
                                             **request_parameters):
        """Add Port assignment for access point in SDA Fabric .

        Args:
            authenticateTemplateName(string): SDA's Authenticate TemplateName associated to Fabric Site . Available
                values are 'No Authentication', 'Open Authentication', 'Closed Authentication ' and 'Low
                Impact '.
            dataIpAddressPoolName(string): SDA's Ip Pool Name, that is assigned to INFRA_VN   .
            deviceManagementIpAddress(string): SDA's Management Ip Address of the edge device  .
            interfaceDescription(string): SDA's Details or note of interface port assignment .
            interfaceName(string): SDA's Interface Name of the edge device  .
            siteNameHierarchy(string): SDA's Path of sda Fabric Site .
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
            'siteNameHierarchy':
                siteNameHierarchy,
            'deviceManagementIpAddress':
                deviceManagementIpAddress,
            'interfaceName':
                interfaceName,
            'dataIpAddressPoolName':
                dataIpAddressPoolName,
            'authenticateTemplateName':
                authenticateTemplateName,
            'interfaceDescription':
                interfaceDescription,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e4a09bf566f35babad9e27f5eb61a86d_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/hostonboarding/access-'
                 + 'point')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e4a09bf566f35babad9e27f5eb61a86d_v2_3_7_6', json_data)

    def delete_port_assignment_for_access_point(self,
                                                device_management_ip_address,
                                                interface_name,
                                                headers=None,
                                                **request_parameters):
        """Delete Port assignment for access point in SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
            interface_name(str): interfaceName query parameter.
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        check_type(interface_name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
            'interfaceName':
                interface_name,
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

        e_url = ('/dna/intent/api/v1/business/sda/hostonboarding/access-'
                 + 'point')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bd26b08b64545bae20f60c56891576_v2_3_7_6', json_data)

    def get_port_assignment_for_access_point(self,
                                             device_management_ip_address,
                                             interface_name,
                                             headers=None,
                                             **request_parameters):
        """Get Port assignment for access point in SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
            interface_name(str): interfaceName query parameter.
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        check_type(interface_name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
            'interfaceName':
                interface_name,
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

        e_url = ('/dna/intent/api/v1/business/sda/hostonboarding/access-'
                 + 'point')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b035b0b3b60b5f2bb7c8c82e7f94b63b_v2_3_7_6', json_data)

    def delete_port_assignment_for_user_device(self,
                                               device_management_ip_address,
                                               interface_name,
                                               headers=None,
                                               **request_parameters):
        """Delete Port assignment for user device in SDA Fabric. .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
            interface_name(str): interfaceName query parameter.
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        check_type(interface_name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
            'interfaceName':
                interface_name,
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

        e_url = ('/dna/intent/api/v1/business/sda/hostonboarding/user-'
                 + 'device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cb88b50dd5ead96ecfb4ab0390f47_v2_3_7_6', json_data)

    def add_port_assignment_for_user_device(self,
                                            authenticateTemplateName=None,
                                            dataIpAddressPoolName=None,
                                            deviceManagementIpAddress=None,
                                            interfaceDescription=None,
                                            interfaceName=None,
                                            interfaceNames=None,
                                            scalableGroupName=None,
                                            siteNameHierarchy=None,
                                            voiceIpAddressPoolName=None,
                                            headers=None,
                                            payload=None,
                                            active_validation=True,
                                            **request_parameters):
        """Add Port assignment for user device in SDA Fabric. .

        Args:
            authenticateTemplateName(string): SDA's Authenticate TemplateName associated with siteNameHierarchy .
                Available values are 'Open Authentication', 'Closed Authentication', 'Low Impact' and
                'No Authentication'.
            dataIpAddressPoolName(string): SDA's Ip Pool Name, that is assigned to virtual network with traffic type
                as DATA(can't be empty if voiceIpAddressPoolName is empty) .
            deviceManagementIpAddress(string): SDA's Management Ip Address of the Edge Node Device. .
            interfaceDescription(string): SDA's User defined text message for port assignment .
            interfaceName(string): SDA's Interface Name on the Edge Node Device. .
            interfaceNames(list): SDA's List of Interface Names on the Edge Node Device.
                E.g.["GigabitEthernet1/0/3","GigabitEthernet1/0/4"]   (list of strings).
            scalableGroupName(string): SDA's Scalable Group name associated with VN .
            siteNameHierarchy(string): SDA's Complete Path of SD-Access Fabric Site. .
            voiceIpAddressPoolName(string): SDA's Ip Pool Name, that is assigned to virtual network with traffic
                type as VOICE(can't be empty if dataIpAddressPoolName is empty) .
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
            'siteNameHierarchy':
                siteNameHierarchy,
            'deviceManagementIpAddress':
                deviceManagementIpAddress,
            'interfaceName':
                interfaceName,
            'interfaceNames':
                interfaceNames,
            'dataIpAddressPoolName':
                dataIpAddressPoolName,
            'voiceIpAddressPoolName':
                voiceIpAddressPoolName,
            'authenticateTemplateName':
                authenticateTemplateName,
            'scalableGroupName':
                scalableGroupName,
            'interfaceDescription':
                interfaceDescription,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_af29516f0c8591da2a92523b5ab3386_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/hostonboarding/user-'
                 + 'device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_af29516f0c8591da2a92523b5ab3386_v2_3_7_6', json_data)

    def get_port_assignment_for_user_device(self,
                                            device_management_ip_address,
                                            interface_name,
                                            headers=None,
                                            **request_parameters):
        """Get Port assignment for user device in SDA Fabric. .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
            interface_name(str): interfaceName query parameter.
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        check_type(interface_name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
            'interfaceName':
                interface_name,
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

        e_url = ('/dna/intent/api/v1/business/sda/hostonboarding/user-'
                 + 'device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a446d7327733580e9a6b661715eb4c09_v2_3_7_6', json_data)

    def add_multicast_in_sda_fabric(self,
                                    multicastMethod=None,
                                    multicastType=None,
                                    multicastVnInfo=None,
                                    siteNameHierarchy=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **request_parameters):
        """Add multicast in SDA fabric .

        Args:
            multicastMethod(string): SDA's Multicast Method . Available values are 'native_multicast'.
            multicastType(string): SDA's Multicast Type . Available values are 'ssm', 'asm_with_internal_rp' and
                'asm_with_external_rp'.
            multicastVnInfo(list): SDA's multicastVnInfo (list of objects).
            siteNameHierarchy(string): SDA's Full path of sda Fabric Site .
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
            'siteNameHierarchy':
                siteNameHierarchy,
            'multicastMethod':
                multicastMethod,
            'multicastType':
                multicastType,
            'multicastVnInfo':
                multicastVnInfo,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_b7079a38844e56dd8f1b6b876880a02e_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/multicast')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_b7079a38844e56dd8f1b6b876880a02e_v2_3_7_6', json_data)

    def get_multicast_details_from_sda_fabric(self,
                                              site_name_hierarchy,
                                              headers=None,
                                              **request_parameters):
        """Get multicast details from SDA fabric .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter. fabric site name hierarchy .
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
        check_type(site_name_hierarchy, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteNameHierarchy':
                site_name_hierarchy,
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

        e_url = ('/dna/intent/api/v1/business/sda/multicast')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c27bbb42365955bc210924e1362c34_v2_3_7_6', json_data)

    def delete_multicast_from_sda_fabric(self,
                                         site_name_hierarchy,
                                         headers=None,
                                         **request_parameters):
        """Delete multicast from SDA fabric .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter.
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
        check_type(site_name_hierarchy, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteNameHierarchy':
                site_name_hierarchy,
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

        e_url = ('/dna/intent/api/v1/business/sda/multicast')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e8e007d3e25f7fb83a6579016aea72_v2_3_7_6', json_data)

    def delete_provisioned_wired_device(self,
                                        device_management_ip_address,
                                        headers=None,
                                        **request_parameters):
        """Delete provisioned Wired Device .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter. Valid IP address of
                the device currently provisioned in a fabric site .
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
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

        e_url = ('/dna/intent/api/v1/business/sda/provision-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e5bd8dbbf65253f0aadd77a62b1b8b58_v2_3_7_6', json_data)

    def re_provision_wired_device(self,
                                  deviceManagementIpAddress=None,
                                  siteNameHierarchy=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Re-Provision Wired Device .

        Args:
            deviceManagementIpAddress(string): SDA's Management Ip Address of the device to be re-provisioned .
            siteNameHierarchy(string): SDA's siteNameHierarchy of the provisioned device .
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
            'deviceManagementIpAddress':
                deviceManagementIpAddress,
            'siteNameHierarchy':
                siteNameHierarchy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_fd488ff002115f3b8f0ee165e5347609_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/provision-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_fd488ff002115f3b8f0ee165e5347609_v2_3_7_6', json_data)

    def provision_wired_device(self,
                               deviceManagementIpAddress=None,
                               siteNameHierarchy=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Provision Wired Device .

        Args:
            deviceManagementIpAddress(string): SDA's Management Ip Address of the device to be provisioned .
            siteNameHierarchy(string): SDA's Site Name Hierarchy for device location(only building / floor level)  .
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
            'deviceManagementIpAddress':
                deviceManagementIpAddress,
            'siteNameHierarchy':
                siteNameHierarchy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d1608b2751c883a072ee3fb80228_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/provision-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d1608b2751c883a072ee3fb80228_v2_3_7_6', json_data)

    def get_provisioned_wired_device(self,
                                     device_management_ip_address,
                                     headers=None,
                                     **request_parameters):
        """Get Provisioned Wired Device .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
        check_type(device_management_ip_address, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceManagementIpAddress':
                device_management_ip_address,
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

        e_url = ('/dna/intent/api/v1/business/sda/provision-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d8f10868c21856eab31776f109aba2bb_v2_3_7_6', json_data)

    def delete_transit_peer_network(self,
                                    transit_peer_network_name,
                                    headers=None,
                                    **request_parameters):
        """Delete Transit Peer Network from SD-Access .

        Args:
            transit_peer_network_name(str): transitPeerNetworkName query parameter. Transit Peer Network Name
                .
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
        check_type(transit_peer_network_name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'transitPeerNetworkName':
                transit_peer_network_name,
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

        e_url = ('/dna/intent/api/v1/business/sda/transit-peer-network')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a34aab91750028f4d584d36811844_v2_3_7_6', json_data)

    def get_transit_peer_network_info(self,
                                      transit_peer_network_name,
                                      headers=None,
                                      **request_parameters):
        """Get Transit Peer Network Info from SD-Access .

        Args:
            transit_peer_network_name(str): transitPeerNetworkName query parameter. Transit or Peer Network
                Name .
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
        check_type(transit_peer_network_name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'transitPeerNetworkName':
                transit_peer_network_name,
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

        e_url = ('/dna/intent/api/v1/business/sda/transit-peer-network')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d39e10793a45d3db229d6d3820c665a_v2_3_7_6', json_data)

    def add_transit_peer_network(self,
                                 ipTransitSettings=None,
                                 sdaTransitSettings=None,
                                 transitPeerNetworkName=None,
                                 transitPeerNetworkType=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **request_parameters):
        """Add Transit Peer Network in SD-Access .

        Args:
            ipTransitSettings(object): SDA's ipTransitSettings.
            sdaTransitSettings(object): SDA's sdaTransitSettings.
            transitPeerNetworkName(string): SDA's Transit Peer Network Name .
            transitPeerNetworkType(string): SDA's Transit Peer Network Type . Available values are 'ip_transit',
                'sda_transit_with_lisp_bgp' and 'sda_transit_with_pub_sub'.
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
            'transitPeerNetworkName':
                transitPeerNetworkName,
            'transitPeerNetworkType':
                transitPeerNetworkType,
            'ipTransitSettings':
                ipTransitSettings,
            'sdaTransitSettings':
                sdaTransitSettings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d7073129453698264e7519d82991c_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/transit-peer-network')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d7073129453698264e7519d82991c_v2_3_7_6', json_data)

    def delete_vn(self,
                  site_name_hierarchy,
                  virtual_network_name,
                  headers=None,
                  **request_parameters):
        """Delete virtual network (VN) from SDA Fabric   .

        Args:
            virtual_network_name(str): virtualNetworkName query parameter.
            site_name_hierarchy(str): siteNameHierarchy query parameter.
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
        check_type(virtual_network_name, str,
                   may_be_none=False)
        check_type(site_name_hierarchy, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'virtualNetworkName':
                virtual_network_name,
            'siteNameHierarchy':
                site_name_hierarchy,
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

        e_url = ('/dna/intent/api/v1/business/sda/virtual-network')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cb9f8ad5359b2b2cbc151ac3a842a_v2_3_7_6', json_data)

    def get_vn(self,
               site_name_hierarchy,
               virtual_network_name,
               headers=None,
               **request_parameters):
        """Get virtual network (VN) from SDA Fabric .

        Args:
            virtual_network_name(str): virtualNetworkName query parameter.
            site_name_hierarchy(str): siteNameHierarchy query parameter.
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
        check_type(virtual_network_name, str,
                   may_be_none=False)
        check_type(site_name_hierarchy, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'virtualNetworkName':
                virtual_network_name,
            'siteNameHierarchy':
                site_name_hierarchy,
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

        e_url = ('/dna/intent/api/v1/business/sda/virtual-network')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cb1fe08692b85767a42b84340c4c7d53_v2_3_7_6', json_data)

    def add_vn(self,
               siteNameHierarchy=None,
               virtualNetworkName=None,
               headers=None,
               payload=None,
               active_validation=True,
               **request_parameters):
        """Add virtual network (VN) in SDA Fabric   .

        Args:
            siteNameHierarchy(string): SDA's Path of sda Fabric Site .
            virtualNetworkName(string): SDA's Virtual Network Name, that is created at Global level .
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
            'virtualNetworkName':
                virtualNetworkName,
            'siteNameHierarchy':
                siteNameHierarchy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e3a724a35854758d65a83823c88435_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/virtual-network')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e3a724a35854758d65a83823c88435_v2_3_7_6', json_data)

    def get_virtual_network_summary(self,
                                    site_name_hierarchy,
                                    headers=None,
                                    **request_parameters):
        """Get Virtual Network Summary .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter. Complete fabric siteNameHierarchy
                Path .
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
        check_type(site_name_hierarchy, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteNameHierarchy':
                site_name_hierarchy,
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

        e_url = ('/dna/intent/api/v1/business/sda/virtual-network/summary')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ccf5ce99e049525f8184fcaa5991d919_v2_3_7_6', json_data)

    def get_ip_pool_from_sda_virtual_network(self,
                                             ip_pool_name,
                                             site_name_hierarchy,
                                             virtual_network_name,
                                             headers=None,
                                             **request_parameters):
        """Get IP Pool from SDA Virtual Network .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter.
            virtual_network_name(str): virtualNetworkName query parameter.
            ip_pool_name(str): ipPoolName query parameter. ipPoolName. Note: Use vlanName as a value for this
                parameter if same ip pool is assigned to multiple virtual networks (e.g..
                ipPoolName=vlan1021) .
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
        check_type(site_name_hierarchy, str,
                   may_be_none=False)
        check_type(virtual_network_name, str,
                   may_be_none=False)
        check_type(ip_pool_name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteNameHierarchy':
                site_name_hierarchy,
            'virtualNetworkName':
                virtual_network_name,
            'ipPoolName':
                ip_pool_name,
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

        e_url = ('/dna/intent/api/v1/business/sda/virtualnetwork/ippool')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b88723912610599ba42292db52d1dae4_v2_3_7_6', json_data)

    def delete_ip_pool_from_sda_virtual_network(self,
                                                ip_pool_name,
                                                site_name_hierarchy,
                                                virtual_network_name,
                                                headers=None,
                                                **request_parameters):
        """Delete IP Pool from SDA Virtual Network .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter.
            virtual_network_name(str): virtualNetworkName query parameter.
            ip_pool_name(str): ipPoolName query parameter.
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
        check_type(site_name_hierarchy, str,
                   may_be_none=False)
        check_type(virtual_network_name, str,
                   may_be_none=False)
        check_type(ip_pool_name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteNameHierarchy':
                site_name_hierarchy,
            'virtualNetworkName':
                virtual_network_name,
            'ipPoolName':
                ip_pool_name,
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

        e_url = ('/dna/intent/api/v1/business/sda/virtualnetwork/ippool')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c923d016d5401b7a9943724df3844_v2_3_7_6', json_data)

    def add_ip_pool_in_sda_virtual_network(self,
                                           autoGenerateVlanName=None,
                                           ipPoolName=None,
                                           isBridgeModeVm=None,
                                           isCommonPool=None,
                                           isIpDirectedBroadcast=None,
                                           isL2FloodingEnabled=None,
                                           isLayer2Only=None,
                                           isThisCriticalPool=None,
                                           isWirelessPool=None,
                                           poolType=None,
                                           scalableGroupName=None,
                                           siteNameHierarchy=None,
                                           trafficType=None,
                                           virtualNetworkName=None,
                                           vlanId=None,
                                           vlanName=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **request_parameters):
        """Add IP Pool in SDA Virtual Network .

        Args:
            autoGenerateVlanName(boolean): SDA's It will auto generate vlanName, if vlanName is empty(applicable for
                L3  and INFRA_VN) .
            ipPoolName(string): SDA's Ip Pool Name, that is reserved to Fabric Site (Required for L3 and INFRA_VN) .
            isBridgeModeVm(boolean): SDA's Bridge Mode Vm enablement flag (applicable for L3 and L2 and default
                value is False ) .
            isCommonPool(boolean): SDA's Common Pool enablement flag(applicable for L3 and L2 and default value is
                False ) .
            isIpDirectedBroadcast(boolean): SDA's Ip Directed Broadcast enablement flag(applicable for L3 and
                default value is False ) .
            isL2FloodingEnabled(boolean): SDA's Layer2 flooding enablement flag(applicable for L3 , L2 and always
                true for L2 and default value is False ) .
            isLayer2Only(boolean): SDA's Layer2 Only enablement flag and default value is False  .
            isThisCriticalPool(boolean): SDA's Critical pool enablement flag(applicable for L3 and default value is
                False ) .
            isWirelessPool(boolean): SDA's Wireless Pool enablement flag(applicable for L3  and L2 and default value
                is False ) .
            poolType(string): SDA's Pool Type (applicable for INFRA_VN) . Available values are 'AP' and 'Extended'.
            scalableGroupName(string): SDA's Scalable Group Name(applicable for L3) .
            siteNameHierarchy(string): SDA's Path of sda Fabric Site .
            trafficType(string): SDA's Traffic type(applicable for L3  and L2) . Available values are 'Data' and
                'Voice'.
            virtualNetworkName(string): SDA's Virtual Network Name, that is associated to Fabric Site .
            vlanId(string): SDA's vlan Id(applicable for L3 , L2 and  INFRA_VN) .
            vlanName(string): SDA's Vlan name represent the segment name, if empty, vlanName would be auto generated
                by API .
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
            'siteNameHierarchy':
                siteNameHierarchy,
            'virtualNetworkName':
                virtualNetworkName,
            'isLayer2Only':
                isLayer2Only,
            'ipPoolName':
                ipPoolName,
            'vlanId':
                vlanId,
            'vlanName':
                vlanName,
            'autoGenerateVlanName':
                autoGenerateVlanName,
            'trafficType':
                trafficType,
            'scalableGroupName':
                scalableGroupName,
            'isL2FloodingEnabled':
                isL2FloodingEnabled,
            'isThisCriticalPool':
                isThisCriticalPool,
            'isWirelessPool':
                isWirelessPool,
            'isIpDirectedBroadcast':
                isIpDirectedBroadcast,
            'isCommonPool':
                isCommonPool,
            'isBridgeModeVm':
                isBridgeModeVm,
            'poolType':
                poolType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_b07f187b7456c8bbb6088a2f24dcee_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/virtualnetwork/ippool')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_b07f187b7456c8bbb6088a2f24dcee_v2_3_7_6', json_data)

    def update_anycast_gateways(self,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **request_parameters):
        """Updates anycast gateways based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_f486694f3da57b4921b7f2036a1b754_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/anycastGateways')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_f486694f3da57b4921b7f2036a1b754_v2_3_7_6', json_data)

    def add_anycast_gateways(self,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **request_parameters):
        """Adds anycast gateways based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_ee8590b6b45048b84e814161272bee_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/anycastGateways')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_ee8590b6b45048b84e814161272bee_v2_3_7_6', json_data)

    def get_anycast_gateways(self,
                             fabric_id=None,
                             id=None,
                             ip_pool_name=None,
                             limit=None,
                             offset=None,
                             virtual_network_name=None,
                             vlan_id=None,
                             vlan_name=None,
                             headers=None,
                             **request_parameters):
        """Returns a list of anycast gateways that match the provided query parameters. .

        Args:
            id(str): id query parameter. ID of the anycast gateway to search for in the database. .
            fabric_id(str): fabricId query parameter. Get anycast gateways within this fabric. .
            virtual_network_name(str): virtualNetworkName query parameter. Get anycast gateways associated
                with this virtual network. .
            ip_pool_name(str): ipPoolName query parameter. Get anycast gateways associated with this IP pool.
                .
            vlan_name(str): vlanName query parameter. Get anycast gateways associated with this VLAN name. .
            vlan_id(int): vlanId query parameter. Get anycast gateways associated with this VLAN ID. .
            offset(int,str): offset query parameter. Starting record for pagination. .
            limit(int,str): limit query parameter. Maximum number of records to return. .
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
        check_type(id, str)
        check_type(fabric_id, str)
        check_type(virtual_network_name, str)
        check_type(ip_pool_name, str)
        check_type(vlan_name, str)
        check_type(vlan_id, int)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'id':
                id,
            'fabricId':
                fabric_id,
            'virtualNetworkName':
                virtual_network_name,
            'ipPoolName':
                ip_pool_name,
            'vlanName':
                vlan_name,
            'vlanId':
                vlan_id,
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

        e_url = ('/dna/intent/api/v1/sda/anycastGateways')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c634a503551e885c053fd1ed9d3fd_v2_3_7_6', json_data)

    def get_anycast_gateway_count(self,
                                  fabric_id=None,
                                  ip_pool_name=None,
                                  virtual_network_name=None,
                                  vlan_id=None,
                                  vlan_name=None,
                                  headers=None,
                                  **request_parameters):
        """Returns the count of anycast gateways that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. Only count anycast gateways within this fabric. .
            virtual_network_name(str): virtualNetworkName query parameter. Only count anycast gateways
                associated with this virtual network. .
            ip_pool_name(str): ipPoolName query parameter. Only count anycast gateways associated with this
                IP pool. .
            vlan_name(str): vlanName query parameter. Only count anycast gateways associated with this VLAN
                name. .
            vlan_id(int): vlanId query parameter. Only count anycast gateways associated with this VLAN ID. .
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
        check_type(fabric_id, str)
        check_type(virtual_network_name, str)
        check_type(ip_pool_name, str)
        check_type(vlan_name, str)
        check_type(vlan_id, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'virtualNetworkName':
                virtual_network_name,
            'ipPoolName':
                ip_pool_name,
            'vlanName':
                vlan_name,
            'vlanId':
                vlan_id,
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

        e_url = ('/dna/intent/api/v1/sda/anycastGateways/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a280b785a3ca53c349c68ca9070_v2_3_7_6', json_data)

    def delete_anycast_gateway_by_id(self,
                                     id,
                                     headers=None,
                                     **request_parameters):
        """Deletes an anycast gateway based on id. .

        Args:
            id(str): id path parameter. ID of the anycast gateway to be deleted. .
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

        e_url = ('/dna/intent/api/v1/sda/anycastGateways/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e66d9fbfe55cf5882bf219b0fffa13_v2_3_7_6', json_data)

    def get_authentication_profiles(self,
                                    authentication_profile_name=None,
                                    fabric_id=None,
                                    headers=None,
                                    **request_parameters):
        """Returns a list of authentication profiles that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric whose authentication profiles are to
                be returned. .
            authentication_profile_name(str): authenticationProfileName query parameter. Return only the
                authentication profiles with this specified name. Note that 'No Authentication' is not a
                valid option for this parameter. .
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
        check_type(fabric_id, str)
        check_type(authentication_profile_name, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'authenticationProfileName':
                authentication_profile_name,
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

        e_url = ('/dna/intent/api/v1/sda/authenticationProfiles')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e6713a34508993b3e9f6837dd690_v2_3_7_6', json_data)

    def update_authentication_profile(self,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **request_parameters):
        """Updates an authentication profile based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_ea8d75a9d8d9e6882da4a4a91_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/authenticationProfiles')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_ea8d75a9d8d9e6882da4a4a91_v2_3_7_6', json_data)

    def update_extranet_policy(self,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Updates an extranet policy based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_ccd75f80ece59f08cadda085402cef5_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/extranetPolicies')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_ccd75f80ece59f08cadda085402cef5_v2_3_7_6', json_data)

    def add_extranet_policy(self,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **request_parameters):
        """Adds an extranet policy based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_a0c237c8fc115b6f98b87cc7a1360dd0_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/extranetPolicies')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a0c237c8fc115b6f98b87cc7a1360dd0_v2_3_7_6', json_data)

    def get_extranet_policies(self,
                              extranet_policy_name=None,
                              limit=None,
                              offset=None,
                              headers=None,
                              **request_parameters):
        """Returns a list of extranet policies that match the provided query parameters. .

        Args:
            extranet_policy_name(str): extranetPolicyName query parameter. Name of the extranet policy. .
            offset(int,str): offset query parameter. Starting record for pagination. .
            limit(int,str): limit query parameter. Maximum number of records to return. .
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
        check_type(extranet_policy_name, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'extranetPolicyName':
                extranet_policy_name,
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

        e_url = ('/dna/intent/api/v1/sda/extranetPolicies')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c88d4f7170b9553abf9af4d011a25f0f_v2_3_7_6', json_data)

    def get_extranet_policy_count(self,
                                  headers=None,
                                  **request_parameters):
        """Returns the count of extranet policies that match the provided query parameters. .

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

        e_url = ('/dna/intent/api/v1/sda/extranetPolicies/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dd8262eb13145dc292e7aee84e56e065_v2_3_7_6', json_data)

    def delete_extranet_policy_by_id(self,
                                     id,
                                     headers=None,
                                     **request_parameters):
        """Deletes an extranet policy based on id. .

        Args:
            id(str): id path parameter. ID of the extranet policy. .
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

        e_url = ('/dna/intent/api/v1/sda/extranetPolicies/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_aeee667e2d567cbbff106e1888bbbe_v2_3_7_6', json_data)

    def get_fabric_devices(self,
                           fabric_id,
                           device_roles=None,
                           limit=None,
                           network_device_id=None,
                           offset=None,
                           headers=None,
                           **request_parameters):
        """Returns a list of fabric devices that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device.
                .
            device_roles(str): deviceRoles query parameter. Device roles of the fabric device. .
            offset(int,str): offset query parameter. Starting record for pagination. .
            limit(int,str): limit query parameter. Maximum number of records to return. .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str)
        check_type(device_roles, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
            'deviceRoles':
                device_roles,
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d5486968c9ff5b23ae1fdd15ad6da1ef_v2_3_7_6', json_data)

    def update_fabric_devices(self,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **request_parameters):
        """Updates fabric devices based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_a924f763a15125a8d5beaa6dd6fa2c_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabricDevices')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_a924f763a15125a8d5beaa6dd6fa2c_v2_3_7_6', json_data)

    def delete_fabric_devices(self,
                              fabric_id,
                              device_roles=None,
                              network_device_id=None,
                              headers=None,
                              **request_parameters):
        """Deletes fabric devices based on user input. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device.
                .
            device_roles(str): deviceRoles query parameter. Device roles of the fabric device. .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str)
        check_type(device_roles, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
            'deviceRoles':
                device_roles,
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c5d22b295a4c8e4a1dfdb4645f92_v2_3_7_6', json_data)

    def add_fabric_devices(self,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """Adds fabric devices based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_d77719c37558f694e5545a21406275_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabricDevices')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d77719c37558f694e5545a21406275_v2_3_7_6', json_data)

    def get_fabric_devices_count(self,
                                 fabric_id,
                                 device_roles=None,
                                 network_device_id=None,
                                 headers=None,
                                 **request_parameters):
        """Returns the count of fabric devices that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device.
                .
            device_roles(str): deviceRoles query parameter. Device roles of the fabric device. .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str)
        check_type(device_roles, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
            'deviceRoles':
                device_roles,
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f081250cdc75361afea8d1624123bb4_v2_3_7_6', json_data)

    def delete_fabric_device_layer2_handoffs(self,
                                             fabric_id,
                                             network_device_id,
                                             headers=None,
                                             **request_parameters):
        """Deletes layer 2 handoffs of a fabric device based on user input. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device.
                .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b6484275a25c54488d300c11c5ddd481_v2_3_7_6', json_data)

    def get_fabric_devices_layer2_handoffs(self,
                                           fabric_id,
                                           limit=None,
                                           network_device_id=None,
                                           offset=None,
                                           headers=None,
                                           **request_parameters):
        """Returns a list of layer 2 handoffs of fabric devices that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device.
                .
            offset(int,str): offset query parameter. Starting record for pagination. .
            limit(int,str): limit query parameter. Maximum number of records to return. .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ec047337e36b59db977e1dae8dd724ef_v2_3_7_6', json_data)

    def add_fabric_devices_layer2_handoffs(self,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **request_parameters):
        """Adds layer 2 handoffs in fabric devices based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_e86b65311b05d29ba5eea0d5f1fd88f_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e86b65311b05d29ba5eea0d5f1fd88f_v2_3_7_6', json_data)

    def get_fabric_devices_layer2_handoffs_count(self,
                                                 fabric_id,
                                                 network_device_id=None,
                                                 headers=None,
                                                 **request_parameters):
        """Returns the count of layer 2 handoffs of fabric devices that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device.
                .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs/coun'
                 + 't')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c6da6b1da95bb691d2e39cee84dbb2_v2_3_7_6', json_data)

    def delete_fabric_device_layer2_handoff_by_id(self,
                                                  id,
                                                  headers=None,
                                                  **request_parameters):
        """Deletes a layer 2 handoff of a fabric device based on id. .

        Args:
            id(str): id path parameter. ID of the layer 2 handoff of a fabric device. .
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b6406a55509e5aeaa71d960f98_v2_3_7_6', json_data)

    def add_fabric_devices_layer3_handoffs_with_ip_transit(self,
                                                           headers=None,
                                                           payload=None,
                                                           active_validation=True,
                                                           **request_parameters):
        """Adds layer 3 handoffs with ip transit in fabric devices based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_c45c1c55d498d03a72933690098_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTr'
                 + 'ansits')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_c45c1c55d498d03a72933690098_v2_3_7_6', json_data)

    def update_fabric_devices_layer3_handoffs_with_ip_transit(self,
                                                              headers=None,
                                                              payload=None,
                                                              active_validation=True,
                                                              **request_parameters):
        """Updates layer 3 handoffs with ip transit of fabric devices based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_f0942fbb79f855e889d60777f41ea944_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTr'
                 + 'ansits')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_f0942fbb79f855e889d60777f41ea944_v2_3_7_6', json_data)

    def delete_fabric_device_layer3_handoffs_with_ip_transit(self,
                                                             fabric_id,
                                                             network_device_id,
                                                             headers=None,
                                                             **request_parameters):
        """Deletes layer 3 handoffs with ip transit of a fabric device based on user input. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device.
                .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTr'
                 + 'ansits')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fdab9b7917a1567980b0071e058921fe_v2_3_7_6', json_data)

    def get_fabric_devices_layer3_handoffs_with_ip_transit(self,
                                                           fabric_id,
                                                           limit=None,
                                                           network_device_id=None,
                                                           offset=None,
                                                           headers=None,
                                                           **request_parameters):
        """Returns a list of layer 3 handoffs with ip transit of fabric devices that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device.
                .
            offset(int,str): offset query parameter. Starting record for pagination. .
            limit(int,str): limit query parameter. Maximum number of records to return. .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTr'
                 + 'ansits')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ee0d11a1e0dd573da2d6fb96d92c4bb8_v2_3_7_6', json_data)

    def get_fabric_devices_layer3_handoffs_with_ip_transit_count(self,
                                                                 fabric_id,
                                                                 network_device_id=None,
                                                                 headers=None,
                                                                 **request_parameters):
        """Returns the count of layer 3 handoffs with ip transit of fabric devices that match the provided query
        parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device.
                .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTr'
                 + 'ansits/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a4fa61561aa0fe56939c3f24d4_v2_3_7_6', json_data)

    def delete_fabric_device_layer3_handoff_with_ip_transit_by_id(self,
                                                                  id,
                                                                  headers=None,
                                                                  **request_parameters):
        """Deletes a layer 3 handoff with ip transit of a fabric device by id. .

        Args:
            id(str): id path parameter. ID of the layer 3 handoff with ip transit of a fabric device to be
                deleted. .
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTr'
                 + 'ansits/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fafe4d2d2fe510db8f0906e5f583559_v2_3_7_6', json_data)

    def update_fabric_devices_layer3_handoffs_with_sda_transit(self,
                                                               headers=None,
                                                               payload=None,
                                                               active_validation=True,
                                                               **request_parameters):
        """Updates layer 3 handoffs with sda transit of fabric devices based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_c90c04b8356cf9974957e0f9516d0_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaT'
                 + 'ransits')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_c90c04b8356cf9974957e0f9516d0_v2_3_7_6', json_data)

    def get_fabric_devices_layer3_handoffs_with_sda_transit(self,
                                                            fabric_id,
                                                            limit=None,
                                                            network_device_id=None,
                                                            offset=None,
                                                            headers=None,
                                                            **request_parameters):
        """Returns a list of layer 3 handoffs with sda transit of fabric devices that match the provided query parameters.
        .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device.
                .
            offset(int,str): offset query parameter. Starting record for pagination. .
            limit(int,str): limit query parameter. Maximum number of records to return. .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaT'
                 + 'ransits')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d8e5a783df185c88bae2bd8ba6b6bb2d_v2_3_7_6', json_data)

    def delete_fabric_device_layer3_handoffs_with_sda_transit(self,
                                                              fabric_id,
                                                              network_device_id,
                                                              headers=None,
                                                              **request_parameters):
        """Deletes layer 3 handoffs with sda transit of a fabric device based on user input. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device.
                .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaT'
                 + 'ransits')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_aae870923852f3ac5904f65812c559_v2_3_7_6', json_data)

    def add_fabric_devices_layer3_handoffs_with_sda_transit(self,
                                                            headers=None,
                                                            payload=None,
                                                            active_validation=True,
                                                            **request_parameters):
        """Adds layer 3 handoffs with sda transit in fabric devices based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_f95014e3b3385f21afa39325f3508427_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaT'
                 + 'ransits')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f95014e3b3385f21afa39325f3508427_v2_3_7_6', json_data)

    def get_fabric_devices_layer3_handoffs_with_sda_transit_count(self,
                                                                  fabric_id,
                                                                  network_device_id=None,
                                                                  headers=None,
                                                                  **request_parameters):
        """Returns the count of layer 3 handoffs with sda transit of fabric devices that match the provided query
        parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device.
                .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaT'
                 + 'ransits/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b183d0cc487506ab776e0d470b0db91_v2_3_7_6', json_data)

    def delete_a_fabric_device_by_id(self,
                                     id,
                                     headers=None,
                                     **request_parameters):
        """Deletes a fabric device based on id. .

        Args:
            id(str): id path parameter. ID of the fabric device. .
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

        e_url = ('/dna/intent/api/v1/sda/fabricDevices/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d9e0c5eb356eda1fa6f45928cb6f2_v2_3_7_6', json_data)

    def get_fabric_sites(self,
                         id=None,
                         limit=None,
                         offset=None,
                         site_id=None,
                         headers=None,
                         **request_parameters):
        """Returns a list of fabric sites that match the provided query parameters. .

        Args:
            id(str): id query parameter. ID of the fabric site to search for in the database. .
            site_id(str): siteId query parameter. Get the fabric site associated with this network hierarchy.
                .
            offset(int,str): offset query parameter. Starting record for pagination. .
            limit(int,str): limit query parameter. Maximum number of records to return. .
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
        check_type(id, str)
        check_type(site_id, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'id':
                id,
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

        e_url = ('/dna/intent/api/v1/sda/fabricSites')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a7079f75dd5973b2bf50461bdcf2de_v2_3_7_6', json_data)

    def add_fabric_site(self,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Adds a fabric site based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_bfca373c5d7c863eef14abc654fd_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabricSites')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_bfca373c5d7c863eef14abc654fd_v2_3_7_6', json_data)

    def update_fabric_site(self,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """Updates a fabric site based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_effb55c158f28469762804e84633_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabricSites')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_effb55c158f28469762804e84633_v2_3_7_6', json_data)

    def get_fabric_site_count(self,
                              headers=None,
                              **request_parameters):
        """Returns the count of fabric sites that match the provided query parameters. .

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

        e_url = ('/dna/intent/api/v1/sda/fabricSites/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b871b97883085717bfbb14e860ab6654_v2_3_7_6', json_data)

    def delete_fabric_site_by_id(self,
                                 id,
                                 headers=None,
                                 **request_parameters):
        """Deletes a fabric site based on id. .

        Args:
            id(str): id path parameter. ID of the fabric site to be deleted. .
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

        e_url = ('/dna/intent/api/v1/sda/fabricSites/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c94ba483b75e03a2c23aae02c510ac_v2_3_7_6', json_data)

    def get_fabric_zones(self,
                         id=None,
                         limit=None,
                         offset=None,
                         site_id=None,
                         headers=None,
                         **request_parameters):
        """Returns a list of fabric zones that match the provided query parameters. .

        Args:
            id(str): id query parameter. ID of the fabric zone to search for in the database. .
            site_id(str): siteId query parameter. get the fabric zone associated with this network hierarchy.
                .
            offset(int,str): offset query parameter. Starting record for pagination. .
            limit(int,str): limit query parameter. Maximum number of records to return. .
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
        check_type(id, str)
        check_type(site_id, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'id':
                id,
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

        e_url = ('/dna/intent/api/v1/sda/fabricZones')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e722d98d14d5e119ca03fa114edb38f_v2_3_7_6', json_data)

    def update_fabric_zone(self,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """Updates a fabric zone based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_ada3522de8ef54729e9fc242df292547_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabricZones')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_ada3522de8ef54729e9fc242df292547_v2_3_7_6', json_data)

    def add_fabric_zone(self,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Adds a fabric zone based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_ae4d33eacca95f109bebc6fd0528ca48_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabricZones')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_ae4d33eacca95f109bebc6fd0528ca48_v2_3_7_6', json_data)

    def get_fabric_zone_count(self,
                              headers=None,
                              **request_parameters):
        """Returns the count of fabric zones that match the provided query parameters. .

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

        e_url = ('/dna/intent/api/v1/sda/fabricZones/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b7004918aecc58c7880ae97d344bb885_v2_3_7_6', json_data)

    def delete_fabric_zone_by_id(self,
                                 id,
                                 headers=None,
                                 **request_parameters):
        """Deletes a fabric zone based on id. .

        Args:
            id(str): id path parameter. ID of the fabric zone to be deleted. .
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

        e_url = ('/dna/intent/api/v1/sda/fabricZones/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cdb33e11852af80e1ed8f26e4336d_v2_3_7_6', json_data)

    def add_port_assignments(self,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **request_parameters):
        """Adds port assignments based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_d6b58f378895114839682dceed1a9b5_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/portAssignments')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d6b58f378895114839682dceed1a9b5_v2_3_7_6', json_data)

    def get_port_assignments(self,
                             data_vlan_name=None,
                             fabric_id=None,
                             interface_name=None,
                             limit=None,
                             network_device_id=None,
                             offset=None,
                             voice_vlan_name=None,
                             headers=None,
                             **request_parameters):
        """Returns a list of port assignments that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the port assignment
                .
            interface_name(str): interfaceName query parameter. Interface Name of the port assignment .
            data_vlan_name(str): dataVlanName query parameter. Data VLAN name of the port assignment .
            voice_vlan_name(str): voiceVlanName query parameter. Voice VLAN name of the port assignment .
            offset(int,str): offset query parameter. Starting record for pagination .
            limit(int,str): limit query parameter. Maximum number of records to return .
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
        check_type(fabric_id, str)
        check_type(network_device_id, str)
        check_type(interface_name, str)
        check_type(data_vlan_name, str)
        check_type(voice_vlan_name, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
            'interfaceName':
                interface_name,
            'dataVlanName':
                data_vlan_name,
            'voiceVlanName':
                voice_vlan_name,
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

        e_url = ('/dna/intent/api/v1/sda/portAssignments')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a9bc4645925814ac76d95268fe3f05_v2_3_7_6', json_data)

    def update_port_assignments(self,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **request_parameters):
        """Updates port assignments based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_cad522e57a7b96b7238935689ed_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/portAssignments')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_cad522e57a7b96b7238935689ed_v2_3_7_6', json_data)

    def delete_port_assignments(self,
                                fabric_id,
                                network_device_id,
                                data_vlan_name=None,
                                interface_name=None,
                                voice_vlan_name=None,
                                headers=None,
                                **request_parameters):
        """Deletes port assignments based on user input. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the port assignment
                .
            interface_name(str): interfaceName query parameter. Interface name of the port assignment .
            data_vlan_name(str): dataVlanName query parameter. Data VLAN name of the port assignment .
            voice_vlan_name(str): voiceVlanName query parameter. Voice VLAN name of the port assignment .
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
        check_type(fabric_id, str,
                   may_be_none=False)
        check_type(network_device_id, str,
                   may_be_none=False)
        check_type(interface_name, str)
        check_type(data_vlan_name, str)
        check_type(voice_vlan_name, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
            'interfaceName':
                interface_name,
            'dataVlanName':
                data_vlan_name,
            'voiceVlanName':
                voice_vlan_name,
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

        e_url = ('/dna/intent/api/v1/sda/portAssignments')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ee38ba825f79a76d9e7e6074c450_v2_3_7_6', json_data)

    def get_port_assignment_count(self,
                                  data_vlan_name=None,
                                  fabric_id=None,
                                  interface_name=None,
                                  network_device_id=None,
                                  voice_vlan_name=None,
                                  headers=None,
                                  **request_parameters):
        """Returns the count of port assignments that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the port assignment
                .
            interface_name(str): interfaceName query parameter. Interface name of the port assignment .
            data_vlan_name(str): dataVlanName query parameter. Data VLAN name of the port assignment .
            voice_vlan_name(str): voiceVlanName query parameter. Voice VLAN name of the port assignment .
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
        check_type(fabric_id, str)
        check_type(network_device_id, str)
        check_type(interface_name, str)
        check_type(data_vlan_name, str)
        check_type(voice_vlan_name, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'fabricId':
                fabric_id,
            'networkDeviceId':
                network_device_id,
            'interfaceName':
                interface_name,
            'dataVlanName':
                data_vlan_name,
            'voiceVlanName':
                voice_vlan_name,
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

        e_url = ('/dna/intent/api/v1/sda/portAssignments/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e11301d6336f512fbc6db01768e3ad5a_v2_3_7_6', json_data)

    def delete_port_assignment_by_id(self,
                                     id,
                                     headers=None,
                                     **request_parameters):
        """Deletes a port assignment based on id. .

        Args:
            id(str): id path parameter. ID of the port assignment. .
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

        e_url = ('/dna/intent/api/v1/sda/portAssignments/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_aa18582de8753438e0908cf9d92c2de_v2_3_7_6', json_data)

    def delete_provisioned_devices(self,
                                   network_device_id=None,
                                   site_id=None,
                                   headers=None,
                                   **request_parameters):
        """Delete provisioned devices based on query parameters. .

        Args:
            network_device_id(str): networkDeviceId query parameter. ID of the network device. .
            site_id(str): siteId query parameter. ID of the site hierarchy. .
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
        check_type(network_device_id, str)
        check_type(site_id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'networkDeviceId':
                network_device_id,
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

        e_url = ('/dna/intent/api/v1/sda/provisionDevices')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b049914e384051afbf87971d3066152b_v2_3_7_6', json_data)

    def provision_devices(self,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **request_parameters):
        """Provisions network devices to respective Sites based on user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_bdcb514ae33b571795e4a42147d11f87_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/provisionDevices')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_bdcb514ae33b571795e4a42147d11f87_v2_3_7_6', json_data)

    def get_provisioned_devices(self,
                                id=None,
                                limit=None,
                                network_device_id=None,
                                offset=None,
                                site_id=None,
                                headers=None,
                                **request_parameters):
        """Returns the list of provisioned devices based on query parameters. .

        Args:
            id(str): id query parameter. ID of the provisioned device. .
            network_device_id(str): networkDeviceId query parameter. ID of the network device. .
            site_id(str): siteId query parameter. ID of the site hierarchy. .
            offset(int,str): offset query parameter. Starting record for pagination. .
            limit(int,str): limit query parameter. Maximum number of devices to return. .
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
        check_type(id, str)
        check_type(network_device_id, str)
        check_type(site_id, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'id':
                id,
            'networkDeviceId':
                network_device_id,
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

        e_url = ('/dna/intent/api/v1/sda/provisionDevices')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f974cbea9645bfda97affac9ea41ffe_v2_3_7_6', json_data)

    def re_provision_devices(self,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **request_parameters):
        """Re-provisions network devices to the site based on the user input. .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_f4b2825561e808787a16f7e0a1f_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/provisionDevices')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_f4b2825561e808787a16f7e0a1f_v2_3_7_6', json_data)

    def get_provisioned_devices_count(self,
                                      site_id=None,
                                      headers=None,
                                      **request_parameters):
        """Returns the count of provisioned devices based on query parameters. .

        Args:
            site_id(str): siteId query parameter. ID of the site hierarchy. .
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

        e_url = ('/dna/intent/api/v1/sda/provisionDevices/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_acb7d048a5455b75965c3706f8977_v2_3_7_6', json_data)

    def delete_provisioned_device_by_id(self,
                                        id,
                                        headers=None,
                                        **request_parameters):
        """Deletes provisioned device based on Id. .

        Args:
            id(str): id path parameter. ID of provisioned device. .
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

        e_url = ('/dna/intent/api/v1/sda/provisionDevices/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ab7cbac7eaa45f259c9035fb828f6c08_v2_3_7_6', json_data)

    def add_virtual_network_with_scalable_groups(self,
                                                 isGuestVirtualNetwork=None,
                                                 scalableGroupNames=None,
                                                 vManageVpnId=None,
                                                 virtualNetworkName=None,
                                                 headers=None,
                                                 payload=None,
                                                 active_validation=True,
                                                 **request_parameters):
        """Add virtual network with scalable groups at global level .

        Args:
            isGuestVirtualNetwork(boolean): SDA's Guest Virtual Network enablement flag, default value is False. .
            scalableGroupNames(list): SDA's Scalable Group to be associated to virtual network  (list of strings).
            vManageVpnId(string): SDA's vManage vpn id for SD-WAN .
            virtualNetworkName(string): SDA's Virtual Network Name to be assigned at global level .
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
            'virtualNetworkName':
                virtualNetworkName,
            'isGuestVirtualNetwork':
                isGuestVirtualNetwork,
            'scalableGroupNames':
                scalableGroupNames,
            'vManageVpnId':
                vManageVpnId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f5ebb9d50aab287f320d32181c0_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/virtual-network')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f5ebb9d50aab287f320d32181c0_v2_3_7_6', json_data)

    def delete_virtual_network_with_scalable_groups(self,
                                                    virtual_network_name,
                                                    headers=None,
                                                    **request_parameters):
        """Delete virtual network with scalable groups .

        Args:
            virtual_network_name(str): virtualNetworkName query parameter.
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
        check_type(virtual_network_name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'virtualNetworkName':
                virtual_network_name,
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

        e_url = ('/dna/intent/api/v1/virtual-network')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f2e8552eabc5e5f97e1f40bcc4b4c75_v2_3_7_6', json_data)

    def get_virtual_network_with_scalable_groups(self,
                                                 virtual_network_name,
                                                 headers=None,
                                                 **request_parameters):
        """Get virtual network with scalable groups .

        Args:
            virtual_network_name(str): virtualNetworkName query parameter.
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
        check_type(virtual_network_name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'virtualNetworkName':
                virtual_network_name,
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

        e_url = ('/dna/intent/api/v1/virtual-network')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea4b1c052b855bd9a0e99f803e6185a5_v2_3_7_6', json_data)

    def update_virtual_network_with_scalable_groups(self,
                                                    isGuestVirtualNetwork=None,
                                                    scalableGroupNames=None,
                                                    vManageVpnId=None,
                                                    virtualNetworkName=None,
                                                    headers=None,
                                                    payload=None,
                                                    active_validation=True,
                                                    **request_parameters):
        """Update virtual network with scalable groups .

        Args:
            isGuestVirtualNetwork(boolean): SDA's Indicates whether to set this as guest virtual network or not,
                default value is False. .
            scalableGroupNames(list): SDA's Scalable Group Name to be associated to virtual network  (list of
                strings).
            vManageVpnId(string): SDA's vManage vpn id for SD-WAN .
            virtualNetworkName(string): SDA's Virtual Network Name to be assigned global level .
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
            'virtualNetworkName':
                virtualNetworkName,
            'isGuestVirtualNetwork':
                isGuestVirtualNetwork,
            'scalableGroupNames':
                scalableGroupNames,
            'vManageVpnId':
                vManageVpnId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f9492367570c5f009cf8b5955790e87c_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/virtual-network')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_f9492367570c5f009cf8b5955790e87c_v2_3_7_6', json_data)

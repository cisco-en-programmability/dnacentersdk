# -*- coding: utf-8 -*-
"""Cisco DNA Center System Settings API wrapper.

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


class SystemSettings(object):
    """Cisco DNA Center System Settings API (version: 2.3.7.6).

    Wraps the DNA Center System Settings
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SystemSettings
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SystemSettings, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def add_authentication_and_policy_server_access_configuration(self,
                                                                  accountingPort=None,
                                                                  authenticationPort=None,
                                                                  ciscoIseDtos=None,
                                                                  encryptionKey=None,
                                                                  encryptionScheme=None,
                                                                  externalCiscoIseIpAddrDtos=None,
                                                                  ipAddress=None,
                                                                  isIseEnabled=None,
                                                                  messageKey=None,
                                                                  port=None,
                                                                  protocol=None,
                                                                  pxgridEnabled=None,
                                                                  retries=None,
                                                                  role=None,
                                                                  sharedSecret=None,
                                                                  timeoutSeconds=None,
                                                                  useDnacCertForPxgrid=None,
                                                                  headers=None,
                                                                  payload=None,
                                                                  active_validation=True,
                                                                  **request_parameters):
        """API to add AAA/ISE server access configuration. Protocol can be configured as either RADIUS OR TACACS OR
        RADIUS_TACACS. If configuring Cisco ISE server, after configuration, use ‘Cisco ISE Server Integration
        Status’ Intent API to check the integration status. Based on integration status, if require use 'Accept
        Cisco ISE Server Certificate for Cisco ISE Server Integration' Intent API to accept the Cisco ISE
        certificate for Cisco ISE server integration, then use again ‘Cisco ISE Server Integration Status’
        Intent API to check the integration status. .

        Args:
            accountingPort(integer): System Settings's Accounting port of RADIUS server (readonly). The range is
                from 1 to 65535. E.g. 1813 .
            authenticationPort(integer): System Settings's Authentication port of RADIUS server (readonly). The
                range is from 1 to 65535. E.g. 1812 .
            ciscoIseDtos(list): System Settings's ciscoIseDtos (list of objects).
            encryptionKey(string): System Settings's Encryption key used to encrypt shared secret (readonly) .
            encryptionScheme(string): System Settings's Type of encryption scheme for additional security (readonly)
                . Available values are 'KEYWRAP' and 'RADSEC'.
            externalCiscoIseIpAddrDtos(list): System Settings's externalCiscoIseIpAddrDtos (list of objects).
            ipAddress(string): System Settings's IP address of authentication and policy server (readonly) .
            isIseEnabled(boolean): System Settings's Value true for Cisco ISE Server (readonly). Default value is
                false .
            messageKey(string): System Settings's Message key used to encrypt shared secret (readonly) .
            port(integer): System Settings's Port of TACACS server (readonly). The range is from 1 to 65535 .
            protocol(string): System Settings's Type of protocol for authentication and policy server. If already
                saved with RADIUS, can update to RADIUS_TACACS. If already saved with TACACS, can update
                to RADIUS_TACACS  . Available values are 'TACACS', 'RADIUS' and 'RADIUS_TACACS'.
            pxgridEnabled(boolean): System Settings's Value true for enable, false for disable. Default value is
                true .
            retries(string): System Settings's Number of communication retries between devices and authentication
                and policy server. The range is from 1 to 3 .
            role(string): System Settings's Role of authentication and policy server (readonly). E.g. primary,
                secondary .
            sharedSecret(string): System Settings's Shared secret between devices and authentication and policy
                server (readonly) .
            timeoutSeconds(string): System Settings's Number of seconds before timing out between devices and
                authentication and policy server. The range is from 2 to 20 .
            useDnacCertForPxgrid(boolean): System Settings's Value true to use DNAC certificate for Pxgrid. Default
                value is false .
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
            'authenticationPort':
                authenticationPort,
            'accountingPort':
                accountingPort,
            'ciscoIseDtos':
                ciscoIseDtos,
            'ipAddress':
                ipAddress,
            'pxgridEnabled':
                pxgridEnabled,
            'useDnacCertForPxgrid':
                useDnacCertForPxgrid,
            'isIseEnabled':
                isIseEnabled,
            'port':
                port,
            'protocol':
                protocol,
            'retries':
                retries,
            'role':
                role,
            'sharedSecret':
                sharedSecret,
            'timeoutSeconds':
                timeoutSeconds,
            'encryptionScheme':
                encryptionScheme,
            'messageKey':
                messageKey,
            'encryptionKey':
                encryptionKey,
            'externalCiscoIseIpAddrDtos':
                externalCiscoIseIpAddrDtos,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_fa3975be5af25501abb40339d96917eb_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/authentication-policy-servers')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_fa3975be5af25501abb40339d96917eb_v2_3_7_6', json_data)

    def get_authentication_and_policy_servers(self,
                                              is_ise_enabled=None,
                                              role=None,
                                              state=None,
                                              headers=None,
                                              **request_parameters):
        """API to get Authentication and Policy Servers .

        Args:
            is_ise_enabled(bool): isIseEnabled query parameter. Valid values are : true, false .
            state(str): state query parameter. Valid values are: ACTIVE, INACTIVE, RBAC_SUCCESS,
                RBAC_FAILURE, DELETED, FAILED, INPROGRESS .
            role(str): role query parameter. Authentication and Policy Server Role (Example: primary,
                secondary) .
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
        check_type(is_ise_enabled, bool)
        check_type(state, str)
        check_type(role, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'isIseEnabled':
                is_ise_enabled,
            'state':
                state,
            'role':
                role,
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

        e_url = ('/dna/intent/api/v1/authentication-policy-servers')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f7cc2592721f5b9b9f99795a26130147_v2_3_7_6', json_data)

    def delete_authentication_and_policy_server_access_configuration(self,
                                                                     id,
                                                                     headers=None,
                                                                     **request_parameters):
        """API to delete AAA/ISE server access configuration. .

        Args:
            id(str): id path parameter. Authentication and Policy Server Identifier. Use 'Get Authentication
                and Policy Servers' intent API to find the identifier. .
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

        e_url = ('/dna/intent/api/v1/authentication-policy-servers/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b5ce4c02a525aa98e49940d5aa006a7_v2_3_7_6', json_data)

    def edit_authentication_and_policy_server_access_configuration(self,
                                                                   id,
                                                                   accountingPort=None,
                                                                   authenticationPort=None,
                                                                   ciscoIseDtos=None,
                                                                   encryptionKey=None,
                                                                   encryptionScheme=None,
                                                                   externalCiscoIseIpAddrDtos=None,
                                                                   ipAddress=None,
                                                                   isIseEnabled=None,
                                                                   messageKey=None,
                                                                   port=None,
                                                                   protocol=None,
                                                                   pxgridEnabled=None,
                                                                   retries=None,
                                                                   role=None,
                                                                   sharedSecret=None,
                                                                   timeoutSeconds=None,
                                                                   useDnacCertForPxgrid=None,
                                                                   headers=None,
                                                                   payload=None,
                                                                   active_validation=True,
                                                                   **request_parameters):
        """API to edit AAA/ISE server access configuration. After edit, use ‘Cisco ISE Server Integration Status’ Intent
        API to check the integration status. .

        Args:
            accountingPort(integer): System Settings's Accounting port of RADIUS server (readonly). The range is
                from 1 to 65535. E.g. 1813 .
            authenticationPort(integer): System Settings's Authentication port of RADIUS server (readonly). The
                range is from 1 to 65535. E.g. 1812 .
            ciscoIseDtos(list): System Settings's ciscoIseDtos (list of objects).
            encryptionKey(string): System Settings's Encryption key used to encrypt shared secret (readonly) .
            encryptionScheme(string): System Settings's Type of encryption scheme for additional security (readonly)
                . Available values are 'KEYWRAP' and 'RADSEC'.
            externalCiscoIseIpAddrDtos(list): System Settings's externalCiscoIseIpAddrDtos (list of objects).
            ipAddress(string): System Settings's IP address of authentication and policy server (readonly) .
            isIseEnabled(boolean): System Settings's Value true for Cisco ISE Server (readonly). Default value is
                false .
            messageKey(string): System Settings's Message key used to encrypt shared secret (readonly) .
            port(integer): System Settings's Port of TACACS server (readonly). The range is from 1 to 65535 .
            protocol(string): System Settings's Type of protocol for authentication and policy server. If already
                saved with RADIUS, can update to RADIUS_TACACS. If already saved with TACACS, can update
                to RADIUS_TACACS  . Available values are 'TACACS', 'RADIUS' and 'RADIUS_TACACS'.
            pxgridEnabled(boolean): System Settings's Value true for enable, false for disable. Default value is
                true .
            retries(string): System Settings's Number of communication retries between devices and authentication
                and policy server. The range is from 1 to 3 .
            role(string): System Settings's Role of authentication and policy server (readonly). E.g. primary,
                secondary .
            sharedSecret(string): System Settings's Shared secret between devices and authentication and policy
                server (readonly) .
            timeoutSeconds(string): System Settings's Number of seconds before timing out between devices and
                authentication and policy server. The range is from 2 to 20 .
            useDnacCertForPxgrid(boolean): System Settings's Value true to use DNAC certificate for Pxgrid. Default
                value is false .
            id(str): id path parameter. Authentication and Policy Server Identifier. Use 'Get Authentication
                and Policy Servers' intent API to find the identifier. .
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
        _payload = {
            'authenticationPort':
                authenticationPort,
            'accountingPort':
                accountingPort,
            'ciscoIseDtos':
                ciscoIseDtos,
            'ipAddress':
                ipAddress,
            'pxgridEnabled':
                pxgridEnabled,
            'useDnacCertForPxgrid':
                useDnacCertForPxgrid,
            'isIseEnabled':
                isIseEnabled,
            'port':
                port,
            'protocol':
                protocol,
            'retries':
                retries,
            'role':
                role,
            'sharedSecret':
                sharedSecret,
            'timeoutSeconds':
                timeoutSeconds,
            'encryptionScheme':
                encryptionScheme,
            'messageKey':
                messageKey,
            'encryptionKey':
                encryptionKey,
            'externalCiscoIseIpAddrDtos':
                externalCiscoIseIpAddrDtos,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_fbdd94fbecd256c08e1d9f6e1a7657ac_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/authentication-policy-servers/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_fbdd94fbecd256c08e1d9f6e1a7657ac_v2_3_7_6', json_data)

    def accept_cisco_ise_server_certificate_for_cisco_ise_server_integration(self,
                                                                             id,
                                                                             isCertAcceptedByUser=None,
                                                                             headers=None,
                                                                             payload=None,
                                                                             active_validation=True,
                                                                             **request_parameters):
        """API to accept Cisco ISE server certificate for Cisco ISE server integration. Use ‘Cisco ISE Server Integration
        Status’ Intent API to check the integration status. This API can be used to retry the failed
        integration. .

        Args:
            isCertAcceptedByUser(boolean): System Settings's Value true for accept, false for deny. Remove this
                field and send empty request payload ( {} ) to retry the failed integration .
            id(str): id path parameter. Cisco ISE Server Identifier. Use 'Get Authentication and Policy
                Servers' intent API to find the identifier. .
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
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        valide = False
        if isCertAcceptedByUser is None and (payload is None or payload == {}):
            _payload = {}
        else:
            _payload = {
                'isCertAcceptedByUser': isCertAcceptedByUser,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
            valide = True

        if active_validation and valide:
            self._request_validator('jsd_e0ed6b9a530ea05d77a199ded4e3_v2_3_7_6').validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/integrate-ise/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_e0ed6b9a530ea05d77a199ded4e3_v2_3_7_6', json_data)

    def cisco_ise_server_integration_status(self,
                                            headers=None,
                                            **request_parameters):
        """API to check Cisco ISE server integration status. .

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

        e_url = ('/dna/intent/api/v1/ise-integration-status')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a1bc4f82533a5d909ed345b4703cff8a_v2_3_7_6', json_data)

    def custom_prompt_support_get_api(self,
                                      headers=None,
                                      **request_parameters):
        """Returns supported custom prompts by Catalyst Center .

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

        e_url = ('/dna/intent/api/v1/network-device/custom-prompt')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ada20dc4915d5901b50634628392e79f_v2_3_7_6', json_data)

    def custom_prompt_post_api(self,
                               passwordPrompt=None,
                               usernamePrompt=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Save custom prompt added by user in Catalyst Center. API will always override the existing prompts. User should
        provide all the custom prompt in case of any update .

        Args:
            passwordPrompt(string): System Settings's Password for Custom Prompt .
            usernamePrompt(string): System Settings's Username for Custom Prompt .
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
            'usernamePrompt':
                usernamePrompt,
            'passwordPrompt':
                passwordPrompt,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d2ea814bfae85da1b77872d095fc8221_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/custom-prompt')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d2ea814bfae85da1b77872d095fc8221_v2_3_7_6', json_data)

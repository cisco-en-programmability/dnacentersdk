# -*- coding: utf-8 -*-
"""Cisco DNA Center Network Discovery API wrapper.

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


class NetworkDiscovery(object):
    """Cisco DNA Center Network Discovery API (version: 1.3.0).

    Wraps the DNA Center Network Discovery
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkDiscovery
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkDiscovery, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_count_of_all_discovery_jobs(self,
                                        headers=None,
                                        **request_parameters):
        """Returns the count of all available discovery jobs.

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
                           basestring, may_be_none=False)

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

        e_url = ('/dna/intent/api/v1/discovery/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_069d9823451b892d_v1_3_0', json_data)

    def create_netconf_credentials(self,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Adds global netconf credentials.

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

        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_17929bc7465bb564_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/netconf')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_17929bc7465bb564_v1_3_0', json_data)

    def update_snmp_write_community(self,
                                    comments=None,
                                    credentialType=None,
                                    description=None,
                                    id=None,
                                    instanceTenantId=None,
                                    instanceUuid=None,
                                    writeCommunity=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **request_parameters):
        """Updates global SNMP write community.

        Args:
            comments(string): SNMPv2WriteCommunityDTO's comments.
            credentialType(string): SNMPv2WriteCommunityDTO's credentialType. Available values are 'GLOBAL' and
                'APP'.
            description(string): SNMPv2WriteCommunityDTO's description.
            id(string): SNMPv2WriteCommunityDTO's id.
            instanceTenantId(string): SNMPv2WriteCommunityDTO's instanceTenantId.
            instanceUuid(string): SNMPv2WriteCommunityDTO's instanceUuid.
            writeCommunity(string): SNMPv2WriteCommunityDTO's writeCommunity.
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
            'credentialType':
                credentialType,
            'description':
                description,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
            'instanceUuid':
                instanceUuid,
            'writeCommunity':
                writeCommunity,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_10b06a6a4f7bb3cb_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/snmpv2-write-'
                 + 'community')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_10b06a6a4f7bb3cb_v1_3_0', json_data)

    def update_snmpv3_credentials(self,
                                  authPassword=None,
                                  authType=None,
                                  comments=None,
                                  credentialType=None,
                                  description=None,
                                  id=None,
                                  instanceTenantId=None,
                                  instanceUuid=None,
                                  privacyPassword=None,
                                  privacyType=None,
                                  snmpMode=None,
                                  username=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Updates global SNMPv3 credential.

        Args:
            authPassword(string): SNMPv3CredentialDTO's authPassword.
            authType(string): SNMPv3CredentialDTO's authType. Available values are 'SHA' and 'MD5'.
            comments(string): SNMPv3CredentialDTO's comments.
            credentialType(string): SNMPv3CredentialDTO's credentialType. Available values are 'GLOBAL' and 'APP'.
            description(string): SNMPv3CredentialDTO's description.
            id(string): SNMPv3CredentialDTO's id.
            instanceTenantId(string): SNMPv3CredentialDTO's instanceTenantId.
            instanceUuid(string): SNMPv3CredentialDTO's instanceUuid.
            privacyPassword(string): SNMPv3CredentialDTO's privacyPassword.
            privacyType(string): SNMPv3CredentialDTO's privacyType. Available values are 'DES' and 'AES128'.
            snmpMode(string): SNMPv3CredentialDTO's snmpMode. Available values are 'AUTHPRIV', 'AUTHNOPRIV' and
                'NOAUTHNOPRIV'.
            username(string): SNMPv3CredentialDTO's username.
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
            'authPassword':
                authPassword,
            'authType':
                authType,
            'comments':
                comments,
            'credentialType':
                credentialType,
            'description':
                description,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
            'instanceUuid':
                instanceUuid,
            'privacyPassword':
                privacyPassword,
            'privacyType':
                privacyType,
            'snmpMode':
                snmpMode,
            'username':
                username,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_1da5ebdd434aacfe_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/snmpv3')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_1da5ebdd434aacfe_v1_3_0', json_data)

    def update_snmp_read_community(self,
                                   comments=None,
                                   credentialType=None,
                                   description=None,
                                   id=None,
                                   instanceTenantId=None,
                                   instanceUuid=None,
                                   readCommunity=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Updates global SNMP read community.

        Args:
            comments(string): SNMPv2ReadCommunityDTO's comments.
            credentialType(string): SNMPv2ReadCommunityDTO's credentialType. Available values are 'GLOBAL' and
                'APP'.
            description(string): SNMPv2ReadCommunityDTO's description.
            id(string): SNMPv2ReadCommunityDTO's id.
            instanceTenantId(string): SNMPv2ReadCommunityDTO's instanceTenantId.
            instanceUuid(string): SNMPv2ReadCommunityDTO's instanceUuid.
            readCommunity(string): SNMPv2ReadCommunityDTO's readCommunity.
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
            'credentialType':
                credentialType,
            'description':
                description,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
            'instanceUuid':
                instanceUuid,
            'readCommunity':
                readCommunity,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_47a1b84b4e1b8044_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/snmpv2-read-'
                 + 'community')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_47a1b84b4e1b8044_v1_3_0', json_data)

    def get_discoveries_by_range(self,
                                 records_to_return,
                                 start_index,
                                 headers=None,
                                 **request_parameters):
        """Returns the discovery by specified range.

        Args:
            start_index(int): Start index.
            records_to_return(int): Number of records to return.
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
        check_type(start_index, int,
                   may_be_none=False)
        check_type(records_to_return, int,
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
            'startIndex': start_index,
            'recordsToReturn': records_to_return,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/${startIndex}/${recordsToRe'
                 + 'turn}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_33b799d04d0a8907_v1_3_0', json_data)

    def get_network_devices_from_discovery(self,
                                           id,
                                           cli_status=None,
                                           http_status=None,
                                           ip_address=None,
                                           netconf_status=None,
                                           ping_status=None,
                                           snmp_status=None,
                                           sort_by=None,
                                           sort_order=None,
                                           task_id=None,
                                           headers=None,
                                           **request_parameters):
        """Returns the network devices from a discovery job based on given
        filters. Discovery ID can be obtained using the "Get
        Discoveries by range" API.

        Args:
            id(basestring): Discovery ID.
            task_id(basestring): taskId query parameter.
            sort_by(basestring): sortBy query parameter.
            sort_order(basestring): sortOrder query parameter.
            ip_address(basestring, list, set, tuple): ipAddress query parameter.
            ping_status(basestring, list, set, tuple): pingStatus query parameter.
            snmp_status(basestring, list, set, tuple): snmpStatus query parameter.
            cli_status(basestring, list, set, tuple): cliStatus query parameter.
            netconf_status(basestring, list, set, tuple): netconfStatus query parameter.
            http_status(basestring, list, set, tuple): httpStatus query parameter.
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
        check_type(task_id, basestring)
        check_type(sort_by, basestring)
        check_type(sort_order, basestring)
        check_type(ip_address, (basestring, list, set, tuple))
        check_type(ping_status, (basestring, list, set, tuple))
        check_type(snmp_status, (basestring, list, set, tuple))
        check_type(cli_status, (basestring, list, set, tuple))
        check_type(netconf_status, (basestring, list, set, tuple))
        check_type(http_status, (basestring, list, set, tuple))
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'taskId':
                task_id,
            'sortBy':
                sort_by,
            'sortOrder':
                sort_order,
            'ipAddress':
                ip_address,
            'pingStatus':
                ping_status,
            'snmpStatus':
                snmp_status,
            'cliStatus':
                cli_status,
            'netconfStatus':
                netconf_status,
            'httpStatus':
                http_status,
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

        e_url = ('/dna/intent/api/v1/discovery/${id}/summary')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_3d9b99c343398a27_v1_3_0', json_data)

    def create_http_write_credentials(self,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **request_parameters):
        """Adds global HTTP write credentials.

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

        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_4d9ca8e2431a8a24_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/http-write')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_4d9ca8e2431a8a24_v1_3_0', json_data)

    def get_snmp_properties(self,
                            headers=None,
                            **request_parameters):
        """Returns SNMP properties.

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
                           basestring, may_be_none=False)

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

        e_url = ('/dna/intent/api/v1/snmp-property')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_44974ba5435a801d_v1_3_0', json_data)

    def delete_discovery_by_id(self,
                               id,
                               headers=None,
                               **request_parameters):
        """Stops the discovery for the given Discovery ID and removes it.
        Discovery ID can be obtained using the "Get Discoveries
        by range" API.

        Args:
            id(basestring): Discovery ID.
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
        check_type(id, basestring,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_4c8cab5f435a80f4_v1_3_0', json_data)

    def start_discovery(self,
                        cdpLevel=None,
                        discoveryType=None,
                        enablePasswordList=None,
                        globalCredentialIdList=None,
                        httpReadCredential=None,
                        httpWriteCredential=None,
                        ipAddressList=None,
                        ipFilterList=None,
                        lldpLevel=None,
                        name=None,
                        netconfPort=None,
                        noAddNewDevice=None,
                        parentDiscoveryId=None,
                        passwordList=None,
                        preferredMgmtIPMethod=None,
                        protocolOrder=None,
                        reDiscovery=None,
                        retry=None,
                        snmpAuthPassphrase=None,
                        snmpAuthProtocol=None,
                        snmpMode=None,
                        snmpPrivPassphrase=None,
                        snmpPrivProtocol=None,
                        snmpROCommunity=None,
                        snmpROCommunityDesc=None,
                        snmpRWCommunity=None,
                        snmpRWCommunityDesc=None,
                        snmpUserName=None,
                        snmpVersion=None,
                        timeout=None,
                        updateMgmtIp=None,
                        userNameList=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Initiates discovery with the given parameters.

        Args:
            cdpLevel(number): InventoryRequest's cdpLevel.
            discoveryType(string): InventoryRequest's discoveryType.
            enablePasswordList(list): InventoryRequest's enablePasswordList (list of string, objects).
            globalCredentialIdList(list): InventoryRequest's globalCredentialIdList (list of string, objects).
            httpReadCredential(object): InventoryRequest's httpReadCredential.
            httpWriteCredential(object): InventoryRequest's httpWriteCredential.
            ipAddressList(string): InventoryRequest's ipAddressList.
            ipFilterList(list): InventoryRequest's ipFilterList (list of string, objects).
            lldpLevel(number): InventoryRequest's lldpLevel.
            name(string): InventoryRequest's name.
            netconfPort(string): InventoryRequest's netconfPort.
            noAddNewDevice(boolean): InventoryRequest's noAddNewDevice.
            parentDiscoveryId(string): InventoryRequest's parentDiscoveryId.
            passwordList(list): InventoryRequest's passwordList (list of string, objects).
            preferredMgmtIPMethod(string): InventoryRequest's preferredMgmtIPMethod.
            protocolOrder(string): InventoryRequest's protocolOrder.
            reDiscovery(boolean): InventoryRequest's reDiscovery.
            retry(number): InventoryRequest's retry.
            snmpAuthPassphrase(string): InventoryRequest's snmpAuthPassphrase.
            snmpAuthProtocol(string): InventoryRequest's snmpAuthProtocol.
            snmpMode(string): InventoryRequest's snmpMode.
            snmpPrivPassphrase(string): InventoryRequest's snmpPrivPassphrase.
            snmpPrivProtocol(string): InventoryRequest's snmpPrivProtocol.
            snmpROCommunity(string): InventoryRequest's snmpROCommunity.
            snmpROCommunityDesc(string): InventoryRequest's snmpROCommunityDesc.
            snmpRWCommunity(string): InventoryRequest's snmpRWCommunity.
            snmpRWCommunityDesc(string): InventoryRequest's snmpRWCommunityDesc.
            snmpUserName(string): InventoryRequest's snmpUserName.
            snmpVersion(string): InventoryRequest's snmpVersion.
            timeout(number): InventoryRequest's timeout.
            updateMgmtIp(boolean): InventoryRequest's updateMgmtIp.
            userNameList(list): InventoryRequest's userNameList (list of string, objects).
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
            'cdpLevel':
                cdpLevel,
            'discoveryType':
                discoveryType,
            'enablePasswordList':
                enablePasswordList,
            'globalCredentialIdList':
                globalCredentialIdList,
            'httpReadCredential':
                httpReadCredential,
            'httpWriteCredential':
                httpWriteCredential,
            'ipAddressList':
                ipAddressList,
            'ipFilterList':
                ipFilterList,
            'lldpLevel':
                lldpLevel,
            'name':
                name,
            'netconfPort':
                netconfPort,
            'noAddNewDevice':
                noAddNewDevice,
            'parentDiscoveryId':
                parentDiscoveryId,
            'passwordList':
                passwordList,
            'preferredMgmtIPMethod':
                preferredMgmtIPMethod,
            'protocolOrder':
                protocolOrder,
            'reDiscovery':
                reDiscovery,
            'retry':
                retry,
            'snmpAuthPassphrase':
                snmpAuthPassphrase,
            'snmpAuthProtocol':
                snmpAuthProtocol,
            'snmpMode':
                snmpMode,
            'snmpPrivPassphrase':
                snmpPrivPassphrase,
            'snmpPrivProtocol':
                snmpPrivProtocol,
            'snmpROCommunity':
                snmpROCommunity,
            'snmpROCommunityDesc':
                snmpROCommunityDesc,
            'snmpRWCommunity':
                snmpRWCommunity,
            'snmpRWCommunityDesc':
                snmpRWCommunityDesc,
            'snmpUserName':
                snmpUserName,
            'snmpVersion':
                snmpVersion,
            'timeout':
                timeout,
            'updateMgmtIp':
                updateMgmtIp,
            'userNameList':
                userNameList,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_55b439dc4239b140_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_55b439dc4239b140_v1_3_0', json_data)

    def get_discovery_by_id(self,
                            id,
                            headers=None,
                            **request_parameters):
        """Returns discovery by Discovery ID. Discovery ID can be obtained
        using the "Get Discoveries by range" API.

        Args:
            id(basestring): Discovery ID.
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
        check_type(id, basestring,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_63bb88b74f59aa17_v1_3_0', json_data)

    def create_snmp_write_community(self,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **request_parameters):
        """Adds global SNMP write community.

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

        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_6bacb8d14639bdc7_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/snmpv2-write-'
                 + 'community')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_6bacb8d14639bdc7_v1_3_0', json_data)

    def create_cli_credentials(self,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Adds global CLI credential.

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

        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_948ea8194348bc0b_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/cli')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_948ea8194348bc0b_v1_3_0', json_data)

    def update_http_read_credential(self,
                                    comments=None,
                                    credentialType=None,
                                    description=None,
                                    id=None,
                                    instanceTenantId=None,
                                    instanceUuid=None,
                                    password=None,
                                    port=None,
                                    secure=None,
                                    username=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **request_parameters):
        """Updates global HTTP Read credential.

        Args:
            comments(string): HTTPReadCredentialDTO's comments.
            credentialType(string): HTTPReadCredentialDTO's credentialType. Available values are 'GLOBAL' and 'APP'.
            description(string): HTTPReadCredentialDTO's description.
            id(string): HTTPReadCredentialDTO's id.
            instanceTenantId(string): HTTPReadCredentialDTO's instanceTenantId.
            instanceUuid(string): HTTPReadCredentialDTO's instanceUuid.
            password(string): HTTPReadCredentialDTO's password.
            port(number): HTTPReadCredentialDTO's port.
            secure(boolean): HTTPReadCredentialDTO's secure.
            username(string): HTTPReadCredentialDTO's username.
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
            'credentialType':
                credentialType,
            'description':
                description,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
            'instanceUuid':
                instanceUuid,
            'password':
                password,
            'port':
                port,
            'secure':
                secure,
            'username':
                username,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_89b36b4649999d81_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/http-read')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_89b36b4649999d81_v1_3_0', json_data)

    def get_list_of_discoveries_by_discovery_id(self,
                                                id,
                                                ip_address=None,
                                                limit=None,
                                                offset=None,
                                                headers=None,
                                                **request_parameters):
        """Returns the list of discovery jobs for the given Discovery ID.
        The results can be optionally filtered based on IP.
        Discovery ID can be obtained using the "Get Discoveries
        by range" API.

        Args:
            id(basestring): Discovery ID.
            offset(int): offset query parameter.
            limit(int): limit query parameter.
            ip_address(basestring): ipAddress query parameter.
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
        check_type(offset, int)
        check_type(limit, int)
        check_type(ip_address, basestring)
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
            'ipAddress':
                ip_address,
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

        e_url = ('/dna/intent/api/v1/discovery/${id}/job')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_99872a134d0a9fb4_v1_3_0', json_data)

    def create_snmpv3_credentials(self,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Adds global SNMPv3 credentials.

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

        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_979688084b7ba60d_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/snmpv3')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_979688084b7ba60d_v1_3_0', json_data)

    def create_update_snmp_properties(self,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **request_parameters):
        """Adds SNMP properties.

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

        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_a5ac99774c6bb541_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/snmp-property')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a5ac99774c6bb541_v1_3_0', json_data)

    def updates_discovery_by_id(self,
                                attributeInfo=None,
                                cdpLevel=None,
                                deviceIds=None,
                                discoveryCondition=None,
                                discoveryStatus=None,
                                discoveryType=None,
                                enablePasswordList=None,
                                globalCredentialIdList=None,
                                httpReadCredential=None,
                                httpWriteCredential=None,
                                id=None,
                                ipAddressList=None,
                                ipFilterList=None,
                                isAutoCdp=None,
                                lldpLevel=None,
                                name=None,
                                netconfPort=None,
                                numDevices=None,
                                parentDiscoveryId=None,
                                passwordList=None,
                                preferredMgmtIPMethod=None,
                                protocolOrder=None,
                                retryCount=None,
                                snmpAuthPassphrase=None,
                                snmpAuthProtocol=None,
                                snmpMode=None,
                                snmpPrivPassphrase=None,
                                snmpPrivProtocol=None,
                                snmpRoCommunity=None,
                                snmpRoCommunityDesc=None,
                                snmpRwCommunity=None,
                                snmpRwCommunityDesc=None,
                                snmpUserName=None,
                                timeOut=None,
                                updateMgmtIp=None,
                                userNameList=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **request_parameters):
        """Stops or starts an existing discovery.

        Args:
            attributeInfo(object): DiscoveryNIO's attributeInfo.
            cdpLevel(number): DiscoveryNIO's cdpLevel.
            deviceIds(string): DiscoveryNIO's deviceIds.
            discoveryCondition(string): DiscoveryNIO's discoveryCondition.
            discoveryStatus(string): DiscoveryNIO's discoveryStatus.
            discoveryType(string): DiscoveryNIO's discoveryType.
            enablePasswordList(string): DiscoveryNIO's enablePasswordList.
            globalCredentialIdList(list): DiscoveryNIO's globalCredentialIdList (list of string, objects).
            httpReadCredential(object): DiscoveryNIO's httpReadCredential.
            httpWriteCredential(object): DiscoveryNIO's httpWriteCredential.
            id(string): DiscoveryNIO's id.
            ipAddressList(string): DiscoveryNIO's ipAddressList.
            ipFilterList(string): DiscoveryNIO's ipFilterList.
            isAutoCdp(boolean): DiscoveryNIO's isAutoCdp.
            lldpLevel(number): DiscoveryNIO's lldpLevel.
            name(string): DiscoveryNIO's name.
            netconfPort(string): DiscoveryNIO's netconfPort.
            numDevices(number): DiscoveryNIO's numDevices.
            parentDiscoveryId(string): DiscoveryNIO's parentDiscoveryId.
            passwordList(string): DiscoveryNIO's passwordList.
            preferredMgmtIPMethod(string): DiscoveryNIO's preferredMgmtIPMethod.
            protocolOrder(string): DiscoveryNIO's protocolOrder.
            retryCount(number): DiscoveryNIO's retryCount.
            snmpAuthPassphrase(string): DiscoveryNIO's snmpAuthPassphrase.
            snmpAuthProtocol(string): DiscoveryNIO's snmpAuthProtocol.
            snmpMode(string): DiscoveryNIO's snmpMode.
            snmpPrivPassphrase(string): DiscoveryNIO's snmpPrivPassphrase.
            snmpPrivProtocol(string): DiscoveryNIO's snmpPrivProtocol.
            snmpRoCommunity(string): DiscoveryNIO's snmpRoCommunity.
            snmpRoCommunityDesc(string): DiscoveryNIO's snmpRoCommunityDesc.
            snmpRwCommunity(string): DiscoveryNIO's snmpRwCommunity.
            snmpRwCommunityDesc(string): DiscoveryNIO's snmpRwCommunityDesc.
            snmpUserName(string): DiscoveryNIO's snmpUserName.
            timeOut(number): DiscoveryNIO's timeOut.
            updateMgmtIp(boolean): DiscoveryNIO's updateMgmtIp.
            userNameList(string): DiscoveryNIO's userNameList.
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
            'attributeInfo':
                attributeInfo,
            'cdpLevel':
                cdpLevel,
            'deviceIds':
                deviceIds,
            'discoveryCondition':
                discoveryCondition,
            'discoveryStatus':
                discoveryStatus,
            'discoveryType':
                discoveryType,
            'enablePasswordList':
                enablePasswordList,
            'globalCredentialIdList':
                globalCredentialIdList,
            'httpReadCredential':
                httpReadCredential,
            'httpWriteCredential':
                httpWriteCredential,
            'id':
                id,
            'ipAddressList':
                ipAddressList,
            'ipFilterList':
                ipFilterList,
            'isAutoCdp':
                isAutoCdp,
            'lldpLevel':
                lldpLevel,
            'name':
                name,
            'netconfPort':
                netconfPort,
            'numDevices':
                numDevices,
            'parentDiscoveryId':
                parentDiscoveryId,
            'passwordList':
                passwordList,
            'preferredMgmtIPMethod':
                preferredMgmtIPMethod,
            'protocolOrder':
                protocolOrder,
            'retryCount':
                retryCount,
            'snmpAuthPassphrase':
                snmpAuthPassphrase,
            'snmpAuthProtocol':
                snmpAuthProtocol,
            'snmpMode':
                snmpMode,
            'snmpPrivPassphrase':
                snmpPrivPassphrase,
            'snmpPrivProtocol':
                snmpPrivProtocol,
            'snmpRoCommunity':
                snmpRoCommunity,
            'snmpRoCommunityDesc':
                snmpRoCommunityDesc,
            'snmpRwCommunity':
                snmpRwCommunity,
            'snmpRwCommunityDesc':
                snmpRwCommunityDesc,
            'snmpUserName':
                snmpUserName,
            'timeOut':
                timeOut,
            'updateMgmtIp':
                updateMgmtIp,
            'userNameList':
                userNameList,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_9788b8fc4418831d_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_9788b8fc4418831d_v1_3_0', json_data)

    def update_http_write_credentials(self,
                                      comments=None,
                                      credentialType=None,
                                      description=None,
                                      id=None,
                                      instanceTenantId=None,
                                      instanceUuid=None,
                                      password=None,
                                      port=None,
                                      secure=None,
                                      username=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **request_parameters):
        """Updates global HTTP write credentials.

        Args:
            comments(string): HTTPWriteCredentialDTO's comments.
            credentialType(string): HTTPWriteCredentialDTO's credentialType. Available values are 'GLOBAL' and
                'APP'.
            description(string): HTTPWriteCredentialDTO's description.
            id(string): HTTPWriteCredentialDTO's id.
            instanceTenantId(string): HTTPWriteCredentialDTO's instanceTenantId.
            instanceUuid(string): HTTPWriteCredentialDTO's instanceUuid.
            password(string): HTTPWriteCredentialDTO's password.
            port(number): HTTPWriteCredentialDTO's port.
            secure(boolean): HTTPWriteCredentialDTO's secure.
            username(string): HTTPWriteCredentialDTO's username.
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
            'credentialType':
                credentialType,
            'description':
                description,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
            'instanceUuid':
                instanceUuid,
            'password':
                password,
            'port':
                port,
            'secure':
                secure,
            'username':
                username,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_b68a6bd8473a9a25_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/http-write')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_b68a6bd8473a9a25_v1_3_0', json_data)

    def delete_discovery_by_specified_range(self,
                                            records_to_delete,
                                            start_index,
                                            headers=None,
                                            **request_parameters):
        """Stops discovery for the given range and removes them.

        Args:
            start_index(int): Start index.
            records_to_delete(int): Number of records to delete.
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
        check_type(start_index, int,
                   may_be_none=False)
        check_type(records_to_delete, int,
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
            'startIndex': start_index,
            'recordsToDelete': records_to_delete,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/${startIndex}/${recordsToDe'
                 + 'lete}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c1ba9a424c08a01b_v1_3_0', json_data)

    def delete_all_discovery(self,
                             headers=None,
                             **request_parameters):
        """Stops all the discoveries and removes them.

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
                           basestring, may_be_none=False)

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

        e_url = ('/dna/intent/api/v1/discovery')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_db8e09234a988bab_v1_3_0', json_data)

    def get_devices_discovered_by_id(self,
                                     id,
                                     task_id=None,
                                     headers=None,
                                     **request_parameters):
        """Returns the count of network devices discovered in the given
        discovery. Discovery ID can be obtained using the "Get
        Discoveries by range" API.

        Args:
            id(basestring): Discovery ID.
            task_id(basestring): taskId query parameter.
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
        check_type(task_id, basestring)
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'taskId':
                task_id,
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

        e_url = ('/dna/intent/api/v1/discovery/${id}/network-device/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a6965b454c9a8663_v1_3_0', json_data)

    def delete_global_credentials_by_id(self,
                                        global_credential_id,
                                        headers=None,
                                        **request_parameters):
        """Deletes global credential for the given ID.

        Args:
            global_credential_id(basestring): ID of global-credential.
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
        check_type(global_credential_id, basestring,
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
            'globalCredentialId': global_credential_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-'
                 + 'credential/${globalCredentialId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f5ac590c4ca9975a_v1_3_0', json_data)

    def update_cli_credentials(self,
                               comments=None,
                               credentialType=None,
                               description=None,
                               enablePassword=None,
                               id=None,
                               instanceTenantId=None,
                               instanceUuid=None,
                               password=None,
                               username=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Updates global CLI credentials.

        Args:
            comments(string): CLICredentialDTO's comments.
            credentialType(string): CLICredentialDTO's credentialType. Available values are 'GLOBAL' and 'APP'.
            description(string): CLICredentialDTO's description.
            enablePassword(string): CLICredentialDTO's enablePassword.
            id(string): CLICredentialDTO's id.
            instanceTenantId(string): CLICredentialDTO's instanceTenantId.
            instanceUuid(string): CLICredentialDTO's instanceUuid.
            password(string): CLICredentialDTO's password.
            username(string): CLICredentialDTO's username.
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
            'credentialType':
                credentialType,
            'description':
                description,
            'enablePassword':
                enablePassword,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
            'instanceUuid':
                instanceUuid,
            'password':
                password,
            'username':
                username,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_fba0d80747eb82e8_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/cli')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_fba0d80747eb82e8_v1_3_0', json_data)

    def create_http_read_credentials(self,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **request_parameters):
        """Adds HTTP read credentials.

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

        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_bf859ac64a0ba19c_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/http-read')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_bf859ac64a0ba19c_v1_3_0', json_data)

    def update_netconf_credentials(self,
                                   comments=None,
                                   credentialType=None,
                                   description=None,
                                   id=None,
                                   instanceTenantId=None,
                                   instanceUuid=None,
                                   netconfPort=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Updates global netconf credentials.

        Args:
            comments(string): NetconfCredentialDTO's comments.
            credentialType(string): NetconfCredentialDTO's credentialType. Available values are 'GLOBAL' and 'APP'.
            description(string): NetconfCredentialDTO's description.
            id(string): NetconfCredentialDTO's id.
            instanceTenantId(string): NetconfCredentialDTO's instanceTenantId.
            instanceUuid(string): NetconfCredentialDTO's instanceUuid.
            netconfPort(string): NetconfCredentialDTO's netconfPort.
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
            'credentialType':
                credentialType,
            'description':
                description,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
            'instanceUuid':
                instanceUuid,
            'netconfPort':
                netconfPort,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_c5acd9fa4c1a8abc_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/netconf')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_c5acd9fa4c1a8abc_v1_3_0', json_data)

    def get_credential_sub_type_by_credential_id(self,
                                                 id,
                                                 headers=None,
                                                 **request_parameters):
        """Returns the credential sub type for the given Id.

        Args:
            id(basestring): Global Credential ID.
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
        check_type(id, basestring,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_58a3699e489b9529_v1_3_0', json_data)

    def update_global_credentials(self,
                                  global_credential_id,
                                  siteUuids=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Update global credential for network devices in site(s).

        Args:
            siteUuids(list): SitesInfoDTO's siteUuids (list of strings).
            global_credential_id(basestring): Global credential Uuid.
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
        check_type(global_credential_id, basestring,
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
            'globalCredentialId': global_credential_id,
        }

        _payload = {
            'siteUuids':
                siteUuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_709fda3c42b8877a_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-'
                 + 'credential/${globalCredentialId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_709fda3c42b8877a_v1_3_0', json_data)

    def create_snmp_read_community(self,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Adds global SNMP read community.

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

        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_7aa3da9d4e098ef2_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/snmpv2-read-'
                 + 'community')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_7aa3da9d4e098ef2_v1_3_0', json_data)

    def get_discovery_jobs_by_ip(self,
                                 ip_address,
                                 limit=None,
                                 name=None,
                                 offset=None,
                                 headers=None,
                                 **request_parameters):
        """Returns the list of discovery jobs for the given IP.

        Args:
            offset(int): offset query parameter.
            limit(int): limit query parameter.
            ip_address(basestring): ipAddress query parameter.
            name(basestring): name query parameter.
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
        check_type(offset, int)
        check_type(limit, int)
        check_type(ip_address, basestring,
                   may_be_none=False)
        check_type(name, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
            'ipAddress':
                ip_address,
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

        e_url = ('/dna/intent/api/v1/discovery/job')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a4967be64dfaaa1a_v1_3_0', json_data)

    def get_discovered_devices_by_range(self,
                                        id,
                                        records_to_return,
                                        start_index,
                                        task_id=None,
                                        headers=None,
                                        **request_parameters):
        """Returns the network devices discovered for the given discovery
        and for the given range. The maximum number of records
        that can be retrieved is 500. Discovery ID can be
        obtained using the "Get Discoveries by range" API.

        Args:
            id(basestring): Discovery ID.
            start_index(int): Start index.
            records_to_return(int): Number of records to return.
            task_id(basestring): taskId query parameter.
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
        check_type(task_id, basestring)
        check_type(id, basestring,
                   may_be_none=False)
        check_type(start_index, int,
                   may_be_none=False)
        check_type(records_to_return, int,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'taskId':
                task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
            'startIndex': start_index,
            'recordsToReturn': records_to_return,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/${id}/network-'
                 + 'device/${startIndex}/${recordsToReturn}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a6b798ab4acaa34e_v1_3_0', json_data)

    def get_global_credentials(self,
                               credential_sub_type=None,
                               order=None,
                               sort_by=None,
                               headers=None,
                               **request_parameters):
        """Returns global credential for the given credential sub type.

        Args:
            credential_sub_type(basestring): Credential type as CLI / SNMPV2_READ_COMMUNITY / SNMPV2_WRITE_COMMUNITY
                / SNMPV3 / HTTP_WRITE / HTTP_READ / NETCONF.
            sort_by(basestring): sortBy query parameter.
            order(basestring): order query parameter.
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
        check_type(credential_sub_type, basestring)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'credentialSubType':
                credential_sub_type,
            'sortBy':
                sort_by,
            'order':
                order,
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

        e_url = ('/dna/intent/api/v1/global-credential')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ff816b8e435897eb_v1_3_0', json_data)

    def get_discovered_network_devices_by_discovery_id(self,
                                                       id,
                                                       task_id=None,
                                                       headers=None,
                                                       **request_parameters):
        """Returns the network devices discovered for the given Discovery
        ID. Discovery ID can be obtained using the "Get
        Discoveries by range" API.

        Args:
            id(basestring): Discovery ID.
            task_id(basestring): taskId query parameter.
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
        check_type(task_id, basestring)
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'taskId':
                task_id,
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

        e_url = ('/dna/intent/api/v1/discovery/${id}/network-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f6ac994f451ba011_v1_3_0', json_data)

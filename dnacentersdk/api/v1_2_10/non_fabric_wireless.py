# -*- coding: utf-8 -*-
"""DNA Center Non-Fabric Wireless API wrapper.

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


class NonFabricWireless(object):
    """DNA Center Non-Fabric Wireless API (version: 1.2.10).

    Wraps the DNA Center Non-Fabric Wireless
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NonFabricWireless
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NonFabricWireless, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def delete_and_provision_ssid(self,
                                  managed_aplocations,
                                  ssid_name,
                                  headers=None,
                                  **request_parameters):
        """**Beta** - Removes SSID from the given site profile and
        provisions these changes to devices matching the site
        profile.

        Args:
            ssid_name(basestring): Enter the SSID name to be
                deleted.
            managed_aplocations(basestring): Enter complete site
                hierarchy to remove the SSID from the
                devices found in it. To enter more than
                one site hierarchy, use comma delimiter
                without extra space.
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
        check_type(ssid_name, basestring,
                   may_be_none=False)
        check_type(managed_aplocations, basestring,
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
            'ssidName': ssid_name,
            'managedAPLocations': managed_aplocations,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/ssid/${ssidName}/${managedAP'
                 + 'Locations}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=params)

        return self._object_factory('bpm_cca098344a489dfa_v1_2_10', json_data)

    def create_enterprise_ssid(self,
                               enableBroadcastSSID=None,
                               enableFastLane=None,
                               enableMACFiltering=None,
                               fastTransition=None,
                               name=None,
                               passphrase=None,
                               radioPolicy=None,
                               securityLevel=None,
                               trafficType=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """**Beta** - Creates enterprise SSID.

        Args:
            enableBroadcastSSID(boolean): enableBroadcastSSID,
                property of the request body.
            enableFastLane(boolean): enableFastLane, property of the
                request body.
            enableMACFiltering(boolean): enableMACFiltering,
                property of the request body.
            fastTransition(string): Fast Transition, property of the
                request body. Available values are
                'Adaptive', 'Enable' and 'Disable'.
            name(string): Enter SSID Name, property of the request
                body. Constraints: maxLength set to 32.
            passphrase(string): Pass Phrase (Only applicable for
                SSID with PERSONAL security level),
                property of the request body.
                Constraints: maxLength set to 63 and
                minLength set to 8.
            radioPolicy(string): Radio Policy, property of the
                request body. Available values are 'Dual
                band operation (2.4GHz and 5GHz)', 'Dual
                band operation with band select', '5GHz
                only' and '2.4GHz only'.
            securityLevel(string): Security Level, property of the
                request body. Available values are
                'WPA2_ENTERPRISE', 'WPA2_PERSONAL' and
                'OPEN'.
            trafficType(string): Traffic Type, property of the
                request body. Available values are
                'voicedata' and 'data'.
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
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
            'name':
                name,
            'securityLevel':
                securityLevel,
            'passphrase':
                passphrase,
            'enableFastLane':
                enableFastLane,
            'enableMACFiltering':
                enableMACFiltering,
            'trafficType':
                trafficType,
            'radioPolicy':
                radioPolicy,
            'enableBroadcastSSID':
                enableBroadcastSSID,
            'fastTransition':
                fastTransition,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_8a96fb954d09a349_v1_2_10')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/enterprise-ssid')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload)

        return self._object_factory('bpm_8a96fb954d09a349_v1_2_10', json_data)

    def create_and_provision_ssid(self,
                                  enableFabric=None,
                                  flexConnect=None,
                                  managedAPLocations=None,
                                  ssidDetails=None,
                                  ssidType=None,
                                  vlanAndDynamicInterfaceDetails=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """**Beta** - Creates SSID, adds it to the corresponding site
        profiles and provisions to devices matching the site
        profile.

        Args:
            enableFabric(boolean): enableFabric, property of the
                request body.
            flexConnect(object): Flex Connect - Applicable for non
                fabric profile, property of the request
                body.
            managedAPLocations(list): Managed AP Locations (Enter
                entire Site(s) hierarchy), property of
                the request body (list of strings).
            ssidDetails(object): SsidDetails, property of the
                request body.
            ssidType(string): SSID Type, property of the request
                body. Available values are 'Guest' and
                'Enterprise'.
            vlanAndDynamicInterfaceDetails(object): VLAN And Dynamic
                Interface Details, property of the
                request body.
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
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
            'managedAPLocations':
                managedAPLocations,
            'ssidDetails':
                ssidDetails,
            'ssidType':
                ssidType,
            'enableFabric':
                enableFabric,
            'flexConnect':
                flexConnect,
            'vlanAndDynamicInterfaceDetails':
                vlanAndDynamicInterfaceDetails,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_db9f997f4e59aec1_v1_2_10')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/ssid')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload)

        return self._object_factory('bpm_db9f997f4e59aec1_v1_2_10', json_data)

    def delete_enterprise_ssid(self,
                               ssid_name,
                               headers=None,
                               **request_parameters):
        """**Beta** - Deletes given enterprise SSID.

        Args:
            ssid_name(basestring): Enter the SSID name to be
                deleted.
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
        check_type(ssid_name, basestring,
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
            'ssidName': ssid_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/enterprise-ssid/${ssidName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=params)

        return self._object_factory('bpm_c7a6592b4b98a369_v1_2_10', json_data)

    def get_enterprise_ssid(self,
                            ssid_name=None,
                            headers=None,
                            **request_parameters):
        """**Beta** - Gets either one or all the enterprise SSID.

        Args:
            ssid_name(basestring): Enter the enterprise SSID name
                that needs to be retrieved. If not
                entered, all the enterprise SSIDs will
                be retrieved.
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
        check_type(ssid_name, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'ssidName':
                ssid_name,
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

        e_url = ('/dna/intent/api/v1/enterprise-ssid')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_cca519ba45ebb423_v1_2_10', json_data)

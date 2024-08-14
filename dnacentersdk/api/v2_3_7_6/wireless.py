# -*- coding: utf-8 -*-
"""Cisco DNA Center Wireless API wrapper.

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


class Wireless(object):
    """Cisco DNA Center Wireless API (version: 2.3.7.6).

    Wraps the DNA Center Wireless
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Wireless
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Wireless, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def sensor_test_results(self,
                            end_time=None,
                            site_id=None,
                            start_time=None,
                            test_failure_by=None,
                            headers=None,
                            **request_parameters):
        """Intent API to get SENSOR test result summary .

        Args:
            site_id(str): siteId query parameter. Assurance site UUID .
            start_time(int): startTime query parameter. The epoch time in milliseconds .
            end_time(int): endTime query parameter. The epoch time in milliseconds .
            test_failure_by(str): testFailureBy query parameter. Obtain failure statistics group by "area",
                "building", or "floor" (case insensitive) .
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
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(test_failure_by, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteId':
                site_id,
            'startTime':
                start_time,
            'endTime':
                end_time,
            'testFailureBy':
                test_failure_by,
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

        e_url = ('/dna/intent/api/v1/AssuranceGetSensorTestResults')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dde2b077d6d052dcae5a76f4aac09c1d_v2_3_7_6', json_data)

    def create_and_provision_ssid(self,
                                  enableFabric=None,
                                  flexConnect=None,
                                  managedAPLocations=None,
                                  ssidDetails=None,
                                  ssidType=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Creates SSID, updates the SSID to the corresponding site profiles and provision it to the devices matching the
        given sites .

        Args:
            enableFabric(boolean): Wireless's Enable SSID for Fabric .
            flexConnect(object): Wireless's flexConnect.
            managedAPLocations(list): Wireless's Managed AP Locations (Enter entire Site(s) hierarchy)  (list of
                strings).
            ssidDetails(object): Wireless's ssidDetails.
            ssidType(string): Wireless's SSID Type . Available values are 'Guest' and 'Enterprise'.
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
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d825ae9a117f5b6bb65b7d78fd42513c_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/ssid')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d825ae9a117f5b6bb65b7d78fd42513c_v2_3_7_6', json_data)

    def delete_ssid_and_provision_it_to_devices(self,
                                                managed_aplocations,
                                                ssid_name,
                                                headers=None,
                                                **request_parameters):
        """Removes SSID or WLAN from the network profile, reprovision the device(s) and deletes the SSID or WLAN from DNA
        Center .

        Args:
            ssid_name(str): ssidName path parameter. SSID Name. This parameter needs to be encoded as per
                UTF-8 encoding. .
            managed_aplocations(str): managedAPLocations path parameter. List of managed AP locations (Site
                Hierarchies). This parameter needs to be encoded as per UTF-8 encoding .
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
        check_type(ssid_name, str,
                   may_be_none=False)
        check_type(managed_aplocations, str,
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
            'ssidName': ssid_name,
            'managedAPLocations': managed_aplocations,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/ssid/{ssidName}/{managedAPLo'
                 + 'cations}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e56eb2c294159d891b7dbe493ddc434_v2_3_7_6', json_data)

    def reboot_access_points(self,
                             apMacAddresses=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **request_parameters):
        """Users can reboot multiple access points up-to 200 at a time using this API .

        Args:
            apMacAddresses(list): Wireless's The ethernet MAC address of the access point.  (list of strings).
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
                           str)
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
            'apMacAddresses':
                apMacAddresses,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f5602b2965e53b5bdda193025a3fc_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/device-reboot/apreboot')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f5602b2965e53b5bdda193025a3fc_v2_3_7_6', json_data)

    def get_access_point_reboot_task_result(self,
                                            parent_task_id=None,
                                            headers=None,
                                            **request_parameters):
        """Users can query the access point reboot status using this intent API .

        Args:
            parent_task_id(str): parentTaskId query parameter. task id of ap reboot request .
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
        check_type(parent_task_id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'parentTaskId':
                parent_task_id,
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

        e_url = ('/dna/intent/api/v1/device-reboot/apreboot/status')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ebabf7f1ce2537f8aedd93e5f5aab1b_v2_3_7_6', json_data)

    def get_enterprise_ssid(self,
                            ssid_name=None,
                            headers=None,
                            **request_parameters):
        """Gets either one or all the enterprise SSID .

        Args:
            ssid_name(str): ssidName query parameter. Enter the enterprise SSID name that needs to be
                retrieved. If not entered, all the enterprise SSIDs will be retrieved. .
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
        check_type(ssid_name, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'ssidName':
                ssid_name,
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

        e_url = ('/dna/intent/api/v1/enterprise-ssid')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fb757e8fce4b51ffa0ba1a8e5ae4d8c0_v2_3_7_6', json_data)

    def create_enterprise_ssid(self,
                               aaaOverride=None,
                               authKeyMgmt=None,
                               basicServiceSetClientIdleTimeout=None,
                               clientExclusionTimeout=None,
                               clientRateLimit=None,
                               coverageHoleDetectionEnable=None,
                               enableBasicServiceSetMaxIdle=None,
                               enableBroadcastSSID=None,
                               enableClientExclusion=None,
                               enableDirectedMulticastService=None,
                               enableFastLane=None,
                               enableMACFiltering=None,
                               enableNeighborList=None,
                               enableSessionTimeOut=None,
                               fastTransition=None,
                               ghz24Policy=None,
                               ghz6PolicyClientSteering=None,
                               mfpClientProtection=None,
                               multiPSKSettings=None,
                               name=None,
                               nasOptions=None,
                               passphrase=None,
                               policyProfileName=None,
                               profileName=None,
                               protectedManagementFrame=None,
                               radioPolicy=None,
                               rsnCipherSuiteCcmp256=None,
                               rsnCipherSuiteGcmp128=None,
                               rsnCipherSuiteGcmp256=None,
                               securityLevel=None,
                               sessionTimeOut=None,
                               trafficType=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Creates enterprise SSID .

        Args:
            aaaOverride(boolean): Wireless's Aaa Override .
            authKeyMgmt(list): Wireless's Takes string inputs for the AKMs that should be set true. Possible AKM
                values : dot1x,dot1x_ft, dot1x_sha, psk, psk_ft, psk_sha, owe, sae, sae_ft  (list of
                strings).
            basicServiceSetClientIdleTimeout(integer): Wireless's Basic Service Set Client Idle Timeout (Default:300
                if enableBasicServiceSetMaxIdle is true, 0 otherwise) .
            clientExclusionTimeout(integer): Wireless's Client Exclusion Timeout(Default: 180 if
                enableClientExclusion is true, 0 otherwise) .
            clientRateLimit(number): Wireless's Client Rate Limit (in bits per second) .
            coverageHoleDetectionEnable(boolean): Wireless's Coverage Hole Detection Enable .
            enableBasicServiceSetMaxIdle(boolean): Wireless's Enable Basic Service Set Max Idle (Default: true) .
            enableBroadcastSSID(boolean): Wireless's Enable Broadcase SSID  .
            enableClientExclusion(boolean): Wireless's Enable Client Exclusion(Default: true) .
            enableDirectedMulticastService(boolean): Wireless's Enable Directed Multicast Service .
            enableFastLane(boolean): Wireless's Enable FastLane .
            enableMACFiltering(boolean): Wireless's Enable MAC Filtering .
            enableNeighborList(boolean): Wireless's Enable Neighbor List .
            enableSessionTimeOut(boolean): Wireless's Enable Session Timeout(Default: true) .
            fastTransition(string): Wireless's Fast Transition . Available values are 'Adaptive', 'Enable' and
                'Disable'.
            ghz24Policy(string): Wireless's Ghz24 Policy . Available values are 'dot11-g-only' and 'dot11-bg-only'.
            ghz6PolicyClientSteering(boolean): Wireless's Ghz6 Policy Client Steering .
            mfpClientProtection(string): Wireless's Management Frame Protection Client . Available values are
                'Optional', 'Disabled' and 'Required'.
            multiPSKSettings(list): Wireless's multiPSKSettings (list of objects).
            name(string): Wireless's SSID NAME .
            nasOptions(list): Wireless's Nas Options  (list of strings).
            passphrase(string): Wireless's Passphrase .
            policyProfileName(string): Wireless's Policy Profile Name .
            profileName(string): Wireless's Profile Name .
            protectedManagementFrame(string): Wireless's (Required applicable for Security Type WPA3_PERSONAL,
                WPA3_ENTERPRISE, OPEN_SECURED) and (Optional, Required Applicable for Security Type
                WPA2_WPA3_PERSONAL and WPA2_WPA3_ENTERPRISE) . Available values are 'Optional',
                'Disabled' and 'Required'.
            radioPolicy(string): Wireless's Radio Policy Enum  . Available values are 'Triple band operation(2.4GHz,
                5GHz and 6GHz)', '5GHz only', '2.4GHz only', '6GHz only', '2.4 and 5 GHz', '2.4 and 6
                GHz' and '5 and 6 GHz'.
            rsnCipherSuiteCcmp256(boolean): Wireless's Rsn Cipher Suite Ccmp256 .
            rsnCipherSuiteGcmp128(boolean): Wireless's Rsn Cipher Suite Gcmp 128 .
            rsnCipherSuiteGcmp256(boolean): Wireless's Rsn Cipher Suite Gcmp256 .
            securityLevel(string): Wireless's Security Level . Available values are 'WPA2_ENTERPRISE',
                'WPA2_PERSONAL', 'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL', 'WPA2_WPA3_PERSONAL' and
                'WPA2_WPA3_ENTERPRISE'.
            sessionTimeOut(integer): Wireless's Session Time Out (Default: 1800 if enableSessionTimeOut is true, 0
                otherwise) .
            trafficType(string): Wireless's Traffic Type Enum (voicedata or data ) . Available values are
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
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

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
            'enableSessionTimeOut':
                enableSessionTimeOut,
            'sessionTimeOut':
                sessionTimeOut,
            'enableClientExclusion':
                enableClientExclusion,
            'clientExclusionTimeout':
                clientExclusionTimeout,
            'enableBasicServiceSetMaxIdle':
                enableBasicServiceSetMaxIdle,
            'basicServiceSetClientIdleTimeout':
                basicServiceSetClientIdleTimeout,
            'enableDirectedMulticastService':
                enableDirectedMulticastService,
            'enableNeighborList':
                enableNeighborList,
            'mfpClientProtection':
                mfpClientProtection,
            'nasOptions':
                nasOptions,
            'profileName':
                profileName,
            'policyProfileName':
                policyProfileName,
            'aaaOverride':
                aaaOverride,
            'coverageHoleDetectionEnable':
                coverageHoleDetectionEnable,
            'protectedManagementFrame':
                protectedManagementFrame,
            'multiPSKSettings':
                multiPSKSettings,
            'clientRateLimit':
                clientRateLimit,
            'authKeyMgmt':
                authKeyMgmt,
            'rsnCipherSuiteGcmp256':
                rsnCipherSuiteGcmp256,
            'rsnCipherSuiteCcmp256':
                rsnCipherSuiteCcmp256,
            'rsnCipherSuiteGcmp128':
                rsnCipherSuiteGcmp128,
            'ghz6PolicyClientSteering':
                ghz6PolicyClientSteering,
            'ghz24Policy':
                ghz24Policy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_bc33daf690ec5399a507829abfc4fe64_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/enterprise-ssid')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_bc33daf690ec5399a507829abfc4fe64_v2_3_7_6', json_data)

    def update_enterprise_ssid(self,
                               aaaOverride=None,
                               authKeyMgmt=None,
                               basicServiceSetClientIdleTimeout=None,
                               clientExclusionTimeout=None,
                               clientRateLimit=None,
                               coverageHoleDetectionEnable=None,
                               enableBasicServiceSetMaxIdle=None,
                               enableBroadcastSSID=None,
                               enableClientExclusion=None,
                               enableDirectedMulticastService=None,
                               enableFastLane=None,
                               enableMACFiltering=None,
                               enableNeighborList=None,
                               enableSessionTimeOut=None,
                               fastTransition=None,
                               ghz24Policy=None,
                               ghz6PolicyClientSteering=None,
                               mfpClientProtection=None,
                               multiPSKSettings=None,
                               name=None,
                               nasOptions=None,
                               passphrase=None,
                               policyProfileName=None,
                               profileName=None,
                               protectedManagementFrame=None,
                               radioPolicy=None,
                               rsnCipherSuiteCcmp256=None,
                               rsnCipherSuiteGcmp128=None,
                               rsnCipherSuiteGcmp256=None,
                               securityLevel=None,
                               sessionTimeOut=None,
                               trafficType=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Update enterprise SSID .

        Args:
            aaaOverride(boolean): Wireless's Aaa Override .
            authKeyMgmt(list): Wireless's Takes string inputs for the AKMs that should be set true. Possible AKM
                values : dot1x,dot1x_ft, dot1x_sha, psk, psk_ft, psk_sha, owe, sae, sae_ft  (list of
                strings).
            basicServiceSetClientIdleTimeout(integer): Wireless's Basic Service Set Client Idle Timeout (Default:300
                if enableBasicServiceSetMaxIdle is true, 0 otherwise) .
            clientExclusionTimeout(integer): Wireless's Client Exclusion Timeout(Default: 180 if
                enableClientExclusion is true, 0 otherwise) .
            clientRateLimit(number): Wireless's Client Rate Limit (in bits per second) .
            coverageHoleDetectionEnable(boolean): Wireless's Coverage Hole Detection Enable .
            enableBasicServiceSetMaxIdle(boolean): Wireless's Enable Basic Service Set Max Idle (Default: true) .
            enableBroadcastSSID(boolean): Wireless's Enable Broadcase SSID  .
            enableClientExclusion(boolean): Wireless's Enable Client Exclusion(Default: true) .
            enableDirectedMulticastService(boolean): Wireless's Enable Directed Multicast Service .
            enableFastLane(boolean): Wireless's Enable FastLane .
            enableMACFiltering(boolean): Wireless's Enable MAC Filtering .
            enableNeighborList(boolean): Wireless's Enable Neighbor List .
            enableSessionTimeOut(boolean): Wireless's Enable Session Timeout(Default: true) .
            fastTransition(string): Wireless's Fast Transition . Available values are 'Adaptive', 'Enable' and
                'Disable'.
            ghz24Policy(string): Wireless's Ghz24 Policy . Available values are 'dot11-g-only' and 'dot11-bg-only'.
            ghz6PolicyClientSteering(boolean): Wireless's Ghz6 Policy Client Steering .
            mfpClientProtection(string): Wireless's Management Frame Protection Client . Available values are
                'Optional', 'Disabled' and 'Required'.
            multiPSKSettings(list): Wireless's multiPSKSettings (list of objects).
            name(string): Wireless's SSID NAME .
            nasOptions(list): Wireless's Nas Options  (list of strings).
            passphrase(string): Wireless's Passphrase .
            policyProfileName(string): Wireless's Policy Profile Name .
            profileName(string): Wireless's Profile Name .
            protectedManagementFrame(string): Wireless's (Required applicable for Security Type WPA3_PERSONAL,
                WPA3_ENTERPRISE, OPEN_SECURED) and (Optional, Required Applicable for Security Type
                WPA2_WPA3_PERSONAL and WPA2_WPA3_ENTERPRISE) . Available values are 'Optional',
                'Disabled' and 'Required'.
            radioPolicy(string): Wireless's Radio Policy Enum  . Available values are 'Triple band operation(2.4GHz,
                5GHz and 6GHz)', '5GHz only', '2.4GHz only', '6GHz only', '2.4 and 5 GHz', '2.4 and 6
                GHz' and '5 and 6 GHz'.
            rsnCipherSuiteCcmp256(boolean): Wireless's Rsn Cipher Suite Ccmp256 .
            rsnCipherSuiteGcmp128(boolean): Wireless's Rsn Cipher Suite Gcmp 128 .
            rsnCipherSuiteGcmp256(boolean): Wireless's Rsn Cipher Suite Gcmp256 .
            securityLevel(string): Wireless's Security Level . Available values are 'WPA2_ENTERPRISE',
                'WPA2_PERSONAL', 'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL', 'WPA2_WPA3_PERSONAL' and
                'WPA2_WPA3_ENTERPRISE'.
            sessionTimeOut(integer): Wireless's Session Time Out (Default: 1800 if enableSessionTimeOut is true, 0
                otherwise) .
            trafficType(string): Wireless's Traffic Type Enum (voicedata or data ) . Available values are
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
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

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
            'enableSessionTimeOut':
                enableSessionTimeOut,
            'sessionTimeOut':
                sessionTimeOut,
            'enableClientExclusion':
                enableClientExclusion,
            'clientExclusionTimeout':
                clientExclusionTimeout,
            'enableBasicServiceSetMaxIdle':
                enableBasicServiceSetMaxIdle,
            'basicServiceSetClientIdleTimeout':
                basicServiceSetClientIdleTimeout,
            'enableDirectedMulticastService':
                enableDirectedMulticastService,
            'enableNeighborList':
                enableNeighborList,
            'mfpClientProtection':
                mfpClientProtection,
            'nasOptions':
                nasOptions,
            'profileName':
                profileName,
            'policyProfileName':
                policyProfileName,
            'aaaOverride':
                aaaOverride,
            'coverageHoleDetectionEnable':
                coverageHoleDetectionEnable,
            'protectedManagementFrame':
                protectedManagementFrame,
            'multiPSKSettings':
                multiPSKSettings,
            'clientRateLimit':
                clientRateLimit,
            'authKeyMgmt':
                authKeyMgmt,
            'rsnCipherSuiteGcmp256':
                rsnCipherSuiteGcmp256,
            'rsnCipherSuiteCcmp256':
                rsnCipherSuiteCcmp256,
            'rsnCipherSuiteGcmp128':
                rsnCipherSuiteGcmp128,
            'ghz6PolicyClientSteering':
                ghz6PolicyClientSteering,
            'ghz24Policy':
                ghz24Policy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a94058a99acaaf8eb73c9227_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/enterprise-ssid')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_a94058a99acaaf8eb73c9227_v2_3_7_6', json_data)

    def delete_enterprise_ssid(self,
                               ssid_name,
                               headers=None,
                               **request_parameters):
        """Deletes given enterprise SSID .

        Args:
            ssid_name(str): ssidName path parameter. Enter the SSID name to be deleted .
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
        check_type(ssid_name, str,
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
            'ssidName': ssid_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/enterprise-ssid/{ssidName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a43afa4d91a5043996c682a7a7a2d62_v2_3_7_6', json_data)

    def delete_wireless_profile(self,
                                wireless_profile_name,
                                headers=None,
                                **request_parameters):
        """Delete the Wireless Profile from Cisco DNA Center whose name is provided. .

        Args:
            wireless_profile_name(str): wirelessProfileName path parameter. Wireless Profile Name .
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
        check_type(wireless_profile_name, str,
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
            'wirelessProfileName': wireless_profile_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wireless-'
                 + 'profile/{wirelessProfileName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a850fb6c5451a7ad20ba76f4ff43_v2_3_7_6', json_data)

    def configure_access_points_v1(self,
                                   adminStatus=None,
                                   apList=None,
                                   apMode=None,
                                   configureAdminStatus=None,
                                   configureApMode=None,
                                   configureFailoverPriority=None,
                                   configureHAController=None,
                                   configureLedBrightnessLevel=None,
                                   configureLedStatus=None,
                                   configureLocation=None,
                                   failoverPriority=None,
                                   isAssignedSiteAsLocation=None,
                                   ledBrightnessLevel=None,
                                   ledStatus=None,
                                   location=None,
                                   primaryControllerName=None,
                                   primaryIpAddress=None,
                                   radioConfigurations=None,
                                   secondaryControllerName=None,
                                   secondaryIpAddress=None,
                                   tertiaryControllerName=None,
                                   tertiaryIpAddress=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """User can configure multiple access points with required options using this intent API. This API does not support
        configuration of CleanAir or SI for IOS-XE devices with version greater than or equal to 17.9 .

        Args:
            adminStatus(boolean): Wireless's Configure the access point's admin status. Set this parameter's value
                to "true" to enable it and "false" to disable it. .
            apList(list): Wireless's apList (list of objects).
            apMode(integer): Wireless's Configure the access point's mode: for local/flexconnect mode, set "0"; for
                monitor mode, set "1"; for sniffer mode, set "4"; and for bridge/flex+bridge mode, set
                "5". .
            configureAdminStatus(boolean): Wireless's To change the access point's admin status, set this
                parameter's value to "true". .
            configureApMode(boolean): Wireless's To change the access point's mode, set this parameter's value to
                "true". .
            configureFailoverPriority(boolean): Wireless's To change the access point's failover priority, set this
                parameter's value to "true". .
            configureHAController(boolean): Wireless's To change the access point's HA controller, set this
                parameter's value to "true". .
            configureLedBrightnessLevel(boolean): Wireless's To change the access point's LED brightness level, set
                this parameter's value to "true". .
            configureLedStatus(boolean): Wireless's To change the access point's LED status, set this parameter's
                value to "true". .
            configureLocation(boolean): Wireless's To change the access point's location, set this parameter's value
                to "true". .
            failoverPriority(integer): Wireless's Configure the acess point's failover priority: for low, set "1";
                for medium, set "2"; for high, set "3"; and for critical, set "4". .
            isAssignedSiteAsLocation(boolean): Wireless's If AP is assigned to a site, then to assign AP location as
                the site name, set this parameter's value to "true". .
            ledBrightnessLevel(integer): Wireless's Configure the access point's LED brightness level by setting a
                value between 1 and 8. .
            ledStatus(boolean): Wireless's Configure the access point's LED status. Set "true" to enable its status
                and "false" to disable it. .
            location(string): Wireless's Configure the access point's location. .
            primaryControllerName(string): Wireless's Configure the hostname for an access point's primary
                controller. .
            primaryIpAddress(object): Wireless's primaryIpAddress.
            radioConfigurations(list): Wireless's radioConfigurations (list of objects).
            secondaryControllerName(string): Wireless's Configure the hostname for an access point's secondary
                controller. .
            secondaryIpAddress(object): Wireless's secondaryIpAddress.
            tertiaryControllerName(string): Wireless's Configure the hostname for an access point's tertiary
                controller. .
            tertiaryIpAddress(object): Wireless's tertiaryIpAddress.
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
                           str)
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
            'apList':
                apList,
            'configureAdminStatus':
                configureAdminStatus,
            'adminStatus':
                adminStatus,
            'configureApMode':
                configureApMode,
            'apMode':
                apMode,
            'configureFailoverPriority':
                configureFailoverPriority,
            'failoverPriority':
                failoverPriority,
            'configureLedStatus':
                configureLedStatus,
            'ledStatus':
                ledStatus,
            'configureLedBrightnessLevel':
                configureLedBrightnessLevel,
            'ledBrightnessLevel':
                ledBrightnessLevel,
            'configureLocation':
                configureLocation,
            'location':
                location,
            'configureHAController':
                configureHAController,
            'primaryControllerName':
                primaryControllerName,
            'primaryIpAddress':
                primaryIpAddress,
            'secondaryControllerName':
                secondaryControllerName,
            'secondaryIpAddress':
                secondaryIpAddress,
            'tertiaryControllerName':
                tertiaryControllerName,
            'tertiaryIpAddress':
                tertiaryIpAddress,
            'radioConfigurations':
                radioConfigurations,
            'isAssignedSiteAsLocation':
                isAssignedSiteAsLocation,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e0bd567c1395531a7f18ab4e14110bd_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wireless/accesspoint-configuration')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e0bd567c1395531a7f18ab4e14110bd_v2_3_7_6', json_data)

    def get_access_point_configuration_task_result(self,
                                                   task_id,
                                                   headers=None,
                                                   **request_parameters):
        """Users can query the access point configuration result using this intent API .

        Args:
            task_id(str): task_id path parameter. task id information of ap config .
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
        check_type(task_id, str,
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
            'task_id': task_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wireless/accesspoint-'
                 + 'configuration/details/{task_id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cc2c3a5b75a4091350fa84ac872c9_v2_3_7_6', json_data)

    def get_access_point_configuration(self,
                                       key,
                                       headers=None,
                                       **request_parameters):
        """Users can query the access point configuration information per device using the ethernet MAC address .

        Args:
            key(str): key query parameter. The ethernet MAC address of Access point .
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
        check_type(key, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'key':
                key,
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

        e_url = ('/dna/intent/api/v1/wireless/accesspoint-'
                 + 'configuration/summary')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fb7514b0e8c52be8cfd19dab5e31b06_v2_3_7_6', json_data)

    def ap_provision(self,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **request_parameters):
        """Access Point Provision and ReProvision  .

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
            if '__persistbapioutput' in headers:
                check_type(headers.get('__persistbapioutput'),
                           str)
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
            self._request_validator('jsd_f790a930d452708353c374f5c0f90f_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wireless/ap-provision')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f790a930d452708353c374f5c0f90f_v2_3_7_6', json_data)

    def delete_dynamic_interface(self,
                                 interface_name,
                                 headers=None,
                                 **request_parameters):
        """Delete a dynamic interface .

        Args:
            interface_name(str): interfaceName query parameter. valid interface-name to be deleted .
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
        check_type(interface_name, str,
                   may_be_none=False)
        if headers is not None:
            if '__runsync' in headers:
                check_type(headers.get('__runsync'),
                           bool)
            if '__timeout' in headers:
                check_type(headers.get('__timeout'),
                           int)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
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

        e_url = ('/dna/intent/api/v1/wireless/dynamic-interface')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ed6ee6a19c5e7da1606b05b7188964_v2_3_7_6', json_data)

    def create_update_dynamic_interface(self,
                                        interfaceName=None,
                                        vlanId=None,
                                        headers=None,
                                        payload=None,
                                        active_validation=True,
                                        **request_parameters):
        """API to create or update an dynamic interface .

        Args:
            interfaceName(string): Wireless's dynamic-interface name .
            vlanId(number): Wireless's Vlan Id .
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
            'interfaceName':
                interfaceName,
            'vlanId':
                vlanId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_c00df3623b5a74ad41e75487ed9b77_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wireless/dynamic-interface')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_c00df3623b5a74ad41e75487ed9b77_v2_3_7_6', json_data)

    def get_dynamic_interface(self,
                              interface_name=None,
                              headers=None,
                              **request_parameters):
        """Get one or all dynamic interface(s) .

        Args:
            interface_name(str): interface-name query parameter. dynamic-interface name, if not specified all
                the existing dynamic interfaces will be retrieved .
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
        check_type(interface_name, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'interface-name':
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

        e_url = ('/dna/intent/api/v1/wireless/dynamic-interface')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c9fb8b0f5c69ba22f920e4044538_v2_3_7_6', json_data)

    def update_wireless_profile(self,
                                profileDetails=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **request_parameters):
        """Updates the wireless Network Profile with updated details provided. All sites to be present in the network
        profile should be provided. This API has been deprecated. Please use the new endpoint URL:
        /dna/intent/api/v2/wireless/profile. .

        Args:
            profileDetails(object): Wireless's profileDetails.
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
            'profileDetails':
                profileDetails,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_bbf7ce025bc2a291b90c37a6b898_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wireless/profile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_bbf7ce025bc2a291b90c37a6b898_v2_3_7_6', json_data)

    def create_wireless_profile(self,
                                profileDetails=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **request_parameters):
        """Creates Wireless Network Profile on Cisco DNA Center and associates sites and SSIDs to it. .

        Args:
            profileDetails(object): Wireless's profileDetails.
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
            'profileDetails':
                profileDetails,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_b95201b6a6905a10b463e036bf591166_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wireless/profile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_b95201b6a6905a10b463e036bf591166_v2_3_7_6', json_data)

    def get_wireless_profile(self,
                             profile_name=None,
                             headers=None,
                             **request_parameters):
        """Gets either one or all the wireless network profiles if no name is provided for network-profile. .

        Args:
            profile_name(str): profileName query parameter. Wireless Network Profile Name .
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
        check_type(profile_name, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'profileName':
                profile_name,
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

        e_url = ('/dna/intent/api/v1/wireless/profile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bbc1866a50505c0695ae243718d51936_v2_3_7_6', json_data)

    def provision_update(self,
                         headers=None,
                         payload=None,
                         active_validation=True,
                         **request_parameters):
        """Updates wireless provisioning .

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
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_d0aab00569b258b481afedc35e6db392_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wireless/provision')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_d0aab00569b258b481afedc35e6db392_v2_3_7_6', json_data)

    def provision(self,
                  headers=None,
                  payload=None,
                  active_validation=True,
                  **request_parameters):
        """Provision wireless devices .

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
            self._request_validator('jsd_e31c795964b3bdf85da1b5a2a5_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wireless/provision')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e31c795964b3bdf85da1b5a2a5_v2_3_7_6', json_data)

    def psk_override(self,
                     passPhrase=None,
                     site=None,
                     ssidName=None,
                     wlanProfileName=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **request_parameters):
        """Update/override pass phrase of enterprise SSID .

        Args:
            passPhrase(string): Wireless's Pass phrase (create/update) .
            site(string): Wireless's site name hierarchy (ex: Global/aaa/zzz/...)  .
            ssidName(string): Wireless's Enterprise SSID Name(already created/present) .
            wlanProfileName(string): Wireless's WLAN Profile Name .
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
            'ssidName':
                ssidName,
            'site':
                site,
            'passPhrase':
                passPhrase,
            'wlanProfileName':
                wlanProfileName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f99c96c3a9b45ddaabc2c75ff8efa67f_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wireless/psk-override')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f99c96c3a9b45ddaabc2c75ff8efa67f_v2_3_7_6', json_data)

    def retrieve_rf_profiles(self,
                             rf_profile_name=None,
                             headers=None,
                             **request_parameters):
        """Retrieve all RF profiles .

        Args:
            rf_profile_name(str): rf-profile-name query parameter. RF Profile Name .
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
        check_type(rf_profile_name, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'rf-profile-name':
                rf_profile_name,
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

        e_url = ('/dna/intent/api/v1/wireless/rf-profile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ac37d6798c0b593088952123df03bb1b_v2_3_7_6', json_data)

    def create_or_update_rf_profile(self,
                                    channelWidth=None,
                                    defaultRfProfile=None,
                                    enableBrownField=None,
                                    enableCustom=None,
                                    enableRadioTypeA=None,
                                    enableRadioTypeB=None,
                                    enableRadioTypeC=None,
                                    name=None,
                                    radioTypeAProperties=None,
                                    radioTypeBProperties=None,
                                    radioTypeCProperties=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **request_parameters):
        """Create or Update RF profile .

        Args:
            channelWidth(string): Wireless's Channel Width .
            defaultRfProfile(boolean): Wireless's Default Rf Profile .
            enableBrownField(boolean): Wireless's Enable Brown Field .
            enableCustom(boolean): Wireless's Enable Custom .
            enableRadioTypeA(boolean): Wireless's Enable Radio Type A .
            enableRadioTypeB(boolean): Wireless's Enable Radio Type B .
            enableRadioTypeC(boolean): Wireless's Enable Radio Type C (6GHz) .
            name(string): Wireless's RF Profile Name .
            radioTypeAProperties(object): Wireless's radioTypeAProperties.
            radioTypeBProperties(object): Wireless's radioTypeBProperties.
            radioTypeCProperties(object): Wireless's radioTypeCProperties.
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
            'name':
                name,
            'defaultRfProfile':
                defaultRfProfile,
            'enableRadioTypeA':
                enableRadioTypeA,
            'enableRadioTypeB':
                enableRadioTypeB,
            'channelWidth':
                channelWidth,
            'enableCustom':
                enableCustom,
            'enableBrownField':
                enableBrownField,
            'radioTypeAProperties':
                radioTypeAProperties,
            'radioTypeBProperties':
                radioTypeBProperties,
            'radioTypeCProperties':
                radioTypeCProperties,
            'enableRadioTypeC':
                enableRadioTypeC,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f24f6c07641580ba6ed710e92c2da16_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wireless/rf-profile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f24f6c07641580ba6ed710e92c2da16_v2_3_7_6', json_data)

    def delete_rf_profiles(self,
                           rf_profile_name,
                           headers=None,
                           **request_parameters):
        """Delete RF profile(s) .

        Args:
            rf_profile_name(str): rfProfileName path parameter. RF profile name to be deleted(required) *non-
                custom RF profile cannot be deleted .
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
        check_type(rf_profile_name, str,
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
            'rfProfileName': rf_profile_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wireless/rf-profile/{rfProfileName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f3790386da5cd49480cb0503e59047_v2_3_7_6', json_data)

    def configure_access_points_v2(self,
                                   adminStatus=None,
                                   apList=None,
                                   apMode=None,
                                   cleanAirSI24=None,
                                   cleanAirSI5=None,
                                   cleanAirSI6=None,
                                   configureAdminStatus=None,
                                   configureApMode=None,
                                   configureCleanAirSI24Ghz=None,
                                   configureCleanAirSI5Ghz=None,
                                   configureCleanAirSI6Ghz=None,
                                   configureFailoverPriority=None,
                                   configureHAController=None,
                                   configureLedBrightnessLevel=None,
                                   configureLedStatus=None,
                                   configureLocation=None,
                                   failoverPriority=None,
                                   isAssignedSiteAsLocation=None,
                                   ledBrightnessLevel=None,
                                   ledStatus=None,
                                   location=None,
                                   primaryControllerName=None,
                                   primaryIpAddress=None,
                                   radioConfigurations=None,
                                   secondaryControllerName=None,
                                   secondaryIpAddress=None,
                                   tertiaryControllerName=None,
                                   tertiaryIpAddress=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """User can configure multiple access points with required options using this intent API .

        Args:
            adminStatus(boolean): Wireless's Configure the access point's admin status. Set this parameter's value
                to "true" to enable it and "false" to disable it. .
            apList(list): Wireless's apList (list of objects).
            apMode(integer): Wireless's Configure the access point's mode: for local/flexconnect mode, set "0"; for
                monitor mode, set "1"; for sniffer mode, set "4"; and for bridge/flex+bridge mode, set
                "5". .
            cleanAirSI24(boolean): Wireless's Configure clean air status for radios that are in 2.4 Ghz band. Set
                this parameter's value to "true" to enable it and "false" to disable it. .
            cleanAirSI5(boolean): Wireless's Configure clean air status for radios that are in 5 Ghz band. Set this
                parameter's value to "true" to enable it and "false" to disable it. .
            cleanAirSI6(boolean): Wireless's Configure clean air status for radios that are in 6 Ghz band. Set this
                parameter's value to "true" to enable it and "false" to disable it. .
            configureAdminStatus(boolean): Wireless's To change the access point's admin status, set this
                parameter's value to "true". .
            configureApMode(boolean): Wireless's To change the access point's mode, set this parameter's value to
                "true". .
            configureCleanAirSI24Ghz(boolean): Wireless's To change the clean air status for radios that are in 2.4
                Ghz band, set this parameter's value to "true". .
            configureCleanAirSI5Ghz(boolean): Wireless's To change the clean air status for radios that are in 5 Ghz
                band, set this parameter's value to "true". .
            configureCleanAirSI6Ghz(boolean): Wireless's To change the clean air status for radios that are in 6 Ghz
                band, set this parameter's value to "true". .
            configureFailoverPriority(boolean): Wireless's To change the access point's failover priority, set this
                parameter's value to "true". .
            configureHAController(boolean): Wireless's To change the access point's HA controller, set this
                parameter's value to "true". .
            configureLedBrightnessLevel(boolean): Wireless's To change the access point's LED brightness level, set
                this parameter's value to "true". .
            configureLedStatus(boolean): Wireless's To change the access point's LED status, set this parameter's
                value to "true". .
            configureLocation(boolean): Wireless's To change the access point's location, set this parameter's value
                to "true". .
            failoverPriority(integer): Wireless's Configure the acess point's failover priority: for low, set "1";
                for medium, set "2"; for high, set "3"; and for critical, set "4". .
            isAssignedSiteAsLocation(boolean): Wireless's To configure the access point's location as the site
                assigned to the access point, set this parameter's value to "true". .
            ledBrightnessLevel(integer): Wireless's Configure the access point's LED brightness level by setting a
                value between 1 and 8. .
            ledStatus(boolean): Wireless's Configure the access point's LED status. Set "true" to enable its status
                and "false" to disable it. .
            location(string): Wireless's Configure the access point's location. .
            primaryControllerName(string): Wireless's Configure the hostname for an access point's primary
                controller. .
            primaryIpAddress(object): Wireless's primaryIpAddress.
            radioConfigurations(list): Wireless's radioConfigurations (list of objects).
            secondaryControllerName(string): Wireless's Configure the hostname for an access point's secondary
                controller. .
            secondaryIpAddress(object): Wireless's secondaryIpAddress.
            tertiaryControllerName(string): Wireless's Configure the hostname for an access point's tertiary
                controller. .
            tertiaryIpAddress(object): Wireless's tertiaryIpAddress.
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
                           str)
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
            'apList':
                apList,
            'configureAdminStatus':
                configureAdminStatus,
            'adminStatus':
                adminStatus,
            'configureApMode':
                configureApMode,
            'apMode':
                apMode,
            'configureFailoverPriority':
                configureFailoverPriority,
            'failoverPriority':
                failoverPriority,
            'configureLedStatus':
                configureLedStatus,
            'ledStatus':
                ledStatus,
            'configureLedBrightnessLevel':
                configureLedBrightnessLevel,
            'ledBrightnessLevel':
                ledBrightnessLevel,
            'configureLocation':
                configureLocation,
            'location':
                location,
            'configureHAController':
                configureHAController,
            'primaryControllerName':
                primaryControllerName,
            'primaryIpAddress':
                primaryIpAddress,
            'secondaryControllerName':
                secondaryControllerName,
            'secondaryIpAddress':
                secondaryIpAddress,
            'tertiaryControllerName':
                tertiaryControllerName,
            'tertiaryIpAddress':
                tertiaryIpAddress,
            'radioConfigurations':
                radioConfigurations,
            'configureCleanAirSI24Ghz':
                configureCleanAirSI24Ghz,
            'cleanAirSI24':
                cleanAirSI24,
            'configureCleanAirSI5Ghz':
                configureCleanAirSI5Ghz,
            'cleanAirSI5':
                cleanAirSI5,
            'configureCleanAirSI6Ghz':
                configureCleanAirSI6Ghz,
            'cleanAirSI6':
                cleanAirSI6,
            'isAssignedSiteAsLocation':
                isAssignedSiteAsLocation,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_deb34387d0235811a90985711be9fe2e_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v2/wireless/accesspoint-configuration')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_deb34387d0235811a90985711be9fe2e_v2_3_7_6', json_data)

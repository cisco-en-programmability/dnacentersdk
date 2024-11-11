# -*- coding: utf-8 -*-
"""Cisco DNA Center Wireless API wrapper.

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

    def sensor_test_results_v1(self,
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!sensor-test-results
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

    def create_and_provision_ssid_v1(self,
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-and-provision-ssid
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

    def delete_ssid_and_provision_it_to_devices_v1(self,
                                                   managed_aplocations,
                                                   ssid_name,
                                                   headers=None,
                                                   **request_parameters):
        """Removes SSID or WLAN from the network profile, reprovision the device(s) and deletes the SSID or WLAN from DNA
        Center    .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-ssid-and-provision-it-to-devices
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

    def reboot_access_points_v1(self,
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!reboot-access-points
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

    def get_access_point_reboot_task_result_v1(self,
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-access-point-reboot-task-result
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

    def get_enterprise_ssid_v1(self,
                               ssid_name=None,
                               headers=None,
                               **request_parameters):
        """Get Enterprise SSID .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-enterprise-ssid
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

    def create_enterprise_ssid_v1(self,
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
        """Creates enterprise SSID  .

        Args:
            aaaOverride(boolean): Wireless's Aaa Override .
            authKeyMgmt(list): Wireless's Takes string inputs for the AKMs that should be set true. Possible AKM
                values : dot1x,dot1x_ft, dot1x_sha, psk, psk_ft, psk_sha, owe, sae, sae_ft  (list of
                strings).
            basicServiceSetClientIdleTimeout(integer): Wireless's Basic Service Set Client Idle Timeout .
            clientExclusionTimeout(integer): Wireless's Client Exclusion Timeout .
            clientRateLimit(number): Wireless's Client Rate Limit (in bits per second) .
            coverageHoleDetectionEnable(boolean): Wireless's Coverage Hole Detection Enable .
            enableBasicServiceSetMaxIdle(boolean): Wireless's Enable Basic Service Set Max Idle  .
            enableBroadcastSSID(boolean): Wireless's Enable Broadcase SSID  .
            enableClientExclusion(boolean): Wireless's Enable Client Exclusion .
            enableDirectedMulticastService(boolean): Wireless's Enable Directed Multicast Service .
            enableFastLane(boolean): Wireless's Enable FastLane .
            enableMACFiltering(boolean): Wireless's Enable MAC Filtering .
            enableNeighborList(boolean): Wireless's Enable Neighbor List .
            enableSessionTimeOut(boolean): Wireless's Enable Session Timeout .
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
                'WPA2_PERSONAL', 'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL', 'WPA2_WPA3_PERSONAL',
                'WPA2_WPA3_ENTERPRISE' and 'OPEN_SECURED'.
            sessionTimeOut(integer): Wireless's Session Time Out .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-enterprise-ssid
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

    def update_enterprise_ssid_v1(self,
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
        """Update enterprise SSID   .

        Args:
            aaaOverride(boolean): Wireless's Aaa Override .
            authKeyMgmt(list): Wireless's Takes string inputs for the AKMs that should be set true. Possible AKM
                values : dot1x,dot1x_ft, dot1x_sha, psk, psk_ft, psk_sha, owe, sae, sae_ft  (list of
                strings).
            basicServiceSetClientIdleTimeout(integer): Wireless's Basic Service Set Client Idle Timeout .
            clientExclusionTimeout(integer): Wireless's Client Exclusion Timeout .
            clientRateLimit(number): Wireless's Client Rate Limit (in bits per second) .
            coverageHoleDetectionEnable(boolean): Wireless's Coverage Hole Detection Enable .
            enableBasicServiceSetMaxIdle(boolean): Wireless's Enable Basic Service Set Max Idle  .
            enableBroadcastSSID(boolean): Wireless's Enable Broadcase SSID  .
            enableClientExclusion(boolean): Wireless's Enable Client Exclusion .
            enableDirectedMulticastService(boolean): Wireless's Enable Directed Multicast Service .
            enableFastLane(boolean): Wireless's Enable FastLane .
            enableMACFiltering(boolean): Wireless's Enable MAC Filtering .
            enableNeighborList(boolean): Wireless's Enable Neighbor List .
            enableSessionTimeOut(boolean): Wireless's Enable Session Timeout .
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
                'WPA2_PERSONAL', 'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL', 'WPA2_WPA3_PERSONAL',
                'WPA2_WPA3_ENTERPRISE' and 'OPEN_SECURED'.
            sessionTimeOut(integer): Wireless's Session Time Out .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-enterprise-ssid
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

    def delete_enterprise_ssid_v1(self,
                                  ssid_name,
                                  headers=None,
                                  **request_parameters):
        """Deletes given enterprise SSID    .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-enterprise-ssid
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

    def create_ssid_v1(self,
                       site_id,
                       aaaOverride=None,
                       acctServers=None,
                       aclName=None,
                       authServer=None,
                       authServers=None,
                       authType=None,
                       basicServiceSetClientIdleTimeout=None,
                       basicServiceSetMaxIdleEnable=None,
                       cckmTsfTolerance=None,
                       clientExclusionEnable=None,
                       clientExclusionTimeout=None,
                       clientRateLimit=None,
                       coverageHoleDetectionEnable=None,
                       directedMulticastServiceEnable=None,
                       egressQos=None,
                       externalAuthIpAddress=None,
                       fastTransition=None,
                       fastTransitionOverTheDistributedSystemEnable=None,
                       ghz24Policy=None,
                       ghz6PolicyClientSteering=None,
                       ingressQos=None,
                       isApBeaconProtectionEnabled=None,
                       isAuthKey8021x=None,
                       isAuthKey8021xPlusFT=None,
                       isAuthKey8021x_SHA256=None,
                       isAuthKeyEasyPSK=None,
                       isAuthKeyOWE=None,
                       isAuthKeyPSK=None,
                       isAuthKeyPSKPlusFT=None,
                       isAuthKeyPSKSHA256=None,
                       isAuthKeySae=None,
                       isAuthKeySaeExt=None,
                       isAuthKeySaeExtPlusFT=None,
                       isAuthKeySaePlusFT=None,
                       isAuthKeySuiteB1921x=None,
                       isAuthKeySuiteB1x=None,
                       isBroadcastSSID=None,
                       isCckmEnabled=None,
                       isEnabled=None,
                       isFastLaneEnabled=None,
                       isHex=None,
                       isMacFilteringEnabled=None,
                       isPosturingEnabled=None,
                       isRandomMacFilterEnabled=None,
                       l3AuthType=None,
                       managementFrameProtectionClientprotection=None,
                       multiPSKSettings=None,
                       nasOptions=None,
                       neighborListEnable=None,
                       openSsid=None,
                       passphrase=None,
                       profileName=None,
                       protectedManagementFrame=None,
                       rsnCipherSuiteCcmp128=None,
                       rsnCipherSuiteCcmp256=None,
                       rsnCipherSuiteGcmp128=None,
                       rsnCipherSuiteGcmp256=None,
                       sessionTimeOut=None,
                       sessionTimeOutEnable=None,
                       sleepingClientEnable=None,
                       sleepingClientTimeout=None,
                       ssid=None,
                       ssidRadioType=None,
                       webPassthrough=None,
                       wlanBandSelectEnable=None,
                       wlanType=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """This API allows the user to create an SSID (Service Set Identifier) at the Global site .

        Args:
            aaaOverride(boolean): Wireless's Activate the AAA Override feature when set to true .
            acctServers(list): Wireless's List of Accounting server IpAddresses  (list of strings).
            aclName(string): Wireless's Pre-Auth Access Control List (ACL) Name .
            authServer(string): Wireless's Authentication Server, Mandatory for Guest SSIDs with wlanType=Guest and
                l3AuthType=web_auth . Available values are 'auth_ise', 'auth_external' and
                'auth_internal'.
            authServers(list): Wireless's List of Authentication/Authorization server IpAddresses  (list of
                strings).
            authType(string): Wireless's L2 Authentication Type (If authType is not open , then atleast one RSN
                Cipher Suite and corresponding valid AKM must be enabled) . Available values are
                'WPA2_ENTERPRISE', 'WPA2_PERSONAL', 'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL',
                'WPA2_WPA3_PERSONAL', 'WPA2_WPA3_ENTERPRISE' and 'OPEN-SECURED'.
            basicServiceSetClientIdleTimeout(integer): Wireless's This refers to the duration of inactivity,
                measured in seconds, before a client connected to the Basic Service Set is considered
                idle and timed out .
            basicServiceSetMaxIdleEnable(boolean): Wireless's Activate the maximum idle feature for the Basic
                Service Set .
            cckmTsfTolerance(integer): Wireless's Cckm TImestamp Tolerance(in milliseconds) .
            clientExclusionEnable(boolean): Wireless's Activate the feature that allows for the exclusion of clients
                .
            clientExclusionTimeout(integer): Wireless's This refers to the length of time, in seconds, a client is
                excluded or blocked from accessing the network after a specified number of unsuccessful
                attempts .
            clientRateLimit(integer): Wireless's This pertains to the maximum data transfer rate, specified in bits
                per second, that a client is permitted to achieve .
            coverageHoleDetectionEnable(boolean): Wireless's Activate Coverage Hole Detection feature when set to
                true .
            directedMulticastServiceEnable(boolean): Wireless's The Directed Multicast Service feature becomes
                operational when it is set to true .
            egressQos(string): Wireless's Egress QOS . Available values are 'PLATINUM', 'SILVER', 'GOLD' and
                'BRONZE'.
            externalAuthIpAddress(string): Wireless's External WebAuth URL (Mandatory for Guest SSIDs with wlanType
                = Guest, l3AuthType = web_auth and authServer = auth_external) .
            fastTransition(string): Wireless's Fast Transition . Available values are 'ADAPTIVE', 'ENABLE' and
                'DISABLE'.
            fastTransitionOverTheDistributedSystemEnable(boolean): Wireless's Enable Fast Transition over the
                Distributed System when set to true .
            ghz24Policy(string): Wireless's 2.4 Ghz Band Policy value. Allowed only when 2.4 Radio Band is enabled
                in ssidRadioType . Available values are 'dot11-bg-only' and 'dot11-g-only'.
            ghz6PolicyClientSteering(boolean): Wireless's True if 6 GHz Policy Client Steering is enabled, else
                False .
            ingressQos(string): Wireless's Ingress QOS . Available values are 'PLATINUM-UP', 'SILVER-UP', 'GOLD-UP'
                and 'BRONZE-UP'.
            isApBeaconProtectionEnabled(boolean): Wireless's When set to true, the Access Point (AP) Beacon
                Protection feature is activated, enhancing the security of the network. .
            isAuthKey8021x(boolean): Wireless's When set to true, the 802.1X authentication key is in use .
            isAuthKey8021xPlusFT(boolean): Wireless's When set to true, the 802.1X-Plus-FT authentication key is in
                use .
            isAuthKey8021x_SHA256(boolean): Wireless's When set to true, the feature that enables 802.1X
                authentication using the SHA256 algorithm is turned on .
            isAuthKeyEasyPSK(boolean): Wireless's When set to true, the feature that enables the use of Easy Pre-
                shared Key (PSK) authentication is activated .
            isAuthKeyOWE(boolean): Wireless's When set to true, the Opportunistic Wireless Encryption (OWE)
                authentication key feature is turned on .
            isAuthKeyPSK(boolean): Wireless's When set to true, the Pre-shared Key (PSK) authentication feature is
                enabled .
            isAuthKeyPSKPlusFT(boolean): Wireless's When set to true, the feature that enables the combination of
                Pre-shared Key (PSK) and Fast Transition (FT) authentication keys is activated .
            isAuthKeyPSKSHA256(boolean): Wireless's The feature that allows the use of Pre-shared Key (PSK)
                authentication with the SHA256 algorithm is enabled when it is set to true .
            isAuthKeySae(boolean): Wireless's When set to true, the feature enabling the Simultaneous Authentication
                of Equals (SAE) authentication key is activated .
            isAuthKeySaeExt(boolean): Wireless's When set to true, the Simultaneous Authentication of Equals (SAE)
                Extended Authentication key feature is turned on. .
            isAuthKeySaeExtPlusFT(boolean): Wireless's When set to true, the Simultaneous Authentication of Equals
                (SAE) combined with Fast Transition (FT) Authentication Key feature is enabled. .
            isAuthKeySaePlusFT(boolean): Wireless's Activating this setting by switching it to true turns on the
                authentication key feature that supports both Simultaneous Authentication of Equals
                (SAE) and Fast Transition (FT) .
            isAuthKeySuiteB1921x(boolean): Wireless's When set to true, the SuiteB192-1x authentication key feature
                is enabled. .
            isAuthKeySuiteB1x(boolean): Wireless's When activated by setting it to true, the SuiteB-1x
                authentication key feature is engaged. .
            isBroadcastSSID(boolean): Wireless's When activated by setting it to true, the Broadcast SSID feature
                will make the SSID publicly visible to wireless devices searching for available networks
                .
            isCckmEnabled(boolean): Wireless's True if CCKM is enabled, else False .
            isEnabled(boolean): Wireless's Set SSID's admin status as 'Enabled' when set to true .
            isFastLaneEnabled(boolean): Wireless's True if FastLane is enabled, else False .
            isHex(boolean): Wireless's True if passphrase is in Hex format, else False. .
            isMacFilteringEnabled(boolean): Wireless's When set to true, MAC Filtering will be activated, allowing
                control over network access based on the MAC address of the device .
            isPosturingEnabled(boolean): Wireless's Applicable only for Enterprise SSIDs. When set to True,
                Posturing will enabled. Required to be set to True if ACL needs to be mapped for
                Enterprise SSID.   .
            isRandomMacFilterEnabled(boolean): Wireless's Deny clients using randomized MAC addresses when set to
                true .
            l3AuthType(string): Wireless's L3 Authentication Type . Available values are 'open' and 'web_auth'.
            managementFrameProtectionClientprotection(string): Wireless's Management Frame Protection Client .
                Available values are 'OPTIONAL', 'DISABLED' and 'REQUIRED'.
            multiPSKSettings(list): Wireless's multiPSKSettings (list of objects).
            nasOptions(list): Wireless's Pre-Defined NAS Options : AP ETH Mac Address, AP IP address, AP Location ,
                AP MAC Address, AP Name, AP Policy Tag, AP Site Tag, SSID, System IP Address, System MAC
                Address, System Name.  (list of strings).
            neighborListEnable(boolean): Wireless's The Neighbor List feature is enabled when it is set to true .
            openSsid(string): Wireless's Open SSID which is already created in the design and not associated to any
                other OPEN-SECURED SSID .
            passphrase(string): Wireless's Passphrase (Only applicable for SSID with PERSONAL security level).
                Passphrase needs to be between 8 and 63 characters for ASCII type. HEX passphrase needs
                to be 64 characters .
            profileName(string): Wireless's WLAN Profile Name, if not passed autogenerated profile name will be
                assigned. The same wlanProfileName will also be used for policyProfileName .
            protectedManagementFrame(string): Wireless's (REQUIRED is applicable for authType WPA3_PERSONAL,
                WPA3_ENTERPRISE, OPEN_SECURED) and (OPTIONAL/REQUIRED is applicable for authType
                WPA2_WPA3_PERSONAL and WPA2_WPA3_ENTERPRISE) . Available values are 'OPTIONAL',
                'DISABLED' and 'REQUIRED'.
            rsnCipherSuiteCcmp128(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite CCMP128 encryption protocol is activated .
            rsnCipherSuiteCcmp256(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite CCMP256 encryption protocol is activated .
            rsnCipherSuiteGcmp128(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite GCMP128 encryption protocol is activated .
            rsnCipherSuiteGcmp256(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite GCMP256 encryption protocol is activated .
            sessionTimeOut(integer): Wireless's This denotes the allotted time span, expressed in seconds, before a
                session is automatically terminated due to inactivity .
            sessionTimeOutEnable(boolean): Wireless's Turn on the feature that imposes a time limit on user sessions
                .
            sleepingClientEnable(boolean): Wireless's When set to true, this will activate the timeout settings that
                apply to clients in sleep mode .
            sleepingClientTimeout(integer): Wireless's This refers to the amount of time, measured in minutes,
                before a sleeping (inactive) client is timed out of the network .
            ssid(string): Wireless's Name of the SSID .
            ssidRadioType(string): Wireless's Radio Policy Enum (default: Triple band operation(2.4GHz, 5GHz and
                6GHz)) . Available values are 'Triple band operation(2.4GHz, 5GHz and 6GHz)', '5GHz
                only', '2.4GHz only', '6GHz only', '2.4 and 5 GHz', '2.4 and 6 GHz' and '5 and 6 GHz'.
            webPassthrough(boolean): Wireless's When set to true, the Web-Passthrough feature will be activated for
                the Guest SSID, allowing guests to bypass certain login requirements .
            wlanBandSelectEnable(boolean): Wireless's Band select is allowed only when band options selected
                contains at least 2.4 GHz and 5 GHz band .
            wlanType(string): Wireless's Wlan Type . Available values are 'Enterprise' and 'Guest'.
            site_id(str): siteId path parameter. Site UUID of Global site .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-ssid
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, str,
                   may_be_none=False)
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
            'siteId': site_id,
        }
        _payload = {
            'ssid':
                ssid,
            'authType':
                authType,
            'passphrase':
                passphrase,
            'isFastLaneEnabled':
                isFastLaneEnabled,
            'isMacFilteringEnabled':
                isMacFilteringEnabled,
            'ssidRadioType':
                ssidRadioType,
            'isBroadcastSSID':
                isBroadcastSSID,
            'fastTransition':
                fastTransition,
            'sessionTimeOutEnable':
                sessionTimeOutEnable,
            'sessionTimeOut':
                sessionTimeOut,
            'clientExclusionEnable':
                clientExclusionEnable,
            'clientExclusionTimeout':
                clientExclusionTimeout,
            'basicServiceSetMaxIdleEnable':
                basicServiceSetMaxIdleEnable,
            'basicServiceSetClientIdleTimeout':
                basicServiceSetClientIdleTimeout,
            'directedMulticastServiceEnable':
                directedMulticastServiceEnable,
            'neighborListEnable':
                neighborListEnable,
            'managementFrameProtectionClientprotection':
                managementFrameProtectionClientprotection,
            'nasOptions':
                nasOptions,
            'profileName':
                profileName,
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
            'rsnCipherSuiteGcmp256':
                rsnCipherSuiteGcmp256,
            'rsnCipherSuiteCcmp256':
                rsnCipherSuiteCcmp256,
            'rsnCipherSuiteGcmp128':
                rsnCipherSuiteGcmp128,
            'rsnCipherSuiteCcmp128':
                rsnCipherSuiteCcmp128,
            'ghz6PolicyClientSteering':
                ghz6PolicyClientSteering,
            'isAuthKey8021x':
                isAuthKey8021x,
            'isAuthKey8021xPlusFT':
                isAuthKey8021xPlusFT,
            'isAuthKey8021x_SHA256':
                isAuthKey8021x_SHA256,
            'isAuthKeySae':
                isAuthKeySae,
            'isAuthKeySaePlusFT':
                isAuthKeySaePlusFT,
            'isAuthKeyPSK':
                isAuthKeyPSK,
            'isAuthKeyPSKPlusFT':
                isAuthKeyPSKPlusFT,
            'isAuthKeyOWE':
                isAuthKeyOWE,
            'isAuthKeyEasyPSK':
                isAuthKeyEasyPSK,
            'isAuthKeyPSKSHA256':
                isAuthKeyPSKSHA256,
            'openSsid':
                openSsid,
            'wlanBandSelectEnable':
                wlanBandSelectEnable,
            'isEnabled':
                isEnabled,
            'authServers':
                authServers,
            'acctServers':
                acctServers,
            'egressQos':
                egressQos,
            'ingressQos':
                ingressQos,
            'wlanType':
                wlanType,
            'l3AuthType':
                l3AuthType,
            'authServer':
                authServer,
            'externalAuthIpAddress':
                externalAuthIpAddress,
            'webPassthrough':
                webPassthrough,
            'sleepingClientEnable':
                sleepingClientEnable,
            'sleepingClientTimeout':
                sleepingClientTimeout,
            'aclName':
                aclName,
            'isPosturingEnabled':
                isPosturingEnabled,
            'isAuthKeySuiteB1x':
                isAuthKeySuiteB1x,
            'isAuthKeySuiteB1921x':
                isAuthKeySuiteB1921x,
            'isAuthKeySaeExt':
                isAuthKeySaeExt,
            'isAuthKeySaeExtPlusFT':
                isAuthKeySaeExtPlusFT,
            'isApBeaconProtectionEnabled':
                isApBeaconProtectionEnabled,
            'ghz24Policy':
                ghz24Policy,
            'cckmTsfTolerance':
                cckmTsfTolerance,
            'isCckmEnabled':
                isCckmEnabled,
            'isHex':
                isHex,
            'isRandomMacFilterEnabled':
                isRandomMacFilterEnabled,
            'fastTransitionOverTheDistributedSystemEnable':
                fastTransitionOverTheDistributedSystemEnable,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_aa663ca2bd1f5a3db67c405987495112_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_aa663ca2bd1f5a3db67c405987495112_v2_3_7_6', json_data)

    def get_ssid_by_site_v1(self,
                            site_id,
                            limit=None,
                            offset=None,
                            headers=None,
                            **request_parameters):
        """This API allows the user to get all SSIDs (Service Set Identifier) at the given site .

        Args:
            site_id(str): siteId path parameter. Site UUID .
            limit(int): limit query parameter.
            offset(int): offset query parameter.
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-ssid-by-site
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(site_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'siteId': site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ae5ed21186c55f9c8485a57cebf85562_v2_3_7_6', json_data)

    def get_ssid_count_by_site_v1(self,
                                  site_id,
                                  headers=None,
                                  **request_parameters):
        """This API allows the user to get count of all SSIDs (Service Set Identifier) present at global site.  .

        Args:
            site_id(str): siteId path parameter. Site UUID .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-ssid-count-by-site
        """
        check_type(headers, dict)
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

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids'
                 + '/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_de3663dc582ebcd90a67635ae18a_v2_3_7_6', json_data)

    def get_ssid_by_id_v1(self,
                          id,
                          site_id,
                          headers=None,
                          **request_parameters):
        """This API allows the user to get an SSID (Service Set Identifier) by ID at the given site .

        Args:
            site_id(str): siteId path parameter. Site UUID .
            id(str): id path parameter. SSID ID. .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-ssid-by-i-d
        """
        check_type(headers, dict)
        check_type(site_id, str,
                   may_be_none=False)
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
            'siteId': site_id,
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids'
                 + '/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c300d8fe965b278388c9aeca543053_v2_3_7_6', json_data)

    def update_ssid_v1(self,
                       id,
                       site_id,
                       aaaOverride=None,
                       acctServers=None,
                       aclName=None,
                       authServer=None,
                       authServers=None,
                       authType=None,
                       basicServiceSetClientIdleTimeout=None,
                       basicServiceSetMaxIdleEnable=None,
                       cckmTsfTolerance=None,
                       clientExclusionEnable=None,
                       clientExclusionTimeout=None,
                       clientRateLimit=None,
                       coverageHoleDetectionEnable=None,
                       directedMulticastServiceEnable=None,
                       egressQos=None,
                       externalAuthIpAddress=None,
                       fastTransition=None,
                       fastTransitionOverTheDistributedSystemEnable=None,
                       ghz24Policy=None,
                       ghz6PolicyClientSteering=None,
                       ingressQos=None,
                       isApBeaconProtectionEnabled=None,
                       isAuthKey8021x=None,
                       isAuthKey8021xPlusFT=None,
                       isAuthKey8021x_SHA256=None,
                       isAuthKeyEasyPSK=None,
                       isAuthKeyOWE=None,
                       isAuthKeyPSK=None,
                       isAuthKeyPSKPlusFT=None,
                       isAuthKeyPSKSHA256=None,
                       isAuthKeySae=None,
                       isAuthKeySaeExt=None,
                       isAuthKeySaeExtPlusFT=None,
                       isAuthKeySaePlusFT=None,
                       isAuthKeySuiteB1921x=None,
                       isAuthKeySuiteB1x=None,
                       isBroadcastSSID=None,
                       isCckmEnabled=None,
                       isEnabled=None,
                       isFastLaneEnabled=None,
                       isHex=None,
                       isMacFilteringEnabled=None,
                       isPosturingEnabled=None,
                       isRandomMacFilterEnabled=None,
                       l3AuthType=None,
                       managementFrameProtectionClientprotection=None,
                       multiPSKSettings=None,
                       nasOptions=None,
                       neighborListEnable=None,
                       openSsid=None,
                       passphrase=None,
                       profileName=None,
                       protectedManagementFrame=None,
                       rsnCipherSuiteCcmp128=None,
                       rsnCipherSuiteCcmp256=None,
                       rsnCipherSuiteGcmp128=None,
                       rsnCipherSuiteGcmp256=None,
                       sessionTimeOut=None,
                       sessionTimeOutEnable=None,
                       sleepingClientEnable=None,
                       sleepingClientTimeout=None,
                       ssid=None,
                       ssidRadioType=None,
                       webPassthrough=None,
                       wlanBandSelectEnable=None,
                       wlanType=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """This API allows the user to update an SSID (Service Set Identifier) at the given site .

        Args:
            aaaOverride(boolean): Wireless's Activate the AAA Override feature when set to true .
            acctServers(list): Wireless's List of Accounting server IpAddresses  (list of strings).
            aclName(string): Wireless's Pre-Auth Access Control List (ACL) Name .
            authServer(string): Wireless's Authentication Server, Mandatory for Guest SSIDs with wlanType=Guest and
                l3AuthType=web_auth . Available values are 'auth_ise', 'auth_external' and
                'auth_internal'.
            authServers(list): Wireless's List of Authentication/Authorization server IpAddresses  (list of
                strings).
            authType(string): Wireless's L2 Authentication Type (If authType is not open , then atleast one RSN
                Cipher Suite and corresponding valid AKM must be enabled) . Available values are
                'WPA2_ENTERPRISE', 'WPA2_PERSONAL', 'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL',
                'WPA2_WPA3_PERSONAL', 'WPA2_WPA3_ENTERPRISE' and 'OPEN-SECURED'.
            basicServiceSetClientIdleTimeout(integer): Wireless's This refers to the duration of inactivity,
                measured in seconds, before a client connected to the Basic Service Set is considered
                idle and timed out .
            basicServiceSetMaxIdleEnable(boolean): Wireless's Activate the maximum idle feature for the Basic
                Service Set .
            cckmTsfTolerance(integer): Wireless's Cckm TImestamp Tolerance(in milliseconds) .
            clientExclusionEnable(boolean): Wireless's Activate the feature that allows for the exclusion of clients
                .
            clientExclusionTimeout(integer): Wireless's This refers to the length of time, in seconds, a client is
                excluded or blocked from accessing the network after a specified number of unsuccessful
                attempts .
            clientRateLimit(integer): Wireless's This pertains to the maximum data transfer rate, specified in bits
                per second, that a client is permitted to achieve .
            coverageHoleDetectionEnable(boolean): Wireless's Activate Coverage Hole Detection feature when set to
                true .
            directedMulticastServiceEnable(boolean): Wireless's The Directed Multicast Service feature becomes
                operational when it is set to true .
            egressQos(string): Wireless's Egress QOS . Available values are 'PLATINUM', 'SILVER', 'GOLD' and
                'BRONZE'.
            externalAuthIpAddress(string): Wireless's External WebAuth URL (Mandatory for Guest SSIDs with wlanType
                = Guest, l3AuthType = web_auth and authServer = auth_external) .
            fastTransition(string): Wireless's Fast Transition . Available values are 'ADAPTIVE', 'ENABLE' and
                'DISABLE'.
            fastTransitionOverTheDistributedSystemEnable(boolean): Wireless's Enable Fast Transition over the
                Distributed System when set to true .
            ghz24Policy(string): Wireless's 2.4 Ghz Band Policy value. Allowed only when 2.4 Radio Band is enabled
                in ssidRadioType . Available values are 'dot11-bg-only' and 'dot11-g-only'.
            ghz6PolicyClientSteering(boolean): Wireless's True if 6 GHz Policy Client Steering is enabled, else
                False .
            ingressQos(string): Wireless's Ingress QOS . Available values are 'PLATINUM-UP', 'SILVER-UP', 'GOLD-UP'
                and 'BRONZE-UP'.
            isApBeaconProtectionEnabled(boolean): Wireless's When set to true, the Access Point (AP) Beacon
                Protection feature is activated, enhancing the security of the network. .
            isAuthKey8021x(boolean): Wireless's When set to true, the 802.1X authentication key is in use .
            isAuthKey8021xPlusFT(boolean): Wireless's When set to true, the 802.1X-Plus-FT authentication key is in
                use .
            isAuthKey8021x_SHA256(boolean): Wireless's When set to true, the feature that enables 802.1X
                authentication using the SHA256 algorithm is turned on .
            isAuthKeyEasyPSK(boolean): Wireless's When set to true, the feature that enables the use of Easy Pre-
                shared Key (PSK) authentication is activated .
            isAuthKeyOWE(boolean): Wireless's When set to true, the Opportunistic Wireless Encryption (OWE)
                authentication key feature is turned on .
            isAuthKeyPSK(boolean): Wireless's When set to true, the Pre-shared Key (PSK) authentication feature is
                enabled .
            isAuthKeyPSKPlusFT(boolean): Wireless's When set to true, the feature that enables the combination of
                Pre-shared Key (PSK) and Fast Transition (FT) authentication keys is activated .
            isAuthKeyPSKSHA256(boolean): Wireless's The feature that allows the use of Pre-shared Key (PSK)
                authentication with the SHA256 algorithm is enabled when it is set to true .
            isAuthKeySae(boolean): Wireless's When set to true, the feature enabling the Simultaneous Authentication
                of Equals (SAE) authentication key is activated .
            isAuthKeySaeExt(boolean): Wireless's When set to true, the Simultaneous Authentication of Equals (SAE)
                Extended Authentication key feature is turned on. .
            isAuthKeySaeExtPlusFT(boolean): Wireless's When set to true, the Simultaneous Authentication of Equals
                (SAE) combined with Fast Transition (FT) Authentication Key feature is enabled. .
            isAuthKeySaePlusFT(boolean): Wireless's Activating this setting by switching it to true turns on the
                authentication key feature that supports both Simultaneous Authentication of Equals
                (SAE) and Fast Transition (FT) .
            isAuthKeySuiteB1921x(boolean): Wireless's When set to true, the SuiteB192-1x authentication key feature
                is enabled. .
            isAuthKeySuiteB1x(boolean): Wireless's When activated by setting it to true, the SuiteB-1x
                authentication key feature is engaged. .
            isBroadcastSSID(boolean): Wireless's When activated by setting it to true, the Broadcast SSID feature
                will make the SSID publicly visible to wireless devices searching for available networks
                .
            isCckmEnabled(boolean): Wireless's True if CCKM is enabled, else False .
            isEnabled(boolean): Wireless's Set SSID's admin status as 'Enabled' when set to true .
            isFastLaneEnabled(boolean): Wireless's True if FastLane is enabled, else False .
            isHex(boolean): Wireless's True if passphrase is in Hex format, else False. .
            isMacFilteringEnabled(boolean): Wireless's When set to true, MAC Filtering will be activated, allowing
                control over network access based on the MAC address of the device .
            isPosturingEnabled(boolean): Wireless's Applicable only for Enterprise SSIDs. When set to True,
                Posturing will enabled. Required to be set to True if ACL needs to be mapped for
                Enterprise SSID.   .
            isRandomMacFilterEnabled(boolean): Wireless's Deny clients using randomized MAC addresses when set to
                true .
            l3AuthType(string): Wireless's L3 Authentication Type . Available values are 'open' and 'web_auth'.
            managementFrameProtectionClientprotection(string): Wireless's Management Frame Protection Client .
                Available values are 'OPTIONAL', 'DISABLED' and 'REQUIRED'.
            multiPSKSettings(list): Wireless's multiPSKSettings (list of objects).
            nasOptions(list): Wireless's Pre-Defined NAS Options : AP ETH Mac Address, AP IP address, AP Location ,
                AP MAC Address, AP Name, AP Policy Tag, AP Site Tag, SSID, System IP Address, System MAC
                Address, System Name.  (list of strings).
            neighborListEnable(boolean): Wireless's The Neighbor List feature is enabled when it is set to true .
            openSsid(string): Wireless's Open SSID which is already created in the design and not associated to any
                other OPEN-SECURED SSID .
            passphrase(string): Wireless's Passphrase (Only applicable for SSID with PERSONAL security level).
                Passphrase needs to be between 8 and 63 characters for ASCII type. HEX passphrase needs
                to be 64 characters .
            profileName(string): Wireless's WLAN Profile Name, if not passed autogenerated profile name will be
                assigned. The same wlanProfileName will also be used for policyProfileName .
            protectedManagementFrame(string): Wireless's (REQUIRED is applicable for authType WPA3_PERSONAL,
                WPA3_ENTERPRISE, OPEN_SECURED) and (OPTIONAL/REQUIRED is applicable for authType
                WPA2_WPA3_PERSONAL and WPA2_WPA3_ENTERPRISE) . Available values are 'OPTIONAL',
                'DISABLED' and 'REQUIRED'.
            rsnCipherSuiteCcmp128(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite CCMP128 encryption protocol is activated .
            rsnCipherSuiteCcmp256(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite CCMP256 encryption protocol is activated .
            rsnCipherSuiteGcmp128(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite GCMP128 encryption protocol is activated .
            rsnCipherSuiteGcmp256(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite GCMP256 encryption protocol is activated .
            sessionTimeOut(integer): Wireless's This denotes the allotted time span, expressed in seconds, before a
                session is automatically terminated due to inactivity .
            sessionTimeOutEnable(boolean): Wireless's Turn on the feature that imposes a time limit on user sessions
                .
            sleepingClientEnable(boolean): Wireless's When set to true, this will activate the timeout settings that
                apply to clients in sleep mode .
            sleepingClientTimeout(integer): Wireless's This refers to the amount of time, measured in minutes,
                before a sleeping (inactive) client is timed out of the network .
            ssid(string): Wireless's Name of the SSID .
            ssidRadioType(string): Wireless's Radio Policy Enum (default: Triple band operation(2.4GHz, 5GHz and
                6GHz)) . Available values are 'Triple band operation(2.4GHz, 5GHz and 6GHz)', '5GHz
                only', '2.4GHz only', '6GHz only', '2.4 and 5 GHz', '2.4 and 6 GHz' and '5 and 6 GHz'.
            webPassthrough(boolean): Wireless's When set to true, the Web-Passthrough feature will be activated for
                the Guest SSID, allowing guests to bypass certain login requirements .
            wlanBandSelectEnable(boolean): Wireless's Band select is allowed only when band options selected
                contains at least 2.4 GHz and 5 GHz band .
            wlanType(string): Wireless's Wlan Type . Available values are 'Enterprise' and 'Guest'.
            site_id(str): siteId path parameter. Site UUID .
            id(str): id path parameter. SSID ID. Inputs containing special characters should be encoded .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-ssid
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, str,
                   may_be_none=False)
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
            'siteId': site_id,
            'id': id,
        }
        _payload = {
            'ssid':
                ssid,
            'authType':
                authType,
            'passphrase':
                passphrase,
            'isFastLaneEnabled':
                isFastLaneEnabled,
            'isMacFilteringEnabled':
                isMacFilteringEnabled,
            'ssidRadioType':
                ssidRadioType,
            'isBroadcastSSID':
                isBroadcastSSID,
            'fastTransition':
                fastTransition,
            'sessionTimeOutEnable':
                sessionTimeOutEnable,
            'sessionTimeOut':
                sessionTimeOut,
            'clientExclusionEnable':
                clientExclusionEnable,
            'clientExclusionTimeout':
                clientExclusionTimeout,
            'basicServiceSetMaxIdleEnable':
                basicServiceSetMaxIdleEnable,
            'basicServiceSetClientIdleTimeout':
                basicServiceSetClientIdleTimeout,
            'directedMulticastServiceEnable':
                directedMulticastServiceEnable,
            'neighborListEnable':
                neighborListEnable,
            'managementFrameProtectionClientprotection':
                managementFrameProtectionClientprotection,
            'nasOptions':
                nasOptions,
            'profileName':
                profileName,
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
            'rsnCipherSuiteGcmp256':
                rsnCipherSuiteGcmp256,
            'rsnCipherSuiteCcmp256':
                rsnCipherSuiteCcmp256,
            'rsnCipherSuiteGcmp128':
                rsnCipherSuiteGcmp128,
            'rsnCipherSuiteCcmp128':
                rsnCipherSuiteCcmp128,
            'ghz6PolicyClientSteering':
                ghz6PolicyClientSteering,
            'isAuthKey8021x':
                isAuthKey8021x,
            'isAuthKey8021xPlusFT':
                isAuthKey8021xPlusFT,
            'isAuthKey8021x_SHA256':
                isAuthKey8021x_SHA256,
            'isAuthKeySae':
                isAuthKeySae,
            'isAuthKeySaePlusFT':
                isAuthKeySaePlusFT,
            'isAuthKeyPSK':
                isAuthKeyPSK,
            'isAuthKeyPSKPlusFT':
                isAuthKeyPSKPlusFT,
            'isAuthKeyOWE':
                isAuthKeyOWE,
            'isAuthKeyEasyPSK':
                isAuthKeyEasyPSK,
            'isAuthKeyPSKSHA256':
                isAuthKeyPSKSHA256,
            'openSsid':
                openSsid,
            'wlanBandSelectEnable':
                wlanBandSelectEnable,
            'isEnabled':
                isEnabled,
            'authServers':
                authServers,
            'acctServers':
                acctServers,
            'egressQos':
                egressQos,
            'ingressQos':
                ingressQos,
            'wlanType':
                wlanType,
            'l3AuthType':
                l3AuthType,
            'authServer':
                authServer,
            'externalAuthIpAddress':
                externalAuthIpAddress,
            'webPassthrough':
                webPassthrough,
            'sleepingClientEnable':
                sleepingClientEnable,
            'sleepingClientTimeout':
                sleepingClientTimeout,
            'aclName':
                aclName,
            'isPosturingEnabled':
                isPosturingEnabled,
            'isAuthKeySuiteB1x':
                isAuthKeySuiteB1x,
            'isAuthKeySuiteB1921x':
                isAuthKeySuiteB1921x,
            'isAuthKeySaeExt':
                isAuthKeySaeExt,
            'isAuthKeySaeExtPlusFT':
                isAuthKeySaeExtPlusFT,
            'isApBeaconProtectionEnabled':
                isApBeaconProtectionEnabled,
            'ghz24Policy':
                ghz24Policy,
            'cckmTsfTolerance':
                cckmTsfTolerance,
            'isCckmEnabled':
                isCckmEnabled,
            'isHex':
                isHex,
            'isRandomMacFilterEnabled':
                isRandomMacFilterEnabled,
            'fastTransitionOverTheDistributedSystemEnable':
                fastTransitionOverTheDistributedSystemEnable,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a602eee5a56faa64436bade8a240e_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids'
                 + '/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_a602eee5a56faa64436bade8a240e_v2_3_7_6', json_data)

    def delete_ssid_v1(self,
                       id,
                       site_id,
                       headers=None,
                       **request_parameters):
        """This API allows the user to delete an SSID (Service Set Identifier) at the global level, if the SSID is not
        mapped to any Wireless Profile .

        Args:
            site_id(str): siteId path parameter. Site UUID where SSID is to be deleted .
            id(str): id path parameter. SSID ID .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-ssid
        """
        check_type(headers, dict)
        check_type(site_id, str,
                   may_be_none=False)
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
            'siteId': site_id,
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids'
                 + '/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_be7fef60e7b5cdbabd4b93f6a0b4b68_v2_3_7_6', json_data)

    def delete_wireless_profile_v1(self,
                                   wireless_profile_name,
                                   headers=None,
                                   **request_parameters):
        """Delete the Wireless Profile whose name is provided. .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-wireless-profile
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!configure-access-points
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

    def get_access_point_configuration_task_result_v1(self,
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-access-point-configuration-task-result
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

    def get_access_point_configuration_v1(self,
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-access-point-configuration
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

    def ap_provision_connectivity_v1(self,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **request_parameters):
        """Access Point Provision and ReProvision   .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!wireless-ap-provision
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

    def delete_dynamic_interface_v1(self,
                                    interface_name,
                                    headers=None,
                                    **request_parameters):
        """Delete a dynamic interface       .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-dynamic-interface
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

    def create_update_dynamic_interface_v1(self,
                                           interfaceName=None,
                                           vlanId=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **request_parameters):
        """API to create or update an dynamic interface     .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-update-dynamic-interface
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

    def get_dynamic_interface_v1(self,
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-dynamic-interface
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

    def update_wireless_profile_v1(self,
                                   profileDetails=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Updates the wireless Network Profile with updated details provided. All sites to be present in the network
        profile should be provided.  .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-wireless-profile
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

    def create_wireless_profile_v1(self,
                                   profileDetails=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Creates Wireless Network Profile on Cisco DNACenter and associates sites and SSIDs to it.       .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-wireless-profile
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

    def get_wireless_profile_v1(self,
                                profile_name=None,
                                headers=None,
                                **request_parameters):
        """Gets either one or all the wireless network profiles if no name is provided for network-profile.         .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-wireless-profile
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

    def provision_update_v1(self,
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!provision-update
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

    def provision_v1(self,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **request_parameters):
        """Provision wireless device .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!provision
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

    def psk_override_v1(self,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **request_parameters):
        """Update/Override passphrase of SSID .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!psk-override
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

    def retrieve_rf_profiles_v1(self,
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieve-rf-profiles
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

    def create_or_update_rf_profile_v1(self,
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
            defaultRfProfile(boolean): Wireless's is Default Rf Profile .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-or-update-rf-profile
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

    def delete_rf_profiles_v1(self,
                              rf_profile_name,
                              headers=None,
                              **request_parameters):
        """Delete RF profile .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-rf-profiles
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

    def factory_reset_access_points_v1(self,
                                       apMacAddresses=None,
                                       keepStaticIPConfig=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **request_parameters):
        """This API is used to factory reset Access Points. It is supported for maximum 100 Access Points per request.
        Factory reset clears all configurations from the Access Points. After factory reset the Access Point may
        become unreachable from the currently associated Wireless Controller and may or may not join back the
        same controller.  .

        Args:
            apMacAddresses(list): Wireless's List of Access Point's Ethernet MAC addresses, set maximum 100 ethernet
                MAC addresses per request.  (list of strings).
            keepStaticIPConfig(boolean): Wireless's Set the value of keepStaticIPConfig to false, to clear all
                configurations from Access Points and set the value of keepStaticIPConfig to true, to
                clear all configurations from Access Points without clearing static IP configuration. .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!factory-reset-access-points
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
            'keepStaticIPConfig':
                keepStaticIPConfig,
            'apMacAddresses':
                apMacAddresses,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_efa7f7a97b95f5885a00e6981b27b11_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessAccessPoints/factoryResetRequ'
                 + 'est/provision')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_efa7f7a97b95f5885a00e6981b27b11_v2_3_7_6', json_data)

    def get_access_points_factory_reset_status_v1(self,
                                                  task_id,
                                                  headers=None,
                                                  **request_parameters):
        """This API returns each AP Factory Reset initiation status. .

        Args:
            task_id(str): taskId query parameter. provide the task id which is returned in the response of ap
                factory reset post api .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-access-points-factory-reset-status
        """
        check_type(headers, dict)
        check_type(task_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'taskId':
                task_id,
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

        e_url = ('/dna/intent/api/v1/wirelessAccessPoints/factoryResetRequ'
                 + 'estStatus')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f10b36d381e85181a857e67339105684_v2_3_7_6', json_data)

    def ap_provision_v1(self,
                        apZoneName=None,
                        networkDevices=None,
                        rfProfileName=None,
                        siteId=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """This API is used to provision access points .

        Args:
            apZoneName(string): Wireless's AP Zone Name. A custom AP Zone should be passed if no rfProfileName is
                provided. .
            networkDevices(list): Wireless's networkDevices (list of objects).
            rfProfileName(string): Wireless's RF Profile Name. RF Profile is not allowed for custom AP Zones. .
            siteId(string): Wireless's Site ID .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!ap-provision
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
            'networkDevices':
                networkDevices,
            'rfProfileName':
                rfProfileName,
            'apZoneName':
                apZoneName,
            'siteId':
                siteId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_eab4d187be085cac8a53971def40bee0_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessAccessPoints/provision')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_eab4d187be085cac8a53971def40bee0_v2_3_7_6', json_data)

    def get_all_mobility_groups_v1(self,
                                   network_device_id=None,
                                   headers=None,
                                   **request_parameters):
        """Retrieve all configured mobility groups if no Network Device Id is provided as a query parameter. If a Network
        Device Id is given and a mobility group is configured for it, return the configured details; otherwise,
        return the default values from the device. .

        Args:
            network_device_id(str): networkDeviceId query parameter. Employ this query parameter to obtain
                the details of the Mobility Group corresponding to the provided networkDeviceId. Obtain
                the network device ID value by using the API GET call /dna/intent/api/v1/network-
                device/ip-address/${ipAddress}. .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-all-mobility-groups
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
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

        e_url = ('/dna/intent/api/v1/wirelessControllers/wirelessMobilityG'
                 + 'roups')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cb3e813f46055a3d945b3f77c58f913d_v2_3_7_6', json_data)

    def get_mobility_groups_count_v1(self,
                                     headers=None,
                                     **request_parameters):
        """Retrieves count of mobility groups configured .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-mobility-groups-count
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

        e_url = ('/dna/intent/api/v1/wirelessControllers/wirelessMobilityG'
                 + 'roups/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f0e19cf1f588cbe6fcbd0332a3987_v2_3_7_6', json_data)

    def mobility_provision_v1(self,
                              dataLinkEncryption=None,
                              dtlsHighCipher=None,
                              macAddress=None,
                              managementIp=None,
                              mobilityGroupName=None,
                              mobilityPeers=None,
                              networkDeviceId=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **request_parameters):
        """This API is used to provision/deploy wireless mobility into Cisco wireless controllers. .

        Args:
            dataLinkEncryption(boolean): Wireless's A secure link in which data is encrypted using CAPWAP DTLS
                protocol can be established between two controllers. This value will be applied to all
                peers during POST operation. .
            dtlsHighCipher(boolean): Wireless's DTLS High Cipher. .
            macAddress(string): Wireless's Device mobility MAC Address. Allowed formats are: 0a0b.0c01.0211,
                0a0b0c010211, 0a:0b:0c:01:02:11 .
            managementIp(string): Wireless's Self device wireless Management IP. .
            mobilityGroupName(string): Wireless's Self device Group Name. Must be alphanumeric without
                {!,<,space,?/'}   and maximum of 31 characters. .
            mobilityPeers(list): Wireless's mobilityPeers (list of objects).
            networkDeviceId(string): Wireless's Obtain the network device ID value by using the API call GET:
                /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!mobility-provision
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
            'mobilityGroupName':
                mobilityGroupName,
            'macAddress':
                macAddress,
            'managementIp':
                managementIp,
            'networkDeviceId':
                networkDeviceId,
            'dtlsHighCipher':
                dtlsHighCipher,
            'dataLinkEncryption':
                dataLinkEncryption,
            'mobilityPeers':
                mobilityPeers,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_bfd1cc1403c951a99c0fcafd59eaabf3_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessControllers/wirelessMobilityG'
                 + 'roups/mobilityProvision')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_bfd1cc1403c951a99c0fcafd59eaabf3_v2_3_7_6', json_data)

    def mobility_reset_v1(self,
                          networkDeviceId=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **request_parameters):
        """This API is used to reset wireless mobility which in turn sets mobility group name as 'default' .

        Args:
            networkDeviceId(string): Wireless's Network device Id of Cisco wireless controller.Obtain the network
                device ID value by using the API call GET /dna/intent/api/v1/network-device/ip-
                address/${ipAddress}. .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!mobility-reset
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
            'networkDeviceId':
                networkDeviceId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a6c4ce7aef8251a2a8646ba0b5c1826a_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessControllers/wirelessMobilityG'
                 + 'roups/mobilityReset')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a6c4ce7aef8251a2a8646ba0b5c1826a_v2_3_7_6', json_data)

    def assign_managed_ap_locations_for_w_l_c_v1(self,
                                                 device_id,
                                                 primaryManagedAPLocationsSiteIds=None,
                                                 secondaryManagedAPLocationsSiteIds=None,
                                                 headers=None,
                                                 payload=None,
                                                 active_validation=True,
                                                 **request_parameters):
        """This API allows user to assign Managed AP Locations for WLC by device ID. The payload should always be a
        complete list. The Managed AP Locations included in the payload will be fully processed for both
        addition and deletion. .

        Args:
            primaryManagedAPLocationsSiteIds(list): Wireless's Site IDs of Primary Managed AP Locations. These
                values can be obtained by using the API call GET: /dna/intent/api/v1/site  (list of
                strings).
            secondaryManagedAPLocationsSiteIds(list): Wireless's Site IDs of Secondary Managed AP Locations. These
                values can be obtained by using the API call GET: /dna/intent/api/v1/site  (list of
                strings).
            device_id(str): deviceId path parameter. Network Device ID. This value can be obtained by using
                the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress} .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!assign-managed-ap-locations-for-wlc
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(device_id, str,
                   may_be_none=False)
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
            'deviceId': device_id,
        }
        _payload = {
            'primaryManagedAPLocationsSiteIds':
                primaryManagedAPLocationsSiteIds,
            'secondaryManagedAPLocationsSiteIds':
                secondaryManagedAPLocationsSiteIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f019a24c5ce50f082d081bb72ff4df9_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessControllers/{deviceId}/assign'
                 + 'ManagedApLocations')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f019a24c5ce50f082d081bb72ff4df9_v2_3_7_6', json_data)

    def wireless_controller_provision_v1(self,
                                         device_id,
                                         interfaces=None,
                                         rollingApUpgrade=None,
                                         skipApProvision=None,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **request_parameters):
        """This API is used to provision wireless controller .

        Args:
            interfaces(list): Wireless's interfaces (list of objects).
            rollingApUpgrade(object): Wireless's rollingApUpgrade.
            skipApProvision(boolean): Wireless's True if Skip AP Provision is enabled, else False .
            device_id(str): deviceId path parameter. Network Device ID. This value can be obtained by using
                the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress} .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!wireless-controller-provision
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(device_id, str,
                   may_be_none=False)
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
            'deviceId': device_id,
        }
        _payload = {
            'interfaces':
                interfaces,
            'skipApProvision':
                skipApProvision,
            'rollingApUpgrade':
                rollingApUpgrade,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_b0aa8e79d21f5e579908825e70aaccf6_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessControllers/{deviceId}/provis'
                 + 'ion')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_b0aa8e79d21f5e579908825e70aaccf6_v2_3_7_6', json_data)

    def get_anchor_managed_ap_locations_for_specific_wireless_controller_v1(self,
                                                                            network_device_id,
                                                                            limit=None,
                                                                            offset=None,
                                                                            headers=None,
                                                                            **request_parameters):
        """Retrieves all the details of Anchor Managed AP locations associated with the specific Wireless Controller. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the network device ID value by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            limit(int): limit query parameter. The number of records to show for this page. .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-anchor-managed-ap-locations-for-specific-wireless-controller
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(network_device_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'networkDeviceId': network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessControllers/{networkDeviceId}'
                 + '/anchorManagedApLocations')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_de386cae35720b6782009e61541c1_v2_3_7_6', json_data)

    def get_managed_ap_locations_count_for_specific_wireless_controller_v1(self,
                                                                           network_device_id,
                                                                           headers=None,
                                                                           **request_parameters):
        """Retrieves the count of Managed AP locations, including Primary Managed AP Locations, Secondary Managed AP
        Locations, and Anchor Managed AP Locations, associated with the specific Wireless Controller. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the network device ID value by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-managed-ap-locations-count-for-specific-wireless-controller
        """
        check_type(headers, dict)
        check_type(network_device_id, str,
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
            'networkDeviceId': network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessControllers/{networkDeviceId}'
                 + '/managedApLocations/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f4a6e8f2c1de51f5b70e9c75c4b6fc1c_v2_3_7_6', json_data)

    def get_primary_managed_ap_locations_for_specific_wireless_controller_v1(self,
                                                                             network_device_id,
                                                                             limit=None,
                                                                             offset=None,
                                                                             headers=None,
                                                                             **request_parameters):
        """Retrieves all the details of Primary Managed AP locations associated with the specific Wireless Controller. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the network device ID value by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            limit(int): limit query parameter. The number of records to show for this page. .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-primary-managed-ap-locations-for-specific-wireless-controller
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(network_device_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'networkDeviceId': network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessControllers/{networkDeviceId}'
                 + '/primaryManagedApLocations')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e9b5024741155ad880b482720757f661_v2_3_7_6', json_data)

    def get_secondary_managed_ap_locations_for_specific_wireless_controller_v1(self,
                                                                               network_device_id,
                                                                               limit=None,
                                                                               offset=None,
                                                                               headers=None,
                                                                               **request_parameters):
        """Retrieves all the details of Secondary Managed AP locations associated with the specific Wireless Controller. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the network device ID value by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            limit(int): limit query parameter. The number of records to show for this page. .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-secondary-managed-ap-locations-for-specific-wireless-controller
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(network_device_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'networkDeviceId': network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessControllers/{networkDeviceId}'
                 + '/secondaryManagedApLocations')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a431078850850a5bef6cb4fa9915fb7_v2_3_7_6', json_data)

    def get_ssid_details_for_specific_wireless_controller_v1(self,
                                                             network_device_id,
                                                             admin_status=None,
                                                             limit=None,
                                                             managed=None,
                                                             offset=None,
                                                             ssid_name=None,
                                                             headers=None,
                                                             **request_parameters):
        """Retrieves all details of SSIDs associated with the specific Wireless Controller. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the network device ID value by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            ssid_name(str): ssidName query parameter. Employ this query parameter to obtain the details of
                the SSID corresponding to the provided SSID name. .
            admin_status(bool): adminStatus query parameter. Utilize this query parameter to obtain the
                administrative status. A 'true' value signifies that the admin status of the SSID is
                enabled, while a 'false' value indicates that the admin status of the SSID is disabled.
                .
            managed(bool): managed query parameter. If value is 'true' means SSIDs are configured through design.If
                the value is 'false' means out of band configuration from the Wireless Controller. .
            limit(int): limit query parameter. The number of records to show for this page. .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-ssid-details-for-specific-wireless-controller
        """
        check_type(headers, dict)
        check_type(ssid_name, str)
        check_type(admin_status, bool)
        check_type(managed, bool)
        check_type(limit, int)
        check_type(offset, int)
        check_type(network_device_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'ssidName':
                ssid_name,
            'adminStatus':
                admin_status,
            'managed':
                managed,
            'limit':
                limit,
            'offset':
                offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'networkDeviceId': network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessControllers/{networkDeviceId}'
                 + '/ssidDetails')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_efdb6b3d51ff9e3e2de942ca96c4_v2_3_7_6', json_data)

    def get_ssid_count_for_specific_wireless_controller_v1(self,
                                                           network_device_id,
                                                           admin_status=None,
                                                           managed=None,
                                                           headers=None,
                                                           **request_parameters):
        """Retrieves the count of SSIDs associated with the specific Wireless Controller. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the network device ID value by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            admin_status(bool): adminStatus query parameter. Utilize this query parameter to obtain the number of
                SSIDs according to their administrative status. A 'true' value signifies that the admin
                status of the SSID is enabled, while a 'false' value indicates that the admin status of
                the SSID is disabled. .
            managed(bool): managed query parameter. If value is 'true' means SSIDs are configured through design.If
                the value is 'false' means out of band configuration from the Wireless Controller. .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-ssid-count-for-specific-wireless-controller
        """
        check_type(headers, dict)
        check_type(admin_status, bool)
        check_type(managed, bool)
        check_type(network_device_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'adminStatus':
                admin_status,
            'managed':
                managed,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'networkDeviceId': network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessControllers/{networkDeviceId}'
                 + '/ssidDetails/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_db60b529835a2e8d3f67c681f1ace4_v2_3_7_6', json_data)

    def get_wireless_profiles_v1(self,
                                 limit=None,
                                 offset=None,
                                 headers=None,
                                 **request_parameters):
        """This API allows the user to get all Wireless Network Profiles .

        Args:
            limit(int): limit query parameter.
            offset(int): offset query parameter.
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-wireless-profiles
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
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

        e_url = ('/dna/intent/api/v1/wirelessProfiles')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bec142b3bf65c109d752da5705ae2ca_v2_3_7_6', json_data)

    def create_wireless_profile_connectivity_v1(self,
                                                ssidDetails=None,
                                                wirelessProfileName=None,
                                                headers=None,
                                                payload=None,
                                                active_validation=True,
                                                **request_parameters):
        """This API allows the user to create a Wireless Network Profile .

        Args:
            ssidDetails(list): Wireless's ssidDetails (list of objects).
            wirelessProfileName(string): Wireless's Wireless Network Profile Name .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-wireless-profile
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
            'wirelessProfileName':
                wirelessProfileName,
            'ssidDetails':
                ssidDetails,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_cc59d48f8159008f52b29e08738811_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessProfiles')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_cc59d48f8159008f52b29e08738811_v2_3_7_6', json_data)

    def get_wireless_profiles_count_v1(self,
                                       headers=None,
                                       **request_parameters):
        """This API allows the user to get count of all wireless profiles .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-wireless-profiles-count
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

        e_url = ('/dna/intent/api/v1/wirelessProfiles/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ef56c845d27d59e5974077ade9deedf3_v2_3_7_6', json_data)

    def update_wireless_profile_connectivity_v1(self,
                                                id,
                                                ssidDetails=None,
                                                wirelessProfileName=None,
                                                headers=None,
                                                payload=None,
                                                active_validation=True,
                                                **request_parameters):
        """This API allows the user to update a Wireless Network Profile by ID .

        Args:
            ssidDetails(list): Wireless's ssidDetails (list of objects).
            wirelessProfileName(string): Wireless's Wireless Network Profile Name .
            id(str): id path parameter. Wireless Profile Id .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-wireless-profile
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str,
                   may_be_none=False)
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
            'id': id,
        }
        _payload = {
            'wirelessProfileName':
                wirelessProfileName,
            'ssidDetails':
                ssidDetails,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d91a3aad0fd954e7a43aa3256ce433f6_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessProfiles/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_d91a3aad0fd954e7a43aa3256ce433f6_v2_3_7_6', json_data)

    def get_wireless_profile_by_id_v1(self,
                                      id,
                                      headers=None,
                                      **request_parameters):
        """This API allows the user to get a Wireless Network Profile by ID .

        Args:
            id(str): id path parameter. Wireless Profile Id .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-wireless-profile-by-id
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

        e_url = ('/dna/intent/api/v1/wirelessProfiles/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d89e08ebbe2528088fbdb3b367cb23b_v2_3_7_6', json_data)

    def delete_wireless_profile_connectivity_v1(self,
                                                id,
                                                headers=None,
                                                **request_parameters):
        """This API allows the user to delete Wireless Network Profile by ID .

        Args:
            id(str): id path parameter. Wireless Profile Id .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-wireless-profile
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

        e_url = ('/dna/intent/api/v1/wirelessProfiles/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_afcc95b9babb1b6a776e065e1_v2_3_7_6', json_data)

    def get_all80211be_profiles_v1(self,
                                   limit=None,
                                   offset=None,
                                   headers=None,
                                   **request_parameters):
        """This API allows the user to get all 802.11be Profile(s) configured under Wireless Settings .

        Args:
            limit(int): limit query parameter.
            offset(int): offset query parameter.
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-all80211be-profiles
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
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

        e_url = ('/dna/intent/api/v1/wirelessSettings/dot11beProfiles')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f2b94a700f80548694685475590d5e0b_v2_3_7_6', json_data)

    def create_a80211be_profile_v1(self,
                                   muMimoDownLink=None,
                                   muMimoUpLink=None,
                                   ofdmaDownLink=None,
                                   ofdmaMultiRu=None,
                                   ofdmaUpLink=None,
                                   profileName=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """This API allows the user to create a 802.11be Profile.DNA Center will push this profile to device's
        "default-dot11be-profile”.Also please note , 802.11be Profile is supported only on IOS-XE controllers
        since device version 17.15 .

        Args:
            muMimoDownLink(boolean): Wireless's MU-MIMO Downlink (Default: false) .
            muMimoUpLink(boolean): Wireless's MU-MIMO Uplink (Default: false) .
            ofdmaDownLink(boolean): Wireless's OFDMA Downlink (Default: true) .
            ofdmaMultiRu(boolean): Wireless's OFDMA Multi-RU (Default: false) .
            ofdmaUpLink(boolean): Wireless's OFDMA Uplink (Default: true) .
            profileName(string): Wireless's 802.11be Profile Name .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-a80211be-profile
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
            'profileName':
                profileName,
            'ofdmaDownLink':
                ofdmaDownLink,
            'ofdmaUpLink':
                ofdmaUpLink,
            'muMimoDownLink':
                muMimoDownLink,
            'muMimoUpLink':
                muMimoUpLink,
            'ofdmaMultiRu':
                ofdmaMultiRu,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f08eb586113e597a91b1658297570934_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessSettings/dot11beProfiles')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f08eb586113e597a91b1658297570934_v2_3_7_6', json_data)

    def get80211be_profiles_count_v1(self,
                                     headers=None,
                                     **request_parameters):
        """This API allows the user to get count of all 802.11be Profile(s) .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get80211be-profiles-count
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

        e_url = ('/dna/intent/api/v1/wirelessSettings/dot11beProfiles/coun'
                 + 't')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b18962654b512e939285910448177d_v2_3_7_6', json_data)

    def delete_a80211be_profile_v1(self,
                                   id,
                                   headers=None,
                                   **request_parameters):
        """This API allows the user to delete a 802.11be Profile,if the 802.11be Profile is not mapped to any Wireless
        Network Profile .

        Args:
            id(str): id path parameter. 802.11be Profile ID .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-a80211be-profile
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

        e_url = ('/dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f08862be5ba89b5c2f50aa30baa0_v2_3_7_6', json_data)

    def update80211be_profile_v1(self,
                                 id,
                                 muMimoDownLink=None,
                                 muMimoUpLink=None,
                                 ofdmaDownLink=None,
                                 ofdmaMultiRu=None,
                                 ofdmaUpLink=None,
                                 profileName=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **request_parameters):
        """This API allows the user to update a 802.11be Profile .

        Args:
            muMimoDownLink(boolean): Wireless's MU-MIMO Downlink (Default: false) .
            muMimoUpLink(boolean): Wireless's MU-MIMO Uplink (Default: false) .
            ofdmaDownLink(boolean): Wireless's OFDMA Downlink (Default: true) .
            ofdmaMultiRu(boolean): Wireless's OFDMA Multi-RU (Default: false) .
            ofdmaUpLink(boolean): Wireless's OFDMA Uplink (Default: true) .
            profileName(string): Wireless's 802.11be Profile Name .
            id(str): id path parameter. 802.11be Profile ID .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update80211be-profile
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
            'profileName':
                profileName,
            'ofdmaDownLink':
                ofdmaDownLink,
            'ofdmaUpLink':
                ofdmaUpLink,
            'muMimoDownLink':
                muMimoDownLink,
            'muMimoUpLink':
                muMimoUpLink,
            'ofdmaMultiRu':
                ofdmaMultiRu,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_ef28900485c4e9842b4a68e483d4e_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_ef28900485c4e9842b4a68e483d4e_v2_3_7_6', json_data)

    def get80211be_profile_by_id_v1(self,
                                    id,
                                    headers=None,
                                    **request_parameters):
        """This API allows the user to get 802.11be Profile by ID .

        Args:
            id(str): id path parameter. 802.11be Profile ID .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get80211be-profile-by-id
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

        e_url = ('/dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ae9378f178355aea0e70e5ece0d430e_v2_3_7_6', json_data)

    def get_interfaces_v1(self,
                          limit=None,
                          offset=None,
                          headers=None,
                          **request_parameters):
        """This API allows the user to get all Interfaces .

        Args:
            limit(int): limit query parameter.
            offset(int): offset query parameter.
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-interfaces
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
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

        e_url = ('/dna/intent/api/v1/wirelessSettings/interfaces')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d2c4823550d79e07dca86c2e8f66_v2_3_7_6', json_data)

    def create_interface_v1(self,
                            interfaceName=None,
                            vlanId=None,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **request_parameters):
        """This API allows the user to create an interface .

        Args:
            interfaceName(string): Wireless's Interface Name .
            vlanId(integer): Wireless's VLAN ID range is 1-4094 .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-interface
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
            self._request_validator('jsd_fb5e152d4d3d59f5afd92f717f3a1eea_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessSettings/interfaces')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_fb5e152d4d3d59f5afd92f717f3a1eea_v2_3_7_6', json_data)

    def get_interfaces_count_v1(self,
                                headers=None,
                                **request_parameters):
        """This API allows the user to get count of all interfaces .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-interfaces-count
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

        e_url = ('/dna/intent/api/v1/wirelessSettings/interfaces/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f8918c9ed835ee580679fd709548682_v2_3_7_6', json_data)

    def get_interface_by_id_v1(self,
                               id,
                               headers=None,
                               **request_parameters):
        """This API allows the user to get an interface by ID .

        Args:
            id(str): id path parameter. Interface ID .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-interface-by-id
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

        e_url = ('/dna/intent/api/v1/wirelessSettings/interfaces/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_feb0798215d52bbdab50542213d44_v2_3_7_6', json_data)

    def delete_interface_v1(self,
                            id,
                            headers=None,
                            **request_parameters):
        """This API allows the user to delete an interface by ID .

        Args:
            id(str): id path parameter. Interface ID .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-interface
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

        e_url = ('/dna/intent/api/v1/wirelessSettings/interfaces/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bdfaf07257c5a1190881ddd70dabf1b_v2_3_7_6', json_data)

    def update_interface_v1(self,
                            id,
                            interfaceName=None,
                            vlanId=None,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **request_parameters):
        """This API allows the user to update an interface by ID .

        Args:
            interfaceName(string): Wireless's Interface Name .
            vlanId(integer): Wireless's VLAN ID range is 1-4094 .
            id(str): id path parameter. Interface ID .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-interface
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
            'interfaceName':
                interfaceName,
            'vlanId':
                vlanId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_ee43cac5fd65c55ab3153d3549d18c0_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessSettings/interfaces/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_ee43cac5fd65c55ab3153d3549d18c0_v2_3_7_6', json_data)

    def create_rf_profile_v1(self,
                             defaultRfProfile=None,
                             enableRadioType6GHz=None,
                             enableRadioTypeA=None,
                             enableRadioTypeB=None,
                             radioType6GHzProperties=None,
                             radioTypeAProperties=None,
                             radioTypeBProperties=None,
                             rfProfileName=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **request_parameters):
        """This API allows the user to create a custom RF Profile .

        Args:
            defaultRfProfile(boolean): Wireless's True if RF Profile is default, else False. Maximum of only 1 RF
                Profile can be marked as default at any given time .
            enableRadioType6GHz(boolean): Wireless's True if 6 GHz radio band is enabled in the RF Profile, else
                False .
            enableRadioTypeA(boolean): Wireless's True if 5 GHz radio band is enabled in the RF Profile, else False
                .
            enableRadioTypeB(boolean): Wireless's True if 2.4 GHz radio band is enabled in the RF Profile, else
                False .
            radioType6GHzProperties(object): Wireless's radioType6GHzProperties.
            radioTypeAProperties(object): Wireless's radioTypeAProperties.
            radioTypeBProperties(object): Wireless's radioTypeBProperties.
            rfProfileName(string): Wireless's RF Profile Name .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-rf-profile
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
            'rfProfileName':
                rfProfileName,
            'defaultRfProfile':
                defaultRfProfile,
            'enableRadioTypeA':
                enableRadioTypeA,
            'enableRadioTypeB':
                enableRadioTypeB,
            'enableRadioType6GHz':
                enableRadioType6GHz,
            'radioTypeAProperties':
                radioTypeAProperties,
            'radioTypeBProperties':
                radioTypeBProperties,
            'radioType6GHzProperties':
                radioType6GHzProperties,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_bcb1d489d735258975828f845df1769_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessSettings/rfProfiles')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_bcb1d489d735258975828f845df1769_v2_3_7_6', json_data)

    def get_rf_profiles_v1(self,
                           limit=None,
                           offset=None,
                           headers=None,
                           **request_parameters):
        """This API allows the user to get all RF Profiles .

        Args:
            limit(int): limit query parameter.
            offset(int): offset query parameter.
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-rf-profiles
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
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

        e_url = ('/dna/intent/api/v1/wirelessSettings/rfProfiles')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e11599ca71552e960dc2cdd182abb9_v2_3_7_6', json_data)

    def get_rf_profiles_count_v1(self,
                                 headers=None,
                                 **request_parameters):
        """This API allows the user to get count of all RF profiles .

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-rf-profiles-count
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

        e_url = ('/dna/intent/api/v1/wirelessSettings/rfProfiles/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f91267d9ae54ae85b4ddad0b92a2dd_v2_3_7_6', json_data)

    def delete_rf_profile_v1(self,
                             id,
                             headers=None,
                             **request_parameters):
        """This API allows the user to delete a custom RF Profile .

        Args:
            id(str): id path parameter. RF Profile ID .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-rf-profile
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

        e_url = ('/dna/intent/api/v1/wirelessSettings/rfProfiles/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dd7b861ab3e8520486d956a1a171dd63_v2_3_7_6', json_data)

    def get_rf_profile_by_id_v1(self,
                                id,
                                headers=None,
                                **request_parameters):
        """This API allows the user to get a RF Profile by RF Profile ID .

        Args:
            id(str): id path parameter. RF Profile ID .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-rf-profile-by-id
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

        e_url = ('/dna/intent/api/v1/wirelessSettings/rfProfiles/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f59b09f4f1cb5b1c9ddb50e2b81815ef_v2_3_7_6', json_data)

    def update_rf_profile_v1(self,
                             id,
                             defaultRfProfile=None,
                             enableRadioType6GHz=None,
                             enableRadioTypeA=None,
                             enableRadioTypeB=None,
                             radioType6GHzProperties=None,
                             radioTypeAProperties=None,
                             radioTypeBProperties=None,
                             rfProfileName=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **request_parameters):
        """This API allows the user to update a custom RF Profile .

        Args:
            defaultRfProfile(boolean): Wireless's True if RF Profile is default, else False. Maximum of only 1 RF
                Profile can be marked as default at any given time .
            enableRadioType6GHz(boolean): Wireless's True if 6 GHz radio band is enabled in the RF Profile, else
                False .
            enableRadioTypeA(boolean): Wireless's True if 5 GHz radio band is enabled in the RF Profile, else False
                .
            enableRadioTypeB(boolean): Wireless's True if 2.4 GHz radio band is enabled in the RF Profile, else
                False .
            radioType6GHzProperties(object): Wireless's radioType6GHzProperties.
            radioTypeAProperties(object): Wireless's radioTypeAProperties.
            radioTypeBProperties(object): Wireless's radioTypeBProperties.
            rfProfileName(string): Wireless's RF Profile Name .
            id(str): id path parameter. RF Profile ID .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-rf-profile
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
            'rfProfileName':
                rfProfileName,
            'defaultRfProfile':
                defaultRfProfile,
            'enableRadioTypeA':
                enableRadioTypeA,
            'enableRadioTypeB':
                enableRadioTypeB,
            'enableRadioType6GHz':
                enableRadioType6GHz,
            'radioTypeAProperties':
                radioTypeAProperties,
            'radioTypeBProperties':
                radioTypeBProperties,
            'radioType6GHzProperties':
                radioType6GHzProperties,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_da455f4be5b75126ba9970c7cc54c7db_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/wirelessSettings/rfProfiles/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_da455f4be5b75126ba9970c7cc54c7db_v2_3_7_6', json_data)

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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!configure-access-points-v2
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

                
    
    # Alias Function
    def assign_managed_ap_locations_for_w_l_c(self,
                                                 device_id,
                                                 primaryManagedAPLocationsSiteIds=None,
                                                 secondaryManagedAPLocationsSiteIds=None,
                                                 headers=None,
                                                 payload=None,
                                                 active_validation=True,
                                                 **request_parameters):
        """ This function is an alias of assign_managed_ap_locations_for_w_l_c_v1 .
        Args:
            primaryManagedAPLocationsSiteIds(list): Wireless's Site IDs of Primary Managed AP Locations. These
                values can be obtained by using the API call GET: /dna/intent/api/v1/site  (list of
                strings).
            secondaryManagedAPLocationsSiteIds(list): Wireless's Site IDs of Secondary Managed AP Locations. These
                values can be obtained by using the API call GET: /dna/intent/api/v1/site  (list of
                strings).
            device_id(basestring): deviceId path parameter. Network Device ID. This value can be obtained by using
                the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress} .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of assign_managed_ap_locations_for_w_l_c_v1 .
        """ 
        return self.assign_managed_ap_locations_for_w_l_c_v1(
                    device_id=device_id,
                    primaryManagedAPLocationsSiteIds=primaryManagedAPLocationsSiteIds,
                    secondaryManagedAPLocationsSiteIds=secondaryManagedAPLocationsSiteIds,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def create_rf_profile(self,
                             defaultRfProfile=None,
                             enableRadioType6GHz=None,
                             enableRadioTypeA=None,
                             enableRadioTypeB=None,
                             radioType6GHzProperties=None,
                             radioTypeAProperties=None,
                             radioTypeBProperties=None,
                             rfProfileName=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **request_parameters):
        """ This function is an alias of create_rf_profile_v1 .
        Args:
            defaultRfProfile(boolean): Wireless's True if RF Profile is default, else False. Maximum of only 1 RF
                Profile can be marked as default at any given time .
            enableRadioType6GHz(boolean): Wireless's True if 6 GHz radio band is enabled in the RF Profile, else
                False .
            enableRadioTypeA(boolean): Wireless's True if 5 GHz radio band is enabled in the RF Profile, else False
                .
            enableRadioTypeB(boolean): Wireless's True if 2.4 GHz radio band is enabled in the RF Profile, else
                False .
            radioType6GHzProperties(object): Wireless's radioType6GHzProperties.
            radioTypeAProperties(object): Wireless's radioTypeAProperties.
            radioTypeBProperties(object): Wireless's radioTypeBProperties.
            rfProfileName(string): Wireless's RF Profile Name .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_rf_profile_v1 .
        """ 
        return self.create_rf_profile_v1(
                    defaultRfProfile=defaultRfProfile,
                    enableRadioType6GHz=enableRadioType6GHz,
                    enableRadioTypeA=enableRadioTypeA,
                    enableRadioTypeB=enableRadioTypeB,
                    radioType6GHzProperties=radioType6GHzProperties,
                    radioTypeAProperties=radioTypeAProperties,
                    radioTypeBProperties=radioTypeBProperties,
                    rfProfileName=rfProfileName,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_interfaces_count(self,
                                headers=None,
                                **request_parameters):
        """ This function is an alias of get_interfaces_count_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_interfaces_count_v1 .
        """
        return self.get_interfaces_count_v1(
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def delete_dynamic_interface(self,
                                    interface_name,
                                    headers=None,
                                    **request_parameters):
        """ This function is an alias of delete_dynamic_interface_v1 .
        Args:
            interface_name(basestring): interfaceName query parameter. valid interface-name to be deleted .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_dynamic_interface_v1 .
        """ 
        return self.delete_dynamic_interface_v1(
                    interface_name=interface_name,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def delete_rf_profile(self,
                             id,
                             headers=None,
                             **request_parameters):
        """ This function is an alias of delete_rf_profile_v1 .
        Args:
            id(basestring): id path parameter. RF Profile ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_rf_profile_v1 .
        """ 
        return self.delete_rf_profile_v1(
                    id=id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def update_wireless_profile(self,
                                   profileDetails=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """ This function is an alias of update_wireless_profile_v1 .
        Args:
            profileDetails(object): Wireless's profileDetails.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_wireless_profile_v1 .
        """ 
        return self.update_wireless_profile_v1(
                    profileDetails=profileDetails,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def update_wireless_profile_connectivity(self,
                                                id,
                                                ssidDetails=None,
                                                wirelessProfileName=None,
                                                headers=None,
                                                payload=None,
                                                active_validation=True,
                                                **request_parameters):
        """ This function is an alias of update_wireless_profile_connectivity_v1 .
        Args:
            ssidDetails(list): Wireless's ssidDetails (list of objects).
            wirelessProfileName(string): Wireless's Wireless Network Profile Name .
            id(basestring): id path parameter. Wireless Profile Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_wireless_profile_connectivity_v1 .
        """ 
        return self.update_wireless_profile_connectivity_v1(
                    id=id,
                    ssidDetails=ssidDetails,
                    wirelessProfileName=wirelessProfileName,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_anchor_managed_ap_locations_for_specific_wireless_controller(self,
                                                                            network_device_id,
                                                                            limit=None,
                                                                            offset=None,
                                                                            headers=None,
                                                                            **request_parameters):
        """ This function is an alias of get_anchor_managed_ap_locations_for_specific_wireless_controller_v1 .
        Args:
            network_device_id(basestring): networkDeviceId path parameter. Obtain the network device ID value by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            limit(int): limit query parameter. The number of records to show for this page. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_anchor_managed_ap_locations_for_specific_wireless_controller_v1 .
        """ 
        return self.get_anchor_managed_ap_locations_for_specific_wireless_controller_v1(
                    network_device_id=network_device_id,
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def create_update_dynamic_interface(self,
                                           interfaceName=None,
                                           vlanId=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **request_parameters):
        """ This function is an alias of create_update_dynamic_interface_v1 .
        Args:
            interfaceName(string): Wireless's dynamic-interface name .
            vlanId(number): Wireless's Vlan Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_update_dynamic_interface_v1 .
        """ 
        return self.create_update_dynamic_interface_v1(
                    interfaceName=interfaceName,
                    vlanId=vlanId,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_interfaces(self,
                          limit=None,
                          offset=None,
                          headers=None,
                          **request_parameters):
        """ This function is an alias of get_interfaces_v1 .
        Args:
            limit(int): limit query parameter.
            offset(int): offset query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_interfaces_v1 .
        """ 
        return self.get_interfaces_v1(
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_enterprise_ssid(self,
                               ssid_name=None,
                               headers=None,
                               **request_parameters):
        """ This function is an alias of get_enterprise_ssid_v1 .
        Args:
            ssid_name(basestring): ssidName query parameter. Enter the enterprise SSID name that needs to be
                retrieved. If not entered, all the enterprise SSIDs will be retrieved. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_enterprise_ssid_v1 .
        """ 
        return self.get_enterprise_ssid_v1(
                    ssid_name=ssid_name,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_ssid_by_id(self,
                          id,
                          site_id,
                          headers=None,
                          **request_parameters):
        """ This function is an alias of get_ssid_by_id_v1 .
        Args:
            site_id(basestring): siteId path parameter. Site UUID .
            id(basestring): id path parameter. SSID ID. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_ssid_by_id_v1 .
        """ 
        return self.get_ssid_by_id_v1(
                    id=id,
                    site_id=site_id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def retrieve_rf_profiles(self,
                                rf_profile_name=None,
                                headers=None,
                                **request_parameters):
        """ This function is an alias of retrieve_rf_profiles_v1 .
        Args:
            rf_profile_name(basestring): rf-profile-name query parameter. RF Profile Name .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieve_rf_profiles_v1 .
        """ 
        return self.retrieve_rf_profiles_v1(
                    rf_profile_name=rf_profile_name,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def configure_access_points(self,
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
        """ This function is an alias of configure_access_points_v1 .
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
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of configure_access_points_v1 .
        """ 
        return self.configure_access_points_v1(
                    adminStatus=adminStatus,
                    apList=apList,
                    apMode=apMode,
                    configureAdminStatus=configureAdminStatus,
                    configureApMode=configureApMode,
                    configureFailoverPriority=configureFailoverPriority,
                    configureHAController=configureHAController,
                    configureLedBrightnessLevel=configureLedBrightnessLevel,
                    configureLedStatus=configureLedStatus,
                    configureLocation=configureLocation,
                    failoverPriority=failoverPriority,
                    isAssignedSiteAsLocation=isAssignedSiteAsLocation,
                    ledBrightnessLevel=ledBrightnessLevel,
                    ledStatus=ledStatus,
                    location=location,
                    primaryControllerName=primaryControllerName,
                    primaryIpAddress=primaryIpAddress,
                    radioConfigurations=radioConfigurations,
                    secondaryControllerName=secondaryControllerName,
                    secondaryIpAddress=secondaryIpAddress,
                    tertiaryControllerName=tertiaryControllerName,
                    tertiaryIpAddress=tertiaryIpAddress,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_rf_profile_by_id(self,
                                id,
                                headers=None,
                                **request_parameters):
        """ This function is an alias of get_rf_profile_by_id_v1 .
        Args:
            id(basestring): id path parameter. RF Profile ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_rf_profile_by_id_v1 .
        """ 
        return self.get_rf_profile_by_id_v1(
                    id=id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def create_wireless_profile(self,
                                   profileDetails=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """ This function is an alias of create_wireless_profile_v1 .
        Args:
            profileDetails(object): Wireless's profileDetails.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_wireless_profile_v1 .
        """ 
        return self.create_wireless_profile_v1(
                    profileDetails=profileDetails,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def mobility_provision(self,
                              dataLinkEncryption=None,
                              dtlsHighCipher=None,
                              macAddress=None,
                              managementIp=None,
                              mobilityGroupName=None,
                              mobilityPeers=None,
                              networkDeviceId=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **request_parameters):
        """ This function is an alias of mobility_provision_v1 .
        Args:
            dataLinkEncryption(boolean): Wireless's A secure link in which data is encrypted using CAPWAP DTLS
                protocol can be established between two controllers. This value will be applied to all
                peers during POST operation. .
            dtlsHighCipher(boolean): Wireless's DTLS High Cipher. .
            macAddress(string): Wireless's Device mobility MAC Address. Allowed formats are: 0a0b.0c01.0211,
                0a0b0c010211, 0a:0b:0c:01:02:11 .
            managementIp(string): Wireless's Self device wireless Management IP. .
            mobilityGroupName(string): Wireless's Self device Group Name. Must be alphanumeric without
                {!,<,space,?/'}   and maximum of 31 characters. .
            mobilityPeers(list): Wireless's mobilityPeers (list of objects).
            networkDeviceId(string): Wireless's Obtain the network device ID value by using the API call GET:
                /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of mobility_provision_v1 .
        """ 
        return self.mobility_provision_v1(
                    dataLinkEncryption=dataLinkEncryption,
                    dtlsHighCipher=dtlsHighCipher,
                    macAddress=macAddress,
                    managementIp=managementIp,
                    mobilityGroupName=mobilityGroupName,
                    mobilityPeers=mobilityPeers,
                    networkDeviceId=networkDeviceId,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def delete_a80211be_profile(self,
                                   id,
                                   headers=None,
                                   **request_parameters):
        """ This function is an alias of delete_a80211be_profile_v1 .
        Args:
            id(basestring): id path parameter. 802.11be Profile ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_a80211be_profile_v1 .
        """ 
        return self.delete_a80211be_profile_v1(
                    id=id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_mobility_groups_count(self,
                                     headers=None,
                                     **request_parameters):
        """ This function is an alias of get_mobility_groups_count_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_mobility_groups_count_v1 .
        """
        return self.get_mobility_groups_count_v1(
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_rf_profiles(self,
                           limit=None,
                           offset=None,
                           headers=None,
                           **request_parameters):
        """ This function is an alias of get_rf_profiles_v1 .
        Args:
            limit(int): limit query parameter.
            offset(int): offset query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_rf_profiles_v1 .
        """ 
        return self.get_rf_profiles_v1(
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_all_mobility_groups(self,
                                   network_device_id=None,
                                   headers=None,
                                   **request_parameters):
        """ This function is an alias of get_all_mobility_groups_v1 .
        Args:
            network_device_id(basestring): networkDeviceId query parameter. Employ this query parameter to obtain
                the details of the Mobility Group corresponding to the provided networkDeviceId. Obtain
                the network device ID value by using the API GET call /dna/intent/api/v1/network-
                device/ip-address/${ipAddress}. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_all_mobility_groups_v1 .
        """ 
        return self.get_all_mobility_groups_v1(
                    network_device_id=network_device_id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def delete_wireless_profile(self,
                                   wireless_profile_name,
                                   headers=None,
                                   **request_parameters):
        """ This function is an alias of delete_wireless_profile_v1 .
        Args:
            wireless_profile_name(basestring): wirelessProfileName path parameter. Wireless Profile Name .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_wireless_profile_v1 .
        """ 
        return self.delete_wireless_profile_v1(
                    wireless_profile_name=wireless_profile_name,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_rf_profiles_count(self,
                                 headers=None,
                                 **request_parameters):
        """ This function is an alias of get_rf_profiles_count_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_rf_profiles_count_v1 .
        """
        return self.get_rf_profiles_count_v1(
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def mobility_reset(self,
                          networkDeviceId=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **request_parameters):
        """ This function is an alias of mobility_reset_v1 .
        Args:
            networkDeviceId(string): Wireless's Network device Id of Cisco wireless controller.Obtain the network
                device ID value by using the API call GET /dna/intent/api/v1/network-device/ip-
                address/${ipAddress}. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of mobility_reset_v1 .
        """ 
        return self.mobility_reset_v1(
                    networkDeviceId=networkDeviceId,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def update80211be_profile(self,
                                 id,
                                 muMimoDownLink=None,
                                 muMimoUpLink=None,
                                 ofdmaDownLink=None,
                                 ofdmaMultiRu=None,
                                 ofdmaUpLink=None,
                                 profileName=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **request_parameters):
        """ This function is an alias of update80211be_profile_v1 .
        Args:
            muMimoDownLink(boolean): Wireless's MU-MIMO Downlink (Default: false) .
            muMimoUpLink(boolean): Wireless's MU-MIMO Uplink (Default: false) .
            ofdmaDownLink(boolean): Wireless's OFDMA Downlink (Default: true) .
            ofdmaMultiRu(boolean): Wireless's OFDMA Multi-RU (Default: false) .
            ofdmaUpLink(boolean): Wireless's OFDMA Uplink (Default: true) .
            profileName(string): Wireless's 802.11be Profile Name .
            id(basestring): id path parameter. 802.11be Profile ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update80211be_profile_v1 .
        """ 
        return self.update80211be_profile_v1(
                    id=id,
                    muMimoDownLink=muMimoDownLink,
                    muMimoUpLink=muMimoUpLink,
                    ofdmaDownLink=ofdmaDownLink,
                    ofdmaMultiRu=ofdmaMultiRu,
                    ofdmaUpLink=ofdmaUpLink,
                    profileName=profileName,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_dynamic_interface(self,
                                 interface_name=None,
                                 headers=None,
                                 **request_parameters):
        """ This function is an alias of get_dynamic_interface_v1 .
        Args:
            interface_name(basestring): interface-name query parameter. dynamic-interface name, if not specified all
                the existing dynamic interfaces will be retrieved .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_dynamic_interface_v1 .
        """ 
        return self.get_dynamic_interface_v1(
                    interface_name=interface_name,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_interface_by_id(self,
                               id,
                               headers=None,
                               **request_parameters):
        """ This function is an alias of get_interface_by_id_v1 .
        Args:
            id(basestring): id path parameter. Interface ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_interface_by_id_v1 .
        """ 
        return self.get_interface_by_id_v1(
                    id=id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_wireless_profile(self,
                                profile_name=None,
                                headers=None,
                                **request_parameters):
        """ This function is an alias of get_wireless_profile_v1 .
        Args:
            profile_name(basestring): profileName query parameter. Wireless Network Profile Name .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_wireless_profile_v1 .
        """ 
        return self.get_wireless_profile_v1(
                    profile_name=profile_name,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def create_ssid(self,
                       site_id,
                       aaaOverride=None,
                       acctServers=None,
                       aclName=None,
                       authServer=None,
                       authServers=None,
                       authType=None,
                       basicServiceSetClientIdleTimeout=None,
                       basicServiceSetMaxIdleEnable=None,
                       cckmTsfTolerance=None,
                       clientExclusionEnable=None,
                       clientExclusionTimeout=None,
                       clientRateLimit=None,
                       coverageHoleDetectionEnable=None,
                       directedMulticastServiceEnable=None,
                       egressQos=None,
                       externalAuthIpAddress=None,
                       fastTransition=None,
                       fastTransitionOverTheDistributedSystemEnable=None,
                       ghz24Policy=None,
                       ghz6PolicyClientSteering=None,
                       ingressQos=None,
                       isApBeaconProtectionEnabled=None,
                       isAuthKey8021x=None,
                       isAuthKey8021xPlusFT=None,
                       isAuthKey8021x_SHA256=None,
                       isAuthKeyEasyPSK=None,
                       isAuthKeyOWE=None,
                       isAuthKeyPSK=None,
                       isAuthKeyPSKPlusFT=None,
                       isAuthKeyPSKSHA256=None,
                       isAuthKeySae=None,
                       isAuthKeySaeExt=None,
                       isAuthKeySaeExtPlusFT=None,
                       isAuthKeySaePlusFT=None,
                       isAuthKeySuiteB1921x=None,
                       isAuthKeySuiteB1x=None,
                       isBroadcastSSID=None,
                       isCckmEnabled=None,
                       isEnabled=None,
                       isFastLaneEnabled=None,
                       isHex=None,
                       isMacFilteringEnabled=None,
                       isPosturingEnabled=None,
                       isRandomMacFilterEnabled=None,
                       l3AuthType=None,
                       managementFrameProtectionClientprotection=None,
                       multiPSKSettings=None,
                       nasOptions=None,
                       neighborListEnable=None,
                       openSsid=None,
                       passphrase=None,
                       profileName=None,
                       protectedManagementFrame=None,
                       rsnCipherSuiteCcmp128=None,
                       rsnCipherSuiteCcmp256=None,
                       rsnCipherSuiteGcmp128=None,
                       rsnCipherSuiteGcmp256=None,
                       sessionTimeOut=None,
                       sessionTimeOutEnable=None,
                       sleepingClientEnable=None,
                       sleepingClientTimeout=None,
                       ssid=None,
                       ssidRadioType=None,
                       webPassthrough=None,
                       wlanBandSelectEnable=None,
                       wlanType=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """ This function is an alias of create_ssid_v1 .
        Args:
            aaaOverride(boolean): Wireless's Activate the AAA Override feature when set to true .
            acctServers(list): Wireless's List of Accounting server IpAddresses  (list of strings).
            aclName(string): Wireless's Pre-Auth Access Control List (ACL) Name .
            authServer(string): Wireless's Authentication Server, Mandatory for Guest SSIDs with wlanType=Guest and
                l3AuthType=web_auth . Available values are 'auth_ise', 'auth_external' and
                'auth_internal'.
            authServers(list): Wireless's List of Authentication/Authorization server IpAddresses  (list of
                strings).
            authType(string): Wireless's L2 Authentication Type (If authType is not open , then atleast one RSN
                Cipher Suite and corresponding valid AKM must be enabled) . Available values are
                'WPA2_ENTERPRISE', 'WPA2_PERSONAL', 'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL',
                'WPA2_WPA3_PERSONAL', 'WPA2_WPA3_ENTERPRISE' and 'OPEN-SECURED'.
            basicServiceSetClientIdleTimeout(integer): Wireless's This refers to the duration of inactivity,
                measured in seconds, before a client connected to the Basic Service Set is considered
                idle and timed out .
            basicServiceSetMaxIdleEnable(boolean): Wireless's Activate the maximum idle feature for the Basic
                Service Set .
            cckmTsfTolerance(integer): Wireless's Cckm TImestamp Tolerance(in milliseconds) .
            clientExclusionEnable(boolean): Wireless's Activate the feature that allows for the exclusion of clients
                .
            clientExclusionTimeout(integer): Wireless's This refers to the length of time, in seconds, a client is
                excluded or blocked from accessing the network after a specified number of unsuccessful
                attempts .
            clientRateLimit(integer): Wireless's This pertains to the maximum data transfer rate, specified in bits
                per second, that a client is permitted to achieve .
            coverageHoleDetectionEnable(boolean): Wireless's Activate Coverage Hole Detection feature when set to
                true .
            directedMulticastServiceEnable(boolean): Wireless's The Directed Multicast Service feature becomes
                operational when it is set to true .
            egressQos(string): Wireless's Egress QOS . Available values are 'PLATINUM', 'SILVER', 'GOLD' and
                'BRONZE'.
            externalAuthIpAddress(string): Wireless's External WebAuth URL (Mandatory for Guest SSIDs with wlanType
                = Guest, l3AuthType = web_auth and authServer = auth_external) .
            fastTransition(string): Wireless's Fast Transition . Available values are 'ADAPTIVE', 'ENABLE' and
                'DISABLE'.
            fastTransitionOverTheDistributedSystemEnable(boolean): Wireless's Enable Fast Transition over the
                Distributed System when set to true .
            ghz24Policy(string): Wireless's 2.4 Ghz Band Policy value. Allowed only when 2.4 Radio Band is enabled
                in ssidRadioType . Available values are 'dot11-bg-only' and 'dot11-g-only'.
            ghz6PolicyClientSteering(boolean): Wireless's True if 6 GHz Policy Client Steering is enabled, else
                False .
            ingressQos(string): Wireless's Ingress QOS . Available values are 'PLATINUM-UP', 'SILVER-UP', 'GOLD-UP'
                and 'BRONZE-UP'.
            isApBeaconProtectionEnabled(boolean): Wireless's When set to true, the Access Point (AP) Beacon
                Protection feature is activated, enhancing the security of the network. .
            isAuthKey8021x(boolean): Wireless's When set to true, the 802.1X authentication key is in use .
            isAuthKey8021xPlusFT(boolean): Wireless's When set to true, the 802.1X-Plus-FT authentication key is in
                use .
            isAuthKey8021x_SHA256(boolean): Wireless's When set to true, the feature that enables 802.1X
                authentication using the SHA256 algorithm is turned on .
            isAuthKeyEasyPSK(boolean): Wireless's When set to true, the feature that enables the use of Easy Pre-
                shared Key (PSK) authentication is activated .
            isAuthKeyOWE(boolean): Wireless's When set to true, the Opportunistic Wireless Encryption (OWE)
                authentication key feature is turned on .
            isAuthKeyPSK(boolean): Wireless's When set to true, the Pre-shared Key (PSK) authentication feature is
                enabled .
            isAuthKeyPSKPlusFT(boolean): Wireless's When set to true, the feature that enables the combination of
                Pre-shared Key (PSK) and Fast Transition (FT) authentication keys is activated .
            isAuthKeyPSKSHA256(boolean): Wireless's The feature that allows the use of Pre-shared Key (PSK)
                authentication with the SHA256 algorithm is enabled when it is set to true .
            isAuthKeySae(boolean): Wireless's When set to true, the feature enabling the Simultaneous Authentication
                of Equals (SAE) authentication key is activated .
            isAuthKeySaeExt(boolean): Wireless's When set to true, the Simultaneous Authentication of Equals (SAE)
                Extended Authentication key feature is turned on. .
            isAuthKeySaeExtPlusFT(boolean): Wireless's When set to true, the Simultaneous Authentication of Equals
                (SAE) combined with Fast Transition (FT) Authentication Key feature is enabled. .
            isAuthKeySaePlusFT(boolean): Wireless's Activating this setting by switching it to true turns on the
                authentication key feature that supports both Simultaneous Authentication of Equals
                (SAE) and Fast Transition (FT) .
            isAuthKeySuiteB1921x(boolean): Wireless's When set to true, the SuiteB192-1x authentication key feature
                is enabled. .
            isAuthKeySuiteB1x(boolean): Wireless's When activated by setting it to true, the SuiteB-1x
                authentication key feature is engaged. .
            isBroadcastSSID(boolean): Wireless's When activated by setting it to true, the Broadcast SSID feature
                will make the SSID publicly visible to wireless devices searching for available networks
                .
            isCckmEnabled(boolean): Wireless's True if CCKM is enabled, else False .
            isEnabled(boolean): Wireless's Set SSID's admin status as 'Enabled' when set to true .
            isFastLaneEnabled(boolean): Wireless's True if FastLane is enabled, else False .
            isHex(boolean): Wireless's True if passphrase is in Hex format, else False. .
            isMacFilteringEnabled(boolean): Wireless's When set to true, MAC Filtering will be activated, allowing
                control over network access based on the MAC address of the device .
            isPosturingEnabled(boolean): Wireless's Applicable only for Enterprise SSIDs. When set to True,
                Posturing will enabled. Required to be set to True if ACL needs to be mapped for
                Enterprise SSID.   .
            isRandomMacFilterEnabled(boolean): Wireless's Deny clients using randomized MAC addresses when set to
                true .
            l3AuthType(string): Wireless's L3 Authentication Type . Available values are 'open' and 'web_auth'.
            managementFrameProtectionClientprotection(string): Wireless's Management Frame Protection Client .
                Available values are 'OPTIONAL', 'DISABLED' and 'REQUIRED'.
            multiPSKSettings(list): Wireless's multiPSKSettings (list of objects).
            nasOptions(list): Wireless's Pre-Defined NAS Options : AP ETH Mac Address, AP IP address, AP Location ,
                AP MAC Address, AP Name, AP Policy Tag, AP Site Tag, SSID, System IP Address, System MAC
                Address, System Name.  (list of strings).
            neighborListEnable(boolean): Wireless's The Neighbor List feature is enabled when it is set to true .
            openSsid(string): Wireless's Open SSID which is already created in the design and not associated to any
                other OPEN-SECURED SSID .
            passphrase(string): Wireless's Passphrase (Only applicable for SSID with PERSONAL security level).
                Passphrase needs to be between 8 and 63 characters for ASCII type. HEX passphrase needs
                to be 64 characters .
            profileName(string): Wireless's WLAN Profile Name, if not passed autogenerated profile name will be
                assigned. The same wlanProfileName will also be used for policyProfileName .
            protectedManagementFrame(string): Wireless's (REQUIRED is applicable for authType WPA3_PERSONAL,
                WPA3_ENTERPRISE, OPEN_SECURED) and (OPTIONAL/REQUIRED is applicable for authType
                WPA2_WPA3_PERSONAL and WPA2_WPA3_ENTERPRISE) . Available values are 'OPTIONAL',
                'DISABLED' and 'REQUIRED'.
            rsnCipherSuiteCcmp128(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite CCMP128 encryption protocol is activated .
            rsnCipherSuiteCcmp256(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite CCMP256 encryption protocol is activated .
            rsnCipherSuiteGcmp128(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite GCMP128 encryption protocol is activated .
            rsnCipherSuiteGcmp256(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite GCMP256 encryption protocol is activated .
            sessionTimeOut(integer): Wireless's This denotes the allotted time span, expressed in seconds, before a
                session is automatically terminated due to inactivity .
            sessionTimeOutEnable(boolean): Wireless's Turn on the feature that imposes a time limit on user sessions
                .
            sleepingClientEnable(boolean): Wireless's When set to true, this will activate the timeout settings that
                apply to clients in sleep mode .
            sleepingClientTimeout(integer): Wireless's This refers to the amount of time, measured in minutes,
                before a sleeping (inactive) client is timed out of the network .
            ssid(string): Wireless's Name of the SSID .
            ssidRadioType(string): Wireless's Radio Policy Enum (default: Triple band operation(2.4GHz, 5GHz and
                6GHz)) . Available values are 'Triple band operation(2.4GHz, 5GHz and 6GHz)', '5GHz
                only', '2.4GHz only', '6GHz only', '2.4 and 5 GHz', '2.4 and 6 GHz' and '5 and 6 GHz'.
            webPassthrough(boolean): Wireless's When set to true, the Web-Passthrough feature will be activated for
                the Guest SSID, allowing guests to bypass certain login requirements .
            wlanBandSelectEnable(boolean): Wireless's Band select is allowed only when band options selected
                contains at least 2.4 GHz and 5 GHz band .
            wlanType(string): Wireless's Wlan Type . Available values are 'Enterprise' and 'Guest'.
            site_id(basestring): siteId path parameter. Site UUID of Global site .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_ssid_v1 .
        """ 
        return self.create_ssid_v1(
                    site_id=site_id,
                    aaaOverride=aaaOverride,
                    acctServers=acctServers,
                    aclName=aclName,
                    authServer=authServer,
                    authServers=authServers,
                    authType=authType,
                    basicServiceSetClientIdleTimeout=basicServiceSetClientIdleTimeout,
                    basicServiceSetMaxIdleEnable=basicServiceSetMaxIdleEnable,
                    cckmTsfTolerance=cckmTsfTolerance,
                    clientExclusionEnable=clientExclusionEnable,
                    clientExclusionTimeout=clientExclusionTimeout,
                    clientRateLimit=clientRateLimit,
                    coverageHoleDetectionEnable=coverageHoleDetectionEnable,
                    directedMulticastServiceEnable=directedMulticastServiceEnable,
                    egressQos=egressQos,
                    externalAuthIpAddress=externalAuthIpAddress,
                    fastTransition=fastTransition,
                    fastTransitionOverTheDistributedSystemEnable=fastTransitionOverTheDistributedSystemEnable,
                    ghz24Policy=ghz24Policy,
                    ghz6PolicyClientSteering=ghz6PolicyClientSteering,
                    ingressQos=ingressQos,
                    isApBeaconProtectionEnabled=isApBeaconProtectionEnabled,
                    isAuthKey8021x=isAuthKey8021x,
                    isAuthKey8021xPlusFT=isAuthKey8021xPlusFT,
                    isAuthKey8021x_SHA256=isAuthKey8021x_SHA256,
                    isAuthKeyEasyPSK=isAuthKeyEasyPSK,
                    isAuthKeyOWE=isAuthKeyOWE,
                    isAuthKeyPSK=isAuthKeyPSK,
                    isAuthKeyPSKPlusFT=isAuthKeyPSKPlusFT,
                    isAuthKeyPSKSHA256=isAuthKeyPSKSHA256,
                    isAuthKeySae=isAuthKeySae,
                    isAuthKeySaeExt=isAuthKeySaeExt,
                    isAuthKeySaeExtPlusFT=isAuthKeySaeExtPlusFT,
                    isAuthKeySaePlusFT=isAuthKeySaePlusFT,
                    isAuthKeySuiteB1921x=isAuthKeySuiteB1921x,
                    isAuthKeySuiteB1x=isAuthKeySuiteB1x,
                    isBroadcastSSID=isBroadcastSSID,
                    isCckmEnabled=isCckmEnabled,
                    isEnabled=isEnabled,
                    isFastLaneEnabled=isFastLaneEnabled,
                    isHex=isHex,
                    isMacFilteringEnabled=isMacFilteringEnabled,
                    isPosturingEnabled=isPosturingEnabled,
                    isRandomMacFilterEnabled=isRandomMacFilterEnabled,
                    l3AuthType=l3AuthType,
                    managementFrameProtectionClientprotection=managementFrameProtectionClientprotection,
                    multiPSKSettings=multiPSKSettings,
                    nasOptions=nasOptions,
                    neighborListEnable=neighborListEnable,
                    openSsid=openSsid,
                    passphrase=passphrase,
                    profileName=profileName,
                    protectedManagementFrame=protectedManagementFrame,
                    rsnCipherSuiteCcmp128=rsnCipherSuiteCcmp128,
                    rsnCipherSuiteCcmp256=rsnCipherSuiteCcmp256,
                    rsnCipherSuiteGcmp128=rsnCipherSuiteGcmp128,
                    rsnCipherSuiteGcmp256=rsnCipherSuiteGcmp256,
                    sessionTimeOut=sessionTimeOut,
                    sessionTimeOutEnable=sessionTimeOutEnable,
                    sleepingClientEnable=sleepingClientEnable,
                    sleepingClientTimeout=sleepingClientTimeout,
                    ssid=ssid,
                    ssidRadioType=ssidRadioType,
                    webPassthrough=webPassthrough,
                    wlanBandSelectEnable=wlanBandSelectEnable,
                    wlanType=wlanType,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
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
        """ This function is an alias of create_enterprise_ssid_v1 .
        Args:
            aaaOverride(boolean): Wireless's Aaa Override .
            authKeyMgmt(list): Wireless's Takes string inputs for the AKMs that should be set true. Possible AKM
                values : dot1x,dot1x_ft, dot1x_sha, psk, psk_ft, psk_sha, owe, sae, sae_ft  (list of
                strings).
            basicServiceSetClientIdleTimeout(integer): Wireless's Basic Service Set Client Idle Timeout .
            clientExclusionTimeout(integer): Wireless's Client Exclusion Timeout .
            clientRateLimit(number): Wireless's Client Rate Limit (in bits per second) .
            coverageHoleDetectionEnable(boolean): Wireless's Coverage Hole Detection Enable .
            enableBasicServiceSetMaxIdle(boolean): Wireless's Enable Basic Service Set Max Idle  .
            enableBroadcastSSID(boolean): Wireless's Enable Broadcase SSID  .
            enableClientExclusion(boolean): Wireless's Enable Client Exclusion .
            enableDirectedMulticastService(boolean): Wireless's Enable Directed Multicast Service .
            enableFastLane(boolean): Wireless's Enable FastLane .
            enableMACFiltering(boolean): Wireless's Enable MAC Filtering .
            enableNeighborList(boolean): Wireless's Enable Neighbor List .
            enableSessionTimeOut(boolean): Wireless's Enable Session Timeout .
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
                'WPA2_PERSONAL', 'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL', 'WPA2_WPA3_PERSONAL',
                'WPA2_WPA3_ENTERPRISE' and 'OPEN_SECURED'.
            sessionTimeOut(integer): Wireless's Session Time Out .
            trafficType(string): Wireless's Traffic Type Enum (voicedata or data ) . Available values are
                'voicedata' and 'data'.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_enterprise_ssid_v1 .
        """ 
        return self.create_enterprise_ssid_v1(
                    aaaOverride=aaaOverride,
                    authKeyMgmt=authKeyMgmt,
                    basicServiceSetClientIdleTimeout=basicServiceSetClientIdleTimeout,
                    clientExclusionTimeout=clientExclusionTimeout,
                    clientRateLimit=clientRateLimit,
                    coverageHoleDetectionEnable=coverageHoleDetectionEnable,
                    enableBasicServiceSetMaxIdle=enableBasicServiceSetMaxIdle,
                    enableBroadcastSSID=enableBroadcastSSID,
                    enableClientExclusion=enableClientExclusion,
                    enableDirectedMulticastService=enableDirectedMulticastService,
                    enableFastLane=enableFastLane,
                    enableMACFiltering=enableMACFiltering,
                    enableNeighborList=enableNeighborList,
                    enableSessionTimeOut=enableSessionTimeOut,
                    fastTransition=fastTransition,
                    ghz24Policy=ghz24Policy,
                    ghz6PolicyClientSteering=ghz6PolicyClientSteering,
                    mfpClientProtection=mfpClientProtection,
                    multiPSKSettings=multiPSKSettings,
                    name=name,
                    nasOptions=nasOptions,
                    passphrase=passphrase,
                    policyProfileName=policyProfileName,
                    profileName=profileName,
                    protectedManagementFrame=protectedManagementFrame,
                    radioPolicy=radioPolicy,
                    rsnCipherSuiteCcmp256=rsnCipherSuiteCcmp256,
                    rsnCipherSuiteGcmp128=rsnCipherSuiteGcmp128,
                    rsnCipherSuiteGcmp256=rsnCipherSuiteGcmp256,
                    securityLevel=securityLevel,
                    sessionTimeOut=sessionTimeOut,
                    trafficType=trafficType,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def update_rf_profile(self,
                             id,
                             defaultRfProfile=None,
                             enableRadioType6GHz=None,
                             enableRadioTypeA=None,
                             enableRadioTypeB=None,
                             radioType6GHzProperties=None,
                             radioTypeAProperties=None,
                             radioTypeBProperties=None,
                             rfProfileName=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **request_parameters):
        """ This function is an alias of update_rf_profile_v1 .
        Args:
            defaultRfProfile(boolean): Wireless's True if RF Profile is default, else False. Maximum of only 1 RF
                Profile can be marked as default at any given time .
            enableRadioType6GHz(boolean): Wireless's True if 6 GHz radio band is enabled in the RF Profile, else
                False .
            enableRadioTypeA(boolean): Wireless's True if 5 GHz radio band is enabled in the RF Profile, else False
                .
            enableRadioTypeB(boolean): Wireless's True if 2.4 GHz radio band is enabled in the RF Profile, else
                False .
            radioType6GHzProperties(object): Wireless's radioType6GHzProperties.
            radioTypeAProperties(object): Wireless's radioTypeAProperties.
            radioTypeBProperties(object): Wireless's radioTypeBProperties.
            rfProfileName(string): Wireless's RF Profile Name .
            id(basestring): id path parameter. RF Profile ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_rf_profile_v1 .
        """ 
        return self.update_rf_profile_v1(
                    id=id,
                    defaultRfProfile=defaultRfProfile,
                    enableRadioType6GHz=enableRadioType6GHz,
                    enableRadioTypeA=enableRadioTypeA,
                    enableRadioTypeB=enableRadioTypeB,
                    radioType6GHzProperties=radioType6GHzProperties,
                    radioTypeAProperties=radioTypeAProperties,
                    radioTypeBProperties=radioTypeBProperties,
                    rfProfileName=rfProfileName,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_access_point_configuration_task_result(self,
                                                      task_id,
                                                      headers=None,
                                                      **request_parameters):
        """ This function is an alias of get_access_point_configuration_task_result_v1 .
        Args:
            task_id(basestring): task_id path parameter. task id information of ap config .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_access_point_configuration_task_result_v1 .
        """ 
        return self.get_access_point_configuration_task_result_v1(
                    task_id=task_id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_wireless_profile_by_id(self,
                                      id,
                                      headers=None,
                                      **request_parameters):
        """ This function is an alias of get_wireless_profile_by_id_v1 .
        Args:
            id(basestring): id path parameter. Wireless Profile Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_wireless_profile_by_id_v1 .
        """ 
        return self.get_wireless_profile_by_id_v1(
                    id=id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get80211be_profile_by_id(self,
                                    id,
                                    headers=None,
                                    **request_parameters):
        """ This function is an alias of get80211be_profile_by_id_v1 .
        Args:
            id(basestring): id path parameter. 802.11be Profile ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get80211be_profile_by_id_v1 .
        """ 
        return self.get80211be_profile_by_id_v1(
                    id=id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_managed_ap_locations_count_for_specific_wireless_controller(self,
                                                                           network_device_id,
                                                                           headers=None,
                                                                           **request_parameters):
        """ This function is an alias of get_managed_ap_locations_count_for_specific_wireless_controller_v1 .
        Args:
            network_device_id(basestring): networkDeviceId path parameter. Obtain the network device ID value by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_managed_ap_locations_count_for_specific_wireless_controller_v1 .
        """ 
        return self.get_managed_ap_locations_count_for_specific_wireless_controller_v1(
                    network_device_id=network_device_id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
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
        """ This function is an alias of update_enterprise_ssid_v1 .
        Args:
            aaaOverride(boolean): Wireless's Aaa Override .
            authKeyMgmt(list): Wireless's Takes string inputs for the AKMs that should be set true. Possible AKM
                values : dot1x,dot1x_ft, dot1x_sha, psk, psk_ft, psk_sha, owe, sae, sae_ft  (list of
                strings).
            basicServiceSetClientIdleTimeout(integer): Wireless's Basic Service Set Client Idle Timeout .
            clientExclusionTimeout(integer): Wireless's Client Exclusion Timeout .
            clientRateLimit(number): Wireless's Client Rate Limit (in bits per second) .
            coverageHoleDetectionEnable(boolean): Wireless's Coverage Hole Detection Enable .
            enableBasicServiceSetMaxIdle(boolean): Wireless's Enable Basic Service Set Max Idle  .
            enableBroadcastSSID(boolean): Wireless's Enable Broadcase SSID  .
            enableClientExclusion(boolean): Wireless's Enable Client Exclusion .
            enableDirectedMulticastService(boolean): Wireless's Enable Directed Multicast Service .
            enableFastLane(boolean): Wireless's Enable FastLane .
            enableMACFiltering(boolean): Wireless's Enable MAC Filtering .
            enableNeighborList(boolean): Wireless's Enable Neighbor List .
            enableSessionTimeOut(boolean): Wireless's Enable Session Timeout .
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
                'WPA2_PERSONAL', 'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL', 'WPA2_WPA3_PERSONAL',
                'WPA2_WPA3_ENTERPRISE' and 'OPEN_SECURED'.
            sessionTimeOut(integer): Wireless's Session Time Out .
            trafficType(string): Wireless's Traffic Type Enum (voicedata or data ) . Available values are
                'voicedata' and 'data'.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_enterprise_ssid_v1 .
        """ 
        return self.update_enterprise_ssid_v1(
                    aaaOverride=aaaOverride,
                    authKeyMgmt=authKeyMgmt,
                    basicServiceSetClientIdleTimeout=basicServiceSetClientIdleTimeout,
                    clientExclusionTimeout=clientExclusionTimeout,
                    clientRateLimit=clientRateLimit,
                    coverageHoleDetectionEnable=coverageHoleDetectionEnable,
                    enableBasicServiceSetMaxIdle=enableBasicServiceSetMaxIdle,
                    enableBroadcastSSID=enableBroadcastSSID,
                    enableClientExclusion=enableClientExclusion,
                    enableDirectedMulticastService=enableDirectedMulticastService,
                    enableFastLane=enableFastLane,
                    enableMACFiltering=enableMACFiltering,
                    enableNeighborList=enableNeighborList,
                    enableSessionTimeOut=enableSessionTimeOut,
                    fastTransition=fastTransition,
                    ghz24Policy=ghz24Policy,
                    ghz6PolicyClientSteering=ghz6PolicyClientSteering,
                    mfpClientProtection=mfpClientProtection,
                    multiPSKSettings=multiPSKSettings,
                    name=name,
                    nasOptions=nasOptions,
                    passphrase=passphrase,
                    policyProfileName=policyProfileName,
                    profileName=profileName,
                    protectedManagementFrame=protectedManagementFrame,
                    radioPolicy=radioPolicy,
                    rsnCipherSuiteCcmp256=rsnCipherSuiteCcmp256,
                    rsnCipherSuiteGcmp128=rsnCipherSuiteGcmp128,
                    rsnCipherSuiteGcmp256=rsnCipherSuiteGcmp256,
                    securityLevel=securityLevel,
                    sessionTimeOut=sessionTimeOut,
                    trafficType=trafficType,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def ap_provision(self,
                        apZoneName=None,
                        networkDevices=None,
                        rfProfileName=None,
                        siteId=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """ This function is an alias of ap_provision_v1 .
        Args:
            apZoneName(string): Wireless's AP Zone Name. A custom AP Zone should be passed if no rfProfileName is
                provided. .
            networkDevices(list): Wireless's networkDevices (list of objects).
            rfProfileName(string): Wireless's RF Profile Name. RF Profile is not allowed for custom AP Zones. .
            siteId(string): Wireless's Site ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of ap_provision_v1 .
        """ 
        return self.ap_provision_v1(
                    apZoneName=apZoneName,
                    networkDevices=networkDevices,
                    rfProfileName=rfProfileName,
                    siteId=siteId,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def psk_override(self,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **request_parameters):
        """ This function is an alias of psk_override_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of psk_override_v1 .
        """ 
        return self.psk_override_v1(
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def provision_update(self,
                         headers=None,
                         payload=None,
                         active_validation=True,
                         **request_parameters):
        """ This function is an alias of provision_update_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of provision_update_v1 .
        """ 
        return self.provision_update_v1(
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_ssid_by_site(self,
                            site_id,
                            limit=None,
                            offset=None,
                            headers=None,
                            **request_parameters):
        """ This function is an alias of get_ssid_by_site_v1 .
        Args:
            site_id(basestring): siteId path parameter. Site UUID .
            limit(int): limit query parameter.
            offset(int): offset query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_ssid_by_site_v1 .
        """ 
        return self.get_ssid_by_site_v1(
                    site_id=site_id,
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def sensor_test_results(self,
                               end_time=None,
                               site_id=None,
                               start_time=None,
                               test_failure_by=None,
                               headers=None,
                               **request_parameters):
        """ This function is an alias of sensor_test_results_v1 .
        Args:
            site_id(basestring): siteId query parameter. Assurance site UUID .
            start_time(int): startTime query parameter. The epoch time in milliseconds .
            end_time(int): endTime query parameter. The epoch time in milliseconds .
            test_failure_by(basestring): testFailureBy query parameter. Obtain failure statistics group by "area",
                "building", or "floor" (case insensitive) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of sensor_test_results_v1 .
        """ 
        return self.sensor_test_results_v1(
                    end_time=end_time,
                    site_id=site_id,
                    start_time=start_time,
                    test_failure_by=test_failure_by,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_all80211be_profiles(self,
                                   limit=None,
                                   offset=None,
                                   headers=None,
                                   **request_parameters):
        """ This function is an alias of get_all80211be_profiles_v1 .
        Args:
            limit(int): limit query parameter.
            offset(int): offset query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_all80211be_profiles_v1 .
        """ 
        return self.get_all80211be_profiles_v1(
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def delete_interface(self,
                            id,
                            headers=None,
                            **request_parameters):
        """ This function is an alias of delete_interface_v1 .
        Args:
            id(basestring): id path parameter. Interface ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_interface_v1 .
        """ 
        return self.delete_interface_v1(
                    id=id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_ssid_count_for_specific_wireless_controller(self,
                                                           network_device_id,
                                                           admin_status=None,
                                                           managed=None,
                                                           headers=None,
                                                           **request_parameters):
        """ This function is an alias of get_ssid_count_for_specific_wireless_controller_v1 .
        Args:
            network_device_id(basestring): networkDeviceId path parameter. Obtain the network device ID value by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            admin_status(bool): adminStatus query parameter. Utilize this query parameter to obtain the number of
                SSIDs according to their administrative status. A 'true' value signifies that the admin
                status of the SSID is enabled, while a 'false' value indicates that the admin status of
                the SSID is disabled. .
            managed(bool): managed query parameter. If value is 'true' means SSIDs are configured through design.If
                the value is 'false' means out of band configuration from the Wireless Controller. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_ssid_count_for_specific_wireless_controller_v1 .
        """ 
        return self.get_ssid_count_for_specific_wireless_controller_v1(
                    network_device_id=network_device_id,
                    admin_status=admin_status,
                    managed=managed,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def provision(self,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **request_parameters):
        """ This function is an alias of provision_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of provision_v1 .
        """ 
        return self.provision_v1(
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def reboot_access_points(self,
                                apMacAddresses=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **request_parameters):
        """ This function is an alias of reboot_access_points_v1 .
        Args:
            apMacAddresses(list): Wireless's The ethernet MAC address of the access point.  (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of reboot_access_points_v1 .
        """ 
        return self.reboot_access_points_v1(
                    apMacAddresses=apMacAddresses,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def ap_provision_connectivity(self,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **request_parameters):
        """ This function is an alias of ap_provision_connectivity_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of ap_provision_connectivity_v1 .
        """ 
        return self.ap_provision_connectivity_v1(
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
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
        """ This function is an alias of create_and_provision_ssid_v1 .
        Args:
            enableFabric(boolean): Wireless's Enable SSID for Fabric .
            flexConnect(object): Wireless's flexConnect.
            managedAPLocations(list): Wireless's Managed AP Locations (Enter entire Site(s) hierarchy)  (list of
                strings).
            ssidDetails(object): Wireless's ssidDetails.
            ssidType(string): Wireless's SSID Type . Available values are 'Guest' and 'Enterprise'.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_and_provision_ssid_v1 .
        """ 
        return self.create_and_provision_ssid_v1(
                    enableFabric=enableFabric,
                    flexConnect=flexConnect,
                    managedAPLocations=managedAPLocations,
                    ssidDetails=ssidDetails,
                    ssidType=ssidType,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
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
        """ This function is an alias of create_or_update_rf_profile_v1 .
        Args:
            channelWidth(string): Wireless's Channel Width .
            defaultRfProfile(boolean): Wireless's is Default Rf Profile .
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
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_or_update_rf_profile_v1 .
        """ 
        return self.create_or_update_rf_profile_v1(
                    channelWidth=channelWidth,
                    defaultRfProfile=defaultRfProfile,
                    enableBrownField=enableBrownField,
                    enableCustom=enableCustom,
                    enableRadioTypeA=enableRadioTypeA,
                    enableRadioTypeB=enableRadioTypeB,
                    enableRadioTypeC=enableRadioTypeC,
                    name=name,
                    radioTypeAProperties=radioTypeAProperties,
                    radioTypeBProperties=radioTypeBProperties,
                    radioTypeCProperties=radioTypeCProperties,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def create_interface(self,
                            interfaceName=None,
                            vlanId=None,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **request_parameters):
        """ This function is an alias of create_interface_v1 .
        Args:
            interfaceName(string): Wireless's Interface Name .
            vlanId(integer): Wireless's VLAN ID range is 1-4094 .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_interface_v1 .
        """ 
        return self.create_interface_v1(
                    interfaceName=interfaceName,
                    vlanId=vlanId,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_ssid_details_for_specific_wireless_controller(self,
                                                             network_device_id,
                                                             admin_status=None,
                                                             limit=None,
                                                             managed=None,
                                                             offset=None,
                                                             ssid_name=None,
                                                             headers=None,
                                                             **request_parameters):
        """ This function is an alias of get_ssid_details_for_specific_wireless_controller_v1 .
        Args:
            network_device_id(basestring): networkDeviceId path parameter. Obtain the network device ID value by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            ssid_name(basestring): ssidName query parameter. Employ this query parameter to obtain the details of
                the SSID corresponding to the provided SSID name. .
            admin_status(bool): adminStatus query parameter. Utilize this query parameter to obtain the
                administrative status. A 'true' value signifies that the admin status of the SSID is
                enabled, while a 'false' value indicates that the admin status of the SSID is disabled.
                .
            managed(bool): managed query parameter. If value is 'true' means SSIDs are configured through design.If
                the value is 'false' means out of band configuration from the Wireless Controller. .
            limit(int): limit query parameter. The number of records to show for this page. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_ssid_details_for_specific_wireless_controller_v1 .
        """ 
        return self.get_ssid_details_for_specific_wireless_controller_v1(
                    network_device_id=network_device_id,
                    admin_status=admin_status,
                    limit=limit,
                    managed=managed,
                    offset=offset,
                    ssid_name=ssid_name,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def delete_ssid_and_provision_it_to_devices(self,
                                                   managed_aplocations,
                                                   ssid_name,
                                                   headers=None,
                                                   **request_parameters):
        """ This function is an alias of delete_ssid_and_provision_it_to_devices_v1 .
        Args:
            ssid_name(basestring): ssidName path parameter. SSID Name. This parameter needs to be encoded as per
                UTF-8 encoding. .
            managed_aplocations(basestring): managedAPLocations path parameter. List of managed AP locations (Site
                Hierarchies). This parameter needs to be encoded as per UTF-8 encoding .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_ssid_and_provision_it_to_devices_v1 .
        """ 
        return self.delete_ssid_and_provision_it_to_devices_v1(
                    managed_aplocations=managed_aplocations,
                    ssid_name=ssid_name,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def update_interface(self,
                            id,
                            interfaceName=None,
                            vlanId=None,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **request_parameters):
        """ This function is an alias of update_interface_v1 .
        Args:
            interfaceName(string): Wireless's Interface Name .
            vlanId(integer): Wireless's VLAN ID range is 1-4094 .
            id(basestring): id path parameter. Interface ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_interface_v1 .
        """ 
        return self.update_interface_v1(
                    id=id,
                    interfaceName=interfaceName,
                    vlanId=vlanId,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_wireless_profiles(self,
                                 limit=None,
                                 offset=None,
                                 headers=None,
                                 **request_parameters):
        """ This function is an alias of get_wireless_profiles_v1 .
        Args:
            limit(int): limit query parameter.
            offset(int): offset query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_wireless_profiles_v1 .
        """ 
        return self.get_wireless_profiles_v1(
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def update_ssid(self,
                       id,
                       site_id,
                       aaaOverride=None,
                       acctServers=None,
                       aclName=None,
                       authServer=None,
                       authServers=None,
                       authType=None,
                       basicServiceSetClientIdleTimeout=None,
                       basicServiceSetMaxIdleEnable=None,
                       cckmTsfTolerance=None,
                       clientExclusionEnable=None,
                       clientExclusionTimeout=None,
                       clientRateLimit=None,
                       coverageHoleDetectionEnable=None,
                       directedMulticastServiceEnable=None,
                       egressQos=None,
                       externalAuthIpAddress=None,
                       fastTransition=None,
                       fastTransitionOverTheDistributedSystemEnable=None,
                       ghz24Policy=None,
                       ghz6PolicyClientSteering=None,
                       ingressQos=None,
                       isApBeaconProtectionEnabled=None,
                       isAuthKey8021x=None,
                       isAuthKey8021xPlusFT=None,
                       isAuthKey8021x_SHA256=None,
                       isAuthKeyEasyPSK=None,
                       isAuthKeyOWE=None,
                       isAuthKeyPSK=None,
                       isAuthKeyPSKPlusFT=None,
                       isAuthKeyPSKSHA256=None,
                       isAuthKeySae=None,
                       isAuthKeySaeExt=None,
                       isAuthKeySaeExtPlusFT=None,
                       isAuthKeySaePlusFT=None,
                       isAuthKeySuiteB1921x=None,
                       isAuthKeySuiteB1x=None,
                       isBroadcastSSID=None,
                       isCckmEnabled=None,
                       isEnabled=None,
                       isFastLaneEnabled=None,
                       isHex=None,
                       isMacFilteringEnabled=None,
                       isPosturingEnabled=None,
                       isRandomMacFilterEnabled=None,
                       l3AuthType=None,
                       managementFrameProtectionClientprotection=None,
                       multiPSKSettings=None,
                       nasOptions=None,
                       neighborListEnable=None,
                       openSsid=None,
                       passphrase=None,
                       profileName=None,
                       protectedManagementFrame=None,
                       rsnCipherSuiteCcmp128=None,
                       rsnCipherSuiteCcmp256=None,
                       rsnCipherSuiteGcmp128=None,
                       rsnCipherSuiteGcmp256=None,
                       sessionTimeOut=None,
                       sessionTimeOutEnable=None,
                       sleepingClientEnable=None,
                       sleepingClientTimeout=None,
                       ssid=None,
                       ssidRadioType=None,
                       webPassthrough=None,
                       wlanBandSelectEnable=None,
                       wlanType=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """ This function is an alias of update_ssid_v1 .
        Args:
            aaaOverride(boolean): Wireless's Activate the AAA Override feature when set to true .
            acctServers(list): Wireless's List of Accounting server IpAddresses  (list of strings).
            aclName(string): Wireless's Pre-Auth Access Control List (ACL) Name .
            authServer(string): Wireless's Authentication Server, Mandatory for Guest SSIDs with wlanType=Guest and
                l3AuthType=web_auth . Available values are 'auth_ise', 'auth_external' and
                'auth_internal'.
            authServers(list): Wireless's List of Authentication/Authorization server IpAddresses  (list of
                strings).
            authType(string): Wireless's L2 Authentication Type (If authType is not open , then atleast one RSN
                Cipher Suite and corresponding valid AKM must be enabled) . Available values are
                'WPA2_ENTERPRISE', 'WPA2_PERSONAL', 'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL',
                'WPA2_WPA3_PERSONAL', 'WPA2_WPA3_ENTERPRISE' and 'OPEN-SECURED'.
            basicServiceSetClientIdleTimeout(integer): Wireless's This refers to the duration of inactivity,
                measured in seconds, before a client connected to the Basic Service Set is considered
                idle and timed out .
            basicServiceSetMaxIdleEnable(boolean): Wireless's Activate the maximum idle feature for the Basic
                Service Set .
            cckmTsfTolerance(integer): Wireless's Cckm TImestamp Tolerance(in milliseconds) .
            clientExclusionEnable(boolean): Wireless's Activate the feature that allows for the exclusion of clients
                .
            clientExclusionTimeout(integer): Wireless's This refers to the length of time, in seconds, a client is
                excluded or blocked from accessing the network after a specified number of unsuccessful
                attempts .
            clientRateLimit(integer): Wireless's This pertains to the maximum data transfer rate, specified in bits
                per second, that a client is permitted to achieve .
            coverageHoleDetectionEnable(boolean): Wireless's Activate Coverage Hole Detection feature when set to
                true .
            directedMulticastServiceEnable(boolean): Wireless's The Directed Multicast Service feature becomes
                operational when it is set to true .
            egressQos(string): Wireless's Egress QOS . Available values are 'PLATINUM', 'SILVER', 'GOLD' and
                'BRONZE'.
            externalAuthIpAddress(string): Wireless's External WebAuth URL (Mandatory for Guest SSIDs with wlanType
                = Guest, l3AuthType = web_auth and authServer = auth_external) .
            fastTransition(string): Wireless's Fast Transition . Available values are 'ADAPTIVE', 'ENABLE' and
                'DISABLE'.
            fastTransitionOverTheDistributedSystemEnable(boolean): Wireless's Enable Fast Transition over the
                Distributed System when set to true .
            ghz24Policy(string): Wireless's 2.4 Ghz Band Policy value. Allowed only when 2.4 Radio Band is enabled
                in ssidRadioType . Available values are 'dot11-bg-only' and 'dot11-g-only'.
            ghz6PolicyClientSteering(boolean): Wireless's True if 6 GHz Policy Client Steering is enabled, else
                False .
            ingressQos(string): Wireless's Ingress QOS . Available values are 'PLATINUM-UP', 'SILVER-UP', 'GOLD-UP'
                and 'BRONZE-UP'.
            isApBeaconProtectionEnabled(boolean): Wireless's When set to true, the Access Point (AP) Beacon
                Protection feature is activated, enhancing the security of the network. .
            isAuthKey8021x(boolean): Wireless's When set to true, the 802.1X authentication key is in use .
            isAuthKey8021xPlusFT(boolean): Wireless's When set to true, the 802.1X-Plus-FT authentication key is in
                use .
            isAuthKey8021x_SHA256(boolean): Wireless's When set to true, the feature that enables 802.1X
                authentication using the SHA256 algorithm is turned on .
            isAuthKeyEasyPSK(boolean): Wireless's When set to true, the feature that enables the use of Easy Pre-
                shared Key (PSK) authentication is activated .
            isAuthKeyOWE(boolean): Wireless's When set to true, the Opportunistic Wireless Encryption (OWE)
                authentication key feature is turned on .
            isAuthKeyPSK(boolean): Wireless's When set to true, the Pre-shared Key (PSK) authentication feature is
                enabled .
            isAuthKeyPSKPlusFT(boolean): Wireless's When set to true, the feature that enables the combination of
                Pre-shared Key (PSK) and Fast Transition (FT) authentication keys is activated .
            isAuthKeyPSKSHA256(boolean): Wireless's The feature that allows the use of Pre-shared Key (PSK)
                authentication with the SHA256 algorithm is enabled when it is set to true .
            isAuthKeySae(boolean): Wireless's When set to true, the feature enabling the Simultaneous Authentication
                of Equals (SAE) authentication key is activated .
            isAuthKeySaeExt(boolean): Wireless's When set to true, the Simultaneous Authentication of Equals (SAE)
                Extended Authentication key feature is turned on. .
            isAuthKeySaeExtPlusFT(boolean): Wireless's When set to true, the Simultaneous Authentication of Equals
                (SAE) combined with Fast Transition (FT) Authentication Key feature is enabled. .
            isAuthKeySaePlusFT(boolean): Wireless's Activating this setting by switching it to true turns on the
                authentication key feature that supports both Simultaneous Authentication of Equals
                (SAE) and Fast Transition (FT) .
            isAuthKeySuiteB1921x(boolean): Wireless's When set to true, the SuiteB192-1x authentication key feature
                is enabled. .
            isAuthKeySuiteB1x(boolean): Wireless's When activated by setting it to true, the SuiteB-1x
                authentication key feature is engaged. .
            isBroadcastSSID(boolean): Wireless's When activated by setting it to true, the Broadcast SSID feature
                will make the SSID publicly visible to wireless devices searching for available networks
                .
            isCckmEnabled(boolean): Wireless's True if CCKM is enabled, else False .
            isEnabled(boolean): Wireless's Set SSID's admin status as 'Enabled' when set to true .
            isFastLaneEnabled(boolean): Wireless's True if FastLane is enabled, else False .
            isHex(boolean): Wireless's True if passphrase is in Hex format, else False. .
            isMacFilteringEnabled(boolean): Wireless's When set to true, MAC Filtering will be activated, allowing
                control over network access based on the MAC address of the device .
            isPosturingEnabled(boolean): Wireless's Applicable only for Enterprise SSIDs. When set to True,
                Posturing will enabled. Required to be set to True if ACL needs to be mapped for
                Enterprise SSID.   .
            isRandomMacFilterEnabled(boolean): Wireless's Deny clients using randomized MAC addresses when set to
                true .
            l3AuthType(string): Wireless's L3 Authentication Type . Available values are 'open' and 'web_auth'.
            managementFrameProtectionClientprotection(string): Wireless's Management Frame Protection Client .
                Available values are 'OPTIONAL', 'DISABLED' and 'REQUIRED'.
            multiPSKSettings(list): Wireless's multiPSKSettings (list of objects).
            nasOptions(list): Wireless's Pre-Defined NAS Options : AP ETH Mac Address, AP IP address, AP Location ,
                AP MAC Address, AP Name, AP Policy Tag, AP Site Tag, SSID, System IP Address, System MAC
                Address, System Name.  (list of strings).
            neighborListEnable(boolean): Wireless's The Neighbor List feature is enabled when it is set to true .
            openSsid(string): Wireless's Open SSID which is already created in the design and not associated to any
                other OPEN-SECURED SSID .
            passphrase(string): Wireless's Passphrase (Only applicable for SSID with PERSONAL security level).
                Passphrase needs to be between 8 and 63 characters for ASCII type. HEX passphrase needs
                to be 64 characters .
            profileName(string): Wireless's WLAN Profile Name, if not passed autogenerated profile name will be
                assigned. The same wlanProfileName will also be used for policyProfileName .
            protectedManagementFrame(string): Wireless's (REQUIRED is applicable for authType WPA3_PERSONAL,
                WPA3_ENTERPRISE, OPEN_SECURED) and (OPTIONAL/REQUIRED is applicable for authType
                WPA2_WPA3_PERSONAL and WPA2_WPA3_ENTERPRISE) . Available values are 'OPTIONAL',
                'DISABLED' and 'REQUIRED'.
            rsnCipherSuiteCcmp128(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite CCMP128 encryption protocol is activated .
            rsnCipherSuiteCcmp256(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite CCMP256 encryption protocol is activated .
            rsnCipherSuiteGcmp128(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite GCMP128 encryption protocol is activated .
            rsnCipherSuiteGcmp256(boolean): Wireless's When set to true, the Robust Security Network (RSN) Cipher
                Suite GCMP256 encryption protocol is activated .
            sessionTimeOut(integer): Wireless's This denotes the allotted time span, expressed in seconds, before a
                session is automatically terminated due to inactivity .
            sessionTimeOutEnable(boolean): Wireless's Turn on the feature that imposes a time limit on user sessions
                .
            sleepingClientEnable(boolean): Wireless's When set to true, this will activate the timeout settings that
                apply to clients in sleep mode .
            sleepingClientTimeout(integer): Wireless's This refers to the amount of time, measured in minutes,
                before a sleeping (inactive) client is timed out of the network .
            ssid(string): Wireless's Name of the SSID .
            ssidRadioType(string): Wireless's Radio Policy Enum (default: Triple band operation(2.4GHz, 5GHz and
                6GHz)) . Available values are 'Triple band operation(2.4GHz, 5GHz and 6GHz)', '5GHz
                only', '2.4GHz only', '6GHz only', '2.4 and 5 GHz', '2.4 and 6 GHz' and '5 and 6 GHz'.
            webPassthrough(boolean): Wireless's When set to true, the Web-Passthrough feature will be activated for
                the Guest SSID, allowing guests to bypass certain login requirements .
            wlanBandSelectEnable(boolean): Wireless's Band select is allowed only when band options selected
                contains at least 2.4 GHz and 5 GHz band .
            wlanType(string): Wireless's Wlan Type . Available values are 'Enterprise' and 'Guest'.
            site_id(basestring): siteId path parameter. Site UUID .
            id(basestring): id path parameter. SSID ID. Inputs containing special characters should be encoded .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_ssid_v1 .
        """ 
        return self.update_ssid_v1(
                    id=id,
                    site_id=site_id,
                    aaaOverride=aaaOverride,
                    acctServers=acctServers,
                    aclName=aclName,
                    authServer=authServer,
                    authServers=authServers,
                    authType=authType,
                    basicServiceSetClientIdleTimeout=basicServiceSetClientIdleTimeout,
                    basicServiceSetMaxIdleEnable=basicServiceSetMaxIdleEnable,
                    cckmTsfTolerance=cckmTsfTolerance,
                    clientExclusionEnable=clientExclusionEnable,
                    clientExclusionTimeout=clientExclusionTimeout,
                    clientRateLimit=clientRateLimit,
                    coverageHoleDetectionEnable=coverageHoleDetectionEnable,
                    directedMulticastServiceEnable=directedMulticastServiceEnable,
                    egressQos=egressQos,
                    externalAuthIpAddress=externalAuthIpAddress,
                    fastTransition=fastTransition,
                    fastTransitionOverTheDistributedSystemEnable=fastTransitionOverTheDistributedSystemEnable,
                    ghz24Policy=ghz24Policy,
                    ghz6PolicyClientSteering=ghz6PolicyClientSteering,
                    ingressQos=ingressQos,
                    isApBeaconProtectionEnabled=isApBeaconProtectionEnabled,
                    isAuthKey8021x=isAuthKey8021x,
                    isAuthKey8021xPlusFT=isAuthKey8021xPlusFT,
                    isAuthKey8021x_SHA256=isAuthKey8021x_SHA256,
                    isAuthKeyEasyPSK=isAuthKeyEasyPSK,
                    isAuthKeyOWE=isAuthKeyOWE,
                    isAuthKeyPSK=isAuthKeyPSK,
                    isAuthKeyPSKPlusFT=isAuthKeyPSKPlusFT,
                    isAuthKeyPSKSHA256=isAuthKeyPSKSHA256,
                    isAuthKeySae=isAuthKeySae,
                    isAuthKeySaeExt=isAuthKeySaeExt,
                    isAuthKeySaeExtPlusFT=isAuthKeySaeExtPlusFT,
                    isAuthKeySaePlusFT=isAuthKeySaePlusFT,
                    isAuthKeySuiteB1921x=isAuthKeySuiteB1921x,
                    isAuthKeySuiteB1x=isAuthKeySuiteB1x,
                    isBroadcastSSID=isBroadcastSSID,
                    isCckmEnabled=isCckmEnabled,
                    isEnabled=isEnabled,
                    isFastLaneEnabled=isFastLaneEnabled,
                    isHex=isHex,
                    isMacFilteringEnabled=isMacFilteringEnabled,
                    isPosturingEnabled=isPosturingEnabled,
                    isRandomMacFilterEnabled=isRandomMacFilterEnabled,
                    l3AuthType=l3AuthType,
                    managementFrameProtectionClientprotection=managementFrameProtectionClientprotection,
                    multiPSKSettings=multiPSKSettings,
                    nasOptions=nasOptions,
                    neighborListEnable=neighborListEnable,
                    openSsid=openSsid,
                    passphrase=passphrase,
                    profileName=profileName,
                    protectedManagementFrame=protectedManagementFrame,
                    rsnCipherSuiteCcmp128=rsnCipherSuiteCcmp128,
                    rsnCipherSuiteCcmp256=rsnCipherSuiteCcmp256,
                    rsnCipherSuiteGcmp128=rsnCipherSuiteGcmp128,
                    rsnCipherSuiteGcmp256=rsnCipherSuiteGcmp256,
                    sessionTimeOut=sessionTimeOut,
                    sessionTimeOutEnable=sessionTimeOutEnable,
                    sleepingClientEnable=sleepingClientEnable,
                    sleepingClientTimeout=sleepingClientTimeout,
                    ssid=ssid,
                    ssidRadioType=ssidRadioType,
                    webPassthrough=webPassthrough,
                    wlanBandSelectEnable=wlanBandSelectEnable,
                    wlanType=wlanType,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def create_a80211be_profile(self,
                                   muMimoDownLink=None,
                                   muMimoUpLink=None,
                                   ofdmaDownLink=None,
                                   ofdmaMultiRu=None,
                                   ofdmaUpLink=None,
                                   profileName=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """ This function is an alias of create_a80211be_profile_v1 .
        Args:
            muMimoDownLink(boolean): Wireless's MU-MIMO Downlink (Default: false) .
            muMimoUpLink(boolean): Wireless's MU-MIMO Uplink (Default: false) .
            ofdmaDownLink(boolean): Wireless's OFDMA Downlink (Default: true) .
            ofdmaMultiRu(boolean): Wireless's OFDMA Multi-RU (Default: false) .
            ofdmaUpLink(boolean): Wireless's OFDMA Uplink (Default: true) .
            profileName(string): Wireless's 802.11be Profile Name .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_a80211be_profile_v1 .
        """ 
        return self.create_a80211be_profile_v1(
                    muMimoDownLink=muMimoDownLink,
                    muMimoUpLink=muMimoUpLink,
                    ofdmaDownLink=ofdmaDownLink,
                    ofdmaMultiRu=ofdmaMultiRu,
                    ofdmaUpLink=ofdmaUpLink,
                    profileName=profileName,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_wireless_profiles_count(self,
                                       headers=None,
                                       **request_parameters):
        """ This function is an alias of get_wireless_profiles_count_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_wireless_profiles_count_v1 .
        """
        return self.get_wireless_profiles_count_v1(
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_access_point_configuration(self,
                                          key,
                                          headers=None,
                                          **request_parameters):
        """ This function is an alias of get_access_point_configuration_v1 .
        Args:
            key(basestring): key query parameter. The ethernet MAC address of Access point .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_access_point_configuration_v1 .
        """ 
        return self.get_access_point_configuration_v1(
                    key=key,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def delete_rf_profiles(self,
                              rf_profile_name,
                              headers=None,
                              **request_parameters):
        """ This function is an alias of delete_rf_profiles_v1 .
        Args:
            rf_profile_name(basestring): rfProfileName path parameter. RF profile name to be deleted(required) *non-
                custom RF profile cannot be deleted .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_rf_profiles_v1 .
        """ 
        return self.delete_rf_profiles_v1(
                    rf_profile_name=rf_profile_name,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def delete_ssid(self,
                       id,
                       site_id,
                       headers=None,
                       **request_parameters):
        """ This function is an alias of delete_ssid_v1 .
        Args:
            site_id(basestring): siteId path parameter. Site UUID where SSID is to be deleted .
            id(basestring): id path parameter. SSID ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_ssid_v1 .
        """ 
        return self.delete_ssid_v1(
                    id=id,
                    site_id=site_id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def delete_enterprise_ssid(self,
                                  ssid_name,
                                  headers=None,
                                  **request_parameters):
        """ This function is an alias of delete_enterprise_ssid_v1 .
        Args:
            ssid_name(basestring): ssidName path parameter. Enter the SSID name to be deleted .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_enterprise_ssid_v1 .
        """ 
        return self.delete_enterprise_ssid_v1(
                    ssid_name=ssid_name,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def delete_wireless_profile_connectivity(self,
                                                id,
                                                headers=None,
                                                **request_parameters):
        """ This function is an alias of delete_wireless_profile_connectivity_v1 .
        Args:
            id(basestring): id path parameter. Wireless Profile Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_wireless_profile_connectivity_v1 .
        """ 
        return self.delete_wireless_profile_connectivity_v1(
                    id=id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get80211be_profiles_count(self,
                                     headers=None,
                                     **request_parameters):
        """ This function is an alias of get80211be_profiles_count_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get80211be_profiles_count_v1 .
        """
        return self.get80211be_profiles_count_v1(
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_ssid_count_by_site(self,
                                  site_id,
                                  headers=None,
                                  **request_parameters):
        """ This function is an alias of get_ssid_count_by_site_v1 .
        Args:
            site_id(basestring): siteId path parameter. Site UUID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_ssid_count_by_site_v1 .
        """ 
        return self.get_ssid_count_by_site_v1(
                    site_id=site_id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_primary_managed_ap_locations_for_specific_wireless_controller(self,
                                                                             network_device_id,
                                                                             limit=None,
                                                                             offset=None,
                                                                             headers=None,
                                                                             **request_parameters):
        """ This function is an alias of get_primary_managed_ap_locations_for_specific_wireless_controller_v1 .
        Args:
            network_device_id(basestring): networkDeviceId path parameter. Obtain the network device ID value by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            limit(int): limit query parameter. The number of records to show for this page. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_primary_managed_ap_locations_for_specific_wireless_controller_v1 .
        """ 
        return self.get_primary_managed_ap_locations_for_specific_wireless_controller_v1(
                    network_device_id=network_device_id,
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def create_wireless_profile_connectivity(self,
                                                ssidDetails=None,
                                                wirelessProfileName=None,
                                                headers=None,
                                                payload=None,
                                                active_validation=True,
                                                **request_parameters):
        """ This function is an alias of create_wireless_profile_connectivity_v1 .
        Args:
            ssidDetails(list): Wireless's ssidDetails (list of objects).
            wirelessProfileName(string): Wireless's Wireless Network Profile Name .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_wireless_profile_connectivity_v1 .
        """ 
        return self.create_wireless_profile_connectivity_v1(
                    ssidDetails=ssidDetails,
                    wirelessProfileName=wirelessProfileName,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def wireless_controller_provision(self,
                                         device_id,
                                         interfaces=None,
                                         rollingApUpgrade=None,
                                         skipApProvision=None,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **request_parameters):
        """ This function is an alias of wireless_controller_provision_v1 .
        Args:
            interfaces(list): Wireless's interfaces (list of objects).
            rollingApUpgrade(object): Wireless's rollingApUpgrade.
            skipApProvision(boolean): Wireless's True if Skip AP Provision is enabled, else False .
            device_id(basestring): deviceId path parameter. Network Device ID. This value can be obtained by using
                the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress} .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of wireless_controller_provision_v1 .
        """ 
        return self.wireless_controller_provision_v1(
                    device_id=device_id,
                    interfaces=interfaces,
                    rollingApUpgrade=rollingApUpgrade,
                    skipApProvision=skipApProvision,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_access_point_reboot_task_result(self,
                                               parent_task_id=None,
                                               headers=None,
                                               **request_parameters):
        """ This function is an alias of get_access_point_reboot_task_result_v1 .
        Args:
            parent_task_id(basestring): parentTaskId query parameter. task id of ap reboot request .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_access_point_reboot_task_result_v1 .
        """ 
        return self.get_access_point_reboot_task_result_v1(
                    parent_task_id=parent_task_id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_secondary_managed_ap_locations_for_specific_wireless_controller(self,
                                                                               network_device_id,
                                                                               limit=None,
                                                                               offset=None,
                                                                               headers=None,
                                                                               **request_parameters):
        """ This function is an alias of get_secondary_managed_ap_locations_for_specific_wireless_controller_v1 .
        Args:
            network_device_id(basestring): networkDeviceId path parameter. Obtain the network device ID value by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            limit(int): limit query parameter. The number of records to show for this page. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_secondary_managed_ap_locations_for_specific_wireless_controller_v1 .
        """ 
        return self.get_secondary_managed_ap_locations_for_specific_wireless_controller_v1(
                    network_device_id=network_device_id,
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )



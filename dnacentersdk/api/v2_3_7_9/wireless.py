# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Wireless API wrapper.

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
    deprecated,
)


class Wireless(object):
    """Cisco Catalyst Center Wireless API (version: 2.3.7.9).

    Wraps the Catalyst Center Wireless
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Wireless
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Wireless, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def sensor_test_results(
        self,
        end_time=None,
        site_id=None,
        start_time=None,
        test_failure_by=None,
        headers=None,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!sensor-test-results
        """
        check_type(headers, dict)
        check_type(site_id, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(test_failure_by, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
            "startTime": start_time,
            "endTime": end_time,
            "testFailureBy": test_failure_by,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/AssuranceGetSensorTestResults"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dde2b077d6d052dcae5a76f4aac09c1d_v2_3_7_9", json_data
        )

    def create_and_provision_ssid(
        self,
        enableFabric=None,
        flexConnect=None,
        managedAPLocations=None,
        ssidDetails=None,
        ssidType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-and-provision-s-s-i-d
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "__persistbapioutput" in headers:
                check_type(headers.get("__persistbapioutput"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "managedAPLocations": managedAPLocations,
            "ssidDetails": ssidDetails,
            "ssidType": ssidType,
            "enableFabric": enableFabric,
            "flexConnect": flexConnect,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d825ae9a117f5b6bb65b7d78fd42513c_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/ssid"
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
            "bpm_d825ae9a117f5b6bb65b7d78fd42513c_v2_3_7_9", json_data
        )

    def delete_ssid_and_provision_it_to_devices(
        self, managed_aplocations, ssid_name, headers=None, **request_parameters
    ):
        """Removes SSID or WLAN from the network profile, reprovision the device(s) and deletes the SSID or WLAN from Catalyst
        Center .

        Args:
            ssid_name(str): ssidName path parameter. SSID Name. This parameter needs to be encoded as per UTF-8
                encoding. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-s-s-i-d-and-provision-it-to-devices
        """
        check_type(headers, dict)
        check_type(ssid_name, str, may_be_none=False)
        check_type(managed_aplocations, str, may_be_none=False)
        if headers is not None:
            if "__persistbapioutput" in headers:
                check_type(headers.get("__persistbapioutput"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "ssidName": ssid_name,
            "managedAPLocations": managed_aplocations,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/ssid/{ssidName}/{managedAPLo" + "cations}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e56eb2c294159d891b7dbe493ddc434_v2_3_7_9", json_data
        )

    def reboot_access_points(
        self,
        apMacAddresses=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!reboot-access-points
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "apMacAddresses": apMacAddresses,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f5602b2965e53b5bdda193025a3fc_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/device-reboot/apreboot"
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
            "bpm_f5602b2965e53b5bdda193025a3fc_v2_3_7_9", json_data
        )

    def get_access_point_reboot_task_result(
        self, parent_task_id=None, headers=None, **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-access-point-reboot-task-result
        """
        check_type(headers, dict)
        check_type(parent_task_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "parentTaskId": parent_task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/device-reboot/apreboot/status"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ebabf7f1ce2537f8aedd93e5f5aab1b_v2_3_7_9", json_data
        )

    def get_enterprise_ssid(self, ssid_name=None, headers=None, **request_parameters):
        """Get Enterprise SSID .

        Args:
            ssid_name(str): ssidName query parameter. Enter the enterprise SSID name that needs to be retrieved. If
                not entered, all the enterprise SSIDs will be retrieved. .
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
            https://developer.cisco.com/docs/dna-center/#!get-enterprise-s-s-i-d
        """
        check_type(headers, dict)
        check_type(ssid_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "ssidName": ssid_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/enterprise-ssid"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fb757e8fce4b51ffa0ba1a8e5ae4d8c0_v2_3_7_9", json_data
        )

    def create_enterprise_ssid(
        self,
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
        **request_parameters
    ):
        """Creates enterprise SSID .

        Args:
            aaaOverride(boolean): Wireless's Aaa Override .
            authKeyMgmt(list): Wireless's Takes string inputs for the AKMs that should be set true. Possible AKM
                values : dot1x,dot1x_ft, dot1x_sha, psk, psk_ft, psk_sha, owe, sae, sae_ft  (list of
                strings).
            basicServiceSetClientIdleTimeout(integer): Wireless's Basic Service Set Client Idle Timeout .
            clientExclusionTimeout(integer): Wireless's Client Exclusion Timeout .
            clientRateLimit(number): Wireless's Client Rate Limit (in bits per second) .
            coverageHoleDetectionEnable(boolean): Wireless's Coverage Hole Detection Enable .
            enableBasicServiceSetMaxIdle(boolean): Wireless's Enable Basic Service Set Max Idle .
            enableBroadcastSSID(boolean): Wireless's Enable Broadcase SSID .
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
            radioPolicy(string): Wireless's Radio Policy Enum . Available values are 'Triple band operation(2.4GHz,
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-enterprise-s-s-i-d
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
            "name": name,
            "securityLevel": securityLevel,
            "passphrase": passphrase,
            "enableFastLane": enableFastLane,
            "enableMACFiltering": enableMACFiltering,
            "trafficType": trafficType,
            "radioPolicy": radioPolicy,
            "enableBroadcastSSID": enableBroadcastSSID,
            "fastTransition": fastTransition,
            "enableSessionTimeOut": enableSessionTimeOut,
            "sessionTimeOut": sessionTimeOut,
            "enableClientExclusion": enableClientExclusion,
            "clientExclusionTimeout": clientExclusionTimeout,
            "enableBasicServiceSetMaxIdle": enableBasicServiceSetMaxIdle,
            "basicServiceSetClientIdleTimeout": basicServiceSetClientIdleTimeout,
            "enableDirectedMulticastService": enableDirectedMulticastService,
            "enableNeighborList": enableNeighborList,
            "mfpClientProtection": mfpClientProtection,
            "nasOptions": nasOptions,
            "profileName": profileName,
            "policyProfileName": policyProfileName,
            "aaaOverride": aaaOverride,
            "coverageHoleDetectionEnable": coverageHoleDetectionEnable,
            "protectedManagementFrame": protectedManagementFrame,
            "multiPSKSettings": multiPSKSettings,
            "clientRateLimit": clientRateLimit,
            "authKeyMgmt": authKeyMgmt,
            "rsnCipherSuiteGcmp256": rsnCipherSuiteGcmp256,
            "rsnCipherSuiteCcmp256": rsnCipherSuiteCcmp256,
            "rsnCipherSuiteGcmp128": rsnCipherSuiteGcmp128,
            "ghz6PolicyClientSteering": ghz6PolicyClientSteering,
            "ghz24Policy": ghz24Policy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bc33daf690ec5399a507829abfc4fe64_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/enterprise-ssid"
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
            "bpm_bc33daf690ec5399a507829abfc4fe64_v2_3_7_9", json_data
        )

    def update_enterprise_ssid(
        self,
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
        **request_parameters
    ):
        """Update enterprise SSID .

        Args:
            aaaOverride(boolean): Wireless's Aaa Override .
            authKeyMgmt(list): Wireless's Takes string inputs for the AKMs that should be set true. Possible AKM
                values : dot1x,dot1x_ft, dot1x_sha, psk, psk_ft, psk_sha, owe, sae, sae_ft  (list of
                strings).
            basicServiceSetClientIdleTimeout(integer): Wireless's Basic Service Set Client Idle Timeout .
            clientExclusionTimeout(integer): Wireless's Client Exclusion Timeout .
            clientRateLimit(number): Wireless's Client Rate Limit (in bits per second) .
            coverageHoleDetectionEnable(boolean): Wireless's Coverage Hole Detection Enable .
            enableBasicServiceSetMaxIdle(boolean): Wireless's Enable Basic Service Set Max Idle .
            enableBroadcastSSID(boolean): Wireless's Enable Broadcase SSID .
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
            radioPolicy(string): Wireless's Radio Policy Enum . Available values are 'Triple band operation(2.4GHz,
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-enterprise-s-s-i-d
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
            "name": name,
            "securityLevel": securityLevel,
            "passphrase": passphrase,
            "enableFastLane": enableFastLane,
            "enableMACFiltering": enableMACFiltering,
            "trafficType": trafficType,
            "radioPolicy": radioPolicy,
            "enableBroadcastSSID": enableBroadcastSSID,
            "fastTransition": fastTransition,
            "enableSessionTimeOut": enableSessionTimeOut,
            "sessionTimeOut": sessionTimeOut,
            "enableClientExclusion": enableClientExclusion,
            "clientExclusionTimeout": clientExclusionTimeout,
            "enableBasicServiceSetMaxIdle": enableBasicServiceSetMaxIdle,
            "basicServiceSetClientIdleTimeout": basicServiceSetClientIdleTimeout,
            "enableDirectedMulticastService": enableDirectedMulticastService,
            "enableNeighborList": enableNeighborList,
            "mfpClientProtection": mfpClientProtection,
            "nasOptions": nasOptions,
            "profileName": profileName,
            "policyProfileName": policyProfileName,
            "aaaOverride": aaaOverride,
            "coverageHoleDetectionEnable": coverageHoleDetectionEnable,
            "protectedManagementFrame": protectedManagementFrame,
            "multiPSKSettings": multiPSKSettings,
            "clientRateLimit": clientRateLimit,
            "authKeyMgmt": authKeyMgmt,
            "rsnCipherSuiteGcmp256": rsnCipherSuiteGcmp256,
            "rsnCipherSuiteCcmp256": rsnCipherSuiteCcmp256,
            "rsnCipherSuiteGcmp128": rsnCipherSuiteGcmp128,
            "ghz6PolicyClientSteering": ghz6PolicyClientSteering,
            "ghz24Policy": ghz24Policy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_a94058a99acaaf8eb73c9227_v2_3_7_9").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/enterprise-ssid"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_a94058a99acaaf8eb73c9227_v2_3_7_9", json_data)

    def delete_enterprise_ssid(self, ssid_name, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-enterprise-s-s-i-d
        """
        check_type(headers, dict)
        check_type(ssid_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "ssidName": ssid_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/enterprise-ssid/{ssidName}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a43afa4d91a5043996c682a7a7a2d62_v2_3_7_9", json_data
        )

    def create_aaa_radius_attributes_configuration_feature_template(
        self,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to create a AAA Radius Attributes configuration feature template. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!create-a-a-a-radius-attributes-configuration-feature-template
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
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f8db651a7bb5f85a936c9fdadf3a9d9_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/aaaRadiusAt"
            + "tributesConfigurations"
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
            "bpm_f8db651a7bb5f85a936c9fdadf3a9d9_v2_3_7_9", json_data
        )

    def get_aaa_radius_attributes_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to retrieve a specific AAA Radius Attributes configuration feature template by ID. .

        Args:
            id(str): id path parameter. AAA Radius Attributes Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-a-a-a-radius-attributes-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/aaaRadiusAt"
            + "tributesConfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dbce6135f7a5581bba6893f6b134999_v2_3_7_9", json_data
        )

    def update_aaa_radius_attributes_configuration_feature_template(
        self,
        id,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to update the details of a specific AAA Radius Attributes configuration feature template
        by ID. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
            id(str): id path parameter. AAA Radius Attributes Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-a-a-a-radius-attributes-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f75156ff30d50d1bced4ec466b56b38_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/aaaRadiusAt"
            + "tributesConfigurations/{id}"
        )
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
            "bpm_f75156ff30d50d1bced4ec466b56b38_v2_3_7_9", json_data
        )

    def delete_aaa_radius_attributes_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to delete a specific AAA Radius Attributes configuration feature template by ID. .

        Args:
            id(str): id path parameter. AAA Radius Attributes Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-a-a-radius-attributes-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/aaaRadiusAt"
            + "tributesConfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b086ad8ac42656aca9efc5c7c8c1e359_v2_3_7_9", json_data
        )

    def create_advanced_ssid_configuration_feature_template(
        self,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to create a Advanced SSID configuration feature template. .

        Args:
            designName(string): Wireless's Design Name .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!create-advanced-s-s-i-d-configuration-feature-template
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
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d9c01903d0645a3d8b56172bb9549be3_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/advancedSSI"
            + "DConfigurations"
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
            "bpm_d9c01903d0645a3d8b56172bb9549be3_v2_3_7_9", json_data
        )

    def delete_advanced_ssid_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to delete a specific Advanced SSID configuration feature template by Id. .

        Args:
            id(str): id path parameter. Advanced SSID Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-advanced-s-s-i-d-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/advancedSSI"
            + "DConfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ddfe7532bb50a0b895ec9ef15528d1_v2_3_7_9", json_data
        )

    def update_advanced_ssid_configuration_feature_template(
        self,
        id,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to update the details of a specific Advanced SSID configuration feature template by ID. .

        Args:
            designName(string): Wireless's Design Name .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
            id(str): id path parameter. Advanced SSID Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-advanced-s-s-i-d-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_438d5b72acb418347ec1e1fa_v2_3_7_9").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/advancedSSI"
            + "DConfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_438d5b72acb418347ec1e1fa_v2_3_7_9", json_data)

    def get_advanced_ssid_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to retrieve a specific Advanced SSID configuration feature template by ID. .

        Args:
            id(str): id path parameter. Advanced SSID Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-advanced-s-s-i-d-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/advancedSSI"
            + "DConfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af6a62d6be8f53149d942c35f2b2aef0_v2_3_7_9", json_data
        )

    def create_clean_air_configuration_feature_template(
        self,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to create a CleanAir configuration feature template. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the first level attributes defined
                under featureAttributes.  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!create-clean-air-configuration-feature-template
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
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e8911ba7a8b54be8e443df8ac842e36_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/cleanAirCon" + "figurations"
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
            "bpm_e8911ba7a8b54be8e443df8ac842e36_v2_3_7_9", json_data
        )

    def delete_clean_air_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to delete a specific CleanAir configuration feature template by ID. .

        Args:
            id(str): id path parameter. Clean Air Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-clean-air-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/cleanAirCon"
            + "figurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f336f907fce45b8dbd74dfdf9f434bab_v2_3_7_9", json_data
        )

    def update_clean_air_configuration_feature_template(
        self,
        id,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to update the details of a specific CleanAir configuration feature template by ID. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the first level attributes defined
                under featureAttributes.  (list of strings).
            id(str): id path parameter. Clean Air Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-clean-air-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f15aaad792fc57fd89c880afc3b84dc4_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/cleanAirCon"
            + "figurations/{id}"
        )
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
            "bpm_f15aaad792fc57fd89c880afc3b84dc4_v2_3_7_9", json_data
        )

    def get_clean_air_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to retrieve a specific CleanAir configuration feature template by ID. .

        Args:
            id(str): id path parameter. Clean Air Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-clean-air-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/cleanAirCon"
            + "figurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bb41ef855e290e52b8db9cd0c43_v2_3_7_9", json_data
        )

    def create_dot11ax_configuration_feature_template(
        self,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to create a Dot11ax configuration feature template. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!create-dot11ax-configuration-feature-template
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
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ad487b01cede5cb4bdd5ee06695a6020_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/dot11axConf" + "igurations"
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
            "bpm_ad487b01cede5cb4bdd5ee06695a6020_v2_3_7_9", json_data
        )

    def get_dot11ax_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to retrieve a specific Dot11ax configuration feature template by ID. .

        Args:
            id(str): id path parameter. Dot11ax Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-dot11ax-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/dot11axConf"
            + "igurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ca4bbb8be5316a1c97bb12137145c_v2_3_7_9", json_data
        )

    def delete_dot11ax_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to delete a specific Dot11ax configuration feature template by ID. .

        Args:
            id(str): id path parameter. Dot11ax Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-dot11ax-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/dot11axConf"
            + "igurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dcbc4139ae25e7987213d7fc176663f_v2_3_7_9", json_data
        )

    def update_dot11ax_configuration_feature_template(
        self,
        id,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to update the details of a specific Dot11ax configuration feature template by ID. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
            id(str): id path parameter. Dot11ax Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-dot11ax-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bfab2e1d87654afb88c77fcfae4e407_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/dot11axConf"
            + "igurations/{id}"
        )
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
            "bpm_bfab2e1d87654afb88c77fcfae4e407_v2_3_7_9", json_data
        )

    def create_dot11be_status_configuration_feature_template(
        self,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to create a Dot11be status configuration feature template. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!create-dot11be-status-configuration-feature-template
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
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a2da4c1e5224542e8474f09eb8d4f32d_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/dot11beStat"
            + "usConfigurations"
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
            "bpm_a2da4c1e5224542e8474f09eb8d4f32d_v2_3_7_9", json_data
        )

    def delete_dot11be_status_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to delete a specific Dot11be status configuration feature template by ID. .

        Args:
            id(str): id path parameter. Dot11be Status Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-dot11be-status-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/dot11beStat"
            + "usConfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe6fe86175ce7bf566b642f7f3da0_v2_3_7_9", json_data
        )

    def update_dot11be_status_configuration_feature_template(
        self,
        id,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to update the details of a specific Dot11be status configuration feature template by ID. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
            id(str): id path parameter. Dot11be Status Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-dot11be-status-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_dfe3872e591f9f3e2a0daa358c1a_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/dot11beStat"
            + "usConfigurations/{id}"
        )
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
            "bpm_dfe3872e591f9f3e2a0daa358c1a_v2_3_7_9", json_data
        )

    def get_dot11be_status_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to retrieve a specific Dot11be status configuration feature template by ID. .

        Args:
            id(str): id path parameter. Dot11be Status Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-dot11be-status-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/dot11beStat"
            + "usConfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fb048f95b0f56209a901f6523f10c08_v2_3_7_9", json_data
        )

    def create_event_driven_r_r_m_configuration_feature_template(
        self,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to create a Event Driven RRM configuration feature template. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!create-event-driven-r-r-m-configuration-feature-template
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
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e70de44247549f9e49cfa5c6b24de9_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/eventDriven"
            + "RRMConfigurations"
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
            "bpm_e70de44247549f9e49cfa5c6b24de9_v2_3_7_9", json_data
        )

    def delete_event_driven_r_r_m_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to delete a specific Event Driven RRM configuration feature template by ID. .

        Args:
            id(str): id path parameter. Event Driven RRM Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-event-driven-r-r-m-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/eventDriven"
            + "RRMConfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e6e53e9b17d750009dcbccf6c7731b37_v2_3_7_9", json_data
        )

    def get_event_driven_r_r_m_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to retrieve a specific Event Driven RRM configuration feature template by ID. .

        Args:
            id(str): id path parameter. Event Driven RRM Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-event-driven-r-r-m-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/eventDriven"
            + "RRMConfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b1b44ebaa5561a75adcc520b42521_v2_3_7_9", json_data
        )

    def update_event_driven_r_r_m_configuration_feature_template(
        self,
        id,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to update the details of a specific Event Driven RRM configuration feature template by ID.
        .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
            id(str): id path parameter. Event Driven RRM Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-event-driven-r-r-m-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b9fbd53af6a5b46b34b17e601680801_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/eventDriven"
            + "RRMConfigurations/{id}"
        )
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
            "bpm_b9fbd53af6a5b46b34b17e601680801_v2_3_7_9", json_data
        )

    def create_flex_connect_configuration_feature_template(
        self,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to create a Flex Connect configuration feature template. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!create-flex-connect-configuration-feature-template
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
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c880bc6a8faa5bb4afbfd6bea38c75fa_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/flexConnect"
            + "Configurations"
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
            "bpm_c880bc6a8faa5bb4afbfd6bea38c75fa_v2_3_7_9", json_data
        )

    def update_flex_connect_configuration_feature_template(
        self,
        id,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to update the details of a specific Flex Connect configuration feature template by ID. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
            id(str): id path parameter. Flex Connect Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-flex-connect-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ed96d98063c5be9aa0005772dc95fc5_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/flexConnect"
            + "Configurations/{id}"
        )
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
            "bpm_ed96d98063c5be9aa0005772dc95fc5_v2_3_7_9", json_data
        )

    def delete_flex_connect_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to delete a specific Flex Connect configuration feature template by ID. .

        Args:
            id(str): id path parameter. Flex Connect Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-flex-connect-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/flexConnect"
            + "Configurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a62d88a29ff654199b64e33a44e4090b_v2_3_7_9", json_data
        )

    def get_flex_connect_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to retrieve a specific Flex Connect configuration feature template by ID. .

        Args:
            id(str): id path parameter. Flex Connect Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-flex-connect-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/flexConnect"
            + "Configurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b4c5c0515fd2982f094ed79afad4_v2_3_7_9", json_data
        )

    def create_multicast_configuration_feature_template(
        self,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to create a Multicast configuration feature template. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!create-multicast-configuration-feature-template
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
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d6451662bd1652e7bdc39053429e87a4_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/multicastCo" + "nfigurations"
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
            "bpm_d6451662bd1652e7bdc39053429e87a4_v2_3_7_9", json_data
        )

    def get_multicast_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to retrieve a specific Multicast configuration feature template by ID. .

        Args:
            id(str): id path parameter. Multicast Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-multicast-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/multicastCo"
            + "nfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a4c2d99220755fa2b3be2d16e8dac41d_v2_3_7_9", json_data
        )

    def delete_multicast_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to delete a specific Multicast configuration feature template by ID. .

        Args:
            id(str): id path parameter. Multicast Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-multicast-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/multicastCo"
            + "nfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_de576e409f555b209e2bd0d56adef888_v2_3_7_9", json_data
        )

    def update_multicast_configuration_feature_template(
        self,
        id,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to update the details of a specific Multicast configuration feature template by ID. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
            id(str): id path parameter. Multicast Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-multicast-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_de24de1222a4500cab78b4b34ee299f2_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/multicastCo"
            + "nfigurations/{id}"
        )
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
            "bpm_de24de1222a4500cab78b4b34ee299f2_v2_3_7_9", json_data
        )

    def create_r_r_m_f_r_a_configuration_feature_template(
        self,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to create a RRM FRA configuration feature template. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!create-r-r-m-f-r-a-configuration-feature-template
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
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a25f176554fb407fbe4952f1c4e_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/featureTemplates/wireless/rrmFraConfi" + "gurations"
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
            "bpm_a25f176554fb407fbe4952f1c4e_v2_3_7_9", json_data
        )

    def get_r_r_m_f_r_a_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to retrieve a specific RRM FRA configuration feature template by ID. .

        Args:
            id(str): id path parameter. RRM FRA Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-r-r-m-f-r-a-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/rrmFraConfi"
            + "gurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d56aecb1a1a859d48326e29777afa004_v2_3_7_9", json_data
        )

    def update_r_r_m_f_r_a_configuration_feature_template(
        self,
        id,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to update the details of a specific RRM FRA configuration feature template by ID. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
            id(str): id path parameter. RRM FRA Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-r-r-m-f-r-a-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f829d3e99565937b9d12c873f8faa46_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/rrmFraConfi"
            + "gurations/{id}"
        )
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
            "bpm_f829d3e99565937b9d12c873f8faa46_v2_3_7_9", json_data
        )

    def delete_r_r_m_f_r_a_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to delete a specific RRM FRA configuration feature template by Id. .

        Args:
            id(str): id path parameter. RRM FRA Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-r-r-m-f-r-a-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/rrmFraConfi"
            + "gurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b5fab4517d89246d68c8701bf9_v2_3_7_9", json_data
        )

    def create_r_r_m_general_configuration_feature_template(
        self,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to create a RRM General configuration feature template. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!create-r-r-m-general-configuration-feature-template
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
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_fe8fb526f9b3b8f3c7aaeebac_v2_3_7_9").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/rrmGeneralC" + "onfigurations"
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

        return self._object_factory("bpm_fe8fb526f9b3b8f3c7aaeebac_v2_3_7_9", json_data)

    def delete_r_r_m_general_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to delete a specific RRM General configuration feature template by ID. .

        Args:
            id(str): id path parameter. Multicast Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-r-r-m-general-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/rrmGeneralC"
            + "onfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e5192c5b056df856988b95c2fa275_v2_3_7_9", json_data
        )

    def update_r_r_m_general_configuration_feature_template(
        self,
        id,
        designName=None,
        featureAttributes=None,
        unlockedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to update the details of a specific RRM General configuration feature template by ID. .

        Args:
            designName(string): Wireless's The feature template design name. `Note:` The following characters are
                not allowed % & < > [ ] ' / .
            featureAttributes(object): Wireless's featureAttributes.
            unlockedAttributes(list): Wireless's attributes unlocked in design can be changed at device provision
                time. `Note:` unlockedAttributes can only contain the attributes defined under
                featureAttributes.  (list of strings).
            id(str): id path parameter. Multicast Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-r-r-m-general-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "designName": designName,
            "featureAttributes": featureAttributes,
            "unlockedAttributes": unlockedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d73fc407278f5eefa67e6a014aeaf742_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/rrmGeneralC"
            + "onfigurations/{id}"
        )
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
            "bpm_d73fc407278f5eefa67e6a014aeaf742_v2_3_7_9", json_data
        )

    def get_r_r_m_general_configuration_feature_template(
        self, id, headers=None, **request_parameters
    ):
        """This API allows users to retrieve a specific RRM General configuration feature template by ID. .

        Args:
            id(str): id path parameter. Multicast Configuration Feature Template Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-r-r-m-general-configuration-feature-template
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/featureTemplates/wireless/rrmGeneralC"
            + "onfigurations/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_baee7f66985144a20dfd7d40d0e074_v2_3_7_9", json_data
        )

    def get_feature_template_summary(
        self,
        design_name=None,
        limit=None,
        offset=None,
        system_template=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """This API allows users to retrieve the feature template summary. .

        Args:
            type(str): type query parameter. Feature template name. Allowed values : EVENT_DRIVEN_RRM_CONFIGURATION,
                DOT11AX_CONFIGURATION, AAA_RADIUS_ATTRIBUTES_CONFIGURATION, ADVANCED_SSID_CONFIGURATION,
                RRM_FRA_CONFIGURATION, CLEANAIR_CONFIGURATION, DOT11BE_STATUS_CONFIGURATION,
                FLEX_CONFIGURATION, MULTICAST_CONFIGURATION, RRM_GENERAL_CONFIGURATION .
            design_name(str): designName query parameter. Feature template design name. .
            limit(int): limit query parameter. The number of records to show for this page. Default is 25 if not
                specified. Maximum allowed limit is 25. .
            offset(int): offset query parameter. The first record to show for this page. The first record is
                numbered 1. .
            system_template(bool): systemTemplate query parameter. If 'True', it signifies a system-generated
                template; if 'False', it denotes a user-modifiable template. .
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
            https://developer.cisco.com/docs/dna-center/#!get-feature-template-summary
        """
        check_type(headers, dict)
        check_type(type, str)
        check_type(design_name, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(system_template, bool)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "type": type,
            "designName": design_name,
            "limit": limit,
            "offset": offset,
            "systemTemplate": system_template,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/featureTemplates/wireless/summary"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f8ab85968766525783f3fe1a529392b3_v2_3_7_9", json_data
        )

    def delete_aaa_override_vlan_settings_by_site(
        self,
        site_id,
        remove_override_in_hierarchy=None,
        headers=None,
        **request_parameters
    ):
        """This API allows the user to delete AAA Override VLAN settings at the given site level .

        Args:
            site_id(str): siteId path parameter. Site Id .
            remove_override_in_hierarchy(bool): removeOverrideInHierarchy query parameter. If the siteId pertains to
                a Global or non-Global site (e.g., Global, Area, Building, or Floor) and
                removeOverrideInHierarchy is set to true, this API will remove the override from the
                specified siteId and any child sites for the same AAA Override VLAN. If
                removeOverrideInHierarchy is set to false, the API will only remove the override from
                the specified siteId only, leaving any overrides for the AAA Override VLAN at child
                sites unaffected. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-a-a-override-vlan-settings-by-site
        """
        check_type(headers, dict)
        check_type(remove_override_in_hierarchy, bool)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "removeOverrideInHierarchy": remove_override_in_hierarchy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexC"
            + "onnectAaaOverride"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bb5bd77c415e9982e01c07a6b1f165_v2_3_7_9", json_data
        )

    def get_aaa_override_vlan_settings_by_site(
        self, site_id, headers=None, **request_parameters
    ):
        """This API allows the user to get all Flex Connect AAA Override VLAN settings at the given site .

        Args:
            site_id(str): siteId path parameter. Site Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-a-a-a-override-vlan-settings-by-site
        """
        check_type(headers, dict)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexC"
            + "onnectAaaOverride"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c3ad5ef56595f45b59c8df890955e02_v2_3_7_9", json_data
        )

    def update_aaa_override_vlan_settings_by_site(
        self,
        site_id,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to update an existing AAA Override VLAN setting at the given site level .

        Args:
            site_id(str): siteId path parameter. Site UUID .
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
            https://developer.cisco.com/docs/dna-center/#!update-a-a-a-override-vlan-settings-by-site
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_a41ac8d894e5ee98fc9324fb8488174_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexC"
            + "onnectAaaOverride"
        )
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
            "bpm_a41ac8d894e5ee98fc9324fb8488174_v2_3_7_9", json_data
        )

    def update_native_vlan_settings_by_site(
        self,
        site_id,
        nativeVlanId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to update an existing Native VLAN setting at the given site level. The default value of
        the native VLAN on the device is 1 when nothing is explicitly set. .

        Args:
            nativeVlanId(integer): Wireless's Native VLAN ID is used for any untagged frames.Range is 1 to 4094 .
            site_id(str): siteId path parameter. Site Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-native-vlan-settings-by-site
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }
        _payload = {
            "nativeVlanId": nativeVlanId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_da24bdb30635515395471fe644cdc7b5_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexC"
            + "onnectNativeVlan"
        )
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
            "bpm_da24bdb30635515395471fe644cdc7b5_v2_3_7_9", json_data
        )

    def delete_native_vlan_settings_by_site(
        self,
        site_id,
        remove_override_in_hierarchy=None,
        headers=None,
        **request_parameters
    ):
        """This API allows the user to delete a Native VLAN setting at the given site level. .

        Args:
            site_id(str): siteId path parameter. Site Id .
            remove_override_in_hierarchy(bool): removeOverrideInHierarchy query parameter. If the siteId pertains to
                a Global or non-Global site (e.g., Global, Area, Building, or Floor) and
                removeOverrideInHierarchy is set to true, this API will remove the override from the
                specified siteId and any child sites for the same Native VLAN. If
                removeOverrideInHierarchy is set to false, the API will only remove the override from
                the specified siteId only, leaving any overrides for the Native VLAN at child sites
                unaffected. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-native-vlan-settings-by-site
        """
        check_type(headers, dict)
        check_type(remove_override_in_hierarchy, bool)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "removeOverrideInHierarchy": remove_override_in_hierarchy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexC"
            + "onnectNativeVlan"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d113be505795a139cbffc189fcd6_v2_3_7_9", json_data
        )

    def get_native_vlan_settings_by_site(
        self, site_id, headers=None, **request_parameters
    ):
        """This API allows the user to get all Native VLAN Settings at the given site. The default value of the native VLAN
        on the device is 1 when nothing is explicitly set. .

        Args:
            site_id(str): siteId path parameter. Site Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-native-vlan-settings-by-site
        """
        check_type(headers, dict)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexC"
            + "onnectNativeVlan"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_a13f951d58006466042473c73_v2_3_7_9", json_data)

    def create_ssid(
        self,
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
        isRadiusProfilingEnabled=None,
        isRandomMacFilterEnabled=None,
        l3AuthType=None,
        managementFrameProtectionClientprotection=None,
        multiPSKSettings=None,
        nasOptions=None,
        neighborListEnable=None,
        openSsid=None,
        passphrase=None,
        policyProfileName=None,
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
        **request_parameters
    ):
        """This API allows the user to create an SSID (Service Set Identifier) at the Global site .

        Args:
            aaaOverride(boolean): Wireless's Activate the AAA Override feature when set to true .
            acctServers(list): Wireless's List of Accounting server IpAddresses  (list of strings).
            aclName(string): Wireless's Pre-Auth Access Control List (ACL) Name .
            authServer(string): Wireless's For Guest SSIDs ('wlanType' is 'Guest' and 'l3AuthType' is 'web_auth'),
                the Authentication Server('authServer') is mandatory. Otherwise, it defaults to
                'auth_external'. . Available values are 'auth_ise', 'auth_external' and 'auth_internal'.
            authServers(list): Wireless's List of Authentication/Authorization server IpAddresses  (list of
                strings).
            authType(string): Wireless's L2 Authentication Type (If authType is not open , then atleast one RSN
                Cipher Suite and corresponding valid AKM must be enabled). Default is L2 Authentication
                Type if exists else None. . Available values are 'WPA2_ENTERPRISE', 'WPA2_PERSONAL',
                'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL', 'WPA2_WPA3_PERSONAL', 'WPA2_WPA3_ENTERPRISE'
                and 'OPEN-SECURED'.
            basicServiceSetClientIdleTimeout(integer): Wireless's This refers to the duration of inactivity,
                measured in seconds, before a client connected to the Basic Service Set is considered
                idle and timed out. Default is Basic ServiceSet ClientIdle Timeout if exists else 300.
                If it needs to be disabled , pass 0 as its value else valid range is [15 to 100000]. .
            basicServiceSetMaxIdleEnable(boolean): Wireless's Activate the maximum idle feature for the Basic
                Service Set .
            cckmTsfTolerance(integer): Wireless's he default value is the Cckm Timestamp Tolerance (in milliseconds,
                if specified); otherwise, it is 0. .
            clientExclusionEnable(boolean): Wireless's Activate the feature that allows for the exclusion of clients
                .
            clientExclusionTimeout(integer): Wireless's This refers to the length of time, in seconds, a client is
                excluded or blocked from accessing the network after a specified number of unsuccessful
                attempts. Default is Client Exclusion Timeout if exists else 180. .
            clientRateLimit(integer): Wireless's This pertains to the maximum data transfer rate, specified in bits
                per second, that a client is permitted to achieve. It should be in mutliples of 500 .
                Default is Client Rate Limit if exists else 0. .
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
                Enterprise SSID. .
            isRadiusProfilingEnabled(boolean): Wireless's 'true' if Radius profiling needs to be enabled, defaults
                to 'false' if not specified. At least one AAA/PSN server is required to enable Radius
                Profiling. .
            isRandomMacFilterEnabled(boolean): Wireless's Deny clients using randomized MAC addresses when set to
                true .
            l3AuthType(string): Wireless's L3 Authentication Type. When 'wlanType' is 'Enterprise', ‘l3AuthType' is
                optional and defaults to 'open' if not specified. If 'wlanType' is 'Guest' then
                'l3AuthType' is mandatory. . Available values are 'open' and 'web_auth'.
            managementFrameProtectionClientprotection(string): Wireless's Default is Management Frame Protection
                Client if exists else Optional. . Available values are 'OPTIONAL', 'DISABLED' and
                'REQUIRED'.
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
            policyProfileName(string): Wireless's Policy Profile Name. If 'policyProfileName' is not provided, the
                value of 'profileName' will be assigned to it. If 'profileName' is also not provided, an
                autogenerated name will be used. Autogenerated name is generated by appending ‘ssid’
                field’s value with ‘_profile’ (Example : If ‘ssid’ = ‘ExampleSsid’, then autogenerated
                name will be ‘ExampleSsid_profile’). .
            profileName(string): Wireless's WLAN Profile Name, if not passed autogenerated profile name will be
                assigned. .
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
                session is automatically terminated due to inactivity. Default sessionTimeOut is 1800. .
            sessionTimeOutEnable(boolean): Wireless's Turn on the feature that imposes a time limit on user sessions
                .
            sleepingClientEnable(boolean): Wireless's When set to true, this will activate the timeout settings that
                apply to clients in sleep mode .
            sleepingClientTimeout(integer): Wireless's This refers to the amount of time, measured in minutes,
                before a sleeping (inactive) client is timed out of the network. Default is Sleeping
                Client Timeout if exists else 720. .
            ssid(string): Wireless's Name of the SSID .
            ssidRadioType(string): Wireless's Radio Policy Enum (default: Triple band operation(2.4GHz, 5GHz and
                6GHz)) . Available values are 'Triple band operation(2.4GHz, 5GHz and 6GHz)', '5GHz
                only', '2.4GHz only', '6GHz only', '2.4 and 5 GHz', '2.4 and 6 GHz' and '5 and 6 GHz'.
            webPassthrough(boolean): Wireless's When set to true, the Web-Passthrough feature will be activated for
                the Guest SSID, allowing guests to bypass certain login requirements .
            wlanBandSelectEnable(boolean): Wireless's Band select is allowed only when band options selected
                contains at least 2.4 GHz and 5 GHz band else false. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-s-s-i-d
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }
        _payload = {
            "ssid": ssid,
            "authType": authType,
            "passphrase": passphrase,
            "isFastLaneEnabled": isFastLaneEnabled,
            "isMacFilteringEnabled": isMacFilteringEnabled,
            "ssidRadioType": ssidRadioType,
            "isBroadcastSSID": isBroadcastSSID,
            "fastTransition": fastTransition,
            "sessionTimeOutEnable": sessionTimeOutEnable,
            "sessionTimeOut": sessionTimeOut,
            "clientExclusionEnable": clientExclusionEnable,
            "clientExclusionTimeout": clientExclusionTimeout,
            "basicServiceSetMaxIdleEnable": basicServiceSetMaxIdleEnable,
            "basicServiceSetClientIdleTimeout": basicServiceSetClientIdleTimeout,
            "directedMulticastServiceEnable": directedMulticastServiceEnable,
            "neighborListEnable": neighborListEnable,
            "managementFrameProtectionClientprotection": managementFrameProtectionClientprotection,
            "nasOptions": nasOptions,
            "profileName": profileName,
            "aaaOverride": aaaOverride,
            "coverageHoleDetectionEnable": coverageHoleDetectionEnable,
            "protectedManagementFrame": protectedManagementFrame,
            "multiPSKSettings": multiPSKSettings,
            "clientRateLimit": clientRateLimit,
            "rsnCipherSuiteGcmp256": rsnCipherSuiteGcmp256,
            "rsnCipherSuiteCcmp256": rsnCipherSuiteCcmp256,
            "rsnCipherSuiteGcmp128": rsnCipherSuiteGcmp128,
            "rsnCipherSuiteCcmp128": rsnCipherSuiteCcmp128,
            "ghz6PolicyClientSteering": ghz6PolicyClientSteering,
            "isAuthKey8021x": isAuthKey8021x,
            "isAuthKey8021xPlusFT": isAuthKey8021xPlusFT,
            "isAuthKey8021x_SHA256": isAuthKey8021x_SHA256,
            "isAuthKeySae": isAuthKeySae,
            "isAuthKeySaePlusFT": isAuthKeySaePlusFT,
            "isAuthKeyPSK": isAuthKeyPSK,
            "isAuthKeyPSKPlusFT": isAuthKeyPSKPlusFT,
            "isAuthKeyOWE": isAuthKeyOWE,
            "isAuthKeyEasyPSK": isAuthKeyEasyPSK,
            "isAuthKeyPSKSHA256": isAuthKeyPSKSHA256,
            "openSsid": openSsid,
            "wlanBandSelectEnable": wlanBandSelectEnable,
            "isEnabled": isEnabled,
            "authServers": authServers,
            "acctServers": acctServers,
            "egressQos": egressQos,
            "ingressQos": ingressQos,
            "wlanType": wlanType,
            "l3AuthType": l3AuthType,
            "authServer": authServer,
            "externalAuthIpAddress": externalAuthIpAddress,
            "webPassthrough": webPassthrough,
            "sleepingClientEnable": sleepingClientEnable,
            "sleepingClientTimeout": sleepingClientTimeout,
            "aclName": aclName,
            "isPosturingEnabled": isPosturingEnabled,
            "isAuthKeySuiteB1x": isAuthKeySuiteB1x,
            "isAuthKeySuiteB1921x": isAuthKeySuiteB1921x,
            "isAuthKeySaeExt": isAuthKeySaeExt,
            "isAuthKeySaeExtPlusFT": isAuthKeySaeExtPlusFT,
            "isApBeaconProtectionEnabled": isApBeaconProtectionEnabled,
            "ghz24Policy": ghz24Policy,
            "cckmTsfTolerance": cckmTsfTolerance,
            "isCckmEnabled": isCckmEnabled,
            "isHex": isHex,
            "isRandomMacFilterEnabled": isRandomMacFilterEnabled,
            "fastTransitionOverTheDistributedSystemEnable": fastTransitionOverTheDistributedSystemEnable,
            "isRadiusProfilingEnabled": isRadiusProfilingEnabled,
            "policyProfileName": policyProfileName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_aa663ca2bd1f5a3db67c405987495112_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids"
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
            "bpm_aa663ca2bd1f5a3db67c405987495112_v2_3_7_9", json_data
        )

    def get_ssid_by_site(
        self,
        site_id,
        auth_type=None,
        l3auth_type=None,
        limit=None,
        offset=None,
        ssid=None,
        wlan_type=None,
        headers=None,
        **request_parameters
    ):
        """This API allows the user to get all SSIDs (Service Set Identifier) at the given site .

        Args:
            site_id(str): siteId path parameter. Site UUID .
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            ssid(str): ssid query parameter. SSID Name .
            wlan_type(str): wlanType query parameter. Wlan Type .
            auth_type(str): authType query parameter. Auth Type .
            l3auth_type(str): l3authType query parameter. L3 Auth Type .
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
            https://developer.cisco.com/docs/dna-center/#!get-s-s-i-d-by-site
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(ssid, str)
        check_type(wlan_type, str)
        check_type(auth_type, str)
        check_type(l3auth_type, str)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "ssid": ssid,
            "wlanType": wlan_type,
            "authType": auth_type,
            "l3authType": l3auth_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ae5ed21186c55f9c8485a57cebf85562_v2_3_7_9", json_data
        )

    def get_ssid_count_by_site(
        self, site_id, inherited=None, headers=None, **request_parameters
    ):
        """This API allows the user to get count of all SSIDs (Service Set Identifier) . .

        Args:
            site_id(str): siteId path parameter. Site UUID .
            inherited(bool): _inherited query parameter. This query parameter indicates whether the current SSID
                count at the given 'siteId' is of the SSID(s) it is inheriting or count of non-
                inheriting SSID(s) .
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
            https://developer.cisco.com/docs/dna-center/#!get-s-s-i-d-count-by-site
        """
        check_type(headers, dict)
        check_type(inherited, bool)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "_inherited": inherited,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids" + "/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_de3663dc582ebcd90a67635ae18a_v2_3_7_9", json_data
        )

    def get_ssid_by_id(self, id, site_id, headers=None, **request_parameters):
        """This API allows the user to get an SSID (Service Set Identifier) by ID at the given site .

        Args:
            site_id(str): siteId path parameter. Site UUID .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-s-s-i-d-by-i-d
        """
        check_type(headers, dict)
        check_type(site_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids" + "/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c300d8fe965b278388c9aeca543053_v2_3_7_9", json_data
        )

    def update_ssid(
        self,
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
        isRadiusProfilingEnabled=None,
        isRandomMacFilterEnabled=None,
        l3AuthType=None,
        managementFrameProtectionClientprotection=None,
        multiPSKSettings=None,
        nasOptions=None,
        neighborListEnable=None,
        openSsid=None,
        passphrase=None,
        policyProfileName=None,
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
        **request_parameters
    ):
        """This API allows the user to update an SSID (Service Set Identifier) at the given site .

        Args:
            aaaOverride(boolean): Wireless's Activate the AAA Override feature when set to true .
            acctServers(list): Wireless's List of Accounting server IpAddresses  (list of strings).
            aclName(string): Wireless's Pre-Auth Access Control List (ACL) Name .
            authServer(string): Wireless's For Guest SSIDs ('wlanType' is 'Guest' and 'l3AuthType' is 'web_auth'),
                the Authentication Server('authServer') is mandatory. Otherwise, it defaults to
                'auth_external'. . Available values are 'auth_ise', 'auth_external' and 'auth_internal'.
            authServers(list): Wireless's List of Authentication/Authorization server IpAddresses  (list of
                strings).
            authType(string): Wireless's L2 Authentication Type (If authType is not open , then atleast one RSN
                Cipher Suite and corresponding valid AKM must be enabled). Default is L2 Authentication
                Type if exists else None. . Available values are 'WPA2_ENTERPRISE', 'WPA2_PERSONAL',
                'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL', 'WPA2_WPA3_PERSONAL', 'WPA2_WPA3_ENTERPRISE'
                and 'OPEN-SECURED'.
            basicServiceSetClientIdleTimeout(integer): Wireless's This refers to the duration of inactivity,
                measured in seconds, before a client connected to the Basic Service Set is considered
                idle and timed out. Default is Basic ServiceSet ClientIdle Timeout if exists else 300.
                If it needs to be disabled , pass 0 as its value else valid range is [15 to 100000]. .
            basicServiceSetMaxIdleEnable(boolean): Wireless's Activate the maximum idle feature for the Basic
                Service Set .
            cckmTsfTolerance(integer): Wireless's he default value is the Cckm Timestamp Tolerance (in milliseconds,
                if specified); otherwise, it is 0. .
            clientExclusionEnable(boolean): Wireless's Activate the feature that allows for the exclusion of clients
                .
            clientExclusionTimeout(integer): Wireless's This refers to the length of time, in seconds, a client is
                excluded or blocked from accessing the network after a specified number of unsuccessful
                attempts. Default is Client Exclusion Timeout if exists else 180. .
            clientRateLimit(integer): Wireless's This pertains to the maximum data transfer rate, specified in bits
                per second, that a client is permitted to achieve. It should be in mutliples of 500 .
                Default is Client Rate Limit if exists else 0. .
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
                Enterprise SSID. .
            isRadiusProfilingEnabled(boolean): Wireless's 'true' if Radius profiling needs to be enabled, defaults
                to 'false' if not specified. At least one AAA/PSN server is required to enable Radius
                Profiling. .
            isRandomMacFilterEnabled(boolean): Wireless's Deny clients using randomized MAC addresses when set to
                true .
            l3AuthType(string): Wireless's L3 Authentication Type. When 'wlanType' is 'Enterprise', ‘l3AuthType' is
                optional and defaults to 'open' if not specified. If 'wlanType' is 'Guest' then
                'l3AuthType' is mandatory. . Available values are 'open' and 'web_auth'.
            managementFrameProtectionClientprotection(string): Wireless's Default is Management Frame Protection
                Client if exists else Optional. . Available values are 'OPTIONAL', 'DISABLED' and
                'REQUIRED'.
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
            policyProfileName(string): Wireless's Policy Profile Name. If 'policyProfileName' is not provided, the
                value of 'profileName' will be assigned to it. If 'profileName' is also not provided, an
                autogenerated name will be used. Autogenerated name is generated by appending ‘ssid’
                field’s value with ‘_profile’ (Example : If ‘ssid’ = ‘ExampleSsid’, then autogenerated
                name will be ‘ExampleSsid_profile’). .
            profileName(string): Wireless's WLAN Profile Name, if not passed autogenerated profile name will be
                assigned. .
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
                session is automatically terminated due to inactivity. Default sessionTimeOut is 1800. .
            sessionTimeOutEnable(boolean): Wireless's Turn on the feature that imposes a time limit on user sessions
                .
            sleepingClientEnable(boolean): Wireless's When set to true, this will activate the timeout settings that
                apply to clients in sleep mode .
            sleepingClientTimeout(integer): Wireless's This refers to the amount of time, measured in minutes,
                before a sleeping (inactive) client is timed out of the network. Default is Sleeping
                Client Timeout if exists else 720. .
            ssid(string): Wireless's Name of the SSID .
            ssidRadioType(string): Wireless's Radio Policy Enum (default: Triple band operation(2.4GHz, 5GHz and
                6GHz)) . Available values are 'Triple band operation(2.4GHz, 5GHz and 6GHz)', '5GHz
                only', '2.4GHz only', '6GHz only', '2.4 and 5 GHz', '2.4 and 6 GHz' and '5 and 6 GHz'.
            webPassthrough(boolean): Wireless's When set to true, the Web-Passthrough feature will be activated for
                the Guest SSID, allowing guests to bypass certain login requirements .
            wlanBandSelectEnable(boolean): Wireless's Band select is allowed only when band options selected
                contains at least 2.4 GHz and 5 GHz band else false. .
            wlanType(string): Wireless's Wlan Type . Available values are 'Enterprise' and 'Guest'.
            site_id(str): siteId path parameter. Site UUID .
            id(str): id path parameter. SSID ID .
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
            https://developer.cisco.com/docs/dna-center/#!update-s-s-i-d
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
            "id": id,
        }
        _payload = {
            "ssid": ssid,
            "authType": authType,
            "passphrase": passphrase,
            "isFastLaneEnabled": isFastLaneEnabled,
            "isMacFilteringEnabled": isMacFilteringEnabled,
            "ssidRadioType": ssidRadioType,
            "isBroadcastSSID": isBroadcastSSID,
            "fastTransition": fastTransition,
            "sessionTimeOutEnable": sessionTimeOutEnable,
            "sessionTimeOut": sessionTimeOut,
            "clientExclusionEnable": clientExclusionEnable,
            "clientExclusionTimeout": clientExclusionTimeout,
            "basicServiceSetMaxIdleEnable": basicServiceSetMaxIdleEnable,
            "basicServiceSetClientIdleTimeout": basicServiceSetClientIdleTimeout,
            "directedMulticastServiceEnable": directedMulticastServiceEnable,
            "neighborListEnable": neighborListEnable,
            "managementFrameProtectionClientprotection": managementFrameProtectionClientprotection,
            "nasOptions": nasOptions,
            "profileName": profileName,
            "aaaOverride": aaaOverride,
            "coverageHoleDetectionEnable": coverageHoleDetectionEnable,
            "protectedManagementFrame": protectedManagementFrame,
            "multiPSKSettings": multiPSKSettings,
            "clientRateLimit": clientRateLimit,
            "rsnCipherSuiteGcmp256": rsnCipherSuiteGcmp256,
            "rsnCipherSuiteCcmp256": rsnCipherSuiteCcmp256,
            "rsnCipherSuiteGcmp128": rsnCipherSuiteGcmp128,
            "rsnCipherSuiteCcmp128": rsnCipherSuiteCcmp128,
            "ghz6PolicyClientSteering": ghz6PolicyClientSteering,
            "isAuthKey8021x": isAuthKey8021x,
            "isAuthKey8021xPlusFT": isAuthKey8021xPlusFT,
            "isAuthKey8021x_SHA256": isAuthKey8021x_SHA256,
            "isAuthKeySae": isAuthKeySae,
            "isAuthKeySaePlusFT": isAuthKeySaePlusFT,
            "isAuthKeyPSK": isAuthKeyPSK,
            "isAuthKeyPSKPlusFT": isAuthKeyPSKPlusFT,
            "isAuthKeyOWE": isAuthKeyOWE,
            "isAuthKeyEasyPSK": isAuthKeyEasyPSK,
            "isAuthKeyPSKSHA256": isAuthKeyPSKSHA256,
            "openSsid": openSsid,
            "wlanBandSelectEnable": wlanBandSelectEnable,
            "isEnabled": isEnabled,
            "authServers": authServers,
            "acctServers": acctServers,
            "egressQos": egressQos,
            "ingressQos": ingressQos,
            "wlanType": wlanType,
            "l3AuthType": l3AuthType,
            "authServer": authServer,
            "externalAuthIpAddress": externalAuthIpAddress,
            "webPassthrough": webPassthrough,
            "sleepingClientEnable": sleepingClientEnable,
            "sleepingClientTimeout": sleepingClientTimeout,
            "aclName": aclName,
            "isPosturingEnabled": isPosturingEnabled,
            "isAuthKeySuiteB1x": isAuthKeySuiteB1x,
            "isAuthKeySuiteB1921x": isAuthKeySuiteB1921x,
            "isAuthKeySaeExt": isAuthKeySaeExt,
            "isAuthKeySaeExtPlusFT": isAuthKeySaeExtPlusFT,
            "isApBeaconProtectionEnabled": isApBeaconProtectionEnabled,
            "ghz24Policy": ghz24Policy,
            "cckmTsfTolerance": cckmTsfTolerance,
            "isCckmEnabled": isCckmEnabled,
            "isHex": isHex,
            "isRandomMacFilterEnabled": isRandomMacFilterEnabled,
            "fastTransitionOverTheDistributedSystemEnable": fastTransitionOverTheDistributedSystemEnable,
            "isRadiusProfilingEnabled": isRadiusProfilingEnabled,
            "policyProfileName": policyProfileName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a602eee5a56faa64436bade8a240e_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids" + "/{id}"
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
            "bpm_a602eee5a56faa64436bade8a240e_v2_3_7_9", json_data
        )

    def delete_ssid(
        self,
        id,
        site_id,
        remove_override_in_hierarchy=None,
        headers=None,
        **request_parameters
    ):
        """This API allows the user to delete an SSID (Service Set Identifier) at the global level , if the SSID is not
        mapped to any Wireless Profile, Or remove override from given site Id . .

        Args:
            site_id(str): siteId path parameter. Site UUID where SSID is to be deleted .
            id(str): id path parameter. SSID ID .
            remove_override_in_hierarchy(bool): removeOverrideInHierarchy query parameter. Remove override in
                hierarchy . Refer Feature tab for details .
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
            https://developer.cisco.com/docs/dna-center/#!delete-s-s-i-d
        """
        check_type(headers, dict)
        check_type(remove_override_in_hierarchy, bool)
        check_type(site_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "removeOverrideInHierarchy": remove_override_in_hierarchy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids" + "/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_be7fef60e7b5cdbabd4b93f6a0b4b68_v2_3_7_9", json_data
        )

    def update_or_overridessid(
        self,
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
        isRadiusProfilingEnabled=None,
        isRandomMacFilterEnabled=None,
        l3AuthType=None,
        managementFrameProtectionClientprotection=None,
        multiPSKSettings=None,
        nasOptions=None,
        neighborListEnable=None,
        openSsid=None,
        passphrase=None,
        policyProfileName=None,
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
        **request_parameters
    ):
        """This API allows to either update SSID at global 'siteId' or override SSID at given non-global 'siteId' .

        Args:
            aaaOverride(boolean): Wireless's Activate the AAA Override feature when set to true .
            acctServers(list): Wireless's List of Accounting server IpAddresses  (list of strings).
            aclName(string): Wireless's Pre-Auth Access Control List (ACL) Name .
            authServer(string): Wireless's For Guest SSIDs ('wlanType' is 'Guest' and 'l3AuthType' is 'web_auth'),
                the Authentication Server('authServer') is mandatory. Otherwise, it defaults to
                'auth_external'. . Available values are 'auth_ise', 'auth_external' and 'auth_internal'.
            authServers(list): Wireless's List of Authentication/Authorization server IpAddresses  (list of
                strings).
            authType(string): Wireless's L2 Authentication Type (If authType is not open , then atleast one RSN
                Cipher Suite and corresponding valid AKM must be enabled) . Available values are
                'WPA2_ENTERPRISE', 'WPA2_PERSONAL', 'OPEN', 'WPA3_ENTERPRISE', 'WPA3_PERSONAL',
                'WPA2_WPA3_PERSONAL', 'WPA2_WPA3_ENTERPRISE' and 'OPEN-SECURED'.
            basicServiceSetClientIdleTimeout(integer): Wireless's This refers to the duration of inactivity,
                measured in seconds, before a client connected to the Basic Service Set is considered
                idle and timed out. Default is Basic ServiceSet ClientIdle Timeout if exists else 300.
                If it needs to be disabled , pass 0 as its value else valid range is [15 to 100000]. .
            basicServiceSetMaxIdleEnable(boolean): Wireless's Activate the maximum idle feature for the Basic
                Service Set .
            cckmTsfTolerance(integer): Wireless's The default value is the Cckm Timestamp Tolerance (in
                milliseconds, if specified); otherwise, it is 0. .
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
                Enterprise SSID. .
            isRadiusProfilingEnabled(boolean): Wireless's 'true' if Radius profiling needs to be enabled, defaults
                to 'false' if not specified. At least one AAA/PSN server is required to enable Radius
                Profiling. .
            isRandomMacFilterEnabled(boolean): Wireless's Deny clients using randomized MAC addresses when set to
                true .
            l3AuthType(string): Wireless's L3 Authentication Type. When 'wlanType' is 'Enterprise', ‘l3AuthType' is
                optional and defaults to 'open' if not specified. If 'wlanType' is 'Guest' then
                'l3AuthType' is mandatory. . Available values are 'open' and 'web_auth'.
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
            policyProfileName(string): Wireless's Policy Profile Name. .
            profileName(string): Wireless's WLAN Profile Name, if not passed autogenerated profile name will be
                assigned. .
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
                session is automatically terminated due to inactivity. Default sessionTimeOut is 1800. .
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
            id(str): id path parameter. SSID ID .
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
            https://developer.cisco.com/docs/dna-center/#!update-or-override-s-s-i-d
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
            "id": id,
        }
        _payload = {
            "ssid": ssid,
            "authType": authType,
            "passphrase": passphrase,
            "isFastLaneEnabled": isFastLaneEnabled,
            "isMacFilteringEnabled": isMacFilteringEnabled,
            "ssidRadioType": ssidRadioType,
            "isBroadcastSSID": isBroadcastSSID,
            "fastTransition": fastTransition,
            "sessionTimeOutEnable": sessionTimeOutEnable,
            "sessionTimeOut": sessionTimeOut,
            "clientExclusionEnable": clientExclusionEnable,
            "clientExclusionTimeout": clientExclusionTimeout,
            "basicServiceSetMaxIdleEnable": basicServiceSetMaxIdleEnable,
            "basicServiceSetClientIdleTimeout": basicServiceSetClientIdleTimeout,
            "directedMulticastServiceEnable": directedMulticastServiceEnable,
            "neighborListEnable": neighborListEnable,
            "managementFrameProtectionClientprotection": managementFrameProtectionClientprotection,
            "nasOptions": nasOptions,
            "profileName": profileName,
            "aaaOverride": aaaOverride,
            "coverageHoleDetectionEnable": coverageHoleDetectionEnable,
            "protectedManagementFrame": protectedManagementFrame,
            "multiPSKSettings": multiPSKSettings,
            "clientRateLimit": clientRateLimit,
            "rsnCipherSuiteGcmp256": rsnCipherSuiteGcmp256,
            "rsnCipherSuiteCcmp256": rsnCipherSuiteCcmp256,
            "rsnCipherSuiteGcmp128": rsnCipherSuiteGcmp128,
            "rsnCipherSuiteCcmp128": rsnCipherSuiteCcmp128,
            "ghz6PolicyClientSteering": ghz6PolicyClientSteering,
            "isAuthKey8021x": isAuthKey8021x,
            "isAuthKey8021xPlusFT": isAuthKey8021xPlusFT,
            "isAuthKey8021x_SHA256": isAuthKey8021x_SHA256,
            "isAuthKeySae": isAuthKeySae,
            "isAuthKeySaePlusFT": isAuthKeySaePlusFT,
            "isAuthKeyPSK": isAuthKeyPSK,
            "isAuthKeyPSKPlusFT": isAuthKeyPSKPlusFT,
            "isAuthKeyOWE": isAuthKeyOWE,
            "isAuthKeyEasyPSK": isAuthKeyEasyPSK,
            "isAuthKeyPSKSHA256": isAuthKeyPSKSHA256,
            "openSsid": openSsid,
            "wlanBandSelectEnable": wlanBandSelectEnable,
            "isEnabled": isEnabled,
            "authServers": authServers,
            "acctServers": acctServers,
            "egressQos": egressQos,
            "ingressQos": ingressQos,
            "wlanType": wlanType,
            "l3AuthType": l3AuthType,
            "authServer": authServer,
            "externalAuthIpAddress": externalAuthIpAddress,
            "webPassthrough": webPassthrough,
            "sleepingClientEnable": sleepingClientEnable,
            "sleepingClientTimeout": sleepingClientTimeout,
            "aclName": aclName,
            "isPosturingEnabled": isPosturingEnabled,
            "isAuthKeySuiteB1x": isAuthKeySuiteB1x,
            "isAuthKeySuiteB1921x": isAuthKeySuiteB1921x,
            "isAuthKeySaeExt": isAuthKeySaeExt,
            "isAuthKeySaeExtPlusFT": isAuthKeySaeExtPlusFT,
            "isApBeaconProtectionEnabled": isApBeaconProtectionEnabled,
            "ghz24Policy": ghz24Policy,
            "cckmTsfTolerance": cckmTsfTolerance,
            "isCckmEnabled": isCckmEnabled,
            "isHex": isHex,
            "isRandomMacFilterEnabled": isRandomMacFilterEnabled,
            "fastTransitionOverTheDistributedSystemEnable": fastTransitionOverTheDistributedSystemEnable,
            "isRadiusProfilingEnabled": isRadiusProfilingEnabled,
            "policyProfileName": policyProfileName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c2a16208da55e8a615348ed3d530ac_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids" + "/{id}/update"
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
            "bpm_c2a16208da55e8a615348ed3d530ac_v2_3_7_9", json_data
        )

    def update_ap_pnp_location_setting(
        self,
        apPnPLocation=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Enable or disable the AP PnP Location setting in the system.Once the AP PnP Location Setting is enabled, the
        Access Point's assigned Site name will be configured as the AP Location during the PnP Claim process.
        This applies only during the PnP onboarding process and not during any subsequent provisioning (dayN). .

        Args:
            apPnPLocation(string): Wireless's Enable Or Disable.Once the AP PnP Location Setting is enabled, the
                Access Point's assigned Site name will be configured as the AP Location during the PnP
                Claim process. This applies only during the PnP onboarding process and not during any
                subsequent provisioning (dayN). .
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
            https://developer.cisco.com/docs/dna-center/#!update-a-p-pn-p-location-setting
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
            "apPnPLocation": apPnPLocation,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ba52bb172d495710aa00f7d4d060ec50_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/systemSettings/apPnpLocation"
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
            "bpm_ba52bb172d495710aa00f7d4d060ec50_v2_3_7_9", json_data
        )

    def get_ap_pnp_location_setting(self, headers=None, **request_parameters):
        """Retrieve the current AP PnP Location setting from the system.Once the AP PnP Location Setting is enabled, the
        Access Point's assigned Site name will be configured as the AP Location during the PnP Claim process.
        This applies only during the PnP onboarding process and not during any subsequent provisioning (dayN). .

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
            https://developer.cisco.com/docs/dna-center/#!get-a-p-pn-p-location-setting
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/systemSettings/apPnpLocation"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ca8a515b6fc5c0eb78955f6218efc2a_v2_3_7_9", json_data
        )

    def delete_wireless_profile(
        self, wireless_profile_name, headers=None, **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-wireless-profile
        """
        check_type(headers, dict)
        check_type(wireless_profile_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "wirelessProfileName": wireless_profile_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless-" + "profile/{wirelessProfileName}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a850fb6c5451a7ad20ba76f4ff43_v2_3_7_9", json_data
        )

    def configure_access_points(
        self,
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
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!configure-access-points
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "apList": apList,
            "configureAdminStatus": configureAdminStatus,
            "adminStatus": adminStatus,
            "configureApMode": configureApMode,
            "apMode": apMode,
            "configureFailoverPriority": configureFailoverPriority,
            "failoverPriority": failoverPriority,
            "configureLedStatus": configureLedStatus,
            "ledStatus": ledStatus,
            "configureLedBrightnessLevel": configureLedBrightnessLevel,
            "ledBrightnessLevel": ledBrightnessLevel,
            "configureLocation": configureLocation,
            "location": location,
            "configureHAController": configureHAController,
            "primaryControllerName": primaryControllerName,
            "primaryIpAddress": primaryIpAddress,
            "secondaryControllerName": secondaryControllerName,
            "secondaryIpAddress": secondaryIpAddress,
            "tertiaryControllerName": tertiaryControllerName,
            "tertiaryIpAddress": tertiaryIpAddress,
            "radioConfigurations": radioConfigurations,
            "isAssignedSiteAsLocation": isAssignedSiteAsLocation,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e0bd567c1395531a7f18ab4e14110bd_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/accesspoint-configuration"
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
            "bpm_e0bd567c1395531a7f18ab4e14110bd_v2_3_7_9", json_data
        )

    def get_access_point_configuration_count(
        self,
        ap_mode=None,
        ap_model=None,
        mesh_role=None,
        provisioned=None,
        wlc_ip_address=None,
        headers=None,
        **request_parameters
    ):
        """Get Access Point Configuration Count .

        Args:
            wlc_ip_address(str): wlcIpAddress query parameter. WLC IP Address .
            ap_mode(str): apMode query parameter. AP Mode. Allowed values are Local, Bridge, Monitor, FlexConnect,
                Sniffer, Rogue Detector, SE-Connect, Flex+Bridge, Sensor. .
            ap_model(str): apModel query parameter. AP Model .
            mesh_role(str): meshRole query parameter. Mesh Role. Allowed values are RAP or MAP .
            provisioned(str): provisioned query parameter. Indicate whether AP provisioned or not. Allowed values
                are True or False .
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
            https://developer.cisco.com/docs/dna-center/#!get-access-point-configuration-count
        """
        check_type(headers, dict)
        check_type(wlc_ip_address, str)
        check_type(ap_mode, str)
        check_type(ap_model, str)
        check_type(mesh_role, str)
        check_type(provisioned, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "wlcIpAddress": wlc_ip_address,
            "apMode": ap_mode,
            "apModel": ap_model,
            "meshRole": mesh_role,
            "provisioned": provisioned,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/accesspoint-" + "configuration/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e2ccd7c54fa91dfe821a7869b84_v2_3_7_9", json_data
        )

    def get_access_point_configuration_task_result(
        self, task_id, headers=None, **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-access-point-configuration-task-result
        """
        check_type(headers, dict)
        check_type(task_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "task_id": task_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wireless/accesspoint-"
            + "configuration/details/{task_id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cc2c3a5b75a4091350fa84ac872c9_v2_3_7_9", json_data
        )

    def get_access_point_configuration(
        self,
        ap_mode=None,
        ap_model=None,
        key=None,
        limit=None,
        mesh_role=None,
        offset=None,
        provisioned=None,
        wlc_ip_address=None,
        headers=None,
        **request_parameters
    ):
        """Users can query access point configuration information for a specific device by using the Ethernet MAC address
        as a 'key' filter. If no key is specified, all access point details will be retrieved based on the
        combination of filters provided. .

        Args:
            key(str): key query parameter. The ethernet MAC address of Access point .
            wlc_ip_address(str): wlcIpAddress query parameter. WLC IP Address .
            ap_mode(str): apMode query parameter. AP Mode. Allowed values are Local, Bridge, Monitor, FlexConnect,
                Sniffer, Rogue Detector, SE-Connect, Flex+Bridge, Sensor. .
            ap_model(str): apModel query parameter. AP Model .
            mesh_role(str): meshRole query parameter. Mesh Role. Allowed values are RAP or MAP .
            provisioned(str): provisioned query parameter. Indicate whether AP provisioned or not. Allowed values
                are True or False .
            limit(int): limit query parameter. The number of records to show for this page. The default is 500 if
                not specified. The maximum allowed limit is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-access-point-configuration
        """
        check_type(headers, dict)
        check_type(key, str)
        check_type(wlc_ip_address, str)
        check_type(ap_mode, str)
        check_type(ap_model, str)
        check_type(mesh_role, str)
        check_type(provisioned, str)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "key": key,
            "wlcIpAddress": wlc_ip_address,
            "apMode": ap_mode,
            "apModel": ap_model,
            "meshRole": mesh_role,
            "provisioned": provisioned,
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

        e_url = "/dna/intent/api/v1/wireless/accesspoint-" + "configuration/summary"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fb7514b0e8c52be8cfd19dab5e31b06_v2_3_7_9", json_data
        )

    def ap_provision_connectivity(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Access Point Provision and ReProvision .

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
            https://developer.cisco.com/docs/dna-center/#!a-p-provision-connectivity
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "__persistbapioutput" in headers:
                check_type(headers.get("__persistbapioutput"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_f790a930d452708353c374f5c0f90f_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/ap-provision"
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
            "bpm_f790a930d452708353c374f5c0f90f_v2_3_7_9", json_data
        )

    def delete_dynamic_interface(
        self, interface_name, headers=None, **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-dynamic-interface
        """
        check_type(headers, dict)
        check_type(interface_name, str, may_be_none=False)
        if headers is not None:
            if "__runsync" in headers:
                check_type(headers.get("__runsync"), bool)
            if "__timeout" in headers:
                check_type(headers.get("__timeout"), int)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "interfaceName": interface_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/dynamic-interface"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ed6ee6a19c5e7da1606b05b7188964_v2_3_7_9", json_data
        )

    def create_update_dynamic_interface(
        self,
        interfaceName=None,
        vlanId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-update-dynamic-interface
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
            "interfaceName": interfaceName,
            "vlanId": vlanId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c00df3623b5a74ad41e75487ed9b77_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/dynamic-interface"
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
            "bpm_c00df3623b5a74ad41e75487ed9b77_v2_3_7_9", json_data
        )

    def get_dynamic_interface(
        self, interface_name=None, headers=None, **request_parameters
    ):
        """Get one or all dynamic interface(s) .

        Args:
            interface_name(str): interface-name query parameter. dynamic-interface name, if not specified all the
                existing dynamic interfaces will be retrieved .
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
            https://developer.cisco.com/docs/dna-center/#!get-dynamic-interface
        """
        check_type(headers, dict)
        check_type(interface_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "interface-name": interface_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/dynamic-interface"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c9fb8b0f5c69ba22f920e4044538_v2_3_7_9", json_data
        )

    def update_wireless_profile(
        self,
        profileDetails=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates the wireless Network Profile with updated details provided. All sites to be present in the network
        profile should be provided. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-wireless-profile
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
            "profileDetails": profileDetails,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bbf7ce025bc2a291b90c37a6b898_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/profile"
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
            "bpm_bbf7ce025bc2a291b90c37a6b898_v2_3_7_9", json_data
        )

    def create_wireless_profile(
        self,
        profileDetails=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates Wireless Network Profile on Cisco Catalyst Center and associates sites and SSIDs to it. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-wireless-profile
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
            "profileDetails": profileDetails,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b95201b6a6905a10b463e036bf591166_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/profile"
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
            "bpm_b95201b6a6905a10b463e036bf591166_v2_3_7_9", json_data
        )

    def get_wireless_profile(
        self, profile_name=None, headers=None, **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-wireless-profile
        """
        check_type(headers, dict)
        check_type(profile_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "profileName": profile_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/profile"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bbc1866a50505c0695ae243718d51936_v2_3_7_9", json_data
        )

    def provision_update(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!provision-update
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "__persistbapioutput" in headers:
                check_type(headers.get("__persistbapioutput"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_d0aab00569b258b481afedc35e6db392_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/provision"
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
            "bpm_d0aab00569b258b481afedc35e6db392_v2_3_7_9", json_data
        )

    def provision(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!provision
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator("jsd_e31c795964b3bdf85da1b5a2a5_v2_3_7_9").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/provision"
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
            "bpm_e31c795964b3bdf85da1b5a2a5_v2_3_7_9", json_data
        )

    def psk_override(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!p-s-k-override
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_f99c96c3a9b45ddaabc2c75ff8efa67f_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/psk-override"
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
            "bpm_f99c96c3a9b45ddaabc2c75ff8efa67f_v2_3_7_9", json_data
        )

    def retrieve_rf_profiles(
        self, rf_profile_name=None, headers=None, **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieve-r-f-profiles
        """
        check_type(headers, dict)
        check_type(rf_profile_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "rf-profile-name": rf_profile_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/rf-profile"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ac37d6798c0b593088952123df03bb1b_v2_3_7_9", json_data
        )

    def create_or_update_rf_profile(
        self,
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
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-or-update-r-f-profile
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
            "name": name,
            "defaultRfProfile": defaultRfProfile,
            "enableRadioTypeA": enableRadioTypeA,
            "enableRadioTypeB": enableRadioTypeB,
            "channelWidth": channelWidth,
            "enableCustom": enableCustom,
            "enableBrownField": enableBrownField,
            "radioTypeAProperties": radioTypeAProperties,
            "radioTypeBProperties": radioTypeBProperties,
            "radioTypeCProperties": radioTypeCProperties,
            "enableRadioTypeC": enableRadioTypeC,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f24f6c07641580ba6ed710e92c2da16_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/rf-profile"
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
            "bpm_f24f6c07641580ba6ed710e92c2da16_v2_3_7_9", json_data
        )

    def delete_rf_profiles(self, rf_profile_name, headers=None, **request_parameters):
        """Delete RF profile .

        Args:
            rf_profile_name(str): rfProfileName path parameter. RF profile name to be deleted(required) *non-custom
                RF profile cannot be deleted .
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
            https://developer.cisco.com/docs/dna-center/#!delete-r-f-profiles
        """
        check_type(headers, dict)
        check_type(rf_profile_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "rfProfileName": rf_profile_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wireless/rf-profile/{rfProfileName}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f3790386da5cd49480cb0503e59047_v2_3_7_9", json_data
        )

    def factory_reset_access_points(
        self,
        apMacAddresses=None,
        keepStaticIPConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API is used to factory reset Access Points. It is supported for maximum 100 Access Points per request.
        Factory reset clears all configurations from the Access Points. After factory reset the Access Point may
        become unreachable from the currently associated Wireless Controller and may or may not join back the
        same controller. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!factory-reset-access-points
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
            "keepStaticIPConfig": keepStaticIPConfig,
            "apMacAddresses": apMacAddresses,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_efa7f7a97b95f5885a00e6981b27b11_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessAccessPoints/factoryResetRequ" + "est/provision"
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
            "bpm_efa7f7a97b95f5885a00e6981b27b11_v2_3_7_9", json_data
        )

    def get_access_points_factory_reset_status(
        self, task_id, headers=None, **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-access-points-factory-reset-status
        """
        check_type(headers, dict)
        check_type(task_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "taskId": task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessAccessPoints/factoryResetRequ" + "estStatus"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f10b36d381e85181a857e67339105684_v2_3_7_9", json_data
        )

    def ap_provision(
        self,
        apZoneName=None,
        networkDevices=None,
        rfProfileName=None,
        siteId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API is used to provision Access Points. Prerequisite: Access Point has to be assigned to the site using the
        API /dna/intent/api/v1/networkDevices/assignToSite/apply. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!a-p-provision
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
            "networkDevices": networkDevices,
            "rfProfileName": rfProfileName,
            "apZoneName": apZoneName,
            "siteId": siteId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_eab4d187be085cac8a53971def40bee0_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessAccessPoints/provision"
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
            "bpm_eab4d187be085cac8a53971def40bee0_v2_3_7_9", json_data
        )

    def get_anchor_capable_devices(self, headers=None, **request_parameters):
        """This API allows the user to get Anchor capable devices .

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
            https://developer.cisco.com/docs/dna-center/#!get-anchor-capable-devices
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessControllers/anchorCapableDevi" + "ces"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e1c353aa15463bf2867d0716712ca_v2_3_7_9", json_data
        )

    def get_mesh_ap_neighbours(
        self,
        ap_name=None,
        ethernet_mac_address=None,
        wlc_ip_address=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves all Mesh accesspoint Neighbours details whether child, parent, etc. .

        Args:
            wlc_ip_address(str): wlcIpAddress query parameter. Employ this query parameter to obtain the details of
                the Access points corresponding to the provided WLC IP address. .
            ap_name(str): apName query parameter. Employ this query parameter to obtain the details of the Access
                points corresponding to the provided ap name. .
            ethernet_mac_address(str): ethernetMacAddress query parameter. Employ this query parameter to obtain the
                details of the Access points corresponding to the provided EthernetMacAddress. .
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
            https://developer.cisco.com/docs/dna-center/#!get-mesh-ap-neighbours
        """
        check_type(headers, dict)
        check_type(wlc_ip_address, str)
        check_type(ap_name, str)
        check_type(ethernet_mac_address, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "wlcIpAddress": wlc_ip_address,
            "apName": ap_name,
            "ethernetMacAddress": ethernet_mac_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessControllers/meshApNeighbours"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cc53655bf17533aa570d6eab1bbf706_v2_3_7_9", json_data
        )

    def get_mesh_ap_neighbours_count(self, headers=None, **request_parameters):
        """This API returns the total number of mesh Ap Neighbours available. .

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
            https://developer.cisco.com/docs/dna-center/#!get-mesh-ap-neighbours-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessControllers/meshApNeighbours/" + "count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_cd2975404a8d98235775136f7_v2_3_7_9", json_data)

    def get_mobility_groups(
        self, network_device_id=None, headers=None, **request_parameters
    ):
        """Retrieve configured mobility groups if no Network Device Id is provided as a query parameter. If a Network
        Device Id is given and a mobility group is configured for it, return the configured details; otherwise,
        return the default values from the device. .

        Args:
            network_device_id(str): networkDeviceId query parameter. Employ this query parameter to obtain the
                details of the Mobility Group corresponding to the provided networkDeviceId. Obtain the
                network device ID value by using the API GET call /dna/intent/api/v1/network-device/ip-
                address/${ipAddress}. .
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
            https://developer.cisco.com/docs/dna-center/#!get-mobility-groups
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessControllers/wirelessMobilityG" + "roups"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cb3e813f46055a3d945b3f77c58f913d_v2_3_7_9", json_data
        )

    def get_mobility_groups_count(self, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-mobility-groups-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessControllers/wirelessMobilityG" + "roups/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f0e19cf1f588cbe6fcbd0332a3987_v2_3_7_9", json_data
        )

    def mobility_provision(
        self,
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
        **request_parameters
    ):
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
                {!,<,space,?/'}  and maximum of 31 characters. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!mobility-provision
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
            "mobilityGroupName": mobilityGroupName,
            "macAddress": macAddress,
            "managementIp": managementIp,
            "networkDeviceId": networkDeviceId,
            "dtlsHighCipher": dtlsHighCipher,
            "dataLinkEncryption": dataLinkEncryption,
            "mobilityPeers": mobilityPeers,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bfd1cc1403c951a99c0fcafd59eaabf3_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessControllers/wirelessMobilityG"
            + "roups/mobilityProvision"
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
            "bpm_bfd1cc1403c951a99c0fcafd59eaabf3_v2_3_7_9", json_data
        )

    def mobility_reset(
        self,
        networkDeviceId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API is used to reset wireless mobility which in turn sets mobility group name as 'default'. .

        Args:
            networkDeviceId(string): Wireless's Network device Id of Cisco wireless controller. Obtain the network
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!mobility-reset
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
            "networkDeviceId": networkDeviceId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a6c4ce7aef8251a2a8646ba0b5c1826a_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessControllers/wirelessMobilityG"
            + "roups/mobilityReset"
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
            "bpm_a6c4ce7aef8251a2a8646ba0b5c1826a_v2_3_7_9", json_data
        )

    def assign_managed_ap_locations_for_w_l_c(
        self,
        device_id,
        primaryManagedAPLocationsSiteIds=None,
        secondaryManagedAPLocationsSiteIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows user to assign Managed AP Locations for IOS-XE Wireless supported devices by device ID. The
        payload should always be a complete list. The Managed AP Locations included in the payload will be fully
        processed for both addition and deletion. .

        Args:
            primaryManagedAPLocationsSiteIds(list): Wireless's Site IDs of Primary Managed AP Locations. These
                values can be obtained by using the API call GET: /dna/intent/api/v1/site  (list of
                strings).
            secondaryManagedAPLocationsSiteIds(list): Wireless's Site IDs of Secondary Managed AP Locations. These
                values can be obtained by using the API call GET: /dna/intent/api/v1/site  (list of
                strings).
            device_id(str): deviceId path parameter. Network Device ID. This value can be obtained by using the API
                call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress} .
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
            https://developer.cisco.com/docs/dna-center/#!assign-managed-a-p-locations-for-w-l-c
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }
        _payload = {
            "primaryManagedAPLocationsSiteIds": primaryManagedAPLocationsSiteIds,
            "secondaryManagedAPLocationsSiteIds": secondaryManagedAPLocationsSiteIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f019a24c5ce50f082d081bb72ff4df9_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessControllers/{deviceId}/assign"
            + "ManagedApLocations"
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
            "bpm_f019a24c5ce50f082d081bb72ff4df9_v2_3_7_9", json_data
        )

    def wireless_controller_provision(
        self,
        device_id,
        apAuthorizationListName=None,
        authorizeMeshAndNonMeshAccessPoints=None,
        featureTemplatesOverridenAttributes=None,
        interfaces=None,
        rollingApUpgrade=None,
        skipApProvision=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API is used to provision wireless controller .

        Args:
            apAuthorizationListName(string): Wireless's AP Authorization List name. 'Obtain the AP Authorization
                List names by using the API call GET:
                /intent/api/v1/wirelessSettings/apAuthorizationLists. During re-provision, obtain the AP
                Authorization List configured for the given provisioned network device Id using the API
                call GET: /intent/api/v1/wireless/apAuthorizationLists/{networkDeviceId}' .
            authorizeMeshAndNonMeshAccessPoints(boolean): Wireless's True if AP Authorization List should  authorize
                against All Mesh/Non-Mesh APs, else false if AP Authorization List should only authorize
                against Mesh APs (Applicable only when Mesh is enabled on sites) .
            featureTemplatesOverridenAttributes(object): Wireless's featureTemplatesOverridenAttributes.
            interfaces(list): Wireless's interfaces (list of objects).
            rollingApUpgrade(object): Wireless's rollingApUpgrade.
            skipApProvision(boolean): Wireless's True if Skip AP Provision is enabled, else False .
            device_id(str): deviceId path parameter. Network Device ID. This value can be obtained by using the API
                call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress} .
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
            https://developer.cisco.com/docs/dna-center/#!wireless-controller-provision
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }
        _payload = {
            "interfaces": interfaces,
            "skipApProvision": skipApProvision,
            "rollingApUpgrade": rollingApUpgrade,
            "apAuthorizationListName": apAuthorizationListName,
            "authorizeMeshAndNonMeshAccessPoints": authorizeMeshAndNonMeshAccessPoints,
            "featureTemplatesOverridenAttributes": featureTemplatesOverridenAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b0aa8e79d21f5e579908825e70aaccf6_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessControllers/{deviceId}/provis" + "ion"
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
            "bpm_b0aa8e79d21f5e579908825e70aaccf6_v2_3_7_9", json_data
        )

    def get_anchor_managed_ap_locations_for_specific_wireless_controller(
        self,
        network_device_id,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves all the details of Anchor Managed AP locations associated with the specific Wireless Controller. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the network device ID value by using the
                API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-anchor-managed-a-p-locations-for-specific-wireless-controller
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessControllers/{networkDeviceId}"
            + "/anchorManagedApLocations"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_de386cae35720b6782009e61541c1_v2_3_7_9", json_data
        )

    def get_ap_authorization_list_by_network_device_id(
        self, network_device_id, headers=None, **request_parameters
    ):
        """This API allows the user to get an AP Authorization List details configured for the given provisioned network
        device Id. Obtain the network device ID value by using the API GET call '/dna/intent/api/v1/network-
        device/ip-address/${ipAddress}'. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network Device ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-a-p-authorization-list-by-network-device-id
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessControllers/{networkDeviceId}"
            + "/apAuthorizationLists"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e9661bbf6b2f5f0d981695212ff1b5ea_v2_3_7_9", json_data
        )

    def get_managed_ap_locations_count_for_specific_wireless_controller(
        self, network_device_id, headers=None, **request_parameters
    ):
        """Retrieves the count of Managed AP locations, including Primary Managed AP Locations, Secondary Managed AP
        Locations, and Anchor Managed AP Locations, associated with the specific Wireless Controller. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the network device ID value by using the
                API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
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
            https://developer.cisco.com/docs/dna-center/#!get-managed-a-p-locations-count-for-specific-wireless-controller
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessControllers/{networkDeviceId}"
            + "/managedApLocations/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f4a6e8f2c1de51f5b70e9c75c4b6fc1c_v2_3_7_9", json_data
        )

    def get_primary_managed_ap_locations_for_specific_wireless_controller(
        self,
        network_device_id,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves all the details of Primary Managed AP locations associated with the specific Wireless Controller. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the network device ID value by using the
                API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-primary-managed-a-p-locations-for-specific-wireless-controller
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessControllers/{networkDeviceId}"
            + "/primaryManagedApLocations"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e9b5024741155ad880b482720757f661_v2_3_7_9", json_data
        )

    def wireless_controller_provision_status(
        self, network_device_id, headers=None, **request_parameters
    ):
        """Retrieves wireless controller's provision status .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the networkDeviceId value by using the
                API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
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
            https://developer.cisco.com/docs/dna-center/#!wireless-controller-provision-status
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessControllers/{networkDeviceId}"
            + "/provisionStatus"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c882059a8b25dbeb4e05b2beff82803_v2_3_7_9", json_data
        )

    def get_secondary_managed_ap_locations_for_specific_wireless_controller(
        self,
        network_device_id,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves all the details of Secondary Managed AP locations associated with the specific Wireless Controller. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the network device ID value by using the
                API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-secondary-managed-a-p-locations-for-specific-wireless-controller
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessControllers/{networkDeviceId}"
            + "/secondaryManagedApLocations"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a431078850850a5bef6cb4fa9915fb7_v2_3_7_9", json_data
        )

    def get_ssid_details_for_specific_wireless_controller(
        self,
        network_device_id,
        admin_status=None,
        limit=None,
        managed=None,
        offset=None,
        ssid_name=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves all details of SSIDs associated with the specific Wireless Controller. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the network device ID value by using the
                API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
            ssid_name(str): ssidName query parameter. Employ this query parameter to obtain the details of the SSID
                corresponding to the provided SSID name. .
            admin_status(bool): adminStatus query parameter. Utilize this query parameter to obtain the
                administrative status. A 'true' value signifies that the admin status of the SSID is
                enabled, while a 'false' value indicates that the admin status of the SSID is disabled.
                .
            managed(bool): managed query parameter. If value is 'true' means SSIDs are configured through design.If
                the value is 'false' means out of band configuration from the Wireless Controller. .
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-s-s-i-d-details-for-specific-wireless-controller
        """
        check_type(headers, dict)
        check_type(ssid_name, str)
        check_type(admin_status, bool)
        check_type(managed, bool)
        check_type(limit, int)
        check_type(offset, int)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "ssidName": ssid_name,
            "adminStatus": admin_status,
            "managed": managed,
            "limit": limit,
            "offset": offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessControllers/{networkDeviceId}" + "/ssidDetails"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_efdb6b3d51ff9e3e2de942ca96c4_v2_3_7_9", json_data
        )

    def get_ssid_count_for_specific_wireless_controller(
        self,
        network_device_id,
        admin_status=None,
        managed=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the count of SSIDs associated with the specific wireless controller. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Obtain the network device ID value by using the
                API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress}. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-s-s-i-d-count-for-specific-wireless-controller
        """
        check_type(headers, dict)
        check_type(admin_status, bool)
        check_type(managed, bool)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "adminStatus": admin_status,
            "managed": managed,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessControllers/{networkDeviceId}"
            + "/ssidDetails/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_db60b529835a2e8d3f67c681f1ace4_v2_3_7_9", json_data
        )

    def get_wireless_profiles(
        self,
        limit=None,
        offset=None,
        wireless_profile_name=None,
        headers=None,
        **request_parameters
    ):
        """This API allows the user to get all Wireless Network Profiles .

        Args:
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500 .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1 .
            wireless_profile_name(str): wirelessProfileName query parameter. Wireless Profile Name .
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
            https://developer.cisco.com/docs/dna-center/#!get-wireless-profiles
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(wireless_profile_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "wirelessProfileName": wireless_profile_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bec142b3bf65c109d752da5705ae2ca_v2_3_7_9", json_data
        )

    def create_wireless_profile_connectivity(
        self,
        additionalInterfaces=None,
        apZones=None,
        featureTemplates=None,
        ssidDetails=None,
        wirelessProfileName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to create a Wireless Network Profile .

        Args:
            additionalInterfaces(list): Wireless's These additional interfaces will be configured on the device as
                independent interfaces in addition to the interfaces mapped to SSIDs. Max Limit 4094
                (list of strings).
            apZones(list): Wireless's apZones (list of objects).
            featureTemplates(list): Wireless's featureTemplates (list of objects).
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-wireless-profile-connectivity
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
            "wirelessProfileName": wirelessProfileName,
            "ssidDetails": ssidDetails,
            "additionalInterfaces": additionalInterfaces,
            "apZones": apZones,
            "featureTemplates": featureTemplates,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cc59d48f8159008f52b29e08738811_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles"
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
            "bpm_cc59d48f8159008f52b29e08738811_v2_3_7_9", json_data
        )

    def get_wireless_profiles_count(self, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-wireless-profiles-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ef56c845d27d59e5974077ade9deedf3_v2_3_7_9", json_data
        )

    def update_wireless_profile_connectivity(
        self,
        id,
        additionalInterfaces=None,
        apZones=None,
        featureTemplates=None,
        ssidDetails=None,
        wirelessProfileName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to update a Wireless Network Profile by ID. Note that, when performing a PUT operation
        on a wireless network profile, it is essential to provide a complete payload. This is because the
        wireless network profile is tightly integrated with other network design entities. Consequently, all
        fields must be included—not just the fields to be updated. Any missing fields will be set to their
        default or null values. To ensure all fields are accurately populated, consider using the GET operation
        to retrieve the current resource data before proceeding with the PUT operation. .

        Args:
            additionalInterfaces(list): Wireless's These additional interfaces will be configured on the device as
                independent interfaces in addition to the interfaces mapped to SSIDs. Max Limit 4094
                (list of strings).
            apZones(list): Wireless's apZones (list of objects).
            featureTemplates(list): Wireless's featureTemplates (list of objects).
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-wireless-profile-connectivity
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "wirelessProfileName": wirelessProfileName,
            "ssidDetails": ssidDetails,
            "additionalInterfaces": additionalInterfaces,
            "apZones": apZones,
            "featureTemplates": featureTemplates,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d91a3aad0fd954e7a43aa3256ce433f6_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}"
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
            "bpm_d91a3aad0fd954e7a43aa3256ce433f6_v2_3_7_9", json_data
        )

    def get_wireless_profile_by_id(self, id, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-wireless-profile-by-i-d
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d89e08ebbe2528088fbdb3b367cb23b_v2_3_7_9", json_data
        )

    def delete_wireless_profile_connectivity(
        self, id, headers=None, **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-wireless-profile-connectivity
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory("bpm_afcc95b9babb1b6a776e065e1_v2_3_7_9", json_data)

    def retrieve_all_policy_tags_for_a_wireless_profile(
        self,
        id,
        limit=None,
        offset=None,
        policy_tag_name=None,
        headers=None,
        **request_parameters
    ):
        """This endpoint retrieves a list of all `Policy Tags` associated with a specific `Wireless Profile`. This API
        requires the `id` of the `Wireless Profile` to be provided as a path parameter. .

        Args:
            id(str): id path parameter. Wireless Profile Id .
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
            offset(int): offset query parameter.
            policy_tag_name(str): policyTagName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-all-policy-tags-for-a-wireless-profile
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(policy_tag_name, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "policyTagName": policy_tag_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}/policyTags"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ea7127c17517d9c507aa279a815a9_v2_3_7_9", json_data
        )

    def create_multiple_policy_tags_for_a_wireless_profile_in_bulk(
        self,
        id,
        items=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This endpoint allows the creation of multiple `Policy Tags` associated with a specific `Wireless Profile` in a
        single request. The `id` of the Wireless Profile must be provided as a path parameter, and a list of
        `Policy Tags` should be included in the request body. Note: Multiple Policy Tags (policyTag) can be
        configured for the same siteId only if they have different sets of AP Zones (apZones). If multiple
        Policy Tags are created with the same apZones for the same site or a parent site, only the last one will
        be saved, overriding the previous ones. .

        Args:
            items(list): Wireless's items (list of arrays).
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-multiple-policy-tags-for-a-wireless-profile-in-bulk
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "items": items,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_eeb595d249295989a4917261463ea82a_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}/policyTags/bulk"
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
            "bpm_eeb595d249295989a4917261463ea82a_v2_3_7_9", json_data
        )

    def retrieve_the_count_of_policy_tags_for_a_wireless_profile(
        self, id, headers=None, **request_parameters
    ):
        """This endpoint retrieves the total count of `Policy Tags` associated with a specific `Wireless Profile`.This API
        requires the `id` of the `Wireless Profile` to be provided as a path parameter. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-policy-tags-for-a-wireless-profile
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}/policyTags/coun" + "t"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b4b3d55b8a57549d0836968ba4bb20_v2_3_7_9", json_data
        )

    def delete_a_specific_policy_tag_from_a_wireless_profile(
        self, id, policy_tag_id, headers=None, **request_parameters
    ):
        """This endpoint allows for the deletion of a specific `Policy Tag` associated with a given `Wireless Profile`.
        This API requires the `id` of the `Wireless Profile` and the `policyTagId` of the `Policy Tag` to be
        provided as path parameters. .

        Args:
            id(str): id path parameter. Wireless Profile Id .
            policy_tag_id(str): policyTagId path parameter. Policy Tag Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-specific-policy-tag-from-a-wireless-profile
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(policy_tag_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "policyTagId": policy_tag_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}/policyTags/{pol" + "icyTagId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ee08c569859cf8518a61fd9ec2045_v2_3_7_9", json_data
        )

    def update_a_specific_policy_tag_for_a_wireless_profile(
        self,
        id,
        policy_tag_id,
        apZones=None,
        policyTagName=None,
        siteIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This endpoint allows updating the details of a specific `Policy Tag` associated with a given `Wireless Profile`.
        The `id` of the `Wireless Profile` and the `policyTagId` of the Policy Tag must be provided as path
        parameters, and the request body should contain the updated details of the `Policy Tag`. The
        `policyTagName` cannot be modified through this endpoint. Note: When updating a Policy Tag, if the same
        set of AP Zones (apZones) is used for the same site or its parent site, the existing Policy Tag will be
        overridden by the new one. .

        Args:
            apZones(list): Wireless's Ap Zones (list of strings).
            policyTagName(string): Wireless's Policy Tag Name.
            siteIds(list): Wireless's Site Ids (list of strings).
            id(str): id path parameter. Wireless Profile Id .
            policy_tag_id(str): policyTagId path parameter. Policy Tag Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-a-specific-policy-tag-for-a-wireless-profile
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(policy_tag_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "policyTagId": policy_tag_id,
        }
        _payload = {
            "siteIds": siteIds,
            "policyTagName": policyTagName,
            "apZones": apZones,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_efc2269ee565e23b7be7b49e4fc0322_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}/policyTags/{pol" + "icyTagId}"
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
            "bpm_efc2269ee565e23b7be7b49e4fc0322_v2_3_7_9", json_data
        )

    def retrieve_a_specific_policy_tag_for_a_wireless_profile(
        self, id, policy_tag_id, headers=None, **request_parameters
    ):
        """This endpoint retrieves the details of a specific `Policy Tag` associated with a given `Wireless Profile`. This
        API requires the `id` of the `Wireless Profile` and the `policyTagId` of the `Policy Tag`. .

        Args:
            id(str): id path parameter. Wireless Profile Id .
            policy_tag_id(str): policyTagId path parameter. Policy Tag Id .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-policy-tag-for-a-wireless-profile
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(policy_tag_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "policyTagId": policy_tag_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}/policyTags/{pol" + "icyTagId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d80aa0ad4b8b57a4b6aca2ed2e6ff240_v2_3_7_9", json_data
        )

    def retrieve_all_site_tags_for_a_wireless_profile(
        self,
        id,
        limit=None,
        offset=None,
        site_tag_name=None,
        headers=None,
        **request_parameters
    ):
        """This endpoint retrieves a list of all `Site Tags` associated with a specific `Wireless Profile`. This API
        requires the `id` of the `Wireless Profile` to be provided as a path parameter. .

        Args:
            id(str): id path parameter. Wireless profile id .
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
            offset(int): offset query parameter.
            site_tag_name(str): siteTagName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-all-site-tags-for-a-wireless-profile
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(site_tag_name, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "siteTagName": site_tag_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}/siteTags"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a13f7910d8f5359a8fc2f0eb1febd5b_v2_3_7_9", json_data
        )

    def create_multiple_site_tags_for_a_wireless_profile_in_bulk(
        self,
        id,
        items=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This endpoint allows the creation of multiple `Site Tags` associated with a specific `Wireless Profile` in a
        single request. The `id` of the `Wireless Profile` must be provided as a path parameter, and a list of
        `Site Tags` should be included in the request body. Note: Only one Site Tag (siteTag) can be created per
        siteId. If multiple siteTags are specified for the same siteId within a request, only the last one will
        be saved, overriding any previously configured tags. When creating a Site Tag under a Flex-enabled
        Wireless Profile (i.e., a Wireless Profile with one or more Flex SSIDs), a non-default Flex Profile Name
        (flexProfileName) will be used. If no custom flexProfileName is defined, the System will automatically
        generate one and configure it in the controller. .

        Args:
            items(list): Wireless's items (list of arrays).
            id(str): id path parameter. network profile id .
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
            https://developer.cisco.com/docs/dna-center/#!create-multiple-site-tags-for-a-wireless-profile-in-bulk
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "items": items,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c6506b22335101a465d2adf5ca7f37_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}/siteTags/bulk"
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
            "bpm_c6506b22335101a465d2adf5ca7f37_v2_3_7_9", json_data
        )

    def retrieve_the_count_of_site_tags_for_a_wireless_profile(
        self, id, headers=None, **request_parameters
    ):
        """This endpoint retrieves the total count of `Site Tags` associated with a specific `Wireless Profile`.This API
        requires the `id` of the `Wireless Profile` to be provided as a path parameter. .

        Args:
            id(str): id path parameter. Wireless profile id .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-site-tags-for-a-wireless-profile
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}/siteTags/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c49b712c551aabc676c8d3aefb02_v2_3_7_9", json_data
        )

    def update_a_specific_site_tag_for_a_wireless_profile(
        self,
        id,
        site_tag_id,
        apProfileName=None,
        flexProfileName=None,
        siteIds=None,
        siteTagName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This endpoint allows updating the details of a specific `Site Tag` associated with a given `Wireless Profile`.
        The `id` of the `Wireless Profile` and the `siteTagId` of the Site Tag must be provided as path
        parameters, and the request body should contain the updated `Site Tag` details.  The `siteTagName`
        cannot be modified through this endpoint. Note: When updating a Site Tag (siteTag), if the siteId
        already has an associated siteTag and the same siteId is included in the update request, the existing
        siteTag for that siteId will be overridden by the new one. For Flex-enabled Wireless Profiles (i.e., a
        Wireless Profile with one or more Flex SSIDs), a non-default Flex Profile Name (flexProfileName) will be
        used. If no custom flexProfileName is provided, the System will automatically generate one and configure
        it in the controller. .

        Args:
            apProfileName(string): Wireless's Ap Profile Name.
            flexProfileName(string): Wireless's Flex Profile Name.
            siteIds(list): Wireless's Site Ids (list of strings).
            siteTagName(string): Wireless's Use English letters, numbers, special characters except <, /, '.*', ?
                and leading/trailing space. .
            id(str): id path parameter. Wireless Profile Id .
            site_tag_id(str): siteTagId path parameter. Site Tag Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-a-specific-site-tag-for-a-wireless-profile
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(site_tag_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "siteTagId": site_tag_id,
        }
        _payload = {
            "siteIds": siteIds,
            "siteTagName": siteTagName,
            "flexProfileName": flexProfileName,
            "apProfileName": apProfileName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ba9e0f3a5db5972a55d4b3fcf2b5432_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}/siteTags/{siteT" + "agId}"
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
            "bpm_ba9e0f3a5db5972a55d4b3fcf2b5432_v2_3_7_9", json_data
        )

    def retrieve_a_specific_site_tag_for_a_wireless_profile(
        self, id, site_tag_id, headers=None, **request_parameters
    ):
        """This endpoint retrieves the details of a specific `Site Tag` associated with a given `Wireless Profile`. This
        API requires the `id` of the `Wireless Profile` and the `siteTagId` of the `Site Tag`. .

        Args:
            id(str): id path parameter. Wireless Profile Id .
            site_tag_id(str): siteTagId path parameter. Site Tag Id .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-site-tag-for-a-wireless-profile
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(site_tag_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "siteTagId": site_tag_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}/siteTags/{siteT" + "agId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f29ee7d063e54c391da1a3e94b3b6a6_v2_3_7_9", json_data
        )

    def delete_a_specific_site_tag_from_a_wireless_profile(
        self, id, site_tag_id, headers=None, **request_parameters
    ):
        """This endpoint enables the deletion of a specific `Site Tag` associated with a given `Wireless Profile`. This API
        requires the `id` of the `Wireless Profile` and the `siteTagId` of the `Site Tag` to be provided as path
        parameters. .

        Args:
            id(str): id path parameter. Wireless Profile id .
            site_tag_id(str): siteTagId path parameter. Site Tag Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-specific-site-tag-from-a-wireless-profile
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(site_tag_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "siteTagId": site_tag_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessProfiles/{id}/siteTags/{siteT" + "agId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ffb265b5ca6b65a2dbc8faecbe3_v2_3_7_9", json_data
        )

    def create_anchor_group(
        self,
        anchorGroupName=None,
        mobilityAnchors=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to create an AnchorGroup .

        Args:
            anchorGroupName(string): Wireless's Anchor Group Name. Max length is 32 characters .
            mobilityAnchors(list): Wireless's mobilityAnchors (list of objects).
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
            https://developer.cisco.com/docs/dna-center/#!create-anchor-group
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
            "anchorGroupName": anchorGroupName,
            "mobilityAnchors": mobilityAnchors,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a5e4452cb2e05682933349833a01d14b_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/anchorGroups"
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
            "bpm_a5e4452cb2e05682933349833a01d14b_v2_3_7_9", json_data
        )

    def get_anchor_groups(
        self, limit=None, offset=None, headers=None, **request_parameters
    ):
        """This API allows the user to get AnchorGroups that captured in wireless settings design. .

        Args:
            limit(str): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
            offset(str): offset query parameter. The first record to show for this page, the first record is
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
            https://developer.cisco.com/docs/dna-center/#!get-anchor-groups
        """
        check_type(headers, dict)
        check_type(limit, str)
        check_type(offset, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/intent/api/v1/wirelessSettings/anchorGroups"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e7c985b3fbe50f1a63ffe82180ae85f_v2_3_7_9", json_data
        )

    def get_count_of_anchor_groups(self, headers=None, **request_parameters):
        """This API allows the user to get count of all AnchorGroups .

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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-anchor-groups
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/anchorGroups/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d16bdccffaa5e0ba0e2c03a404065e1_v2_3_7_9", json_data
        )

    def get_anchor_group_by_id(self, id, headers=None, **request_parameters):
        """This API allows the user to get an AnchorGroup by AnchorGroup ID .

        Args:
            id(str): id path parameter. AnchorGroup ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-anchor-group-by-i-d
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/anchorGroups/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e45188547287c882c1b01480bd_v2_3_7_9", json_data
        )

    def delete_anchor_group_by_id(self, id, headers=None, **request_parameters):
        """This API allows the user to delete an AnchorGroup  by specifying the AnchorGroup ID .

        Args:
            id(str): id path parameter. AnchorGroup ID .
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
            https://developer.cisco.com/docs/dna-center/#!delete-anchor-group-by-i-d
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/anchorGroups/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ff2aeab6a8fe5355b362c848d94a3c88_v2_3_7_9", json_data
        )

    def update_anchor_group(
        self,
        id,
        anchorGroupName=None,
        mobilityAnchors=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to update an AnchorGroup .

        Args:
            anchorGroupName(string): Wireless's Anchor Group Name. Max length is 32 characters .
            mobilityAnchors(list): Wireless's mobilityAnchors (list of objects).
            id(str): id path parameter. AnchorGroup ID .
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
            https://developer.cisco.com/docs/dna-center/#!update-anchor-group
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "anchorGroupName": anchorGroupName,
            "mobilityAnchors": mobilityAnchors,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ecfe864dc5012ab9c25d23e2ce9f5_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/anchorGroups/{id}"
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
            "bpm_ecfe864dc5012ab9c25d23e2ce9f5_v2_3_7_9", json_data
        )

    def get_ap_authorization_lists(
        self,
        ap_authorization_list_name=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the AP Authorization Lists that are created in the Catalyst Centre network Design for wireless. If an
        AP Authorization List name is given as query parameter, then returns respective AP Authorization List
        details including Local and/or Remote authorization. .

        Args:
            ap_authorization_list_name(str): apAuthorizationListName query parameter. Employ this query parameter to
                obtain the details of the AP Authorization List corresponding to the provided
                apAuthorizationListName. .
            offset(str): offset query parameter. The first record to show for this page. The first record is
                numbered 1. .
            limit(str): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-a-p-authorization-lists
        """
        check_type(headers, dict)
        check_type(ap_authorization_list_name, str)
        check_type(offset, str)
        check_type(limit, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "apAuthorizationListName": ap_authorization_list_name,
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

        e_url = "/dna/intent/api/v1/wirelessSettings/apAuthorizationLists"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e07df6057be8775b54b138e6e68_v2_3_7_9", json_data
        )

    def create_ap_authorization_list(
        self,
        apAuthorizationListName=None,
        localAuthorization=None,
        remoteAuthorization=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to create an AP Authorization List. .

        Args:
            apAuthorizationListName(string): Wireless's AP Authorization List Name. For a AP Authorization List to
                be created successfully, either Local Authorization or Remote Authorization is
                mandatory. .
            localAuthorization(object): Wireless's localAuthorization.
            remoteAuthorization(object): Wireless's remoteAuthorization.
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
            https://developer.cisco.com/docs/dna-center/#!create-a-p-authorization-list
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
            "apAuthorizationListName": apAuthorizationListName,
            "localAuthorization": localAuthorization,
            "remoteAuthorization": remoteAuthorization,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bd400dbef41e53ed82541c766f14f1eb_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/apAuthorizationLists"
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
            "bpm_bd400dbef41e53ed82541c766f14f1eb_v2_3_7_9", json_data
        )

    def get_ap_authorization_list_count(self, headers=None, **request_parameters):
        """This API allows the user to get count of all AP Authorization lists. .

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
            https://developer.cisco.com/docs/dna-center/#!get-a-p-authorization-list-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/apAuthorizationLists" + "/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dbb918195bc3a42c095abc5e37fc_v2_3_7_9", json_data
        )

    def delete_ap_authorization_list(self, id, headers=None, **request_parameters):
        """This API allows the user to delete an AP Authorization List. .

        Args:
            id(str): id path parameter. AP Authorization List ID .
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-p-authorization-list
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/apAuthorizationLists" + "/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b0a5d8bc0a15df3a53fa81743b965a1_v2_3_7_9", json_data
        )

    def update_ap_authorization_list(
        self,
        id,
        apAuthorizationListName=None,
        localAuthorization=None,
        remoteAuthorization=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to update an AP Authorization List. .

        Args:
            apAuthorizationListName(string): Wireless's AP Authorization List Name. For a AP Authorization List to
                be created successfully, either Local Authorization or Remote Authorization is
                mandatory. .
            localAuthorization(object): Wireless's localAuthorization.
            remoteAuthorization(object): Wireless's remoteAuthorization.
            id(str): id path parameter. AP Authorization List ID .
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
            https://developer.cisco.com/docs/dna-center/#!update-a-p-authorization-list
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "apAuthorizationListName": apAuthorizationListName,
            "localAuthorization": localAuthorization,
            "remoteAuthorization": remoteAuthorization,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e55cca88065707a6f812a679f69a5d_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/apAuthorizationLists" + "/{id}"
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
            "bpm_e55cca88065707a6f812a679f69a5d_v2_3_7_9", json_data
        )

    def get_ap_authorization_list_by_id(self, id, headers=None, **request_parameters):
        """This API allows the user to get an AP Authorization List by AP Authorization List ID that captured in wireless
        settings design. .

        Args:
            id(str): id path parameter. AP Authorization List ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-a-p-authorization-list-by-i-d
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/apAuthorizationLists" + "/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ca771ed49fa45c4cb7402bbb76f0d63d_v2_3_7_9", json_data
        )

    def create_ap_profile(
        self,
        apPowerProfileName=None,
        apProfileName=None,
        awipsEnabled=None,
        awipsForensicEnabled=None,
        calendarPowerProfiles=None,
        clientLimit=None,
        countryCode=None,
        description=None,
        managementSetting=None,
        meshEnabled=None,
        meshSetting=None,
        pmfDenialEnabled=None,
        remoteWorkerEnabled=None,
        rogueDetectionSetting=None,
        timeZone=None,
        timeZoneOffsetHour=None,
        timeZoneOffsetMinutes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to create a custom AP Profile. .

        Args:
            apPowerProfileName(string): Wireless's Name of the existing AP power profile. .
            apProfileName(string): Wireless's Name of the Access Point profile. Max length is 32 characters. .
            awipsEnabled(boolean): Wireless's Indicates if AWIPS is enabled on the AP. .
            awipsForensicEnabled(boolean): Wireless's Indicates if AWIPS forensic is enabled on the AP. Forensic
                Capture is supported from IOS-XE version 17.4 and above. Forensic Capture can be
                activated only if aWIPS is enabled. .
            calendarPowerProfiles(object): Wireless's calendarPowerProfiles.
            clientLimit(integer): Wireless's Number of clients. Value should be between 0-1200. .
            countryCode(string): Wireless's Country Code. Available values are '(AF|AE|AL|AR|AT|AO|AU|BD|BA|BB|BE|BG
                |BH|BM|BN|BO|BR|BT|BY|CA|CD|CH|CI|CL|CM|CN|CO|CR|CU|CY|CZ|DE|DK|DO|DZ|EC|EE|EG|EL|ES|ET|
                FI|FJ|FR|GB|GH|GI|GE|GR|GT|HK|HN|HR|HU|ID|IE|IL|IN|IQ|IS|IT|J2|J4|JM|JO|KE|KH|KN|KW|KZ|L
                A|LB|LI|LK|LT|LU|LV|LY|MA|MC|MD|ME|MK|MN|MM|MO|MT|MX|MY|NG|NI|NL|NO|NP|NZ|OM|PA|PE|PH|PK
                |PL|PR|PT|PY|QA|RO|RS|RU|SA|SD|SE|SG|SI|SK|SM|TH|TI|TN|TR|TW|TZ|UA|US|UY|VA|VE|VN|XK|YE|
                ZA|ZW|MU|ZM|BI|NA|BW|GA|UG|UZ)'.
            description(string): Wireless's Description of the AP profile. Max length is 241 characters .
            managementSetting(object): Wireless's managementSetting.
            meshEnabled(boolean): Wireless's This indicates whether mesh networking is enabled on the AP. For IOS-XE
                devices, when mesh networking is enabled, a custom mesh profile with the configured
                parameters will be created and mapped to the AP join profile on the device. When mesh
                networking is disabled, any existing custom mesh profile will be deleted from the
                device, and the AP join profile will be mapped to the default mesh profile on the
                device. .
            meshSetting(object): Wireless's meshSetting.
            pmfDenialEnabled(boolean): Wireless's Indicates if PMF denial is active on the AP. PMF Denial is
                supported from IOS-XE version 17.12 and above. .
            remoteWorkerEnabled(boolean): Wireless's Indicates if remote worker mode is enabled on the AP. Remote
                teleworker enabled profile cannot support security features like aWIPS,Forensic Capture
                Enablement, Rogue Detection and Rogue Containment. .
            rogueDetectionSetting(object): Wireless's rogueDetectionSetting.
            timeZone(string): Wireless's In the Time Zone area, choose one of the following options.             Not
                Configured APs operate in the UTC time zone.             Controller APs operate in the
                Cisco Wireless Controller time zone.             Delta from Controller APs operate in
                the offset time from the wireless controller time zone. . Available values are 'Not
                Configured', 'Controller' and 'Delta from Controller'.
            timeZoneOffsetHour(integer): Wireless's Enter the hour value (HH). The valid range is from -12 through
                14. .
            timeZoneOffsetMinutes(integer): Wireless's Enter the minute value (MM). The valid range is from 0
                through 59. .
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
            https://developer.cisco.com/docs/dna-center/#!create-a-p-profile
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
            "apProfileName": apProfileName,
            "description": description,
            "remoteWorkerEnabled": remoteWorkerEnabled,
            "managementSetting": managementSetting,
            "awipsEnabled": awipsEnabled,
            "awipsForensicEnabled": awipsForensicEnabled,
            "rogueDetectionSetting": rogueDetectionSetting,
            "pmfDenialEnabled": pmfDenialEnabled,
            "meshEnabled": meshEnabled,
            "meshSetting": meshSetting,
            "apPowerProfileName": apPowerProfileName,
            "calendarPowerProfiles": calendarPowerProfiles,
            "countryCode": countryCode,
            "timeZone": timeZone,
            "timeZoneOffsetHour": timeZoneOffsetHour,
            "timeZoneOffsetMinutes": timeZoneOffsetMinutes,
            "clientLimit": clientLimit,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a0f799d5ec6954d1bd7a25853080a9f1_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/apProfiles"
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
            "bpm_a0f799d5ec6954d1bd7a25853080a9f1_v2_3_7_9", json_data
        )

    def get_ap_profiles(
        self,
        ap_profile_name=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """This API allows the user to get AP Profiles that captured in wireless settings design. .

        Args:
            limit(str): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
            offset(str): offset query parameter. The first record to show for this page, the first record is
                numbered 1. .
            ap_profile_name(str): apProfileName query parameter. Employ this query parameter to obtain the details
                of the apProfiles corresponding to the provided apProfileName. .
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
            https://developer.cisco.com/docs/dna-center/#!get-a-p-profiles
        """
        check_type(headers, dict)
        check_type(limit, str)
        check_type(offset, str)
        check_type(ap_profile_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "apProfileName": ap_profile_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/apProfiles"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bfbdf9349a35ef5bd4ef3ee9dfafcc8_v2_3_7_9", json_data
        )

    def get_ap_profiles_count(self, headers=None, **request_parameters):
        """This API returns the total number of AP Profiles available. .

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
            https://developer.cisco.com/docs/dna-center/#!get-a-p-profiles-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/apProfiles/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b5a1e426fa455e2a07d80a65a03db57_v2_3_7_9", json_data
        )

    def delete_ap_profile_by_id(self, id, headers=None, **request_parameters):
        """This API allows the user to delete an AP Profile by specifying the AP Profile ID. .

        Args:
            id(str): id path parameter. AP Profile ID .
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-p-profile-by-i-d
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/apProfiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe43f12f8092513cba2344d43987cb57_v2_3_7_9", json_data
        )

    def update_ap_profile_by_id(
        self,
        id,
        apPowerProfileName=None,
        apProfileName=None,
        awipsEnabled=None,
        awipsForensicEnabled=None,
        calendarPowerProfiles=None,
        clientLimit=None,
        countryCode=None,
        description=None,
        managementSetting=None,
        meshEnabled=None,
        meshSetting=None,
        pmfDenialEnabled=None,
        remoteWorkerEnabled=None,
        rogueDetectionSetting=None,
        timeZone=None,
        timeZoneOffsetHour=None,
        timeZoneOffsetMinutes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to update a custom AP Profile .

        Args:
            apPowerProfileName(string): Wireless's Name of the existing AP power profile. .
            apProfileName(string): Wireless's Name of the Access Point profile. Max length is 32 characters. .
            awipsEnabled(boolean): Wireless's Indicates if AWIPS is enabled on the AP. .
            awipsForensicEnabled(boolean): Wireless's Indicates if AWIPS forensic is enabled on the AP. Forensic
                Capture is supported from IOS-XE version 17.4 and above. Forensic Capture can be
                activated only if aWIPS is enabled. .
            calendarPowerProfiles(object): Wireless's calendarPowerProfiles.
            clientLimit(integer): Wireless's Number of clients. Value should be between 0-1200. .
            countryCode(string): Wireless's Country Code. Available values are '(AF|AE|AL|AR|AT|AO|AU|BD|BA|BB|BE|BG
                |BH|BM|BN|BO|BR|BT|BY|CA|CD|CH|CI|CL|CM|CN|CO|CR|CU|CY|CZ|DE|DK|DO|DZ|EC|EE|EG|EL|ES|ET|
                FI|FJ|FR|GB|GH|GI|GE|GR|GT|HK|HN|HR|HU|ID|IE|IL|IN|IQ|IS|IT|J2|J4|JM|JO|KE|KH|KN|KW|KZ|L
                A|LB|LI|LK|LT|LU|LV|LY|MA|MC|MD|ME|MK|MN|MM|MO|MT|MX|MY|NG|NI|NL|NO|NP|NZ|OM|PA|PE|PH|PK
                |PL|PR|PT|PY|QA|RO|RS|RU|SA|SD|SE|SG|SI|SK|SM|TH|TI|TN|TR|TW|TZ|UA|US|UY|VA|VE|VN|XK|YE|
                ZA|ZW|MU|ZM|BI|NA|BW|GA|UG|UZ)'.
            description(string): Wireless's Description of the AP profile. Max length is 241 characters .
            managementSetting(object): Wireless's managementSetting.
            meshEnabled(boolean): Wireless's This indicates whether mesh networking is enabled on the AP. For IOS-XE
                devices, when mesh networking is enabled, a custom mesh profile with the configured
                parameters will be created and mapped to the AP join profile on the device. When mesh
                networking is disabled, any existing custom mesh profile will be deleted from the
                device, and the AP join profile will be mapped to the default mesh profile on the
                device. .
            meshSetting(object): Wireless's meshSetting.
            pmfDenialEnabled(boolean): Wireless's Indicates if PMF denial is active on the AP. PMF Denial is
                supported from IOS-XE version 17.12 and above. .
            remoteWorkerEnabled(boolean): Wireless's Indicates if remote worker mode is enabled on the AP. Remote
                teleworker enabled profile cannot support security features like aWIPS,Forensic Capture
                Enablement, Rogue Detection and Rogue Containment. .
            rogueDetectionSetting(object): Wireless's rogueDetectionSetting.
            timeZone(string): Wireless's In the Time Zone area, choose one of the following options.             Not
                Configured APs operate in the UTC time zone.             Controller APs operate in the
                Cisco Wireless Controller time zone.             Delta from Controller APs operate in
                the offset time from the wireless controller time zone. . Available values are 'Not
                Configured', 'Controller' and 'Delta from Controller'.
            timeZoneOffsetHour(integer): Wireless's Enter the hour value (HH). The valid range is from -12 through
                14. .
            timeZoneOffsetMinutes(integer): Wireless's Enter the minute value (MM). The valid range is from 0
                through 59. .
            id(str): id path parameter. Ap Profile ID .
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
            https://developer.cisco.com/docs/dna-center/#!update-a-p-profile-by-i-d
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "apProfileName": apProfileName,
            "description": description,
            "remoteWorkerEnabled": remoteWorkerEnabled,
            "managementSetting": managementSetting,
            "awipsEnabled": awipsEnabled,
            "awipsForensicEnabled": awipsForensicEnabled,
            "rogueDetectionSetting": rogueDetectionSetting,
            "pmfDenialEnabled": pmfDenialEnabled,
            "meshEnabled": meshEnabled,
            "meshSetting": meshSetting,
            "apPowerProfileName": apPowerProfileName,
            "calendarPowerProfiles": calendarPowerProfiles,
            "countryCode": countryCode,
            "timeZone": timeZone,
            "timeZoneOffsetHour": timeZoneOffsetHour,
            "timeZoneOffsetMinutes": timeZoneOffsetMinutes,
            "clientLimit": clientLimit,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b42a01655325be161ab2ad60aa68_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/apProfiles/{id}"
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
            "bpm_b42a01655325be161ab2ad60aa68_v2_3_7_9", json_data
        )

    def get_ap_profile_by_id(self, id, headers=None, **request_parameters):
        """This API allows the user to get a AP Profile by AP Profile ID that captured in wireless settings design .

        Args:
            id(str): id path parameter. Ap Profile ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-a-p-profile-by-i-d
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/apProfiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c9969e72561da513d74a8fecbaff_v2_3_7_9", json_data
        )

    def get80211be_profiles(
        self,
        is_mu_mimo_down_link=None,
        is_mu_mimo_up_link=None,
        is_of_dma_down_link=None,
        is_of_dma_multi_ru=None,
        is_of_dma_up_link=None,
        limit=None,
        offset=None,
        profile_name=None,
        headers=None,
        **request_parameters
    ):
        """This API allows the user to get 802.11be Profile(s) configured under Wireless Settings .

        Args:
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
            offset(int): offset query parameter. The first record to show for this page, the first record is
                numbered 1 .
            profile_name(str): profileName query parameter. Profile Name .
            is_of_dma_down_link(bool): isOfDmaDownLink query parameter. OFDMA Downlink .
            is_of_dma_up_link(bool): isOfDmaUpLink query parameter. OFDMA Uplink .
            is_mu_mimo_up_link(bool): isMuMimoUpLink query parameter. MU-MIMO Uplink .
            is_mu_mimo_down_link(bool): isMuMimoDownLink query parameter. MU-MIMO Downlink .
            is_of_dma_multi_ru(bool): isOfDmaMultiRu query parameter. OFDMA Multi-RU .
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
            https://developer.cisco.com/docs/dna-center/#!get80211be-profiles
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(profile_name, str)
        check_type(is_of_dma_down_link, bool)
        check_type(is_of_dma_up_link, bool)
        check_type(is_mu_mimo_up_link, bool)
        check_type(is_mu_mimo_down_link, bool)
        check_type(is_of_dma_multi_ru, bool)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "profileName": profile_name,
            "isOfDmaDownLink": is_of_dma_down_link,
            "isOfDmaUpLink": is_of_dma_up_link,
            "isMuMimoUpLink": is_mu_mimo_up_link,
            "isMuMimoDownLink": is_mu_mimo_down_link,
            "isOfDmaMultiRu": is_of_dma_multi_ru,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/dot11beProfiles"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f2b94a700f80548694685475590d5e0b_v2_3_7_9", json_data
        )

    def create_a80211be_profile(
        self,
        muMimoDownLink=None,
        muMimoUpLink=None,
        ofdmaDownLink=None,
        ofdmaMultiRu=None,
        ofdmaUpLink=None,
        profileName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to create a 802.11be Profile.Catalyst Center will push this profile to device's
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-a80211be-profile
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
            "profileName": profileName,
            "ofdmaDownLink": ofdmaDownLink,
            "ofdmaUpLink": ofdmaUpLink,
            "muMimoDownLink": muMimoDownLink,
            "muMimoUpLink": muMimoUpLink,
            "ofdmaMultiRu": ofdmaMultiRu,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f08eb586113e597a91b1658297570934_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/dot11beProfiles"
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
            "bpm_f08eb586113e597a91b1658297570934_v2_3_7_9", json_data
        )

    def get80211be_profiles_count(self, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get80211be-profiles-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/dot11beProfiles/coun" + "t"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b18962654b512e939285910448177d_v2_3_7_9", json_data
        )

    def delete_a80211be_profile(self, id, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-a80211be-profile
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f08862be5ba89b5c2f50aa30baa0_v2_3_7_9", json_data
        )

    def update80211be_profile(
        self,
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
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update80211be-profile
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "profileName": profileName,
            "ofdmaDownLink": ofdmaDownLink,
            "ofdmaUpLink": ofdmaUpLink,
            "muMimoDownLink": muMimoDownLink,
            "muMimoUpLink": muMimoUpLink,
            "ofdmaMultiRu": ofdmaMultiRu,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ef28900485c4e9842b4a68e483d4e_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id}"
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
            "bpm_ef28900485c4e9842b4a68e483d4e_v2_3_7_9", json_data
        )

    def get80211be_profile_by_id(self, id, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get80211be-profile-by-i-d
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ae9378f178355aea0e70e5ece0d430e_v2_3_7_9", json_data
        )

    def get_interfaces(
        self,
        interface_name=None,
        limit=None,
        offset=None,
        vlan_id=None,
        headers=None,
        **request_parameters
    ):
        """This API allows the user to get all Interfaces .

        Args:
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
            offset(int): offset query parameter. The first record to show for this page. The first record is
                numbered 1. .
            interface_name(str): interfaceName query parameter. Interface Name .
            vlan_id(int): vlanId query parameter. Vlan Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-interfaces
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(interface_name, str)
        check_type(vlan_id, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "interfaceName": interface_name,
            "vlanId": vlan_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/interfaces"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d2c4823550d79e07dca86c2e8f66_v2_3_7_9", json_data
        )

    def create_interface(
        self,
        interfaceName=None,
        vlanId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-interface
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
            "interfaceName": interfaceName,
            "vlanId": vlanId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fb5e152d4d3d59f5afd92f717f3a1eea_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/interfaces"
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
            "bpm_fb5e152d4d3d59f5afd92f717f3a1eea_v2_3_7_9", json_data
        )

    def get_interface_by_id(self, id, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-interface-by-i-d
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/interfaces/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_feb0798215d52bbdab50542213d44_v2_3_7_9", json_data
        )

    def delete_interface(self, id, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-interface
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/interfaces/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bdfaf07257c5a1190881ddd70dabf1b_v2_3_7_9", json_data
        )

    def update_interface(
        self,
        id,
        interfaceName=None,
        vlanId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-interface
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "interfaceName": interfaceName,
            "vlanId": vlanId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ee43cac5fd65c55ab3153d3549d18c0_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/interfaces/{id}"
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
            "bpm_ee43cac5fd65c55ab3153d3549d18c0_v2_3_7_9", json_data
        )

    def create_power_profile(
        self,
        description=None,
        profileName=None,
        rules=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to create a custom Power Profile. .

        Args:
            description(string): Wireless's Description of the Power Profile. Max allowed characters is 128 .
            profileName(string): Wireless's Name of the Power Profile. Max allowed characters is 128 .
            rules(list): Wireless's rules (list of objects).
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
            https://developer.cisco.com/docs/dna-center/#!create-power-profile
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
            "profileName": profileName,
            "description": description,
            "rules": rules,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cc239fa9b185ecbab9e306289850a63_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/powerProfiles"
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
            "bpm_cc239fa9b185ecbab9e306289850a63_v2_3_7_9", json_data
        )

    def get_power_profiles(
        self,
        limit=None,
        offset=None,
        profile_name=None,
        headers=None,
        **request_parameters
    ):
        """This API allows the user to get Power Profiles that captured in wireless settings design. .

        Args:
            limit(int): limit query parameter.
            offset(int): offset query parameter.
            profile_name(str): profileName query parameter. Power Profile Name .
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
            https://developer.cisco.com/docs/dna-center/#!get-power-profiles
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(profile_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "profileName": profile_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/powerProfiles"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ac4ba3554d259989ff8f52fc1ac8b7c_v2_3_7_9", json_data
        )

    def get_power_profiles_count(self, headers=None, **request_parameters):
        """This API returns the total number of Power Profiles available. .

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
            https://developer.cisco.com/docs/dna-center/#!get-power-profiles-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/powerProfiles/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f71e461c251a5826a88c9eac7d4ed1c0_v2_3_7_9", json_data
        )

    def delete_power_profile_by_id(self, id, headers=None, **request_parameters):
        """This API allows the user to delete an Power Profile by specifying the Power Profile ID. .

        Args:
            id(str): id path parameter. Power Profile ID .
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
            https://developer.cisco.com/docs/dna-center/#!delete-power-profile-by-i-d
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/powerProfiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a82a74143e78550c93b8fcca1fea1041_v2_3_7_9", json_data
        )

    def update_power_profile_by_id(
        self,
        id,
        description=None,
        profileName=None,
        rules=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows the user to update a custom power Profile .

        Args:
            description(string): Wireless's Description of the Power Profile. Max length is 32 characters .
            profileName(string): Wireless's Name of the Power Profile. Max length is 32 characters .
            rules(list): Wireless's rules (list of objects).
            id(str): id path parameter. Power Profile Id .
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
            https://developer.cisco.com/docs/dna-center/#!update-power-profile-by-i-d
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "profileName": profileName,
            "description": description,
            "rules": rules,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f0f7b6e1e4e159e7a40001fc3e649dfc_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/powerProfiles/{id}"
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
            "bpm_f0f7b6e1e4e159e7a40001fc3e649dfc_v2_3_7_9", json_data
        )

    def get_power_profile_by_id(self, id, headers=None, **request_parameters):
        """This API allows the user to get a Power Profile by Power Profile ID that captured in wireless settings design .

        Args:
            id(str): id path parameter. Power Profile ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-power-profile-by-i-d
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/powerProfiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ed0bc9ed852068ecb2addb8350220_v2_3_7_9", json_data
        )

    def create_rf_profile(
        self,
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
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-r-f-profile
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
            "rfProfileName": rfProfileName,
            "defaultRfProfile": defaultRfProfile,
            "enableRadioTypeA": enableRadioTypeA,
            "enableRadioTypeB": enableRadioTypeB,
            "enableRadioType6GHz": enableRadioType6GHz,
            "radioTypeAProperties": radioTypeAProperties,
            "radioTypeBProperties": radioTypeBProperties,
            "radioType6GHzProperties": radioType6GHzProperties,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bcb1d489d735258975828f845df1769_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/rfProfiles"
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
            "bpm_bcb1d489d735258975828f845df1769_v2_3_7_9", json_data
        )

    def get_rf_profiles(
        self,
        enable_radio_type6_g_hz=None,
        enable_radio_type_a=None,
        enable_radio_type_b=None,
        limit=None,
        offset=None,
        rf_profile_name=None,
        headers=None,
        **request_parameters
    ):
        """This API allows the user to get all RF Profiles .

        Args:
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500 .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1 .
            rf_profile_name(str): rfProfileName query parameter. RF Profile Name .
            enable_radio_type_a(bool): enableRadioTypeA query parameter. Enable Radio TypeA .
            enable_radio_type_b(bool): enableRadioTypeB query parameter. Enable Radio TypeB .
            enable_radio_type6_g_hz(bool): enableRadioType6GHz query parameter. Enable Radio Type6GHz .
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
            https://developer.cisco.com/docs/dna-center/#!get-r-f-profiles
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(rf_profile_name, str)
        check_type(enable_radio_type_a, bool)
        check_type(enable_radio_type_b, bool)
        check_type(enable_radio_type6_g_hz, bool)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "rfProfileName": rf_profile_name,
            "enableRadioTypeA": enable_radio_type_a,
            "enableRadioTypeB": enable_radio_type_b,
            "enableRadioType6GHz": enable_radio_type6_g_hz,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/rfProfiles"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e11599ca71552e960dc2cdd182abb9_v2_3_7_9", json_data
        )

    def get_rf_profiles_count(self, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-r-f-profiles-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/rfProfiles/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f91267d9ae54ae85b4ddad0b92a2dd_v2_3_7_9", json_data
        )

    def delete_rf_profile(self, id, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-r-f-profile
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/rfProfiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dd7b861ab3e8520486d956a1a171dd63_v2_3_7_9", json_data
        )

    def get_rf_profile_by_id(self, id, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-r-f-profile-by-i-d
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/rfProfiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f59b09f4f1cb5b1c9ddb50e2b81815ef_v2_3_7_9", json_data
        )

    def update_rf_profile(
        self,
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
        **request_parameters
    ):
        """This API allows the user to update a custom RF Profile. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-r-f-profile
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "rfProfileName": rfProfileName,
            "defaultRfProfile": defaultRfProfile,
            "enableRadioTypeA": enableRadioTypeA,
            "enableRadioTypeB": enableRadioTypeB,
            "enableRadioType6GHz": enableRadioType6GHz,
            "radioTypeAProperties": radioTypeAProperties,
            "radioTypeBProperties": radioTypeBProperties,
            "radioType6GHzProperties": radioType6GHzProperties,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_da455f4be5b75126ba9970c7cc54c7db_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/wirelessSettings/rfProfiles/{id}"
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
            "bpm_da455f4be5b75126ba9970c7cc54c7db_v2_3_7_9", json_data
        )

    def retrieve_sites_with_overridden_ssids(
        self, limit=None, offset=None, site_id=None, headers=None, **request_parameters
    ):
        """Retrieve list of siteId(s) with information of SSID(s) which are overridden .

        Args:
            site_id(str): siteId query parameter. Site UUID .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1 .
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-sites-with-overridden-s-s-i-ds
        """
        check_type(headers, dict)
        check_type(site_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
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

        e_url = "/dna/intent/api/v1/wirelessSettings/ssids/overrideAtSite" + "s"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d3c9ecf485c29b68497b7b6730e83_v2_3_7_9", json_data
        )

    def assign_anchor_managed_ap_locations_for_w_l_c(
        self,
        network_device_id,
        anchorManagedAPLocationsSiteIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows user to assign Anchor Managed AP Locations for WLC by device ID. The payload should always be a
        complete list. The Managed AP Locations included in the payload will be fully processed for both
        addition and deletion.         When anchor managed location array present then it will add the anchor
        managed locations. .

        Args:
            anchorManagedAPLocationsSiteIds(list): Wireless's This API allows user to assign Anchor Managed AP
                Locations for WLC by device ID. The payload should always be a complete list. The
                Managed AP Locations included in the payload will be fully processed for both addition
                and deletion.                When anchor managed location array present then it will add
                the anchor managed locations.  (list of strings).
            network_device_id(str): networkDeviceId path parameter. Network Device ID. This value can be obtained by
                using the API call GET: /dna/intent/api/v1/network-device/ip-address/${ipAddress} .
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
            https://developer.cisco.com/docs/dna-center/#!assign-anchor-managed-a-p-locations-for-w-l-c
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }
        _payload = {
            "anchorManagedAPLocationsSiteIds": anchorManagedAPLocationsSiteIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_af893464e53d2abc8922f4f3310ea_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wirelessSettings/{networkDeviceId}/as"
            + "signAnchorManagedApLocations"
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
            "bpm_af893464e53d2abc8922f4f3310ea_v2_3_7_9", json_data
        )

    def configure_access_points_v2(
        self,
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
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!configure-access-points-v2
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "apList": apList,
            "configureAdminStatus": configureAdminStatus,
            "adminStatus": adminStatus,
            "configureApMode": configureApMode,
            "apMode": apMode,
            "configureFailoverPriority": configureFailoverPriority,
            "failoverPriority": failoverPriority,
            "configureLedStatus": configureLedStatus,
            "ledStatus": ledStatus,
            "configureLedBrightnessLevel": configureLedBrightnessLevel,
            "ledBrightnessLevel": ledBrightnessLevel,
            "configureLocation": configureLocation,
            "location": location,
            "configureHAController": configureHAController,
            "primaryControllerName": primaryControllerName,
            "primaryIpAddress": primaryIpAddress,
            "secondaryControllerName": secondaryControllerName,
            "secondaryIpAddress": secondaryIpAddress,
            "tertiaryControllerName": tertiaryControllerName,
            "tertiaryIpAddress": tertiaryIpAddress,
            "radioConfigurations": radioConfigurations,
            "configureCleanAirSI24Ghz": configureCleanAirSI24Ghz,
            "cleanAirSI24": cleanAirSI24,
            "configureCleanAirSI5Ghz": configureCleanAirSI5Ghz,
            "cleanAirSI5": cleanAirSI5,
            "configureCleanAirSI6Ghz": configureCleanAirSI6Ghz,
            "cleanAirSI6": cleanAirSI6,
            "isAssignedSiteAsLocation": isAssignedSiteAsLocation,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_deb34387d0235811a90985711be9fe2e_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/wireless/accesspoint-configuration"
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
            "bpm_deb34387d0235811a90985711be9fe2e_v2_3_7_9", json_data
        )

    def get_interfaces_count(self, headers=None, **request_parameters):
        """This API allows the user to get count of all interfaces. .

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
            https://developer.cisco.com/docs/dna-center/#!get-interfaces-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/intent/api/v1/wirelessSettings/interfaces/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_e2472592d96a069b246c26531_v2_3_7_9", json_data)

    # Alias Functions
    @deprecated
    def get_all80211be_profiles(self, headers=None, **request_parameters):
        """alias for get80211be_profiles"""
        return self.get80211be_profiles(headers=headers, **request_parameters)

    @deprecated
    def get_all_mobility_groups(
        self, network_device_id=None, headers=None, **request_parameters
    ):
        """alias for get_mobility_groups"""
        return self.get_mobility_groups(
            network_device_id=network_device_id, headers=headers, **request_parameters
        )

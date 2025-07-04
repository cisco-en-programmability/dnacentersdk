# -*- coding: utf-8 -*-
"""Cisco Catalyst Center AI Endpoint Analytics API wrapper.

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
)


class AIEndpointAnalytics(object):
    """Cisco Catalyst Center AI Endpoint Analytics API (version: 3.1.3.0).

    Wraps the Catalyst Center AI Endpoint Analytics
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new AIEndpointAnalytics
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(AIEndpointAnalytics, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_anc_policies(self, headers=None, **request_parameters):
        """Fetches the list of ANC policies available in ISE. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!get-a-n-c-policies
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

        e_url = "/dna/intent/api/v1/endpoint-analytics/anc-policies"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c888e4f05d80571483ebe5793f6c44c1_v3_1_3_0", json_data
        )

    def process_cmdb_endpoints(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Processes incoming CMDB endpoints data and imports the same in AI Endpoint Analytics. .

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
            https://developer.cisco.com/docs/dna-center/#!process-c-m-d-b-endpoints
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_aba18f6e605ce28a112b34dcb4fe82_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/cmdb/endpoints"
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
            "bpm_aba18f6e605ce28a112b34dcb4fe82_v3_1_3_0", json_data
        )

    def get_ai_endpoint_analytics_attribute_dictionaries(
        self, include_attributes=None, headers=None, **request_parameters
    ):
        """Fetches the list of attribute dictionaries. .

        Args:
            include_attributes(bool): includeAttributes query parameter. Flag to indicate whether attribute list for
                each dictionary should be included in response. .
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
            https://developer.cisco.com/docs/dna-center/#!get-a-i-endpoint-analytics-attribute-dictionaries
        """
        check_type(headers, dict)
        check_type(include_attributes, bool)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "includeAttributes": include_attributes,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/dictionaries"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b12a3ca89c475179b182da81bdb64a8a_v3_1_3_0", json_data
        )

    def register_an_endpoint(
        self,
        deviceType=None,
        hardwareManufacturer=None,
        hardwareModel=None,
        macAddress=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Register a new endpoint in the system. .

        Args:
            deviceType(string): AI Endpoint Analytics's Type of the device represented by this endpoint. .
            hardwareManufacturer(string): AI Endpoint Analytics's Hardware manufacturer for the endpoint. .
            hardwareModel(string): AI Endpoint Analytics's Hardware model of the endpoint. .
            macAddress(string): AI Endpoint Analytics's MAC address of the endpoint. .
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
            https://developer.cisco.com/docs/dna-center/#!register-an-endpoint
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
            "macAddress": macAddress,
            "deviceType": deviceType,
            "hardwareManufacturer": hardwareManufacturer,
            "hardwareModel": hardwareModel,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b7ae9494b05a57bf6393eaf308b1e7_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/endpoints"
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
            "bpm_b7ae9494b05a57bf6393eaf308b1e7_v3_1_3_0", json_data
        )

    def query_the_endpoints(
        self,
        ai_spoofing_trust_level=None,
        anc_policy=None,
        auth_method=None,
        changed_profile_trust_level=None,
        concurrent_mac_trust_level=None,
        device_type=None,
        hardware_manufacturer=None,
        hardware_model=None,
        include=None,
        ip=None,
        ip_blocklist_detected=None,
        limit=None,
        mac_address=None,
        mac_addresses=None,
        nat_trust_level=None,
        offset=None,
        operating_system=None,
        order=None,
        posture_status=None,
        profiling_status=None,
        random_mac=None,
        registered=None,
        sort_by=None,
        trust_score=None,
        unauth_port_detected=None,
        weak_cred_detected=None,
        headers=None,
        **request_parameters
    ):
        """Query the endpoints, optionally using various filter and pagination criteria. 'GET /endpoints/count' API can be
        used to find out the total number of endpoints matching the filter criteria. .

        Args:
            profiling_status(str): profilingStatus query parameter. Profiling status of the endpoint. Possible
                values are 'profiled', 'partialProfiled', 'notProfiled'. .
            mac_address(str): macAddress query parameter. MAC address to search for. Partial string is allowed. .
            mac_addresses(list, set, str, tuple): macAddresses query parameter. List of MAC addresses to filter on.
                Only exact matches will be returned. .
            ip(str): ip query parameter. IP address to search for. Partial string is allowed. .
            device_type(str): deviceType query parameter. Type of device to search for. Partial string is allowed. .
            hardware_manufacturer(str): hardwareManufacturer query parameter. Hardware manufacturer to search for.
                Partial string is allowed. .
            hardware_model(str): hardwareModel query parameter. Hardware model to search for. Partial string is
                allowed. .
            operating_system(str): operatingSystem query parameter. Operating system to search for. Partial string
                is allowed. .
            registered(bool): registered query parameter. Flag to fetch manually registered or non-registered
                endpoints. .
            random_mac(bool): randomMac query parameter. Flag to fetch endpoints having randomized MAC or not. .
            trust_score(str): trustScore query parameter. Overall trust score of the endpoint. It can be provided
                either as a number value (e.g. 5), or as a range (e.g. 3-7). Provide value as '-' if you
                want to search for all endpoints where trust score is not assigned. .
            auth_method(str): authMethod query parameter. Authentication method. Partial string is allowed. .
            posture_status(str): postureStatus query parameter. Posture status. .
            ai_spoofing_trust_level(str): aiSpoofingTrustLevel query parameter. Trust level of the endpoint due to
                AI spoofing. Possible values are 'low', 'medium', 'high'. .
            changed_profile_trust_level(str): changedProfileTrustLevel query parameter. Trust level of the endpoint
                due to changing profile labels. Possible values are 'low', 'medium', 'high'. .
            nat_trust_level(str): natTrustLevel query parameter. Trust level of the endpoint due to NAT access.
                Possible values are 'low', 'medium', 'high'. .
            concurrent_mac_trust_level(str): concurrentMacTrustLevel query parameter. Trust level of the endpoint
                due to concurrent MAC address. Possible values are 'low', 'medium', 'high'. .
            ip_blocklist_detected(bool): ipBlocklistDetected query parameter. Flag to fetch endpoints hitting IP
                blocklist or not. .
            unauth_port_detected(bool): unauthPortDetected query parameter. Flag to fetch endpoints exposing
                unauthorized ports or not. .
            weak_cred_detected(bool): weakCredDetected query parameter. Flag to fetch endpoints having weak
                credentials or not. .
            anc_policy(str): ancPolicy query parameter. ANC policy. Only exact match will be returned. .
            limit(int): limit query parameter. Maximum number of records to be fetched. If not provided, 50 records
                will be fetched by default. Maximum 1000 records can be fetched at a time. Use
                pagination if more records need to be fetched. .
            offset(int): offset query parameter. Record offset to start data fetch at. Offset starts at zero. .
            sort_by(str): sortBy query parameter. Name of the column to sort the results on. Please note that fetch
                might take more time if sorting is requested. Possible values are 'macAddress', 'ip'. .
            order(str): order query parameter. Order to be used for sorting. Possible values are 'asc', 'desc'. .
            include(str): include query parameter. The datasets that should be included in the response. By default,
                value of this parameter is blank, and the response will include only basic details of
                the endpoint. To include other datasets or dictionaries, send comma separated list of
                following values: 'ALL' Include all attributes. 'CDP', 'DHCP', etc. Include attributes
                from given dictionaries. To get full list of dictionaries, use corresponding GET API.
                'ANC' Include ANC policy related details. 'TRUST' Include trust score details. .
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
            https://developer.cisco.com/docs/dna-center/#!query-the-endpoints
        """
        check_type(headers, dict)
        check_type(profiling_status, str)
        check_type(mac_address, str)
        check_type(mac_addresses, (list, set, str, tuple))
        check_type(ip, str)
        check_type(device_type, str)
        check_type(hardware_manufacturer, str)
        check_type(hardware_model, str)
        check_type(operating_system, str)
        check_type(registered, bool)
        check_type(random_mac, bool)
        check_type(trust_score, str)
        check_type(auth_method, str)
        check_type(posture_status, str)
        check_type(ai_spoofing_trust_level, str)
        check_type(changed_profile_trust_level, str)
        check_type(nat_trust_level, str)
        check_type(concurrent_mac_trust_level, str)
        check_type(ip_blocklist_detected, bool)
        check_type(unauth_port_detected, bool)
        check_type(weak_cred_detected, bool)
        check_type(anc_policy, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(include, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "profilingStatus": profiling_status,
            "macAddress": mac_address,
            "macAddresses": mac_addresses,
            "ip": ip,
            "deviceType": device_type,
            "hardwareManufacturer": hardware_manufacturer,
            "hardwareModel": hardware_model,
            "operatingSystem": operating_system,
            "registered": registered,
            "randomMac": random_mac,
            "trustScore": trust_score,
            "authMethod": auth_method,
            "postureStatus": posture_status,
            "aiSpoofingTrustLevel": ai_spoofing_trust_level,
            "changedProfileTrustLevel": changed_profile_trust_level,
            "natTrustLevel": nat_trust_level,
            "concurrentMacTrustLevel": concurrent_mac_trust_level,
            "ipBlocklistDetected": ip_blocklist_detected,
            "unauthPortDetected": unauth_port_detected,
            "weakCredDetected": weak_cred_detected,
            "ancPolicy": anc_policy,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "include": include,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/endpoints"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b4f18988d61253bd8565ce2a22a909ae_v3_1_3_0", json_data
        )

    def fetch_the_count_of_endpoints(
        self,
        ai_spoofing_trust_level=None,
        anc_policy=None,
        auth_method=None,
        changed_profile_trust_level=None,
        concurrent_mac_trust_level=None,
        device_type=None,
        hardware_manufacturer=None,
        hardware_model=None,
        ip=None,
        ip_blocklist_detected=None,
        mac_address=None,
        mac_addresses=None,
        nat_trust_level=None,
        operating_system=None,
        posture_status=None,
        profiling_status=None,
        random_mac=None,
        registered=None,
        trust_score=None,
        unauth_port_detected=None,
        weak_cred_detected=None,
        headers=None,
        **request_parameters
    ):
        """Fetch the total count of endpoints that match the given filter criteria. .

        Args:
            profiling_status(str): profilingStatus query parameter. Profiling status of the endpoint. Possible
                values are 'profiled', 'partialProfiled', 'notProfiled'. .
            mac_address(str): macAddress query parameter. MAC address to search for. Partial string is allowed. .
            mac_addresses(list, set, str, tuple): macAddresses query parameter. List of MAC addresses to filter on.
                Only exact matches will be returned. .
            ip(str): ip query parameter. IP address to search for. Partial string is allowed. .
            device_type(str): deviceType query parameter. Type of device to search for. Partial string is allowed. .
            hardware_manufacturer(str): hardwareManufacturer query parameter. Hardware manufacturer to search for.
                Partial string is allowed. .
            hardware_model(str): hardwareModel query parameter. Hardware model to search for. Partial string is
                allowed. .
            operating_system(str): operatingSystem query parameter. Operating system to search for. Partial string
                is allowed. .
            registered(bool): registered query parameter. Flag to fetch manually registered or non-registered
                endpoints. .
            random_mac(bool): randomMac query parameter. Flag to fetch endpoints having randomized MAC or not. .
            trust_score(str): trustScore query parameter. Overall trust score of the endpoint. It can be provided
                either as a number value (e.g. 5), or as a range (e.g. 3-7). Provide value as '-' if you
                want to search for all endpoints where trust score is not assigned. .
            auth_method(str): authMethod query parameter. Authentication method. Partial string is allowed. .
            posture_status(str): postureStatus query parameter. Posture status. .
            ai_spoofing_trust_level(str): aiSpoofingTrustLevel query parameter. Trust level of the endpoint due to
                AI spoofing. Possible values are 'low', 'medium', 'high'. .
            changed_profile_trust_level(str): changedProfileTrustLevel query parameter. Trust level of the endpoint
                due to changing profile labels. Possible values are 'low', 'medium', 'high'. .
            nat_trust_level(str): natTrustLevel query parameter. Trust level of the endpoint due to NAT access.
                Possible values are 'low', 'medium', 'high'. .
            concurrent_mac_trust_level(str): concurrentMacTrustLevel query parameter. Trust level of the endpoint
                due to concurrent MAC address. Possible values are 'low', 'medium', 'high'. .
            ip_blocklist_detected(bool): ipBlocklistDetected query parameter. Flag to fetch endpoints hitting IP
                blocklist or not. .
            unauth_port_detected(bool): unauthPortDetected query parameter. Flag to fetch endpoints exposing
                unauthorized ports or not. .
            weak_cred_detected(bool): weakCredDetected query parameter. Flag to fetch endpoints having weak
                credentials or not. .
            anc_policy(str): ancPolicy query parameter. ANC policy. Only exact match will be returned. .
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
            https://developer.cisco.com/docs/dna-center/#!fetch-the-count-of-endpoints
        """
        check_type(headers, dict)
        check_type(profiling_status, str)
        check_type(mac_address, str)
        check_type(mac_addresses, (list, set, str, tuple))
        check_type(ip, str)
        check_type(device_type, str)
        check_type(hardware_manufacturer, str)
        check_type(hardware_model, str)
        check_type(operating_system, str)
        check_type(registered, bool)
        check_type(random_mac, bool)
        check_type(trust_score, str)
        check_type(auth_method, str)
        check_type(posture_status, str)
        check_type(ai_spoofing_trust_level, str)
        check_type(changed_profile_trust_level, str)
        check_type(nat_trust_level, str)
        check_type(concurrent_mac_trust_level, str)
        check_type(ip_blocklist_detected, bool)
        check_type(unauth_port_detected, bool)
        check_type(weak_cred_detected, bool)
        check_type(anc_policy, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "profilingStatus": profiling_status,
            "macAddress": mac_address,
            "macAddresses": mac_addresses,
            "ip": ip,
            "deviceType": device_type,
            "hardwareManufacturer": hardware_manufacturer,
            "hardwareModel": hardware_model,
            "operatingSystem": operating_system,
            "registered": registered,
            "randomMac": random_mac,
            "trustScore": trust_score,
            "authMethod": auth_method,
            "postureStatus": posture_status,
            "aiSpoofingTrustLevel": ai_spoofing_trust_level,
            "changedProfileTrustLevel": changed_profile_trust_level,
            "natTrustLevel": nat_trust_level,
            "concurrentMacTrustLevel": concurrent_mac_trust_level,
            "ipBlocklistDetected": ip_blocklist_detected,
            "unauthPortDetected": unauth_port_detected,
            "weakCredDetected": weak_cred_detected,
            "ancPolicy": anc_policy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/endpoints/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fab7e4bf248589894a0ad79c4f0940f_v3_1_3_0", json_data
        )

    def update_a_registered_endpoint(
        self,
        ep_id,
        deviceType=None,
        hardwareManufacturer=None,
        hardwareModel=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update attributes of a registered endpoint. .

        Args:
            deviceType(string): AI Endpoint Analytics's Type of the device represented by this endpoint. .
            hardwareManufacturer(string): AI Endpoint Analytics's Hardware manufacturer for the endpoint. .
            hardwareModel(string): AI Endpoint Analytics's Hardware model of the endpoint. .
            ep_id(str): epId path parameter. Unique identifier for the endpoint. .
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
            https://developer.cisco.com/docs/dna-center/#!update-a-registered-endpoint
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(ep_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "epId": ep_id,
        }
        _payload = {
            "deviceType": deviceType,
            "hardwareManufacturer": hardwareManufacturer,
            "hardwareModel": hardwareModel,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b107800544384c1ddad7b60c237_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/endpoints/{epId}"
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
            "bpm_b107800544384c1ddad7b60c237_v3_1_3_0", json_data
        )

    def get_endpoint_details(
        self, ep_id, include=None, headers=None, **request_parameters
    ):
        """Fetches details of the endpoint for the given unique identifier 'epId'. .

        Args:
            ep_id(str): epId path parameter. Unique identifier for the endpoint. .
            include(str): include query parameter. The datasets that should be included in the response. By default,
                value of this parameter is blank, and the response will include only basic details of
                the endpoint. To include other datasets or dictionaries, send comma separated list of
                following values: 'ALL' Include all attributes. 'CDP', 'DHCP', etc. Include attributes
                from given dictionaries. To get full list of dictionaries, use corresponding GET API.
                'ANC' Include ANC policy related details. 'TRUST' Include trust score details. .
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
            https://developer.cisco.com/docs/dna-center/#!get-endpoint-details
        """
        check_type(headers, dict)
        check_type(include, str)
        check_type(ep_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "include": include,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "epId": ep_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/endpoints/{epId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cde73293a8235ed8ae4cfe5f6717bff1_v3_1_3_0", json_data
        )

    def delete_an_endpoint(self, ep_id, headers=None, **request_parameters):
        """Deletes the endpoint for the given unique identifier 'epId'. .

        Args:
            ep_id(str): epId path parameter. Unique identifier for the endpoint. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-an-endpoint
        """
        check_type(headers, dict)
        check_type(ep_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "epId": ep_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/endpoints/{epId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d82c78cf10395b2baba3b51fd8370a14_v3_1_3_0", json_data
        )

    def apply_anc_policy(
        self,
        ep_id,
        ancPolicy=None,
        granularAncPolicy=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Applies given ANC policy to the endpoint. .

        Args:
            ancPolicy(string): AI Endpoint Analytics's ANC policy name. .
            granularAncPolicy(list): AI Endpoint Analytics's granularAncPolicy (list of objects).
            ep_id(str): epId path parameter. Unique identifier for the endpoint. .
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
            https://developer.cisco.com/docs/dna-center/#!apply-a-n-c-policy
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(ep_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "epId": ep_id,
        }
        _payload = {
            "ancPolicy": ancPolicy,
            "granularAncPolicy": granularAncPolicy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_de92f8ae3c15ea0bad5562452eb5c40_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-" + "analytics/endpoints/{epId}/anc-policy"
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
            "bpm_de92f8ae3c15ea0bad5562452eb5c40_v3_1_3_0", json_data
        )

    def revoke_anc_policy(self, ep_id, headers=None, **request_parameters):
        """Revokes given ANC policy from the endpoint. .

        Args:
            ep_id(str): epId path parameter. Unique identifier for the endpoint. .
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
            https://developer.cisco.com/docs/dna-center/#!revoke-a-n-c-policy
        """
        check_type(headers, dict)
        check_type(ep_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "epId": ep_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-" + "analytics/endpoints/{epId}/anc-policy"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f136ac6d3b145d35922c4ba15ccb941a_v3_1_3_0", json_data
        )

    def create_a_profiling_rule(
        self,
        clusterId=None,
        conditionGroups=None,
        isDeleted=None,
        lastModifiedBy=None,
        lastModifiedOn=None,
        pluginId=None,
        rejected=None,
        result=None,
        ruleId=None,
        ruleName=None,
        rulePriority=None,
        ruleType=None,
        ruleVersion=None,
        sourcePriority=None,
        usedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates profiling rule from the request body. .

        Args:
            clusterId(string): AI Endpoint Analytics's Unique identifier for ML cluster. Only applicable for 'ML
                Rule'. .
            conditionGroups(object): AI Endpoint Analytics's conditionGroups.
            isDeleted(boolean): AI Endpoint Analytics's Flag to indicate whether the rule was deleted. .
            lastModifiedBy(string): AI Endpoint Analytics's User that last modified the rule. It is read-only, and
                is ignored if provided as part of input request. .
            lastModifiedOn(integer): AI Endpoint Analytics's Timestamp (in epoch milliseconds) of last modification.
                It is read-only, and is ignored if provided as part of input request. .
            pluginId(string): AI Endpoint Analytics's Plugin for the rule. Only applicable for 'Cisco Default'
                rules. .
            rejected(boolean): AI Endpoint Analytics's Flag to indicate whether rule has been rejected by user or
                not. Only applicable for 'ML Rule'. .
            result(object): AI Endpoint Analytics's result.
            ruleId(string): AI Endpoint Analytics's Unique identifier for the rule. This is normally generated by
                the system, and client does not need to provide it for rules that need to be newly
                created. .
            ruleName(string): AI Endpoint Analytics's Human readable name for the rule. .
            rulePriority(integer): AI Endpoint Analytics's Priority for the rule. .
            ruleType(string): AI Endpoint Analytics's Type of the rule. . Available values are 'Cisco Default -
                Static', 'Cisco Default - Dynamic', 'Custom Rule' and 'ML Rule'.
            ruleVersion(integer): AI Endpoint Analytics's Version of the rule. .
            sourcePriority(integer): AI Endpoint Analytics's Source priority for the rule. .
            usedAttributes(list): AI Endpoint Analytics's List of attributes used in the rule. Only applicable for
                'Cisco Default' rules.  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!create-a-profiling-rule
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
            "ruleId": ruleId,
            "ruleName": ruleName,
            "ruleType": ruleType,
            "ruleVersion": ruleVersion,
            "rulePriority": rulePriority,
            "sourcePriority": sourcePriority,
            "isDeleted": isDeleted,
            "lastModifiedBy": lastModifiedBy,
            "lastModifiedOn": lastModifiedOn,
            "pluginId": pluginId,
            "clusterId": clusterId,
            "rejected": rejected,
            "result": result,
            "conditionGroups": conditionGroups,
            "usedAttributes": usedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bf80823752baba63a8849fd521cd_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/profiling-rules"
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
            "bpm_bf80823752baba63a8849fd521cd_v3_1_3_0", json_data
        )

    def get_list_of_profiling_rules(
        self,
        include_deleted=None,
        limit=None,
        offset=None,
        order=None,
        rule_type=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """This API fetches the list of profiling rules. It can be used to show profiling rules in client applications, or
        export those from an environment. 'POST /profiling-rules/bulk' API can be used to import such exported
        rules into another environment. If this API is used to export rules to be imported into another Cisco
        Catalyst Center system, then ensure that 'includeDeleted' parameter is 'true', so that deleted rules get
        synchronized correctly. Use query parameters to filter the data, as required. If no filter is provided,
        then it will include only rules of type 'Custom Rule' in the response. By default, the response is
        limited to 500 records. Use 'limit' parameter to fetch higher number of records, if required. 'GET
        /profiling-rules/count' API can be used to find out the total number of rules in the system. .

        Args:
            rule_type(str): ruleType query parameter. Use comma-separated list of rule types to filter the data.
                Defaults to 'Custom Rule'. .
            include_deleted(bool): includeDeleted query parameter. Flag to indicate whether deleted rules should be
                part of the records fetched. .
            limit(int): limit query parameter. Maximum number of records to be fetched. If not provided, 500 records
                will be fetched by default. To fetch all the records in the system, provide a large
                value for this parameter. .
            offset(int): offset query parameter. Record offset to start data fetch at. Offset starts at zero. .
            sort_by(str): sortBy query parameter. Name of the column to sort the results on. Please note that fetch
                might take more time if sorting is requested. .
            order(str): order query parameter. Order to be used for sorting. .
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
            https://developer.cisco.com/docs/dna-center/#!get-list-of-profiling-rules
        """
        check_type(headers, dict)
        check_type(rule_type, str)
        check_type(include_deleted, bool)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "ruleType": rule_type,
            "includeDeleted": include_deleted,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/profiling-rules"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a4571194a9e05664ad348f72d7651bb0_v3_1_3_0", json_data
        )

    def import_profiling_rules_in_bulk(
        self,
        profilingRules=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API imports the given list of profiling rules. For each record, 1) If 'ruleType' for a record is not
        'Custom Rule', then it is rejected. 2) If 'ruleId' is provided in the input record,    2a) Record with
        same 'ruleId' exists in the system, then it is replaced with new data.   2b) Record with same 'ruleId'
        does not exist, then it is inserted in the database. 3) If 'ruleId' is not provided in the input record,
        then new 'ruleId' is generated by the system, and record is inserted. .

        Args:
            profilingRules(list): AI Endpoint Analytics's profilingRules (list of objects).
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
            https://developer.cisco.com/docs/dna-center/#!import-profiling-rules-in-bulk
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
            "profilingRules": profilingRules,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_b4155d6f885a53ad0e47b1a4_v3_1_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/profiling-" + "rules/bulk"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_b4155d6f885a53ad0e47b1a4_v3_1_3_0", json_data)

    def get_count_of_profiling_rules(
        self, include_deleted=None, rule_type=None, headers=None, **request_parameters
    ):
        """This API fetches the count of profiling rules based on the filter values provided in the query parameters. The
        filter parameters are same as that of 'GET /profiling-rules' API, excluding the pagination and sort
        parameters. .

        Args:
            rule_type(str): ruleType query parameter. Use comma-separated list of rule types to filter the data.
                Defaults to 'Custom Rule'. .
            include_deleted(bool): includeDeleted query parameter. Flag to indicate whether deleted rules should be
                part of the records fetched. .
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-profiling-rules
        """
        check_type(headers, dict)
        check_type(rule_type, str)
        check_type(include_deleted, bool)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "ruleType": rule_type,
            "includeDeleted": include_deleted,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/profiling-" + "rules/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ec43ed2e44c5f3ea7a904d39af66899_v3_1_3_0", json_data
        )

    def update_an_existing_profiling_rule(
        self,
        rule_id,
        clusterId=None,
        conditionGroups=None,
        isDeleted=None,
        lastModifiedBy=None,
        lastModifiedOn=None,
        pluginId=None,
        rejected=None,
        result=None,
        ruleId=None,
        ruleName=None,
        rulePriority=None,
        ruleType=None,
        ruleVersion=None,
        sourcePriority=None,
        usedAttributes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates the profiling rule for the given 'ruleId'. .

        Args:
            clusterId(string): AI Endpoint Analytics's Unique identifier for ML cluster. Only applicable for 'ML
                Rule'. .
            conditionGroups(object): AI Endpoint Analytics's conditionGroups.
            isDeleted(boolean): AI Endpoint Analytics's Flag to indicate whether the rule was deleted. .
            lastModifiedBy(string): AI Endpoint Analytics's User that last modified the rule. It is read-only, and
                is ignored if provided as part of input request. .
            lastModifiedOn(integer): AI Endpoint Analytics's Timestamp (in epoch milliseconds) of last modification.
                It is read-only, and is ignored if provided as part of input request. .
            pluginId(string): AI Endpoint Analytics's Plugin for the rule. Only applicable for 'Cisco Default'
                rules. .
            rejected(boolean): AI Endpoint Analytics's Flag to indicate whether rule has been rejected by user or
                not. Only applicable for 'ML Rule'. .
            result(object): AI Endpoint Analytics's result.
            ruleId(string): AI Endpoint Analytics's Unique identifier for the rule. This is normally generated by
                the system, and client does not need to provide it for rules that need to be newly
                created. .
            ruleName(string): AI Endpoint Analytics's Human readable name for the rule. .
            rulePriority(integer): AI Endpoint Analytics's Priority for the rule. .
            ruleType(string): AI Endpoint Analytics's Type of the rule. . Available values are 'Cisco Default -
                Static', 'Cisco Default - Dynamic', 'Custom Rule' and 'ML Rule'.
            ruleVersion(integer): AI Endpoint Analytics's Version of the rule. .
            sourcePriority(integer): AI Endpoint Analytics's Source priority for the rule. .
            usedAttributes(list): AI Endpoint Analytics's List of attributes used in the rule. Only applicable for
                'Cisco Default' rules.  (list of strings).
            rule_id(str): ruleId path parameter. Unique rule identifier .
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
            https://developer.cisco.com/docs/dna-center/#!update-an-existing-profiling-rule
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(rule_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "ruleId": rule_id,
        }
        _payload = {
            "ruleId": ruleId,
            "ruleName": ruleName,
            "ruleType": ruleType,
            "ruleVersion": ruleVersion,
            "rulePriority": rulePriority,
            "sourcePriority": sourcePriority,
            "isDeleted": isDeleted,
            "lastModifiedBy": lastModifiedBy,
            "lastModifiedOn": lastModifiedOn,
            "pluginId": pluginId,
            "clusterId": clusterId,
            "rejected": rejected,
            "result": result,
            "conditionGroups": conditionGroups,
            "usedAttributes": usedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a4dab79d54829548004029a91ba1_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/profiling-" + "rules/{ruleId}"
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
            "bpm_a4dab79d54829548004029a91ba1_v3_1_3_0", json_data
        )

    def get_details_of_a_single_profiling_rule(
        self, rule_id, headers=None, **request_parameters
    ):
        """Fetches details of the profiling rule for the given 'ruleId'. .

        Args:
            rule_id(str): ruleId path parameter. Unique rule identifier .
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
            https://developer.cisco.com/docs/dna-center/#!get-details-of-a-single-profiling-rule
        """
        check_type(headers, dict)
        check_type(rule_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "ruleId": rule_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/profiling-" + "rules/{ruleId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fbea90831e6e57e79062edab0c76f8a1_v3_1_3_0", json_data
        )

    def delete_an_existing_profiling_rule(
        self, rule_id, headers=None, **request_parameters
    ):
        """Deletes the profiling rule for the given 'ruleId'. .

        Args:
            rule_id(str): ruleId path parameter. Unique rule identifier .
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
            https://developer.cisco.com/docs/dna-center/#!delete-an-existing-profiling-rule
        """
        check_type(headers, dict)
        check_type(rule_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "ruleId": rule_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/profiling-" + "rules/{ruleId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a3f7b6780725e83beed53d6ce2256e4_v3_1_3_0", json_data
        )

    def get_task_details(self, task_id, headers=None, **request_parameters):
        """Fetches the details of backend task. Task is typically created by making call to some other API that takes
        longer time to execute. .

        Args:
            task_id(str): taskId path parameter. Unique identifier for the task. .
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
            https://developer.cisco.com/docs/dna-center/#!get-task-details
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
            "taskId": task_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/endpoint-analytics/tasks/{taskId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a0d1d05fe582aa287acb470e3af1d_v3_1_3_0", json_data
        )


# Alias Functions

# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Network Settings API wrapper.

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


class NetworkSettings(object):
    """Cisco Catalyst Center Network Settings API (version: 3.1.3.0).

    Wraps the Catalyst Center Network Settings
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkSettings
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkSettings, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def assign_device_credential_to_site(
        self,
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
        **request_parameters
    ):
        """Assign Device Credential to a site. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!assign-device-credential-to-site
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "__persistbapioutput" in headers:
                check_type(headers.get("__persistbapioutput"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }
        _payload = {
            "cliId": cliId,
            "snmpV2ReadId": snmpV2ReadId,
            "snmpV2WriteId": snmpV2WriteId,
            "httpRead": httpRead,
            "httpWrite": httpWrite,
            "snmpV3Id": snmpV3Id,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e4f91ea42515ccdbc24549b84ca1e90_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/credential-to-site/{siteId}"
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
            "bpm_e4f91ea42515ccdbc24549b84ca1e90_v3_1_3_0", json_data
        )

    def create_device_credentials(
        self,
        settings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-device-credentials
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
            "settings": settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cf2cac6f150c9bee9ade37921b162_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/device-credential"
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
            "bpm_cf2cac6f150c9bee9ade37921b162_v3_1_3_0", json_data
        )

    def update_device_credentials(
        self,
        settings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-device-credentials
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
            "settings": settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d7161b33157dba957ba18eda440c2_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/device-credential"
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
            "bpm_d7161b33157dba957ba18eda440c2_v3_1_3_0", json_data
        )

    def get_device_credential_details(
        self, site_id=None, headers=None, **request_parameters
    ):
        """API to get device credential details. .

        Args:
            site_id(str): siteId query parameter. Site id to retrieve the credential details associated with the
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-device-credential-details
        """
        check_type(headers, dict)
        check_type(site_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/device-credential"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d8cf995d9d99bdc31707817456_v3_1_3_0", json_data
        )

    def delete_device_credential(self, id, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-device-credential
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

        e_url = "/dna/intent/api/v1/device-credential/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e8e021f1c51eeaf0d102084481486_v3_1_3_0", json_data
        )

    def get_global_pool(
        self, limit=None, offset=None, headers=None, **request_parameters
    ):
        """API to get the global pool. .

        Args:
            offset(int): offset query parameter. Offset/starting row. Indexed from 1. Default value of 1. .
            limit(int): limit query parameter. Number of Global Pools to be retrieved. Default is 25 if not
                specified. .
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
            https://developer.cisco.com/docs/dna-center/#!get-global-pool
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/intent/api/v1/global-pool"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ebdcd84fc41754a69eaeacf7c0b0731c_v3_1_3_0", json_data
        )

    def update_global_pool(
        self,
        settings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to update global pool. There is a limit of updating 25 global pools per request. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-global-pool
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
            "settings": settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c380301e3e05423bdc1857ff00ae77a_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/global-pool"
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
            "bpm_c380301e3e05423bdc1857ff00ae77a_v3_1_3_0", json_data
        )

    def create_global_pool(
        self,
        settings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to create global pool. There is a limit of creating 25 global pools per request. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-global-pool
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
            "settings": settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_eecf4323cb285985be72a7e061891059_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/global-pool"
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
            "bpm_eecf4323cb285985be72a7e061891059_v3_1_3_0", json_data
        )

    def delete_global_ip_pool(self, id, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-global-i-p-pool
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

        e_url = "/dna/intent/api/v1/global-pool/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f9079863c95acd945c51f728cbf81f_v3_1_3_0", json_data
        )

    def create_a_global_ip_address_pool(
        self,
        addressSpace=None,
        name=None,
        poolType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates a global IP address pool, which is not bound to a particular site. A global pool must be either an IPv4
        or IPv6 pool. .

        Args:
            addressSpace(object): Network Settings's addressSpace.
            name(string): Network Settings's The name for this reserve IP pool. Only letters, numbers, '-' (hyphen),
                '_' (underscore), '.' (period), and '/' (forward slash) are allowed. .
            poolType(string): Network Settings's Once created, a global pool type cannot be changed. Tunnel: Assigns
                IP addresses to site-to-site VPN for IPSec tunneling. Generic: used for all other
                network types. . Available values are 'Generic' and 'Tunnel'.
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
            https://developer.cisco.com/docs/dna-center/#!create-a-global-i-p-address-pool
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
            "addressSpace": addressSpace,
            "name": name,
            "poolType": poolType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d833c51c4f5cd2879d3e69f773295c_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/ipam/globalIpAddressPools"
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
            "bpm_d833c51c4f5cd2879d3e69f773295c_v3_1_3_0", json_data
        )

    def retrieves_global_ip_address_pools(
        self,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves global IP address pools. Global pools are not associated with any particular site, but may have
        portions of their address space reserved by site-specific subpools. .

        Args:
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page; the minimum is 1, and
                the maximum is 500. .
            sort_by(str): sortBy query parameter. A property within the response to sort by. .
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-global-i-p-address-pools
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
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

        e_url = "/dna/intent/api/v1/ipam/globalIpAddressPools"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c6b166895678be157ab0d389c0c6_v3_1_3_0", json_data
        )

    def counts_global_ip_address_pools(self, headers=None, **request_parameters):
        """Counts global IP address pools. Global pools are not associated with any particular site, but may have portions
        of their address space reserved by site-specific subpools. .

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
            https://developer.cisco.com/docs/dna-center/#!counts-global-i-p-address-pools
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

        e_url = "/dna/intent/api/v1/ipam/globalIpAddressPools/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ab655674f4156dc92f7ba1ed3a0de68_v3_1_3_0", json_data
        )

    def retrieves_subpools_ids_of_a_global_ip_address_pool(
        self,
        global_ip_address_pool_id,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves subpools IDs of a global IP address pool.  The IDs can be fetched with
        `/dna/intent/api/v1/ipam/siteIpAddressPools/{id}` .

        Args:
            global_ip_address_pool_id(str): globalIpAddressPoolId path parameter. The `id` of the global IP address
                pool for which to retrieve subpool IDs. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page; the minimum is 1, and
                the maximum is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-subpools-i-ds-of-a-global-i-p-address-pool
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(global_ip_address_pool_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "globalIpAddressPoolId": global_ip_address_pool_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/ipam/globalIpAddressPools/{globalIpAd"
            + "dressPoolId}/subpools"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e3d5e2a49655fa8fa7a0257a0fcd35_v3_1_3_0", json_data
        )

    def counts_subpools_of_a_global_ip_address_pool(
        self, global_ip_address_pool_id, headers=None, **request_parameters
    ):
        """Counts subpools of a global IP address pool. .

        Args:
            global_ip_address_pool_id(str): globalIpAddressPoolId path parameter. The `id` of the global IP address
                pool for which to count subpools. .
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
            https://developer.cisco.com/docs/dna-center/#!counts-subpools-of-a-global-i-p-address-pool
        """
        check_type(headers, dict)
        check_type(global_ip_address_pool_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "globalIpAddressPoolId": global_ip_address_pool_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/ipam/globalIpAddressPools/{globalIpAd"
            + "dressPoolId}/subpools/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cdc0978bfef5699abbfabf52ecd5fa8_v3_1_3_0", json_data
        )

    def retrieves_a_global_ip_address_pool(
        self, id, headers=None, **request_parameters
    ):
        """Retrieves a global IP address pool. Global pools are not associated with any particular site, but may have
        portions of their address space reserved by site-specific subpools. .

        Args:
            id(str): id path parameter. The `id` of the global IP address pool to retrieve. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-a-global-i-p-address-pool
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

        e_url = "/dna/intent/api/v1/ipam/globalIpAddressPools/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe2440acbc059fb866295bb4d4eeb38_v3_1_3_0", json_data
        )

    def updates_a_global_ip_address_pool(
        self,
        id,
        addressSpace=None,
        name=None,
        poolType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates a global IP address pool. Restrictions on updating a global IP address pool: The `poolType` cannot be
        changed. The `subnet` and `prefixLength` within `addressSpace` cannot be changed. .

        Args:
            addressSpace(object): Network Settings's addressSpace.
            name(string): Network Settings's The name for this reserve IP pool. Only letters, numbers, '-' (hyphen),
                '_' (underscore), '.' (period), and '/' (forward slash) are allowed. .
            poolType(string): Network Settings's Once created, a global pool type cannot be changed. Tunnel: Assigns
                IP addresses to site-to-site VPN for IPSec tunneling. Generic: used for all other
                network types. . Available values are 'Generic' and 'Tunnel'.
            id(str): id path parameter. The `id` of the global IP address pool to update. .
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
            https://developer.cisco.com/docs/dna-center/#!updates-a-global-i-p-address-pool
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
            "addressSpace": addressSpace,
            "name": name,
            "poolType": poolType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e235d44e4485bafa4499f5a8e53bcd3_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/ipam/globalIpAddressPools/{id}"
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
            "bpm_e235d44e4485bafa4499f5a8e53bcd3_v3_1_3_0", json_data
        )

    def delete_a_global_ip_address_pool(self, id, headers=None, **request_parameters):
        """Deletes a global IP address pool.  A global IP address pool can only be deleted if there are no subpools
        reserving address space from it. .

        Args:
            id(str): id path parameter. The `id` of the global IP address pool to delete. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-global-i-p-address-pool
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

        e_url = "/dna/intent/api/v1/ipam/globalIpAddressPools/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ca56aef75ed559f821e14d17e289d7b_v3_1_3_0", json_data
        )

    def reservecreate_ip_address_subpools(
        self,
        ipV4AddressSpace=None,
        ipV6AddressSpace=None,
        name=None,
        poolType=None,
        siteId=None,
        siteName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Reserves (creates) an IP address subpool, which reserves address space from a global pool (or global pools) for
        a particular site (and it's child sites). A subpool must be either an IPv4 or dual-stack pool, with
        `ipV4AddressSpace` and optionally `ipV6AddressSpace` properties specified. .

        Args:
            ipV4AddressSpace(object): Network Settings's ipV4AddressSpace.
            ipV6AddressSpace(object): Network Settings's ipV6AddressSpace.
            name(string): Network Settings's The name for this reserve IP pool. Only letters, numbers, '-' (hyphen),
                '_' (underscore), '.' (period), and '/' (forward slash) are allowed. .
            poolType(string): Network Settings's Once created, a subpool type cannot be changed.  LAN: Assigns IP
                addresses to LAN interfaces of applicable VNFs and underlay LAN automation.  Management:
                Assigns IP addresses to management interfaces. A management network is a dedicated
                network connected to VNFs for VNF management.  Service: Assigns IP addresses to service
                interfaces. Service networks are used for communication within VNFs.  WAN: Assigns IP
                addresses to NFVIS for UCS-E provisioning.  Generic: used for all other network types. .
                Available values are 'Generic', 'LAN', 'Management', 'Service' and 'WAN'.
            siteId(string): Network Settings's The `id` of the site that this subpool belongs to. This must be the
                `id` of a non-Global site. .
            siteName(string): Network Settings's The name of the site that this subpool belongs to. .
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
            https://developer.cisco.com/docs/dna-center/#!reservecreate-i-p-address-subpools
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
            "ipV4AddressSpace": ipV4AddressSpace,
            "ipV6AddressSpace": ipV6AddressSpace,
            "name": name,
            "poolType": poolType,
            "siteId": siteId,
            "siteName": siteName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_c7315d78a2ddda76b62777e8_v3_1_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/ipam/siteIpAddressPools"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_c7315d78a2ddda76b62777e8_v3_1_3_0", json_data)

    def retrieves_ip_address_subpools(
        self,
        limit=None,
        offset=None,
        order=None,
        site_id=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves IP address subpools, which reserve address space from a global pool (or global pools). .

        Args:
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page; the minimum is 1, and
                the maximum is 500. .
            sort_by(str): sortBy query parameter. A property within the response to sort by. .
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. .
            site_id(str): siteId query parameter. The `id` of the site for which to retrieve IP address subpools.
                Only subpools whose `siteId` exactly matches will be fetched, parent or child site
                matches will not be included. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-i-p-address-subpools
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(site_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
            "siteId": site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/ipam/siteIpAddressPools"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ebda74d4458fc9d197089571726d5_v3_1_3_0", json_data
        )

    def counts_ip_address_subpools(
        self, site_id=None, headers=None, **request_parameters
    ):
        """Counts IP address subpools, which reserve address space from a global pool (or global pools). .

        Args:
            site_id(str): siteId query parameter. The `id` of the site for which to retrieve IP address subpools.
                Only subpools whose `siteId` matches will be counted. .
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
            https://developer.cisco.com/docs/dna-center/#!counts-i-p-address-subpools
        """
        check_type(headers, dict)
        check_type(site_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/ipam/siteIpAddressPools/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e192825119d5baaa2edd636e7c4d12d_v3_1_3_0", json_data
        )

    def release_an_ip_address_subpool(self, id, headers=None, **request_parameters):
        """Releases an IP address subpool. **Release** completely removes the subpool from the site, and from all child
        sites, and frees the address use from the global pool(s).  Subpools cannot be released when assigned
        addresses in use. .

        Args:
            id(str): id path parameter. The `id` of the IP address subpool to delete. .
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
            https://developer.cisco.com/docs/dna-center/#!release-an-i-p-address-subpool
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

        e_url = "/dna/intent/api/v1/ipam/siteIpAddressPools/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f3a0040b7a89523f8d95ff69fb620047_v3_1_3_0", json_data
        )

    def updates_an_ip_address_subpool(
        self,
        id,
        ipV4AddressSpace=None,
        ipV6AddressSpace=None,
        name=None,
        poolType=None,
        siteId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates an IP address subpool, which reserves address space from a global pool (or global pools) for a
        particular site. Restrictions on updating an IP address subpool: The `poolType` cannot be changed. The
        `siteId` cannot be changed. The `ipV4AddressSpace` may not be removed. The `globalPoolId`, `subnet`, and
        `prefixLength` cannot be changed once it's already been set. However you may edit a subpool to add an IP
        address space if it does not already have one. .

        Args:
            ipV4AddressSpace(object): Network Settings's ipV4AddressSpace.
            ipV6AddressSpace(object): Network Settings's ipV6AddressSpace.
            name(string): Network Settings's The name for this reserve IP pool. Only letters, numbers, '-' (hyphen),
                '_' (underscore), '.' (period), and '/' (forward slash) are allowed. .
            poolType(string): Network Settings's Once created, a subpool type cannot be changed.  LAN: Assigns IP
                addresses to LAN interfaces of applicable VNFs and underlay LAN automation.  Management:
                Assigns IP addresses to management interfaces. A management network is a dedicated
                network connected to VNFs for VNF management.  Service: Assigns IP addresses to service
                interfaces. Service networks are used for communication within VNFs.  WAN: Assigns IP
                addresses to NFVIS for UCS-E provisioning.  Generic: used for all other network types. .
                Available values are 'Generic', 'LAN', 'Management', 'Service' and 'WAN'.
            siteId(string): Network Settings's The `id` of the site that this subpool belongs to. This must be the
                `id` of a non-Global site. .
            id(str): id path parameter. The `id` of the IP address subpool to update. .
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
            https://developer.cisco.com/docs/dna-center/#!updates-an-i-p-address-subpool
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
            "ipV4AddressSpace": ipV4AddressSpace,
            "ipV6AddressSpace": ipV6AddressSpace,
            "name": name,
            "poolType": poolType,
            "siteId": siteId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e328f7d015535897877f3ecb0c927453_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/ipam/siteIpAddressPools/{id}"
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
            "bpm_e328f7d015535897877f3ecb0c927453_v3_1_3_0", json_data
        )

    def retrieves_an_ip_address_subpool(self, id, headers=None, **request_parameters):
        """Retrieves an IP address subpool, which reserves address space from a global pool (or global pools) for a
        particular site. .

        Args:
            id(str): id path parameter. The `id` of the IP address subpool to retrieve. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-an-i-p-address-subpool
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

        e_url = "/dna/intent/api/v1/ipam/siteIpAddressPools/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f88725b8419857269dcb0d735af3e828_v3_1_3_0", json_data
        )

    def get_network(self, site_id=None, headers=None, **request_parameters):
        """API to get  DHCP and DNS center server details. .

        Args:
            site_id(str): siteId query parameter. Site id to get the network settings associated with the site. .
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
            https://developer.cisco.com/docs/dna-center/#!get-network
        """
        check_type(headers, dict)
        check_type(site_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b199c175281977a7e9e6bd9255b_v3_1_3_0", json_data
        )

    def create_network(
        self,
        site_id,
        settings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to create a network for DHCP,  Syslog, SNMP, NTP, Network AAA, Client and EndPoint AAA, and/or DNS center
        server settings. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-network
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "__persistbapioutput" in headers:
                check_type(headers.get("__persistbapioutput"), bool)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }
        _payload = {
            "settings": settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_eca62ef076b5627a85b2a5959613fb8_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network/{siteId}"
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
            "bpm_eca62ef076b5627a85b2a5959613fb8_v3_1_3_0", json_data
        )

    def update_network(
        self,
        site_id,
        settings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to update network settings for DHCP,  Syslog, SNMP, NTP, Network AAA, Client and EndPoint AAA, and/or DNS
        server settings. .

        Args:
            settings(object): Network Settings's settings.
            site_id(str): siteId path parameter. Site id to update the network settings which is associated with the
                site .
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
            https://developer.cisco.com/docs/dna-center/#!update-network
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
            "settings": settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e1b8c435195d56368c24a54dcce007d0_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network/{siteId}"
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
            "bpm_e1b8c435195d56368c24a54dcce007d0_v3_1_3_0", json_data
        )

    def retrieve_cli_templates_attached_to_a_network_profile(
        self, profile_id, headers=None, **request_parameters
    ):
        """Retrieves a list of CLI templates attached to a network profile based on the network profile ID. .

        Args:
            profile_id(str): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-c-l-i-templates-attached-to-a-network-profile
        """
        check_type(headers, dict)
        check_type(profile_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "profileId": profile_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkProfilesForSites/{profileId}/t" + "emplates"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d743268b5b5705a00e002a4484b003_v3_1_3_0", json_data
        )

    def retrieve_count_of_cli_templates_attached_to_a_network_profile(
        self, profile_id, headers=None, **request_parameters
    ):
        """Retrieves the count of all CLI templates attached to a network profile by the profile ID. .

        Args:
            profile_id(str): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-count-of-c-l-i-templates-attached-to-a-network-profile
        """
        check_type(headers, dict)
        check_type(profile_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "profileId": profile_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/networkProfilesForSites/{profileId}/t"
            + "emplates/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b8047373040656b29dc1306cad58366b_v3_1_3_0", json_data
        )

    def get_reserve_ip_subpool(
        self,
        group_name=None,
        ignore_inherited_groups=None,
        limit=None,
        offset=None,
        pool_usage=None,
        site_id=None,
        headers=None,
        **request_parameters
    ):
        """API to get the ip subpool info. .

        Args:
            site_id(str): siteId query parameter. site id of site from which to retrieve associated reserve pools.
                Either siteId (per site queries) or ignoreInheritedGroups must be used. They can also be
                used together. .
            offset(int): offset query parameter. offset/starting row. Indexed from 1. .
            limit(int): limit query parameter. Number of reserve pools to be retrieved. Default is 25 if not
                specified. Maximum allowed limit is 500. .
            ignore_inherited_groups(bool): ignoreInheritedGroups query parameter. Ignores pools inherited from
                parent site. Either siteId or ignoreInheritedGroups must be passed. They can also be
                used together. .
            pool_usage(str): poolUsage query parameter. Can take values empty, partially-full or empty-partially-
                full .
            group_name(str): groupName query parameter. Name of the group .
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
            https://developer.cisco.com/docs/dna-center/#!get-reserve-i-p-subpool
        """
        check_type(headers, dict)
        check_type(site_id, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(ignore_inherited_groups, bool)
        check_type(pool_usage, str)
        check_type(group_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
            "offset": offset,
            "limit": limit,
            "ignoreInheritedGroups": ignore_inherited_groups,
            "poolUsage": pool_usage,
            "groupName": group_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/reserve-ip-subpool"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d84253559e9d3e81881a4bd2fc_v3_1_3_0", json_data
        )

    def release_reserve_ip_subpool(self, id, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!release-reserve-i-p-subpool
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

        e_url = "/dna/intent/api/v1/reserve-ip-subpool/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eabbb425255a57578e9db00cda1f303a_v3_1_3_0", json_data
        )

    def reserve_ip_subpool(
        self,
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
        **request_parameters
    ):
        """API to reserve an ip subpool from the global pool .

        Args:
            ipv4DhcpServers(list): Network Settings's IPv4 input for dhcp server ip example: ["1.1.1.1"]  (list of
                strings).
            ipv4DnsServers(list): Network Settings's IPv4 input for dns server ip example: ["4.4.4.4"]  (list of
                strings).
            ipv4GateWay(string): Network Settings's Gateway ip address details, example: 175.175.0.1 .
            ipv4GlobalPool(string): Network Settings's IP v4 Global pool address with cidr, example: 175.175.0.0/16
                .
            ipv4Prefix(boolean): Network Settings's IPv4 prefix value is true, the ip4 prefix length input field is
                enabled , if it is false ipv4 total Host input is enable .
            ipv4PrefixLength(integer): Network Settings's The ipv4 prefix length is required when ipv4prefix value
                is true. .
            ipv4Subnet(string): Network Settings's IPv4 Subnet address, example: 175.175.0.0. Either ipv4Subnet or
                ipv4TotalHost needs to be passed if creating IPv4 subpool. .
            ipv4TotalHost(integer): Network Settings's IPv4 total host is required when ipv4prefix value is false. .
            ipv6AddressSpace(boolean): Network Settings's If the value is omitted or false only ipv4 input are
                required, otherwise both ipv6 and ipv4 are required .
            ipv6DhcpServers(list): Network Settings's IPv6 format dhcp server as input example : ["2001:db8::1234"]
                (list of strings).
            ipv6DnsServers(list): Network Settings's IPv6 format dns server input example: ["2001:db8::1234"]  (list
                of strings).
            ipv6GateWay(string): Network Settings's Gateway ip address details, example: 2001:db8:85a3:0:100::1 .
            ipv6GlobalPool(string): Network Settings's IPv6 Global pool address with cidr this is required when
                Ipv6AddressSpace value is true, example: 2001:db8:85a3::/64 .
            ipv6Prefix(boolean): Network Settings's Ipv6 prefix value is true, the ip6 prefix length input field is
                enabled , if it is false ipv6 total Host input is enable .
            ipv6PrefixLength(integer): Network Settings's IPv6 prefix length is required when the ipv6prefix value
                is true .
            ipv6Subnet(string): Network Settings's IPv6 Subnet address, example :2001:db8:85a3:0:100::. Either
                ipv6Subnet or ipv6TotalHost needs to be passed if creating IPv6 subpool. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!reserve-i-p-subpool
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
            "name": name,
            "type": type,
            "ipv6AddressSpace": ipv6AddressSpace,
            "ipv4GlobalPool": ipv4GlobalPool,
            "ipv4Prefix": ipv4Prefix,
            "ipv4PrefixLength": ipv4PrefixLength,
            "ipv4Subnet": ipv4Subnet,
            "ipv4GateWay": ipv4GateWay,
            "ipv4DhcpServers": ipv4DhcpServers,
            "ipv4DnsServers": ipv4DnsServers,
            "ipv6GlobalPool": ipv6GlobalPool,
            "ipv6Prefix": ipv6Prefix,
            "ipv6PrefixLength": ipv6PrefixLength,
            "ipv6Subnet": ipv6Subnet,
            "ipv6GateWay": ipv6GateWay,
            "ipv6DhcpServers": ipv6DhcpServers,
            "ipv6DnsServers": ipv6DnsServers,
            "ipv4TotalHost": ipv4TotalHost,
            "ipv6TotalHost": ipv6TotalHost,
            "slaacSupport": slaacSupport,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_cec6c85d9bb4bcc8f61f31296b_v3_1_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/reserve-ip-subpool/{siteId}"
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
            "bpm_cec6c85d9bb4bcc8f61f31296b_v3_1_3_0", json_data
        )

    def update_reserve_ip_subpool(
        self,
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
        **request_parameters
    ):
        """API to update ip subpool from the global pool .

        Args:
            ipv4DhcpServers(list): Network Settings's IPv4 input for dhcp server ip example: ["1.1.1.1"]  (list of
                strings).
            ipv4DnsServers(list): Network Settings's IPv4 input for dns server ip  example: ["4.4.4.4"]  (list of
                strings).
            ipv4GateWay(string): Network Settings's Gateway ip address details, example: 175.175.0.1 .
            ipv6AddressSpace(boolean): Network Settings's If the value is false only ipv4 input are required. NOTE
                if value is false then any existing ipv6 subpool in the group will be removed. .
            ipv6DhcpServers(list): Network Settings's IPv6 format dhcp server as input example : ["2001:db8::1234"]
                (list of strings).
            ipv6DnsServers(list): Network Settings's IPv6 format dns server input example: ["2001:db8::1234"]  (list
                of strings).
            ipv6GateWay(string): Network Settings's Gateway ip address details, example: 2001:db8:85a3:0:100::1 .
            ipv6GlobalPool(string): Network Settings's IPv6 Global pool address with cidr this is required when
                Ipv6AddressSpace value is true, example: 2001:db8:85a3::/64 .
            ipv6Prefix(boolean): Network Settings's Ipv6 prefix value is true, the ip6 prefix length input field is
                enabled, if it is false ipv6 total Host input is enable .
            ipv6PrefixLength(integer): Network Settings's IPv6 prefix length is required when the ipv6prefix value
                is true .
            ipv6Subnet(string): Network Settings's IPv6 Subnet address, example :2001:db8:85a3:0:100::. .
            ipv6TotalHost(integer): Network Settings's Size of pool in terms of number of IPs. IPv6 total host is
                required when ipv6prefix value is false. .
            name(string): Network Settings's Name of the reserve ip sub pool .
            slaacSupport(boolean): Network Settings's Slaac Support.
            site_id(str): siteId path parameter. Site id of site to update sub pool. .
            id(str): id query parameter. Id of subpool group .
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
            https://developer.cisco.com/docs/dna-center/#!update-reserve-i-p-subpool
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }
        _payload = {
            "name": name,
            "ipv6AddressSpace": ipv6AddressSpace,
            "ipv4DhcpServers": ipv4DhcpServers,
            "ipv4DnsServers": ipv4DnsServers,
            "ipv6GlobalPool": ipv6GlobalPool,
            "ipv6Prefix": ipv6Prefix,
            "ipv6PrefixLength": ipv6PrefixLength,
            "ipv6Subnet": ipv6Subnet,
            "ipv6TotalHost": ipv6TotalHost,
            "ipv6GateWay": ipv6GateWay,
            "ipv6DhcpServers": ipv6DhcpServers,
            "ipv6DnsServers": ipv6DnsServers,
            "slaacSupport": slaacSupport,
            "ipv4GateWay": ipv4GateWay,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fd6083b0c65d03b2d53f10b3ece59d_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/reserve-ip-subpool/{siteId}"
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
            "bpm_fd6083b0c65d03b2d53f10b3ece59d_v3_1_3_0", json_data
        )

    def get_service_provider_details(self, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-service-provider-details
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

        e_url = "/dna/intent/api/v1/service-provider"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dda850a0675b888048adf8d488aec1_v3_1_3_0", json_data
        )

    def create_sp_profile(
        self,
        settings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to create Service Provider Profile(QOS). .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-s-p-profile
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
            "settings": settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ffa347eb411567a9c793696795250a5_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/service-provider"
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
            "bpm_ffa347eb411567a9c793696795250a5_v3_1_3_0", json_data
        )

    def update_sp_profile(
        self,
        settings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to update Service Provider Profile (QoS). .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-s-p-profile
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
            "settings": settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e22c99a82f5764828810acb45e7a9e_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/service-provider"
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
            "bpm_e22c99a82f5764828810acb45e7a9e_v3_1_3_0", json_data
        )

    def sync_network_devices_credential(
        self,
        deviceCredentialId=None,
        siteId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """When sync is triggered at a site with the credential that are associated to the same site, network devices in
        impacted sites (child sites which are inheriting the credential) get managed in inventory with the
        associated site credential. Credential gets configured on network devices before these get managed in
        inventory. Please make a note that cli credential wouldn't be configured on AAA authenticated devices
        but they just get managed with the associated site cli credential. .

        Args:
            deviceCredentialId(string): Network Settings's It must be cli/snmpV2Read/snmpV2Write/snmpV3 Id. .
            siteId(string): Network Settings's Site Id. .
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
            https://developer.cisco.com/docs/dna-center/#!sync-network-devices-credential
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
            "deviceCredentialId": deviceCredentialId,
            "siteId": siteId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e73b352ff2573aab906c2ad75c5a71_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/deviceCredentials/apply"
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
            "bpm_e73b352ff2573aab906c2ad75c5a71_v3_1_3_0", json_data
        )

    def set_aaa_settings_for_a_site(
        self,
        id,
        aaaClient=None,
        aaaNetwork=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Set AAA settings for a site; `null` values indicate that the settings will be inherited from the parent site;
        empty objects (`{}`) indicate that the settings is unset. .

        Args:
            aaaClient(object): Network Settings's aaaClient.
            aaaNetwork(object): Network Settings's aaaNetwork.
            id(str): id path parameter. Site Id .
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
            https://developer.cisco.com/docs/dna-center/#!set-a-a-a-settings-for-a-site
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
            "aaaNetwork": aaaNetwork,
            "aaaClient": aaaClient,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_cd2e825a78b6de087e991f6fe0_v3_1_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{id}/aaaSettings"
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
            "bpm_cd2e825a78b6de087e991f6fe0_v3_1_3_0", json_data
        )

    def retrieve_aaa_settings_for_a_site(
        self, id, inherited=None, headers=None, **request_parameters
    ):
        """Retrieve AAA settings for a site; `null` values indicate that the setting will be inherited from the parent
        site; empty objects (`{}`) indicate that the setting is unset at a site. .

        Args:
            id(str): id path parameter. Site Id .
            inherited(bool): _inherited query parameter. Include settings explicitly set for this site and settings
                inherited from sites higher in the site hierarchy; when `false`, `null` values indicate
                that the site inherits that setting from the parent site or a site higher in the site
                hierarchy. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-a-a-settings-for-a-site
        """
        check_type(headers, dict)
        check_type(inherited, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "_inherited": inherited,
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

        e_url = "/dna/intent/api/v1/sites/{id}/aaaSettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c13899171d45b4f828423c6feaa1e46_v3_1_3_0", json_data
        )

    def retrieve_banner_settings_for_a_site(
        self, id, inherited=None, headers=None, **request_parameters
    ):
        """Retrieve banner settings for a site; `null` values indicate that the setting will be inherited from the parent
        site; empty objects (`{}`) indicate that the setting is unset at a site. .

        Args:
            id(str): id path parameter. Site Id .
            inherited(bool): _inherited query parameter. Include settings explicitly set for this site and settings
                inherited from sites higher in the site hierarchy; when `false`, `null` values indicate
                that the site inherits that setting from the parent site or a site higher in the site
                hierarchy. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-banner-settings-for-a-site
        """
        check_type(headers, dict)
        check_type(inherited, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "_inherited": inherited,
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

        e_url = "/dna/intent/api/v1/sites/{id}/bannerSettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b29d90ce0125ad898bc06bbceb07403_v3_1_3_0", json_data
        )

    def set_banner_settings_for_a_site(
        self,
        id,
        banner=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Set banner settings for a site; `null` values indicate that the setting will be inherited from the parent site;
        empty objects (`{}`) indicate that the settings is unset. .

        Args:
            banner(object): Network Settings's banner.
            id(str): id path parameter. Site Id .
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
            https://developer.cisco.com/docs/dna-center/#!set-banner-settings-for-a-site
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
            "banner": banner,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b3c4383ecc13514c85c6f3d8484f6d68_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{id}/bannerSettings"
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
            "bpm_b3c4383ecc13514c85c6f3d8484f6d68_v3_1_3_0", json_data
        )

    def get_device_credential_settings_for_a_site(
        self, id, inherited=None, headers=None, **request_parameters
    ):
        """Gets device credential settings for a site; `null` values indicate that the setting will be inherited from the
        parent site; empty objects (`{}`) indicate that the credential is unset, and that no credential of that
        type will be used for the site. .

        Args:
            id(str): id path parameter. Site Id, retrievable from the `id` attribute in `/dna/intent/api/v1/sites` .
            inherited(bool): _inherited query parameter. Include settings explicitly set for this site and settings
                inherited from sites higher in the site hierarchy; when `false`, `null` values indicate
                that the site inherits that setting from the parent site or a site higher in the site
                hierarchy. .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-credential-settings-for-a-site
        """
        check_type(headers, dict)
        check_type(inherited, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "_inherited": inherited,
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

        e_url = "/dna/intent/api/v1/sites/{id}/deviceCredentials"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e4e92f7adc845290b11168e59ab4c88b_v3_1_3_0", json_data
        )

    def update_device_credential_settings_for_a_site(
        self,
        id,
        cliCredentialsId=None,
        httpReadCredentialsId=None,
        httpWriteCredentialsId=None,
        snmpv2cReadCredentialsId=None,
        snmpv2cWriteCredentialsId=None,
        snmpv3CredentialsId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates device credential settings for a site; `null` values indicate that the setting will be inherited from
        the parent site; empty objects (`{}`) indicate that the credential is unset, and that no credential of
        that type will be used for the site. .

        Args:
            cliCredentialsId(object): Network Settings's cliCredentialsId.
            httpReadCredentialsId(object): Network Settings's httpReadCredentialsId.
            httpWriteCredentialsId(object): Network Settings's httpWriteCredentialsId.
            snmpv2cReadCredentialsId(object): Network Settings's snmpv2cReadCredentialsId.
            snmpv2cWriteCredentialsId(object): Network Settings's snmpv2cWriteCredentialsId.
            snmpv3CredentialsId(object): Network Settings's snmpv3CredentialsId.
            id(str): id path parameter. Site Id, retrievable from the `id` attribute in `/dna/intent/api/v1/sites` .
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
            https://developer.cisco.com/docs/dna-center/#!update-device-credential-settings-for-a-site
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
            "cliCredentialsId": cliCredentialsId,
            "snmpv2cReadCredentialsId": snmpv2cReadCredentialsId,
            "snmpv2cWriteCredentialsId": snmpv2cWriteCredentialsId,
            "snmpv3CredentialsId": snmpv3CredentialsId,
            "httpReadCredentialsId": httpReadCredentialsId,
            "httpWriteCredentialsId": httpWriteCredentialsId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e481654675355408be8daff9a82f9a0_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{id}/deviceCredentials"
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
            "bpm_e481654675355408be8daff9a82f9a0_v3_1_3_0", json_data
        )

    def get_network_devices_credentials_sync_status(
        self, id, headers=None, **request_parameters
    ):
        """Get network devices credentials sync status at a given site. .

        Args:
            id(str): id path parameter. Site Id. .
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
            https://developer.cisco.com/docs/dna-center/#!get-network-devices-credentials-sync-status
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

        e_url = "/dna/intent/api/v1/sites/{id}/deviceCredentials/status"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_be59a332e9e45f6991e96111743fd775_v3_1_3_0", json_data
        )

    def set_dhcp_settings_for_a_site(
        self,
        id,
        dhcp=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Set DHCP settings for a site; `null` values indicate that the setting will be inherited from the parent site;
        empty objects (`{}`) indicate that the settings is unset. .

        Args:
            dhcp(object): Network Settings's dhcp.
            id(str): id path parameter. Site Id .
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
            https://developer.cisco.com/docs/dna-center/#!set-dhcp-settings-for-a-site
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
            "dhcp": dhcp,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a15a2f83f975a6a9964e7da79a605de_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{id}/dhcpSettings"
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
            "bpm_a15a2f83f975a6a9964e7da79a605de_v3_1_3_0", json_data
        )

    def retrieve_d_h_c_p_settings_for_a_site(
        self, id, inherited=None, headers=None, **request_parameters
    ):
        """Retrieve DHCP settings for a site; `null` values indicate that the setting will be inherited from the parent
        site; empty objects (`{}`) indicate that the setting is unset at a site. .

        Args:
            id(str): id path parameter. Site Id .
            inherited(bool): _inherited query parameter. Include settings explicitly set for this site and settings
                inherited from sites higher in the site hierarchy; when `false`, `null` values indicate
                that the site inherits that setting from the parent site or a site higher in the site
                hierarchy. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-d-h-c-p-settings-for-a-site
        """
        check_type(headers, dict)
        check_type(inherited, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "_inherited": inherited,
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

        e_url = "/dna/intent/api/v1/sites/{id}/dhcpSettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe723d00fce5700b8abe2a43b82f035_v3_1_3_0", json_data
        )

    def retrieve_d_n_s_settings_for_a_site(
        self, id, inherited=None, headers=None, **request_parameters
    ):
        """Retrieve DNS settings for a site; `null` values indicate that the setting will be inherited from the parent
        site; empty objects (`{}`) indicate that the setting is unset at a site. .

        Args:
            id(str): id path parameter. Site Id .
            inherited(bool): _inherited query parameter. Include settings explicitly set for this site and settings
                inherited from sites higher in the site hierarchy; when `false`, `null` values indicate
                that the site inherits that setting from the parent site or a site higher in the site
                hierarchy. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-d-n-s-settings-for-a-site
        """
        check_type(headers, dict)
        check_type(inherited, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "_inherited": inherited,
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

        e_url = "/dna/intent/api/v1/sites/{id}/dnsSettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f32e172f454564ba92d7a410c63c164_v3_1_3_0", json_data
        )

    def set_d_n_s_settings_for_a_site(
        self,
        id,
        dns=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Set DNS settings for a site; `null` values indicate that the setting will be inherited from the parent site;
        empty objects (`{}`) indicate that the settings is unset. .

        Args:
            dns(object): Network Settings's dns.
            id(str): id path parameter. Site Id .
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
            https://developer.cisco.com/docs/dna-center/#!set-d-n-s-settings-for-a-site
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
            "dns": dns,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_eb3b18894545315b25b94d0c0e2ec67_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{id}/dnsSettings"
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
            "bpm_eb3b18894545315b25b94d0c0e2ec67_v3_1_3_0", json_data
        )

    def set_image_distribution_settings_for_a_site(
        self,
        id,
        imageDistribution=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Set image distribution settings for a site; `null` values indicate that the setting will be inherited from the
        parent site; empty objects (`{}`) indicate that the settings is unset. .

        Args:
            imageDistribution(object): Network Settings's imageDistribution.
            id(str): id path parameter. Site Id .
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
            https://developer.cisco.com/docs/dna-center/#!set-image-distribution-settings-for-a-site
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
            "imageDistribution": imageDistribution,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d02614492a2251c18de2e36c097e40ff_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{id}/imageDistributionSettings"
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
            "bpm_d02614492a2251c18de2e36c097e40ff_v3_1_3_0", json_data
        )

    def retrieve_image_distribution_settings_for_a_site(
        self, id, inherited=None, headers=None, **request_parameters
    ):
        """Retrieve image distribution settings for a site; `null` values indicate that the setting will be inherited from
        the parent site; empty objects (`{}`) indicate that the setting is unset at a site. .

        Args:
            id(str): id path parameter. Site Id .
            inherited(bool): _inherited query parameter. Include settings explicitly set for this site and settings
                inherited from sites higher in the site hierarchy; when `false`, `null` values indicate
                that the site inherits that setting from the parent site or a site higher in the site
                hierarchy. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-image-distribution-settings-for-a-site
        """
        check_type(headers, dict)
        check_type(inherited, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "_inherited": inherited,
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

        e_url = "/dna/intent/api/v1/sites/{id}/imageDistributionSettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d0c5259b59bd5751994e2aa77a15f70e_v3_1_3_0", json_data
        )

    def set_n_t_p_settings_for_a_site(
        self,
        id,
        ntp=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Set NTP settings for a site; `null` values indicate that the setting will be inherited from the parent site;
        empty objects (`{}`) indicate that the settings is unset. .

        Args:
            ntp(object): Network Settings's ntp.
            id(str): id path parameter. Site Id .
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
            https://developer.cisco.com/docs/dna-center/#!set-n-t-p-settings-for-a-site
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
            "ntp": ntp,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_df9ec5aa58815a849b4853b223343e5e_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{id}/ntpSettings"
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
            "bpm_df9ec5aa58815a849b4853b223343e5e_v3_1_3_0", json_data
        )

    def retrieve_n_t_p_settings_for_a_site(
        self, id, inherited=None, headers=None, **request_parameters
    ):
        """Retrieve NTP settings for a site; `null` values indicate that the setting will be inherited from the parent
        site; empty objects (`{}`) indicate that the setting is unset at a site. .

        Args:
            id(str): id path parameter. Site Id .
            inherited(bool): _inherited query parameter. Include settings explicitly set for this site and settings
                inherited from sites higher in the site hierarchy; when `false`, `null` values indicate
                that the site inherits that setting from the parent site or a site higher in the site
                hierarchy. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-n-t-p-settings-for-a-site
        """
        check_type(headers, dict)
        check_type(inherited, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "_inherited": inherited,
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

        e_url = "/dna/intent/api/v1/sites/{id}/ntpSettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c49b666d3a305b509d0d3b356e912ab4_v3_1_3_0", json_data
        )

    def retrieve_telemetry_settings_for_a_site(
        self, id, inherited=None, headers=None, **request_parameters
    ):
        """Retrieves telemetry settings for the given site. `null` values indicate that the setting will be inherited from
        the parent site. .

        Args:
            id(str): id path parameter. Site Id, retrievable from the `id` attribute in `/dna/intent/api/v1/sites` .
            inherited(bool): _inherited query parameter. Include settings explicitly set for this site and settings
                inherited from sites higher in the site hierarchy; when `false`, `null` values indicate
                that the site inherits that setting from the parent site or a site higher in the site
                hierarchy. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-telemetry-settings-for-a-site
        """
        check_type(headers, dict)
        check_type(inherited, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "_inherited": inherited,
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

        e_url = "/dna/intent/api/v1/sites/{id}/telemetrySettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af4b3c5d1dc6505cadd13bf41c894700_v3_1_3_0", json_data
        )

    def set_telemetry_settings_for_a_site(
        self,
        id,
        applicationVisibility=None,
        snmpTraps=None,
        syslogs=None,
        wiredDataCollection=None,
        wirelessTelemetry=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Sets telemetry settings for the given site; `null` values indicate that the setting will be inherited from the
        parent site. .

        Args:
            applicationVisibility(object): Network Settings's applicationVisibility.
            snmpTraps(object): Network Settings's snmpTraps.
            syslogs(object): Network Settings's syslogs.
            wiredDataCollection(object): Network Settings's wiredDataCollection.
            wirelessTelemetry(object): Network Settings's wirelessTelemetry.
            id(str): id path parameter. Site Id, retrievable from the `id` attribute in `/dna/intent/api/v1/sites` .
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
            https://developer.cisco.com/docs/dna-center/#!set-telemetry-settings-for-a-site
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
            "wiredDataCollection": wiredDataCollection,
            "wirelessTelemetry": wirelessTelemetry,
            "snmpTraps": snmpTraps,
            "syslogs": syslogs,
            "applicationVisibility": applicationVisibility,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bac0c488707959c182dfef18681bceda_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{id}/telemetrySettings"
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
            "bpm_bac0c488707959c182dfef18681bceda_v3_1_3_0", json_data
        )

    def set_time_zone_for_a_site(
        self,
        id,
        timeZone=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Set time zone settings for a site; `null` values indicate that the setting will be inherited from the parent
        site; empty objects (`{}`) indicate that the settings is unset. .

        Args:
            timeZone(object): Network Settings's timeZone.
            id(str): id path parameter. Site Id .
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
            https://developer.cisco.com/docs/dna-center/#!set-time-zone-for-a-site
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
            "timeZone": timeZone,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c17432d928f755f8bb9f4edb83089d3e_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{id}/timeZoneSettings"
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
            "bpm_c17432d928f755f8bb9f4edb83089d3e_v3_1_3_0", json_data
        )

    def retrieve_time_zone_settings_for_a_site(
        self, id, inherited=None, headers=None, **request_parameters
    ):
        """Retrieve time zone settings for a site; `null` values indicate that the setting will be inherited from the
        parent site; empty objects (`{}`) indicate that the setting is unset at a site. .

        Args:
            id(str): id path parameter. Site Id .
            inherited(bool): _inherited query parameter. Include settings explicitly set for this site and settings
                inherited from sites higher in the site hierarchy; when `false`, `null` values indicate
                that the site inherits that setting from the parent site or a site higher in the site
                hierarchy. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-time-zone-settings-for-a-site
        """
        check_type(headers, dict)
        check_type(inherited, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "_inherited": inherited,
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

        e_url = "/dna/intent/api/v1/sites/{id}/timeZoneSettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a03efc6bba51eeabcde938f0856074_v3_1_3_0", json_data
        )

    def delete_sp_profile(self, sp_profile_name, headers=None, **request_parameters):
        """API to delete Service Provider Profile (QoS). .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-s-p-profile
        """
        check_type(headers, dict)
        check_type(sp_profile_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "spProfileName": sp_profile_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sp-profile/{spProfileName}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a1d68f15e02adc37239b3fcbbb6_v3_1_3_0", json_data
        )

    def update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site(
        self,
        deviceIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update a device(s) telemetry settings to conform to the telemetry settings for its site.  One Task is created to
        track the update, for more granular status tracking, split your devices into multiple requests. .

        Args:
            deviceIds(list): Network Settings's The list of device Ids to perform the provisioning against  (list of
                strings).
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
            https://developer.cisco.com/docs/dna-center/#!update-a-devices-telemetry-settings-to-conform-to-the-telemetry-settings-for-its-site
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
            "deviceIds": deviceIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_de1b75d59b083df0ece12259ecd_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/telemetrySettings/apply"
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
            "bpm_de1b75d59b083df0ece12259ecd_v3_1_3_0", json_data
        )

    def assign_device_credential_to_site_v2(
        self,
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
        **request_parameters
    ):
        """API to assign Device Credential to a site. .

        Args:
            cliId(string): Network Settings's CLI Credential Id .
            httpRead(string): Network Settings's HTTP(S) Read Credential Id .
            httpWrite(string): Network Settings's HTTP(S) Write Credential Id .
            snmpV2ReadId(string): Network Settings's SNMPv2c Read Credential Id .
            snmpV2WriteId(string): Network Settings's SNMPv2c Write Credential Id .
            snmpV3Id(string): Network Settings's SNMPv3 Credential Id .
            site_id(str): siteId path parameter. Site Id to assign credential. .
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
            https://developer.cisco.com/docs/dna-center/#!assign-device-credential-to-site-v2
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
            "cliId": cliId,
            "snmpV2ReadId": snmpV2ReadId,
            "snmpV2WriteId": snmpV2WriteId,
            "snmpV3Id": snmpV3Id,
            "httpRead": httpRead,
            "httpWrite": httpWrite,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a3954b27e5eeb82789ed231e0557f_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/credential-to-site/{siteId}"
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
            "bpm_a3954b27e5eeb82789ed231e0557f_v3_1_3_0", json_data
        )

    def get_network_v2(self, site_id, headers=None, **request_parameters):
        """API to get SNMP, NTP, Network AAA, Client and Endpoint AAA, and/or DNS center server settings. .

        Args:
            site_id(str): siteId query parameter. Site Id to get the network settings associated with the site. .
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
            https://developer.cisco.com/docs/dna-center/#!get-network-v2
        """
        check_type(headers, dict)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/network"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d0b7bffe821755dab4e2a2df8ea79404_v3_1_3_0", json_data
        )

    def create_network_v2(
        self,
        site_id,
        settings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to create network settings for DHCP,  Syslog, SNMP, NTP, Network AAA, Client and Endpoint AAA, and/or DNS
        center server settings. .

        Args:
            settings(object): Network Settings's settings.
            site_id(str): siteId path parameter. Site Id to which site details to associate with the network
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-network-v2
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
            "settings": settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c5f97865727857d5b1eeaedee3dcccd2_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/network/{siteId}"
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
            "bpm_c5f97865727857d5b1eeaedee3dcccd2_v3_1_3_0", json_data
        )

    def update_network_v2(
        self,
        site_id,
        settings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to update network settings for DHCP, Syslog, SNMP, NTP, Network AAA, Client and Endpoint AAA, and/or DNS
        center server settings. .

        Args:
            settings(object): Network Settings's settings.
            site_id(str): siteId path parameter. Site Id to update the network settings which is associated with the
                site .
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
            https://developer.cisco.com/docs/dna-center/#!update-network-v2
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
            "settings": settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a7935eedd53a5b8c84668c903cc1c705_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/network/{siteId}"
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
            "bpm_a7935eedd53a5b8c84668c903cc1c705_v3_1_3_0", json_data
        )

    def create_sp_profile_v2(
        self,
        settings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to create Service Provider Profile(QOS). .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-s-p-profile-v2
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
            "settings": settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a66db26df529597c84c2a15ea2d632ce_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/service-provider"
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
            "bpm_a66db26df529597c84c2a15ea2d632ce_v3_1_3_0", json_data
        )

    def update_sp_profile_v2(
        self,
        settings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to update Service Provider Profile (QoS). .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-s-p-profile-v2
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
            "settings": settings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_e0b654c39dc6e19cd6f5194d_v3_1_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/service-provider"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_e0b654c39dc6e19cd6f5194d_v3_1_3_0", json_data)

    def get_service_provider_details_v2(self, headers=None, **request_parameters):
        """API to get Service Provider details (QoS). .

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
            https://developer.cisco.com/docs/dna-center/#!get-service-provider-details-v2
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

        e_url = "/dna/intent/api/v2/service-provider"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f01025635a52bdfdac7226911b31_v3_1_3_0", json_data
        )

    def delete_sp_profile_v2(self, sp_profile_name, headers=None, **request_parameters):
        """API to delete Service Provider Profile (QoS). .

        Args:
            sp_profile_name(str): spProfileName path parameter. SP profile name .
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
            https://developer.cisco.com/docs/dna-center/#!delete-s-p-profile-v2
        """
        check_type(headers, dict)
        check_type(sp_profile_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "spProfileName": sp_profile_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/sp-profile/{spProfileName}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a9bbbce953615baeb0a324c61753139d_v3_1_3_0", json_data
        )


# Alias Functions

# -*- coding: utf-8 -*-
"""Cisco DNA Center Site Design API wrapper.

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


class SiteDesign(object):
    """Cisco DNA Center Site Design API (version: 2.3.7.6).

    Wraps the DNA Center Site Design
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SiteDesign
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SiteDesign, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def creates_an_area_v1(
        self,
        name=None,
        parentId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates an area in the network hierarchy. .

        Args:
            name(string): Site Design's Area name .
            parentId(string): Site Design's Parent Id .
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
            https://developer.cisco.com/docs/dna-center/#!creates-an-area
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
            "name": name,
            "parentId": parentId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f6a4086c00f45dc5a634f0b8db5cdfd3_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/areas"
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
            "bpm_f6a4086c00f45dc5a634f0b8db5cdfd3_v2_3_7_6", json_data
        )

    def updates_an_area_v1(
        self,
        id,
        name=None,
        parentId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates an area in the network hierarchy. .

        Args:
            name(string): Site Design's Area name .
            parentId(string): Site Design's Parent Id .
            id(str): id path parameter. Area Id .
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
            https://developer.cisco.com/docs/dna-center/#!updates-an-area
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
            "name": name,
            "parentId": parentId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f50f8c552f5d2eb68d715e1318976e_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/areas/{id}"
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
            "bpm_f50f8c552f5d2eb68d715e1318976e_v2_3_7_6", json_data
        )

    def deletes_an_area_v1(self, id, headers=None, **request_parameters):
        """Deletes an area in the network hierarchy. This operations fails if there are any child areas or buildings for
        this area. .

        Args:
            id(str): id path parameter. Area ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!deletes-an-area
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

        e_url = "/dna/intent/api/v1/areas/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e3604000c24755bd855c3124712ed10f_v2_3_7_6", json_data
        )

    def gets_an_area_v1(self, id, headers=None, **request_parameters):
        """Gets an area in the network hierarchy. .

        Args:
            id(str): id path parameter. Area Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!gets-an-area
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

        e_url = "/dna/intent/api/v1/areas/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d4479806c54eb89c4214f716731fc_v2_3_7_6", json_data
        )

    def assign_network_devices_to_a_site_v1(
        self,
        deviceIds=None,
        siteId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Assign unprovisioned network devices to a site. Along with that it can also be used to assign unprovisioned
        network devices to a different site. If device controllability is enabled, it will be triggered once
        device assigned to site successfully. Device Controllability can be enabled/disabled using
        `/dna/intent/api/v1/networkDevices/deviceControllability/settings`. .

        Args:
            deviceIds(list): Site Design's Unassigned network devices.  (list of strings).
            siteId(string): Site Design's This must be building Id or floor Id. Access points, Sensors are assigned
                to floor. Remaining network devices are assigned to building. Site Id can be retrieved
                using '/intent/api/v1/sites'. .
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
            https://developer.cisco.com/docs/dna-center/#!assign-network-devices-to-a-site
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
            "siteId": siteId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c279ba052250d883ef87775a415089_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/assignToSite/apply"
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
            "bpm_c279ba052250d883ef87775a415089_v2_3_7_6", json_data
        )

    def get_site_assigned_network_devices_v1(
        self, site_id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Get all site assigned network devices. The items in the list are arranged in an order that corresponds with
        their internal identifiers. .

        Args:
            site_id(str): siteId query parameter. Site Id. It must be area Id or building Id or floor Id. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!get-site-assigned-network-devices
        """
        check_type(headers, dict)
        check_type(site_id, str, may_be_none=False)
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

        e_url = "/dna/intent/api/v1/networkDevices/assignedToSite"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c8f7e2eddc752739209482b6386e2d5_v2_3_7_6", json_data
        )

    def get_site_assigned_network_devices_count_v1(
        self, site_id, headers=None, **request_parameters
    ):
        """Get all network devices count under the given site in the network hierarchy. .

        Args:
            site_id(str): siteId query parameter. Site Id. It must be area Id or building Id or floor Id. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!get-site-assigned-network-devices-count
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

        e_url = "/dna/intent/api/v1/networkDevices/assignedToSite/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ac24397435521da0a2feaf8af96162_v2_3_7_6", json_data
        )

    def get_device_controllability_settings_v1(
        self, headers=None, **request_parameters
    ):
        """Device Controllability is a system-level process on DNA Center that enforces state synchronization for some
        device-layer features. Its purpose is to aid in the deployment of required network settings that
        DNA Center needs to manage devices. Changes are made on network devices during discovery, when
        adding a device to Inventory, or when assigning a device to a site. If changes are made to any settings
        that are under the scope of this process, these changes are applied to the network devices during the
        Provision and Update Telemetry Settings operations, even if Device Controllability is disabled. The
        following device settings will be enabled as part of Device Controllability when devices are discovered.
        SNMP Credentials. NETCONF Credentials. Subsequent to discovery, devices will be added to Inventory. The
        following device settings will be enabled when devices are added to inventory. Cisco TrustSec (CTS)
        Credentials. The following device settings will be enabled when devices are assigned to a site. Some of
        these settings can be defined at a site level under Design > Network Settings > Telemetry & Wireless.
        Wired Endpoint Data Collection Enablement. Controller Certificates. SNMP Trap Server Definitions. Syslog
        Server Definitions. Application Visibility. Application QoS Policy. Wireless Service Assurance (WSA).
        Wireless Telemetry. DTLS Ciphersuite. AP Impersonation. If Device Controllability is disabled, DNA
        Center does not configure any of the preceding credentials or settings on devices during discovery, at
        runtime, or during site assignment. However, the telemetry settings and related configuration are pushed
        when the device is provisioned or when the update Telemetry Settings action is performed. DNA
        Center identifies and automatically corrects the following telemetry configuration issues on the device.
        SWIM certificate issue. IOS WLC NA certificate issue. PKCS12 certificate issue. IOS telemetry
        configuration issu .

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
            https://developer.cisco.com/docs/dna-center/#!get-device-controllability-settings
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

        e_url = "/dna/intent/api/v1/networkDevices/deviceControllability/" + "settings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a9b27c573ea0530ce2858a1c1d_v2_3_7_6", json_data
        )

    def update_device_controllability_settings_v1(
        self,
        autocorrectTelemetryConfig=None,
        deviceControllability=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Device Controllability is a system-level process on DNA Center that enforces state synchronization for some
        device-layer features. Its purpose is to aid in the deployment of required network settings that
        DNA Center needs to manage devices. Changes are made on network devices  during discovery, when
        adding a device to Inventory, or when assigning a device to a site. If changes  are made to any settings
        that are under the scope of this process, these changes are applied to the  network devices during the
        Provision and Update Telemetry Settings operations, even if Device  Controllability is disabled. The
        following device settings will be enabled as part of  Device Controllability when devices are
        discovered.     SNMP Credentials.   NETCONF Credentials.    Subsequent to discovery, devices will be
        added to Inventory. The following device settings will be  enabled when devices are added to inventory.
        Cisco TrustSec (CTS) Credentials.    The following device settings will be enabled when devices are
        assigned to a site. Some of these  settings can be defined at a site level under Design > Network
        Settings > Telemetry & Wireless.    Wired Endpoint Data Collection Enablement.   Controller
        Certificates.   SNMP Trap Server Definitions.   Syslog Server Definitions.   Application Visibility.
        Application QoS Policy.   Wireless Service Assurance (WSA).   Wireless Telemetry.   DTLS Ciphersuite.
        AP Impersonation.    If Device Controllability is disabled, DNA Center does not configure any of
        the preceding  credentials or settings on devices during discovery, at runtime, or during site
        assignment. However,  the telemetry settings and related configuration are pushed when the device is
        provisioned or when the  update Telemetry Settings action is performed.  DNA Center identifies and
        automatically corrects the following telemetry configuration issues on  the device.    SWIM certificate
        issue.   IOS WLC NA certificate issue.   PKCS12 certificate issue.   IOS telemetry configuration issue.
        The autocorrect telemetry config feature is supported only when Device Controllability is enabled. .

        Args:
            autocorrectTelemetryConfig(boolean): Site Design's If it is true, autocorrect telemetry config is
                enabled. If it is false, autocorrect telemetry config is disabled. The autocorrect
                telemetry config feature is supported only when device controllability is enabled. .
            deviceControllability(boolean): Site Design's If it is true, device controllability is enabled. If it is
                false, device controllability is disabled. .
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
            https://developer.cisco.com/docs/dna-center/#!update-device-controllability-settings
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
            "autocorrectTelemetryConfig": autocorrectTelemetryConfig,
            "deviceControllability": deviceControllability,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c7f28c3d23ba5384be5e769ae0505d00_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/deviceControllability/" + "settings"
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
            "bpm_c7f28c3d23ba5384be5e769ae0505d00_v2_3_7_6", json_data
        )

    def get_site_not_assigned_network_devices_v1(
        self, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Get network devices that are not assigned to any site. .

        Args:
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!get-site-not-assigned-network-devices
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

        e_url = "/dna/intent/api/v1/networkDevices/notAssignedToSite"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_abb50ef5853d5772a8c7184b972af6d5_v2_3_7_6", json_data
        )

    def get_site_not_assigned_network_devices_count_v1(
        self, headers=None, **request_parameters
    ):
        """Get network devices count that are not assigned to any site. .

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
            https://developer.cisco.com/docs/dna-center/#!get-site-not-assigned-network-devices-count
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

        e_url = "/dna/intent/api/v1/networkDevices/notAssignedToSite/coun" + "t"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f0f95023b5e85d68916757f62ebe3a39_v2_3_7_6", json_data
        )

    def unassign_network_devices_from_sites_v1(
        self,
        deviceIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Unassign unprovisioned network devices from their site. If device controllability is enabled, it will be
        triggered once device unassigned from site successfully. Device Controllability can be enabled/disabled
        using `/dna/intent/api/v1/networkDevices/deviceControllability/settings`. .

        Args:
            deviceIds(list): Site Design's Network device Ids.  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!unassign-network-devices-from-sites
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
                "jsd_a41113bc28515538af4fe4d2ff707f60_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/unassignFromSite/apply"
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
            "bpm_a41113bc28515538af4fe4d2ff707f60_v2_3_7_6", json_data
        )

    def get_site_assigned_network_device_v1(
        self, id, headers=None, **request_parameters
    ):
        """Get site assigned network device. The items in the list are arranged in an order that corresponds with their
        internal identifiers. .

        Args:
            id(str): id path parameter. Network Device Id. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!get-site-assigned-network-device
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

        e_url = "/dna/intent/api/v1/networkDevices/{id}/assignedToSite"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f439c50a9743505a89dd01b099ae2ac2_v2_3_7_6", json_data
        )

    def retrieves_the_list_of_network_profiles_for_sites_v1(
        self,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of network profiles for sites. .

        Args:
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            sort_by(str): sortBy query parameter. A property within the response to sort by. .
            order(str): order query parameter. Whether ascending or descending order should be used to sort
                the response. .
            type(str): type query parameter. Filter responses to only include profiles of a given type .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-network-profiles-for-sites
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(type, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
            "type": type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkProfilesForSites"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f98e2b2923855879acfcb06c5723add_v2_3_7_6", json_data
        )

    def retrieves_the_count_of_network_profiles_for_sites_v1(
        self, type=None, headers=None, **request_parameters
    ):
        """Retrieves the count of network profiles for sites .

        Args:
            type(str): type query parameter. Filter the response to only count profiles of a given type .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-network-profiles-for-sites
        """
        check_type(headers, dict)
        check_type(type, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "type": type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkProfilesForSites/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ee735f82a2d9552097c69352326c3630_v2_3_7_6", json_data
        )

    def deletes_a_network_profile_for_sites_v1(
        self, id, headers=None, **request_parameters
    ):
        """Deletes a network profile for sites. .

        Args:
            id(str): id path parameter. The `id` of the network profile, retrievable from `GET
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!deletes-a-network-profile-for-sites
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

        e_url = "/dna/intent/api/v1/networkProfilesForSites/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e753f36584d75677a7076577f36dd515_v2_3_7_6", json_data
        )

    def retrieve_a_network_profile_for_sites_by_id_v1(
        self, id, headers=None, **request_parameters
    ):
        """Retrieves a network profile for sites by id. .

        Args:
            id(str): id path parameter. The `id` of the network profile, retrievable from `GET
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-network-profile-for-sites-by-id
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

        e_url = "/dna/intent/api/v1/networkProfilesForSites/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e67cf4ec83635f318184f32dff700aa7_v2_3_7_6", json_data
        )

    def assign_a_network_profile_for_sites_to_the_given_site_v1(
        self,
        profile_id,
        id=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Assigns a given network profile for sites to a given site. Also assigns the profile to child sites. .

        Args:
            id(string): Site Design's Id.
            profile_id(str): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
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
            https://developer.cisco.com/docs/dna-center/#!assign-a-network-profile-for-sites-to-the-given-site
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(profile_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "profileId": profile_id,
        }
        _payload = {
            "id": id,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b350fb0876a25879973b0840fbb690bb_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/networkProfilesForSites/{profileId}/s"
            + "iteAssignments"
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
            "bpm_b350fb0876a25879973b0840fbb690bb_v2_3_7_6", json_data
        )

    def retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
        self, profile_id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Retrieves the list of sites that the given network profile for sites is assigned to. The list includes the sites
        the profile has been directly assigned to, as well as child sites that have inherited the profile. .

        Args:
            profile_id(str): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-sites-that-the-given-network-profile-for-sites-is-assigned-to
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(profile_id, str, may_be_none=False)
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
            "profileId": profile_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/networkProfilesForSites/{profileId}/s"
            + "iteAssignments"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c5786cf2e69852a1aefbcd9f06a0366d_v2_3_7_6", json_data
        )

    def assign_a_network_profile_for_sites_to_a_list_of_sites_v1(
        self,
        profile_id,
        type=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Assign a network profile for sites to a list of sites. Also assigns the profile to child sites. .

        Args:
            type(object): Site Design's type.
            profile_id(str): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
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
            https://developer.cisco.com/docs/dna-center/#!assign-a-network-profile-for-sites-to-a-list-of-sites
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(profile_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "profileId": profile_id,
        }
        _payload = {
            "type": type,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_eea0014365ef78d30d9ba8f1752e8_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/networkProfilesForSites/{profileId}/s"
            + "iteAssignments/bulk"
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
            "bpm_eea0014365ef78d30d9ba8f1752e8_v2_3_7_6", json_data
        )

    def unassigns_a_network_profile_for_sites_from_multiple_sites_v1(
        self, profile_id, site_id, headers=None, **request_parameters
    ):
        """Unassigns a given network profile for sites from multiple sites. The profile must be removed from the containing
        building first if this site is a floor. .

        Args:
            profile_id(str): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
            site_id(str): siteId query parameter. The `id` of the site, retrievable from `GET
                /intent/api/v1/sites` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!unassigns-a-network-profile-for-sites-from-multiple-sites
        """
        check_type(headers, dict)
        check_type(site_id, str, may_be_none=False)
        check_type(profile_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
        }
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
            "/dna/intent/api/v1/networkProfilesForSites/{profileId}/s"
            + "iteAssignments/bulk"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d9b6dfe95d348865dfe1710ad9a9_v2_3_7_6", json_data
        )

    def retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
        self, profile_id, headers=None, **request_parameters
    ):
        """Retrieves the count of sites that the given network profile for sites is assigned to. .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-sites-that-the-given-network-profile-for-sites-is-assigned-to
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
            "/dna/intent/api/v1/networkProfilesForSites/{profileId}/s"
            + "iteAssignments/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c26aa98f05665962c91a1d780b943_v2_3_7_6", json_data
        )

    def unassigns_a_network_profile_for_sites_from_a_site_v1(
        self, id, profile_id, headers=None, **request_parameters
    ):
        """Unassigns a given network profile for sites from a site. The profile must be removed from parent sites first,
        otherwise this operation will not ulimately  unassign the profile. .

        Args:
            profile_id(str): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
            id(str): id path parameter. The `id` of the site, retrievable from `GET
                /intent/api/v1/networkProfilesForSites/{id}/siteAssignments` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!unassigns-a-network-profile-for-sites-from-a-site
        """
        check_type(headers, dict)
        check_type(profile_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "profileId": profile_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/networkProfilesForSites/{profileId}/s"
            + "iteAssignments/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a1e170a11d519b88cadd674fa2ea31_v2_3_7_6", json_data
        )

    def associate_v1(
        self, network_profile_id, site_id, headers=None, **request_parameters
    ):
        """Associate Site to a Network Profile .

        Args:
            network_profile_id(str): networkProfileId path parameter. Network-Profile Id to be associated .
            site_id(str): siteId path parameter. Site Id to be associated .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!associate
        """
        check_type(headers, dict)
        check_type(network_profile_id, str, may_be_none=False)
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
            "networkProfileId": network_profile_id,
            "siteId": site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/networkprofile/{networkProfileId}/sit" + "e/{siteId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a1800508058e4b82a08ea5637b794_v2_3_7_6", json_data
        )

    def disassociate_v1(
        self, network_profile_id, site_id, headers=None, **request_parameters
    ):
        """Disassociate a Site from a Network Profile .

        Args:
            network_profile_id(str): networkProfileId path parameter. Network-Profile Id to be associated .
            site_id(str): siteId path parameter. Site Id to be associated .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!disassociate
        """
        check_type(headers, dict)
        check_type(network_profile_id, str, may_be_none=False)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkProfileId": network_profile_id,
            "siteId": site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/networkprofile/{networkProfileId}/sit" + "e/{siteId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c8936d6a0c54e89b471fe36bf28de8_v2_3_7_6", json_data
        )

    def get_sites_v1(
        self,
        limit=None,
        name=None,
        name_hierarchy=None,
        offset=None,
        type=None,
        units_of_measure=None,
        headers=None,
        **request_parameters
    ):
        """Get sites. .

        Args:
            name(str): name query parameter. Site name. .
            name_hierarchy(str): nameHierarchy query parameter. Site name hierarchy. .
            type(str): type query parameter. Site type. .
            units_of_measure(str): _unitsOfMeasure query parameter. Floor units of measure .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!get-sites
        """
        check_type(headers, dict)
        check_type(name, str)
        check_type(name_hierarchy, str)
        check_type(type, str)
        check_type(units_of_measure, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
            "nameHierarchy": name_hierarchy,
            "type": type,
            "_unitsOfMeasure": units_of_measure,
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

        e_url = "/dna/intent/api/v1/sites"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a36b1e624416553eb72d8f1c9461c938_v2_3_7_6", json_data
        )

    def create_sites_v1(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Create area/building/floor together in bulk. If site already exist, then that will be ignored. Sites in the
        request payload need not to be ordered. .

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
            https://developer.cisco.com/docs/dna-center/#!create-sites
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
                "jsd_d292147221524a96616d982b0147c0_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/bulk"
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
            "bpm_d292147221524a96616d982b0147c0_v2_3_7_6", json_data
        )

    def get_sites_count_v1(self, name=None, headers=None, **request_parameters):
        """Get sites count. .

        Args:
            name(str): name query parameter. Site name. .
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
            https://developer.cisco.com/docs/dna-center/#!get-sites-count
        """
        check_type(headers, dict)
        check_type(name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c2d6e954468a7300d9ff8b2e22_v2_3_7_6", json_data
        )

    def retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1(
        self, site_id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Retrieves the list of profiles that the given site has been assigned.  These profiles may either be directly
        assigned to this site, or were assigned to a parent site and have been inherited. These assigments can
        be modified via the `/dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments` resources.
        .

        Args:
            site_id(str): siteId path parameter. The `id` of the site, retrievable from
                `/dna/intent/api/v1/sites` .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-network-profiles-that-the-given-site-has-been-assigned
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(site_id, str, may_be_none=False)
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
            "siteId": site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sites/{siteId}/profileAssignments"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f12eba75e472591490a014a7335e1e9b_v2_3_7_6", json_data
        )

    def retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1(
        self, site_id, headers=None, **request_parameters
    ):
        """Retrieves the count of profiles that the given site has been assigned.  These profiles may either be directly
        assigned to this site, or were assigned to a parent site and have been inherited. .

        Args:
            site_id(str): siteId path parameter. The `id` of the site, retrievable from
                `/dna/intent/api/v1/sites` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-profiles-that-the-given-site-has-been-assigned
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

        e_url = "/dna/intent/api/v1/sites/{siteId}/profileAssignments/cou" + "nt"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dc2361873bf7553c8fa5c7cb2024e5bb_v2_3_7_6", json_data
        )

    def creates_a_building_v2(
        self,
        address=None,
        country=None,
        latitude=None,
        longitude=None,
        name=None,
        parentId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates a building in the network hierarchy under area. .

        Args:
            address(string): Site Design's Building address. Example: 4900 Marie P. Debartolo Way, Santa Clara,
                California 95054, United States .
            country(string): Site Design's Country name .
            latitude(number): Site Design's Building Latitude. Example: 37.403712 .
            longitude(number): Site Design's Building Longitude. Example: -121.971063 .
            name(string): Site Design's Building name .
            parentId(string): Site Design's Parent Id .
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
            https://developer.cisco.com/docs/dna-center/#!creates-a-building
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
            "parentId": parentId,
            "name": name,
            "latitude": latitude,
            "longitude": longitude,
            "address": address,
            "country": country,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fc95c917352ad8410ffe6d6e522ed_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/buildings"
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
            "bpm_fc95c917352ad8410ffe6d6e522ed_v2_3_7_6", json_data
        )

    def updates_a_building_v2(
        self,
        id,
        address=None,
        country=None,
        latitude=None,
        longitude=None,
        name=None,
        parentId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates a building in the network hierarchy. .

        Args:
            address(string): Site Design's Building address. Example: 4900 Marie P. Debartolo Way, Santa Clara,
                California 95054, United States .
            country(string): Site Design's Country name .
            latitude(number): Site Design's Building Latitude. Example: 37.403712 .
            longitude(number): Site Design's Building Longitude. Example: -121.971063 .
            name(string): Site Design's Building name .
            parentId(string): Site Design's Parent Id .
            id(str): id path parameter. Building Id .
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
            https://developer.cisco.com/docs/dna-center/#!updates-a-building
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
            "parentId": parentId,
            "name": name,
            "latitude": latitude,
            "longitude": longitude,
            "address": address,
            "country": country,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cd16daa50533eb0f5873b7601abb2_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/buildings/{id}"
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
            "bpm_cd16daa50533eb0f5873b7601abb2_v2_3_7_6", json_data
        )

    def deletes_a_building_v2(self, id, headers=None, **request_parameters):
        """Deletes building in the network hierarchy. This operations fails if there are any floors for this building, or
        if there are any devices assigned to this building. .

        Args:
            id(str): id path parameter. Building ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!deletes-a-building
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

        e_url = "/dna/intent/api/v2/buildings/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory("bpm_2e5b54d99d30ea084daf36dc_v2_3_7_6", json_data)

    def gets_a_building_v2(self, id, headers=None, **request_parameters):
        """Gets a building in the network hierarchy. .

        Args:
            id(str): id path parameter. Building Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!gets-a-building
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

        e_url = "/dna/intent/api/v2/buildings/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ab03e8addf5c7e98475769ae1a97a8_v2_3_7_6", json_data
        )

    def creates_a_floor_v2(
        self,
        floorNumber=None,
        height=None,
        length=None,
        name=None,
        parentId=None,
        rfModel=None,
        unitsOfMeasure=None,
        width=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Create a floor in the network hierarchy under building. .

        Args:
            floorNumber(integer): Site Design's Floor number .
            height(number): Site Design's Floor height. Example : 10.1 .
            length(number): Site Design's Floor length. Example : 110.3 .
            name(string): Site Design's Floor name .
            parentId(string): Site Design's Parent Id.
            rfModel(string): Site Design's RF Model . Available values are 'Free Space', 'Outdoor Open Space',
                'Cubes And Walled Offices', 'Indoor High Ceiling' and 'Drywall Office Only'.
            unitsOfMeasure(string): Site Design's Units Of Measure. Available values are 'feet' and 'meters'.
            width(number): Site Design's Floor width. Example : 100.5 .
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
            https://developer.cisco.com/docs/dna-center/#!creates-a-floor
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
            "parentId": parentId,
            "name": name,
            "floorNumber": floorNumber,
            "rfModel": rfModel,
            "width": width,
            "length": length,
            "height": height,
            "unitsOfMeasure": unitsOfMeasure,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bfb1005f4d265f8bb340637175a5841f_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/floors"
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
            "bpm_bfb1005f4d265f8bb340637175a5841f_v2_3_7_6", json_data
        )

    def updates_floor_settings_v2(
        self,
        unitsOfMeasure=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates UI user preference for floor unit system. Unit sytem change will effect for all floors across all sites.
        .

        Args:
            unitsOfMeasure(string): Site Design's Floor units of measure . Available values are 'feet' and 'meters'.
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
            https://developer.cisco.com/docs/dna-center/#!updates-floor-settings
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
            "unitsOfMeasure": unitsOfMeasure,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ad936677c99a58f6b532359d66fe98a7_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/floors/settings"
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
            "bpm_ad936677c99a58f6b532359d66fe98a7_v2_3_7_6", json_data
        )

    def get_floor_settings_v2(self, headers=None, **request_parameters):
        """Gets UI user preference for floor unit system. .

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
            https://developer.cisco.com/docs/dna-center/#!get-floor-settings
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

        e_url = "/dna/intent/api/v2/floors/settings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a774ea6dda56adb3fc81df221f62c8_v2_3_7_6", json_data
        )

    def updates_a_floor_v2(
        self,
        id,
        floorNumber=None,
        height=None,
        length=None,
        name=None,
        parentId=None,
        rfModel=None,
        unitsOfMeasure=None,
        width=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates a floor in the network hierarchy. .

        Args:
            floorNumber(integer): Site Design's Floor number .
            height(number): Site Design's Floor height. Example : 10.1 .
            length(number): Site Design's Floor length. Example : 110.3 .
            name(string): Site Design's Floor name .
            parentId(string): Site Design's Parent Id.
            rfModel(string): Site Design's RF Model . Available values are 'Free Space', 'Outdoor Open Space',
                'Cubes And Walled Offices', 'Indoor High Ceiling' and 'Drywall Office Only'.
            unitsOfMeasure(string): Site Design's Units Of Measure. Available values are 'feet' and 'meters'.
            width(number): Site Design's Floor width. Example : 100.5 .
            id(str): id path parameter. Floor Id .
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
            https://developer.cisco.com/docs/dna-center/#!updates-a-floor
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
            "parentId": parentId,
            "name": name,
            "floorNumber": floorNumber,
            "rfModel": rfModel,
            "width": width,
            "length": length,
            "height": height,
            "unitsOfMeasure": unitsOfMeasure,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d5da0365e31972173f015ed3614_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/floors/{id}"
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
            "bpm_d5da0365e31972173f015ed3614_v2_3_7_6", json_data
        )

    def gets_a_floor_v2(
        self, id, units_of_measure=None, headers=None, **request_parameters
    ):
        """Gets a floor in the network hierarchy. .

        Args:
            id(str): id path parameter. Floor Id .
            units_of_measure(str): _unitsOfMeasure query parameter. Floor units of measure .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!gets-a-floor
        """
        check_type(headers, dict)
        check_type(units_of_measure, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "_unitsOfMeasure": units_of_measure,
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

        e_url = "/dna/intent/api/v2/floors/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f2f085a136a55e6a03f75ca03de17bd_v2_3_7_6", json_data
        )

    def deletes_a_floor_v2(self, id, headers=None, **request_parameters):
        """Deletes a floor from the network hierarchy. This operations fails if there are any devices assigned to this
        floor. .

        Args:
            id(str): id path parameter. Floor ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!deletes-a-floor
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

        e_url = "/dna/intent/api/v2/floors/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ec0e563f25f44bbe568527ea87fd6_v2_3_7_6", json_data
        )

    def uploads_floor_image_v2(
        self,
        id,
        multipart_fields,
        headers=None,
        multipart_monitor_callback=None,
        **request_parameters
    ):
        """Uploads floor image. .

        Args:
            id(str): id path parameter. Floor Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request.
            multipart_fields(dict,list): form data values.
            create_callback(function): function that creates a function that
                monitors the progress of the upload.
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
            https://developer.cisco.com/docs/dna-center/#!uploads-floor-image
        """
        check_type(headers, dict)
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
        multipart_body = self._session.multipart_data(
            fields=multipart_fields, create_callback=multipart_monitor_callback
        )
        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        else:
            _headers["Content-Type"] = multipart_body.content_type
            with_custom_headers = True
        e_url = "/dna/intent/api/v2/floors/{id}/uploadImage"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers, data=multipart_body
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, data=multipart_body
            )

        return self._object_factory(
            "bpm_df8448b465a0abdc9bb7ee17aac9f_v2_3_7_6", json_data
        )

    # Alias Function
    def updates_floor_settings(
        self,
        unitsOfMeasure=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of updates_floor_settings_v2 .
        Args:
            unitsOfMeasure(string): Site Design's Floor units of measure . Available values are 'feet' and 'meters'.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of updates_floor_settings_v2 .
        """
        return self.updates_floor_settings_v2(
            unitsOfMeasure=unitsOfMeasure,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_sites_count(self, name=None, headers=None, **request_parameters):
        """This function is an alias of get_sites_count_v1 .
        Args:
            name(basestring): name query parameter. Site name. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_sites_count_v1 .
        """
        return self.get_sites_count_v1(name=name, headers=headers, **request_parameters)

    # Alias Function
    def retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned(
        self, site_id, headers=None, **request_parameters
    ):
        """This function is an alias of retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1 .
        Args:
            site_id(basestring): siteId path parameter. The `id` of the site, retrievable from
                `/dna/intent/api/v1/sites` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1 .
        """
        return self.retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1(
            site_id=site_id, headers=headers, **request_parameters
        )

    # Alias Function
    def retrieves_the_list_of_network_profiles_for_sites(
        self,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of retrieves_the_list_of_network_profiles_for_sites_v1 .
        Args:
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            sort_by(basestring): sortBy query parameter. A property within the response to sort by. .
            order(basestring): order query parameter. Whether ascending or descending order should be used to sort
                the response. .
            type(basestring): type query parameter. Filter responses to only include profiles of a given type .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_list_of_network_profiles_for_sites_v1 .
        """
        return self.retrieves_the_list_of_network_profiles_for_sites_v1(
            limit=limit,
            offset=offset,
            order=order,
            sort_by=sort_by,
            type=type,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def get_site_not_assigned_network_devices(
        self, limit=None, offset=None, headers=None, **request_parameters
    ):
        """This function is an alias of get_site_not_assigned_network_devices_v1 .
        Args:
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_site_not_assigned_network_devices_v1 .
        """
        return self.get_site_not_assigned_network_devices_v1(
            limit=limit, offset=offset, headers=headers, **request_parameters
        )

    # Alias Function
    def get_site_not_assigned_network_devices_count(
        self, headers=None, **request_parameters
    ):
        """This function is an alias of get_site_not_assigned_network_devices_count_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_site_not_assigned_network_devices_count_v1 .
        """
        return self.get_site_not_assigned_network_devices_count_v1(
            headers=headers, **request_parameters
        )

    # Alias Function
    def creates_a_floor(
        self,
        floorNumber=None,
        height=None,
        length=None,
        name=None,
        parentId=None,
        rfModel=None,
        unitsOfMeasure=None,
        width=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of creates_a_floor_v2 .
        Args:
            floorNumber(integer): Site Design's Floor number .
            height(number): Site Design's Floor height. Example : 10.1 .
            length(number): Site Design's Floor length. Example : 110.3 .
            name(string): Site Design's Floor name .
            parentId(string): Site Design's Parent Id.
            rfModel(string): Site Design's RF Model . Available values are 'Free Space', 'Outdoor Open Space',
                'Cubes And Walled Offices', 'Indoor High Ceiling' and 'Drywall Office Only'.
            unitsOfMeasure(string): Site Design's Units Of Measure. Available values are 'feet' and 'meters'.
            width(number): Site Design's Floor width. Example : 100.5 .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of creates_a_floor_v2 .
        """
        return self.creates_a_floor_v2(
            floorNumber=floorNumber,
            height=height,
            length=length,
            name=name,
            parentId=parentId,
            rfModel=rfModel,
            unitsOfMeasure=unitsOfMeasure,
            width=width,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def updates_an_area(
        self,
        id,
        name=None,
        parentId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of updates_an_area_v1 .
        Args:
            name(string): Site Design's Area name .
            parentId(string): Site Design's Parent Id .
            id(basestring): id path parameter. Area Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of updates_an_area_v1 .
        """
        return self.updates_an_area_v1(
            id=id,
            name=name,
            parentId=parentId,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def uploads_floor_image(
        self,
        id,
        multipart_fields,
        headers=None,
        multipart_monitor_callback=None,
        **request_parameters
    ):
        """This function is an alias of uploads_floor_image_v2 .
        Args:
            id(str): id path parameter. Floor Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request.
            multipart_fields(dict,list): form data values.
            create_callback(function): function that creates a function that
                monitors the progress of the upload.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of uploads_floor_image_v2 .
        """
        return self.uploads_floor_image_v2(
            id=id,
            multipart_fields=multipart_fields,
            headers=headers,
            multipart_monitor_callback=multipart_monitor_callback,
            **request_parameters
        )

    # Alias Function
    def creates_an_area(
        self,
        name=None,
        parentId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of creates_an_area_v1 .
        Args:
            name(string): Site Design's Area name .
            parentId(string): Site Design's Parent Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of creates_an_area_v1 .
        """
        return self.creates_an_area_v1(
            name=name,
            parentId=parentId,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to(
        self, profile_id, headers=None, **request_parameters
    ):
        """This function is an alias of retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1 .
        Args:
            profile_id(basestring): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1 .
        """
        return self.retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
            profile_id=profile_id, headers=headers, **request_parameters
        )

    # Alias Function
    def updates_a_floor(
        self,
        id,
        floorNumber=None,
        height=None,
        length=None,
        name=None,
        parentId=None,
        rfModel=None,
        unitsOfMeasure=None,
        width=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of updates_a_floor_v2 .
        Args:
            floorNumber(integer): Site Design's Floor number .
            height(number): Site Design's Floor height. Example : 10.1 .
            length(number): Site Design's Floor length. Example : 110.3 .
            name(string): Site Design's Floor name .
            parentId(string): Site Design's Parent Id.
            rfModel(string): Site Design's RF Model . Available values are 'Free Space', 'Outdoor Open Space',
                'Cubes And Walled Offices', 'Indoor High Ceiling' and 'Drywall Office Only'.
            unitsOfMeasure(string): Site Design's Units Of Measure. Available values are 'feet' and 'meters'.
            width(number): Site Design's Floor width. Example : 100.5 .
            id(basestring): id path parameter. Floor Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of updates_a_floor_v2 .
        """
        return self.updates_a_floor_v2(
            id=id,
            floorNumber=floorNumber,
            height=height,
            length=length,
            name=name,
            parentId=parentId,
            rfModel=rfModel,
            unitsOfMeasure=unitsOfMeasure,
            width=width,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def deletes_a_network_profile_for_sites(
        self, id, headers=None, **request_parameters
    ):
        """This function is an alias of deletes_a_network_profile_for_sites_v1 .
        Args:
            id(basestring): id path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of deletes_a_network_profile_for_sites_v1 .
        """
        return self.deletes_a_network_profile_for_sites_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def get_site_assigned_network_device(self, id, headers=None, **request_parameters):
        """This function is an alias of get_site_assigned_network_device_v1 .
        Args:
            id(basestring): id path parameter. Network Device Id. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_site_assigned_network_device_v1 .
        """
        return self.get_site_assigned_network_device_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def assign_a_network_profile_for_sites_to_the_given_site(
        self,
        profile_id,
        id=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of assign_a_network_profile_for_sites_to_the_given_site_v1 .
        Args:
            id(string): Site Design's Id.
            profile_id(basestring): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of assign_a_network_profile_for_sites_to_the_given_site_v1 .
        """
        return self.assign_a_network_profile_for_sites_to_the_given_site_v1(
            profile_id=profile_id,
            id=id,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def creates_a_building(
        self,
        address=None,
        country=None,
        latitude=None,
        longitude=None,
        name=None,
        parentId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of creates_a_building_v2 .
        Args:
            address(string): Site Design's Building address. Example: 4900 Marie P. Debartolo Way, Santa Clara,
                California 95054, United States .
            country(string): Site Design's Country name .
            latitude(number): Site Design's Building Latitude. Example: 37.403712 .
            longitude(number): Site Design's Building Longitude. Example: -121.971063 .
            name(string): Site Design's Building name .
            parentId(string): Site Design's Parent Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of creates_a_building_v2 .
        """
        return self.creates_a_building_v2(
            address=address,
            country=country,
            latitude=latitude,
            longitude=longitude,
            name=name,
            parentId=parentId,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def deletes_an_area(self, id, headers=None, **request_parameters):
        """This function is an alias of deletes_an_area_v1 .
        Args:
            id(basestring): id path parameter. Area ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of deletes_an_area_v1 .
        """
        return self.deletes_an_area_v1(id=id, headers=headers, **request_parameters)

    # Alias Function
    def retrieve_a_network_profile_for_sites_by_id(
        self, id, headers=None, **request_parameters
    ):
        """This function is an alias of retrieve_a_network_profile_for_sites_by_id_v1 .
        Args:
            id(basestring): id path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieve_a_network_profile_for_sites_by_id_v1 .
        """
        return self.retrieve_a_network_profile_for_sites_by_id_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def gets_a_floor(
        self, id, units_of_measure=None, headers=None, **request_parameters
    ):
        """This function is an alias of gets_a_floor_v2 .
        Args:
            id(basestring): id path parameter. Floor Id .
            units_of_measure(basestring): _unitsOfMeasure query parameter. Floor units of measure .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of gets_a_floor_v2 .
        """
        return self.gets_a_floor_v2(
            id=id,
            units_of_measure=units_of_measure,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to(
        self, profile_id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """This function is an alias of retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1 .
        Args:
            profile_id(basestring): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1 .
        """
        return self.retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1(
            profile_id=profile_id,
            limit=limit,
            offset=offset,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def assign_a_network_profile_for_sites_to_a_list_of_sites(
        self,
        profile_id,
        type=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of assign_a_network_profile_for_sites_to_a_list_of_sites_v1 .
        Args:
            type(object): Site Design's type.
            profile_id(basestring): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of assign_a_network_profile_for_sites_to_a_list_of_sites_v1 .
        """
        return self.assign_a_network_profile_for_sites_to_a_list_of_sites_v1(
            profile_id=profile_id,
            type=type,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def updates_a_building(
        self,
        id,
        address=None,
        country=None,
        latitude=None,
        longitude=None,
        name=None,
        parentId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of updates_a_building_v2 .
        Args:
            address(string): Site Design's Building address. Example: 4900 Marie P. Debartolo Way, Santa Clara,
                California 95054, United States .
            country(string): Site Design's Country name .
            latitude(number): Site Design's Building Latitude. Example: 37.403712 .
            longitude(number): Site Design's Building Longitude. Example: -121.971063 .
            name(string): Site Design's Building name .
            parentId(string): Site Design's Parent Id .
            id(basestring): id path parameter. Building Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of updates_a_building_v2 .
        """
        return self.updates_a_building_v2(
            id=id,
            address=address,
            country=country,
            latitude=latitude,
            longitude=longitude,
            name=name,
            parentId=parentId,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def retrieves_the_count_of_network_profiles_for_sites(
        self, type=None, headers=None, **request_parameters
    ):
        """This function is an alias of retrieves_the_count_of_network_profiles_for_sites_v1 .
        Args:
            type(basestring): type query parameter. Filter the response to only count profiles of a given type .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_count_of_network_profiles_for_sites_v1 .
        """
        return self.retrieves_the_count_of_network_profiles_for_sites_v1(
            type=type, headers=headers, **request_parameters
        )

    # Alias Function
    def unassigns_a_network_profile_for_sites_from_multiple_sites(
        self, profile_id, site_id, headers=None, **request_parameters
    ):
        """This function is an alias of unassigns_a_network_profile_for_sites_from_multiple_sites_v1 .
        Args:
            profile_id(basestring): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
            site_id(basestring): siteId query parameter. The `id` of the site, retrievable from `GET
                /intent/api/v1/sites` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of unassigns_a_network_profile_for_sites_from_multiple_sites_v1 .
        """
        return self.unassigns_a_network_profile_for_sites_from_multiple_sites_v1(
            profile_id=profile_id,
            site_id=site_id,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def unassign_network_devices_from_sites(
        self,
        deviceIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of unassign_network_devices_from_sites_v1 .
        Args:
            deviceIds(list): Site Design's Network device Ids.  (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of unassign_network_devices_from_sites_v1 .
        """
        return self.unassign_network_devices_from_sites_v1(
            deviceIds=deviceIds,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def unassigns_a_network_profile_for_sites_from_a_site(
        self, id, profile_id, headers=None, **request_parameters
    ):
        """This function is an alias of unassigns_a_network_profile_for_sites_from_a_site_v1 .
        Args:
            profile_id(basestring): profileId path parameter. The `id` of the network profile, retrievable from `GET
                /intent/api/v1/networkProfilesForSites` .
            id(basestring): id path parameter. The `id` of the site, retrievable from `GET
                /intent/api/v1/networkProfilesForSites/{id}/siteAssignments` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of unassigns_a_network_profile_for_sites_from_a_site_v1 .
        """
        return self.unassigns_a_network_profile_for_sites_from_a_site_v1(
            id=id, profile_id=profile_id, headers=headers, **request_parameters
        )

    # Alias Function
    def gets_an_area(self, id, headers=None, **request_parameters):
        """This function is an alias of gets_an_area_v1 .
        Args:
            id(basestring): id path parameter. Area Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of gets_an_area_v1 .
        """
        return self.gets_an_area_v1(id=id, headers=headers, **request_parameters)

    # Alias Function
    def deletes_a_building(self, id, headers=None, **request_parameters):
        """This function is an alias of deletes_a_building_v2 .
        Args:
            id(basestring): id path parameter. Building ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of deletes_a_building_v2 .
        """
        return self.deletes_a_building_v2(id=id, headers=headers, **request_parameters)

    # Alias Function
    def get_device_controllability_settings(self, headers=None, **request_parameters):
        """This function is an alias of get_device_controllability_settings_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_controllability_settings_v1 .
        """
        return self.get_device_controllability_settings_v1(
            headers=headers, **request_parameters
        )

    # Alias Function
    def get_site_assigned_network_devices_count(
        self, site_id, headers=None, **request_parameters
    ):
        """This function is an alias of get_site_assigned_network_devices_count_v1 .
        Args:
            site_id(basestring): siteId query parameter. Site Id. It must be area Id or building Id or floor Id. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_site_assigned_network_devices_count_v1 .
        """
        return self.get_site_assigned_network_devices_count_v1(
            site_id=site_id, headers=headers, **request_parameters
        )

    # Alias Function
    def gets_a_building(self, id, headers=None, **request_parameters):
        """This function is an alias of gets_a_building_v2 .
        Args:
            id(basestring): id path parameter. Building Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of gets_a_building_v2 .
        """
        return self.gets_a_building_v2(id=id, headers=headers, **request_parameters)

    # Alias Function
    def assign_network_devices_to_a_site(
        self,
        deviceIds=None,
        siteId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of assign_network_devices_to_a_site_v1 .
        Args:
            deviceIds(list): Site Design's Unassigned network devices.  (list of strings).
            siteId(string): Site Design's This must be building Id or floor Id. Access points, Sensors are assigned
                to floor. Remaining network devices are assigned to building. Site Id can be retrieved
                using '/intent/api/v1/sites'. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of assign_network_devices_to_a_site_v1 .
        """
        return self.assign_network_devices_to_a_site_v1(
            deviceIds=deviceIds,
            siteId=siteId,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned(
        self, site_id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """This function is an alias of retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1 .
        Args:
            site_id(basestring): siteId path parameter. The `id` of the site, retrievable from
                `/dna/intent/api/v1/sites` .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1 .
        """
        return self.retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned_v1(
            site_id=site_id,
            limit=limit,
            offset=offset,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def create_sites(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """This function is an alias of create_sites_v1 .
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
            This function returns the output of create_sites_v1 .
        """
        return self.create_sites_v1(
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def deletes_a_floor(self, id, headers=None, **request_parameters):
        """This function is an alias of deletes_a_floor_v2 .
        Args:
            id(basestring): id path parameter. Floor ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of deletes_a_floor_v2 .
        """
        return self.deletes_a_floor_v2(id=id, headers=headers, **request_parameters)

    # Alias Function
    def update_device_controllability_settings(
        self,
        autocorrectTelemetryConfig=None,
        deviceControllability=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of update_device_controllability_settings_v1 .
        Args:
            autocorrectTelemetryConfig(boolean): Site Design's If it is true, autocorrect telemetry config is
                enabled. If it is false, autocorrect telemetry config is disabled. The autocorrect
                telemetry config feature is supported only when device controllability is enabled. .
            deviceControllability(boolean): Site Design's If it is true, device controllability is enabled. If it is
                false, device controllability is disabled. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_device_controllability_settings_v1 .
        """
        return self.update_device_controllability_settings_v1(
            autocorrectTelemetryConfig=autocorrectTelemetryConfig,
            deviceControllability=deviceControllability,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_floor_settings(self, headers=None, **request_parameters):
        """This function is an alias of get_floor_settings_v2 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_floor_settings_v2 .
        """
        return self.get_floor_settings_v2(headers=headers, **request_parameters)

    # Alias Function
    def get_site_assigned_network_devices(
        self, site_id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """This function is an alias of get_site_assigned_network_devices_v1 .
        Args:
            site_id(basestring): siteId query parameter. Site Id. It must be area Id or building Id or floor Id. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_site_assigned_network_devices_v1 .
        """
        return self.get_site_assigned_network_devices_v1(
            site_id=site_id,
            limit=limit,
            offset=offset,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def get_sites(
        self,
        limit=None,
        name=None,
        name_hierarchy=None,
        offset=None,
        type=None,
        units_of_measure=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_sites_v1 .
        Args:
            name(basestring): name query parameter. Site name. .
            name_hierarchy(basestring): nameHierarchy query parameter. Site name hierarchy. .
            type(basestring): type query parameter. Site type. .
            units_of_measure(basestring): _unitsOfMeasure query parameter. Floor units of measure .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_sites_v1 .
        """
        return self.get_sites_v1(
            limit=limit,
            name=name,
            name_hierarchy=name_hierarchy,
            offset=offset,
            type=type,
            units_of_measure=units_of_measure,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def associate(
        self, network_profile_id, site_id, headers=None, **request_parameters
    ):
        """This function is an alias of associate_v1 .
        Args:
            network_profile_id(basestring): networkProfileId path parameter. Network-Profile Id to be associated .
            site_id(basestring): siteId path parameter. Site Id to be associated .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of associate_v1 .
        """
        return self.associate_v1(
            network_profile_id=network_profile_id,
            site_id=site_id,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def disassociate(
        self, network_profile_id, site_id, headers=None, **request_parameters
    ):
        """This function is an alias of disassociate_v1 .
        Args:
            network_profile_id(basestring): networkProfileId path parameter. Network-Profile Id to be associated .
            site_id(basestring): siteId path parameter. Site Id to be associated .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of disassociate_v1 .
        """
        return self.disassociate_v1(
            network_profile_id=network_profile_id,
            site_id=site_id,
            headers=headers,
            **request_parameters
        )

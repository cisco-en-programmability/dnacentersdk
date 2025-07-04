# -*- coding: utf-8 -*-
"""Cisco Catalyst Center LAN Automation API wrapper.

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


class LanAutomation(object):
    """Cisco Catalyst Center LAN Automation API (version: 3.1.3.0).

    Wraps the Catalyst Center LAN Automation
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new LanAutomation
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(LanAutomation, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def lan_automation_start(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Invoke this API to start LAN Automation for the given site. .

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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-start
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
                "jsd_b119a4d455e35cc3b2cc6695a045cbfa_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/lan-automation"
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
            "bpm_b119a4d455e35cc3b2cc6695a045cbfa_v3_1_3_0", json_data
        )

    def start(
        self, headers=None, payload=None, active_validation=True, **query_parameters
    ):
        """Alias for `lan_automation_start <#dnacentersdk.
        api.v3_1_3_0.lan_automation.
        LanAutomation.lan_automation_start>`_
        """
        return self.lan_automation_start(
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def lan_automation_session_count(self, headers=None, **request_parameters):
        """Invoke this API to get the total count of LAN Automation sessions. .

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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-session-count
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

        e_url = "/dna/intent/api/v1/lan-automation/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eea014edd5807925df3a414a92ed4_v3_1_3_0", json_data
        )

    def session_count(self, headers=None, **query_parameters):
        """Alias for `lan_automation_session_count <#dnacentersdk.
        api.v3_1_3_0.lan_automation.
        LanAutomation.lan_automation_session_count>`_
        """
        return self.lan_automation_session_count(headers=headers, **query_parameters)

    def lan_automation_log(
        self, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Invoke this API to get the LAN Automation session logs. .

        Args:
            offset(int): offset query parameter. Starting index of the LAN Automation session. Minimum value is 1. .
            limit(int): limit query parameter. Number of LAN Automation sessions to be retrieved. Limit value can
                range between 1 to 10. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-log
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

        e_url = "/dna/intent/api/v1/lan-automation/log"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e37f6c9650b68e0aaac866a162cf_v3_1_3_0", json_data
        )

    def log(self, limit=None, offset=None, headers=None, **query_parameters):
        """Alias for `lan_automation_log <#dnacentersdk.
        api.v3_1_3_0.lan_automation.
        LanAutomation.lan_automation_log>`_
        """
        return self.lan_automation_log(
            limit=limit, offset=offset, headers=headers, **query_parameters
        )

    def lan_automation_log_by_id(self, id, headers=None, **request_parameters):
        """Invoke this API to get the LAN Automation session logs based on the given LAN Automation session id. .

        Args:
            id(str): id path parameter. LAN Automation session identifier. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-log-by-id
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

        e_url = "/dna/intent/api/v1/lan-automation/log/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e98b744fde50a1b53761251c43bfb0_v3_1_3_0", json_data
        )

    def log_by_id(self, id, headers=None, **query_parameters):
        """Alias for `lan_automation_log_by_id <#dnacentersdk.
        api.v3_1_3_0.lan_automation.
        LanAutomation.lan_automation_log_by_id>`_
        """
        return self.lan_automation_log_by_id(id=id, headers=headers, **query_parameters)

    def lan_automation_logs_for_individual_devices(
        self, id, serial_number, log_level=None, headers=None, **request_parameters
    ):
        """Invoke this API to get the LAN Automation session logs for individual devices based on the given LAN Automation
        session id and device serial number. .

        Args:
            id(str): id path parameter. LAN Automation session identifier. .
            serial_number(str): serialNumber path parameter. Device serial number. .
            log_level(str): logLevel query parameter. Supported levels are ERROR, INFO, WARNING, TRACE, CONFIG and
                ALL. Specifying ALL will display device specific logs with the exception of CONFIG logs.
                In order to view CONFIG logs along with the remaining logs, please leave the query
                parameter blank. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-logs-for-individual-devices
        """
        check_type(headers, dict)
        check_type(log_level, str)
        check_type(id, str, may_be_none=False)
        check_type(serial_number, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "logLevel": log_level,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "serialNumber": serial_number,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/lan-" + "automation/log/{id}/{serialNumber}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c3441f7507a98d02579c25814f4_v3_1_3_0", json_data
        )

    def lan_automation_active_sessions(self, headers=None, **request_parameters):
        """Invoke this API to get the LAN Automation active session information .

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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-active-sessions
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

        e_url = "/dna/intent/api/v1/lan-automation/sessions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a19cf2241e75c648220d7172e9e4013_v3_1_3_0", json_data
        )

    def lan_automation_status(
        self, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Invoke this API to get the LAN Automation session status. .

        Args:
            offset(int): offset query parameter. Starting index of the LAN Automation session. Minimum value is 1. .
            limit(int): limit query parameter. Number of LAN Automation sessions to be retrieved. Limit value can
                range between 1 to 10. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-status
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

        e_url = "/dna/intent/api/v1/lan-automation/status"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c56a6c58fd5b71b7949036855ee25b_v3_1_3_0", json_data
        )

    def status(self, limit=None, offset=None, headers=None, **query_parameters):
        """Alias for `lan_automation_status <#dnacentersdk.
        api.v3_1_3_0.lan_automation.
        LanAutomation.lan_automation_status>`_
        """
        return self.lan_automation_status(
            limit=limit, offset=offset, headers=headers, **query_parameters
        )

    def lan_automation_status_by_id(self, id, headers=None, **request_parameters):
        """Invoke this API to get the LAN Automation session status based on the given Lan Automation session id. .

        Args:
            id(str): id path parameter. LAN Automation session identifier. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-status-by-id
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

        e_url = "/dna/intent/api/v1/lan-automation/status/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d5727c4bdb1056308cd10e99dff2acb8_v3_1_3_0", json_data
        )

    def status_by_id(self, id, headers=None, **query_parameters):
        """Alias for `lan_automation_status_by_id <#dnacentersdk.
        api.v3_1_3_0.lan_automation.
        LanAutomation.lan_automation_status_by_id>`_
        """
        return self.lan_automation_status_by_id(
            id=id, headers=headers, **query_parameters
        )

    def lan_automation_device_update(
        self,
        feature,
        hostnameUpdateDevices=None,
        linkUpdate=None,
        loopbackUpdateDeviceList=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Invoke this API to perform a DAY-N update on LAN Automation-related devices. Supported features include
        Loopback0 IP update, hostname update, link addition, and link deletion. .

        Args:
            hostnameUpdateDevices(list): LAN Automation's hostnameUpdateDevices (list of objects).
            linkUpdate(object): LAN Automation's linkUpdate.
            loopbackUpdateDeviceList(list): LAN Automation's loopbackUpdateDeviceList (list of objects).
            feature(str): feature query parameter. Feature ID for the update. Supported feature IDs include:
                LOOPBACK0_IPADDRESS_UPDATE, HOSTNAME_UPDATE, LINK_ADD, and LINK_DELETE. .
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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-device-update
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "feature": feature,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "loopbackUpdateDeviceList": loopbackUpdateDeviceList,
            "linkUpdate": linkUpdate,
            "hostnameUpdateDevices": hostnameUpdateDevices,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_aac9ba55e5043b4d5e0995c566dce_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/lan-automation/updateDevice"
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
            "bpm_aac9ba55e5043b4d5e0995c566dce_v3_1_3_0", json_data
        )

    def lan_automation_stop(self, id, headers=None, **request_parameters):
        """Invoke this API to stop LAN Automation for the given site. .

        Args:
            id(str): id path parameter. LAN Automation id can be obtained from /dna/intent/api/v1/lan-
                automation/status. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-stop
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

        e_url = "/dna/intent/api/v1/lan-automation/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ed815ca3e5ab5ae48720795217ec776b_v3_1_3_0", json_data
        )

    def stop(self, id, headers=None, **query_parameters):
        """Alias for `lan_automation_stop <#dnacentersdk.
        api.v3_1_3_0.lan_automation.
        LanAutomation.lan_automation_stop>`_
        """
        return self.lan_automation_stop(id=id, headers=headers, **query_parameters)

    def lan_automation_stop_and_update_devices(
        self,
        id,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Invoke this API to stop LAN Automation and Update Loopback0 IP Address of Devices, discovered in the current
        session .

        Args:
            id(str): id path parameter. LAN Automation id can be obtained from /dna/intent/api/v1/lan-
                automation/status. .
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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-stop-and-update-devices
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_d413a3d054ac50fa921ca8cf7fdf5449_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/lan-automation/{id}"
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
            "bpm_d413a3d054ac50fa921ca8cf7fdf5449_v3_1_3_0", json_data
        )

    def get_port_channels(
        self,
        device1_management_ipaddress=None,
        device1_uuid=None,
        device2_management_ipaddress=None,
        device2_uuid=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of Port Channel between the LAN Automation associated devices. .

        Args:
            device1_management_ipaddress(str): device1ManagementIPAddress query parameter. The management IP address
                of the device1. .
            device1_uuid(str): device1Uuid query parameter. Unique identifier for the network device1 .
            device2_management_ipaddress(str): device2ManagementIPAddress query parameter. The management IP address
                of the device2. .
            device2_uuid(str): device2Uuid query parameter. Unique identifier for the network device2 .
            offset(str): offset query parameter. Starting record for pagination. .
            limit(str): limit query parameter. Maximum number of Port Channel to return. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!get-port-channels
        """
        check_type(headers, dict)
        check_type(device1_management_ipaddress, str)
        check_type(device1_uuid, str)
        check_type(device2_management_ipaddress, str)
        check_type(device2_uuid, str)
        check_type(offset, str)
        check_type(limit, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "device1ManagementIPAddress": device1_management_ipaddress,
            "device1Uuid": device1_uuid,
            "device2ManagementIPAddress": device2_management_ipaddress,
            "device2Uuid": device2_uuid,
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

        e_url = "/dna/intent/api/v1/lanAutomation/portChannels"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ee969674421c512494b828e1115d899f_v3_1_3_0", json_data
        )

    def create_a_new_port_channel_between_devices(
        self,
        device1ManagementIPAddress=None,
        device1Uuid=None,
        device2ManagementIPAddress=None,
        device2Uuid=None,
        portChannelMembers=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates a Port Channel between two LAN Automation associated devices using the PAgP protocol, with a
        minimum of 2 and a maximum of 8 LAN Automated interfaces in UP status. .

        Args:
            device1ManagementIPAddress(string): LAN Automation's Either device1ManagementIPAddress or device1Uuid is
                required. .
            device1Uuid(string): LAN Automation's Either device1ManagementIPAddress or device1Uuid is required. .
            device2ManagementIPAddress(string): LAN Automation's Either device2ManagementIPAddress or device2Uuid is
                required. .
            device2Uuid(string): LAN Automation's Either device2ManagementIPAddress or device2Uuid is required. .
            portChannelMembers(list): LAN Automation's portChannelMembers (list of objects).
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
            https://developer.cisco.com/docs/dna-center/#!create-a-new-port-channel-between-devices
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
            "device1ManagementIPAddress": device1ManagementIPAddress,
            "device1Uuid": device1Uuid,
            "device2ManagementIPAddress": device2ManagementIPAddress,
            "device2Uuid": device2Uuid,
            "portChannelMembers": portChannelMembers,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cf0138550909ea413dab063868c_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/lanAutomation/portChannels"
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
            "bpm_cf0138550909ea413dab063868c_v3_1_3_0", json_data
        )

    def get_port_channel_information_by_id(
        self, id, headers=None, **request_parameters
    ):
        """This API retrieves Port Channel information using its ID. .

        Args:
            id(str): id path parameter. ID of the port channel. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!get-port-channel-information-by-id
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

        e_url = "/dna/intent/api/v1/lanAutomation/portChannels/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e149c0cd53b8b8998d82fd3dc1d1_v3_1_3_0", json_data
        )

    def delete_port_channel(self, id, headers=None, **request_parameters):
        """This API deletes a Port Channel between LAN Automation associated devices using a valid Port Channel ID. .

        Args:
            id(str): id path parameter. ID of the port channel. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
            https://developer.cisco.com/docs/dna-center/#!delete-port-channel
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

        e_url = "/dna/intent/api/v1/lanAutomation/portChannels/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bec4a00bb2bf5a63a75f745862904e4d_v3_1_3_0", json_data
        )

    def add_a_lan_automated_link_to_a_port_channel(
        self,
        id,
        portChannelMembers=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API adds a new LAN Automated link as a member to an existing Port Channel, provided the interface is in UP
        state and already LAN Automated. .

        Args:
            portChannelMembers(list): LAN Automation's portChannelMembers (list of objects).
            id(str): id path parameter. ID of the port channel. .
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
            https://developer.cisco.com/docs/dna-center/#!add-a-l-a-n-automated-link-to-a-port-channel
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
            "portChannelMembers": portChannelMembers,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fa8fb3bdbffe5958858f20447dcb3ca5_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/lanAutomation/portChannels/{id}/addLi" + "nk"
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
            "bpm_fa8fb3bdbffe5958858f20447dcb3ca5_v3_1_3_0", json_data
        )

    def remove_a_link_from_port_channel(
        self,
        id,
        portChannelMembers=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API removes a member link from an existing Port Channel, reverting the link to a P2P L3 interface. .

        Args:
            portChannelMembers(list): LAN Automation's portChannelMembers (list of objects).
            id(str): id path parameter. ID of the port channel. .
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
            https://developer.cisco.com/docs/dna-center/#!remove-a-link-from-port-channel
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
            "portChannelMembers": portChannelMembers,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fb433ea1bbc5dc49dce4fde0a04e5ed_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/lanAutomation/portChannels/{id}/remov" + "eLink"
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
            "bpm_fb433ea1bbc5dc49dce4fde0a04e5ed_v3_1_3_0", json_data
        )

    def lan_automation_start_v2(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Invoke V2 LAN Automation Start API, which supports optional auto-stop processing feature based on the provided
        timeout or a specific device list, or both. The stop processing will be executed automatically when
        either of the cases is satisfied, without specifically calling the stop API. The V2 API behaves
        similarly to V1 if no timeout or device list is provided, and the user needs to call the stop API for
        LAN Automation stop processing. With the V2 API, the user can also specify the level up to which the
        devices can be LAN automated. .

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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-start-v2
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
                "jsd_dc5d352dfaeb5b17800b0af2858c2f5c_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/lan-automation"
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
            "bpm_dc5d352dfaeb5b17800b0af2858c2f5c_v3_1_3_0", json_data
        )

    def lan_automation_stop_and_update_devices_v2(
        self,
        id,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Invoke this API to stop LAN Automation and update device parameters such as Loopback0 IP address and/or hostname
        discovered in the current session. .

        Args:
            id(str): id path parameter. LAN Automation id can be obtained from /dna/intent/api/v1/lan-
                automation/status. .
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
            https://developer.cisco.com/docs/dna-center/#!l-a-n-automation-stop-and-update-devices-v2
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator("jsd_ad0cb5a12a76384ba4644e55e_v3_1_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/lan-automation/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_ad0cb5a12a76384ba4644e55e_v3_1_3_0", json_data)


# Alias Functions

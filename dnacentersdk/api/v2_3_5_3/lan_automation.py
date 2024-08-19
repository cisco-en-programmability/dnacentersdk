# -*- coding: utf-8 -*-
"""Cisco DNA Center LAN Automation API wrapper.

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


class LanAutomation(object):
    """Cisco DNA Center LAN Automation API (version: 2.3.5.3).

    Wraps the DNA Center LAN Automation
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new LanAutomation
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(LanAutomation, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def lan_automation_start(self,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **request_parameters):
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!lan-automation-start
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_b119a4d455e35cc3b2cc6695a045cbfa_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/lan-automation')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_b119a4d455e35cc3b2cc6695a045cbfa_v2_3_5_3', json_data)

    def start(self,
              headers=None,
              payload=None,
              active_validation=True,
              **query_parameters):
        """Alias for `lan_automation_start <#dnacentersdk.
        api.v2_3_5_3.lan_automation.
        LanAutomation.lan_automation_start>`_
        """
        return self.lan_automation_start(
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def lan_automation_session_count(self,
                                     headers=None,
                                     **request_parameters):
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!lan-automation-session-count
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

        e_url = ('/dna/intent/api/v1/lan-automation/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_eea014edd5807925df3a414a92ed4_v2_3_5_3', json_data)

    def session_count(self,
                      headers=None,
                      **query_parameters):
        """Alias for `lan_automation_session_count <#dnacentersdk.
        api.v2_3_5_3.lan_automation.
        LanAutomation.lan_automation_session_count>`_
        """
        return self.lan_automation_session_count(
            headers=headers,
            **query_parameters
        )

    def lan_automation_log(self,
                           limit=None,
                           offset=None,
                           headers=None,
                           **request_parameters):
        """Invoke this API to get the LAN Automation session logs. .

        Args:
            offset(int,str): offset query parameter. Starting index of the LAN Automation session. Minimum value is 1. .
            limit(int,str): limit query parameter. Number of LAN Automation sessions to be retrieved. Limit value can
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!lan-automation-log
        """
        check_type(headers, dict)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
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

        e_url = ('/dna/intent/api/v1/lan-automation/log')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e37f6c9650b68e0aaac866a162cf_v2_3_5_3', json_data)

    def log(self,
            limit=None,
            offset=None,
            headers=None,
            **query_parameters):
        """Alias for `lan_automation_log <#dnacentersdk.
        api.v2_3_5_3.lan_automation.
        LanAutomation.lan_automation_log>`_
        """
        return self.lan_automation_log(
            limit=limit,
            offset=offset,
            headers=headers,
            **query_parameters
        )

    def lan_automation_log_by_id(self,
                                 id,
                                 headers=None,
                                 **request_parameters):
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!lan-automation-log-by-id
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

        e_url = ('/dna/intent/api/v1/lan-automation/log/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e98b744fde50a1b53761251c43bfb0_v2_3_5_3', json_data)

    def log_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `lan_automation_log_by_id <#dnacentersdk.
        api.v2_3_5_3.lan_automation.
        LanAutomation.lan_automation_log_by_id>`_
        """
        return self.lan_automation_log_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def lan_automation_logs_for_individual_devices(self,
                                                   id,
                                                   serial_number,
                                                   log_level=None,
                                                   headers=None,
                                                   **request_parameters):
        """Invoke this API to get the LAN Automation session logs for individual devices based on the given LAN Automation
        session id and device serial number.  .

        Args:
            id(str): id path parameter. LAN Automation session identifier. .
            serial_number(str): serialNumber path parameter. Device serial number. .
            log_level(str): logLevel query parameter. Supported levels are ERROR, INFO, WARNING, TRACE,
                CONFIG and ALL. Specifying ALL will display device specific logs with the exception of
                CONFIG logs. In order to view CONFIG logs along with the remaining logs, please leave
                the query parameter blank. .
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
            https://developer.cisco.com/docs/dna-center/#!lan-automation-logs-for-individual-devices
        """
        check_type(headers, dict)
        check_type(log_level, str)
        check_type(id, str,
                   may_be_none=False)
        check_type(serial_number, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'logLevel':
                log_level,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
            'serialNumber': serial_number,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/lan-'
                 + 'automation/log/{id}/{serialNumber}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c3441f7507a98d02579c25814f4_v2_3_5_3', json_data)

    def lan_automation_active_sessions(self,
                                       headers=None,
                                       **request_parameters):
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!lan-automation-active-sessions
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

        e_url = ('/dna/intent/api/v1/lan-automation/sessions')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a19cf2241e75c648220d7172e9e4013_v2_3_5_3', json_data)

    def lan_automation_status(self,
                              limit=None,
                              offset=None,
                              headers=None,
                              **request_parameters):
        """Invoke this API to get the LAN Automation session status.  .

        Args:
            offset(int,str): offset query parameter. Starting index of the LAN Automation session. Minimum value is 1. .
            limit(int,str): limit query parameter. Number of LAN Automation sessions to be retrieved. Limit value can
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!lan-automation-status
        """
        check_type(headers, dict)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
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

        e_url = ('/dna/intent/api/v1/lan-automation/status')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c56a6c58fd5b71b7949036855ee25b_v2_3_5_3', json_data)

    def status(self,
               limit=None,
               offset=None,
               headers=None,
               **query_parameters):
        """Alias for `lan_automation_status <#dnacentersdk.
        api.v2_3_5_3.lan_automation.
        LanAutomation.lan_automation_status>`_
        """
        return self.lan_automation_status(
            limit=limit,
            offset=offset,
            headers=headers,
            **query_parameters
        )

    def lan_automation_status_by_id(self,
                                    id,
                                    headers=None,
                                    **request_parameters):
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!lan-automation-status-by-id
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

        e_url = ('/dna/intent/api/v1/lan-automation/status/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d5727c4bdb1056308cd10e99dff2acb8_v2_3_5_3', json_data)

    def status_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `lan_automation_status_by_id <#dnacentersdk.
        api.v2_3_5_3.lan_automation.
        LanAutomation.lan_automation_status_by_id>`_
        """
        return self.lan_automation_status_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def lan_automation_stop(self,
                            id,
                            headers=None,
                            **request_parameters):
        """Invoke this API to stop LAN Automation for the given site.  .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!lan-automation-stop
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

        e_url = ('/dna/intent/api/v1/lan-automation/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ed815ca3e5ab5ae48720795217ec776b_v2_3_5_3', json_data)

    def stop(self,
             id,
             headers=None,
             **query_parameters):
        """Alias for `lan_automation_stop <#dnacentersdk.
        api.v2_3_5_3.lan_automation.
        LanAutomation.lan_automation_stop>`_
        """
        return self.lan_automation_stop(
            id=id,
            headers=headers,
            **query_parameters
        )

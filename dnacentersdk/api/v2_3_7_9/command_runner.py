# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Command Runner API wrapper.

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


class CommandRunner(object):
    """Cisco Catalyst Center Command Runner API (version: 2.3.7.9).

    Wraps the Catalyst Center Command Runner
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new CommandRunner
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(CommandRunner, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_all_keywords_of_clis_accepted_by_command_runner_v1(self,
                                          headers=None,
                                          **request_parameters):
        """Get valid keywords .

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
            https://developer.cisco.com/docs/dna-center/#!get-all-keywords-of-c-l-is-accepted-by-command-runner
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

        e_url = ('/dna/intent/api/v1/network-device-poller/cli/legit-reads')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e946adf864590082fe3111a2a2fa74_v2_3_7_9', json_data)

    def run_read_only_commands_on_devices_to_get_their_real_time_configuration_v1(self,
                                          commands=None,
                                          description=None,
                                          deviceUuids=None,
                                          name=None,
                                          timeout=None,
                                          headers=None,
                                          payload=None,
                                          active_validation=True,
                                          **request_parameters):
        """Submit request for read-only CLIs .

        Args:
            commands(list): Command Runner's Commands to be executed  (list of strings).
            description(string): Command Runner's Describe the details about the command request .
            deviceUuids(list): Command Runner's Device Id of the device  (list of strings).
            name(string): Command Runner's Name of the the request like getshowrun , deviceinterfacestatusCli. .
            timeout(integer): Command Runner's The timeout value in unit of second. If no timeout provided wait till
                300sec .
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
            https://developer.cisco.com/docs/dna-center/#!run-read-only-commands-on-devices-to-get-their-real-time-configuration
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
            'commands':
                commands,
            'description':
                description,
            'deviceUuids':
                deviceUuids,
            'name':
                name,
            'timeout':
                timeout,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_b2dae3b41636596aa02c3ad0a4bcb8d7_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device-poller/cli/read-'
                 + 'request')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_b2dae3b41636596aa02c3ad0a4bcb8d7_v2_3_7_9', json_data)



    # Alias Function
    def get_all_keywords_of_clis_accepted_by_command_runner(self,
                                          headers=None,
                                          **request_parameters):
        """ This function is an alias of get_all_keywords_of_clis_accepted_by_command_runner_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_all_keywords_of_clis_accepted_by_command_runner_v1 .
        """
        return self.get_all_keywords_of_clis_accepted_by_command_runner_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def run_read_only_commands_on_devices_to_get_their_real_time_configuration(self,
                                          commands=None,
                                          description=None,
                                          deviceUuids=None,
                                          name=None,
                                          timeout=None,
                                          headers=None,
                                          payload=None,
                                          active_validation=True,
                                          **request_parameters):
        """ This function is an alias of run_read_only_commands_on_devices_to_get_their_real_time_configuration_v1 .
        Args:
            commands(list): Command Runner's Commands to be executed  (list of strings).
            description(string): Command Runner's Describe the details about the command request .
            deviceUuids(list): Command Runner's Device Id of the device  (list of strings).
            name(string): Command Runner's Name of the the request like getshowrun , deviceinterfacestatusCli. .
            timeout(integer): Command Runner's The timeout value in unit of second. If no timeout provided wait till
                300sec .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of run_read_only_commands_on_devices_to_get_their_real_time_configuration_v1 .
        """
        return self.run_read_only_commands_on_devices_to_get_their_real_time_configuration_v1(
                    commands=commands,
                    description=description,
                    deviceUuids=deviceUuids,
                    name=name,
                    timeout=timeout,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )



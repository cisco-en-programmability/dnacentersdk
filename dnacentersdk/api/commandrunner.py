# -*- coding: utf-8 -*-
"""DNA Center Command Runner API wrapper.

Copyright (c) 2019 Cisco and/or its affiliates.

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

from ..generator_containers import generator_container
from ..restsession import RestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_filt,
)

class CommandRunner( object ):
    """DNA Center Command Runner API.

    Wraps the DNA Center Command Runner API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new CommandRunner object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(CommandRunner, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator


    # Get all keywords of CLIs accepted by command runner
    def get_all_keywords_of_clis_accepted_by_command_runner(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_33bb2b9d40199e14').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device-poller/cli/legit-reads', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device-poller/cli/legit-reads', path_params), params=params, json=payload)

        return self._object_factory('bpm_33bb2b9d40199e14', json_data)


    # Run read-only commands on devices to get their real-time configuration
    def run_read_only_commands_on_devices_to_get_their_real_time_configuration(self, rq_commands = None, rq_description = None, rq_deviceUuids = None, rq_name = None, rq_timeout = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_commands is not None: payload.update( { 'commands':  rq_commands })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_deviceUuids is not None: payload.update( { 'deviceUuids':  rq_deviceUuids })
        if rq_name is not None: payload.update( { 'name':  rq_name })
        if rq_timeout is not None: payload.update( { 'timeout':  rq_timeout })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_d6b8ca774739adf4').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/api/v1/network-device-poller/cli/read-request', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/api/v1/network-device-poller/cli/read-request', path_params), params=params, json=payload)

        return self._object_factory('bpm_d6b8ca774739adf4', json_data)



# -*- coding: utf-8 -*-
"""DNA Center Sites API wrapper.

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

class Sites( object ):
    """DNA Center Sites API.

    Wraps the DNA Center Sites API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Sites object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Sites, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator


    # Get Site Health
    def get_site_health(self, param_timestamp, headers=None,payload=None,**request_parameters):
        check_type( param_timestamp, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'timestamp': param_timestamp,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_17a82ac94cf99ab0').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/site-health', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/site-health', path_params), params=params, json=payload)

        return self._object_factory('bpm_17a82ac94cf99ab0', json_data)


    # Assign Device To Site
    def assign_device_to_site(self, path_param_site_id, rq_device = None, headers=None,payload=None,**request_parameters):
        check_type( path_param_site_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('__runsync', self._session.headers.get('__runsync')), bool, may_be_none=False)
            check_type( headers.get('__persistbapioutput', self._session.headers.get('__persistbapioutput')), bool, may_be_none=False)
            check_type( headers.get('__timeout', self._session.headers.get('__timeout')), int)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'siteId': path_param_site_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_device is not None: payload.update( { 'device':  rq_device })
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_eeb168eb41988e07').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/site/${siteId}/device', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/site/${siteId}/device', path_params), params=params, json=payload)

        return self._object_factory('bpm_eeb168eb41988e07', json_data)


    # Create Site
    def create_site(self, rq_site = None, rq_type = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('__runsync', self._session.headers.get('__runsync')), bool, may_be_none=False)
            check_type( headers.get('__timeout', self._session.headers.get('__timeout')), int)
            check_type( headers.get('__persistbapioutput', self._session.headers.get('__persistbapioutput')), bool, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_type is not None: payload.update( { 'type':  rq_type })
        if rq_site is not None: payload.update( { 'site':  rq_site })
        payload.update( dict_filt(request_parameters, 'payload') )

        print("validate: ", self._request_validator('jsd_50b589fd4c7a930a').validate(payload) )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/system/api/v1/site', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/system/api/v1/site', path_params), params=params, json=payload)

        return self._object_factory('bpm_50b589fd4c7a930a', json_data)



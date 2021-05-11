# -*- coding: utf-8 -*-
"""DNA Center Applications API wrapper.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_of_str,
)


class Applications(object):
    """DNA Center Applications API (version: 2.1.2).

    Wraps the DNA Center Applications
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Applications
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Applications, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def applications(self,
                     application_health=None,
                     device_id=None,
                     end_time=None,
                     limit=None,
                     mac_address=None,
                     offset=None,
                     site_id=None,
                     start_time=None,
                     headers=None,
                     **request_parameters):
        """Intent API to get a list of applications for a specific site, a
        device, or a client device's MAC address.

        Args:
            site_id(basestring): Assurance site UUID value (Cannot
                be submitted together with deviceId and
                clientMac).
            device_id(basestring): Assurance device UUID value
                (Cannot be submitted together with
                siteId and clientMac).
            mac_address(basestring): Client device's MAC address
                (Cannot be submitted together with
                siteId and deviceId).
            start_time(int): Starting epoch time in milliseconds of
                time window.
            end_time(int): Ending epoch time in milliseconds of time
                window.
            application_health(basestring): Application health
                category (POOR, FAIR, or GOOD.
                Optionally use with siteId only).
            offset(int): The offset of the first application in the
                returned data (optionally used with
                siteId only).
            limit(int): The max number of application entries in
                returned data [1, 1000] (optionally used
                with siteId only).
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
        """
        check_type(headers, dict)
        check_type(site_id, basestring)
        check_type(device_id, basestring)
        check_type(mac_address, basestring)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(application_health, basestring)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'siteId':
                site_id,
            'deviceId':
                device_id,
            'macAddress':
                mac_address,
            'startTime':
                start_time,
            'endTime':
                end_time,
            'applicationHealth':
                application_health,
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

        e_url = ('/dna/intent/api/v1/application-health')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_2db58a1f4fea9242_v2_1_2', json_data)
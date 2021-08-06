# -*- coding: utf-8 -*-
"""Cisco DNA Center Site Profile API wrapper.

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


class SiteProfile(object):
    """Cisco DNA Center Site Profile API (version: 1.2.10).

    Wraps the DNA Center Site Profile
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SiteProfile
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SiteProfile, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_device_details_by_ip(self,
                                 device_ip,
                                 headers=None,
                                 **request_parameters):
        """**Beta** - Returns provisioning device information for the
        specified IP address.

        Args:
            device_ip(basestring): Device to which the provisioning detail has to be retrieved.
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
        check_type(device_ip, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'deviceIp':
                device_ip,
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

        e_url = ('/dna/intent/api/v1/business/nfv/provisioningDetail')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_7fbe4b804879baa4_v1_2_10', json_data)

    def provision_nfv(self,
                      callbackUrl=None,
                      provisioning=None,
                      siteProfile=None,
                      headers=None,
                      payload=None,
                      active_validation=True,
                      **request_parameters):
        """Design and Provision single/multi NFV device with given
        site/area/building/floor .

        Args:
            callbackUrl(string): Callback Url, property of the request body.
            provisioning(list): Provisioning, property of the request body (list of objects).
            siteProfile(list): Site Profile, property of the request body (list of objects).
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if '__runsync' in headers:
                check_type(headers.get('__runsync'),
                           bool, may_be_none=False)
            if '__persistbapioutput' in headers:
                check_type(headers.get('__persistbapioutput'),
                           bool, may_be_none=False)
            if '__timeout' in headers:
                check_type(headers.get('__timeout'),
                           int)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = {
            'siteProfile':
                siteProfile,
            'provisioning':
                provisioning,
            'callbackUrl':
                callbackUrl,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_828828f44f28bd0d_v1_2_10')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/nfv')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_828828f44f28bd0d_v1_2_10', json_data)

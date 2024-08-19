# -*- coding: utf-8 -*-
"""Cisco DNA Center Configuration Archive API wrapper.

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


class ConfigurationArchive(object):
    """Cisco DNA Center Configuration Archive API (version: 2.3.7.6).

    Wraps the DNA Center Configuration Archive
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new ConfigurationArchive
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(ConfigurationArchive, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def export_device_configurations(self,
                                     deviceId=None,
                                     password=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **request_parameters):
        """Export Device configurations to an encrypted zip file .

        Args:
            deviceId(string): Configuration Archive's UUIDs of the devices for which configurations need to be
                exported.  .
            password(string): Configuration Archive's Password for the zip file to protect exported configurations.
                Must contain, at minimum 8 characters, one lowercase letter, one uppercase letter, one
                number, one special character(-=[];,./~!@#$%^&*()_+{}|:?). It may not contain white
                space or the characters <>. .
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
            'password':
                password,
            'deviceId':
                deviceId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e85b40c5ca055f4c82281617a8f95644_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device-archive/cleartext')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e85b40c5ca055f4c82281617a8f95644_v2_3_7_6', json_data)

    def get_configuration_archive_details(self,
                                          created_by=None,
                                          created_time=None,
                                          device_id=None,
                                          file_type=None,
                                          limit=None,
                                          offset=None,
                                          headers=None,
                                          **request_parameters):
        """Returns the historical device configurations (running configuration , startup configuration , vlan if
        applicable) by specified criteria .

        Args:
            device_id(str): deviceId query parameter. comma separated device id for example
                cf35b0a1-407f-412f-b2f4-f0c3156695f9,aaa38191-0c22-4158-befd-779a09d7cec1 . if device id
                is not provided it will fetch for all devices .
            file_type(str): fileType query parameter. Config File Type can be RUNNINGCONFIG or STARTUPCONFIG
                .
            created_time(str): createdTime query parameter. Supported with logical filters GT,GTE,LT,LTE & BT
                : time in milliseconds (epoc format) .
            created_by(str): createdBy query parameter. Comma separated values for createdBy SCHEDULED, USER,
                CONFIG_CHANGE_EVENT, SCHEDULED_FIRST_TIME, DR_CALL_BACK, PRE_DEPLOY .
            offset(int,str): offset query parameter.
            limit(int,str): limit query parameter.
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
        """
        check_type(headers, dict)
        check_type(device_id, str)
        check_type(file_type, str)
        check_type(created_time, str)
        check_type(created_by, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceId':
                device_id,
            'fileType':
                file_type,
            'createdTime':
                created_time,
            'createdBy':
                created_by,
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

        e_url = ('/dna/intent/api/v1/network-device-config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ff699112d3854d99557dc1f48987f09_v2_3_7_6', json_data)

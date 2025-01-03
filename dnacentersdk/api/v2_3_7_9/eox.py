# -*- coding: utf-8 -*-
"""Cisco Catalyst Center EoX API wrapper.

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


class EoX(object):
    """Cisco Catalyst Center EoX API (version: 2.3.7.9).

    Wraps the Catalyst Center EoX
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new EoX
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(EoX, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_eox_status_for_all_devices_v1(self,
                                          limit=None,
                                          offset=None,
                                          headers=None,
                                          **request_parameters):
        """Retrieves EoX status for all devices in the network .

        Args:
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
            offset(int): offset query parameter. The first record to show for this page, the first record is
                numbered 1 .
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
            https://developer.cisco.com/docs/dna-center/#!get-eo-x-status-for-all-devices
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
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

        e_url = ('/dna/intent/api/v1/eox-status/device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d5d27a53ac53258fa2183b7e93a7d5_v2_3_7_9', json_data)

    def get_eox_details_per_device_v1(self,
                                      device_id,
                                      headers=None,
                                      **request_parameters):
        """Retrieves EoX details for a device .

        Args:
            device_id(str): deviceId path parameter. Device instance UUID .
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
            https://developer.cisco.com/docs/dna-center/#!get-eo-x-details-per-device
        """
        check_type(headers, dict)
        check_type(device_id, str,
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
            'deviceId': device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/eox-status/device/{deviceId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ec048832853f8a63f34415d0e6fce_v2_3_7_9', json_data)

    def get_eox_summary_v1(self,
                           headers=None,
                           **request_parameters):
        """Retrieves EoX summary for all devices in the network .

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
            https://developer.cisco.com/docs/dna-center/#!get-eo-x-summary
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

        e_url = ('/dna/intent/api/v1/eox-status/summary')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f0a0dfdaca465bdc91fc290d87476b89_v2_3_7_9', json_data)



    # Alias Function
    def get_eox_details_per_device(self,
                                      device_id,
                                      headers=None,
                                      **request_parameters):
        """ This function is an alias of get_eox_details_per_device_v1 .
        Args:
            device_id(str): deviceId path parameter. Device instance UUID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_eox_details_per_device_v1 .
        """
        return self.get_eox_details_per_device_v1(
                    device_id=device_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_eox_status_for_all_devices(self,
                                          limit=None,
                                          offset=None,
                                          headers=None,
                                          **request_parameters):
        """ This function is an alias of get_eox_status_for_all_devices_v1 .
        Args:
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500. .
            offset(int): offset query parameter. The first record to show for this page, the first record is
                numbered 1 .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_eox_status_for_all_devices_v1 .
        """
        return self.get_eox_status_for_all_devices_v1(
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_eox_summary(self,
                           headers=None,
                           **request_parameters):
        """ This function is an alias of get_eox_summary_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_eox_summary_v1 .
        """
        return self.get_eox_summary_v1(
                    headers=headers,
                    **request_parameters
        )



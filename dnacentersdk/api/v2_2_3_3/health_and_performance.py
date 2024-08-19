# -*- coding: utf-8 -*-
"""Cisco DNA Center Health and Performance API wrapper.

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


class HealthAndPerformance(object):
    """Cisco DNA Center Health and Performance API (version: 2.2.3.3).

    Wraps the DNA Center Health and Performance
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new HealthAndPerformance
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(HealthAndPerformance, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def system_health(self,
                      domain=None,
                      limit=None,
                      offset=None,
                      subdomain=None,
                      summary=None,
                      headers=None,
                      **request_parameters):
        """This API retrieves the latest system events  .

        Args:
            summary(bool): summary query parameter. Fetch the latest high severity event .
            domain(str): domain query parameter. Fetch system events with this domain. Possible values of
                domain are listed here : /dna/platform/app/consumer-portal/developer-toolkit/events .
            subdomain(str): subdomain query parameter. Fetch system events with this subdomain. Possible
                values of subdomain are listed here : /dna/platform/app/consumer-portal/developer-
                toolkit/events .
            limit(int,str): limit query parameter.
            offset(int,str): offset query parameter.
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
        check_type(summary, bool)
        check_type(domain, str)
        check_type(subdomain, str)
        check_type(limit, (int, str))
        check_type(offset, (int, str))
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'summary':
                summary,
            'domain':
                domain,
            'subdomain':
                subdomain,
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

        e_url = ('/dna/intent/api/v1/diagnostics/system/health')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d0acccfae6885bc28f8f39c67f4acfc1_v2_2_3_3', json_data)

    def system_health_count(self,
                            domain=None,
                            subdomain=None,
                            headers=None,
                            **request_parameters):
        """This API gives the count of the latest system events .

        Args:
            domain(str): domain query parameter. Fetch system events with this domain. Possible values of
                domain are listed here : /dna/platform/app/consumer-portal/developer-toolkit/events .
            subdomain(str): subdomain query parameter. Fetch system events with this subdomain. Possible
                values of subdomain are listed here : /dna/platform/app/consumer-portal/developer-
                toolkit/events .
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
        check_type(domain, str)
        check_type(subdomain, str)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'domain':
                domain,
            'subdomain':
                subdomain,
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

        e_url = ('/dna/intent/api/v1/diagnostics/system/health/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f6dd603bc35db1948f31c782a37647_v2_2_3_3', json_data)

    def system_performance(self,
                           end_time=None,
                           function=None,
                           kpi=None,
                           start_time=None,
                           headers=None,
                           **request_parameters):
        """This API gives the aggregated performance indicators. The data can be retrieved for the last 3 months. .

        Args:
            kpi(str): kpi query parameter. Valid values: cpu,memory,network .
            function(str): function query parameter. Valid values: sum,average,max .
            start_time(int): startTime query parameter. This is the epoch start time in milliseconds from which
                performance indicator need to be fetched .
            end_time(int): endTime query parameter. This is the epoch end time in milliseconds upto which
                performance indicator need to be fetched .
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
        check_type(kpi, str)
        check_type(function, str)
        check_type(start_time, int)
        check_type(end_time, int)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'kpi':
                kpi,
            'function':
                function,
            'startTime':
                start_time,
            'endTime':
                end_time,
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

        e_url = ('/dna/intent/api/v1/diagnostics/system/performance')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cfcb7a875f215cb4ba59be38abb871e6_v2_2_3_3', json_data)

    def system_performance_historical(self,
                                      end_time=None,
                                      kpi=None,
                                      start_time=None,
                                      headers=None,
                                      **request_parameters):
        """This API retrieves the historical performance indicators . The data can be retrieved for the last 3 months. .

        Args:
            kpi(str): kpi query parameter. Fetch historical data for this kpi. Valid values:
                cpu,memory,network .
            start_time(int): startTime query parameter. This is the epoch start time in milliseconds from which
                performance indicator need to be fetched .
            end_time(int): endTime query parameter. This is the epoch end time in milliseconds upto which
                performance indicator need to be fetched .
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
        check_type(kpi, str)
        check_type(start_time, int)
        check_type(end_time, int)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'kpi':
                kpi,
            'startTime':
                start_time,
            'endTime':
                end_time,
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

        e_url = ('/dna/intent/api/v1/diagnostics/system/performance/histor'
                 + 'y')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f131d712dc253dca528c0298b3e41c6_v2_2_3_3', json_data)

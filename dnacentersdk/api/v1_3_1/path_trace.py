# -*- coding: utf-8 -*-
"""DNA Center Path Trace API wrapper.

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


class PathTrace(object):
    """DNA Center Path Trace API (version: 1.3.1).

    Wraps the DNA Center Path Trace
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new PathTrace
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(PathTrace, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def deletes_pathtrace_by_id(self,
                                flow_analysis_id,
                                headers=None,
                                **request_parameters):
        """Deletes a flow analysis request by its id.

        Args:
            flow_analysis_id(basestring): Flow analysis request id.
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
        check_type(flow_analysis_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'flowAnalysisId': flow_analysis_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/flow-analysis/${flowAnalysisId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=params)

        return self._object_factory('bpm_8a9d2b76443b914e_v1_3_1', json_data)

    def retrieves_previous_pathtrace(self,
                                     flow_analysis_id,
                                     headers=None,
                                     **request_parameters):
        """Returns result of a previously requested flow analysis by its
        Flow Analysis id.

        Args:
            flow_analysis_id(basestring): Flow analysis request id.
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
        check_type(flow_analysis_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'flowAnalysisId': flow_analysis_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/flow-analysis/${flowAnalysisId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_7ab9a8bd4f3b86a4_v1_3_1', json_data)

    def retrives_all_previous_pathtraces_summary(self,
                                                 dest_ip=None,
                                                 dest_port=None,
                                                 gt_create_time=None,
                                                 last_update_time=None,
                                                 limit=None,
                                                 lt_create_time=None,
                                                 offset=None,
                                                 order=None,
                                                 periodic_refresh=None,
                                                 protocol=None,
                                                 sort_by=None,
                                                 source_ip=None,
                                                 source_port=None,
                                                 status=None,
                                                 task_id=None,
                                                 headers=None,
                                                 **request_parameters):
        """Returns a summary of all flow analyses stored. Results can be
        filtered by specified parameters.

        Args:
            periodic_refresh(bool): Is analysis periodically
                refreshed?.
            source_ip(basestring): Source IP address.
            dest_ip(basestring): Destination IP address.
            source_port(basestring): Source port.
            dest_port(basestring): Destination port.
            gt_create_time(basestring): Analyses requested after
                this time.
            lt_create_time(basestring): Analyses requested before
                this time.
            protocol(basestring): protocol query parameter.
            status(basestring): status query parameter.
            task_id(basestring): Task ID.
            last_update_time(basestring): Last update time.
            limit(basestring): Number of resources returned.
            offset(basestring): Start index of resources returned
                (1-based).
            order(basestring): Order by this field.
            sort_by(basestring): Sort by this field.
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
        check_type(periodic_refresh, bool)
        check_type(source_ip, basestring)
        check_type(dest_ip, basestring)
        check_type(source_port, basestring)
        check_type(dest_port, basestring)
        check_type(gt_create_time, basestring)
        check_type(lt_create_time, basestring)
        check_type(protocol, basestring)
        check_type(status, basestring)
        check_type(task_id, basestring)
        check_type(last_update_time, basestring)
        check_type(limit, basestring)
        check_type(offset, basestring)
        check_type(order, basestring)
        check_type(sort_by, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'periodicRefresh':
                periodic_refresh,
            'sourceIP':
                source_ip,
            'destIP':
                dest_ip,
            'sourcePort':
                source_port,
            'destPort':
                dest_port,
            'gtCreateTime':
                gt_create_time,
            'ltCreateTime':
                lt_create_time,
            'protocol':
                protocol,
            'status':
                status,
            'taskId':
                task_id,
            'lastUpdateTime':
                last_update_time,
            'limit':
                limit,
            'offset':
                offset,
            'order':
                order,
            'sortBy':
                sort_by,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/flow-analysis')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_55bc3bf94e38b6ff_v1_3_1', json_data)

    def initiate_a_new_pathtrace(self,
                                 controlPath=None,
                                 destIP=None,
                                 destPort=None,
                                 inclusions=None,
                                 periodicRefresh=None,
                                 protocol=None,
                                 sourceIP=None,
                                 sourcePort=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **request_parameters):
        """Initiates a new flow analysis with periodic refresh and stat
        collection options. Returns a request id and a task id
        to get results and follow progress.

        Args:
            controlPath(boolean): FlowAnalysisRequest's controlPath.
            destIP(string): FlowAnalysisRequest's destIP.
            destPort(string): FlowAnalysisRequest's destPort.
            inclusions(list): FlowAnalysisRequest's inclusions (list
                of strings).
            periodicRefresh(boolean): FlowAnalysisRequest's
                periodicRefresh.
            protocol(string): FlowAnalysisRequest's protocol.
            sourceIP(string): FlowAnalysisRequest's sourceIP.
            sourcePort(string): FlowAnalysisRequest's sourcePort.
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
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
            'controlPath':
                controlPath,
            'destIP':
                destIP,
            'destPort':
                destPort,
            'inclusions':
                inclusions,
            'periodicRefresh':
                periodicRefresh,
            'protocol':
                protocol,
            'sourceIP':
                sourceIP,
            'sourcePort':
                sourcePort,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a395fae644ca899c_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/flow-analysis')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload)

        return self._object_factory('bpm_a395fae644ca899c_v1_3_1', json_data)

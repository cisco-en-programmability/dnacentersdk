# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Path Trace API wrapper.

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


class PathTrace(object):
    """Cisco Catalyst Center Path Trace API (version: 2.3.7.9).

    Wraps the Catalyst Center Path Trace
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new PathTrace
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(PathTrace, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def retrieves_all_previous_pathtraces_summary_v1(self,
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
        """Returns a summary of all flow analyses stored. Results can be filtered by specified parameters. .

        Args:
            periodic_refresh(bool): periodicRefresh query parameter. Is analysis periodically refreshed? .
            source_ip(str): sourceIP query parameter. Source IP address .
            dest_ip(str): destIP query parameter. Destination IP address .
            source_port(int): sourcePort query parameter. Source port .
            dest_port(int): destPort query parameter. Destination port .
            gt_create_time(int): gtCreateTime query parameter. Analyses requested after this time .
            lt_create_time(int): ltCreateTime query parameter. Analyses requested before this time .
            protocol(str): protocol query parameter.
            status(str): status query parameter.
            task_id(str): taskId query parameter. Task ID .
            last_update_time(int): lastUpdateTime query parameter. Last update time .
            limit(int): limit query parameter. Number of resources returned .
            offset(int): offset query parameter. Start index of resources returned (1-based) .
            order(str): order query parameter. Order by this field .
            sort_by(str): sortBy query parameter. Sort by this field .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-all-previous-pathtraces-summary
        """
        check_type(headers, dict)
        check_type(periodic_refresh, bool)
        check_type(source_ip, str)
        check_type(dest_ip, str)
        check_type(source_port, int)
        check_type(dest_port, int)
        check_type(gt_create_time, int)
        check_type(lt_create_time, int)
        check_type(protocol, str)
        check_type(status, str)
        check_type(task_id, str)
        check_type(last_update_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(order, str)
        check_type(sort_by, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
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
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

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
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a75e4b27171c5c6782e84f902da9e5be_v2_3_7_9', json_data)

    def initiate_a_new_pathtrace_v1(self,
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
        """Initiates a new flow analysis with periodic refresh and stat collection options. Returns a request id and a task
        id to get results and follow progress. .

        Args:
            controlPath(boolean): Path Trace's Control path tracing .
            destIP(string): Path Trace's Destination IP address .
            destPort(string): Path Trace's Destination Port, range: 1-65535 .
            inclusions(list): Path Trace's Subset of {INTERFACE-STATS, QOS-STATS, DEVICE-STATS, PERFORMANCE-STATS,
                ACL-TRACE}  (list of strings).
            periodicRefresh(boolean): Path Trace's Periodic refresh of path for every 30 sec .
            protocol(string): Path Trace's Protocol one of [TCP, UDP] checks both when left blank .
            sourceIP(string): Path Trace's Source IP address .
            sourcePort(string): Path Trace's Source Port, range: 1-65535 .
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
            https://developer.cisco.com/docs/dna-center/#!initiate-a-new-pathtrace
        """
        check_type(headers, dict)
        check_type(payload, dict)
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
            self._request_validator('jsd_a54fce1a0c305bdabfe91a8a6161e539_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/flow-analysis')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a54fce1a0c305bdabfe91a8a6161e539_v2_3_7_9', json_data)

    def retrieves_previous_pathtrace_v1(self,
                                        flow_analysis_id,
                                        headers=None,
                                        **request_parameters):
        """Returns result of a previously requested flow analysis by its Flow Analysis id .

        Args:
            flow_analysis_id(str): flowAnalysisId path parameter. Flow analysis request id .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-previous-pathtrace
        """
        check_type(headers, dict)
        check_type(flow_analysis_id, str,
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
            'flowAnalysisId': flow_analysis_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/flow-analysis/{flowAnalysisId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ed5cbafc332a5efa97547736ba8b6044_v2_3_7_9', json_data)

    def deletes_pathtrace_by_id_v1(self,
                                   flow_analysis_id,
                                   headers=None,
                                   **request_parameters):
        """Deletes a flow analysis request by its id .

        Args:
            flow_analysis_id(str): flowAnalysisId path parameter. Flow analysis request id .
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
            https://developer.cisco.com/docs/dna-center/#!deletes-pathtrace-by-id
        """
        check_type(headers, dict)
        check_type(flow_analysis_id, str,
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
            'flowAnalysisId': flow_analysis_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/flow-analysis/{flowAnalysisId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a7ae984f943507ba621abe155e6e744_v2_3_7_9', json_data)



    # Alias Function
    def retrieves_previous_pathtrace(self,
                                        flow_analysis_id,
                                        headers=None,
                                        **request_parameters):
        """ This function is an alias of retrieves_previous_pathtrace_v1 .
        Args:
            flow_analysis_id(str): flowAnalysisId path parameter. Flow analysis request id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_previous_pathtrace_v1 .
        """
        return self.retrieves_previous_pathtrace_v1(
                    flow_analysis_id=flow_analysis_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def deletes_pathtrace_by_id(self,
                                   flow_analysis_id,
                                   headers=None,
                                   **request_parameters):
        """ This function is an alias of deletes_pathtrace_by_id_v1 .
        Args:
            flow_analysis_id(str): flowAnalysisId path parameter. Flow analysis request id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of deletes_pathtrace_by_id_v1 .
        """
        return self.deletes_pathtrace_by_id_v1(
                    flow_analysis_id=flow_analysis_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def retrieves_all_previous_pathtraces_summary(self,
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
        """ This function is an alias of retrieves_all_previous_pathtraces_summary_v1 .
        Args:
            periodic_refresh(bool): periodicRefresh query parameter. Is analysis periodically refreshed? .
            source_ip(str): sourceIP query parameter. Source IP address .
            dest_ip(str): destIP query parameter. Destination IP address .
            source_port(int): sourcePort query parameter. Source port .
            dest_port(int): destPort query parameter. Destination port .
            gt_create_time(int): gtCreateTime query parameter. Analyses requested after this time .
            lt_create_time(int): ltCreateTime query parameter. Analyses requested before this time .
            protocol(str): protocol query parameter.
            status(str): status query parameter.
            task_id(str): taskId query parameter. Task ID .
            last_update_time(int): lastUpdateTime query parameter. Last update time .
            limit(int): limit query parameter. Number of resources returned .
            offset(int): offset query parameter. Start index of resources returned (1-based) .
            order(str): order query parameter. Order by this field .
            sort_by(str): sortBy query parameter. Sort by this field .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_all_previous_pathtraces_summary_v1 .
        """
        return self.retrieves_all_previous_pathtraces_summary_v1(
                    dest_ip=dest_ip,
                    dest_port=dest_port,
                    gt_create_time=gt_create_time,
                    last_update_time=last_update_time,
                    limit=limit,
                    lt_create_time=lt_create_time,
                    offset=offset,
                    order=order,
                    periodic_refresh=periodic_refresh,
                    protocol=protocol,
                    sort_by=sort_by,
                    source_ip=source_ip,
                    source_port=source_port,
                    status=status,
                    task_id=task_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
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
        """ This function is an alias of initiate_a_new_pathtrace_v1 .
        Args:
            controlPath(boolean): Path Trace's Control path tracing .
            destIP(string): Path Trace's Destination IP address .
            destPort(string): Path Trace's Destination Port, range: 1-65535 .
            inclusions(list): Path Trace's Subset of {INTERFACE-STATS, QOS-STATS, DEVICE-STATS, PERFORMANCE-STATS,
                ACL-TRACE}  (list of strings).
            periodicRefresh(boolean): Path Trace's Periodic refresh of path for every 30 sec .
            protocol(string): Path Trace's Protocol one of [TCP, UDP] checks both when left blank .
            sourceIP(string): Path Trace's Source IP address .
            sourcePort(string): Path Trace's Source Port, range: 1-65535 .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of initiate_a_new_pathtrace_v1 .
        """
        return self.initiate_a_new_pathtrace_v1(
                    controlPath=controlPath,
                    destIP=destIP,
                    destPort=destPort,
                    inclusions=inclusions,
                    periodicRefresh=periodicRefresh,
                    protocol=protocol,
                    sourceIP=sourceIP,
                    sourcePort=sourcePort,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )



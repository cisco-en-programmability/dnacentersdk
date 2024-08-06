# -*- coding: utf-8 -*-
"""Cisco DNA Center Task API wrapper.

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

from __future__ import absolute_import, division, print_function, unicode_literals

from builtins import *

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class Task(object):
    """Cisco DNA Center Task API (version: 2.3.7.6).

    Wraps the DNA Center Task
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Task
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Task, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_business_api_execution_details(self,
                                           execution_id,
                                           headers=None,
                                           **request_parameters):
        """Retrieves the execution details of a Business API .

        Args:
            execution_id(basestring): executionId path parameter. Execution Id of API .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-business-a-p-i-execution-details
        """
        check_type(headers, dict)
        check_type(execution_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'executionId': execution_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/dnacaap/management/execution-'
                 + 'status/{executionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ffc19ddea705526b7d9db01baf4997e_v2_3_7_6', json_data)

    def get_tasks2(self,
                   data=None,
                   end_time=None,
                   error_code=None,
                   failure_reason=None,
                   is_error=None,
                   limit=None,
                   offset=None,
                   order=None,
                   parent_id=None,
                   progress=None,
                   service_type=None,
                   sort_by=None,
                   start_time=None,
                   username=None,
                   headers=None,
                   **request_parameters):
        """Returns task(s) based on filter criteria .

        Args:
            start_time(basestring): startTime query parameter. This is the epoch start time from which tasks need to
                be fetched .
            end_time(basestring): endTime query parameter. This is the epoch end time upto which audit records need
                to be fetched .
            data(basestring): data query parameter. Fetch tasks that contains this data .
            error_code(basestring): errorCode query parameter. Fetch tasks that have this error code .
            service_type(basestring): serviceType query parameter. Fetch tasks with this service type .
            username(basestring): username query parameter. Fetch tasks with this username .
            progress(basestring): progress query parameter. Fetch tasks that contains this progress .
            is_error(basestring): isError query parameter. Fetch tasks ended as success or failure. Valid values:
                true, false .
            failure_reason(basestring): failureReason query parameter. Fetch tasks that contains this failure reason
                .
            parent_id(basestring): parentId query parameter. Fetch tasks that have this parent Id .
            offset(int): offset query parameter.
            limit(int): limit query parameter.
            sort_by(basestring): sortBy query parameter. Sort results by this field .
            order(basestring): order query parameter. Sort order asc or dsc .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-tasks2
        """
        check_type(headers, dict)
        check_type(start_time, basestring)
        check_type(end_time, basestring)
        check_type(data, basestring)
        check_type(error_code, basestring)
        check_type(service_type, basestring)
        check_type(username, basestring)
        check_type(progress, basestring)
        check_type(is_error, basestring)
        check_type(failure_reason, basestring)
        check_type(parent_id, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'startTime':
                start_time,
            'endTime':
                end_time,
            'data':
                data,
            'errorCode':
                error_code,
            'serviceType':
                service_type,
            'username':
                username,
            'progress':
                progress,
            'isError':
                is_error,
            'failureReason':
                failure_reason,
            'parentId':
                parent_id,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
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

        e_url = ('/dna/intent/api/v1/task')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ff485556f6504d8443789f42098be7_v2_3_7_6', json_data)

    def get_task_count(self,
                       data=None,
                       end_time=None,
                       error_code=None,
                       failure_reason=None,
                       is_error=None,
                       parent_id=None,
                       progress=None,
                       service_type=None,
                       start_time=None,
                       username=None,
                       headers=None,
                       **request_parameters):
        """Returns Task count .

        Args:
            start_time(basestring): startTime query parameter. This is the epoch start time from which tasks need to
                be fetched .
            end_time(basestring): endTime query parameter. This is the epoch end time upto which audit records need
                to be fetched .
            data(basestring): data query parameter. Fetch tasks that contains this data .
            error_code(basestring): errorCode query parameter. Fetch tasks that have this error code .
            service_type(basestring): serviceType query parameter. Fetch tasks with this service type .
            username(basestring): username query parameter. Fetch tasks with this username .
            progress(basestring): progress query parameter. Fetch tasks that contains this progress .
            is_error(basestring): isError query parameter. Fetch tasks ended as success or failure. Valid values:
                true, false .
            failure_reason(basestring): failureReason query parameter. Fetch tasks that contains this failure reason
                .
            parent_id(basestring): parentId query parameter. Fetch tasks that have this parent Id .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-task-count
        """
        check_type(headers, dict)
        check_type(start_time, basestring)
        check_type(end_time, basestring)
        check_type(data, basestring)
        check_type(error_code, basestring)
        check_type(service_type, basestring)
        check_type(username, basestring)
        check_type(progress, basestring)
        check_type(is_error, basestring)
        check_type(failure_reason, basestring)
        check_type(parent_id, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'startTime':
                start_time,
            'endTime':
                end_time,
            'data':
                data,
            'errorCode':
                error_code,
            'serviceType':
                service_type,
            'username':
                username,
            'progress':
                progress,
            'isError':
                is_error,
            'failureReason':
                failure_reason,
            'parentId':
                parent_id,
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

        e_url = ('/dna/intent/api/v1/task/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d0586946be75e0f9f2c170217d45a28_v2_3_7_6', json_data)

    def get_task_by_operationid(self,
                                limit,
                                offset,
                                operation_id,
                                headers=None,
                                **request_parameters):
        """Returns root tasks associated with an Operationid .

        Args:
            operation_id(basestring): operationId path parameter.
            offset(int): offset path parameter. Index, minimum value is 0 .
            limit(int): limit path parameter. The maximum value of {limit} supported is 500.               Base 1
                indexing for {limit}, minimum value is 1 .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-task-by-operation-id
        """
        check_type(headers, dict)
        check_type(operation_id, basestring,
                   may_be_none=False)
        check_type(offset, int,
                   may_be_none=False)
        check_type(limit, int,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'operationId': operation_id,
            'offset': offset,
            'limit': limit,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/task/operation/{operationId}/{offset}'
                 + '/{limit}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d95c21e41dce5a9dbee07d33eefef2b2_v2_3_7_6', json_data)

    def get_task_by_id(self,
                       task_id,
                       headers=None,
                       **request_parameters):
        """Returns a task by specified id .

        Args:
            task_id(basestring): taskId path parameter. UUID of the Task .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-task-by-id
        """
        check_type(headers, dict)
        check_type(task_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'taskId': task_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/task/{taskId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_99a75ba5a6bae1d568700bd3_v2_3_7_6', json_data)

    def get_task_tree(self,
                      task_id,
                      headers=None,
                      **request_parameters):
        """Returns a task with its children tasks by based on their id .

        Args:
            task_id(basestring): taskId path parameter. UUID of the Task .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-task-tree
        """
        check_type(headers, dict)
        check_type(task_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'taskId': task_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/task/{taskId}/tree')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fa2865e229b536aacd59585a1d29704_v2_3_7_6', json_data)

    def get_tasks(self,
                  end_time=None,
                  limit=None,
                  offset=None,
                  order=None,
                  parent_id=None,
                  root_id=None,
                  sort_by=None,
                  start_time=None,
                  status=None,
                  headers=None,
                  **request_parameters):
        """Returns task(s) based on filter criteria .

        Args:
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            sort_by(basestring): sortBy query parameter. A property within the response to sort by. .
            order(basestring): order query parameter. Whether ascending or descending order should be used to sort
                the response. .
            start_time(int): startTime query parameter. This is the epoch millisecond start time from which tasks
                need to be fetched .
            end_time(int): endTime query parameter. This is the epoch millisecond end time upto which task records
                need to be fetched .
            parent_id(basestring): parentId query parameter. Fetch tasks that have this parent Id .
            root_id(basestring): rootId query parameter. Fetch tasks that have this root Id .
            status(basestring): status query parameter. Fetch tasks that have this status. Available values :
                PENDING, FAILURE, SUCCESS .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-tasks
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(parent_id, basestring)
        check_type(root_id, basestring)
        check_type(status, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
            'startTime':
                start_time,
            'endTime':
                end_time,
            'parentId':
                parent_id,
            'rootId':
                root_id,
            'status':
                status,
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

        e_url = ('/dna/intent/api/v1/tasks')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b485e8aa7d9150ddb5048aa3b0617866_v2_3_7_6', json_data)

    def get_tasks_count(self,
                        end_time=None,
                        parent_id=None,
                        root_id=None,
                        start_time=None,
                        status=None,
                        headers=None,
                        **request_parameters):
        """Returns the number of tasks that meet the filter criteria .

        Args:
            start_time(int): startTime query parameter. This is the epoch millisecond start time from which tasks
                need to be fetched .
            end_time(int): endTime query parameter. This is the epoch millisecond end time upto which task records
                need to be fetched .
            parent_id(basestring): parentId query parameter. Fetch tasks that have this parent Id .
            root_id(basestring): rootId query parameter. Fetch tasks that have this root Id .
            status(basestring): status query parameter. Fetch tasks that have this status. Available values :
                PENDING, FAILURE, SUCCESS .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-tasks-count
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(parent_id, basestring)
        check_type(root_id, basestring)
        check_type(status, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'startTime':
                start_time,
            'endTime':
                end_time,
            'parentId':
                parent_id,
            'rootId':
                root_id,
            'status':
                status,
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

        e_url = ('/dna/intent/api/v1/tasks/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ff937b756f5eec9f5cd519ea6e9fec_v2_3_7_6', json_data)

    def get_tasks_by_id(self,
                        id,
                        headers=None,
                        **request_parameters):
        """Returns the task with the given ID .

        Args:
            id(basestring): id path parameter. the `id` of the task to retrieve .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-tasks-by-i-d
        """
        check_type(headers, dict)
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/tasks/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ffc437c17db355ae92597ce411cec6c8_v2_3_7_6', json_data)

    def get_task_details_by_id(self,
                               id,
                               headers=None,
                               **request_parameters):
        """Returns the task details for the given task ID .

        Args:
            id(basestring): id path parameter. the `id` of the task to retrieve details for .
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-task-details-by-i-d
        """
        check_type(headers, dict)
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/tasks/{id}/detail')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a48eee2b20065722ba9688176af178c1_v2_3_7_6', json_data)

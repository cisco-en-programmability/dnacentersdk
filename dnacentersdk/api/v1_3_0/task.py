# -*- coding: utf-8 -*-
"""DNA Center Task API wrapper.

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


class Task(object):
    """DNA Center Task API (version: 1.3.0).

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
        """Returns Task count.

        Args:
            start_time(basestring): This is the epoch start time
                from which tasks need to be fetched.
            end_time(basestring): This is the epoch end time upto
                which audit records need to be fetched.
            data(basestring): Fetch tasks that contains this data.
            error_code(basestring): Fetch tasks that have this error
                code.
            service_type(basestring): Fetch tasks with this service
                type.
            username(basestring): Fetch tasks with this username.
            progress(basestring): Fetch tasks that contains this
                progress.
            is_error(basestring): Fetch tasks ended as success or
                failure. Valid values: true, false.
            failure_reason(basestring): Fetch tasks that contains
                this failure reason.
            parent_id(basestring): Fetch tasks that have this parent
                Id.
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

        params = {
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
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_26b44ab04649a183_v1_3_0', json_data)

    def get_task_by_id(self,
                       task_id,
                       headers=None,
                       **request_parameters):
        """Returns a task by specified id.

        Args:
            task_id(basestring): UUID of the Task.
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
        check_type(task_id, basestring,
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
            'taskId': task_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/task/${taskId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_a1a9387346ba92b1_v1_3_0', json_data)

    def get_tasks(self,
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
        """Returns task(s) based on filter criteria.

        Args:
            start_time(basestring): This is the epoch start time
                from which tasks need to be fetched.
            end_time(basestring): This is the epoch end time upto
                which audit records need to be fetched.
            data(basestring): Fetch tasks that contains this data.
            error_code(basestring): Fetch tasks that have this error
                code.
            service_type(basestring): Fetch tasks with this service
                type.
            username(basestring): Fetch tasks with this username.
            progress(basestring): Fetch tasks that contains this
                progress.
            is_error(basestring): Fetch tasks ended as success or
                failure. Valid values: true, false.
            failure_reason(basestring): Fetch tasks that contains
                this failure reason.
            parent_id(basestring): Fetch tasks that have this parent
                Id.
            offset(basestring): offset query parameter.
            limit(basestring): limit query parameter.
            sort_by(basestring): Sort results by this field.
            order(basestring): Sort order - asc or dsc.
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
        check_type(offset, basestring)
        check_type(limit, basestring)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
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
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_e78bb8a2449b9eed_v1_3_0', json_data)

    def get_task_tree(self,
                      task_id,
                      headers=None,
                      **request_parameters):
        """Returns a task with its children tasks by based on their id.

        Args:
            task_id(basestring): UUID of the Task.
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
        check_type(task_id, basestring,
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
            'taskId': task_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/task/${taskId}/tree')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_f5a269c44f2a95fa_v1_3_0', json_data)

    def get_task_by_operationid(self,
                                limit,
                                offset,
                                operation_id,
                                headers=None,
                                **request_parameters):
        """Returns root tasks associated with an Operationid.

        Args:
            operation_id(basestring): operationId path parameter.
            offset(int): Index, minimum value is 0.
            limit(int): The maximum value of {limit} supported is
                500.              Base 1 indexing for
                {limit}, minimum value is 1.
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

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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

        e_url = ('/dna/intent/api/v1/task/operation/${operationId}/${offse'
                 + 't}/${limit}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_e487f8d3481b94f2_v1_3_0', json_data)

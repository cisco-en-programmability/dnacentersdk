# -*- coding: utf-8 -*-
"""DNA Center Task API wrapper.

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

class Task( object ):
    """DNA Center Task API.

    Wraps the DNA Center Task API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Task object with the provided RestSession.

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


    # Get task count
    def get_task_count(self, param_data = None, param_end_time = None, param_error_code = None, param_failure_reason = None, param_is_error = None, param_parent_id = None, param_progress = None, param_service_type = None, param_start_time = None, param_username = None, headers=None,payload=None,**request_parameters):
        check_type( param_start_time, basestring)
        check_type( param_end_time, basestring)
        check_type( param_data, basestring)
        check_type( param_error_code, basestring)
        check_type( param_service_type, basestring)
        check_type( param_username, basestring)
        check_type( param_progress, basestring)
        check_type( param_is_error, basestring)
        check_type( param_failure_reason, basestring)
        check_type( param_parent_id, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_start_time is not None: params.update( { 'startTime': param_start_time })
        if param_end_time is not None: params.update( { 'endTime': param_end_time })
        if param_data is not None: params.update( { 'data': param_data })
        if param_error_code is not None: params.update( { 'errorCode': param_error_code })
        if param_service_type is not None: params.update( { 'serviceType': param_service_type })
        if param_username is not None: params.update( { 'username': param_username })
        if param_progress is not None: params.update( { 'progress': param_progress })
        if param_is_error is not None: params.update( { 'isError': param_is_error })
        if param_failure_reason is not None: params.update( { 'failureReason': param_failure_reason })
        if param_parent_id is not None: params.update( { 'parentId': param_parent_id })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_26b44ab04649a183').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/task/count', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/task/count', path_params), params=params, json=payload)

        return self._object_factory('bpm_26b44ab04649a183', json_data)


    # Get task by Id
    def get_task_by_id(self, path_param_task_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_task_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'taskId': path_param_task_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_a1a9387346ba92b1').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/task/${taskId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/task/${taskId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_a1a9387346ba92b1', json_data)


    # Get tasks
    def get_tasks(self, param_data = None, param_end_time = None, param_error_code = None, param_failure_reason = None, param_is_error = None, param_limit = None, param_offset = None, param_order = None, param_parent_id = None, param_progress = None, param_service_type = None, param_sort_by = None, param_start_time = None, param_username = None, headers=None,payload=None,**request_parameters):
        check_type( param_start_time, basestring)
        check_type( param_end_time, basestring)
        check_type( param_data, basestring)
        check_type( param_error_code, basestring)
        check_type( param_service_type, basestring)
        check_type( param_username, basestring)
        check_type( param_progress, basestring)
        check_type( param_is_error, basestring)
        check_type( param_failure_reason, basestring)
        check_type( param_parent_id, basestring)
        check_type( param_offset, basestring)
        check_type( param_limit, basestring)
        check_type( param_sort_by, basestring)
        check_type( param_order, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_start_time is not None: params.update( { 'startTime': param_start_time })
        if param_end_time is not None: params.update( { 'endTime': param_end_time })
        if param_data is not None: params.update( { 'data': param_data })
        if param_error_code is not None: params.update( { 'errorCode': param_error_code })
        if param_service_type is not None: params.update( { 'serviceType': param_service_type })
        if param_username is not None: params.update( { 'username': param_username })
        if param_progress is not None: params.update( { 'progress': param_progress })
        if param_is_error is not None: params.update( { 'isError': param_is_error })
        if param_failure_reason is not None: params.update( { 'failureReason': param_failure_reason })
        if param_parent_id is not None: params.update( { 'parentId': param_parent_id })
        if param_offset is not None: params.update( { 'offset': param_offset })
        if param_limit is not None: params.update( { 'limit': param_limit })
        if param_sort_by is not None: params.update( { 'sortBy': param_sort_by })
        if param_order is not None: params.update( { 'order': param_order })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_e78bb8a2449b9eed').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/task', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/task', path_params), params=params, json=payload)

        return self._object_factory('bpm_e78bb8a2449b9eed', json_data)


    # Get task tree
    def get_task_tree(self, path_param_task_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_task_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'taskId': path_param_task_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_f5a269c44f2a95fa').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/task/${taskId}/tree', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/task/${taskId}/tree', path_params), params=params, json=payload)

        return self._object_factory('bpm_f5a269c44f2a95fa', json_data)


    # Get task by OperationId
    def get_task_by_operationid(self, path_param_limit, path_param_offset, path_param_operation_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_operation_id, basestring, may_be_none=False)
        check_type( path_param_offset, int, may_be_none=False)
        check_type( path_param_limit, int, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'operationId': path_param_operation_id,
            'offset': path_param_offset,
            'limit': path_param_limit,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_e487f8d3481b94f2').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/task/operation/${operationId}/${offset}/${limit}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/task/operation/${operationId}/${offset}/${limit}', path_params), params=params, json=payload)

        return self._object_factory('bpm_e487f8d3481b94f2', json_data)



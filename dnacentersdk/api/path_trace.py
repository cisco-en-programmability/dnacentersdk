# -*- coding: utf-8 -*-
"""DNA Center Path Trace API wrapper.

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

class PathTrace( object ):
    """DNA Center Path Trace API.

    Wraps the DNA Center Path Trace API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new PathTrace object with the provided RestSession.

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


    # Retrives all previous Pathtraces summary
    def retrives_all_previous_pathtraces_summary(self, param_dest_ip = None, param_dest_port = None, param_gt_create_time = None, param_last_update_time = None, param_limit = None, param_lt_create_time = None, param_offset = None, param_order = None, param_periodic_refresh = None, param_protocol = None, param_sort_by = None, param_source_ip = None, param_source_port = None, param_status = None, param_task_id = None, headers=None,payload=None,**request_parameters):
        check_type( param_periodic_refresh, bool)
        check_type( param_source_ip, basestring)
        check_type( param_dest_ip, basestring)
        check_type( param_source_port, basestring)
        check_type( param_dest_port, basestring)
        check_type( param_gt_create_time, basestring)
        check_type( param_lt_create_time, basestring)
        check_type( param_protocol, basestring)
        check_type( param_status, basestring)
        check_type( param_task_id, basestring)
        check_type( param_last_update_time, basestring)
        check_type( param_limit, basestring)
        check_type( param_offset, basestring)
        check_type( param_order, basestring)
        check_type( param_sort_by, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_periodic_refresh is not None: params.update( { 'periodicRefresh': param_periodic_refresh })
        if param_source_ip is not None: params.update( { 'sourceIP': param_source_ip })
        if param_dest_ip is not None: params.update( { 'destIP': param_dest_ip })
        if param_source_port is not None: params.update( { 'sourcePort': param_source_port })
        if param_dest_port is not None: params.update( { 'destPort': param_dest_port })
        if param_gt_create_time is not None: params.update( { 'gtCreateTime': param_gt_create_time })
        if param_lt_create_time is not None: params.update( { 'ltCreateTime': param_lt_create_time })
        if param_protocol is not None: params.update( { 'protocol': param_protocol })
        if param_status is not None: params.update( { 'status': param_status })
        if param_task_id is not None: params.update( { 'taskId': param_task_id })
        if param_last_update_time is not None: params.update( { 'lastUpdateTime': param_last_update_time })
        if param_limit is not None: params.update( { 'limit': param_limit })
        if param_offset is not None: params.update( { 'offset': param_offset })
        if param_order is not None: params.update( { 'order': param_order })
        if param_sort_by is not None: params.update( { 'sortBy': param_sort_by })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_55bc3bf94e38b6ff').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/flow-analysis', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/flow-analysis', path_params), params=params, json=payload)

        return self._object_factory('bpm_55bc3bf94e38b6ff', json_data)


    # Deletes Pathtrace by Id
    def deletes_pathtrace_by_id(self, path_param_flow_analysis_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_flow_analysis_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'flowAnalysisId': path_param_flow_analysis_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_8a9d2b76443b914e').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/api/v1/flow-analysis/${flowAnalysisId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/api/v1/flow-analysis/${flowAnalysisId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_8a9d2b76443b914e', json_data)


    # Initiate a new Pathtrace
    def initiate_a_new_pathtrace(self, rq_controlPath = None, rq_destIP = None, rq_destPort = None, rq_inclusions = None, rq_periodicRefresh = None, rq_protocol = None, rq_sourceIP = None, rq_sourcePort = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_controlPath is not None: payload.update( { 'controlPath':  rq_controlPath })
        if rq_destIP is not None: payload.update( { 'destIP':  rq_destIP })
        if rq_destPort is not None: payload.update( { 'destPort':  rq_destPort })
        if rq_inclusions is not None: payload.update( { 'inclusions':  rq_inclusions })
        if rq_periodicRefresh is not None: payload.update( { 'periodicRefresh':  rq_periodicRefresh })
        if rq_protocol is not None: payload.update( { 'protocol':  rq_protocol })
        if rq_sourceIP is not None: payload.update( { 'sourceIP':  rq_sourceIP })
        if rq_sourcePort is not None: payload.update( { 'sourcePort':  rq_sourcePort })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_a395fae644ca899c').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/api/v1/flow-analysis', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/api/v1/flow-analysis', path_params), params=params, json=payload)

        return self._object_factory('bpm_a395fae644ca899c', json_data)


    # Retrieves previous Pathtrace
    def retrieves_previous_pathtrace(self, path_param_flow_analysis_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_flow_analysis_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'flowAnalysisId': path_param_flow_analysis_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_7ab9a8bd4f3b86a4').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/flow-analysis/${flowAnalysisId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/flow-analysis/${flowAnalysisId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_7ab9a8bd4f3b86a4', json_data)



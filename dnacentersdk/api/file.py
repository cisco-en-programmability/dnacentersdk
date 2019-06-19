# -*- coding: utf-8 -*-
"""DNA Center File API wrapper.

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

class File( object ):
    """DNA Center File API.

    Wraps the DNA Center File API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new File object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(File, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator


    # Get list of available namespaces
    def get_list_of_available_namespaces(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_3f89bbfc4f6b8b50').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/file/namespace', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/file/namespace', path_params), params=params, json=payload)

        return self._object_factory('bpm_3f89bbfc4f6b8b50', json_data)


    # Get list of files
    def get_list_of_files(self, path_param_name_space, headers=None,payload=None,**request_parameters):
        check_type( path_param_name_space, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'nameSpace': path_param_name_space,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_42b6a86e44b8bdfc').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/file/namespace/${nameSpace}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/file/namespace/${nameSpace}', path_params), params=params, json=payload)

        return self._object_factory('bpm_42b6a86e44b8bdfc', json_data)


    # Download a file by fileId
    def download_a_file_by_fileid(self, path_param_file_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_file_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'fileId': path_param_file_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_9698c8ec4a0b8c1a').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/file/${fileId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/file/${fileId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_9698c8ec4a0b8c1a', json_data)



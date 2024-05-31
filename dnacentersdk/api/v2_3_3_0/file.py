# -*- coding: utf-8 -*-
"""Cisco DNA Center File API wrapper.

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


class File(object):
    """Cisco DNA Center File API (version: 2.3.3.0).

    Wraps the DNA Center File
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new File
        object with the provided RestSession.

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

    def get_list_of_available_namespaces(self,
                                         headers=None,
                                         **request_parameters):
        """Returns list of available namespaces .

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
            ApiError: If the DNA Center cloud returns an error.
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

        e_url = ('/dna/intent/api/v1/file/namespace')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b7fc125c901c5d4488b7a2b75fa292bc_v2_3_3_0', json_data)

    def get_list_of_files(self,
                          name_space,
                          headers=None,
                          **request_parameters):
        """Returns list of files under a specific namespace .

        Args:
            name_space(str): nameSpace path parameter. A listing of fileId's .
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
        check_type(name_space, str,
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
            'nameSpace': name_space,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/file/namespace/{nameSpace}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b7d63a5ae65b59a5a35d43edc58b6db5_v2_3_3_0', json_data)

    def download_a_file_by_fileid(self,
                                  file_id,
                                  dirpath=None,
                                  save_file=None,
                                  filename=None,
                                  headers=None,
                                  **request_parameters):
        """Downloads a file specified by fileId .

        Args:
            file_id(str): fileId path parameter. File Identification number .
            dirpath(str): Directory absolute path. Defaults to
                os.getcwd().
            save_file(bool): Enable or disable automatic file creation of
                raw response.
            filename(str): The filename used to save the download
                file.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            DownloadResponse: The DownloadResponse wrapper. Wraps the urllib3.response.HTTPResponse. For more
            information check the `urlib3 documentation <https://urllib3.readthedocs.io/en/latest/reference/urllib3.response.html>`_

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
            DownloadFailure: If was not able to download the raw
            response to a file.
        """
        check_type(headers, dict)
        check_type(file_id, str,
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
            'fileId': file_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/file/{fileId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers,
                                          stream=True, dirpath=dirpath, save_file=save_file, filename=filename)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          stream=True, dirpath=dirpath, save_file=save_file, filename=filename)

        return self._object_factory('bpm_fa4ab7605a75aafa6c7da6ac3f13_v2_3_3_0', json_data)

    def upload_file(self,
                    multipart_fields,
                    multipart_monitor_callback,
                    name_space,
                    headers=None,
                    **request_parameters):
        """Uploads a new file within a specific nameSpace .

        The following code gives an example of the multipart_fields.

        .. code-block:: python

            multipart_fields={'file': ('file.zip', open('file.zip', 'rb')}
            multipart_fields={'file': ('file.txt', open('file.txt', 'rb'),
                'text/plain',
                {'X-My-Header': 'my-value'})}
            multipart_fields=[('images', ('foo.png', open('foo.png', 'rb'),
                'image/png')),
                ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]

        The following example demonstrates how to use
        `multipart_monitor_callback=create_callback` to create a progress bar
        using clint.

        .. code-block:: python

            from clint.textui.progress import Bar
            def create_callback(encoder):
                encoder_len = encoder.len
                bar = Bar(expected_size=encoder_len,
                          filled_char="=")
                def callback(monitor):
                    bar.show(monitor.bytes_read)
                return callback

        Args:
            name_space(str): nameSpace path parameter.
            multipart_fields(dict): Fields from which to create a
                multipart/form-data body.
            multipart_monitor_callback(function): function used to monitor
                the progress of the upload.
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
        check_type(name_space, str,
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
            'nameSpace': name_space,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/file/{nameSpace}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        m_data = self._session.multipart_data(multipart_fields,
                                              multipart_monitor_callback)
        _headers.update({'Content-Type': m_data.content_type,
                         'Content-Length': str(m_data.len),
                         'Connection': 'keep-alive'})
        with_custom_headers = True
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           data=m_data,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e7fb3df05906b8cd6077d4d9cc5c_v2_3_3_0', json_data)

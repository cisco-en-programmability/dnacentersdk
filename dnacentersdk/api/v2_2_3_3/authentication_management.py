# -*- coding: utf-8 -*-
"""Cisco DNA Center Authentication Management API wrapper.

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


class AuthenticationManagement(object):
    """Cisco DNA Center Authentication Management API (version: 2.2.3.3).

    Wraps the DNA Center Authentication Management
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new AuthenticationManagement
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(AuthenticationManagement, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def import_certificate(self,
                           multipart_fields,
                           multipart_monitor_callback,
                           list_of_users=None,
                           pk_password=None,
                           headers=None,
                           **request_parameters):
        """This method is used to upload a certificate. Upload the files to the **certFileUpload** and **pkFileUpload**
        form data fields .

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
            pk_password(str): pkPassword query parameter. Private Key Passsword .
            list_of_users(str, list, set, tuple): listOfUsers query parameter.
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
        check_type(pk_password, str)
        check_type(list_of_users, (str, list, set, tuple))
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'pkPassword':
                pk_password,
            'listOfUsers':
                list_of_users,
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

        e_url = ('/dna/intent/api/v1/certificate')
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

        return self._object_factory('bpm_b19d7e8de2ca5329930d06f041a4a173_v2_2_3_3', json_data)

    def import_certificate_p12(self,
                               multipart_fields,
                               multipart_monitor_callback,
                               list_of_users=None,
                               p12_password=None,
                               pk_password=None,
                               headers=None,
                               **request_parameters):
        """This method is used to upload a PKCS#12 file. Upload the file to the **p12FileUpload** form data field .

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
            p12_password(str): p12Password query parameter. P12 Passsword .
            pk_password(str): pkPassword query parameter. Private Key Passsword .
            list_of_users(str, list, set, tuple): listOfUsers query parameter.
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
        check_type(p12_password, str)
        check_type(pk_password, str)
        check_type(list_of_users, (str, list, set, tuple))
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'p12Password':
                p12_password,
            'pkPassword':
                pk_password,
            'listOfUsers':
                list_of_users,
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

        e_url = ('/dna/intent/api/v1/certificate-p12')
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

        return self._object_factory('bpm_c80e660c2e36582f939a7403ef15de22_v2_2_3_3', json_data)

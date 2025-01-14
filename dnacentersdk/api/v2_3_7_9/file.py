# -*- coding: utf-8 -*-
"""Cisco Catalyst Center File API wrapper.

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


class File(object):
    """Cisco Catalyst Center File API (version: 2.3.7.9).

    Wraps the Catalyst Center File
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new File
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(File, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_list_of_available_namespaces_v1(self,
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-list-of-available-namespaces
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

        return self._object_factory('bpm_b7fc125c901c5d4488b7a2b75fa292bc_v2_3_7_9', json_data)

    def get_list_of_files_v1(self,
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-list-of-files
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

        return self._object_factory('bpm_b7d63a5ae65b59a5a35d43edc58b6db5_v2_3_7_9', json_data)

    def download_a_file_by_file_id_v1(self,
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
            ApiError: If the Catalyst Center cloud returns an error.
            DownloadFailure: If was not able to download the raw
            response to a file.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!download-a-file-by-file-id
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

        return self._object_factory('bpm_fa4ab7605a75aafa6c7da6ac3f13_v2_3_7_9', json_data)

    def upload_file_v1(self,
                       name_space,
                       headers=None,
                       **request_parameters):
        """Uploads a new file within a specific nameSpace .

        Args:
            name_space(str): nameSpace path parameter.
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
            https://developer.cisco.com/docs/dna-center/#!upload-file
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
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e7fb3df05906b8cd6077d4d9cc5c_v2_3_7_9', json_data)



    # Alias Function
    def upload_file(self,
                       name_space,
                       headers=None,
                       **request_parameters):
        """ This function is an alias of upload_file_v1 .
        Args:
            name_space(str): nameSpace path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of upload_file_v1 .
        """
        return self.upload_file_v1(
                    name_space=name_space,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_list_of_files(self,
                             name_space,
                             headers=None,
                             **request_parameters):
        """ This function is an alias of get_list_of_files_v1 .
        Args:
            name_space(str): nameSpace path parameter. A listing of fileId's .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_list_of_files_v1 .
        """
        return self.get_list_of_files_v1(
                    name_space=name_space,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_list_of_available_namespaces(self,
                                            headers=None,
                                            **request_parameters):
        """ This function is an alias of get_list_of_available_namespaces_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_list_of_available_namespaces_v1 .
        """
        return self.get_list_of_available_namespaces_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def download_a_file_by_file_id(self,
                                  file_id,
                                  headers=None,
                                  **request_parameters):
        """ This function is an alias of download_a_file_by_file_id_v1 .
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
            This function returns the output of download_a_file_by_file_id_v1 .
        """
        return self.download_a_file_by_file_id_v1(
                    file_id=file_id,
                    headers=headers,
                    **request_parameters
        )



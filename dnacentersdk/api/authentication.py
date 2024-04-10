# -*- coding: utf-8 -*-
"""Cisco DNA Center Authentication API wrapper.

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


import urllib.parse
from builtins import *

import requests


from ..response_codes import EXPECTED_RESPONSE_CODE
from ..utils import (
    check_response_code,
    check_type,
    dict_from_items_with_values,
    extract_and_parse_json,
    validate_base_url,
)


__author__ = ""
__author_email__ = ""
__copyright__ = "Copyright (c) 2019-2021 Cisco Systems."
__license__ = "MIT"


class Authentication(object):
    """Cisco DNA Center Authentication API.

    Wraps the DNA Center Authentication API and exposes the API as native
    Python methods that return native Python objects.

    """

    def __init__(self, base_url, object_factory, single_request_timeout=None,
                 verify=True):
        """Initialize an Authentication
        object with the provided RestSession.

        Args:
            base_url(str): The base URL to be prefixed to the
                individual API endpoint suffixes.
            object_factory(callable): The factory function to use to create
                Python objects from the returned DNA Center JSON data objects.
            single_request_timeout(int): Timeout in seconds for the API
                requests.
            verify(bool,str): Controls whether we verify the server's
                TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(base_url, str, may_be_none=False)
        check_type(single_request_timeout, int)
        check_type(verify, (bool, str), may_be_none=False)

        super(Authentication, self).__init__()

        self._base_url = str(validate_base_url(base_url))
        self._single_request_timeout = single_request_timeout
        self._verify = verify
        self._request_kwargs = {"timeout": single_request_timeout,
                                "verify": verify}
        self._object_factory = object_factory

        if verify is False:
            requests.packages.urllib3.disable_warnings()

    @property
    def verify(self):
        """The verify (TLS Certificate) for the API endpoints."""
        return self._verify

    @property
    def base_url(self):
        """The base URL for the API endpoints."""
        return self._base_url

    @property
    def single_request_timeout(self):
        """Timeout in seconds for the API requests."""
        return self._single_request_timeout

    @verify.setter
    def verify(self, value):
        """The verify (TLS Certificate) for the API endpoints."""
        check_type(value, (bool, str), may_be_none=False)
        self._verify = value
        self._request_kwargs = {"timeout": self._single_request_timeout,
                                "verify": self._verify}

    @base_url.setter
    def base_url(self, value):
        """The base URL for the API endpoints."""
        check_type(value, str, may_be_none=False)
        self._base_url = str(validate_base_url(value))

    @single_request_timeout.setter
    def single_request_timeout(self, value):
        """The timeout (seconds) for a single HTTP REST API request."""
        check_type(value, int)
        assert value is None or value > 0
        self._single_request_timeout = value
        self._request_kwargs = {"timeout": self._single_request_timeout,
                                "verify": self._verify}

    def authentication_api(self, username, password, encoded_auth=None):
        """Exchange basic auth data for an Access Token(x-auth-token)
        that can be used to invoke the APIs.

        Args:
            username(str): HTTP Basic Auth username.
            password(str): HTTP Basic Auth password.
            encoded_auth(str): HTTP Basic Auth base64 encoded string.

        Returns:
            AccessToken: An AccessToken object with the access token provided
            by the DNA Center cloud.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the DNA Center cloud returns an error.

        """
        temp_url = '/dna/system/api/v1/auth/token'
        self._endpoint_url = urllib.parse.urljoin(self._base_url, temp_url)

        if encoded_auth is not None:
            check_type(encoded_auth, str, may_be_none=False)
            if isinstance(encoded_auth, str):
                encoded_auth = bytes(encoded_auth, 'utf-8')
            # API request
            response = requests.post(self._endpoint_url, data=None,
                                     headers={'authorization': b'Basic '
                                              + encoded_auth},
                                     **self._request_kwargs)
        else:
            check_type(username, str, may_be_none=False)
            check_type(password, str, may_be_none=False)
            # API request
            response = requests.post(self._endpoint_url, data=None,
                                     auth=(username, password),
                                     **self._request_kwargs)

        check_response_code(response, EXPECTED_RESPONSE_CODE['POST'])
        json_data = extract_and_parse_json(response)

        # Return a access_token object created from the response JSON data
        return self._object_factory('bpm_ac8ae94c4e69a09d', json_data)

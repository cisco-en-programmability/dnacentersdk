# -*- coding: utf-8 -*-
"""DNA Center Access-Tokens API wrapper.

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

from future import standard_library
standard_library.install_aliases()

from builtins import *
import urllib.parse

from past.builtins import basestring
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
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "MIT"


class Authentication( object ):
    """DNA Center Authentication API.

    Wraps the DNA Center Authentication API and exposes the API as native
    Python methods that return native Python objects.

    """

    def __init__(self, base_url, object_factory, single_request_timeout=None, verify=True):
        """Initialize an Authentication object with the provided RestSession.

        Args:
            base_url(basestring): The base URL the API endpoints.
            single_request_timeout(int): Timeout in seconds for the API
                requests.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(base_url, basestring, may_be_none=False)
        check_type(single_request_timeout, int)
        check_type(verify, (bool, basestring), may_be_none=False)

        super(Authentication, self).__init__()

        self._base_url = str(validate_base_url(base_url))
        self._single_request_timeout = single_request_timeout
        self._verify = verify
        self._request_kwargs = {"timeout": single_request_timeout, "verify": verify}
        self._object_factory = object_factory

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

    # Authentication API
    def authentication_api(self, username, password, encodedAuth = None):
        """Exchange an Authorization Code for an Access Token.

        Exchange an Authorization Code for an Access Token that can be used to
        invoke the APIs.

        Args:
            client_id(basestring): Provided when you created your integration.
            client_secret(basestring): Provided when you created your
                integration.
            code(basestring): The Authorization Code provided by the user
                OAuth process.
            redirect_uri(basestring): The redirect URI used in the user OAuth
                process.

        Returns:
            AccessToken: An AccessToken object with the access token provided
            by the DNA Center cloud.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the DNA Center cloud returns an error.

        """
        self._endpoint_url = urllib.parse.urljoin(self._base_url, '/dna/system/api/v1/auth/token')

        if encodedAuth is not None:
            check_type(encodedAuth, basestring, may_be_none=False)
            # API request
            response = requests.post(self._endpoint_url, data=None, headers={'authorization': b'Basic ' + encodedAuth},
                                    **self._request_kwargs)
        else:
            check_type(username, basestring, may_be_none=False)
            check_type(password, basestring, may_be_none=False)
            # API request
            response = requests.post(self._endpoint_url, data=None, auth=(username, password),
                                    **self._request_kwargs)
        
        check_response_code(response, EXPECTED_RESPONSE_CODE['POST'])
        json_data = extract_and_parse_json(response)

        # Return a access_token object created from the response JSON data
        return self._object_factory('bpm_ac8ae94c4e69a09d', json_data)


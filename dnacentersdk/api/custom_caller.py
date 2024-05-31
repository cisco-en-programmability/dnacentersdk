# -*- coding: utf-8 -*-
"""Cisco DNA Center CustomCaller

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


import logging
from builtins import *


from requests.exceptions import HTTPError

from ..restsession import RestSession
from ..utils import (
    apply_path_params,
    check_type,
    extract_and_parse_json,
    pprint_request_info,
    pprint_response_info,
)

logger = logging.getLogger(__name__)


class CustomCaller(object):
    """Cisco DNA Center CustomCaller.

    DNA Center CustomCaller allows API creation.

    """

    def __init__(self, session, object_factory):
        """Initialize a new CustomCaller object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(CustomCaller, self).__init__()

        self._session = session
        self._object_factory = object_factory

        if self._session._debug:
            logger.setLevel(logging.DEBUG)
            logger.propagate = True
        else:
            logger.setLevel(logging.INFO)

    def add_api(self, name, obj):
        """Adds an api call to the CustomCaller.

        Args:
            name (str): name you want to set to the api client, has to follow
                python variable naming rule.
            obj (object): api call which is actually a calling call_api
                method.

        """

        setattr(self, name, obj)

    def call_api(self, method, resource_path, raise_exception=True,
                 original_response=False,
                 **kwargs):
        """Handles the requests and response.

        Args:
            method(str): type of request.
            resource_path(str): URL in the request object.
            raise_exception(bool): If True, http exceptions will be raised.
            original_response(bool): If True, MyDict (JSON response) is
                returned, else response object.
            path_params(dict) (optional): Find each path_params' key in the
                resource_path and replace it with path_params' value.
            params (optional): Dictionary or bytes to be sent in the query
                string for the Request.
            data (optional): Dictionary, bytes, or file-like object to send in
                the body of the Request.
            json (optional): json data to send in the body of the Request.
            headers (optional): Dictionary of HTTP Headers to send with the
                Request.
            cookies (optional): Dict or CookieJar object to send with the
                Request.
            files (optional): Dictionary of 'name': file-like-objects
                (or {'name': ('filename', fileobj)}) for multipart encoding
                upload.
            auth (optional): Auth tuple to enable Basic/Digest/Custom
                HTTP Auth.
            timeout(float, tuple) (optional): How long to wait for the server
                to send data before giving up, as a float, or a (connect
                timeout, read timeout) tuple.
            allow_redirects(bool) (optional): bool. Set to True if
                POST/PUT/DELETE redirect following is allowed.
            proxies(optional): Dictionary mapping protocol to the URL of the
                proxy.
            verify(bool,string) (optional): if True, the SSL cert will be
                verified. A CA_BUNDLE path can also be provided as a string.
            stream(optional): if False, the response content will be
                immediately downloaded.
            cert(str, tuple) (optional): if String, path to ssl client
                cert file (.pem). If Tuple, (‘cert’, ‘key’) pair

        Returns:
            MyDict or object: If original_response is True returns the
            original object response, else returns a JSON response with
            access to the object's properties by using the dot notation
            or the bracket notation. Defaults to False.

        Raises:
            TypeError: If the parameter types are incorrect.
            HTTPError: If the DNA Center cloud returns an error.
        """

        path_params = kwargs.pop('path_params', {})
        resource_path = apply_path_params(resource_path, path_params)

        # Ensure the url is an absolute URL
        abs_url = self._session.abs_url(resource_path)
        headers = self._session.headers

        if 'headers' in kwargs:
            headers.update(kwargs.pop('headers'))

        verify = kwargs.pop("verify", self._session.verify)

        logger.debug(pprint_request_info(abs_url, method,
                                         headers,
                                         **kwargs))
        response = self._session._req_session.request(method,
                                                      abs_url,
                                                      headers=headers,
                                                      verify=verify,
                                                      **kwargs)

        if raise_exception:
            try:
                response.raise_for_status()
            except HTTPError as e:
                logger.debug(pprint_response_info(e.response))
                raise e

        logger.debug(pprint_response_info(response))
        if original_response:
            return response
        else:
            json_data = extract_and_parse_json(response)
            return self._object_factory('bpm_custom', json_data)

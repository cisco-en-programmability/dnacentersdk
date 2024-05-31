# -*- coding: utf-8 -*-
"""Package helper functions and classes.

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


native_str = str

import json
import mimetypes
import os
import sys
import urllib.parse
from builtins import *
from collections import OrderedDict, namedtuple
from datetime import datetime, timedelta, tzinfo


from .exceptions import ApiError, RateLimitError
from .response_codes import RATE_LIMIT_RESPONSE_CODE


EncodableFile = namedtuple('EncodableFile',
                           ['file_name', 'file_object', 'content_type'])


def to_unicode(string):
    """Convert a string (bytes, str or unicode) to unicode."""
    assert isinstance(string, str)
    if sys.version_info[0] >= 3:
        if isinstance(string, bytes):
            return string.decode('utf-8')
        else:
            return string
    else:
        if isinstance(string, str):
            return string.decode('utf-8')
        else:
            return string


def to_bytes(string):
    """Convert a string (bytes, str or unicode) to bytes."""
    assert isinstance(string, str)
    if sys.version_info[0] >= 3:
        if isinstance(string, str):
            return string.encode('utf-8')
        else:
            return string
    else:
        if isinstance(string, unicode):
            return string.encode('utf-8')
        else:
            return string


def validate_base_url(base_url):
    """Verify that base_url specifies a protocol and network location."""
    parsed_url = urllib.parse.urlparse(base_url)
    if parsed_url.scheme and parsed_url.netloc:
        return parsed_url.geturl()
    else:
        error_message = "base_url must contain a valid scheme (protocol " \
                        "specifier) and network location (hostname)"
        raise ValueError(error_message)


def is_web_url(string):
    """Check to see if string is an validly-formatted web url."""
    assert isinstance(string, str)
    parsed_url = urllib.parse.urlparse(string)
    return (
        (
            parsed_url.scheme.lower() == 'http'
            or parsed_url.scheme.lower() == 'https'
        )
        and parsed_url.netloc
    )


def is_local_file(string):
    """Check to see if string is a valid local file path."""
    assert isinstance(string, str)
    return os.path.isfile(string)


def open_local_file(file_path):
    """Open the file and return an EncodableFile tuple."""
    assert isinstance(file_path, str)
    assert is_local_file(file_path)
    file_name = os.path.basename(file_path)
    file_object = open(file_path, 'rb')
    content_type = mimetypes.guess_type(file_name)[0] or 'text/plain'
    return EncodableFile(file_name=file_name,
                         file_object=file_object,
                         content_type=content_type)


def check_type(o, acceptable_types, may_be_none=True):
    """Object is an instance of one of the acceptable types or None.

    Args:
        o: The object to be inspected.
        acceptable_types: A type or tuple of acceptable types.
        may_be_none(bool): Whether or not the object may be None.

    Raises:
        TypeError: If the object is None and may_be_none=False, or if the
            object is not an instance of one of the acceptable types.

    """
    if not isinstance(acceptable_types, tuple):
        acceptable_types = (acceptable_types,)

    if may_be_none and o is None:
        # Object is None, and that is OK!
        pass
    elif isinstance(o, acceptable_types):
        # Object is an instance of an acceptable type.
        pass
    else:
        # Object is something else.
        error_message = (
            "We were expecting to receive an instance of one of the following "
            "types: {types}{none}; but instead we received {o} which is a "
            "{o_type}.".format(
                types=", ".join([repr(t.__name__) for t in acceptable_types]),
                none="or 'None'" if may_be_none else "",
                o=o,
                o_type=repr(type(o).__name__)
            )
        )
        raise TypeError(error_message)


def dict_from_items_with_values(*dictionaries, **items):
    """Creates a dict with the inputted items; pruning any that are `None`.

    Args:
        *dictionaries(dict): Dictionaries of items to be pruned and included.
        **items: Items to be pruned and included.

    Returns:
        dict: A dictionary containing all of the items with a 'non-None' value.

    """
    dict_list = list(dictionaries)
    dict_list.append(items)
    result = {}
    for d in dict_list:
        for key, value in d.items():
            if value is not None:
                result[key] = value
    return result


def raise_if_extra_kwargs(kwargs):
    """Raise a TypeError if kwargs is not empty."""
    if kwargs:
        raise TypeError("Unexpected **kwargs: {!r}".format(kwargs))


def check_response_code(response, expected_response_code):
    """Check response code against the expected code; raise ApiError.

    Checks the requests.response.status_code against the provided expected
    response code (erc), and raises a ApiError if they do not match.

    Args:
        response(requests.response): The response object returned by a request
            using the requests package.
        expected_response_code(int): The expected response code (HTTP response
            code).

    Raises:
        ApiError: If the requests.response.status_code does not match the
            provided expected response code (erc).

     """
    if response.status_code in expected_response_code:
        pass
    elif response.status_code == RATE_LIMIT_RESPONSE_CODE:
        raise RateLimitError(response)
    else:
        raise ApiError(response)


def extract_and_parse_json(response):
    """Extract and parse the JSON data from an requests.response object.

    Args:
        response(requests.response): The response object returned by a request
            using the requests package.
        stream(bool): If the request was to get a raw response content

    Returns:
        The parsed JSON data as the appropriate native Python data type.

    Raises:
        JSONDecodeError: caused by json.loads
        TypeError: caused by json.loads
    """
    try:
        return json.loads(response.text, object_hook=OrderedDict)
    except Exception as e:
        raise e


def json_dict(json_data):
    """Given a dictionary or JSON string; return a dictionary.

    Args:
        json_data(dict, str): Input JSON object.

    Returns:
        A Python dictionary with the contents of the JSON object.

    Raises:
        TypeError: If the input object is not a dictionary or string.

    """
    if isinstance(json_data, dict):
        return json_data
    elif isinstance(json_data, str):
        return json.loads(json_data, object_hook=OrderedDict)
    elif isinstance(json_data, list):
        return json_data
    else:
        raise TypeError(
            "'json_data' must be a dictionary or valid JSON string; "
            "received: {!r}".format(json_data)
        )


def apply_path_params(URL, path_params):
    if isinstance(URL, str) and isinstance(path_params, dict):
        for k in path_params:
            URL = URL.replace('${' + k + '}', str(path_params[k]))
            URL = URL.replace('{' + k + '}', str(path_params[k]))
        return URL
    else:
        raise TypeError(
            "'URL' must be a string; "
            "'path_params' must be a dictionary or valid JSON string; "
            "received: (URL={}, path_params={})".format(URL, path_params)
        )


def pprint_request_info(url, method, _headers, **kwargs):
    debug_print = (
        "\nRequest"
        "\n\tURL: {}"
        "\n\tMethod: {}"
        "\n\tHeaders: \n{}"
    )
    _headers.update(kwargs.get('headers', {}))
    _headers = '\n'.join(['\t\t{}: {}'.format(a, b)
                         for a, b in _headers.items()])
    debug_print = debug_print.format(url, method, _headers)

    kwargs_to_include = ['params', 'json', 'data', 'stream']
    kwargs_pprint = {
        'params': 'Params', 'json': 'Body',
        'data': 'Body', 'stream': 'Stream'
    }

    for kw in kwargs_to_include:
        if kwargs.get(kw) is not None and kwargs_pprint.get(kw):
            value = kwargs.get(kw)
            key = kwargs_pprint.get(kw)
            if isinstance(value, list) or isinstance(value, dict):
                value = json.dumps(value, indent=4)
                lines = [' ' * (8 + len(key)) + line
                         for line in value.split('\n')]
                value = '\n'.join(lines)
            else:
                value = '\t\t{}'.format(value)

            format_str = '{}\n\t{}:\n{}'
            debug_print = format_str.format(debug_print,
                                            key,
                                            value)
    return debug_print


def pprint_response_info(response):
    debug_print = (
        "\nResponse"
        "\n\tStatus: {} - {}"
        "\n\tHeaders: \n{}"
    )
    headers = response.headers
    headers = '\n'.join(['\t\t{}: {}'.format(a, b)
                         for a, b in headers.items()])
    body = None
    file_resp_headers = ['Content-Disposition', 'fileName']

    if 'application/json' in response.headers.get('Content-Type'):
        try:
            body = response.json()
            body = json.dumps(body, indent=4)
            body = '\n'.join([' ' * 13 + line for line in body.split('\n')])
        except Exception:
            body = response.text or response.content
            pass
    elif any([i in response.headers for i in file_resp_headers]):
        body = None
    else:
        body = response.text or response.content

    debug_print = debug_print.format(response.status_code,
                                     response.reason,
                                     headers)

    if body is not None:
        format_str = '{}\n\t{}:\n{}'
        debug_print = format_str.format(debug_print, 'Body', body)

    return debug_print


def dict_of_str(json_dict):
    """Given a dictionary; return a new dictionary with all items as strings.

    Args:
        json_dict(dict): Input JSON dictionary.

    Returns:
        A Python dictionary with the contents of the JSON object as strings.
    """
    result = {}
    for key, value in json_dict.items():
        result[key] = '{}'.format(value)
    return result

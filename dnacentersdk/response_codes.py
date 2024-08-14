# -*- coding: utf-8 -*-
"""Cisco DNA Center Response Codes.

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


RESPONSE_CODES = {
    200: "Successful request with body content.",
    201: "Fulfilled request, a new resource has been created.",
    202: "The request was accepted for processing, but the processing has not"
         " been completed.",
    204: "Successful request without body content.",
    206: "The request included a Range Header, and the server responded with "
         "the partial content matching the range.",
    400: "The request was invalid or cannot be otherwise served.",
    401: "Authentication credentials were missing or incorrect.",
    403: "The request is understood, but it has been refused or access is not "
         "allowed.",
    404: "The URI requested is invalid or the resource requested, such as a "
         "user, does not exist. Also returned when the requested format is "
         "not supported by the requested method.",
    409: "The request could not be processed because it conflicts with some "
         "established rule of the system.",
    415: "The request was made to a resource without specifying a media type "
         "or used a media type that is not supported.",
    500: "The server could not fulfill the request.",
    501: "The server has not implemented the functionality required to fulfill"
         " the request.",
    503: "Server is overloaded with requests. Try again later.",
    504: "The server did not respond inside time restrictions and timed-out.",
    # Other http statuses
    405: "The request was made to a resource using an HTTP request method "
         "that is not supported.",
    429: "Too many requests have been sent in a given amount of time and the "
         "request has been rate limited. A Retry-After header should be "
         "present that specifies how many seconds you need to wait before a "
         "successful request can be made.",
    502: "The server received an invalid response from an upstream server "
         "while processing the request. Try again later."
}

RATE_LIMIT_RESPONSE_CODE = 429

EXPECTED_RESPONSE_CODE = {
    'GET': [200, 202, 204, 206],
    'PATCH': [200, 201, 202, 204, 206],
    'POST': [200, 201, 202, 204, 206],
    'PUT': [200, 201, 202, 204, 206],
    'DELETE': [200, 202, 204, 206],
}

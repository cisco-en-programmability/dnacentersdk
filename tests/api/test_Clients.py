# -*- coding: utf-8 -*-
"""DNACenterAPI clients API fixtures and tests.

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

import pytest
import dnacentersdk




# e2ad-ba79-43ba-b3e9
def is_valid_get_client_detail(obj):
    some_keys = ['executionId', 'executionStatusUrl', 'message']
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_client_detail(api):
    endpoint_result = api.clients.get_client_detail( param_mac_address = '', param_timestamp = '1562604696', payload = '' )
    return endpoint_result


def test_get_client_detail(api):
    assert is_valid_get_client_detail(get_client_detail(api))


# 149a-a93b-4ddb-80dd
def is_valid_get_overall_client_health(obj):
    some_keys = ['executionId', 'executionStatusUrl', 'message']
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_overall_client_health(api):
    endpoint_result = api.clients.get_overall_client_health( param_timestamp = '1562604696', payload = '' )
    return endpoint_result


def test_get_overall_client_health(api):
    assert is_valid_get_overall_client_health(get_overall_client_health(api))


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
import time
from tests.environment import DNA_CENTER_VERSION


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_get_client_detail(obj):
    some_keys = ['executionId', 'executionStatusUrl', 'message']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_client_detail(api):
    endpoint_result = api.clients.get_client_detail(
        mac_address='',
        timestamp='',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.clients
def test_get_client_detail(api):
    assert is_valid_get_client_detail(
        get_client_detail(api)
    )


def is_valid_get_overall_client_health(obj):
    some_keys = ['response']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_overall_client_health(api):
    endpoint_result = api.clients.get_overall_client_health(
        timestamp='',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.clients
def test_get_overall_client_health(api):
    assert is_valid_get_overall_client_health(
        get_overall_client_health(api)
    )

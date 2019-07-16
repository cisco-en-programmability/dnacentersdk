# -*- coding: utf-8 -*-
"""dnacentersdk/restsession.py Fixtures & Tests

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


import logging
import warnings

import pytest

import dnacentersdk


logging.captureWarnings(True)


# Helper Functions
def rate_limit_detected(w):
    """Check to see if a rate-limit warning is in the warnings list."""
    while w:
        if issubclass(w.pop().category, dnacentersdk.RateLimitWarning):
            return True
    return False


# Tests
@pytest.mark.ratelimit
def test_rate_limit_retry(api):
    # Save state and initialize test setup
    original_wait_on_rate_limit = api._session.wait_on_rate_limit
    api._session.wait_on_rate_limit = True

    with warnings.catch_warnings(record=True) as w:
        devices = api.devices.get_device_list()
        i = 0
        while i < len(devices.response):
            # Try and trigger a rate-limit
            api.devices.get_device_config_by_id(path_network_device_id=devices.response[i].id)
            i += 1
            if rate_limit_detected(w):
                break
    api._session.wait_on_rate_limit = original_wait_on_rate_limit

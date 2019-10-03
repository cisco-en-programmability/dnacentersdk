# -*- coding: utf-8 -*-
"""DNACenterAPI fixtures and tests.

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

from dnacentersdk import DNACenterAPI
from tests.environment import (
    DNA_CENTER_USERNAME, DNA_CENTER_PASSWORD,
    DNA_CENTER_ENCODED_AUTH, DNA_CENTER_VERSION,
)
from tests.config import (
    DEFAULT_BASE_URL, DEFAULT_VERIFY,
    DEFAULT_SINGLE_REQUEST_TIMEOUT, DEFAULT_WAIT_ON_RATE_LIMIT
)


# Fixtures

@pytest.fixture(scope="session")
def api():
    return DNACenterAPI(username=DNA_CENTER_USERNAME,
                        password=DNA_CENTER_PASSWORD,
                        encoded_auth=DNA_CENTER_ENCODED_AUTH,
                        base_url=DEFAULT_BASE_URL,
                        single_request_timeout=DEFAULT_SINGLE_REQUEST_TIMEOUT,
                        wait_on_rate_limit=DEFAULT_WAIT_ON_RATE_LIMIT,
                        verify=DEFAULT_VERIFY,
                        version=DNA_CENTER_VERSION)

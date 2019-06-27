# -*- coding: utf-8 -*-
"""Test suite environment variables.

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

import os
import string

from .config import ACCESS_TOKEN_ENVIRONMENT_VARIABLE, DEFAULT_PASS, DEFAULT_USER

DNA_CENTER_ACCESS_TOKEN = os.getenv(ACCESS_TOKEN_ENVIRONMENT_VARIABLE)
if DNA_CENTER_ACCESS_TOKEN is None and not (DEFAULT_PASS and DEFAULT_USER):
    raise RuntimeError(
        "You must set a {} environment variable to run the test suite "
        "or check the DEFAULT_PASS and DEFAULT_USER values in config."
        "".format(ACCESS_TOKEN_ENVIRONMENT_VARIABLE)
    )

DNA_CENTER_TEST_STRING_PREFIX = os.getenv(
    "DNA_CENTER_TEST_STRING_PREFIX", default="dnacentersdk py.test",
)

DNA_CENTER_TEST_STRING_TEMPLATE = string.Template(os.getenv(
    "DNA_CENTER_TEST_STRING_TEMPLATE", default="$prefix $item [$datetime]",
))

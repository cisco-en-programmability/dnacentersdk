# -*- coding: utf-8 -*-
"""Community-developed Python SDK for the DNA Center APIs.

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

import logging

from ._metadata import *
from .api import DNACenterAPI
from .exceptions import (
    AccessTokenError,
    ApiError,
    dnacentersdkException,
    MalformedRequest,
    RateLimitError,
    RateLimitWarning,
    VersionError,
)
from .models.mydict import mydict_data_factory

from .models.schema_validator import (
    json_schema_validate
)


# Initialize Package Logging
logging.basicConfig()
logger = logging.getLogger(__name__)
requests_log = logging.getLogger("urllib3")
requests_log.addHandler(logging.NullHandler())
requests_log.propagate = False

from pkg_resources import get_distribution
release = get_distribution('dnacentersdk').version
__version__ = '.'.join(release.split('.')[:3])

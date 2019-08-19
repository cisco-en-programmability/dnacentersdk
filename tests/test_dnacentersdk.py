# -*- coding: utf-8 -*-
"""Test suite for the community-developed Python SDK for the DNA Center APIs.

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

import dnacentersdk
import pytest


@pytest.mark.dnacentersdk
class TestDNACenterSDK:
    """Test the package-level code."""

    def test_package_contents(self):
        """Ensure the package contains the correct top-level objects."""
        # DNA Center API Wrapper
        assert hasattr(dnacentersdk, "DNACenterAPI")

        # Exceptions
        assert hasattr(dnacentersdk, "AccessTokenError")
        assert hasattr(dnacentersdk, "ApiError")
        assert hasattr(dnacentersdk, "dnacentersdkException")
        assert hasattr(dnacentersdk, "MalformedRequest")
        assert hasattr(dnacentersdk, "RateLimitError")
        assert hasattr(dnacentersdk, "RateLimitWarning")
        assert hasattr(dnacentersdk, "VersionError")

        # Data Models
        assert hasattr(dnacentersdk, "mydict_data_factory")
        assert hasattr(dnacentersdk, "json_schema_validate")

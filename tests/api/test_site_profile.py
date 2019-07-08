# -*- coding: utf-8 -*-
"""DNACenterAPI site_profile API fixtures and tests.

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




# 7fbe-4b80-4879-baa4
def is_valid_get_device_details_by_ip(obj):
    some_keys = ['executionId', 'executionStatusUrl', 'message']
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_device_details_by_ip(api):
    endpoint_result = api.site_profile.get_device_details_by_ip( param_device_ip = '10.10.20.253', payload = '' )
    return endpoint_result


def test_get_device_details_by_ip(api):
    assert is_valid_get_device_details_by_ip(get_device_details_by_ip(api))


# 8288-28f4-4f28-bd0d
def is_valid_provision_nfv(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def provision_nfv(api):
    endpoint_result = api.site_profile.provision_nfv( rq_provisioning = None, rq_siteProfile = None, payload = '' )
    return endpoint_result


def test_provision_nfv(api):
    assert is_valid_provision_nfv(provision_nfv(api))


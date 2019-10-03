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
import time
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate
from tests.config import SITE_PROFILE_DEVICE_IP


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_get_device_details_by_ip(obj):
    some_keys = ['executionId', 'executionStatusUrl', 'message']
    return True if len(some_keys) == 0 else\
        any([obj.has_path(item) for item in some_keys])


def get_device_details_by_ip(api):
    endpoint_result = api.site_profile.get_device_details_by_ip(
        device_ip=SITE_PROFILE_DEVICE_IP,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([SITE_PROFILE_DEVICE_IP]) is True,
                    reason="tests.config values required not present")
@pytest.mark.site_profile
def test_get_device_details_by_ip(api):
    assert is_valid_get_device_details_by_ip(
        get_device_details_by_ip(api)
    )


def is_valid_provision_nfv(obj):
    json_schema_validate('jsd_828828f44f28bd0d_v1_2_10').validate(obj)
    return True


def provision_nfv(api):
    endpoint_result = api.site_profile.provision_nfv(
        callbackUrl=None,
        provisioning=None,
        siteProfile=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.site_profile
def test_provision_nfv(api):
    assert is_valid_provision_nfv(
        provision_nfv(api)
    )

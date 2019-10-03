# -*- coding: utf-8 -*-
"""DNACenterAPI sites API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_get_site_health(obj):
    json_schema_validate('jsd_17a82ac94cf99ab0_v1_2_10').validate(obj)
    return True


def get_site_health(api):
    endpoint_result = api.sites.get_site_health(
        timestamp=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_health(api):
    assert is_valid_get_site_health(
        get_site_health(api)
    )


def is_valid_create_site(obj):
    json_schema_validate('jsd_50b589fd4c7a930a_v1_2_10').validate(obj)
    return True


def create_site(api):
    endpoint_result = api.sites.create_site(
        site=None,
        type=None,
        payload={
            'type': 'building',
            'site': {
                'building': {
                    'name': 'Test_Building',
                    'address': '10.10.22.70'
                }
            }
        },
        active_validation=True
    )
    return endpoint_result


@pytest.mark.sites
def test_create_site(api):
    assert is_valid_create_site(
        create_site(api)
    )


def is_valid_assign_device_to_site(obj):
    json_schema_validate('jsd_eeb168eb41988e07_v1_2_10').validate(obj)
    return True


def assign_device_to_site(api):
    sites = get_site_health(api).response
    siteId = sites[0].siteId if sites and len(sites) > 0 else '1'
    device = api.devices.get_device_list().response[0]
    endpoint_result = api.sites.assign_device_to_site(
        site_id=siteId,
        device=[{'ip': device.managementIpAddress}],
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.sites
def test_assign_device_to_site(api):
    assert is_valid_assign_device_to_site(
        assign_device_to_site(api)
    )

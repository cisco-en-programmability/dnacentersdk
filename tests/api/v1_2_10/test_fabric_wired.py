# -*- coding: utf-8 -*-
"""DNACenterAPI fabric_wired API fixtures and tests.

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
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_gets_border_device_detail(obj):
    json_schema_validate('jsd_98a39bf4485a9871_v1_2_10').validate(obj)
    return True


def gets_border_device_detail(api):
    endpoint_result = api.fabric_wired.gets_border_device_detail(
        device_ip_address='string',
        sda_border_device='border-device'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_gets_border_device_detail(api):
    assert is_valid_gets_border_device_detail(
        gets_border_device_detail(api)
    )


def gets_border_device_detail_default(api):
    endpoint_result = api.fabric_wired.gets_border_device_detail(
        device_ip_address='string',
        sda_border_device='border-device'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_gets_border_device_detail_default(api):
    try:
        assert is_valid_gets_border_device_detail(
            gets_border_device_detail_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_adds_border_device(obj):
    json_schema_validate('jsd_bead7b3443b996a7_v1_2_10').validate(obj)
    return True


def adds_border_device(api):
    endpoint_result = api.fabric_wired.adds_border_device(
        active_validation=True,
        payload=[{'deviceManagementIpAddress': 'string', 'siteHierarchy': 'string', 'externalDomainRoutingProtocolName': 'string', 'externalConnectivityIpPoolName': 'string', 'internalAutonomouSystemNumber': 'string', 'borderSessionType': 'string', 'connectedToInternet': True, 'externalConnectivitySettings': [{'interfaceName': 'string', 'externalAutonomouSystemNumber': 'string', 'l3Handoff': [{'virtualNetwork': {'virtualNetworkName': 'string'}}]}]}],
        sda_border_device='border-device'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_adds_border_device(api):
    assert is_valid_adds_border_device(
        adds_border_device(api)
    )


def adds_border_device_default(api):
    endpoint_result = api.fabric_wired.adds_border_device(
        active_validation=True,
        payload=None,
        sda_border_device='border-device'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_adds_border_device_default(api):
    try:
        assert is_valid_adds_border_device(
            adds_border_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_deletes_border_device(obj):
    json_schema_validate('jsd_cb81b93540baaab0_v1_2_10').validate(obj)
    return True


def deletes_border_device(api):
    endpoint_result = api.fabric_wired.deletes_border_device(
        device_ip_address='string',
        sda_border_device='border-device'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_deletes_border_device(api):
    assert is_valid_deletes_border_device(
        deletes_border_device(api)
    )


def deletes_border_device_default(api):
    endpoint_result = api.fabric_wired.deletes_border_device(
        device_ip_address='string',
        sda_border_device='border-device'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_deletes_border_device_default(api):
    try:
        assert is_valid_deletes_border_device(
            deletes_border_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

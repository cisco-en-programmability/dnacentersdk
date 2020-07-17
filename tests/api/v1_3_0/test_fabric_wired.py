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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.0', reason='version does not match')


def is_valid_deletes_border_device_from_sda_fabric(obj):
    json_schema_validate('jsd_1e80bb50430b8634_v1_3_0').validate(obj)
    return True


def deletes_border_device_from_sda_fabric(api):
    endpoint_result = api.fabric_wired.deletes_border_device_from_sda_fabric(
        device_ip_address='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_deletes_border_device_from_sda_fabric(api):
    assert is_valid_deletes_border_device_from_sda_fabric(
        deletes_border_device_from_sda_fabric(api)
    )


def deletes_border_device_from_sda_fabric_default(api):
    endpoint_result = api.fabric_wired.deletes_border_device_from_sda_fabric(
        device_ip_address='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_deletes_border_device_from_sda_fabric_default(api):
    try:
        assert is_valid_deletes_border_device_from_sda_fabric(
            deletes_border_device_from_sda_fabric_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_adds_border_device_in_sda_fabric(obj):
    json_schema_validate('jsd_a4b56a5f478a97dd_v1_3_0').validate(obj)
    return True


def adds_border_device_in_sda_fabric(api):
    endpoint_result = api.fabric_wired.adds_border_device_in_sda_fabric(
        active_validation=True,
        payload=[{'deviceManagementIpAddress': 'string', 'siteHierarchy': 'string', 'externalDomainRoutingProtocolName': 'string', 'externalConnectivityIpPoolName': 'string', 'internalAutonomouSystemNumber': 'string', 'borderSessionType': 'string', 'connectedToInternet': True, 'externalConnectivitySettings': [{'interfaceName': 'string', 'externalAutonomouSystemNumber': 'string', 'l3Handoff': [{'virtualNetwork': {'virtualNetworkName': 'string'}}]}]}]
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_adds_border_device_in_sda_fabric(api):
    assert is_valid_adds_border_device_in_sda_fabric(
        adds_border_device_in_sda_fabric(api)
    )


def adds_border_device_in_sda_fabric_default(api):
    endpoint_result = api.fabric_wired.adds_border_device_in_sda_fabric(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_adds_border_device_in_sda_fabric_default(api):
    try:
        assert is_valid_adds_border_device_in_sda_fabric(
            adds_border_device_in_sda_fabric_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_gets_border_device_details_from_sda_fabric(obj):
    json_schema_validate('jsd_d0b3593c4a7aaf22_v1_3_0').validate(obj)
    return True


def gets_border_device_details_from_sda_fabric(api):
    endpoint_result = api.fabric_wired.gets_border_device_details_from_sda_fabric(
        device_ip_address='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_gets_border_device_details_from_sda_fabric(api):
    assert is_valid_gets_border_device_details_from_sda_fabric(
        gets_border_device_details_from_sda_fabric(api)
    )


def gets_border_device_details_from_sda_fabric_default(api):
    endpoint_result = api.fabric_wired.gets_border_device_details_from_sda_fabric(
        device_ip_address='string'
    )
    return endpoint_result


@pytest.mark.fabric_wired
def test_gets_border_device_details_from_sda_fabric_default(api):
    try:
        assert is_valid_gets_border_device_details_from_sda_fabric(
            gets_border_device_details_from_sda_fabric_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

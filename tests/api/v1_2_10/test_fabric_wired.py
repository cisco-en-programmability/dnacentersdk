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
import dnacentersdk
import time
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate
from tests.config import BORDER_DEVICE_SDA_FABRIC_PATH


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_adds_border_device_in_sda_fabric(obj):
    json_schema_validate('jsd_bead7b3443b996a7_v1_2_10').validate(obj)
    return True


def adds_border_device_in_sda_fabric(api):
    device = api.devices.get_device_list().response[0]
    endpoint_result = api.fabric_wired.adds_border_device_in_sda_fabric(
        sda_border_device=BORDER_DEVICE_SDA_FABRIC_PATH,
        payload=[{
            "deviceManagementIpAddress": device.managementIpAddress
        }],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([BORDER_DEVICE_SDA_FABRIC_PATH]) is True,
                    reason="tests.config values required not present")
@pytest.mark.fabric_wired
def test_adds_border_device_in_sda_fabric(api):
    assert is_valid_adds_border_device_in_sda_fabric(
        adds_border_device_in_sda_fabric(api)
    )


def is_valid_gets_border_device_details_from_sda_fabric(obj):
    json_schema_validate('jsd_98a39bf4485a9871_v1_2_10').validate(obj)
    return True


def gets_border_device_details_from_sda_fabric(api):
    device = api.devices.get_device_list().response[0]
    endpoint_result = api.fabric_wired.gets_border_device_details_from_sda_fabric(
        device_ip_address=device.managementIpAddress,
        sda_border_device=BORDER_DEVICE_SDA_FABRIC_PATH,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([BORDER_DEVICE_SDA_FABRIC_PATH]) is True,
                    reason="tests.config values required not present")
@pytest.mark.fabric_wired
def test_gets_border_device_details_from_sda_fabric(api):
    assert is_valid_gets_border_device_details_from_sda_fabric(
        gets_border_device_details_from_sda_fabric(api)
    )


def is_valid_deletes_border_device_from_sda_fabric(obj):
    json_schema_validate('jsd_cb81b93540baaab0_v1_2_10').validate(obj)
    return True


def deletes_border_device_from_sda_fabric(api):
    device = api.devices.get_device_list().response[0]
    endpoint_result = api.fabric_wired.deletes_border_device_from_sda_fabric(
        device_ip_address=device.managementIpAddress,
        sda_border_device=BORDER_DEVICE_SDA_FABRIC_PATH,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([BORDER_DEVICE_SDA_FABRIC_PATH]) is True,
                    reason="tests.config values required not present")
@pytest.mark.fabric_wired
def test_deletes_border_device_from_sda_fabric(api):
    assert is_valid_deletes_border_device_from_sda_fabric(
        deletes_border_device_from_sda_fabric(api)
    )

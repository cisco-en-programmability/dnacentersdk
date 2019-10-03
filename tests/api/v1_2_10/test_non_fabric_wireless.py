# -*- coding: utf-8 -*-
"""DNACenterAPI non_fabric_wireless API fixtures and tests.

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
from tests.config import (NEW_ENTERPRISE_SSID_NAME,
                          NEW_MANAGED_APLOCATIONS)


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_create_enterprise_ssid(obj):
    json_schema_validate('jsd_8a96fb954d09a349_v1_2_10').validate(obj)
    return True


def create_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.create_enterprise_ssid(
        enableBroadcastSSID=None,
        enableFastLane=None,
        enableMACFiltering=None,
        fastTransition=None,
        name=None,
        passphrase=None,
        radioPolicy=None,
        securityLevel=None,
        trafficType=None,
        payload={},
        active_validation=True
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_create_enterprise_ssid(api):
    assert is_valid_create_enterprise_ssid(
        create_enterprise_ssid(api)
    )


def is_valid_get_enterprise_ssid(obj):
    json_schema_validate('jsd_cca519ba45ebb423_v1_2_10').validate(obj)
    return True


def get_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.get_enterprise_ssid(
        ssid_name=NEW_ENTERPRISE_SSID_NAME,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([NEW_ENTERPRISE_SSID_NAME]) is True,
                    reason="tests.config values required not present")
@pytest.mark.non_fabric_wireless
def test_get_enterprise_ssid(api):
    assert is_valid_get_enterprise_ssid(
        get_enterprise_ssid(api)
    )


def is_valid_create_and_provision_ssid(obj):
    json_schema_validate('jsd_db9f997f4e59aec1_v1_2_10').validate(obj)
    return True


def create_and_provision_ssid(api):
    endpoint_result = api.non_fabric_wireless.create_and_provision_ssid(
        enableFabric=None,
        flexConnect=None,
        managedAPLocations=None,
        ssidDetails=None,
        ssidType=None,
        vlanAndDynamicInterfaceDetails=None,
        payload={},
        active_validation=True
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_create_and_provision_ssid(api):
    assert is_valid_create_and_provision_ssid(
        create_and_provision_ssid(api)
    )


def is_valid_delete_and_provision_ssid(obj):
    json_schema_validate('jsd_cca098344a489dfa_v1_2_10').validate(obj)
    return True


def delete_and_provision_ssid(api):
    endpoint_result = api.non_fabric_wireless.delete_and_provision_ssid(
        managed_aplocations=NEW_MANAGED_APLOCATIONS,
        ssid_name=NEW_ENTERPRISE_SSID_NAME,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([NEW_MANAGED_APLOCATIONS, NEW_ENTERPRISE_SSID_NAME]) is True,
                    reason="tests.config values required not present")
@pytest.mark.non_fabric_wireless
def test_delete_and_provision_ssid(api):
    assert is_valid_delete_and_provision_ssid(
        delete_and_provision_ssid(api)
    )


def is_valid_delete_enterprise_ssid(obj):
    json_schema_validate('jsd_c7a6592b4b98a369_v1_2_10').validate(obj)
    return True


def delete_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.delete_enterprise_ssid(
        ssid_name=NEW_ENTERPRISE_SSID_NAME,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([NEW_ENTERPRISE_SSID_NAME]) is True,
                    reason="tests.config values required not present")
@pytest.mark.non_fabric_wireless
def test_delete_enterprise_ssid(api):
    assert is_valid_delete_enterprise_ssid(
        delete_enterprise_ssid(api)
    )

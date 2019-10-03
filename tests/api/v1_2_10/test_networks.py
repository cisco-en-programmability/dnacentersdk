# -*- coding: utf-8 -*-
"""DNACenterAPI networks API fixtures and tests.

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


def is_valid_get_vlan_details(obj):
    json_schema_validate('jsd_6284db4649aa8d31_v1_2_10').validate(obj)
    return True


def get_vlan_details(api):
    endpoint_result = api.networks.get_vlan_details(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.networks
def test_get_vlan_details(api):
    assert is_valid_get_vlan_details(
        get_vlan_details(api)
    )


def is_valid_get_site_topology(obj):
    json_schema_validate('jsd_9ba14a9e441b8a60_v1_2_10').validate(obj)
    return True


def get_site_topology(api):
    endpoint_result = api.networks.get_site_topology(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.networks
def test_get_site_topology(api):
    assert is_valid_get_site_topology(
        get_site_topology(api)
    )


def is_valid_get_physical_topology(obj):
    json_schema_validate('jsd_b2b8cb91459aa58f_v1_2_10').validate(obj)
    return True


def get_physical_topology(api):
    endpoint_result = api.networks.get_physical_topology(
        node_type=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.networks
def test_get_physical_topology(api):
    assert is_valid_get_physical_topology(
        get_physical_topology(api)
    )


def is_valid_get_l3_topology_details(obj):
    json_schema_validate('jsd_c2b5fb764d888375_v1_2_10').validate(obj)
    return True


def get_l3_topology_details(api):
    endpoint_result = api.networks.get_l3_topology_details(
        topology_type='OSPF',
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.networks
def test_get_l3_topology_details(api):
    assert is_valid_get_l3_topology_details(
        get_l3_topology_details(api)
    )


def is_valid_get_topology_details(obj):
    json_schema_validate('jsd_b9b48ac8463a8aba_v1_2_10').validate(obj)
    return True


def get_topology_details(api):
    endpoint_result = api.networks.get_topology_details(
        vlan_id=get_vlan_details(api).response[0],
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.networks
def test_get_topology_details(api):
    assert is_valid_get_topology_details(
        get_topology_details(api)
    )


def is_valid_get_overall_network_health(obj):
    json_schema_validate('jsd_ca91da84401abba1_v1_2_10').validate(obj)
    return True


def get_overall_network_health(api):
    endpoint_result = api.networks.get_overall_network_health(
        timestamp=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.networks
def test_get_overall_network_health(api):
    assert is_valid_get_overall_network_health(
        get_overall_network_health(api)
    )

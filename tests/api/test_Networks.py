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




# 6284-db46-49aa-8d31
def is_valid_get_vlan_details(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_vlan_details(api):
    endpoint_result = api.networks.get_vlan_details( payload = '' )
    return endpoint_result


def test_get_vlan_details(api):
    assert is_valid_get_vlan_details(get_vlan_details(api))


# 9ba1-4a9e-441b-8a60
def is_valid_get_site_topology(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_site_topology(api):
    endpoint_result = api.networks.get_site_topology( payload = '' )
    return endpoint_result


def test_get_site_topology(api):
    assert is_valid_get_site_topology(get_site_topology(api))


# b2b8-cb91-459a-a58f
def is_valid_get_physical_topology(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_physical_topology(api):
    endpoint_result = api.networks.get_physical_topology( param_node_type = None, payload = '' )
    return endpoint_result


def test_get_physical_topology(api):
    assert is_valid_get_physical_topology(get_physical_topology(api))


# c2b5-fb76-4d88-8375
def is_valid_get_l3_topology_details(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_l3_topology_details(api):
    endpoint_result = api.networks.get_l3_topology_details( path_param_topology_type = 'OSPF', payload = '' )
    return endpoint_result


def test_get_l3_topology_details(api):
    assert is_valid_get_l3_topology_details(get_l3_topology_details(api))


# b9b4-8ac8-463a-8aba
def is_valid_get_topology_details(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_topology_details(api):
    endpoint_result = api.networks.get_topology_details( path_param_vlan_id = get_vlan_details(api).response[0], payload = '' )
    return endpoint_result


def test_get_topology_details(api):
    assert is_valid_get_topology_details(get_topology_details(api))


# ca91-da84-401a-bba1
def is_valid_get_overall_network_health(obj):
    some_keys = ['executionId', 'executionStatusUrl', 'message']
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_overall_network_health(api):
    endpoint_result = api.networks.get_overall_network_health( param_timestamp = '1563231300', payload = '' )
    return endpoint_result


def test_get_overall_network_health(api):
    assert is_valid_get_overall_network_health(get_overall_network_health(api))


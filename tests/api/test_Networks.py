# networks

import pytest
import dnacentersdk


def is_valid_get_vlan_details(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_vlan_details(api):
    endpoint_result = api.networks.get_vlan_details( )
    assert is_valid_get_vlan_details(endpoint_result)


def is_valid_get_site_topology(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_site_topology(api):
    endpoint_result = api.networks.get_site_topology( )
    assert is_valid_get_site_topology(endpoint_result)


def is_valid_get_physical_topology(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_physical_topology(api):
    endpoint_result = api.networks.get_physical_topology( param_node_type = None)
    assert is_valid_get_physical_topology(endpoint_result)


def is_valid_get_l3_topology_details(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_l3_topology_details(api):
    endpoint_result = api.networks.get_l3_topology_details( path_param_topology_type = '')
    assert is_valid_get_l3_topology_details(endpoint_result)


def is_valid_get_topology_details(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_topology_details(api):
    endpoint_result = api.networks.get_topology_details( path_param_vlan_i_d = '')
    assert is_valid_get_topology_details(endpoint_result)


def is_valid_get_overall_network_health(obj):
    some_keys = [ 'version', 'response', 'measuredBy', 'latestMeasuredByEntity' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_overall_network_health(api):
    endpoint_result = api.networks.get_overall_network_health( param_timestamp = '1560378327')
    assert is_valid_get_overall_network_health(endpoint_result)


# networks

import pytest
import dnacentersdk


# 6284-db46-49aa-8d31
def is_valid_get_vlan_details(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 6284-db46-49aa-8d31
def get_vlan_details(api):
    endpoint_result = api.networks.get_vlan_details(  )
    return endpoint_result

# 6284-db46-49aa-8d31
def test_get_vlan_details(api):
    assert is_valid_get_vlan_details(get_vlan_details(api))


# 9ba1-4a9e-441b-8a60
def is_valid_get_site_topology(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 9ba1-4a9e-441b-8a60
def get_site_topology(api):
    endpoint_result = api.networks.get_site_topology(  )
    return endpoint_result

# 9ba1-4a9e-441b-8a60
def test_get_site_topology(api):
    assert is_valid_get_site_topology(get_site_topology(api))


# b2b8-cb91-459a-a58f
def is_valid_get_physical_topology(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# b2b8-cb91-459a-a58f
def get_physical_topology(api):
    endpoint_result = api.networks.get_physical_topology( param_node_type = None )
    return endpoint_result

# b2b8-cb91-459a-a58f
def test_get_physical_topology(api):
    assert is_valid_get_physical_topology(get_physical_topology(api))


# c2b5-fb76-4d88-8375
def is_valid_get_l3_topology_details(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# c2b5-fb76-4d88-8375
def get_l3_topology_details(api):
    endpoint_result = api.networks.get_l3_topology_details( path_param_topology_type = 'OSPF' )
    return endpoint_result

# c2b5-fb76-4d88-8375
def test_get_l3_topology_details(api):
    assert is_valid_get_l3_topology_details(get_l3_topology_details(api))


# b9b4-8ac8-463a-8aba
def is_valid_get_topology_details(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# b9b4-8ac8-463a-8aba
def get_topology_details(api):
    endpoint_result = api.networks.get_topology_details( path_param_vlan_id = get_vlan_details(api).response[0] )
    return endpoint_result

# b9b4-8ac8-463a-8aba
def test_get_topology_details(api):
    assert is_valid_get_topology_details(get_topology_details(api))


# ca91-da84-401a-bba1
def is_valid_get_overall_network_health(obj):
    some_keys = ['executionId', 'executionStatusUrl', 'message']
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# ca91-da84-401a-bba1
def get_overall_network_health(api):
    endpoint_result = api.networks.get_overall_network_health( param_timestamp = '1561076614' )
    return endpoint_result

# ca91-da84-401a-bba1
def test_get_overall_network_health(api):
    assert is_valid_get_overall_network_health(get_overall_network_health(api))


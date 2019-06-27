# -*- coding: utf-8 -*-
"""DNACenterAPI network_discovery API fixtures and tests.

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




# 069d-9823-451b-892d
def is_valid_get_count_of_all_discovery_jobs(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_count_of_all_discovery_jobs(api):
    endpoint_result = api.network_discovery.get_count_of_all_discovery_jobs( payload = '' )
    return endpoint_result


def test_get_count_of_all_discovery_jobs(api):
    assert is_valid_get_count_of_all_discovery_jobs(get_count_of_all_discovery_jobs(api))


# 4497-4ba5-435a-801d
def is_valid_get_snmp_properties(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_snmp_properties(api):
    endpoint_result = api.network_discovery.get_snmp_properties( payload = '' )
    return endpoint_result


def test_get_snmp_properties(api):
    assert is_valid_get_snmp_properties(get_snmp_properties(api))


# 33b7-99d0-4d0a-8907
def is_valid_get_discoveries_by_range(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_discoveries_by_range(api):
    endpoint_result = api.network_discovery.get_discoveries_by_range( path_param_records_to_return = 5, path_param_start_index = 1, payload = '' )
    return endpoint_result


def test_get_discoveries_by_range(api):
    assert is_valid_get_discoveries_by_range(get_discoveries_by_range(api))


# 3d9b-99c3-4339-8a27
def is_valid_get_network_devices_from_discovery(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_network_devices_from_discovery(api):
    endpoint_result = api.network_discovery.get_network_devices_from_discovery( path_param_id = get_discoveries_by_range(api).response[0].id, param_cli_status = None, param_http_status = None, param_ip_address = None, param_netconf_status = None, param_ping_status = None, param_snmp_status = None, param_sort_by = None, param_sort_order = None, param_task_id = None, payload = '' )
    return endpoint_result


def test_get_network_devices_from_discovery(api):
    assert is_valid_get_network_devices_from_discovery(get_network_devices_from_discovery(api))


# 63bb-88b7-4f59-aa17
def is_valid_get_discovery_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_discovery_by_id(api):
    endpoint_result = api.network_discovery.get_discovery_by_id( path_param_id = get_discoveries_by_range(api).response[0].id, payload = '' )
    return endpoint_result


def test_get_discovery_by_id(api):
    assert is_valid_get_discovery_by_id(get_discovery_by_id(api))


# 9987-2a13-4d0a-9fb4
def is_valid_get_list_of_discoveries_by_discovery_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_list_of_discoveries_by_discovery_id(api):
    endpoint_result = api.network_discovery.get_list_of_discoveries_by_discovery_id( path_param_id = get_discoveries_by_range(api).response[0].id, param_ip_address = None, param_limit = None, param_offset = None, payload = '' )
    return endpoint_result


def test_get_list_of_discoveries_by_discovery_id(api):
    assert is_valid_get_list_of_discoveries_by_discovery_id(get_list_of_discoveries_by_discovery_id(api))


# a496-7be6-4dfa-aa1a
def is_valid_get_discovery_jobs_by_ip(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_discovery_jobs_by_ip(api):
    endpoint_result = api.network_discovery.get_discovery_jobs_by_ip( param_ip_address = get_discoveries_by_range(api).response[0].ipAddressList.split('-')[0], param_limit = None, param_name = None, param_offset = None, payload = '' )
    return endpoint_result


def test_get_discovery_jobs_by_ip(api):
    assert is_valid_get_discovery_jobs_by_ip(get_discovery_jobs_by_ip(api))


# a6b7-98ab-4aca-a34e
def is_valid_get_discovered_devices_by_range(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_discovered_devices_by_range(api):
    endpoint_result = api.network_discovery.get_discovered_devices_by_range( path_param_id = get_discoveries_by_range(api).response[1].id, path_param_records_to_return = 3, path_param_start_index = 1, param_task_id = None, payload = '' )
    return endpoint_result


def test_get_discovered_devices_by_range(api):
    assert is_valid_get_discovered_devices_by_range(get_discovered_devices_by_range(api))


# a696-5b45-4c9a-8663
def is_valid_get_devices_discovered_by_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_devices_discovered_by_id(api):
    endpoint_result = api.network_discovery.get_devices_discovered_by_id( path_param_id = get_discoveries_by_range(api).response[0].id, param_task_id = None, payload = '' )
    return endpoint_result


def test_get_devices_discovered_by_id(api):
    assert is_valid_get_devices_discovered_by_id(get_devices_discovered_by_id(api))


# ff81-6b8e-4358-97eb
def is_valid_get_global_credentials(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_global_credentials(api):
    endpoint_result = api.network_discovery.get_global_credentials( param_credential_sub_type = 'CLI', param_order = None, param_sort_by = None, payload = '' )
    return endpoint_result


def test_get_global_credentials(api):
    assert is_valid_get_global_credentials(get_global_credentials(api))


# 58a3-699e-489b-9529
def is_valid_get_credential_sub_type_by_credential_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_credential_sub_type_by_credential_id(api):
    endpoint_result = api.network_discovery.get_credential_sub_type_by_credential_id( path_param_id = get_global_credentials(api).response[0].id, payload = '' )
    return endpoint_result


def test_get_credential_sub_type_by_credential_id(api):
    assert is_valid_get_credential_sub_type_by_credential_id(get_credential_sub_type_by_credential_id(api))


# f6ac-994f-451b-a011
def is_valid_get_discovered_network_devices_by_discovery_id(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_discovered_network_devices_by_discovery_id(api):
    endpoint_result = api.network_discovery.get_discovered_network_devices_by_discovery_id( path_param_id = get_discoveries_by_range(api).response[0].id, param_task_id = None, payload = '' )
    return endpoint_result


def test_get_discovered_network_devices_by_discovery_id(api):
    assert is_valid_get_discovered_network_devices_by_discovery_id(get_discovered_network_devices_by_discovery_id(api))


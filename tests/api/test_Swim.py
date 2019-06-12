# swim

import pytest
import dnacentersdk


def is_valid_get_software_image_details(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_software_image_details(api):
    endpoint_result = api.swim.get_software_image_details( param_application_type = None, param_created_time = None, param_family = None, param_image_integrity_status = None, param_image_name = None, param_image_series = None, param_image_size_greater_than = None, param_image_size_lesser_than = None, param_image_uuid = None, param_is_c_c_o_latest = None, param_is_c_c_o_recommended = None, param_is_tagged_golden = None, param_limit = None, param_name = None, param_offset = None, param_sort_by = None, param_sort_order = 'asc', param_version = None)
    assert is_valid_get_software_image_details(endpoint_result)


def is_valid_trigger_software_image_distribution(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_trigger_software_image_distribution(api):
    endpoint_result = api.swim.trigger_software_image_distribution( )
    assert is_valid_trigger_software_image_distribution(endpoint_result)


def is_valid_import_local_software_image(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_import_local_software_image(api):
    endpoint_result = api.swim.import_local_software_image( param_is_third_party = None, param_third_party_application_type = None, param_third_party_image_family = None, param_third_party_vendor = None)
    assert is_valid_import_local_software_image(endpoint_result)


def is_valid_import_software_image_via_url(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_import_software_image_via_url(api):
    endpoint_result = api.swim.import_software_image_via_url( param_schedule_at = None, param_schedule_desc = None, param_schedule_origin = None)
    assert is_valid_import_software_image_via_url(endpoint_result)


def is_valid_trigger_software_image_activation(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_trigger_software_image_activation(api):
    endpoint_result = api.swim.trigger_software_image_activation( param_schedule_validate = None)
    assert is_valid_trigger_software_image_activation(endpoint_result)


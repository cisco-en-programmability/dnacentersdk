# swim

import pytest
import dnacentersdk


# 0c8f-7a0b-49b9-aedd
def is_valid_get_software_image_details(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 0c8f-7a0b-49b9-aedd
def get_software_image_details(api):
    endpoint_result = api.swim.get_software_image_details( param_application_type = None, param_created_time = None, param_family = None, param_image_integrity_status = None, param_image_name = None, param_image_series = None, param_image_size_greater_than = None, param_image_size_lesser_than = None, param_image_uuid = None, param_is_cco_latest = None, param_is_cco_recommended = None, param_is_tagged_golden = None, param_limit = None, param_name = None, param_offset = None, param_sort_by = None, param_sort_order = 'asc', param_version = None )
    return endpoint_result

# 0c8f-7a0b-49b9-aedd
def test_get_software_image_details(api):
    assert is_valid_get_software_image_details(get_software_image_details(api))


# 4dbe-3bc7-43a8-91bc
def is_valid_import_local_software_image(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 4dbe-3bc7-43a8-91bc
def import_local_software_image(api):
    endpoint_result = api.swim.import_local_software_image( param_is_third_party = None, param_third_party_application_type = None, param_third_party_image_family = None, param_third_party_vendor = None )
    return endpoint_result

# 4dbe-3bc7-43a8-91bc
@pytest.mark.skip(reason="no way of currently testing this")
def test_import_local_software_image(api):
    assert is_valid_import_local_software_image(import_local_software_image(api))


# bc8a-ab47-46ca-883d
def is_valid_import_software_image_via_url(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# bc8a-ab47-46ca-883d
def import_software_image_via_url(api):
    endpoint_result = api.swim.import_software_image_via_url( param_schedule_at = None, param_schedule_desc = None, param_schedule_origin = None )
    return endpoint_result

# bc8a-ab47-46ca-883d
def test_import_software_image_via_url(api):
    assert is_valid_import_software_image_via_url(import_software_image_via_url(api))


# fb9b-eb66-4f2a-ba4c
def is_valid_trigger_software_image_activation(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# fb9b-eb66-4f2a-ba4c
def trigger_software_image_activation(api):
    endpoint_result = api.swim.trigger_software_image_activation( param_schedule_validate = None )
    return endpoint_result

# fb9b-eb66-4f2a-ba4c
def test_trigger_software_image_activation(api):
    assert is_valid_trigger_software_image_activation(trigger_software_image_activation(api))


# 8cb6-783b-4fab-a1f4
def is_valid_trigger_software_image_distribution(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 8cb6-783b-4fab-a1f4
def trigger_software_image_distribution(api):
    endpoint_result = api.swim.trigger_software_image_distribution(  )
    return endpoint_result

# 8cb6-783b-4fab-a1f4
def test_trigger_software_image_distribution(api):
    assert is_valid_trigger_software_image_distribution(trigger_software_image_distribution(api))


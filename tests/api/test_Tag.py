# tag

import pytest
import dnacentersdk


# 1399-891c-42a8-be64
def is_valid_create_tag(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 1399-891c-42a8-be64
def create_tag(api):
    endpoint_result = api.tag.create_tag( rq_description = None, rq_dynamicRules = None, rq_id = None, rq_instanceTenantId = None, rq_name = 'InterestingTool01', rq_systemTag = None )
    return endpoint_result

# 1399-891c-42a8-be64
def test_create_tag(api):
    assert is_valid_create_tag(create_tag(api))


# ee9a-ab01-487a-8896
def is_valid_get_tag(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# ee9a-ab01-487a-8896
def get_tag(api):
    endpoint_result = api.tag.get_tag( param_additional_info_attributes = None, param_additional_info_name_space = None, param_field = None, param_level = None, param_limit = None, param_name = None, param_offset = None, param_order = 'des', param_size = None, param_sort_by = 'name', param_system_tag = None )
    return endpoint_result

# ee9a-ab01-487a-8896
def test_get_tag(api):
    assert is_valid_get_tag(get_tag(api))


# c1a3-59b1-4c89-b573
def is_valid_get_tag_by_id(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# c1a3-59b1-4c89-b573
def get_tag_by_id(api):
    endpoint_result = api.tag.get_tag_by_id( path_param_id = get_tag(api).response[0].id )
    return endpoint_result

# c1a3-59b1-4c89-b573
def test_get_tag_by_id(api):
    assert is_valid_get_tag_by_id(get_tag_by_id(api))


# 8091-a9b8-4bfb-a53b
def is_valid_get_tag_count(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 8091-a9b8-4bfb-a53b
def get_tag_count(api):
    endpoint_result = api.tag.get_tag_count( param_attribute_name = None, param_level = None, param_name = None, param_name_space = None, param_size = None, param_system_tag = None )
    return endpoint_result

# 8091-a9b8-4bfb-a53b
def test_get_tag_count(api):
    assert is_valid_get_tag_count(get_tag_count(api))


# 4695-090d-403b-8eaa
def is_valid_get_tag_resource_types(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 4695-090d-403b-8eaa
def get_tag_resource_types(api):
    endpoint_result = api.tag.get_tag_resource_types(  )
    return endpoint_result

# 4695-090d-403b-8eaa
def test_get_tag_resource_types(api):
    assert is_valid_get_tag_resource_types(get_tag_resource_types(api))


# 2e9d-b858-40fb-b1cf
def is_valid_get_tag_member_count(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 2e9d-b858-40fb-b1cf
def get_tag_member_count(api):
    endpoint_result = api.tag.get_tag_member_count( param_member_type = get_tag_resource_types(api).response[0], path_param_id = get_tag(api).response[0].id, param_level = '0', param_member_association_type = None )
    return endpoint_result

# 2e9d-b858-40fb-b1cf
def test_get_tag_member_count(api):
    assert is_valid_get_tag_member_count(get_tag_member_count(api))


# 45bc-7a83-44a8-bc1e
def is_valid_updates_tag_membership(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 45bc-7a83-44a8-bc1e
def updates_tag_membership(api):
    endpoint_result = api.tag.updates_tag_membership( rq_memberToTags = [{'key': ['get_tag(api).response[0].id']}], rq_memberType = get_tag_resource_types(api).response[0] )
    return endpoint_result

# 45bc-7a83-44a8-bc1e
@pytest.mark.skip(reason="no way of currently testing this")
def test_updates_tag_membership(api):
    assert is_valid_updates_tag_membership(updates_tag_membership(api))


# 00a2-fa61-4608-9317
def is_valid_add_members_to_the_tag(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 00a2-fa61-4608-9317
def add_members_to_the_tag(api):
    endpoint_result = api.tag.add_members_to_the_tag( path_param_id = get_tag(api).response[0].id )
    return endpoint_result

# 00a2-fa61-4608-9317
@pytest.mark.skip(reason="no way of currently testing this")
def test_add_members_to_the_tag(api):
    assert is_valid_add_members_to_the_tag(add_members_to_the_tag(api))


# eab7-abe0-48fb-99ad
def is_valid_get_tag_members_by_id(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# eab7-abe0-48fb-99ad
def get_tag_members_by_id(api):
    endpoint_result = api.tag.get_tag_members_by_id( param_member_type = get_tag_resource_types(api).response[0], path_param_id = get_tag(api).response[0].id, param_level = '0', param_limit = None, param_member_association_type = None, param_offset = None )
    return endpoint_result

# eab7-abe0-48fb-99ad
def test_get_tag_members_by_id(api):
    assert is_valid_get_tag_members_by_id(get_tag_members_by_id(api))


# 4d86-a993-469a-9da9
def is_valid_update_tag(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 4d86-a993-469a-9da9
def update_tag(api):
    endpoint_result = api.tag.update_tag( rq_description = None, rq_dynamicRules = None, rq_id = get_tag(api).response[0].id, rq_instanceTenantId = None, rq_name = '{} Updated'.format(get_tag(api).response[0].name), rq_systemTag = None )
    return endpoint_result

# 4d86-a993-469a-9da9
def test_update_tag(api):
    assert is_valid_update_tag(update_tag(api))


# 429c-2815-4bda-a13d
def is_valid_delete_tag(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 429c-2815-4bda-a13d
def delete_tag(api):
    endpoint_result = api.tag.delete_tag( path_param_id = get_tag(api).response[0].id )
    return endpoint_result

# 429c-2815-4bda-a13d
def test_delete_tag(api):
    assert is_valid_delete_tag(delete_tag(api))


# caa3-ea70-4d78-b37e
def is_valid_remove_tag_member(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# caa3-ea70-4d78-b37e
def remove_tag_member(api):
    endpoint_result = api.tag.remove_tag_member( path_param_id = get_tag(api).response[0].id, path_param_member_id = get_tag_resource_types(api).response[0] )
    return endpoint_result

# caa3-ea70-4d78-b37e
@pytest.mark.skip(reason="no way of currently testing this")
def test_remove_tag_member(api):
    assert is_valid_remove_tag_member(remove_tag_member(api))


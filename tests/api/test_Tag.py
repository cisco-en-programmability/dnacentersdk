# tag

import pytest
import dnacentersdk


def is_valid_add_members_to_the_tag(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_add_members_to_the_tag(api):
    endpoint_result = api.tag.add_members_to_the_tag( path_param_id = '')
    assert is_valid_add_members_to_the_tag(endpoint_result)


def is_valid_get_tag_member_count(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_tag_member_count(api):
    endpoint_result = api.tag.get_tag_member_count( param_member_type = '', path_param_id = '', param_level = '0', param_member_association_type = None)
    assert is_valid_get_tag_member_count(endpoint_result)


def is_valid_create_tag(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_create_tag(api):
    endpoint_result = api.tag.create_tag( rq_description = None, rq_dynamicRules = None, rq_id = None, rq_instanceTenantId = None, rq_name = None, rq_systemTag = None)
    assert is_valid_create_tag(endpoint_result)


def is_valid_get_tag_resource_types(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_tag_resource_types(api):
    endpoint_result = api.tag.get_tag_resource_types( )
    assert is_valid_get_tag_resource_types(endpoint_result)


def is_valid_updates_tag_membership(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_updates_tag_membership(api):
    endpoint_result = api.tag.updates_tag_membership( rq_memberToTags = None, rq_memberType = None)
    assert is_valid_updates_tag_membership(endpoint_result)


def is_valid_update_tag(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_update_tag(api):
    endpoint_result = api.tag.update_tag( rq_description = None, rq_dynamicRules = None, rq_id = None, rq_instanceTenantId = None, rq_name = None, rq_systemTag = None)
    assert is_valid_update_tag(endpoint_result)


def is_valid_get_tag_count(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_tag_count(api):
    endpoint_result = api.tag.get_tag_count( param_attribute_name = None, param_level = None, param_name = None, param_name_space = None, param_size = None, param_system_tag = None)
    assert is_valid_get_tag_count(endpoint_result)


def is_valid_delete_tag(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_tag(api):
    endpoint_result = api.tag.delete_tag( path_param_id = '')
    assert is_valid_delete_tag(endpoint_result)


def is_valid_remove_tag_member(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_remove_tag_member(api):
    endpoint_result = api.tag.remove_tag_member( path_param_id = '', path_param_member_id = '')
    assert is_valid_remove_tag_member(endpoint_result)


def is_valid_get_tag_members_by_id(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_tag_members_by_id(api):
    endpoint_result = api.tag.get_tag_members_by_id( param_member_type = '', path_param_id = '', param_level = '0', param_limit = None, param_member_association_type = None, param_offset = None)
    assert is_valid_get_tag_members_by_id(endpoint_result)


def is_valid_get_tag_by_id(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_tag_by_id(api):
    endpoint_result = api.tag.get_tag_by_id( path_param_id = '')
    assert is_valid_get_tag_by_id(endpoint_result)


def is_valid_get_tag(obj):
    some_keys = [ 'version' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_tag(api):
    endpoint_result = api.tag.get_tag( param_additional_info_attributes = None, param_additional_info_name_space = None, param_field = None, param_level = None, param_limit = None, param_name = None, param_offset = None, param_order = None, param_size = None, param_sort_by = None, param_system_tag = None)
    assert is_valid_get_tag(endpoint_result)


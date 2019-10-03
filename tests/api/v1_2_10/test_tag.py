# -*- coding: utf-8 -*-
"""DNACenterAPI tag API fixtures and tests.

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


def is_valid_create_tag(obj):
    json_schema_validate('jsd_1399891c42a8be64_v1_2_10').validate(obj)
    return True


def create_tag(api):
    endpoint_result = api.tag.create_tag(
        description=None,
        dynamicRules=None,
        id=None,
        instanceTenantId=None,
        name='InterestingTool01',
        systemTag=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_create_tag(api):
    assert is_valid_create_tag(
        create_tag(api)
    )


def is_valid_get_tag(obj):
    json_schema_validate('jsd_ee9aab01487a8896_v1_2_10').validate(obj)
    return True


def get_tag(api):
    endpoint_result = api.tag.get_tag(
        additional_info_attributes=None,
        additional_info_name_space=None,
        field=None,
        level=None,
        limit=None,
        name=None,
        offset=None,
        order='des',
        size=None,
        sort_by='name',
        system_tag=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag(api):
    assert is_valid_get_tag(
        get_tag(api)
    )


def is_valid_get_tag_created(obj):
    json_schema_validate('jsd_ee9aab01487a8896_v1_2_10').validate(obj)
    return True


def get_tag_created(api):
    endpoint_result = api.tag.get_tag(
        additional_info_attributes=None,
        additional_info_name_space=None,
        field=None,
        level=None,
        limit=None,
        name='InterestingTool01',
        offset=None,
        order=None,
        size=None,
        sort_by=None,
        system_tag=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_created(api):
    assert is_valid_get_tag_created(
        get_tag_created(api)
    )


def is_valid_get_tag_by_id(obj):
    json_schema_validate('jsd_c1a359b14c89b573_v1_2_10').validate(obj)
    return True


def get_tag_by_id(api):
    endpoint_result = api.tag.get_tag_by_id(
        id=get_tag(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_by_id(api):
    assert is_valid_get_tag_by_id(
        get_tag_by_id(api)
    )


def is_valid_get_tag_by_id_created(obj):
    json_schema_validate('jsd_c1a359b14c89b573_v1_2_10').validate(obj)
    return True


def get_tag_by_id_created(api):
    endpoint_result = api.tag.get_tag_by_id(
        id=get_tag_created(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_by_id_created(api):
    assert is_valid_get_tag_by_id_created(
        get_tag_by_id_created(api)
    )


def is_valid_get_tag_count(obj):
    json_schema_validate('jsd_8091a9b84bfba53b_v1_2_10').validate(obj)
    return True


def get_tag_count(api):
    endpoint_result = api.tag.get_tag_count(
        attribute_name=None,
        level=None,
        name=None,
        name_space=None,
        size=None,
        system_tag=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_count(api):
    assert is_valid_get_tag_count(
        get_tag_count(api)
    )


def is_valid_get_tag_resource_types(obj):
    json_schema_validate('jsd_4695090d403b8eaa_v1_2_10').validate(obj)
    return True


def get_tag_resource_types(api):
    endpoint_result = api.tag.get_tag_resource_types(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_resource_types(api):
    assert is_valid_get_tag_resource_types(
        get_tag_resource_types(api)
    )


def is_valid_get_tag_member_count(obj):
    json_schema_validate('jsd_2e9db85840fbb1cf_v1_2_10').validate(obj)
    return True


def get_tag_member_count(api):
    endpoint_result = api.tag.get_tag_member_count(
        id=get_tag(api).response[0].id,
        member_type=get_tag_resource_types(api).response[0],
        level='0',
        member_association_type=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_member_count(api):
    assert is_valid_get_tag_member_count(
        get_tag_member_count(api)
    )


def is_valid_updates_tag_membership(obj):
    json_schema_validate('jsd_45bc7a8344a8bc1e_v1_2_10').validate(obj)
    return True


def updates_tag_membership(api):
    tag = get_tag_created(api).response[0].id
    key = api.devices.get_device_list().response[0].id
    endpoint_result = api.tag.updates_tag_membership(
        memberToTags={key: [tag]},
        memberType='networkdevice',
        payload=None,
        active_validation=False
    )
    return endpoint_result


@pytest.mark.tag
def test_updates_tag_membership(api):
    assert is_valid_updates_tag_membership(
        updates_tag_membership(api)
    )


def is_valid_add_members_to_the_tag(obj):
    json_schema_validate('jsd_00a2fa6146089317_v1_2_10').validate(obj)
    return True


def add_members_to_the_tag(api):
    endpoint_result = api.tag.add_members_to_the_tag(
        id=get_tag_created(api).response[0].id,
        payload={
            "networkdevice": [api.devices.get_device_list().response[0].id]
        },
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_add_members_to_the_tag(api):
    assert is_valid_add_members_to_the_tag(
        add_members_to_the_tag(api)
    )


def is_valid_get_tag_members_by_id(obj):
    json_schema_validate('jsd_eab7abe048fb99ad_v1_2_10').validate(obj)
    return True


def get_tag_members_by_id(api):
    endpoint_result = api.tag.get_tag_members_by_id(
        id=get_tag_created(api).response[0].id,
        member_type=get_tag_resource_types(api).response[0],
        level='0',
        limit=None,
        member_association_type=None,
        offset=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_members_by_id(api):
    assert is_valid_get_tag_members_by_id(
        get_tag_members_by_id(api)
    )


def is_valid_update_tag(obj):
    json_schema_validate('jsd_4d86a993469a9da9_v1_2_10').validate(obj)
    return True


def update_tag(api):
    tag = get_tag_created(api).response[0]
    endpoint_result = api.tag.update_tag(
        description=None,
        dynamicRules=None,
        id=tag.id,
        instanceTenantId=None,
        name='{} Updated'.format(tag.name),
        systemTag=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_update_tag(api):
    assert is_valid_update_tag(
        update_tag(api)
    )


def is_valid_remove_tag_member(obj):
    json_schema_validate('jsd_caa3ea704d78b37e_v1_2_10').validate(obj)
    return True


def remove_tag_member(api):
    tag = api.tag.get_tag(name='InterestingTool01 Updated').response[0]
    device = api.devices.get_device_list().response[0]
    endpoint_result = api.tag.remove_tag_member(
        id=tag.id,
        member_id=device.id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_remove_tag_member(api):
    assert is_valid_remove_tag_member(
        remove_tag_member(api)
    )


def is_valid_delete_tag(obj):
    json_schema_validate('jsd_429c28154bdaa13d_v1_2_10').validate(obj)
    return True


def delete_tag(api):
    tag = api.tag.get_tag(name='InterestingTool01 Updated').response[0]
    endpoint_result = api.tag.delete_tag(
        id=tag.id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.tag
def test_delete_tag(api):
    assert is_valid_delete_tag(
        delete_tag(api)
    )

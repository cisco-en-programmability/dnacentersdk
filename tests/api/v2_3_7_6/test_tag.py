# -*- coding: utf-8 -*-
"""DNACenterAPI tag API fixtures and tests.

Copyright (c) 2024 Cisco Systems.

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
from fastjsonschema.exceptions import JsonSchemaException
from dnacentersdk.exceptions import MalformedRequest
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.6', reason='version does not match')


def is_valid_update_tag_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c9f995abc21b54e7860f66aef2ffbc85_v2_3_7_6').validate(obj)
    return True


def update_tag_v1(api):
    endpoint_result = api.tag.update_tag_v1(
        active_validation=True,
        description='string',
        dynamicRules=[{'memberType': 'string', 'rules': {'values': ['string'], 'items': ['string'], 'operation': 'string', 'name': 'string', 'value': 'string'}}],
        id='string',
        instanceTenantId='string',
        name='string',
        payload=None,
        systemTag=True
    )
    return endpoint_result


@pytest.mark.tag
def test_update_tag_v1(api, validator):
    try:
        assert is_valid_update_tag_v1(
            validator,
            update_tag_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_tag_v1_default_val(api):
    endpoint_result = api.tag.update_tag_v1(
        active_validation=True,
        description=None,
        dynamicRules=None,
        id=None,
        instanceTenantId=None,
        name=None,
        payload=None,
        systemTag=None
    )
    return endpoint_result


@pytest.mark.tag
def test_update_tag_v1_default_val(api, validator):
    try:
        assert is_valid_update_tag_v1(
            validator,
            update_tag_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tag_v1(json_schema_validate, obj):
    json_schema_validate('jsd_983979a4185f5b40aabe991f8cdb2816_v2_3_7_6').validate(obj)
    return True


def get_tag_v1(api):
    endpoint_result = api.tag.get_tag_v1(
        additional_info_attributes='string',
        additional_info_name_space='string',
        field='string',
        level='string',
        limit=0,
        name='string',
        offset=0,
        order='string',
        size='string',
        sort_by='string',
        system_tag='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_v1(api, validator):
    try:
        assert is_valid_get_tag_v1(
            validator,
            get_tag_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tag_v1_default_val(api):
    endpoint_result = api.tag.get_tag_v1(
        additional_info_attributes=None,
        additional_info_name_space=None,
        field=None,
        level=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        size=None,
        sort_by=None,
        system_tag=None
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_v1_default_val(api, validator):
    try:
        assert is_valid_get_tag_v1(
            validator,
            get_tag_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_tag_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e8271b05b62c54609f74b4f2f373ad5a_v2_3_7_6').validate(obj)
    return True


def create_tag_v1(api):
    endpoint_result = api.tag.create_tag_v1(
        active_validation=True,
        description='string',
        dynamicRules=[{'memberType': 'string', 'rules': {'values': ['string'], 'items': ['string'], 'operation': 'string', 'name': 'string', 'value': 'string'}}],
        id='string',
        instanceTenantId='string',
        name='string',
        payload=None,
        systemTag=True
    )
    return endpoint_result


@pytest.mark.tag
def test_create_tag_v1(api, validator):
    try:
        assert is_valid_create_tag_v1(
            validator,
            create_tag_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_tag_v1_default_val(api):
    endpoint_result = api.tag.create_tag_v1(
        active_validation=True,
        description=None,
        dynamicRules=None,
        id=None,
        instanceTenantId=None,
        name=None,
        payload=None,
        systemTag=None
    )
    return endpoint_result


@pytest.mark.tag
def test_create_tag_v1_default_val(api, validator):
    try:
        assert is_valid_create_tag_v1(
            validator,
            create_tag_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tag_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_afb52259f7c3501ca4d8ccd277828658_v2_3_7_6').validate(obj)
    return True


def get_tag_count_v1(api):
    endpoint_result = api.tag.get_tag_count_v1(
        attribute_name='string',
        name='string',
        name_space='string',
        size='string',
        system_tag='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_count_v1(api, validator):
    try:
        assert is_valid_get_tag_count_v1(
            validator,
            get_tag_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tag_count_v1_default_val(api):
    endpoint_result = api.tag.get_tag_count_v1(
        attribute_name=None,
        name=None,
        name_space=None,
        size=None,
        system_tag=None
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_tag_count_v1(
            validator,
            get_tag_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_tag_membership_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e3934b0fb68a5ff787e65e9b7c8e6296_v2_3_7_6').validate(obj)
    return True


def update_tag_membership_v1(api):
    endpoint_result = api.tag.update_tag_membership_v1(
        active_validation=True,
        memberToTags={'key': ['string']},
        memberType='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.tag
def test_update_tag_membership_v1(api, validator):
    try:
        assert is_valid_update_tag_membership_v1(
            validator,
            update_tag_membership_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_tag_membership_v1_default_val(api):
    endpoint_result = api.tag.update_tag_membership_v1(
        active_validation=True,
        memberToTags=None,
        memberType=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.tag
def test_update_tag_membership_v1_default_val(api, validator):
    try:
        assert is_valid_update_tag_membership_v1(
            validator,
            update_tag_membership_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tag_resource_types_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9baf47897d525e5899f62e4d5bdd260b_v2_3_7_6').validate(obj)
    return True


def get_tag_resource_types_v1(api):
    endpoint_result = api.tag.get_tag_resource_types_v1(

    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_resource_types_v1(api, validator):
    try:
        assert is_valid_get_tag_resource_types_v1(
            validator,
            get_tag_resource_types_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tag_resource_types_v1_default_val(api):
    endpoint_result = api.tag.get_tag_resource_types_v1(

    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_resource_types_v1_default_val(api, validator):
    try:
        assert is_valid_get_tag_resource_types_v1(
            validator,
            get_tag_resource_types_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_tag_v1(json_schema_validate, obj):
    json_schema_validate('jsd_153ed48fc373506cb1688cff36c2cb0f_v2_3_7_6').validate(obj)
    return True


def delete_tag_v1(api):
    endpoint_result = api.tag.delete_tag_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_delete_tag_v1(api, validator):
    try:
        assert is_valid_delete_tag_v1(
            validator,
            delete_tag_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_tag_v1_default_val(api):
    endpoint_result = api.tag.delete_tag_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_delete_tag_v1_default_val(api, validator):
    try:
        assert is_valid_delete_tag_v1(
            validator,
            delete_tag_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tag_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4d65f9b9d8ad5426bdf7e55461fcf761_v2_3_7_6').validate(obj)
    return True


def get_tag_by_id_v1(api):
    endpoint_result = api.tag.get_tag_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_by_id_v1(api, validator):
    try:
        assert is_valid_get_tag_by_id_v1(
            validator,
            get_tag_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tag_by_id_v1_default_val(api):
    endpoint_result = api.tag.get_tag_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_tag_by_id_v1(
            validator,
            get_tag_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tag_members_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ff12c50ea3fb53c9a53f9c9e2c595d44_v2_3_7_6').validate(obj)
    return True


def get_tag_members_by_id_v1(api):
    endpoint_result = api.tag.get_tag_members_by_id_v1(
        id='string',
        level='string',
        limit=0,
        member_association_type='string',
        member_type='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_members_by_id_v1(api, validator):
    try:
        assert is_valid_get_tag_members_by_id_v1(
            validator,
            get_tag_members_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tag_members_by_id_v1_default_val(api):
    endpoint_result = api.tag.get_tag_members_by_id_v1(
        id='string',
        level=None,
        limit=None,
        member_association_type=None,
        member_type=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_members_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_tag_members_by_id_v1(
            validator,
            get_tag_members_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_members_to_the_tag_v1(json_schema_validate, obj):
    json_schema_validate('jsd_dcc43be0514e50fea80cfa827f13ee5c_v2_3_7_6').validate(obj)
    return True


def add_members_to_the_tag_v1(api):
    endpoint_result = api.tag.add_members_to_the_tag_v1(
        active_validation=True,
        id='string',
        memberType=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.tag
def test_add_members_to_the_tag_v1(api, validator):
    try:
        assert is_valid_add_members_to_the_tag_v1(
            validator,
            add_members_to_the_tag_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_members_to_the_tag_v1_default_val(api):
    endpoint_result = api.tag.add_members_to_the_tag_v1(
        active_validation=True,
        id='string',
        memberType=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.tag
def test_add_members_to_the_tag_v1_default_val(api, validator):
    try:
        assert is_valid_add_members_to_the_tag_v1(
            validator,
            add_members_to_the_tag_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tag_member_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_82ffacb52f745c15b40b9b352754e2e1_v2_3_7_6').validate(obj)
    return True


def get_tag_member_count_v1(api):
    endpoint_result = api.tag.get_tag_member_count_v1(
        id='string',
        member_association_type='string',
        member_type='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_member_count_v1(api, validator):
    try:
        assert is_valid_get_tag_member_count_v1(
            validator,
            get_tag_member_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tag_member_count_v1_default_val(api):
    endpoint_result = api.tag.get_tag_member_count_v1(
        id='string',
        member_association_type=None,
        member_type=None
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_member_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_tag_member_count_v1(
            validator,
            get_tag_member_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_tag_member_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5581cc9883be5c1cad1959347babb342_v2_3_7_6').validate(obj)
    return True


def remove_tag_member_v1(api):
    endpoint_result = api.tag.remove_tag_member_v1(
        id='string',
        member_id='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_remove_tag_member_v1(api, validator):
    try:
        assert is_valid_remove_tag_member_v1(
            validator,
            remove_tag_member_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def remove_tag_member_v1_default_val(api):
    endpoint_result = api.tag.remove_tag_member_v1(
        id='string',
        member_id='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_remove_tag_member_v1_default_val(api, validator):
    try:
        assert is_valid_remove_tag_member_v1(
            validator,
            remove_tag_member_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_tags_associated_with_the_interfaces_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7252c07bbbe75f63913bd83b34277d12_v2_3_7_6').validate(obj)
    return True


def retrieve_tags_associated_with_the_interfaces_v1(api):
    endpoint_result = api.tag.retrieve_tags_associated_with_the_interfaces_v1(
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.tag
def test_retrieve_tags_associated_with_the_interfaces_v1(api, validator):
    try:
        assert is_valid_retrieve_tags_associated_with_the_interfaces_v1(
            validator,
            retrieve_tags_associated_with_the_interfaces_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_tags_associated_with_the_interfaces_v1_default_val(api):
    endpoint_result = api.tag.retrieve_tags_associated_with_the_interfaces_v1(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.tag
def test_retrieve_tags_associated_with_the_interfaces_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_tags_associated_with_the_interfaces_v1(
            validator,
            retrieve_tags_associated_with_the_interfaces_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f55ae4d0c6f65207a7630fa556ba2774_v2_3_7_6').validate(obj)
    return True


def retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1(api):
    endpoint_result = api.tag.retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1(

    )
    return endpoint_result


@pytest.mark.tag
def test_retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1(
            validator,
            retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1_default_val(api):
    endpoint_result = api.tag.retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1(

    )
    return endpoint_result


@pytest.mark.tag
def test_retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1(
            validator,
            retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_the_tags_associated_with_interfaces_v1(json_schema_validate, obj):
    json_schema_validate('jsd_096f751cc2f55767b34e4c890b3fd36e_v2_3_7_6').validate(obj)
    return True


def query_the_tags_associated_with_interfaces_v1(api):
    endpoint_result = api.tag.query_the_tags_associated_with_interfaces_v1(
        active_validation=True,
        ids=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.tag
def test_query_the_tags_associated_with_interfaces_v1(api, validator):
    try:
        assert is_valid_query_the_tags_associated_with_interfaces_v1(
            validator,
            query_the_tags_associated_with_interfaces_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def query_the_tags_associated_with_interfaces_v1_default_val(api):
    endpoint_result = api.tag.query_the_tags_associated_with_interfaces_v1(
        active_validation=True,
        ids=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.tag
def test_query_the_tags_associated_with_interfaces_v1_default_val(api, validator):
    try:
        assert is_valid_query_the_tags_associated_with_interfaces_v1(
            validator,
            query_the_tags_associated_with_interfaces_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_tags_associated_with_network_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_da9595ad2c4d51eaa0d2740d18c97d3a_v2_3_7_6').validate(obj)
    return True


def retrieve_tags_associated_with_network_devices_v1(api):
    endpoint_result = api.tag.retrieve_tags_associated_with_network_devices_v1(
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.tag
def test_retrieve_tags_associated_with_network_devices_v1(api, validator):
    try:
        assert is_valid_retrieve_tags_associated_with_network_devices_v1(
            validator,
            retrieve_tags_associated_with_network_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_tags_associated_with_network_devices_v1_default_val(api):
    endpoint_result = api.tag.retrieve_tags_associated_with_network_devices_v1(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.tag
def test_retrieve_tags_associated_with_network_devices_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_tags_associated_with_network_devices_v1(
            validator,
            retrieve_tags_associated_with_network_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1(json_schema_validate, obj):
    json_schema_validate('jsd_49edcdc3299250419200cea088186337_v2_3_7_6').validate(obj)
    return True


def retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1(api):
    endpoint_result = api.tag.retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1(

    )
    return endpoint_result


@pytest.mark.tag
def test_retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1(
            validator,
            retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1_default_val(api):
    endpoint_result = api.tag.retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1(

    )
    return endpoint_result


@pytest.mark.tag
def test_retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1(
            validator,
            retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_query_the_tags_associated_with_network_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e4d083d956805f63b970be543c34eb0e_v2_3_7_6').validate(obj)
    return True


def query_the_tags_associated_with_network_devices_v1(api):
    endpoint_result = api.tag.query_the_tags_associated_with_network_devices_v1(
        active_validation=True,
        ids=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.tag
def test_query_the_tags_associated_with_network_devices_v1(api, validator):
    try:
        assert is_valid_query_the_tags_associated_with_network_devices_v1(
            validator,
            query_the_tags_associated_with_network_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def query_the_tags_associated_with_network_devices_v1_default_val(api):
    endpoint_result = api.tag.query_the_tags_associated_with_network_devices_v1(
        active_validation=True,
        ids=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.tag
def test_query_the_tags_associated_with_network_devices_v1_default_val(api, validator):
    try:
        assert is_valid_query_the_tags_associated_with_network_devices_v1(
            validator,
            query_the_tags_associated_with_network_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

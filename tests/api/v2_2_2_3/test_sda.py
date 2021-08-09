# -*- coding: utf-8 -*-
"""DNACenterAPI sda API fixtures and tests.

Copyright (c) 2019-2021 Cisco Systems.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.2.3', reason='version does not match')


def is_valid_get_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_e414dcbeeabd5a359352a0e2ad5ec3f5_v2_2_2_3').validate(obj)
    return True


def get_default_authentication_profile(api):
    endpoint_result = api.sda.get_default_authentication_profile(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_default_authentication_profile(api, validator):
    try:
        assert is_valid_get_default_authentication_profile(
            validator,
            get_default_authentication_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_default_authentication_profile_default(api):
    endpoint_result = api.sda.get_default_authentication_profile(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_default_authentication_profile_default(api, validator):
    try:
        assert is_valid_get_default_authentication_profile(
            validator,
            get_default_authentication_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_d1d42ef2f1895a82a2830bf1353e6baa_v2_2_2_3').validate(obj)
    return True


def add_default_authentication_profile(api):
    endpoint_result = api.sda.add_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_default_authentication_profile(api, validator):
    try:
        assert is_valid_add_default_authentication_profile(
            validator,
            add_default_authentication_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_default_authentication_profile_default(api):
    endpoint_result = api.sda.add_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_default_authentication_profile_default(api, validator):
    try:
        assert is_valid_add_default_authentication_profile(
            validator,
            add_default_authentication_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_0d999a1d36ee52babb6b619877dad734_v2_2_2_3').validate(obj)
    return True


def update_default_authentication_profile(api):
    endpoint_result = api.sda.update_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_default_authentication_profile(api, validator):
    try:
        assert is_valid_update_default_authentication_profile(
            validator,
            update_default_authentication_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_default_authentication_profile_default(api):
    endpoint_result = api.sda.update_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_default_authentication_profile_default(api, validator):
    try:
        assert is_valid_update_default_authentication_profile(
            validator,
            update_default_authentication_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_916231b2be8b5dda8b81620b903afe9f_v2_2_2_3').validate(obj)
    return True


def delete_default_authentication_profile(api):
    endpoint_result = api.sda.delete_default_authentication_profile(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_default_authentication_profile(api, validator):
    try:
        assert is_valid_delete_default_authentication_profile(
            validator,
            delete_default_authentication_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_default_authentication_profile_default(api):
    endpoint_result = api.sda.delete_default_authentication_profile(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_default_authentication_profile_default(api, validator):
    try:
        assert is_valid_delete_default_authentication_profile(
            validator,
            delete_default_authentication_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_adds_border_device(json_schema_validate, obj):
    json_schema_validate('jsd_b6f2d8e46cdd5f05bb06f52cd1b26fb2_v2_2_2_3').validate(obj)
    return True


def adds_border_device(api):
    endpoint_result = api.sda.adds_border_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_adds_border_device(api, validator):
    try:
        assert is_valid_adds_border_device(
            validator,
            adds_border_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def adds_border_device_default(api):
    endpoint_result = api.sda.adds_border_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_adds_border_device_default(api, validator):
    try:
        assert is_valid_adds_border_device(
            validator,
            adds_border_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_border_device_detail(json_schema_validate, obj):
    json_schema_validate('jsd_7aae881ff75d5488a5325ea949be4c5b_v2_2_2_3').validate(obj)
    return True


def gets_border_device_detail(api):
    endpoint_result = api.sda.gets_border_device_detail(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_gets_border_device_detail(api, validator):
    try:
        assert is_valid_gets_border_device_detail(
            validator,
            gets_border_device_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_border_device_detail_default(api):
    endpoint_result = api.sda.gets_border_device_detail(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_gets_border_device_detail_default(api, validator):
    try:
        assert is_valid_gets_border_device_detail(
            validator,
            gets_border_device_detail_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_border_device(json_schema_validate, obj):
    json_schema_validate('jsd_9a102ba155e35f84b7af3396aa407d02_v2_2_2_3').validate(obj)
    return True


def deletes_border_device(api):
    endpoint_result = api.sda.deletes_border_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_deletes_border_device(api, validator):
    try:
        assert is_valid_deletes_border_device(
            validator,
            deletes_border_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_border_device_default(api):
    endpoint_result = api.sda.deletes_border_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_deletes_border_device_default(api, validator):
    try:
        assert is_valid_deletes_border_device(
            validator,
            deletes_border_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_control_plane_device(json_schema_validate, obj):
    json_schema_validate('jsd_6c05702ed7075a2f9ab14c051f1ac883_v2_2_2_3').validate(obj)
    return True


def delete_control_plane_device(api):
    endpoint_result = api.sda.delete_control_plane_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_control_plane_device(api, validator):
    try:
        assert is_valid_delete_control_plane_device(
            validator,
            delete_control_plane_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_control_plane_device_default(api):
    endpoint_result = api.sda.delete_control_plane_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_control_plane_device_default(api, validator):
    try:
        assert is_valid_delete_control_plane_device(
            validator,
            delete_control_plane_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_control_plane_device(json_schema_validate, obj):
    json_schema_validate('jsd_c1a89e4a8ff15608bc6c10d7ef7389d7_v2_2_2_3').validate(obj)
    return True


def get_control_plane_device(api):
    endpoint_result = api.sda.get_control_plane_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_control_plane_device(api, validator):
    try:
        assert is_valid_get_control_plane_device(
            validator,
            get_control_plane_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_control_plane_device_default(api):
    endpoint_result = api.sda.get_control_plane_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_control_plane_device_default(api, validator):
    try:
        assert is_valid_get_control_plane_device(
            validator,
            get_control_plane_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_control_plane_device(json_schema_validate, obj):
    json_schema_validate('jsd_54ae7f02a3d051f2baf7cc087990d658_v2_2_2_3').validate(obj)
    return True


def add_control_plane_device(api):
    endpoint_result = api.sda.add_control_plane_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_control_plane_device(api, validator):
    try:
        assert is_valid_add_control_plane_device(
            validator,
            add_control_plane_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_control_plane_device_default(api):
    endpoint_result = api.sda.add_control_plane_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_control_plane_device_default(api, validator):
    try:
        assert is_valid_add_control_plane_device(
            validator,
            add_control_plane_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_info(json_schema_validate, obj):
    json_schema_validate('jsd_d12790f461c553a08142ec740db5efbf_v2_2_2_3').validate(obj)
    return True


def get_device_info(api):
    endpoint_result = api.sda.get_device_info(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_device_info(api, validator):
    try:
        assert is_valid_get_device_info(
            validator,
            get_device_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_info_default(api):
    endpoint_result = api.sda.get_device_info(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_device_info_default(api, validator):
    try:
        assert is_valid_get_device_info(
            validator,
            get_device_info_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_role_in_sda_fabric(json_schema_validate, obj):
    json_schema_validate('jsd_1ea24b22ce355a229b7fd067401ddf3a_v2_2_2_3').validate(obj)
    return True


def get_device_role_in_sda_fabric(api):
    endpoint_result = api.sda.get_device_role_in_sda_fabric(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_device_role_in_sda_fabric(api, validator):
    try:
        assert is_valid_get_device_role_in_sda_fabric(
            validator,
            get_device_role_in_sda_fabric(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_role_in_sda_fabric_default(api):
    endpoint_result = api.sda.get_device_role_in_sda_fabric(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_device_role_in_sda_fabric_default(api, validator):
    try:
        assert is_valid_get_device_role_in_sda_fabric(
            validator,
            get_device_role_in_sda_fabric_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_edge_device(json_schema_validate, obj):
    json_schema_validate('jsd_e0c7b28d55c85d49a84c1403ca14bd5f_v2_2_2_3').validate(obj)
    return True


def add_edge_device(api):
    endpoint_result = api.sda.add_edge_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_edge_device(api, validator):
    try:
        assert is_valid_add_edge_device(
            validator,
            add_edge_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_edge_device_default(api):
    endpoint_result = api.sda.add_edge_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_edge_device_default(api, validator):
    try:
        assert is_valid_add_edge_device(
            validator,
            add_edge_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_edge_device(json_schema_validate, obj):
    json_schema_validate('jsd_409b70d8c6f85254a053ab281fd9e8fc_v2_2_2_3').validate(obj)
    return True


def delete_edge_device(api):
    endpoint_result = api.sda.delete_edge_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_edge_device(api, validator):
    try:
        assert is_valid_delete_edge_device(
            validator,
            delete_edge_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_edge_device_default(api):
    endpoint_result = api.sda.delete_edge_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_edge_device_default(api, validator):
    try:
        assert is_valid_delete_edge_device(
            validator,
            delete_edge_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_edge_device(json_schema_validate, obj):
    json_schema_validate('jsd_5a2ee396d6595001acfbbcdfa25093ff_v2_2_2_3').validate(obj)
    return True


def get_edge_device(api):
    endpoint_result = api.sda.get_edge_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_edge_device(api, validator):
    try:
        assert is_valid_get_edge_device(
            validator,
            get_edge_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_edge_device_default(api):
    endpoint_result = api.sda.get_edge_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_edge_device_default(api, validator):
    try:
        assert is_valid_get_edge_device(
            validator,
            get_edge_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sda_fabric(json_schema_validate, obj):
    json_schema_validate('jsd_e14e65da844f55448c1378ca851c7d43_v2_2_2_3').validate(obj)
    return True


def delete_sda_fabric(api):
    endpoint_result = api.sda.delete_sda_fabric(
        fabric_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_sda_fabric(api, validator):
    try:
        assert is_valid_delete_sda_fabric(
            validator,
            delete_sda_fabric(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_sda_fabric_default(api):
    endpoint_result = api.sda.delete_sda_fabric(
        fabric_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_sda_fabric_default(api, validator):
    try:
        assert is_valid_delete_sda_fabric(
            validator,
            delete_sda_fabric_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sda_fabric_info(json_schema_validate, obj):
    json_schema_validate('jsd_48b7335c6b5057b183a339aa30e7c233_v2_2_2_3').validate(obj)
    return True


def get_sda_fabric_info(api):
    endpoint_result = api.sda.get_sda_fabric_info(
        fabric_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_sda_fabric_info(api, validator):
    try:
        assert is_valid_get_sda_fabric_info(
            validator,
            get_sda_fabric_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sda_fabric_info_default(api):
    endpoint_result = api.sda.get_sda_fabric_info(
        fabric_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_sda_fabric_info_default(api, validator):
    try:
        assert is_valid_get_sda_fabric_info(
            validator,
            get_sda_fabric_info_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric(json_schema_validate, obj):
    json_schema_validate('jsd_c31231005eaf51faa0bf1b651bdcb7a0_v2_2_2_3').validate(obj)
    return True


def add_fabric(api):
    endpoint_result = api.sda.add_fabric(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric(api, validator):
    try:
        assert is_valid_add_fabric(
            validator,
            add_fabric(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_default(api):
    endpoint_result = api.sda.add_fabric(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_default(api, validator):
    try:
        assert is_valid_add_fabric(
            validator,
            add_fabric_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site(json_schema_validate, obj):
    json_schema_validate('jsd_0d23f3e54f8c59caac3ca905f7bf543a_v2_2_2_3').validate(obj)
    return True


def get_site(api):
    endpoint_result = api.sda.get_site(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_site(api, validator):
    try:
        assert is_valid_get_site(
            validator,
            get_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_site_default(api):
    endpoint_result = api.sda.get_site(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_site_default(api, validator):
    try:
        assert is_valid_get_site(
            validator,
            get_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_site(json_schema_validate, obj):
    json_schema_validate('jsd_9124f9db3b115f0b8c8b3ce14bc5f975_v2_2_2_3').validate(obj)
    return True


def delete_site(api):
    endpoint_result = api.sda.delete_site(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_site(api, validator):
    try:
        assert is_valid_delete_site(
            validator,
            delete_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_site_default(api):
    endpoint_result = api.sda.delete_site(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_site_default(api, validator):
    try:
        assert is_valid_delete_site(
            validator,
            delete_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_site(json_schema_validate, obj):
    json_schema_validate('jsd_9a764c85d8df5c30b9143619d4f9cde9_v2_2_2_3').validate(obj)
    return True


def add_site(api):
    endpoint_result = api.sda.add_site(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_site(api, validator):
    try:
        assert is_valid_add_site(
            validator,
            add_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_site_default(api):
    endpoint_result = api.sda.add_site(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_site_default(api, validator):
    try:
        assert is_valid_add_site(
            validator,
            add_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sda_fabric_count(json_schema_validate, obj):
    json_schema_validate('jsd_a74fcc0d07935a06a74662dc648ac0b7_v2_2_2_3').validate(obj)
    return True


def get_sda_fabric_count(api):
    endpoint_result = api.sda.get_sda_fabric_count(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_sda_fabric_count(api, validator):
    try:
        assert is_valid_get_sda_fabric_count(
            validator,
            get_sda_fabric_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sda_fabric_count_default(api):
    endpoint_result = api.sda.get_sda_fabric_count(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_sda_fabric_count_default(api, validator):
    try:
        assert is_valid_get_sda_fabric_count(
            validator,
            get_sda_fabric_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_port_assignment_for_access_point(json_schema_validate, obj):
    json_schema_validate('jsd_e4a09bf566f35babad9e27f5eb61a86d_v2_2_2_3').validate(obj)
    return True


def add_port_assignment_for_access_point(api):
    endpoint_result = api.sda.add_port_assignment_for_access_point(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_access_point(api, validator):
    try:
        assert is_valid_add_port_assignment_for_access_point(
            validator,
            add_port_assignment_for_access_point(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_port_assignment_for_access_point_default(api):
    endpoint_result = api.sda.add_port_assignment_for_access_point(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_access_point_default(api, validator):
    try:
        assert is_valid_add_port_assignment_for_access_point(
            validator,
            add_port_assignment_for_access_point_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_assignment_for_access_point(json_schema_validate, obj):
    json_schema_validate('jsd_27bd26b08b64545bae20f60c56891576_v2_2_2_3').validate(obj)
    return True


def delete_port_assignment_for_access_point(api):
    endpoint_result = api.sda.delete_port_assignment_for_access_point(
        device_ip='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_access_point(api, validator):
    try:
        assert is_valid_delete_port_assignment_for_access_point(
            validator,
            delete_port_assignment_for_access_point(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_port_assignment_for_access_point_default(api):
    endpoint_result = api.sda.delete_port_assignment_for_access_point(
        device_ip=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_access_point_default(api, validator):
    try:
        assert is_valid_delete_port_assignment_for_access_point(
            validator,
            delete_port_assignment_for_access_point_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_assignment_for_access_point(json_schema_validate, obj):
    json_schema_validate('jsd_b035b0b3b60b5f2bb7c8c82e7f94b63b_v2_2_2_3').validate(obj)
    return True


def get_port_assignment_for_access_point(api):
    endpoint_result = api.sda.get_port_assignment_for_access_point(
        device_ip='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_access_point(api, validator):
    try:
        assert is_valid_get_port_assignment_for_access_point(
            validator,
            get_port_assignment_for_access_point(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_port_assignment_for_access_point_default(api):
    endpoint_result = api.sda.get_port_assignment_for_access_point(
        device_ip=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_access_point_default(api, validator):
    try:
        assert is_valid_get_port_assignment_for_access_point(
            validator,
            get_port_assignment_for_access_point_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_assignment_for_user_device(json_schema_validate, obj):
    json_schema_validate('jsd_072cb88b50dd5ead96ecfb4ab0390f47_v2_2_2_3').validate(obj)
    return True


def delete_port_assignment_for_user_device(api):
    endpoint_result = api.sda.delete_port_assignment_for_user_device(
        device_ip='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_user_device(api, validator):
    try:
        assert is_valid_delete_port_assignment_for_user_device(
            validator,
            delete_port_assignment_for_user_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_port_assignment_for_user_device_default(api):
    endpoint_result = api.sda.delete_port_assignment_for_user_device(
        device_ip=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_user_device_default(api, validator):
    try:
        assert is_valid_delete_port_assignment_for_user_device(
            validator,
            delete_port_assignment_for_user_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_port_assignment_for_user_device(json_schema_validate, obj):
    json_schema_validate('jsd_3af29516f0c8591da2a92523b5ab3386_v2_2_2_3').validate(obj)
    return True


def add_port_assignment_for_user_device(api):
    endpoint_result = api.sda.add_port_assignment_for_user_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_user_device(api, validator):
    try:
        assert is_valid_add_port_assignment_for_user_device(
            validator,
            add_port_assignment_for_user_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_port_assignment_for_user_device_default(api):
    endpoint_result = api.sda.add_port_assignment_for_user_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_user_device_default(api, validator):
    try:
        assert is_valid_add_port_assignment_for_user_device(
            validator,
            add_port_assignment_for_user_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_assignment_for_user_device(json_schema_validate, obj):
    json_schema_validate('jsd_a446d7327733580e9a6b661715eb4c09_v2_2_2_3').validate(obj)
    return True


def get_port_assignment_for_user_device(api):
    endpoint_result = api.sda.get_port_assignment_for_user_device(
        device_ip='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_user_device(api, validator):
    try:
        assert is_valid_get_port_assignment_for_user_device(
            validator,
            get_port_assignment_for_user_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_port_assignment_for_user_device_default(api):
    endpoint_result = api.sda.get_port_assignment_for_user_device(
        device_ip=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_user_device_default(api, validator):
    try:
        assert is_valid_get_port_assignment_for_user_device(
            validator,
            get_port_assignment_for_user_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_multicast_in_sda_fabric(json_schema_validate, obj):
    json_schema_validate('jsd_b7079a38844e56dd8f1b6b876880a02e_v2_2_2_3').validate(obj)
    return True


def add_multicast_in_sda_fabric(api):
    endpoint_result = api.sda.add_multicast_in_sda_fabric(
        active_validation=True,
        fabricSiteNameHierarchy='string',
        multicastMethod='string',
        multicastVnInfo={'virtualNetworkName': 'string', 'ipPoolName': 'string', 'externalRpIpAddress': 'string', 'ssmInfo': {}, 'ssmGroupRange': 'string', 'ssmWildcardMask': 'string'},
        muticastType='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_multicast_in_sda_fabric(api, validator):
    try:
        assert is_valid_add_multicast_in_sda_fabric(
            validator,
            add_multicast_in_sda_fabric(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_multicast_in_sda_fabric_default(api):
    endpoint_result = api.sda.add_multicast_in_sda_fabric(
        active_validation=True,
        fabricSiteNameHierarchy=None,
        multicastMethod=None,
        multicastVnInfo=None,
        muticastType=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_multicast_in_sda_fabric_default(api, validator):
    try:
        assert is_valid_add_multicast_in_sda_fabric(
            validator,
            add_multicast_in_sda_fabric_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_multicast_details_from_sda_fabric(json_schema_validate, obj):
    json_schema_validate('jsd_55c27bbb42365955bc210924e1362c34_v2_2_2_3').validate(obj)
    return True


def get_multicast_details_from_sda_fabric(api):
    endpoint_result = api.sda.get_multicast_details_from_sda_fabric(
        fabric_site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_multicast_details_from_sda_fabric(api, validator):
    try:
        assert is_valid_get_multicast_details_from_sda_fabric(
            validator,
            get_multicast_details_from_sda_fabric(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_multicast_details_from_sda_fabric_default(api):
    endpoint_result = api.sda.get_multicast_details_from_sda_fabric(
        fabric_site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_multicast_details_from_sda_fabric_default(api, validator):
    try:
        assert is_valid_get_multicast_details_from_sda_fabric(
            validator,
            get_multicast_details_from_sda_fabric_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_multicast_from_sda_fabric(json_schema_validate, obj):
    json_schema_validate('jsd_45e8e007d3e25f7fb83a6579016aea72_v2_2_2_3').validate(obj)
    return True


def delete_multicast_from_sda_fabric(api):
    endpoint_result = api.sda.delete_multicast_from_sda_fabric(
        fabric_site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_multicast_from_sda_fabric(api, validator):
    try:
        assert is_valid_delete_multicast_from_sda_fabric(
            validator,
            delete_multicast_from_sda_fabric(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_multicast_from_sda_fabric_default(api):
    endpoint_result = api.sda.delete_multicast_from_sda_fabric(
        fabric_site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_multicast_from_sda_fabric_default(api, validator):
    try:
        assert is_valid_delete_multicast_from_sda_fabric(
            validator,
            delete_multicast_from_sda_fabric_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_provisioned_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_e5bd8dbbf65253f0aadd77a62b1b8b58_v2_2_2_3').validate(obj)
    return True


def delete_provisioned_wired_device(api):
    endpoint_result = api.sda.delete_provisioned_wired_device(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_wired_device(api, validator):
    try:
        assert is_valid_delete_provisioned_wired_device(
            validator,
            delete_provisioned_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_provisioned_wired_device_default(api):
    endpoint_result = api.sda.delete_provisioned_wired_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_wired_device_default(api, validator):
    try:
        assert is_valid_delete_provisioned_wired_device(
            validator,
            delete_provisioned_wired_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_provision_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_7750d1608b2751c883a072ee3fb80228_v2_2_2_3').validate(obj)
    return True


def provision_wired_device(api):
    endpoint_result = api.sda.provision_wired_device(
        active_validation=True,
        deviceManagementIpAddress='string',
        payload=None,
        siteNameHierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_provision_wired_device(api, validator):
    try:
        assert is_valid_provision_wired_device(
            validator,
            provision_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def provision_wired_device_default(api):
    endpoint_result = api.sda.provision_wired_device(
        active_validation=True,
        deviceManagementIpAddress=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_provision_wired_device_default(api, validator):
    try:
        assert is_valid_provision_wired_device(
            validator,
            provision_wired_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_provisioned_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_d8f10868c21856eab31776f109aba2bb_v2_2_2_3').validate(obj)
    return True


def get_provisioned_wired_device(api):
    endpoint_result = api.sda.get_provisioned_wired_device(
        device_management_ip_address='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_wired_device(api, validator):
    try:
        assert is_valid_get_provisioned_wired_device(
            validator,
            get_provisioned_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_provisioned_wired_device_default(api):
    endpoint_result = api.sda.get_provisioned_wired_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_wired_device_default(api, validator):
    try:
        assert is_valid_get_provisioned_wired_device(
            validator,
            get_provisioned_wired_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_vn(json_schema_validate, obj):
    json_schema_validate('jsd_176cb9f8ad5359b2b2cbc151ac3a842a_v2_2_2_3').validate(obj)
    return True


def delete_vn(api):
    endpoint_result = api.sda.delete_vn(
        site_name_hierarchy='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_vn(api, validator):
    try:
        assert is_valid_delete_vn(
            validator,
            delete_vn(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_vn_default(api):
    endpoint_result = api.sda.delete_vn(
        site_name_hierarchy=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_vn_default(api, validator):
    try:
        assert is_valid_delete_vn(
            validator,
            delete_vn_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_vn(json_schema_validate, obj):
    json_schema_validate('jsd_cb1fe08692b85767a42b84340c4c7d53_v2_2_2_3').validate(obj)
    return True


def get_vn(api):
    endpoint_result = api.sda.get_vn(
        site_name_hierarchy='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_vn(api, validator):
    try:
        assert is_valid_get_vn(
            validator,
            get_vn(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_vn_default(api):
    endpoint_result = api.sda.get_vn(
        site_name_hierarchy=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_vn_default(api, validator):
    try:
        assert is_valid_get_vn(
            validator,
            get_vn_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_vn(json_schema_validate, obj):
    json_schema_validate('jsd_15e3a724a35854758d65a83823c88435_v2_2_2_3').validate(obj)
    return True


def add_vn(api):
    endpoint_result = api.sda.add_vn(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_vn(api, validator):
    try:
        assert is_valid_add_vn(
            validator,
            add_vn(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_vn_default(api):
    endpoint_result = api.sda.add_vn(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_vn_default(api, validator):
    try:
        assert is_valid_add_vn(
            validator,
            add_vn_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ip_pool_from_sda_virtual_network(json_schema_validate, obj):
    json_schema_validate('jsd_b88723912610599ba42292db52d1dae4_v2_2_2_3').validate(obj)
    return True


def get_ip_pool_from_sda_virtual_network(api):
    endpoint_result = api.sda.get_ip_pool_from_sda_virtual_network(
        ip_pool_name='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_ip_pool_from_sda_virtual_network(api, validator):
    try:
        assert is_valid_get_ip_pool_from_sda_virtual_network(
            validator,
            get_ip_pool_from_sda_virtual_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ip_pool_from_sda_virtual_network_default(api):
    endpoint_result = api.sda.get_ip_pool_from_sda_virtual_network(
        ip_pool_name=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_ip_pool_from_sda_virtual_network_default(api, validator):
    try:
        assert is_valid_get_ip_pool_from_sda_virtual_network(
            validator,
            get_ip_pool_from_sda_virtual_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_ip_pool_from_sda_virtual_network(json_schema_validate, obj):
    json_schema_validate('jsd_951c923d016d5401b7a9943724df3844_v2_2_2_3').validate(obj)
    return True


def delete_ip_pool_from_sda_virtual_network(api):
    endpoint_result = api.sda.delete_ip_pool_from_sda_virtual_network(
        ip_pool_name='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_ip_pool_from_sda_virtual_network(api, validator):
    try:
        assert is_valid_delete_ip_pool_from_sda_virtual_network(
            validator,
            delete_ip_pool_from_sda_virtual_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_ip_pool_from_sda_virtual_network_default(api):
    endpoint_result = api.sda.delete_ip_pool_from_sda_virtual_network(
        ip_pool_name=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_ip_pool_from_sda_virtual_network_default(api, validator):
    try:
        assert is_valid_delete_ip_pool_from_sda_virtual_network(
            validator,
            delete_ip_pool_from_sda_virtual_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_ip_pool_in_sda_virtual_network(json_schema_validate, obj):
    json_schema_validate('jsd_62b07f187b7456c8bbb6088a2f24dcee_v2_2_2_3').validate(obj)
    return True


def add_ip_pool_in_sda_virtual_network(api):
    endpoint_result = api.sda.add_ip_pool_in_sda_virtual_network(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_ip_pool_in_sda_virtual_network(api, validator):
    try:
        assert is_valid_add_ip_pool_in_sda_virtual_network(
            validator,
            add_ip_pool_in_sda_virtual_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_ip_pool_in_sda_virtual_network_default(api):
    endpoint_result = api.sda.add_ip_pool_in_sda_virtual_network(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_ip_pool_in_sda_virtual_network_default(api, validator):
    try:
        assert is_valid_add_ip_pool_in_sda_virtual_network(
            validator,
            add_ip_pool_in_sda_virtual_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_virtual_network_with_scalable_groups(json_schema_validate, obj):
    json_schema_validate('jsd_72472f5ebb9d50aab287f320d32181c0_v2_2_2_3').validate(obj)
    return True


def add_virtual_network_with_scalable_groups(api):
    endpoint_result = api.sda.add_virtual_network_with_scalable_groups(
        active_validation=True,
        payload=None,
        scalableGroupNames=['string'],
        virtualNetworkName='string',
        virtualNetworkType='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_add_virtual_network_with_scalable_groups(api, validator):
    try:
        assert is_valid_add_virtual_network_with_scalable_groups(
            validator,
            add_virtual_network_with_scalable_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_virtual_network_with_scalable_groups_default(api):
    endpoint_result = api.sda.add_virtual_network_with_scalable_groups(
        active_validation=True,
        payload=None,
        scalableGroupNames=None,
        virtualNetworkName=None,
        virtualNetworkType=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_virtual_network_with_scalable_groups_default(api, validator):
    try:
        assert is_valid_add_virtual_network_with_scalable_groups(
            validator,
            add_virtual_network_with_scalable_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_virtual_network_with_scalable_groups(json_schema_validate, obj):
    json_schema_validate('jsd_2f2e8552eabc5e5f97e1f40bcc4b4c75_v2_2_2_3').validate(obj)
    return True


def delete_virtual_network_with_scalable_groups(api):
    endpoint_result = api.sda.delete_virtual_network_with_scalable_groups(
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_virtual_network_with_scalable_groups(api, validator):
    try:
        assert is_valid_delete_virtual_network_with_scalable_groups(
            validator,
            delete_virtual_network_with_scalable_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_virtual_network_with_scalable_groups_default(api):
    endpoint_result = api.sda.delete_virtual_network_with_scalable_groups(
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_virtual_network_with_scalable_groups_default(api, validator):
    try:
        assert is_valid_delete_virtual_network_with_scalable_groups(
            validator,
            delete_virtual_network_with_scalable_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_virtual_network_with_scalable_groups(json_schema_validate, obj):
    json_schema_validate('jsd_ea4b1c052b855bd9a0e99f803e6185a5_v2_2_2_3').validate(obj)
    return True


def get_virtual_network_with_scalable_groups(api):
    endpoint_result = api.sda.get_virtual_network_with_scalable_groups(
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_virtual_network_with_scalable_groups(api, validator):
    try:
        assert is_valid_get_virtual_network_with_scalable_groups(
            validator,
            get_virtual_network_with_scalable_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_virtual_network_with_scalable_groups_default(api):
    endpoint_result = api.sda.get_virtual_network_with_scalable_groups(
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_virtual_network_with_scalable_groups_default(api, validator):
    try:
        assert is_valid_get_virtual_network_with_scalable_groups(
            validator,
            get_virtual_network_with_scalable_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_virtual_network_with_scalable_groups(json_schema_validate, obj):
    json_schema_validate('jsd_f9492367570c5f009cf8b5955790e87c_v2_2_2_3').validate(obj)
    return True


def update_virtual_network_with_scalable_groups(api):
    endpoint_result = api.sda.update_virtual_network_with_scalable_groups(
        active_validation=True,
        payload=None,
        scalableGroupNames=['string'],
        virtualNetworkName='string',
        virtualNetworkType='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_update_virtual_network_with_scalable_groups(api, validator):
    try:
        assert is_valid_update_virtual_network_with_scalable_groups(
            validator,
            update_virtual_network_with_scalable_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_virtual_network_with_scalable_groups_default(api):
    endpoint_result = api.sda.update_virtual_network_with_scalable_groups(
        active_validation=True,
        payload=None,
        scalableGroupNames=None,
        virtualNetworkName=None,
        virtualNetworkType=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_virtual_network_with_scalable_groups_default(api, validator):
    try:
        assert is_valid_update_virtual_network_with_scalable_groups(
            validator,
            update_virtual_network_with_scalable_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

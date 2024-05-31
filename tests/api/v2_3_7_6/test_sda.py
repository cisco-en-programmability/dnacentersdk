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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.6', reason='version does not match')


def is_valid_get_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_e414dcbeeabd5a359352a0e2ad5ec3f5_v2_3_7_6').validate(obj)
    return True


def get_default_authentication_profile(api):
    endpoint_result = api.sda.get_default_authentication_profile(
        authenticate_template_name='string',
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


def get_default_authentication_profile_default_val(api):
    endpoint_result = api.sda.get_default_authentication_profile(
        authenticate_template_name=None,
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_default_authentication_profile_default_val(api, validator):
    try:
        assert is_valid_get_default_authentication_profile(
            validator,
            get_default_authentication_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_d1d42ef2f1895a82a2830bf1353e6baa_v2_3_7_6').validate(obj)
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


def add_default_authentication_profile_default_val(api):
    endpoint_result = api.sda.add_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_default_authentication_profile_default_val(api, validator):
    try:
        assert is_valid_add_default_authentication_profile(
            validator,
            add_default_authentication_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_0d999a1d36ee52babb6b619877dad734_v2_3_7_6').validate(obj)
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


def update_default_authentication_profile_default_val(api):
    endpoint_result = api.sda.update_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_default_authentication_profile_default_val(api, validator):
    try:
        assert is_valid_update_default_authentication_profile(
            validator,
            update_default_authentication_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_916231b2be8b5dda8b81620b903afe9f_v2_3_7_6').validate(obj)
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


def delete_default_authentication_profile_default_val(api):
    endpoint_result = api.sda.delete_default_authentication_profile(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_default_authentication_profile_default_val(api, validator):
    try:
        assert is_valid_delete_default_authentication_profile(
            validator,
            delete_default_authentication_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_adds_border_device(json_schema_validate, obj):
    json_schema_validate('jsd_b6f2d8e46cdd5f05bb06f52cd1b26fb2_v2_3_7_6').validate(obj)
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


def adds_border_device_default_val(api):
    endpoint_result = api.sda.adds_border_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_adds_border_device_default_val(api, validator):
    try:
        assert is_valid_adds_border_device(
            validator,
            adds_border_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_border_device_detail(json_schema_validate, obj):
    json_schema_validate('jsd_7aae881ff75d5488a5325ea949be4c5b_v2_3_7_6').validate(obj)
    return True


def gets_border_device_detail(api):
    endpoint_result = api.sda.gets_border_device_detail(
        device_management_ip_address='string'
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


def gets_border_device_detail_default_val(api):
    endpoint_result = api.sda.gets_border_device_detail(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_gets_border_device_detail_default_val(api, validator):
    try:
        assert is_valid_gets_border_device_detail(
            validator,
            gets_border_device_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_border_device(json_schema_validate, obj):
    json_schema_validate('jsd_9a102ba155e35f84b7af3396aa407d02_v2_3_7_6').validate(obj)
    return True


def deletes_border_device(api):
    endpoint_result = api.sda.deletes_border_device(
        device_management_ip_address='string'
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


def deletes_border_device_default_val(api):
    endpoint_result = api.sda.deletes_border_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_deletes_border_device_default_val(api, validator):
    try:
        assert is_valid_deletes_border_device(
            validator,
            deletes_border_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_control_plane_device(json_schema_validate, obj):
    json_schema_validate('jsd_6c05702ed7075a2f9ab14c051f1ac883_v2_3_7_6').validate(obj)
    return True


def delete_control_plane_device(api):
    endpoint_result = api.sda.delete_control_plane_device(
        device_management_ip_address='string'
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


def delete_control_plane_device_default_val(api):
    endpoint_result = api.sda.delete_control_plane_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_control_plane_device_default_val(api, validator):
    try:
        assert is_valid_delete_control_plane_device(
            validator,
            delete_control_plane_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_control_plane_device(json_schema_validate, obj):
    json_schema_validate('jsd_c1a89e4a8ff15608bc6c10d7ef7389d7_v2_3_7_6').validate(obj)
    return True


def get_control_plane_device(api):
    endpoint_result = api.sda.get_control_plane_device(
        device_management_ip_address='string'
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


def get_control_plane_device_default_val(api):
    endpoint_result = api.sda.get_control_plane_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_control_plane_device_default_val(api, validator):
    try:
        assert is_valid_get_control_plane_device(
            validator,
            get_control_plane_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_control_plane_device(json_schema_validate, obj):
    json_schema_validate('jsd_54ae7f02a3d051f2baf7cc087990d658_v2_3_7_6').validate(obj)
    return True


def add_control_plane_device(api):
    endpoint_result = api.sda.add_control_plane_device(
        active_validation=True,
        deviceManagementIpAddress='string',
        payload=None,
        routeDistributionProtocol='string',
        siteNameHierarchy='string'
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


def add_control_plane_device_default_val(api):
    endpoint_result = api.sda.add_control_plane_device(
        active_validation=True,
        deviceManagementIpAddress=None,
        payload=None,
        routeDistributionProtocol=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_control_plane_device_default_val(api, validator):
    try:
        assert is_valid_add_control_plane_device(
            validator,
            add_control_plane_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_info(json_schema_validate, obj):
    json_schema_validate('jsd_d12790f461c553a08142ec740db5efbf_v2_3_7_6').validate(obj)
    return True


def get_device_info(api):
    endpoint_result = api.sda.get_device_info(
        device_management_ip_address='string'
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


def get_device_info_default_val(api):
    endpoint_result = api.sda.get_device_info(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_device_info_default_val(api, validator):
    try:
        assert is_valid_get_device_info(
            validator,
            get_device_info_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_role_in_sda_fabric(json_schema_validate, obj):
    json_schema_validate('jsd_1ea24b22ce355a229b7fd067401ddf3a_v2_3_7_6').validate(obj)
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


def get_device_role_in_sda_fabric_default_val(api):
    endpoint_result = api.sda.get_device_role_in_sda_fabric(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_device_role_in_sda_fabric_default_val(api, validator):
    try:
        assert is_valid_get_device_role_in_sda_fabric(
            validator,
            get_device_role_in_sda_fabric_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_edge_device(json_schema_validate, obj):
    json_schema_validate('jsd_e0c7b28d55c85d49a84c1403ca14bd5f_v2_3_7_6').validate(obj)
    return True


def add_edge_device(api):
    endpoint_result = api.sda.add_edge_device(
        active_validation=True,
        deviceManagementIpAddress='string',
        payload=None,
        siteNameHierarchy='string'
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


def add_edge_device_default_val(api):
    endpoint_result = api.sda.add_edge_device(
        active_validation=True,
        deviceManagementIpAddress=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_edge_device_default_val(api, validator):
    try:
        assert is_valid_add_edge_device(
            validator,
            add_edge_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_edge_device(json_schema_validate, obj):
    json_schema_validate('jsd_409b70d8c6f85254a053ab281fd9e8fc_v2_3_7_6').validate(obj)
    return True


def delete_edge_device(api):
    endpoint_result = api.sda.delete_edge_device(
        device_management_ip_address='string'
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


def delete_edge_device_default_val(api):
    endpoint_result = api.sda.delete_edge_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_edge_device_default_val(api, validator):
    try:
        assert is_valid_delete_edge_device(
            validator,
            delete_edge_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_edge_device(json_schema_validate, obj):
    json_schema_validate('jsd_5a2ee396d6595001acfbbcdfa25093ff_v2_3_7_6').validate(obj)
    return True


def get_edge_device(api):
    endpoint_result = api.sda.get_edge_device(
        device_management_ip_address='string'
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


def get_edge_device_default_val(api):
    endpoint_result = api.sda.get_edge_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_edge_device_default_val(api, validator):
    try:
        assert is_valid_get_edge_device(
            validator,
            get_edge_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site(json_schema_validate, obj):
    json_schema_validate('jsd_0d23f3e54f8c59caac3ca905f7bf543a_v2_3_7_6').validate(obj)
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


def get_site_default_val(api):
    endpoint_result = api.sda.get_site(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_site_default_val(api, validator):
    try:
        assert is_valid_get_site(
            validator,
            get_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_site(json_schema_validate, obj):
    json_schema_validate('jsd_9124f9db3b115f0b8c8b3ce14bc5f975_v2_3_7_6').validate(obj)
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


def delete_site_default_val(api):
    endpoint_result = api.sda.delete_site(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_site_default_val(api, validator):
    try:
        assert is_valid_delete_site(
            validator,
            delete_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_site(json_schema_validate, obj):
    json_schema_validate('jsd_9a764c85d8df5c30b9143619d4f9cde9_v2_3_7_6').validate(obj)
    return True


def add_site(api):
    endpoint_result = api.sda.add_site(
        active_validation=True,
        fabricName='string',
        fabricType='string',
        payload=None,
        siteNameHierarchy='string'
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


def add_site_default_val(api):
    endpoint_result = api.sda.add_site(
        active_validation=True,
        fabricName=None,
        fabricType=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_site_default_val(api, validator):
    try:
        assert is_valid_add_site(
            validator,
            add_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_port_assignment_for_access_point(json_schema_validate, obj):
    json_schema_validate('jsd_e4a09bf566f35babad9e27f5eb61a86d_v2_3_7_6').validate(obj)
    return True


def add_port_assignment_for_access_point(api):
    endpoint_result = api.sda.add_port_assignment_for_access_point(
        active_validation=True,
        authenticateTemplateName='string',
        dataIpAddressPoolName='string',
        deviceManagementIpAddress='string',
        interfaceDescription='string',
        interfaceName='string',
        payload=None,
        siteNameHierarchy='string'
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


def add_port_assignment_for_access_point_default_val(api):
    endpoint_result = api.sda.add_port_assignment_for_access_point(
        active_validation=True,
        authenticateTemplateName=None,
        dataIpAddressPoolName=None,
        deviceManagementIpAddress=None,
        interfaceDescription=None,
        interfaceName=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_access_point_default_val(api, validator):
    try:
        assert is_valid_add_port_assignment_for_access_point(
            validator,
            add_port_assignment_for_access_point_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_assignment_for_access_point(json_schema_validate, obj):
    json_schema_validate('jsd_27bd26b08b64545bae20f60c56891576_v2_3_7_6').validate(obj)
    return True


def delete_port_assignment_for_access_point(api):
    endpoint_result = api.sda.delete_port_assignment_for_access_point(
        device_management_ip_address='string',
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


def delete_port_assignment_for_access_point_default_val(api):
    endpoint_result = api.sda.delete_port_assignment_for_access_point(
        device_management_ip_address=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_access_point_default_val(api, validator):
    try:
        assert is_valid_delete_port_assignment_for_access_point(
            validator,
            delete_port_assignment_for_access_point_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_assignment_for_access_point(json_schema_validate, obj):
    json_schema_validate('jsd_b035b0b3b60b5f2bb7c8c82e7f94b63b_v2_3_7_6').validate(obj)
    return True


def get_port_assignment_for_access_point(api):
    endpoint_result = api.sda.get_port_assignment_for_access_point(
        device_management_ip_address='string',
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


def get_port_assignment_for_access_point_default_val(api):
    endpoint_result = api.sda.get_port_assignment_for_access_point(
        device_management_ip_address=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_access_point_default_val(api, validator):
    try:
        assert is_valid_get_port_assignment_for_access_point(
            validator,
            get_port_assignment_for_access_point_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_assignment_for_user_device(json_schema_validate, obj):
    json_schema_validate('jsd_072cb88b50dd5ead96ecfb4ab0390f47_v2_3_7_6').validate(obj)
    return True


def delete_port_assignment_for_user_device(api):
    endpoint_result = api.sda.delete_port_assignment_for_user_device(
        device_management_ip_address='string',
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


def delete_port_assignment_for_user_device_default_val(api):
    endpoint_result = api.sda.delete_port_assignment_for_user_device(
        device_management_ip_address=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_user_device_default_val(api, validator):
    try:
        assert is_valid_delete_port_assignment_for_user_device(
            validator,
            delete_port_assignment_for_user_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_port_assignment_for_user_device(json_schema_validate, obj):
    json_schema_validate('jsd_3af29516f0c8591da2a92523b5ab3386_v2_3_7_6').validate(obj)
    return True


def add_port_assignment_for_user_device(api):
    endpoint_result = api.sda.add_port_assignment_for_user_device(
        active_validation=True,
        authenticateTemplateName='string',
        dataIpAddressPoolName='string',
        deviceManagementIpAddress='string',
        interfaceDescription='string',
        interfaceName='string',
        interfaceNames=['string'],
        payload=None,
        scalableGroupName='string',
        siteNameHierarchy='string',
        voiceIpAddressPoolName='string'
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


def add_port_assignment_for_user_device_default_val(api):
    endpoint_result = api.sda.add_port_assignment_for_user_device(
        active_validation=True,
        authenticateTemplateName=None,
        dataIpAddressPoolName=None,
        deviceManagementIpAddress=None,
        interfaceDescription=None,
        interfaceName=None,
        interfaceNames=None,
        payload=None,
        scalableGroupName=None,
        siteNameHierarchy=None,
        voiceIpAddressPoolName=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_user_device_default_val(api, validator):
    try:
        assert is_valid_add_port_assignment_for_user_device(
            validator,
            add_port_assignment_for_user_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_assignment_for_user_device(json_schema_validate, obj):
    json_schema_validate('jsd_a446d7327733580e9a6b661715eb4c09_v2_3_7_6').validate(obj)
    return True


def get_port_assignment_for_user_device(api):
    endpoint_result = api.sda.get_port_assignment_for_user_device(
        device_management_ip_address='string',
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


def get_port_assignment_for_user_device_default_val(api):
    endpoint_result = api.sda.get_port_assignment_for_user_device(
        device_management_ip_address=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_user_device_default_val(api, validator):
    try:
        assert is_valid_get_port_assignment_for_user_device(
            validator,
            get_port_assignment_for_user_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_multicast_in_sda_fabric(json_schema_validate, obj):
    json_schema_validate('jsd_b7079a38844e56dd8f1b6b876880a02e_v2_3_7_6').validate(obj)
    return True


def add_multicast_in_sda_fabric(api):
    endpoint_result = api.sda.add_multicast_in_sda_fabric(
        active_validation=True,
        multicastMethod='string',
        multicastType='string',
        multicastVnInfo=[{'virtualNetworkName': 'string', 'ipPoolName': 'string', 'internalRpIpAddress': ['string'], 'externalRpIpAddress': 'string', 'ssmInfo': [{'ssmGroupRange': 'string', 'ssmWildcardMask': 'string'}]}],
        payload=None,
        siteNameHierarchy='string'
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


def add_multicast_in_sda_fabric_default_val(api):
    endpoint_result = api.sda.add_multicast_in_sda_fabric(
        active_validation=True,
        multicastMethod=None,
        multicastType=None,
        multicastVnInfo=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_multicast_in_sda_fabric_default_val(api, validator):
    try:
        assert is_valid_add_multicast_in_sda_fabric(
            validator,
            add_multicast_in_sda_fabric_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_multicast_details_from_sda_fabric(json_schema_validate, obj):
    json_schema_validate('jsd_55c27bbb42365955bc210924e1362c34_v2_3_7_6').validate(obj)
    return True


def get_multicast_details_from_sda_fabric(api):
    endpoint_result = api.sda.get_multicast_details_from_sda_fabric(
        site_name_hierarchy='string'
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


def get_multicast_details_from_sda_fabric_default_val(api):
    endpoint_result = api.sda.get_multicast_details_from_sda_fabric(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_multicast_details_from_sda_fabric_default_val(api, validator):
    try:
        assert is_valid_get_multicast_details_from_sda_fabric(
            validator,
            get_multicast_details_from_sda_fabric_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_multicast_from_sda_fabric(json_schema_validate, obj):
    json_schema_validate('jsd_45e8e007d3e25f7fb83a6579016aea72_v2_3_7_6').validate(obj)
    return True


def delete_multicast_from_sda_fabric(api):
    endpoint_result = api.sda.delete_multicast_from_sda_fabric(
        site_name_hierarchy='string'
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


def delete_multicast_from_sda_fabric_default_val(api):
    endpoint_result = api.sda.delete_multicast_from_sda_fabric(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_multicast_from_sda_fabric_default_val(api, validator):
    try:
        assert is_valid_delete_multicast_from_sda_fabric(
            validator,
            delete_multicast_from_sda_fabric_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_provisioned_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_e5bd8dbbf65253f0aadd77a62b1b8b58_v2_3_7_6').validate(obj)
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


def delete_provisioned_wired_device_default_val(api):
    endpoint_result = api.sda.delete_provisioned_wired_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_wired_device_default_val(api, validator):
    try:
        assert is_valid_delete_provisioned_wired_device(
            validator,
            delete_provisioned_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_re_provision_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_fd488ff002115f3b8f0ee165e5347609_v2_3_7_6').validate(obj)
    return True


def re_provision_wired_device(api):
    endpoint_result = api.sda.re_provision_wired_device(
        active_validation=True,
        deviceManagementIpAddress='string',
        payload=None,
        siteNameHierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_re_provision_wired_device(api, validator):
    try:
        assert is_valid_re_provision_wired_device(
            validator,
            re_provision_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def re_provision_wired_device_default_val(api):
    endpoint_result = api.sda.re_provision_wired_device(
        active_validation=True,
        deviceManagementIpAddress=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_re_provision_wired_device_default_val(api, validator):
    try:
        assert is_valid_re_provision_wired_device(
            validator,
            re_provision_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_provision_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_7750d1608b2751c883a072ee3fb80228_v2_3_7_6').validate(obj)
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


def provision_wired_device_default_val(api):
    endpoint_result = api.sda.provision_wired_device(
        active_validation=True,
        deviceManagementIpAddress=None,
        payload=None,
        siteNameHierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_provision_wired_device_default_val(api, validator):
    try:
        assert is_valid_provision_wired_device(
            validator,
            provision_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_provisioned_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_d8f10868c21856eab31776f109aba2bb_v2_3_7_6').validate(obj)
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


def get_provisioned_wired_device_default_val(api):
    endpoint_result = api.sda.get_provisioned_wired_device(
        device_management_ip_address=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_wired_device_default_val(api, validator):
    try:
        assert is_valid_get_provisioned_wired_device(
            validator,
            get_provisioned_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_transit_peer_network(json_schema_validate, obj):
    json_schema_validate('jsd_770a34aab91750028f4d584d36811844_v2_3_7_6').validate(obj)
    return True


def delete_transit_peer_network(api):
    endpoint_result = api.sda.delete_transit_peer_network(
        transit_peer_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_transit_peer_network(api, validator):
    try:
        assert is_valid_delete_transit_peer_network(
            validator,
            delete_transit_peer_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_transit_peer_network_default_val(api):
    endpoint_result = api.sda.delete_transit_peer_network(
        transit_peer_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_transit_peer_network_default_val(api, validator):
    try:
        assert is_valid_delete_transit_peer_network(
            validator,
            delete_transit_peer_network_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_transit_peer_network_info(json_schema_validate, obj):
    json_schema_validate('jsd_6d39e10793a45d3db229d6d3820c665a_v2_3_7_6').validate(obj)
    return True


def get_transit_peer_network_info(api):
    endpoint_result = api.sda.get_transit_peer_network_info(
        transit_peer_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_transit_peer_network_info(api, validator):
    try:
        assert is_valid_get_transit_peer_network_info(
            validator,
            get_transit_peer_network_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_transit_peer_network_info_default_val(api):
    endpoint_result = api.sda.get_transit_peer_network_info(
        transit_peer_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_transit_peer_network_info_default_val(api, validator):
    try:
        assert is_valid_get_transit_peer_network_info(
            validator,
            get_transit_peer_network_info_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_transit_peer_network(json_schema_validate, obj):
    json_schema_validate('jsd_096d7073129453698264e7519d82991c_v2_3_7_6').validate(obj)
    return True


def add_transit_peer_network(api):
    endpoint_result = api.sda.add_transit_peer_network(
        active_validation=True,
        ipTransitSettings={'routingProtocolName': 'string', 'autonomousSystemNumber': 'string'},
        payload=None,
        sdaTransitSettings={'transitControlPlaneSettings': [{'siteNameHierarchy': 'string', 'deviceManagementIpAddress': 'string'}]},
        transitPeerNetworkName='string',
        transitPeerNetworkType='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_add_transit_peer_network(api, validator):
    try:
        assert is_valid_add_transit_peer_network(
            validator,
            add_transit_peer_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_transit_peer_network_default_val(api):
    endpoint_result = api.sda.add_transit_peer_network(
        active_validation=True,
        ipTransitSettings=None,
        payload=None,
        sdaTransitSettings=None,
        transitPeerNetworkName=None,
        transitPeerNetworkType=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_transit_peer_network_default_val(api, validator):
    try:
        assert is_valid_add_transit_peer_network(
            validator,
            add_transit_peer_network_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_vn(json_schema_validate, obj):
    json_schema_validate('jsd_176cb9f8ad5359b2b2cbc151ac3a842a_v2_3_7_6').validate(obj)
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


def delete_vn_default_val(api):
    endpoint_result = api.sda.delete_vn(
        site_name_hierarchy=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_vn_default_val(api, validator):
    try:
        assert is_valid_delete_vn(
            validator,
            delete_vn_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_vn(json_schema_validate, obj):
    json_schema_validate('jsd_cb1fe08692b85767a42b84340c4c7d53_v2_3_7_6').validate(obj)
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


def get_vn_default_val(api):
    endpoint_result = api.sda.get_vn(
        site_name_hierarchy=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_vn_default_val(api, validator):
    try:
        assert is_valid_get_vn(
            validator,
            get_vn_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_vn(json_schema_validate, obj):
    json_schema_validate('jsd_15e3a724a35854758d65a83823c88435_v2_3_7_6').validate(obj)
    return True


def add_vn(api):
    endpoint_result = api.sda.add_vn(
        active_validation=True,
        payload=None,
        siteNameHierarchy='string',
        virtualNetworkName='string'
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


def add_vn_default_val(api):
    endpoint_result = api.sda.add_vn(
        active_validation=True,
        payload=None,
        siteNameHierarchy=None,
        virtualNetworkName=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_vn_default_val(api, validator):
    try:
        assert is_valid_add_vn(
            validator,
            add_vn_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_virtual_network_summary(json_schema_validate, obj):
    json_schema_validate('jsd_ccf5ce99e049525f8184fcaa5991d919_v2_3_7_6').validate(obj)
    return True


def get_virtual_network_summary(api):
    endpoint_result = api.sda.get_virtual_network_summary(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_virtual_network_summary(api, validator):
    try:
        assert is_valid_get_virtual_network_summary(
            validator,
            get_virtual_network_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_virtual_network_summary_default_val(api):
    endpoint_result = api.sda.get_virtual_network_summary(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_virtual_network_summary_default_val(api, validator):
    try:
        assert is_valid_get_virtual_network_summary(
            validator,
            get_virtual_network_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ip_pool_from_sda_virtual_network(json_schema_validate, obj):
    json_schema_validate('jsd_b88723912610599ba42292db52d1dae4_v2_3_7_6').validate(obj)
    return True


def get_ip_pool_from_sda_virtual_network(api):
    endpoint_result = api.sda.get_ip_pool_from_sda_virtual_network(
        ip_pool_name='string',
        site_name_hierarchy='string',
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


def get_ip_pool_from_sda_virtual_network_default_val(api):
    endpoint_result = api.sda.get_ip_pool_from_sda_virtual_network(
        ip_pool_name=None,
        site_name_hierarchy=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_ip_pool_from_sda_virtual_network_default_val(api, validator):
    try:
        assert is_valid_get_ip_pool_from_sda_virtual_network(
            validator,
            get_ip_pool_from_sda_virtual_network_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_ip_pool_from_sda_virtual_network(json_schema_validate, obj):
    json_schema_validate('jsd_951c923d016d5401b7a9943724df3844_v2_3_7_6').validate(obj)
    return True


def delete_ip_pool_from_sda_virtual_network(api):
    endpoint_result = api.sda.delete_ip_pool_from_sda_virtual_network(
        ip_pool_name='string',
        site_name_hierarchy='string',
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


def delete_ip_pool_from_sda_virtual_network_default_val(api):
    endpoint_result = api.sda.delete_ip_pool_from_sda_virtual_network(
        ip_pool_name=None,
        site_name_hierarchy=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_ip_pool_from_sda_virtual_network_default_val(api, validator):
    try:
        assert is_valid_delete_ip_pool_from_sda_virtual_network(
            validator,
            delete_ip_pool_from_sda_virtual_network_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_ip_pool_in_sda_virtual_network(json_schema_validate, obj):
    json_schema_validate('jsd_62b07f187b7456c8bbb6088a2f24dcee_v2_3_7_6').validate(obj)
    return True


def add_ip_pool_in_sda_virtual_network(api):
    endpoint_result = api.sda.add_ip_pool_in_sda_virtual_network(
        active_validation=True,
        autoGenerateVlanName=True,
        ipPoolName='string',
        isBridgeModeVm=True,
        isCommonPool=True,
        isIpDirectedBroadcast=True,
        isL2FloodingEnabled=True,
        isLayer2Only=True,
        isThisCriticalPool=True,
        isWirelessPool=True,
        payload=None,
        poolType='string',
        scalableGroupName='string',
        siteNameHierarchy='string',
        trafficType='string',
        virtualNetworkName='string',
        vlanId='string',
        vlanName='string'
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


def add_ip_pool_in_sda_virtual_network_default_val(api):
    endpoint_result = api.sda.add_ip_pool_in_sda_virtual_network(
        active_validation=True,
        autoGenerateVlanName=None,
        ipPoolName=None,
        isBridgeModeVm=None,
        isCommonPool=None,
        isIpDirectedBroadcast=None,
        isL2FloodingEnabled=None,
        isLayer2Only=None,
        isThisCriticalPool=None,
        isWirelessPool=None,
        payload=None,
        poolType=None,
        scalableGroupName=None,
        siteNameHierarchy=None,
        trafficType=None,
        virtualNetworkName=None,
        vlanId=None,
        vlanName=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_ip_pool_in_sda_virtual_network_default_val(api, validator):
    try:
        assert is_valid_add_ip_pool_in_sda_virtual_network(
            validator,
            add_ip_pool_in_sda_virtual_network_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_anycast_gateways(json_schema_validate, obj):
    json_schema_validate('jsd_6f486694f3da57b4921b7f2036a1b754_v2_3_7_6').validate(obj)
    return True


def update_anycast_gateways(api):
    endpoint_result = api.sda.update_anycast_gateways(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_anycast_gateways(api, validator):
    try:
        assert is_valid_update_anycast_gateways(
            validator,
            update_anycast_gateways(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_anycast_gateways_default_val(api):
    endpoint_result = api.sda.update_anycast_gateways(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_anycast_gateways_default_val(api, validator):
    try:
        assert is_valid_update_anycast_gateways(
            validator,
            update_anycast_gateways_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_anycast_gateways(json_schema_validate, obj):
    json_schema_validate('jsd_05ee8590b6b45048b84e814161272bee_v2_3_7_6').validate(obj)
    return True


def add_anycast_gateways(api):
    endpoint_result = api.sda.add_anycast_gateways(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_anycast_gateways(api, validator):
    try:
        assert is_valid_add_anycast_gateways(
            validator,
            add_anycast_gateways(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_anycast_gateways_default_val(api):
    endpoint_result = api.sda.add_anycast_gateways(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_anycast_gateways_default_val(api, validator):
    try:
        assert is_valid_add_anycast_gateways(
            validator,
            add_anycast_gateways_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_anycast_gateways(json_schema_validate, obj):
    json_schema_validate('jsd_067c634a503551e885c053fd1ed9d3fd_v2_3_7_6').validate(obj)
    return True


def get_anycast_gateways(api):
    endpoint_result = api.sda.get_anycast_gateways(
        fabric_id='string',
        id='string',
        ip_pool_name='string',
        limit=0,
        offset=0,
        virtual_network_name='string',
        vlan_id=0,
        vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_anycast_gateways(api, validator):
    try:
        assert is_valid_get_anycast_gateways(
            validator,
            get_anycast_gateways(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_anycast_gateways_default_val(api):
    endpoint_result = api.sda.get_anycast_gateways(
        fabric_id=None,
        id=None,
        ip_pool_name=None,
        limit=None,
        offset=None,
        virtual_network_name=None,
        vlan_id=None,
        vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_anycast_gateways_default_val(api, validator):
    try:
        assert is_valid_get_anycast_gateways(
            validator,
            get_anycast_gateways_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_anycast_gateway_count(json_schema_validate, obj):
    json_schema_validate('jsd_51126a280b785a3ca53c349c68ca9070_v2_3_7_6').validate(obj)
    return True


def get_anycast_gateway_count(api):
    endpoint_result = api.sda.get_anycast_gateway_count(
        fabric_id='string',
        ip_pool_name='string',
        virtual_network_name='string',
        vlan_id=0,
        vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_anycast_gateway_count(api, validator):
    try:
        assert is_valid_get_anycast_gateway_count(
            validator,
            get_anycast_gateway_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_anycast_gateway_count_default_val(api):
    endpoint_result = api.sda.get_anycast_gateway_count(
        fabric_id=None,
        ip_pool_name=None,
        virtual_network_name=None,
        vlan_id=None,
        vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_anycast_gateway_count_default_val(api, validator):
    try:
        assert is_valid_get_anycast_gateway_count(
            validator,
            get_anycast_gateway_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_anycast_gateway_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_98e66d9fbfe55cf5882bf219b0fffa13_v2_3_7_6').validate(obj)
    return True


def delete_anycast_gateway_by_id(api):
    endpoint_result = api.sda.delete_anycast_gateway_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_anycast_gateway_by_id(api, validator):
    try:
        assert is_valid_delete_anycast_gateway_by_id(
            validator,
            delete_anycast_gateway_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_anycast_gateway_by_id_default_val(api):
    endpoint_result = api.sda.delete_anycast_gateway_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_anycast_gateway_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_anycast_gateway_by_id(
            validator,
            delete_anycast_gateway_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_authentication_profiles(json_schema_validate, obj):
    json_schema_validate('jsd_3827e6713a34508993b3e9f6837dd690_v2_3_7_6').validate(obj)
    return True


def get_authentication_profiles(api):
    endpoint_result = api.sda.get_authentication_profiles(
        authentication_profile_name='string',
        fabric_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_authentication_profiles(api, validator):
    try:
        assert is_valid_get_authentication_profiles(
            validator,
            get_authentication_profiles(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_authentication_profiles_default_val(api):
    endpoint_result = api.sda.get_authentication_profiles(
        authentication_profile_name=None,
        fabric_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_authentication_profiles_default_val(api, validator):
    try:
        assert is_valid_get_authentication_profiles(
            validator,
            get_authentication_profiles_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_8948077ea8d75a9d8d9e6882da4a4a91_v2_3_7_6').validate(obj)
    return True


def update_authentication_profile(api):
    endpoint_result = api.sda.update_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_authentication_profile(api, validator):
    try:
        assert is_valid_update_authentication_profile(
            validator,
            update_authentication_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_authentication_profile_default_val(api):
    endpoint_result = api.sda.update_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_authentication_profile_default_val(api, validator):
    try:
        assert is_valid_update_authentication_profile(
            validator,
            update_authentication_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_extranet_policy(json_schema_validate, obj):
    json_schema_validate('jsd_6ccd75f80ece59f08cadda085402cef5_v2_3_7_6').validate(obj)
    return True


def update_extranet_policy(api):
    endpoint_result = api.sda.update_extranet_policy(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_extranet_policy(api, validator):
    try:
        assert is_valid_update_extranet_policy(
            validator,
            update_extranet_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_extranet_policy_default_val(api):
    endpoint_result = api.sda.update_extranet_policy(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_extranet_policy_default_val(api, validator):
    try:
        assert is_valid_update_extranet_policy(
            validator,
            update_extranet_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_extranet_policy(json_schema_validate, obj):
    json_schema_validate('jsd_a0c237c8fc115b6f98b87cc7a1360dd0_v2_3_7_6').validate(obj)
    return True


def add_extranet_policy(api):
    endpoint_result = api.sda.add_extranet_policy(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_extranet_policy(api, validator):
    try:
        assert is_valid_add_extranet_policy(
            validator,
            add_extranet_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_extranet_policy_default_val(api):
    endpoint_result = api.sda.add_extranet_policy(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_extranet_policy_default_val(api, validator):
    try:
        assert is_valid_add_extranet_policy(
            validator,
            add_extranet_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_extranet_policies(json_schema_validate, obj):
    json_schema_validate('jsd_c88d4f7170b9553abf9af4d011a25f0f_v2_3_7_6').validate(obj)
    return True


def get_extranet_policies(api):
    endpoint_result = api.sda.get_extranet_policies(
        extranet_policy_name='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_extranet_policies(api, validator):
    try:
        assert is_valid_get_extranet_policies(
            validator,
            get_extranet_policies(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_extranet_policies_default_val(api):
    endpoint_result = api.sda.get_extranet_policies(
        extranet_policy_name=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_extranet_policies_default_val(api, validator):
    try:
        assert is_valid_get_extranet_policies(
            validator,
            get_extranet_policies_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_extranet_policy_count(json_schema_validate, obj):
    json_schema_validate('jsd_dd8262eb13145dc292e7aee84e56e065_v2_3_7_6').validate(obj)
    return True


def get_extranet_policy_count(api):
    endpoint_result = api.sda.get_extranet_policy_count(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_extranet_policy_count(api, validator):
    try:
        assert is_valid_get_extranet_policy_count(
            validator,
            get_extranet_policy_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_extranet_policy_count_default_val(api):
    endpoint_result = api.sda.get_extranet_policy_count(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_extranet_policy_count_default_val(api, validator):
    try:
        assert is_valid_get_extranet_policy_count(
            validator,
            get_extranet_policy_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_extranet_policy_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_22aeee667e2d567cbbff106e1888bbbe_v2_3_7_6').validate(obj)
    return True


def delete_extranet_policy_by_id(api):
    endpoint_result = api.sda.delete_extranet_policy_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_extranet_policy_by_id(api, validator):
    try:
        assert is_valid_delete_extranet_policy_by_id(
            validator,
            delete_extranet_policy_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_extranet_policy_by_id_default_val(api):
    endpoint_result = api.sda.delete_extranet_policy_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_extranet_policy_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_extranet_policy_by_id(
            validator,
            delete_extranet_policy_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices(json_schema_validate, obj):
    json_schema_validate('jsd_d5486968c9ff5b23ae1fdd15ad6da1ef_v2_3_7_6').validate(obj)
    return True


def get_fabric_devices(api):
    endpoint_result = api.sda.get_fabric_devices(
        device_roles='string',
        fabric_id='string',
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices(api, validator):
    try:
        assert is_valid_get_fabric_devices(
            validator,
            get_fabric_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_default_val(api):
    endpoint_result = api.sda.get_fabric_devices(
        device_roles=None,
        fabric_id=None,
        limit=None,
        network_device_id=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices(
            validator,
            get_fabric_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_fabric_devices(json_schema_validate, obj):
    json_schema_validate('jsd_28a924f763a15125a8d5beaa6dd6fa2c_v2_3_7_6').validate(obj)
    return True


def update_fabric_devices(api):
    endpoint_result = api.sda.update_fabric_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_devices(api, validator):
    try:
        assert is_valid_update_fabric_devices(
            validator,
            update_fabric_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_fabric_devices_default_val(api):
    endpoint_result = api.sda.update_fabric_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_devices_default_val(api, validator):
    try:
        assert is_valid_update_fabric_devices(
            validator,
            update_fabric_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_devices(json_schema_validate, obj):
    json_schema_validate('jsd_8010c5d22b295a4c8e4a1dfdb4645f92_v2_3_7_6').validate(obj)
    return True


def delete_fabric_devices(api):
    endpoint_result = api.sda.delete_fabric_devices(
        device_roles='string',
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_devices(api, validator):
    try:
        assert is_valid_delete_fabric_devices(
            validator,
            delete_fabric_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_devices_default_val(api):
    endpoint_result = api.sda.delete_fabric_devices(
        device_roles=None,
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_devices_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_devices(
            validator,
            delete_fabric_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric_devices(json_schema_validate, obj):
    json_schema_validate('jsd_30d77719c37558f694e5545a21406275_v2_3_7_6').validate(obj)
    return True


def add_fabric_devices(api):
    endpoint_result = api.sda.add_fabric_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices(api, validator):
    try:
        assert is_valid_add_fabric_devices(
            validator,
            add_fabric_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_devices_default_val(api):
    endpoint_result = api.sda.add_fabric_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_default_val(api, validator):
    try:
        assert is_valid_add_fabric_devices(
            validator,
            add_fabric_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_count(json_schema_validate, obj):
    json_schema_validate('jsd_2f081250cdc75361afea8d1624123bb4_v2_3_7_6').validate(obj)
    return True


def get_fabric_devices_count(api):
    endpoint_result = api.sda.get_fabric_devices_count(
        device_roles='string',
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_count(api, validator):
    try:
        assert is_valid_get_fabric_devices_count(
            validator,
            get_fabric_devices_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_count_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_count(
        device_roles=None,
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_count_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_count(
            validator,
            get_fabric_devices_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_device_layer2_handoffs(json_schema_validate, obj):
    json_schema_validate('jsd_b6484275a25c54488d300c11c5ddd481_v2_3_7_6').validate(obj)
    return True


def delete_fabric_device_layer2_handoffs(api):
    endpoint_result = api.sda.delete_fabric_device_layer2_handoffs(
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer2_handoffs(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer2_handoffs(
            validator,
            delete_fabric_device_layer2_handoffs(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_device_layer2_handoffs_default_val(api):
    endpoint_result = api.sda.delete_fabric_device_layer2_handoffs(
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer2_handoffs_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer2_handoffs(
            validator,
            delete_fabric_device_layer2_handoffs_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_layer2_handoffs(json_schema_validate, obj):
    json_schema_validate('jsd_ec047337e36b59db977e1dae8dd724ef_v2_3_7_6').validate(obj)
    return True


def get_fabric_devices_layer2_handoffs(api):
    endpoint_result = api.sda.get_fabric_devices_layer2_handoffs(
        fabric_id='string',
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer2_handoffs(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer2_handoffs(
            validator,
            get_fabric_devices_layer2_handoffs(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_layer2_handoffs_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_layer2_handoffs(
        fabric_id=None,
        limit=None,
        network_device_id=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer2_handoffs_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer2_handoffs(
            validator,
            get_fabric_devices_layer2_handoffs_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric_devices_layer2_handoffs(json_schema_validate, obj):
    json_schema_validate('jsd_0e86b65311b05d29ba5eea0d5f1fd88f_v2_3_7_6').validate(obj)
    return True


def add_fabric_devices_layer2_handoffs(api):
    endpoint_result = api.sda.add_fabric_devices_layer2_handoffs(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_layer2_handoffs(api, validator):
    try:
        assert is_valid_add_fabric_devices_layer2_handoffs(
            validator,
            add_fabric_devices_layer2_handoffs(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_devices_layer2_handoffs_default_val(api):
    endpoint_result = api.sda.add_fabric_devices_layer2_handoffs(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_layer2_handoffs_default_val(api, validator):
    try:
        assert is_valid_add_fabric_devices_layer2_handoffs(
            validator,
            add_fabric_devices_layer2_handoffs_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_layer2_handoffs_count(json_schema_validate, obj):
    json_schema_validate('jsd_35c6da6b1da95bb691d2e39cee84dbb2_v2_3_7_6').validate(obj)
    return True


def get_fabric_devices_layer2_handoffs_count(api):
    endpoint_result = api.sda.get_fabric_devices_layer2_handoffs_count(
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer2_handoffs_count(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer2_handoffs_count(
            validator,
            get_fabric_devices_layer2_handoffs_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_layer2_handoffs_count_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_layer2_handoffs_count(
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer2_handoffs_count_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer2_handoffs_count(
            validator,
            get_fabric_devices_layer2_handoffs_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_device_layer2_handoff_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_380853b6406a55509e5aeaa71d960f98_v2_3_7_6').validate(obj)
    return True


def delete_fabric_device_layer2_handoff_by_id(api):
    endpoint_result = api.sda.delete_fabric_device_layer2_handoff_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer2_handoff_by_id(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer2_handoff_by_id(
            validator,
            delete_fabric_device_layer2_handoff_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_device_layer2_handoff_by_id_default_val(api):
    endpoint_result = api.sda.delete_fabric_device_layer2_handoff_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer2_handoff_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer2_handoff_by_id(
            validator,
            delete_fabric_device_layer2_handoff_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric_devices_layer3_handoffs_with_ip_transit(json_schema_validate, obj):
    json_schema_validate('jsd_69625c45c1c55d498d03a72933690098_v2_3_7_6').validate(obj)
    return True


def add_fabric_devices_layer3_handoffs_with_ip_transit(api):
    endpoint_result = api.sda.add_fabric_devices_layer3_handoffs_with_ip_transit(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_layer3_handoffs_with_ip_transit(api, validator):
    try:
        assert is_valid_add_fabric_devices_layer3_handoffs_with_ip_transit(
            validator,
            add_fabric_devices_layer3_handoffs_with_ip_transit(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_devices_layer3_handoffs_with_ip_transit_default_val(api):
    endpoint_result = api.sda.add_fabric_devices_layer3_handoffs_with_ip_transit(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_layer3_handoffs_with_ip_transit_default_val(api, validator):
    try:
        assert is_valid_add_fabric_devices_layer3_handoffs_with_ip_transit(
            validator,
            add_fabric_devices_layer3_handoffs_with_ip_transit_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_fabric_devices_layer3_handoffs_with_ip_transit(json_schema_validate, obj):
    json_schema_validate('jsd_f0942fbb79f855e889d60777f41ea944_v2_3_7_6').validate(obj)
    return True


def update_fabric_devices_layer3_handoffs_with_ip_transit(api):
    endpoint_result = api.sda.update_fabric_devices_layer3_handoffs_with_ip_transit(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_devices_layer3_handoffs_with_ip_transit(api, validator):
    try:
        assert is_valid_update_fabric_devices_layer3_handoffs_with_ip_transit(
            validator,
            update_fabric_devices_layer3_handoffs_with_ip_transit(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_fabric_devices_layer3_handoffs_with_ip_transit_default_val(api):
    endpoint_result = api.sda.update_fabric_devices_layer3_handoffs_with_ip_transit(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_devices_layer3_handoffs_with_ip_transit_default_val(api, validator):
    try:
        assert is_valid_update_fabric_devices_layer3_handoffs_with_ip_transit(
            validator,
            update_fabric_devices_layer3_handoffs_with_ip_transit_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_device_layer3_handoffs_with_ip_transit(json_schema_validate, obj):
    json_schema_validate('jsd_fdab9b7917a1567980b0071e058921fe_v2_3_7_6').validate(obj)
    return True


def delete_fabric_device_layer3_handoffs_with_ip_transit(api):
    endpoint_result = api.sda.delete_fabric_device_layer3_handoffs_with_ip_transit(
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer3_handoffs_with_ip_transit(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer3_handoffs_with_ip_transit(
            validator,
            delete_fabric_device_layer3_handoffs_with_ip_transit(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_device_layer3_handoffs_with_ip_transit_default_val(api):
    endpoint_result = api.sda.delete_fabric_device_layer3_handoffs_with_ip_transit(
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer3_handoffs_with_ip_transit_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer3_handoffs_with_ip_transit(
            validator,
            delete_fabric_device_layer3_handoffs_with_ip_transit_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_layer3_handoffs_with_ip_transit(json_schema_validate, obj):
    json_schema_validate('jsd_ee0d11a1e0dd573da2d6fb96d92c4bb8_v2_3_7_6').validate(obj)
    return True


def get_fabric_devices_layer3_handoffs_with_ip_transit(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_ip_transit(
        fabric_id='string',
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_ip_transit(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_ip_transit(
            validator,
            get_fabric_devices_layer3_handoffs_with_ip_transit(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_layer3_handoffs_with_ip_transit_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_ip_transit(
        fabric_id=None,
        limit=None,
        network_device_id=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_ip_transit_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_ip_transit(
            validator,
            get_fabric_devices_layer3_handoffs_with_ip_transit_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_layer3_handoffs_with_ip_transit_count(json_schema_validate, obj):
    json_schema_validate('jsd_878592a4fa61561aa0fe56939c3f24d4_v2_3_7_6').validate(obj)
    return True


def get_fabric_devices_layer3_handoffs_with_ip_transit_count(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_ip_transit_count(
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_ip_transit_count(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_ip_transit_count(
            validator,
            get_fabric_devices_layer3_handoffs_with_ip_transit_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_layer3_handoffs_with_ip_transit_count_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_ip_transit_count(
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_ip_transit_count_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_ip_transit_count(
            validator,
            get_fabric_devices_layer3_handoffs_with_ip_transit_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_device_layer3_handoff_with_ip_transit_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_3fafe4d2d2fe510db8f0906e5f583559_v2_3_7_6').validate(obj)
    return True


def delete_fabric_device_layer3_handoff_with_ip_transit_by_id(api):
    endpoint_result = api.sda.delete_fabric_device_layer3_handoff_with_ip_transit_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer3_handoff_with_ip_transit_by_id(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer3_handoff_with_ip_transit_by_id(
            validator,
            delete_fabric_device_layer3_handoff_with_ip_transit_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_device_layer3_handoff_with_ip_transit_by_id_default_val(api):
    endpoint_result = api.sda.delete_fabric_device_layer3_handoff_with_ip_transit_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer3_handoff_with_ip_transit_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer3_handoff_with_ip_transit_by_id(
            validator,
            delete_fabric_device_layer3_handoff_with_ip_transit_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_fabric_devices_layer3_handoffs_with_sda_transit(json_schema_validate, obj):
    json_schema_validate('jsd_902c90c04b8356cf9974957e0f9516d0_v2_3_7_6').validate(obj)
    return True


def update_fabric_devices_layer3_handoffs_with_sda_transit(api):
    endpoint_result = api.sda.update_fabric_devices_layer3_handoffs_with_sda_transit(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_devices_layer3_handoffs_with_sda_transit(api, validator):
    try:
        assert is_valid_update_fabric_devices_layer3_handoffs_with_sda_transit(
            validator,
            update_fabric_devices_layer3_handoffs_with_sda_transit(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_fabric_devices_layer3_handoffs_with_sda_transit_default_val(api):
    endpoint_result = api.sda.update_fabric_devices_layer3_handoffs_with_sda_transit(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_devices_layer3_handoffs_with_sda_transit_default_val(api, validator):
    try:
        assert is_valid_update_fabric_devices_layer3_handoffs_with_sda_transit(
            validator,
            update_fabric_devices_layer3_handoffs_with_sda_transit_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_layer3_handoffs_with_sda_transit(json_schema_validate, obj):
    json_schema_validate('jsd_d8e5a783df185c88bae2bd8ba6b6bb2d_v2_3_7_6').validate(obj)
    return True


def get_fabric_devices_layer3_handoffs_with_sda_transit(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_sda_transit(
        fabric_id='string',
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_sda_transit(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_sda_transit(
            validator,
            get_fabric_devices_layer3_handoffs_with_sda_transit(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_layer3_handoffs_with_sda_transit_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_sda_transit(
        fabric_id=None,
        limit=None,
        network_device_id=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_sda_transit_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_sda_transit(
            validator,
            get_fabric_devices_layer3_handoffs_with_sda_transit_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_device_layer3_handoffs_with_sda_transit(json_schema_validate, obj):
    json_schema_validate('jsd_62aae870923852f3ac5904f65812c559_v2_3_7_6').validate(obj)
    return True


def delete_fabric_device_layer3_handoffs_with_sda_transit(api):
    endpoint_result = api.sda.delete_fabric_device_layer3_handoffs_with_sda_transit(
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer3_handoffs_with_sda_transit(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer3_handoffs_with_sda_transit(
            validator,
            delete_fabric_device_layer3_handoffs_with_sda_transit(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_device_layer3_handoffs_with_sda_transit_default_val(api):
    endpoint_result = api.sda.delete_fabric_device_layer3_handoffs_with_sda_transit(
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_device_layer3_handoffs_with_sda_transit_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_device_layer3_handoffs_with_sda_transit(
            validator,
            delete_fabric_device_layer3_handoffs_with_sda_transit_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric_devices_layer3_handoffs_with_sda_transit(json_schema_validate, obj):
    json_schema_validate('jsd_f95014e3b3385f21afa39325f3508427_v2_3_7_6').validate(obj)
    return True


def add_fabric_devices_layer3_handoffs_with_sda_transit(api):
    endpoint_result = api.sda.add_fabric_devices_layer3_handoffs_with_sda_transit(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_layer3_handoffs_with_sda_transit(api, validator):
    try:
        assert is_valid_add_fabric_devices_layer3_handoffs_with_sda_transit(
            validator,
            add_fabric_devices_layer3_handoffs_with_sda_transit(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_devices_layer3_handoffs_with_sda_transit_default_val(api):
    endpoint_result = api.sda.add_fabric_devices_layer3_handoffs_with_sda_transit(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_devices_layer3_handoffs_with_sda_transit_default_val(api, validator):
    try:
        assert is_valid_add_fabric_devices_layer3_handoffs_with_sda_transit(
            validator,
            add_fabric_devices_layer3_handoffs_with_sda_transit_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_devices_layer3_handoffs_with_sda_transit_count(json_schema_validate, obj):
    json_schema_validate('jsd_9b183d0cc487506ab776e0d470b0db91_v2_3_7_6').validate(obj)
    return True


def get_fabric_devices_layer3_handoffs_with_sda_transit_count(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_sda_transit_count(
        fabric_id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_sda_transit_count(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_sda_transit_count(
            validator,
            get_fabric_devices_layer3_handoffs_with_sda_transit_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_devices_layer3_handoffs_with_sda_transit_count_default_val(api):
    endpoint_result = api.sda.get_fabric_devices_layer3_handoffs_with_sda_transit_count(
        fabric_id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_devices_layer3_handoffs_with_sda_transit_count_default_val(api, validator):
    try:
        assert is_valid_get_fabric_devices_layer3_handoffs_with_sda_transit_count(
            validator,
            get_fabric_devices_layer3_handoffs_with_sda_transit_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_fabric_device_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_497d9e0c5eb356eda1fa6f45928cb6f2_v2_3_7_6').validate(obj)
    return True


def delete_a_fabric_device_by_id(api):
    endpoint_result = api.sda.delete_a_fabric_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_a_fabric_device_by_id(api, validator):
    try:
        assert is_valid_delete_a_fabric_device_by_id(
            validator,
            delete_a_fabric_device_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_fabric_device_by_id_default_val(api):
    endpoint_result = api.sda.delete_a_fabric_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_a_fabric_device_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_a_fabric_device_by_id(
            validator,
            delete_a_fabric_device_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_sites(json_schema_validate, obj):
    json_schema_validate('jsd_07a7079f75dd5973b2bf50461bdcf2de_v2_3_7_6').validate(obj)
    return True


def get_fabric_sites(api):
    endpoint_result = api.sda.get_fabric_sites(
        id='string',
        limit=0,
        offset=0,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_sites(api, validator):
    try:
        assert is_valid_get_fabric_sites(
            validator,
            get_fabric_sites(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_sites_default_val(api):
    endpoint_result = api.sda.get_fabric_sites(
        id=None,
        limit=None,
        offset=None,
        site_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_sites_default_val(api, validator):
    try:
        assert is_valid_get_fabric_sites(
            validator,
            get_fabric_sites_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric_site(json_schema_validate, obj):
    json_schema_validate('jsd_7680bfca373c5d7c863eef14abc654fd_v2_3_7_6').validate(obj)
    return True


def add_fabric_site(api):
    endpoint_result = api.sda.add_fabric_site(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_site(api, validator):
    try:
        assert is_valid_add_fabric_site(
            validator,
            add_fabric_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_site_default_val(api):
    endpoint_result = api.sda.add_fabric_site(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_site_default_val(api, validator):
    try:
        assert is_valid_add_fabric_site(
            validator,
            add_fabric_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_fabric_site(json_schema_validate, obj):
    json_schema_validate('jsd_5198effb55c158f28469762804e84633_v2_3_7_6').validate(obj)
    return True


def update_fabric_site(api):
    endpoint_result = api.sda.update_fabric_site(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_site(api, validator):
    try:
        assert is_valid_update_fabric_site(
            validator,
            update_fabric_site(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_fabric_site_default_val(api):
    endpoint_result = api.sda.update_fabric_site(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_site_default_val(api, validator):
    try:
        assert is_valid_update_fabric_site(
            validator,
            update_fabric_site_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_site_count(json_schema_validate, obj):
    json_schema_validate('jsd_b871b97883085717bfbb14e860ab6654_v2_3_7_6').validate(obj)
    return True


def get_fabric_site_count(api):
    endpoint_result = api.sda.get_fabric_site_count(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_site_count(api, validator):
    try:
        assert is_valid_get_fabric_site_count(
            validator,
            get_fabric_site_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_site_count_default_val(api):
    endpoint_result = api.sda.get_fabric_site_count(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_site_count_default_val(api, validator):
    try:
        assert is_valid_get_fabric_site_count(
            validator,
            get_fabric_site_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_site_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_72c94ba483b75e03a2c23aae02c510ac_v2_3_7_6').validate(obj)
    return True


def delete_fabric_site_by_id(api):
    endpoint_result = api.sda.delete_fabric_site_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_site_by_id(api, validator):
    try:
        assert is_valid_delete_fabric_site_by_id(
            validator,
            delete_fabric_site_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_site_by_id_default_val(api):
    endpoint_result = api.sda.delete_fabric_site_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_site_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_site_by_id(
            validator,
            delete_fabric_site_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_zones(json_schema_validate, obj):
    json_schema_validate('jsd_7e722d98d14d5e119ca03fa114edb38f_v2_3_7_6').validate(obj)
    return True


def get_fabric_zones(api):
    endpoint_result = api.sda.get_fabric_zones(
        id='string',
        limit=0,
        offset=0,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_zones(api, validator):
    try:
        assert is_valid_get_fabric_zones(
            validator,
            get_fabric_zones(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_zones_default_val(api):
    endpoint_result = api.sda.get_fabric_zones(
        id=None,
        limit=None,
        offset=None,
        site_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_zones_default_val(api, validator):
    try:
        assert is_valid_get_fabric_zones(
            validator,
            get_fabric_zones_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_fabric_zone(json_schema_validate, obj):
    json_schema_validate('jsd_ada3522de8ef54729e9fc242df292547_v2_3_7_6').validate(obj)
    return True


def update_fabric_zone(api):
    endpoint_result = api.sda.update_fabric_zone(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_zone(api, validator):
    try:
        assert is_valid_update_fabric_zone(
            validator,
            update_fabric_zone(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_fabric_zone_default_val(api):
    endpoint_result = api.sda.update_fabric_zone(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_fabric_zone_default_val(api, validator):
    try:
        assert is_valid_update_fabric_zone(
            validator,
            update_fabric_zone_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric_zone(json_schema_validate, obj):
    json_schema_validate('jsd_ae4d33eacca95f109bebc6fd0528ca48_v2_3_7_6').validate(obj)
    return True


def add_fabric_zone(api):
    endpoint_result = api.sda.add_fabric_zone(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_zone(api, validator):
    try:
        assert is_valid_add_fabric_zone(
            validator,
            add_fabric_zone(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_fabric_zone_default_val(api):
    endpoint_result = api.sda.add_fabric_zone(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_zone_default_val(api, validator):
    try:
        assert is_valid_add_fabric_zone(
            validator,
            add_fabric_zone_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_fabric_zone_count(json_schema_validate, obj):
    json_schema_validate('jsd_b7004918aecc58c7880ae97d344bb885_v2_3_7_6').validate(obj)
    return True


def get_fabric_zone_count(api):
    endpoint_result = api.sda.get_fabric_zone_count(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_zone_count(api, validator):
    try:
        assert is_valid_get_fabric_zone_count(
            validator,
            get_fabric_zone_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_fabric_zone_count_default_val(api):
    endpoint_result = api.sda.get_fabric_zone_count(

    )
    return endpoint_result


@pytest.mark.sda
def test_get_fabric_zone_count_default_val(api, validator):
    try:
        assert is_valid_get_fabric_zone_count(
            validator,
            get_fabric_zone_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_fabric_zone_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_232cdb33e11852af80e1ed8f26e4336d_v2_3_7_6').validate(obj)
    return True


def delete_fabric_zone_by_id(api):
    endpoint_result = api.sda.delete_fabric_zone_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_zone_by_id(api, validator):
    try:
        assert is_valid_delete_fabric_zone_by_id(
            validator,
            delete_fabric_zone_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_fabric_zone_by_id_default_val(api):
    endpoint_result = api.sda.delete_fabric_zone_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_fabric_zone_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_fabric_zone_by_id(
            validator,
            delete_fabric_zone_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_port_assignments(json_schema_validate, obj):
    json_schema_validate('jsd_8d6b58f378895114839682dceed1a9b5_v2_3_7_6').validate(obj)
    return True


def add_port_assignments(api):
    endpoint_result = api.sda.add_port_assignments(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignments(api, validator):
    try:
        assert is_valid_add_port_assignments(
            validator,
            add_port_assignments(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_port_assignments_default_val(api):
    endpoint_result = api.sda.add_port_assignments(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignments_default_val(api, validator):
    try:
        assert is_valid_add_port_assignments(
            validator,
            add_port_assignments_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_assignments(json_schema_validate, obj):
    json_schema_validate('jsd_61a9bc4645925814ac76d95268fe3f05_v2_3_7_6').validate(obj)
    return True


def get_port_assignments(api):
    endpoint_result = api.sda.get_port_assignments(
        data_vlan_name='string',
        fabric_id='string',
        interface_name='string',
        limit=0,
        network_device_id='string',
        offset=0,
        voice_vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignments(api, validator):
    try:
        assert is_valid_get_port_assignments(
            validator,
            get_port_assignments(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_port_assignments_default_val(api):
    endpoint_result = api.sda.get_port_assignments(
        data_vlan_name=None,
        fabric_id=None,
        interface_name=None,
        limit=None,
        network_device_id=None,
        offset=None,
        voice_vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignments_default_val(api, validator):
    try:
        assert is_valid_get_port_assignments(
            validator,
            get_port_assignments_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_port_assignments(json_schema_validate, obj):
    json_schema_validate('jsd_39350cad522e57a7b96b7238935689ed_v2_3_7_6').validate(obj)
    return True


def update_port_assignments(api):
    endpoint_result = api.sda.update_port_assignments(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_port_assignments(api, validator):
    try:
        assert is_valid_update_port_assignments(
            validator,
            update_port_assignments(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_port_assignments_default_val(api):
    endpoint_result = api.sda.update_port_assignments(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_port_assignments_default_val(api, validator):
    try:
        assert is_valid_update_port_assignments(
            validator,
            update_port_assignments_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_assignments(json_schema_validate, obj):
    json_schema_validate('jsd_3238ee38ba825f79a76d9e7e6074c450_v2_3_7_6').validate(obj)
    return True


def delete_port_assignments(api):
    endpoint_result = api.sda.delete_port_assignments(
        data_vlan_name='string',
        fabric_id='string',
        interface_name='string',
        network_device_id='string',
        voice_vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignments(api, validator):
    try:
        assert is_valid_delete_port_assignments(
            validator,
            delete_port_assignments(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_port_assignments_default_val(api):
    endpoint_result = api.sda.delete_port_assignments(
        data_vlan_name=None,
        fabric_id=None,
        interface_name=None,
        network_device_id=None,
        voice_vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignments_default_val(api, validator):
    try:
        assert is_valid_delete_port_assignments(
            validator,
            delete_port_assignments_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_assignment_count(json_schema_validate, obj):
    json_schema_validate('jsd_e11301d6336f512fbc6db01768e3ad5a_v2_3_7_6').validate(obj)
    return True


def get_port_assignment_count(api):
    endpoint_result = api.sda.get_port_assignment_count(
        data_vlan_name='string',
        fabric_id='string',
        interface_name='string',
        network_device_id='string',
        voice_vlan_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_count(api, validator):
    try:
        assert is_valid_get_port_assignment_count(
            validator,
            get_port_assignment_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_port_assignment_count_default_val(api):
    endpoint_result = api.sda.get_port_assignment_count(
        data_vlan_name=None,
        fabric_id=None,
        interface_name=None,
        network_device_id=None,
        voice_vlan_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_count_default_val(api, validator):
    try:
        assert is_valid_get_port_assignment_count(
            validator,
            get_port_assignment_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_assignment_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_7aa18582de8753438e0908cf9d92c2de_v2_3_7_6').validate(obj)
    return True


def delete_port_assignment_by_id(api):
    endpoint_result = api.sda.delete_port_assignment_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_by_id(api, validator):
    try:
        assert is_valid_delete_port_assignment_by_id(
            validator,
            delete_port_assignment_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_port_assignment_by_id_default_val(api):
    endpoint_result = api.sda.delete_port_assignment_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_port_assignment_by_id(
            validator,
            delete_port_assignment_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_provisioned_devices(json_schema_validate, obj):
    json_schema_validate('jsd_b049914e384051afbf87971d3066152b_v2_3_7_6').validate(obj)
    return True


def delete_provisioned_devices(api):
    endpoint_result = api.sda.delete_provisioned_devices(
        network_device_id='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_devices(api, validator):
    try:
        assert is_valid_delete_provisioned_devices(
            validator,
            delete_provisioned_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_provisioned_devices_default_val(api):
    endpoint_result = api.sda.delete_provisioned_devices(
        network_device_id=None,
        site_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_devices_default_val(api, validator):
    try:
        assert is_valid_delete_provisioned_devices(
            validator,
            delete_provisioned_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_provision_devices(json_schema_validate, obj):
    json_schema_validate('jsd_bdcb514ae33b571795e4a42147d11f87_v2_3_7_6').validate(obj)
    return True


def provision_devices(api):
    endpoint_result = api.sda.provision_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_provision_devices(api, validator):
    try:
        assert is_valid_provision_devices(
            validator,
            provision_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def provision_devices_default_val(api):
    endpoint_result = api.sda.provision_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_provision_devices_default_val(api, validator):
    try:
        assert is_valid_provision_devices(
            validator,
            provision_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_provisioned_devices(json_schema_validate, obj):
    json_schema_validate('jsd_4f974cbea9645bfda97affac9ea41ffe_v2_3_7_6').validate(obj)
    return True


def get_provisioned_devices(api):
    endpoint_result = api.sda.get_provisioned_devices(
        id='string',
        limit=0,
        network_device_id='string',
        offset=0,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_devices(api, validator):
    try:
        assert is_valid_get_provisioned_devices(
            validator,
            get_provisioned_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_provisioned_devices_default_val(api):
    endpoint_result = api.sda.get_provisioned_devices(
        id=None,
        limit=None,
        network_device_id=None,
        offset=None,
        site_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_devices_default_val(api, validator):
    try:
        assert is_valid_get_provisioned_devices(
            validator,
            get_provisioned_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_re_provision_devices(json_schema_validate, obj):
    json_schema_validate('jsd_92843f4b2825561e808787a16f7e0a1f_v2_3_7_6').validate(obj)
    return True


def re_provision_devices(api):
    endpoint_result = api.sda.re_provision_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_re_provision_devices(api, validator):
    try:
        assert is_valid_re_provision_devices(
            validator,
            re_provision_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def re_provision_devices_default_val(api):
    endpoint_result = api.sda.re_provision_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_re_provision_devices_default_val(api, validator):
    try:
        assert is_valid_re_provision_devices(
            validator,
            re_provision_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_provisioned_devices_count(json_schema_validate, obj):
    json_schema_validate('jsd_580acb7d048a5455b75965c3706f8977_v2_3_7_6').validate(obj)
    return True


def get_provisioned_devices_count(api):
    endpoint_result = api.sda.get_provisioned_devices_count(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_devices_count(api, validator):
    try:
        assert is_valid_get_provisioned_devices_count(
            validator,
            get_provisioned_devices_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_provisioned_devices_count_default_val(api):
    endpoint_result = api.sda.get_provisioned_devices_count(
        site_id=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_provisioned_devices_count_default_val(api, validator):
    try:
        assert is_valid_get_provisioned_devices_count(
            validator,
            get_provisioned_devices_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_provisioned_device_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_ab7cbac7eaa45f259c9035fb828f6c08_v2_3_7_6').validate(obj)
    return True


def delete_provisioned_device_by_id(api):
    endpoint_result = api.sda.delete_provisioned_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_device_by_id(api, validator):
    try:
        assert is_valid_delete_provisioned_device_by_id(
            validator,
            delete_provisioned_device_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_provisioned_device_by_id_default_val(api):
    endpoint_result = api.sda.delete_provisioned_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_provisioned_device_by_id_default_val(api, validator):
    try:
        assert is_valid_delete_provisioned_device_by_id(
            validator,
            delete_provisioned_device_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_virtual_network_with_scalable_groups(json_schema_validate, obj):
    json_schema_validate('jsd_72472f5ebb9d50aab287f320d32181c0_v2_3_7_6').validate(obj)
    return True


def add_virtual_network_with_scalable_groups(api):
    endpoint_result = api.sda.add_virtual_network_with_scalable_groups(
        active_validation=True,
        isGuestVirtualNetwork=True,
        payload=None,
        scalableGroupNames=['string'],
        vManageVpnId='string',
        virtualNetworkName='string'
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


def add_virtual_network_with_scalable_groups_default_val(api):
    endpoint_result = api.sda.add_virtual_network_with_scalable_groups(
        active_validation=True,
        isGuestVirtualNetwork=None,
        payload=None,
        scalableGroupNames=None,
        vManageVpnId=None,
        virtualNetworkName=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_virtual_network_with_scalable_groups_default_val(api, validator):
    try:
        assert is_valid_add_virtual_network_with_scalable_groups(
            validator,
            add_virtual_network_with_scalable_groups_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_virtual_network_with_scalable_groups(json_schema_validate, obj):
    json_schema_validate('jsd_2f2e8552eabc5e5f97e1f40bcc4b4c75_v2_3_7_6').validate(obj)
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


def delete_virtual_network_with_scalable_groups_default_val(api):
    endpoint_result = api.sda.delete_virtual_network_with_scalable_groups(
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_virtual_network_with_scalable_groups_default_val(api, validator):
    try:
        assert is_valid_delete_virtual_network_with_scalable_groups(
            validator,
            delete_virtual_network_with_scalable_groups_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_virtual_network_with_scalable_groups(json_schema_validate, obj):
    json_schema_validate('jsd_ea4b1c052b855bd9a0e99f803e6185a5_v2_3_7_6').validate(obj)
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


def get_virtual_network_with_scalable_groups_default_val(api):
    endpoint_result = api.sda.get_virtual_network_with_scalable_groups(
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_virtual_network_with_scalable_groups_default_val(api, validator):
    try:
        assert is_valid_get_virtual_network_with_scalable_groups(
            validator,
            get_virtual_network_with_scalable_groups_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_virtual_network_with_scalable_groups(json_schema_validate, obj):
    json_schema_validate('jsd_f9492367570c5f009cf8b5955790e87c_v2_3_7_6').validate(obj)
    return True


def update_virtual_network_with_scalable_groups(api):
    endpoint_result = api.sda.update_virtual_network_with_scalable_groups(
        active_validation=True,
        isGuestVirtualNetwork=True,
        payload=None,
        scalableGroupNames=['string'],
        vManageVpnId='string',
        virtualNetworkName='string'
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


def update_virtual_network_with_scalable_groups_default_val(api):
    endpoint_result = api.sda.update_virtual_network_with_scalable_groups(
        active_validation=True,
        isGuestVirtualNetwork=None,
        payload=None,
        scalableGroupNames=None,
        vManageVpnId=None,
        virtualNetworkName=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_virtual_network_with_scalable_groups_default_val(api, validator):
    try:
        assert is_valid_update_virtual_network_with_scalable_groups(
            validator,
            update_virtual_network_with_scalable_groups_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

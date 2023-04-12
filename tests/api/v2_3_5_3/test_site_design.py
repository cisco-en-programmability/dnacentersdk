# -*- coding: utf-8 -*-
"""DNACenterAPI site_design API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.5.3', reason='version does not match')


def is_valid_provision_nfv(json_schema_validate, obj):
    json_schema_validate('jsd_cc72e307e5df50c48ce57370f27395a0_v2_3_5_3').validate(obj)
    return True


def provision_nfv(api):
    endpoint_result = api.site_design.provision_nfv(
        active_validation=True,
        payload=None,
        provisioning=[{'site': {'siteProfileName': 'string', 'area': {'name': 'string', 'parentName': 'string'}, 'building': {'name': 'string', 'address': 'string', 'latitude': 0, 'longitude': 0, 'parentName': 'string'}, 'floor': {'name': 'string', 'parentName': 'string', 'rfModel': 'string', 'width': 0, 'length': 0, 'height': 0}}, 'device': [{'ip': 'string', 'deviceSerialNumber': 'string', 'tagName': 'string', 'serviceProviders': [{'serviceProvider': 'string', 'wanInterface': {'ipAddress': 'string', 'interfaceName': 'string', 'subnetmask': 'string', 'bandwidth': 'string', 'gateway': 'string'}}], 'services': [{'type': 'string', 'mode': 'string', 'systemIp': 'string', 'centralManagerIP': 'string', 'centralRegistrationKey': 'string', 'commonKey': 'string', 'adminPasswordHash': 'string', 'disk': 'string'}], 'vlan': [{'type': 'string', 'id': 'string', 'interfaces': 'string', 'network': 'string'}], 'subPools': [{'type': 'string', 'name': 'string', 'ipSubnet': 'string', 'gateway': 'string', 'parentPoolName': 'string'}], 'customNetworks': [{'name': 'string', 'port': 'string', 'ipAddressPool': 'string'}], 'templateParam': {'nfvis': {'var1': 'string'}, 'asav': {'var1': 'string'}}}]}],
        siteProfile=[{'siteProfileName': 'string', 'device': [{'deviceType': 'string', 'tagName': 'string', 'serviceProviders': [{'serviceProvider': 'string', 'linkType': 'string', 'connect': True, 'defaultGateway': True}], 'dia': True, 'services': [{'type': 'string', 'profile': 'string', 'mode': 'string', 'name': 'string', 'imageName': 'string', 'topology': {'type': 'string', 'name': 'string', 'assignIp': 'string'}}], 'customServices': [{'name': 'string', 'applicationType': 'string', 'profile': 'string', 'topology': {'type': 'string', 'name': 'string', 'assignIp': 'string'}, 'imageName': 'string'}], 'customNetworks': [{'name': 'string', 'servicesToConnect': [{'service': 'string'}], 'connectionType': 'string', 'networkMode': 'string', 'vlan': 'string'}], 'vlan': [{'type': 'string', 'id': 'string'}], 'customTemplate': [{'deviceType': 'string', 'template': 'string'}]}]}]
    )
    return endpoint_result


@pytest.mark.site_design
def test_provision_nfv(api, validator):
    try:
        assert is_valid_provision_nfv(
            validator,
            provision_nfv(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def provision_nfv_default_val(api):
    endpoint_result = api.site_design.provision_nfv(
        active_validation=True,
        payload=None,
        provisioning=None,
        siteProfile=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_provision_nfv_default_val(api, validator):
    try:
        assert is_valid_provision_nfv(
            validator,
            provision_nfv_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_details_by_ip(json_schema_validate, obj):
    json_schema_validate('jsd_2bfde206eb445821a5722511f138814a_v2_3_5_3').validate(obj)
    return True


def get_device_details_by_ip(api):
    endpoint_result = api.site_design.get_device_details_by_ip(
        device_ip='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_device_details_by_ip(api, validator):
    try:
        assert is_valid_get_device_details_by_ip(
            validator,
            get_device_details_by_ip(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_details_by_ip_default_val(api):
    endpoint_result = api.site_design.get_device_details_by_ip(
        device_ip=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_device_details_by_ip_default_val(api, validator):
    try:
        assert is_valid_get_device_details_by_ip(
            validator,
            get_device_details_by_ip_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_associate(json_schema_validate, obj):
    json_schema_validate('jsd_378a1800508058e4b82a08ea5637b794_v2_3_5_3').validate(obj)
    return True


def associate(api):
    endpoint_result = api.site_design.associate(
        active_validation=True,
        network_profile_id='string',
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_associate(api, validator):
    try:
        assert is_valid_associate(
            validator,
            associate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def associate_default_val(api):
    endpoint_result = api.site_design.associate(
        active_validation=True,
        network_profile_id='string',
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_associate_default_val(api, validator):
    try:
        assert is_valid_associate(
            validator,
            associate_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_disassociate(json_schema_validate, obj):
    json_schema_validate('jsd_21c8936d6a0c54e89b471fe36bf28de8_v2_3_5_3').validate(obj)
    return True


def disassociate(api):
    endpoint_result = api.site_design.disassociate(
        network_profile_id='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_disassociate(api, validator):
    try:
        assert is_valid_disassociate(
            validator,
            disassociate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def disassociate_default_val(api):
    endpoint_result = api.site_design.disassociate(
        network_profile_id='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_disassociate_default_val(api, validator):
    try:
        assert is_valid_disassociate(
            validator,
            disassociate_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_nfv_provisioning_detail(json_schema_validate, obj):
    json_schema_validate('jsd_497d9ccfce8451809129ec5de42c5048_v2_3_5_3').validate(obj)
    return True


def nfv_provisioning_detail(api):
    endpoint_result = api.site_design.nfv_provisioning_detail(
        active_validation=True,
        device_ip='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_nfv_provisioning_detail(api, validator):
    try:
        assert is_valid_nfv_provisioning_detail(
            validator,
            nfv_provisioning_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def nfv_provisioning_detail_default_val(api):
    endpoint_result = api.site_design.nfv_provisioning_detail(
        active_validation=True,
        device_ip=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_nfv_provisioning_detail_default_val(api, validator):
    try:
        assert is_valid_nfv_provisioning_detail(
            validator,
            nfv_provisioning_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_nfv_profile(json_schema_validate, obj):
    json_schema_validate('jsd_d2a712eb315650618d475db5de0aabec_v2_3_5_3').validate(obj)
    return True


def create_nfv_profile(api):
    endpoint_result = api.site_design.create_nfv_profile(
        active_validation=True,
        device=[{'deviceType': 'string', 'deviceTag': 'string', 'serviceProviderProfile': [{'serviceProvider': 'string', 'linkType': 'string', 'connect': True, 'connectDefaultGatewayOnWan': True}], 'directInternetAccessForFirewall': True, 'services': [{'serviceType': 'string', 'profileType': 'string', 'serviceName': 'string', 'imageName': 'string', 'vNicMapping': [{'networkType': 'string', 'assignIpAddressToNetwork': 'string'}], 'firewallMode': 'string'}], 'customNetworks': [{'networkName': 'string', 'servicesToConnect': [{'serviceName': 'string'}], 'connectionType': 'string', 'vlanMode': 'string', 'vlanId': 0}], 'vlanForL2': [{'vlanType': 'string', 'vlanId': 0, 'vlanDescription': 'string'}], 'customTemplate': [{'deviceType': 'string', 'template': 'string', 'templateType': 'string'}]}],
        payload=None,
        profileName='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_create_nfv_profile(api, validator):
    try:
        assert is_valid_create_nfv_profile(
            validator,
            create_nfv_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_nfv_profile_default_val(api):
    endpoint_result = api.site_design.create_nfv_profile(
        active_validation=True,
        device=None,
        payload=None,
        profileName=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_create_nfv_profile_default_val(api, validator):
    try:
        assert is_valid_create_nfv_profile(
            validator,
            create_nfv_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_nfv_profile(json_schema_validate, obj):
    json_schema_validate('jsd_159612e2202e5f7586e68778ed7772b1_v2_3_5_3').validate(obj)
    return True


def update_nfv_profile(api):
    endpoint_result = api.site_design.update_nfv_profile(
        active_validation=True,
        device=[{'deviceTag': 'string', 'directInternetAccessForFirewall': True, 'services': [{'serviceType': 'string', 'profileType': 'string', 'serviceName': 'string', 'imageName': 'string', 'vNicMapping': [{'networkType': 'string', 'assignIpAddressToNetwork': 'string'}], 'firewallMode': 'string'}], 'customNetworks': [{'networkName': 'string', 'servicesToConnect': [{'serviceName': 'string'}], 'connectionType': 'string', 'vlanMode': 'string', 'vlanId': 0}], 'vlanForL2': [{'vlanType': 'string', 'vlanId': 0, 'vlanDescription': 'string'}], 'customTemplate': [{'deviceType': 'string', 'template': 'string', 'templateType': 'string'}], 'currentDeviceTag': 'string'}],
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_update_nfv_profile(api, validator):
    try:
        assert is_valid_update_nfv_profile(
            validator,
            update_nfv_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_nfv_profile_default_val(api):
    endpoint_result = api.site_design.update_nfv_profile(
        active_validation=True,
        device=None,
        id='string',
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_update_nfv_profile_default_val(api, validator):
    try:
        assert is_valid_update_nfv_profile(
            validator,
            update_nfv_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_nfv_profile(json_schema_validate, obj):
    json_schema_validate('jsd_f50579d855255df89ab3545de9745545_v2_3_5_3').validate(obj)
    return True


def get_nfv_profile(api):
    endpoint_result = api.site_design.get_nfv_profile(
        id='string',
        limit=0,
        name='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_nfv_profile(api, validator):
    try:
        assert is_valid_get_nfv_profile(
            validator,
            get_nfv_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_nfv_profile_default_val(api):
    endpoint_result = api.site_design.get_nfv_profile(
        id='string',
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_nfv_profile_default_val(api, validator):
    try:
        assert is_valid_get_nfv_profile(
            validator,
            get_nfv_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_nfv_profile(json_schema_validate, obj):
    json_schema_validate('jsd_89252bcefb205d26b9aced6dc6d8c269_v2_3_5_3').validate(obj)
    return True


def delete_nfv_profile(api):
    endpoint_result = api.site_design.delete_nfv_profile(
        id='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_delete_nfv_profile(api, validator):
    try:
        assert is_valid_delete_nfv_profile(
            validator,
            delete_nfv_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_nfv_profile_default_val(api):
    endpoint_result = api.site_design.delete_nfv_profile(
        id='string',
        name=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_delete_nfv_profile_default_val(api, validator):
    try:
        assert is_valid_delete_nfv_profile(
            validator,
            delete_nfv_profile_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

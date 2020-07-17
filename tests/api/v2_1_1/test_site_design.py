# -*- coding: utf-8 -*-
"""DNACenterAPI site_design API fixtures and tests.

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
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.1.1', reason='version does not match')


def is_valid_get_nfv_profile(obj):
    json_schema_validate('jsd_1eb19887457b9616_v2_1_1').validate(obj)
    return True


def get_nfv_profile(api):
    endpoint_result = api.site_design.get_nfv_profile(
        id='string',
        limit='string',
        name='string',
        offset='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_nfv_profile(api):
    assert is_valid_get_nfv_profile(
        get_nfv_profile(api)
    )


def get_nfv_profile_default(api):
    endpoint_result = api.site_design.get_nfv_profile(
        id='string',
        limit=None,
        name=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_nfv_profile_default(api):
    try:
        assert is_valid_get_nfv_profile(
            get_nfv_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_nfv_profile(obj):
    json_schema_validate('jsd_0fa00adf48698287_v2_1_1').validate(obj)
    return True


def update_nfv_profile(api):
    endpoint_result = api.site_design.update_nfv_profile(
        active_validation=True,
        device=[{'deviceTag': 'string', 'directInternetAccessForFirewall': True, 'services': [{'serviceType': 'isr', 'profileType': 'ASAv5', 'serviceName': 'string', 'imageName': 'string', 'vNicMapping': [{'networkType': 'wan-net', 'assignIpAddressToNetwork': 'string'}], 'firewallMode': 'routed'}], 'customNetworks': [{'networkName': 'string', 'servicesToConnect': [{'serviceName': 'string'}], 'connectionType': 'wan-net', 'vlanMode': 'trunk', 'vlanId': 0}], 'vlanForL2': [{'vlanType': 'access', 'vlanId': 0, 'vlanDescription': 'string'}], 'customTemplate': [{'deviceType': 'Cisco 5400 Enterprise Network Compute System', 'template': 'string', 'templateType': 'Onboarding Template(s)'}], 'currentDeviceTag': 'string'}],
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_update_nfv_profile(api):
    assert is_valid_update_nfv_profile(
        update_nfv_profile(api)
    )


def update_nfv_profile_default(api):
    endpoint_result = api.site_design.update_nfv_profile(
        active_validation=True,
        device=None,
        id='string',
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_update_nfv_profile_default(api):
    try:
        assert is_valid_update_nfv_profile(
            update_nfv_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_nfv_provisioning_detail(obj):
    json_schema_validate('jsd_2f97e8fa45f8b2a3_v2_1_1').validate(obj)
    return True


def nfv_provisioning_detail(api):
    endpoint_result = api.site_design.nfv_provisioning_detail(
        active_validation=True,
        device_ip='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_nfv_provisioning_detail(api):
    assert is_valid_nfv_provisioning_detail(
        nfv_provisioning_detail(api)
    )


def nfv_provisioning_detail_default(api):
    endpoint_result = api.site_design.nfv_provisioning_detail(
        active_validation=True,
        device_ip=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_nfv_provisioning_detail_default(api):
    try:
        assert is_valid_nfv_provisioning_detail(
            nfv_provisioning_detail_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_nfv_profile(obj):
    json_schema_validate('jsd_5ebbfa2541b8b8a9_v2_1_1').validate(obj)
    return True


def delete_nfv_profile(api):
    endpoint_result = api.site_design.delete_nfv_profile(
        id='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_delete_nfv_profile(api):
    assert is_valid_delete_nfv_profile(
        delete_nfv_profile(api)
    )


def delete_nfv_profile_default(api):
    endpoint_result = api.site_design.delete_nfv_profile(
        id='string',
        name=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_delete_nfv_profile_default(api):
    try:
        assert is_valid_delete_nfv_profile(
            delete_nfv_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_nfv_profile(obj):
    json_schema_validate('jsd_66951aaa407ba89c_v2_1_1').validate(obj)
    return True


def create_nfv_profile(api):
    endpoint_result = api.site_design.create_nfv_profile(
        active_validation=True,
        device=[{'deviceType': 'Cisco 5400 Enterprise Network Compute System', 'deviceTag': 'string', 'serviceProviderProfile': [{'serviceProvider': 'string', 'linkType': 'GigabitEthernet', 'connect': True, 'connectDefaultGatewayOnWan': True}], 'directInternetAccessForFirewall': True, 'services': [{'serviceType': 'isr', 'profileType': 'ASAv5', 'serviceName': 'string', 'imageName': 'string', 'vNicMapping': [{'networkType': 'wan-net', 'assignIpAddressToNetwork': 'string'}], 'firewallMode': 'routed'}], 'customNetworks': [{'networkName': 'string', 'servicesToConnect': [{'serviceName': 'string'}], 'connectionType': 'wan-net', 'vlanMode': 'trunk', 'vlanId': 0}], 'vlanForL2': [{'vlanType': 'access', 'vlanId': 0, 'vlanDescription': 'string'}], 'customTemplate': [{'deviceType': 'Cisco 5400 Enterprise Network Compute System', 'template': 'string', 'templateType': 'Onboarding Template(s)'}]}],
        payload=None,
        profileName='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_create_nfv_profile(api):
    assert is_valid_create_nfv_profile(
        create_nfv_profile(api)
    )


def create_nfv_profile_default(api):
    endpoint_result = api.site_design.create_nfv_profile(
        active_validation=True,
        device=None,
        payload=None,
        profileName=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_create_nfv_profile_default(api):
    try:
        assert is_valid_create_nfv_profile(
            create_nfv_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_provision_nfv(obj):
    json_schema_validate('jsd_6f9cda9a465884b4_v2_1_1').validate(obj)
    return True


def provision_nfv(api):
    endpoint_result = api.site_design.provision_nfv(
        active_validation=True,
        payload=None,
        provisioning=[{'site': {'siteProfileName': 'string', 'area': {'name': 'string', 'parentName': 'string'}, 'building': {'name': 'string', 'address': 'string', 'latitude': 0, 'longitude': 0, 'parentName': 'string'}, 'floor': {'name': 'string', 'parentName': 'string', 'rfModel': 'string', 'width': 0, 'length': 0, 'height': 0}}, 'device': [{'ip': 'string', 'deviceSerialNumber': 'string', 'tagName': 'string', 'serviceProviders': [{'serviceProvider': 'string', 'wanInterface': {'ipAddress': 'string', 'interfaceName': 'string', 'subnetmask': 'string', 'bandwidth': 'string', 'gateway': 'string'}}], 'services': [{'type': 'string', 'mode': 'string', 'systemIp': 'string', 'centralManagerIP': 'string', 'centralRegistrationKey': 'string', 'commonKey': 'string', 'adminPasswordHash': 'string', 'disk': 'string'}], 'vlan': [{'type': 'string', 'id': 'string', 'interfaces': 'string', 'network': 'string'}], 'subPools': [{'type': 'Lan', 'name': 'string', 'ipSubnet': 'string', 'gateway': 'string', 'parentPoolName': 'string'}], 'customNetworks': [{'name': 'string', 'port': 'string', 'ipAddressPool': 'string'}], 'templateParam': {'nfvis': {'var1': 'string'}, 'asav': {'var1': 'string'}}}]}],
        siteProfile=[{'siteProfileName': 'string', 'device': [{'deviceType': 'ENCS5100', 'tagName': 'string', 'serviceProviders': [{'serviceProvider': 'string', 'linkType': 'GigabitEthernet', 'connect': True, 'defaultGateway': True}], 'dia': True, 'services': [{'type': 'isr', 'profile': 'string', 'mode': 'string', 'name': 'string', 'imageName': 'string', 'topology': {'type': 'string', 'name': 'string', 'assignIp': 'string'}}], 'customServices': [{'name': 'string', 'applicationType': 'string', 'profile': 'string', 'topology': {'type': 'string', 'name': 'string', 'assignIp': 'string'}, 'imageName': 'string'}], 'customNetworks': [{'name': 'string', 'servicesToConnect': [{'service': 'string'}], 'connectionType': 'string', 'networkMode': 'string', 'vlan': 'string'}], 'vlan': [{'type': 'string', 'id': 'string'}], 'customTemplate': [{'deviceType': 'NFVIS', 'template': 'string'}]}]}]
    )
    return endpoint_result


@pytest.mark.site_design
def test_provision_nfv(api):
    assert is_valid_provision_nfv(
        provision_nfv(api)
    )


def provision_nfv_default(api):
    endpoint_result = api.site_design.provision_nfv(
        active_validation=True,
        payload=None,
        provisioning=None,
        siteProfile=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_provision_nfv_default(api):
    try:
        assert is_valid_provision_nfv(
            provision_nfv_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_device_details_by_ip(obj):
    json_schema_validate('jsd_9cb2cb3f494a824f_v2_1_1').validate(obj)
    return True


def get_device_details_by_ip(api):
    endpoint_result = api.site_design.get_device_details_by_ip(
        device_ip='string'
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_device_details_by_ip(api):
    assert is_valid_get_device_details_by_ip(
        get_device_details_by_ip(api)
    )


def get_device_details_by_ip_default(api):
    endpoint_result = api.site_design.get_device_details_by_ip(
        device_ip=None
    )
    return endpoint_result


@pytest.mark.site_design
def test_get_device_details_by_ip_default(api):
    try:
        assert is_valid_get_device_details_by_ip(
            get_device_details_by_ip_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

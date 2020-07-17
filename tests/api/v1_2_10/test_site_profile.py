# -*- coding: utf-8 -*-
"""DNACenterAPI site_profile API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_get_device_details_by_ip(obj):
    json_schema_validate('jsd_7fbe4b804879baa4_v1_2_10').validate(obj)
    return True


def get_device_details_by_ip(api):
    endpoint_result = api.site_profile.get_device_details_by_ip(
        device_ip='string'
    )
    return endpoint_result


@pytest.mark.site_profile
def test_get_device_details_by_ip(api):
    assert is_valid_get_device_details_by_ip(
        get_device_details_by_ip(api)
    )


def get_device_details_by_ip_default(api):
    endpoint_result = api.site_profile.get_device_details_by_ip(
        device_ip=None
    )
    return endpoint_result


@pytest.mark.site_profile
def test_get_device_details_by_ip_default(api):
    try:
        assert is_valid_get_device_details_by_ip(
            get_device_details_by_ip_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_provision_nfv(obj):
    json_schema_validate('jsd_828828f44f28bd0d_v1_2_10').validate(obj)
    return True


def provision_nfv(api):
    endpoint_result = api.site_profile.provision_nfv(
        active_validation=True,
        callbackUrl='string',
        payload=None,
        provisioning=[{'site': {'siteProfileName': 'string', 'area': {'name': 'string', 'parentName': 'string'}, 'building': {'name': 'string', 'address': 'string'}, 'floor': {'name': 'string', 'parentName': 'string'}}, 'templateParam': {'nfvis': {'var1': 'string'}, 'asav': {'var1': 'string'}}, 'networksettings': {'ipPool': {'globalPool': {'name': 'string'}}}, 'device': [{'ip': 'string', 'deviceSerialNumber': 'string', 'tagName': 'string', 'serviceProviders': [{'serviceProvider': 'string', 'wanInterface': {'ipAddress': 'string', 'interfaceName': 'string', 'subnetmask': 'string', 'bandwidth': 'string', 'gateway': 'string'}}], 'services': [{'type': 'string', 'mode': 'string', 'systemIp': 'string', 'centralManagerIP': 'string', 'centralRegistrationKey': 'string', 'commonKey': 'string', 'adminPasswordHash': 'string'}], 'vlan': [{'type': 'string', 'id': 'string', 'interfaces': 'string', 'network': 'string'}], 'subPools': [{'type': 'Lan', 'name': 'string', 'ipSubnet': 'string', 'gateway': 'string'}], 'customNetworks': [{'name': 'string', 'port': 'string', 'ipAddressPool': 'string'}]}]}],
        siteProfile=[{'siteProfileName': 'string', 'device': [{'deviceType': 'ENCS5100', 'tagName': 'string', 'serviceProviders': [{'serviceProvider': 'string', 'linkType': 'GigabitEthernet', 'connect': True, 'defaultGateway': True}], 'dia': True, 'services': [{'type': 'isr', 'profile': 'string', 'mode': 'string'}], 'customServices': [{'name': 'string', 'applicationType': 'string', 'profile': 'string'}], 'customNetworks': [{'name': 'string', 'servicesToConnect': [{'service': 'string'}], 'connectionType': 'string', 'networkMode': 'string', 'vlan': 'string'}], 'vlan': [{'type': 'string', 'id': 'string'}]}], 'customTemplate': [{'deviceType': 'NFVIS', 'template': 'string'}]}]
    )
    return endpoint_result


@pytest.mark.site_profile
def test_provision_nfv(api):
    assert is_valid_provision_nfv(
        provision_nfv(api)
    )


def provision_nfv_default(api):
    endpoint_result = api.site_profile.provision_nfv(
        active_validation=True,
        callbackUrl=None,
        payload=None,
        provisioning=None,
        siteProfile=None
    )
    return endpoint_result


@pytest.mark.site_profile
def test_provision_nfv_default(api):
    try:
        assert is_valid_provision_nfv(
            provision_nfv_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

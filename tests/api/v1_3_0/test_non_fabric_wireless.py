# -*- coding: utf-8 -*-
"""DNACenterAPI non_fabric_wireless API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.0', reason='version does not match')


def is_valid_provision(obj):
    json_schema_validate('jsd_07913b7f4e1880de_v1_3_0').validate(obj)
    return True


def provision(api):
    endpoint_result = api.non_fabric_wireless.provision(
        active_validation=True,
        payload=[{'deviceName': 'string', 'site': 'string', 'managedAPLocations': ['string'], 'dynamicInterfaces': [{'interfaceIPAddress': 'string', 'interfaceNetmaskInCIDR': 0, 'interfaceGateway': 'string', 'lagOrPortNumber': 0, 'vlanId': 0, 'interfaceName': 'string'}]}]
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_provision(api):
    assert is_valid_provision(
        provision(api)
    )


def provision_default(api):
    endpoint_result = api.non_fabric_wireless.provision(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_provision_default(api):
    try:
        assert is_valid_provision(
            provision_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_wireless_profile(obj):
    json_schema_validate('jsd_20872aec43b9bf50_v1_3_0').validate(obj)
    return True


def update_wireless_profile(api):
    endpoint_result = api.non_fabric_wireless.update_wireless_profile(
        active_validation=True,
        payload=None,
        profileDetails={'name': 'string', 'sites': ['string'], 'ssidDetails': [{'name': 'string', 'type': 'Guest', 'enableFabric': True, 'flexConnect': {'enableFlexConnect': True, 'localToVlan': 0}, 'interfaceName': 'string'}]}
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_update_wireless_profile(api):
    assert is_valid_update_wireless_profile(
        update_wireless_profile(api)
    )


def update_wireless_profile_default(api):
    endpoint_result = api.non_fabric_wireless.update_wireless_profile(
        active_validation=True,
        payload=None,
        profileDetails=None
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_update_wireless_profile_default(api):
    try:
        assert is_valid_update_wireless_profile(
            update_wireless_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_wireless_profile(obj):
    json_schema_validate('jsd_6896993e41b8bd7a_v1_3_0').validate(obj)
    return True


def get_wireless_profile(api):
    endpoint_result = api.non_fabric_wireless.get_wireless_profile(
        profile_name='string'
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_get_wireless_profile(api):
    assert is_valid_get_wireless_profile(
        get_wireless_profile(api)
    )


def get_wireless_profile_default(api):
    endpoint_result = api.non_fabric_wireless.get_wireless_profile(
        profile_name=None
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_get_wireless_profile_default(api):
    try:
        assert is_valid_get_wireless_profile(
            get_wireless_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_provision(obj):
    json_schema_validate('jsd_a0be3a2f47ab9f3c_v1_3_0').validate(obj)
    return True


def update_provision(api):
    endpoint_result = api.non_fabric_wireless.update_provision(
        active_validation=True,
        payload=[{'deviceName': 'string', 'managedAPLocations': ['string'], 'dynamicInterfaces': [{'interfaceIPAddress': 'string', 'interfaceNetmaskInCIDR': 0, 'interfaceGateway': 'string', 'lagOrPortNumber': 0, 'vlanId': 0, 'interfaceName': 'string'}]}]
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_update_provision(api):
    assert is_valid_update_provision(
        update_provision(api)
    )


def update_provision_default(api):
    endpoint_result = api.non_fabric_wireless.update_provision(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_update_provision_default(api):
    try:
        assert is_valid_update_provision(
            update_provision_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_wireless_profile(obj):
    json_schema_validate('jsd_ae86a8c14b5980b7_v1_3_0').validate(obj)
    return True


def delete_wireless_profile(api):
    endpoint_result = api.non_fabric_wireless.delete_wireless_profile(
        wireless_profile_name='string'
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_delete_wireless_profile(api):
    assert is_valid_delete_wireless_profile(
        delete_wireless_profile(api)
    )


def delete_wireless_profile_default(api):
    endpoint_result = api.non_fabric_wireless.delete_wireless_profile(
        wireless_profile_name='string'
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_delete_wireless_profile_default(api):
    try:
        assert is_valid_delete_wireless_profile(
            delete_wireless_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_wireless_profile(obj):
    json_schema_validate('jsd_47ba59204e0ab742_v1_3_0').validate(obj)
    return True


def create_wireless_profile(api):
    endpoint_result = api.non_fabric_wireless.create_wireless_profile(
        active_validation=True,
        payload=None,
        profileDetails={'name': 'string', 'sites': ['string'], 'ssidDetails': [{'name': 'string', 'type': 'Guest', 'enableFabric': True, 'flexConnect': {'enableFlexConnect': True, 'localToVlan': 0}, 'interfaceName': 'string'}]}
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_create_wireless_profile(api):
    assert is_valid_create_wireless_profile(
        create_wireless_profile(api)
    )


def create_wireless_profile_default(api):
    endpoint_result = api.non_fabric_wireless.create_wireless_profile(
        active_validation=True,
        payload=None,
        profileDetails=None
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_create_wireless_profile_default(api):
    try:
        assert is_valid_create_wireless_profile(
            create_wireless_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_and_provision_ssid(obj):
    json_schema_validate('jsd_db9f997f4e59aec1_v1_3_0').validate(obj)
    return True


def create_and_provision_ssid(api):
    endpoint_result = api.non_fabric_wireless.create_and_provision_ssid(
        active_validation=True,
        enableFabric=True,
        flexConnect={'enableFlexConnect': True, 'localToVlan': 0},
        managedAPLocations=['string'],
        payload=None,
        ssidDetails={'name': 'string', 'securityLevel': 'WPA2_ENTERPRISE', 'enableFastLane': True, 'passphrase': 'string', 'trafficType': 'data', 'enableBroadcastSSID': True, 'radioPolicy': 'Dual band operation (2.4GHz and 5GHz)', 'enableMACFiltering': True, 'fastTransition': 'Adaptive', 'webAuthURL': 'string'},
        ssidType='Guest'
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_create_and_provision_ssid(api):
    assert is_valid_create_and_provision_ssid(
        create_and_provision_ssid(api)
    )


def create_and_provision_ssid_default(api):
    endpoint_result = api.non_fabric_wireless.create_and_provision_ssid(
        active_validation=True,
        enableFabric=None,
        flexConnect=None,
        managedAPLocations=None,
        payload=None,
        ssidDetails=None,
        ssidType=None
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_create_and_provision_ssid_default(api):
    try:
        assert is_valid_create_and_provision_ssid(
            create_and_provision_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_enterprise_ssid(obj):
    json_schema_validate('jsd_c7a6592b4b98a369_v1_3_0').validate(obj)
    return True


def delete_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.delete_enterprise_ssid(
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_delete_enterprise_ssid(api):
    assert is_valid_delete_enterprise_ssid(
        delete_enterprise_ssid(api)
    )


def delete_enterprise_ssid_default(api):
    endpoint_result = api.non_fabric_wireless.delete_enterprise_ssid(
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_delete_enterprise_ssid_default(api):
    try:
        assert is_valid_delete_enterprise_ssid(
            delete_enterprise_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_and_provision_ssid(obj):
    json_schema_validate('jsd_cca098344a489dfa_v1_3_0').validate(obj)
    return True


def delete_and_provision_ssid(api):
    endpoint_result = api.non_fabric_wireless.delete_and_provision_ssid(
        managed_aplocations='string',
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_delete_and_provision_ssid(api):
    assert is_valid_delete_and_provision_ssid(
        delete_and_provision_ssid(api)
    )


def delete_and_provision_ssid_default(api):
    endpoint_result = api.non_fabric_wireless.delete_and_provision_ssid(
        managed_aplocations='string',
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_delete_and_provision_ssid_default(api):
    try:
        assert is_valid_delete_and_provision_ssid(
            delete_and_provision_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_enterprise_ssid(obj):
    json_schema_validate('jsd_cca519ba45ebb423_v1_3_0').validate(obj)
    return True


def get_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.get_enterprise_ssid(
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_get_enterprise_ssid(api):
    assert is_valid_get_enterprise_ssid(
        get_enterprise_ssid(api)
    )


def get_enterprise_ssid_default(api):
    endpoint_result = api.non_fabric_wireless.get_enterprise_ssid(
        ssid_name=None
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_get_enterprise_ssid_default(api):
    try:
        assert is_valid_get_enterprise_ssid(
            get_enterprise_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_enterprise_ssid(obj):
    return True if obj else False


def create_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.create_enterprise_ssid(
        active_validation=True,
        enableBroadcastSSID=True,
        enableFastLane=True,
        enableMACFiltering=True,
        fastTransition='Adaptive',
        name='********************************',
        passphrase='********',
        payload=None,
        radioPolicy='Dual band operation (2.4GHz and 5GHz)',
        securityLevel='WPA2_ENTERPRISE',
        trafficType='voicedata'
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_create_enterprise_ssid(api):
    assert is_valid_create_enterprise_ssid(
        create_enterprise_ssid(api)
    )


def create_enterprise_ssid_default(api):
    endpoint_result = api.non_fabric_wireless.create_enterprise_ssid(
        active_validation=True,
        enableBroadcastSSID=None,
        enableFastLane=None,
        enableMACFiltering=None,
        fastTransition=None,
        name=None,
        passphrase=None,
        payload=None,
        radioPolicy=None,
        securityLevel=None,
        trafficType=None
    )
    return endpoint_result


@pytest.mark.non_fabric_wireless
def test_create_enterprise_ssid_default(api):
    try:
        assert is_valid_create_enterprise_ssid(
            create_enterprise_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

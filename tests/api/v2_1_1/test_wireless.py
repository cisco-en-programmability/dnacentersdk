# -*- coding: utf-8 -*-
"""DNACenterAPI wireless API fixtures and tests.

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


def is_valid_retrieve_rf_profiles(obj):
    json_schema_validate('jsd_098cab9141c9a3fe_v2_1_1').validate(obj)
    return True


def retrieve_rf_profiles(api):
    endpoint_result = api.wireless.retrieve_rf_profiles(
        rf_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_rf_profiles(api):
    assert is_valid_retrieve_rf_profiles(
        retrieve_rf_profiles(api)
    )


def retrieve_rf_profiles_default(api):
    endpoint_result = api.wireless.retrieve_rf_profiles(
        rf_profile_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_rf_profiles_default(api):
    try:
        assert is_valid_retrieve_rf_profiles(
            retrieve_rf_profiles_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_and_provision_ssid(obj):
    json_schema_validate('jsd_1eb72ad34e098990_v2_1_1').validate(obj)
    return True


def create_and_provision_ssid(api):
    endpoint_result = api.wireless.create_and_provision_ssid(
        active_validation=True,
        enableFabric=True,
        flexConnect={'enableFlexConnect': True, 'localToVlan': 0},
        managedAPLocations=['string'],
        payload=None,
        ssidDetails={'name': 'string', 'securityLevel': 'WPA2_ENTERPRISE', 'enableFastLane': True, 'passphrase': 'string', 'trafficType': 'data', 'enableBroadcastSSID': True, 'radioPolicy': 'Dual band operation (2.4GHz and 5GHz)', 'enableMACFiltering': True, 'fastTransition': 'Adaptive', 'webAuthURL': 'string'},
        ssidType='Guest'
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_and_provision_ssid(api):
    assert is_valid_create_and_provision_ssid(
        create_and_provision_ssid(api)
    )


def create_and_provision_ssid_default(api):
    endpoint_result = api.wireless.create_and_provision_ssid(
        active_validation=True,
        enableFabric=None,
        flexConnect=None,
        managedAPLocations=None,
        payload=None,
        ssidDetails=None,
        ssidType=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_and_provision_ssid_default(api):
    try:
        assert is_valid_create_and_provision_ssid(
            create_and_provision_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_rf_profiles(obj):
    json_schema_validate('jsd_28b24a744a9994be_v2_1_1').validate(obj)
    return True


def delete_rf_profiles(api):
    endpoint_result = api.wireless.delete_rf_profiles(
        rf_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_rf_profiles(api):
    assert is_valid_delete_rf_profiles(
        delete_rf_profiles(api)
    )


def delete_rf_profiles_default(api):
    endpoint_result = api.wireless.delete_rf_profiles(
        rf_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_rf_profiles_default(api):
    try:
        assert is_valid_delete_rf_profiles(
            delete_rf_profiles_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_wireless_profile(obj):
    json_schema_validate('jsd_709769624bf988d5_v2_1_1').validate(obj)
    return True


def create_wireless_profile(api):
    endpoint_result = api.wireless.create_wireless_profile(
        active_validation=True,
        payload=None,
        profileDetails={'name': 'string', 'sites': ['string'], 'ssidDetails': [{'name': 'string', 'type': 'Guest', 'enableFabric': True, 'flexConnect': {'enableFlexConnect': True, 'localToVlan': 0}, 'interfaceName': 'string'}]}
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_wireless_profile(api):
    assert is_valid_create_wireless_profile(
        create_wireless_profile(api)
    )


def create_wireless_profile_default(api):
    endpoint_result = api.wireless.create_wireless_profile(
        active_validation=True,
        payload=None,
        profileDetails=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_wireless_profile_default(api):
    try:
        assert is_valid_create_wireless_profile(
            create_wireless_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_provision_update(obj):
    json_schema_validate('jsd_87a5ab044139862d_v2_1_1').validate(obj)
    return True


def provision_update(api):
    endpoint_result = api.wireless.provision_update(
        active_validation=True,
        payload=[{'deviceName': 'string', 'managedAPLocations': ['string'], 'dynamicInterfaces': [{'interfaceIPAddress': 'string', 'interfaceNetmaskInCIDR': 0, 'interfaceGateway': 'string', 'lagOrPortNumber': 0, 'vlanId': 0, 'interfaceName': 'string'}]}]
    )
    return endpoint_result


@pytest.mark.wireless
def test_provision_update(api):
    assert is_valid_provision_update(
        provision_update(api)
    )


def provision_update_default(api):
    endpoint_result = api.wireless.provision_update(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_provision_update_default(api):
    try:
        assert is_valid_provision_update(
            provision_update_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_enterprise_ssid(obj):
    return True if obj else False


def create_enterprise_ssid(api):
    endpoint_result = api.wireless.create_enterprise_ssid(
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


@pytest.mark.wireless
def test_create_enterprise_ssid(api):
    assert is_valid_create_enterprise_ssid(
        create_enterprise_ssid(api)
    )


def create_enterprise_ssid_default(api):
    endpoint_result = api.wireless.create_enterprise_ssid(
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


@pytest.mark.wireless
def test_create_enterprise_ssid_default(api):
    try:
        assert is_valid_create_enterprise_ssid(
            create_enterprise_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_wireless_profile(obj):
    json_schema_validate('jsd_b3a1c8804c8b9b8b_v2_1_1').validate(obj)
    return True


def get_wireless_profile(api):
    endpoint_result = api.wireless.get_wireless_profile(
        profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_wireless_profile(api):
    assert is_valid_get_wireless_profile(
        get_wireless_profile(api)
    )


def get_wireless_profile_default(api):
    endpoint_result = api.wireless.get_wireless_profile(
        profile_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_wireless_profile_default(api):
    try:
        assert is_valid_get_wireless_profile(
            get_wireless_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_or_update_rf_profile(obj):
    json_schema_validate('jsd_b78329674878b815_v2_1_1').validate(obj)
    return True


def create_or_update_rf_profile(api):
    endpoint_result = api.wireless.create_or_update_rf_profile(
        active_validation=True,
        channelWidth='string',
        defaultRfProfile=True,
        enableBrownField=True,
        enableCustom=True,
        enableRadioTypeA=True,
        enableRadioTypeB=True,
        name='string',
        payload=None,
        radioTypeAProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'powerThresholdV1': 0, 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0},
        radioTypeBProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'powerThresholdV1': 0, 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0}
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_or_update_rf_profile(api):
    assert is_valid_create_or_update_rf_profile(
        create_or_update_rf_profile(api)
    )


def create_or_update_rf_profile_default(api):
    endpoint_result = api.wireless.create_or_update_rf_profile(
        active_validation=True,
        channelWidth=None,
        defaultRfProfile=None,
        enableBrownField=None,
        enableCustom=None,
        enableRadioTypeA=None,
        enableRadioTypeB=None,
        name=None,
        payload=None,
        radioTypeAProperties=None,
        radioTypeBProperties=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_or_update_rf_profile_default(api):
    try:
        assert is_valid_create_or_update_rf_profile(
            create_or_update_rf_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_enterprise_ssid(obj):
    json_schema_validate('jsd_c7a6592b4b98a369_v2_1_1').validate(obj)
    return True


def delete_enterprise_ssid(api):
    endpoint_result = api.wireless.delete_enterprise_ssid(
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_enterprise_ssid(api):
    assert is_valid_delete_enterprise_ssid(
        delete_enterprise_ssid(api)
    )


def delete_enterprise_ssid_default(api):
    endpoint_result = api.wireless.delete_enterprise_ssid(
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_enterprise_ssid_default(api):
    try:
        assert is_valid_delete_enterprise_ssid(
            delete_enterprise_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_provision(obj):
    json_schema_validate('jsd_d09b08a3447aa3b9_v2_1_1').validate(obj)
    return True


def provision(api):
    endpoint_result = api.wireless.provision(
        active_validation=True,
        payload=[{'deviceName': 'string', 'site': 'string', 'managedAPLocations': ['string'], 'dynamicInterfaces': [{'interfaceIPAddress': 'string', 'interfaceNetmaskInCIDR': 0, 'interfaceGateway': 'string', 'lagOrPortNumber': 0, 'vlanId': 0, 'interfaceName': 'string'}]}]
    )
    return endpoint_result


@pytest.mark.wireless
def test_provision(api):
    assert is_valid_provision(
        provision(api)
    )


def provision_default(api):
    endpoint_result = api.wireless.provision(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_provision_default(api):
    try:
        assert is_valid_provision(
            provision_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_enterprise_ssid(obj):
    json_schema_validate('jsd_cca519ba45ebb423_v2_1_1').validate(obj)
    return True


def get_enterprise_ssid(api):
    endpoint_result = api.wireless.get_enterprise_ssid(
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_enterprise_ssid(api):
    assert is_valid_get_enterprise_ssid(
        get_enterprise_ssid(api)
    )


def get_enterprise_ssid_default(api):
    endpoint_result = api.wireless.get_enterprise_ssid(
        ssid_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_enterprise_ssid_default(api):
    try:
        assert is_valid_get_enterprise_ssid(
            get_enterprise_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_ap_provision(obj):
    json_schema_validate('jsd_e9b99b2248c88014_v2_1_1').validate(obj)
    return True


def ap_provision(api):
    endpoint_result = api.wireless.ap_provision(
        active_validation=True,
        payload=[{'rfProfile': 'string', 'siteId': 'string', 'type': 'string', 'deviceName': 'string', 'customFlexGroupName': ['string'], 'customApGroupName': 'string'}]
    )
    return endpoint_result


@pytest.mark.wireless
def test_ap_provision(api):
    assert is_valid_ap_provision(
        ap_provision(api)
    )


def ap_provision_default(api):
    endpoint_result = api.wireless.ap_provision(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_ap_provision_default(api):
    try:
        assert is_valid_ap_provision(
            ap_provision_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_ap_provision_and_re_provision(obj):
    json_schema_validate('jsd_d89719b847aaa9c4_v2_1_1').validate(obj)
    return True


def ap_provision_and_re_provision(api):
    endpoint_result = api.wireless.ap_provision_and_re_provision(
        active_validation=True,
        payload=[{'executionId': 'string', 'executionUrl': 'string', 'message': 'string'}]
    )
    return endpoint_result


@pytest.mark.wireless
def test_ap_provision_and_re_provision(api):
    assert is_valid_ap_provision_and_re_provision(
        ap_provision_and_re_provision(api)
    )


def ap_provision_and_re_provision_default(api):
    endpoint_result = api.wireless.ap_provision_and_re_provision(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_ap_provision_and_re_provision_default(api):
    try:
        assert is_valid_ap_provision_and_re_provision(
            ap_provision_and_re_provision_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_wireless_profile(obj):
    json_schema_validate('jsd_cfbd3870405aad55_v2_1_1').validate(obj)
    return True


def update_wireless_profile(api):
    endpoint_result = api.wireless.update_wireless_profile(
        active_validation=True,
        payload=None,
        profileDetails={'name': 'string', 'sites': ['string'], 'ssidDetails': [{'name': 'string', 'type': 'Guest', 'enableFabric': True, 'flexConnect': {'enableFlexConnect': True, 'localToVlan': 0}, 'interfaceName': 'string'}]}
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_wireless_profile(api):
    assert is_valid_update_wireless_profile(
        update_wireless_profile(api)
    )


def update_wireless_profile_default(api):
    endpoint_result = api.wireless.update_wireless_profile(
        active_validation=True,
        payload=None,
        profileDetails=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_wireless_profile_default(api):
    try:
        assert is_valid_update_wireless_profile(
            update_wireless_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_wireless_profile(obj):
    json_schema_validate('jsd_e39588a5494982c4_v2_1_1').validate(obj)
    return True


def delete_wireless_profile(api):
    endpoint_result = api.wireless.delete_wireless_profile(
        wireless_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_wireless_profile(api):
    assert is_valid_delete_wireless_profile(
        delete_wireless_profile(api)
    )


def delete_wireless_profile_default(api):
    endpoint_result = api.wireless.delete_wireless_profile(
        wireless_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_wireless_profile_default(api):
    try:
        assert is_valid_delete_wireless_profile(
            delete_wireless_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_ssid_and_provision_it_to_devices(obj):
    json_schema_validate('jsd_fc9538fe43d9884d_v2_1_1').validate(obj)
    return True


def delete_ssid_and_provision_it_to_devices(api):
    endpoint_result = api.wireless.delete_ssid_and_provision_it_to_devices(
        managed_aplocations='string',
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_ssid_and_provision_it_to_devices(api):
    assert is_valid_delete_ssid_and_provision_it_to_devices(
        delete_ssid_and_provision_it_to_devices(api)
    )


def delete_ssid_and_provision_it_to_devices_default(api):
    endpoint_result = api.wireless.delete_ssid_and_provision_it_to_devices(
        managed_aplocations='string',
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_ssid_and_provision_it_to_devices_default(api):
    try:
        assert is_valid_delete_ssid_and_provision_it_to_devices(
            delete_ssid_and_provision_it_to_devices_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

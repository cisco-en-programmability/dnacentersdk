# -*- coding: utf-8 -*-
"""CatalystCenterAPI wireless API fixtures and tests.

Copyright (c) 2025 Cisco Systems.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '3.1.3.0', reason='version does not match')


def is_valid_sensor_test_results_v1(json_schema_validate, obj):
    json_schema_validate('jsd_dde2b077d6d052dcae5a76f4aac09c1d_v3_1_3_0').validate(obj)
    return True


def sensor_test_results_v1(api):
    endpoint_result = api.wireless.sensor_test_results_v1(
        end_time=0,
        site_id='string',
        start_time=0,
        test_failure_by='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_sensor_test_results_v1(api, validator):
    try:
        assert is_valid_sensor_test_results_v1(
            validator,
            sensor_test_results_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def sensor_test_results_v1_default_val(api):
    endpoint_result = api.wireless.sensor_test_results_v1(
        end_time=None,
        site_id=None,
        start_time=None,
        test_failure_by=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_sensor_test_results_v1_default_val(api, validator):
    try:
        assert is_valid_sensor_test_results_v1(
            validator,
            sensor_test_results_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_and_provision_ssid_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d825ae9a117f5b6bb65b7d78fd42513c_v3_1_3_0').validate(obj)
    return True


def create_and_provision_ssid_v1(api):
    endpoint_result = api.wireless.create_and_provision_ssid_v1(
        active_validation=True,
        enableFabric=True,
        flexConnect={'enableFlexConnect': True, 'localToVlan': 0},
        managedAPLocations=['string'],
        payload=None,
        ssidDetails={'name': 'string', 'securityLevel': 'string', 'enableFastLane': True, 'passphrase': 'string', 'trafficType': 'string', 'enableBroadcastSSID': True, 'radioPolicy': 'string', 'enableMACFiltering': True, 'fastTransition': 'string', 'webAuthURL': 'string', 'authKeyMgmt': ['string'], 'rsnCipherSuiteGcmp256': True, 'rsnCipherSuiteGcmp128': True, 'rsnCipherSuiteCcmp256': True, 'ghz6PolicyClientSteering': True, 'ghz24Policy': 'string'},
        ssidType='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_and_provision_ssid_v1(api, validator):
    try:
        assert is_valid_create_and_provision_ssid_v1(
            validator,
            create_and_provision_ssid_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_and_provision_ssid_v1_default_val(api):
    endpoint_result = api.wireless.create_and_provision_ssid_v1(
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
def test_create_and_provision_ssid_v1_default_val(api, validator):
    try:
        assert is_valid_create_and_provision_ssid_v1(
            validator,
            create_and_provision_ssid_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_ssid_and_provision_it_to_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8e56eb2c294159d891b7dbe493ddc434_v3_1_3_0').validate(obj)
    return True


def delete_ssid_and_provision_it_to_devices_v1(api):
    endpoint_result = api.wireless.delete_ssid_and_provision_it_to_devices_v1(
        managed_aplocations='string',
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_ssid_and_provision_it_to_devices_v1(api, validator):
    try:
        assert is_valid_delete_ssid_and_provision_it_to_devices_v1(
            validator,
            delete_ssid_and_provision_it_to_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_ssid_and_provision_it_to_devices_v1_default_val(api):
    endpoint_result = api.wireless.delete_ssid_and_provision_it_to_devices_v1(
        managed_aplocations='string',
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_ssid_and_provision_it_to_devices_v1_default_val(api, validator):
    try:
        assert is_valid_delete_ssid_and_provision_it_to_devices_v1(
            validator,
            delete_ssid_and_provision_it_to_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reboot_access_points_v1(json_schema_validate, obj):
    json_schema_validate('jsd_858f5602b2965e53b5bdda193025a3fc_v3_1_3_0').validate(obj)
    return True


def reboot_access_points_v1(api):
    endpoint_result = api.wireless.reboot_access_points_v1(
        active_validation=True,
        apMacAddresses=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_reboot_access_points_v1(api, validator):
    try:
        assert is_valid_reboot_access_points_v1(
            validator,
            reboot_access_points_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def reboot_access_points_v1_default_val(api):
    endpoint_result = api.wireless.reboot_access_points_v1(
        active_validation=True,
        apMacAddresses=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_reboot_access_points_v1_default_val(api, validator):
    try:
        assert is_valid_reboot_access_points_v1(
            validator,
            reboot_access_points_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_access_point_reboot_task_result_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1ebabf7f1ce2537f8aedd93e5f5aab1b_v3_1_3_0').validate(obj)
    return True


def get_access_point_reboot_task_result_v1(api):
    endpoint_result = api.wireless.get_access_point_reboot_task_result_v1(
        parent_task_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_access_point_reboot_task_result_v1(api, validator):
    try:
        assert is_valid_get_access_point_reboot_task_result_v1(
            validator,
            get_access_point_reboot_task_result_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_access_point_reboot_task_result_v1_default_val(api):
    endpoint_result = api.wireless.get_access_point_reboot_task_result_v1(
        parent_task_id=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_access_point_reboot_task_result_v1_default_val(api, validator):
    try:
        assert is_valid_get_access_point_reboot_task_result_v1(
            validator,
            get_access_point_reboot_task_result_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_enterprise_ssid_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fb757e8fce4b51ffa0ba1a8e5ae4d8c0_v3_1_3_0').validate(obj)
    return True


def get_enterprise_ssid_v1(api):
    endpoint_result = api.wireless.get_enterprise_ssid_v1(
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_enterprise_ssid_v1(api, validator):
    try:
        assert is_valid_get_enterprise_ssid_v1(
            validator,
            get_enterprise_ssid_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_enterprise_ssid_v1_default_val(api):
    endpoint_result = api.wireless.get_enterprise_ssid_v1(
        ssid_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_enterprise_ssid_v1_default_val(api, validator):
    try:
        assert is_valid_get_enterprise_ssid_v1(
            validator,
            get_enterprise_ssid_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_enterprise_ssid_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bc33daf690ec5399a507829abfc4fe64_v3_1_3_0').validate(obj)
    return True


def create_enterprise_ssid_v1(api):
    endpoint_result = api.wireless.create_enterprise_ssid_v1(
        aaaOverride=True,
        active_validation=True,
        authKeyMgmt=['string'],
        basicServiceSetClientIdleTimeout=0,
        clientExclusionTimeout=0,
        clientRateLimit=0,
        coverageHoleDetectionEnable=True,
        enableBasicServiceSetMaxIdle=True,
        enableBroadcastSSID=True,
        enableClientExclusion=True,
        enableDirectedMulticastService=True,
        enableFastLane=True,
        enableMACFiltering=True,
        enableNeighborList=True,
        enableSessionTimeOut=True,
        fastTransition='string',
        ghz24Policy='string',
        ghz6PolicyClientSteering=True,
        mfpClientProtection='string',
        multiPSKSettings=[{'priority': 0, 'passphraseType': 'string', 'passphrase': 'string'}],
        name='string',
        nasOptions=['string'],
        passphrase='string',
        payload=None,
        policyProfileName='string',
        profileName='string',
        protectedManagementFrame='string',
        radioPolicy='string',
        rsnCipherSuiteCcmp256=True,
        rsnCipherSuiteGcmp128=True,
        rsnCipherSuiteGcmp256=True,
        securityLevel='string',
        sessionTimeOut=0,
        trafficType='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_enterprise_ssid_v1(api, validator):
    try:
        assert is_valid_create_enterprise_ssid_v1(
            validator,
            create_enterprise_ssid_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_enterprise_ssid_v1_default_val(api):
    endpoint_result = api.wireless.create_enterprise_ssid_v1(
        aaaOverride=None,
        active_validation=True,
        authKeyMgmt=None,
        basicServiceSetClientIdleTimeout=None,
        clientExclusionTimeout=None,
        clientRateLimit=None,
        coverageHoleDetectionEnable=None,
        enableBasicServiceSetMaxIdle=None,
        enableBroadcastSSID=None,
        enableClientExclusion=None,
        enableDirectedMulticastService=None,
        enableFastLane=None,
        enableMACFiltering=None,
        enableNeighborList=None,
        enableSessionTimeOut=None,
        fastTransition=None,
        ghz24Policy=None,
        ghz6PolicyClientSteering=None,
        mfpClientProtection=None,
        multiPSKSettings=None,
        name=None,
        nasOptions=None,
        passphrase=None,
        payload=None,
        policyProfileName=None,
        profileName=None,
        protectedManagementFrame=None,
        radioPolicy=None,
        rsnCipherSuiteCcmp256=None,
        rsnCipherSuiteGcmp128=None,
        rsnCipherSuiteGcmp256=None,
        securityLevel=None,
        sessionTimeOut=None,
        trafficType=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_enterprise_ssid_v1_default_val(api, validator):
    try:
        assert is_valid_create_enterprise_ssid_v1(
            validator,
            create_enterprise_ssid_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_enterprise_ssid_v1(json_schema_validate, obj):
    json_schema_validate('jsd_25479623a94058a99acaaf8eb73c9227_v3_1_3_0').validate(obj)
    return True


def update_enterprise_ssid_v1(api):
    endpoint_result = api.wireless.update_enterprise_ssid_v1(
        aaaOverride=True,
        active_validation=True,
        authKeyMgmt=['string'],
        basicServiceSetClientIdleTimeout=0,
        clientExclusionTimeout=0,
        clientRateLimit=0,
        coverageHoleDetectionEnable=True,
        enableBasicServiceSetMaxIdle=True,
        enableBroadcastSSID=True,
        enableClientExclusion=True,
        enableDirectedMulticastService=True,
        enableFastLane=True,
        enableMACFiltering=True,
        enableNeighborList=True,
        enableSessionTimeOut=True,
        fastTransition='string',
        ghz24Policy='string',
        ghz6PolicyClientSteering=True,
        mfpClientProtection='string',
        multiPSKSettings=[{'priority': 0, 'passphraseType': 'string', 'passphrase': 'string'}],
        name='string',
        nasOptions=['string'],
        passphrase='string',
        payload=None,
        policyProfileName='string',
        profileName='string',
        protectedManagementFrame='string',
        radioPolicy='string',
        rsnCipherSuiteCcmp256=True,
        rsnCipherSuiteGcmp128=True,
        rsnCipherSuiteGcmp256=True,
        securityLevel='string',
        sessionTimeOut=0,
        trafficType='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_enterprise_ssid_v1(api, validator):
    try:
        assert is_valid_update_enterprise_ssid_v1(
            validator,
            update_enterprise_ssid_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_enterprise_ssid_v1_default_val(api):
    endpoint_result = api.wireless.update_enterprise_ssid_v1(
        aaaOverride=None,
        active_validation=True,
        authKeyMgmt=None,
        basicServiceSetClientIdleTimeout=None,
        clientExclusionTimeout=None,
        clientRateLimit=None,
        coverageHoleDetectionEnable=None,
        enableBasicServiceSetMaxIdle=None,
        enableBroadcastSSID=None,
        enableClientExclusion=None,
        enableDirectedMulticastService=None,
        enableFastLane=None,
        enableMACFiltering=None,
        enableNeighborList=None,
        enableSessionTimeOut=None,
        fastTransition=None,
        ghz24Policy=None,
        ghz6PolicyClientSteering=None,
        mfpClientProtection=None,
        multiPSKSettings=None,
        name=None,
        nasOptions=None,
        passphrase=None,
        payload=None,
        policyProfileName=None,
        profileName=None,
        protectedManagementFrame=None,
        radioPolicy=None,
        rsnCipherSuiteCcmp256=None,
        rsnCipherSuiteGcmp128=None,
        rsnCipherSuiteGcmp256=None,
        securityLevel=None,
        sessionTimeOut=None,
        trafficType=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_enterprise_ssid_v1_default_val(api, validator):
    try:
        assert is_valid_update_enterprise_ssid_v1(
            validator,
            update_enterprise_ssid_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_enterprise_ssid_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6a43afa4d91a5043996c682a7a7a2d62_v3_1_3_0').validate(obj)
    return True


def delete_enterprise_ssid_v1(api):
    endpoint_result = api.wireless.delete_enterprise_ssid_v1(
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_enterprise_ssid_v1(api, validator):
    try:
        assert is_valid_delete_enterprise_ssid_v1(
            validator,
            delete_enterprise_ssid_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_enterprise_ssid_v1_default_val(api):
    endpoint_result = api.wireless.delete_enterprise_ssid_v1(
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_enterprise_ssid_v1_default_val(api, validator):
    try:
        assert is_valid_delete_enterprise_ssid_v1(
            validator,
            delete_enterprise_ssid_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_aaa_radius_attributes_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4f8db651a7bb5f85a936c9fdadf3a9d9_v3_1_3_0').validate(obj)
    return True


def create_aaa_radius_attributes_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.create_aaa_radius_attributes_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'calledStationId': 'string'},
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_aaa_radius_attributes_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_create_aaa_radius_attributes_configuration_feature_template_v1(
            validator,
            create_aaa_radius_attributes_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_aaa_radius_attributes_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.create_aaa_radius_attributes_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_aaa_radius_attributes_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_create_aaa_radius_attributes_configuration_feature_template_v1(
            validator,
            create_aaa_radius_attributes_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_aaa_radius_attributes_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8dbce6135f7a5581bba6893f6b134999_v3_1_3_0').validate(obj)
    return True


def get_aaa_radius_attributes_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.get_aaa_radius_attributes_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_aaa_radius_attributes_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_get_aaa_radius_attributes_configuration_feature_template_v1(
            validator,
            get_aaa_radius_attributes_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_aaa_radius_attributes_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.get_aaa_radius_attributes_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_aaa_radius_attributes_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_get_aaa_radius_attributes_configuration_feature_template_v1(
            validator,
            get_aaa_radius_attributes_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_aaa_radius_attributes_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5f75156ff30d50d1bced4ec466b56b38_v3_1_3_0').validate(obj)
    return True


def update_aaa_radius_attributes_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.update_aaa_radius_attributes_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'calledStationId': 'string'},
        id='string',
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_aaa_radius_attributes_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_update_aaa_radius_attributes_configuration_feature_template_v1(
            validator,
            update_aaa_radius_attributes_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_aaa_radius_attributes_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.update_aaa_radius_attributes_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        id='string',
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_aaa_radius_attributes_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_update_aaa_radius_attributes_configuration_feature_template_v1(
            validator,
            update_aaa_radius_attributes_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_aaa_radius_attributes_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b086ad8ac42656aca9efc5c7c8c1e359_v3_1_3_0').validate(obj)
    return True


def delete_aaa_radius_attributes_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.delete_aaa_radius_attributes_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_aaa_radius_attributes_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_delete_aaa_radius_attributes_configuration_feature_template_v1(
            validator,
            delete_aaa_radius_attributes_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_aaa_radius_attributes_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.delete_aaa_radius_attributes_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_aaa_radius_attributes_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_delete_aaa_radius_attributes_configuration_feature_template_v1(
            validator,
            delete_aaa_radius_attributes_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_advanced_ssid_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d9c01903d0645a3d8b56172bb9549be3_v3_1_3_0').validate(obj)
    return True


def create_advanced_ssid_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.create_advanced_ssid_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'peer2peerblocking': 'string', 'passiveClient': True, 'predictionOptimization': True, 'dualBandNeighborList': True, 'radiusNacState': True, 'dhcpRequired': True, 'dhcpServer': 'string', 'flexLocalAuth': True, 'targetWakeupTime': True, 'downlinkOfdma': True, 'uplinkOfdma': True, 'downlinkMuMimo': True, 'uplinkMuMimo': True, 'dot11ax': True, 'aironetIESupport': True, 'loadBalancing': True, 'dtimPeriod5GHz': 0, 'dtimPeriod24GHz': 0, 'scanDeferTime': 0, 'maxClients': 0, 'maxClientsPerRadio': 0, 'maxClientsPerAp': 0, 'wmmPolicy': 'string', 'multicastBuffer': True, 'multicastBufferValue': 0, 'mediaStreamMulticastDirect': True, 'muMimo11ac': True, 'wifiToCellularSteering': True, 'wifiAllianceAgileMultiband': True, 'fastlaneASR': True, 'dot11vBSSMaxIdleProtected': True, 'universalAPAdmin': True, 'opportunisticKeyCaching': True, 'ipSourceGuard': True, 'dhcpOpt82RemoteIDSubOption': True, 'vlanCentralSwitching': True, 'callSnooping': True, 'sendDisassociate': True, 'sent486Busy': True, 'ipMacBinding': True, 'idleThreshold': 0, 'deferPriority0': True, 'deferPriority1': True, 'deferPriority2': True, 'deferPriority3': True, 'deferPriority4': True, 'deferPriority5': True, 'deferPriority6': True, 'deferPriority7': True, 'shareDataWithClient': True, 'advertiseSupport': True, 'advertisePCAnalyticsSupport': True, 'sendBeaconOnAssociation': True, 'sendBeaconOnRoam': True, 'fastTransitionReassociationTimeout': 0, 'mDNSMode': 'string'},
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_advanced_ssid_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_create_advanced_ssid_configuration_feature_template_v1(
            validator,
            create_advanced_ssid_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_advanced_ssid_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.create_advanced_ssid_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_advanced_ssid_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_create_advanced_ssid_configuration_feature_template_v1(
            validator,
            create_advanced_ssid_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_advanced_ssid_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_06ddfe7532bb50a0b895ec9ef15528d1_v3_1_3_0').validate(obj)
    return True


def delete_advanced_ssid_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.delete_advanced_ssid_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_advanced_ssid_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_delete_advanced_ssid_configuration_feature_template_v1(
            validator,
            delete_advanced_ssid_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_advanced_ssid_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.delete_advanced_ssid_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_advanced_ssid_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_delete_advanced_ssid_configuration_feature_template_v1(
            validator,
            delete_advanced_ssid_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_advanced_ssid_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_24914839438d5b72acb418347ec1e1fa_v3_1_3_0').validate(obj)
    return True


def update_advanced_ssid_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.update_advanced_ssid_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'peer2peerblocking': 'string', 'passiveClient': True, 'predictionOptimization': True, 'dualBandNeighborList': True, 'radiusNacState': True, 'dhcpRequired': True, 'dhcpServer': 'string', 'flexLocalAuth': True, 'targetWakeupTime': True, 'downlinkOfdma': True, 'uplinkOfdma': True, 'downlinkMuMimo': True, 'uplinkMuMimo': True, 'dot11ax': True, 'aironetIESupport': True, 'loadBalancing': True, 'dtimPeriod5GHz': 0, 'dtimPeriod24GHz': 0, 'scanDeferTime': 0, 'maxClients': 0, 'maxClientsPerRadio': 0, 'maxClientsPerAp': 0, 'wmmPolicy': 'string', 'multicastBuffer': True, 'multicastBufferValue': 0, 'mediaStreamMulticastDirect': True, 'muMimo11ac': True, 'wifiToCellularSteering': True, 'wifiAllianceAgileMultiband': True, 'fastlaneASR': True, 'dot11vBSSMaxIdleProtected': True, 'universalAPAdmin': True, 'opportunisticKeyCaching': True, 'ipSourceGuard': True, 'dhcpOpt82RemoteIDSubOption': True, 'vlanCentralSwitching': True, 'callSnooping': True, 'sendDisassociate': True, 'sent486Busy': True, 'ipMacBinding': True, 'idleThreshold': 0, 'deferPriority0': True, 'deferPriority1': True, 'deferPriority2': True, 'deferPriority3': True, 'deferPriority4': True, 'deferPriority5': True, 'deferPriority6': True, 'deferPriority7': True, 'shareDataWithClient': True, 'advertiseSupport': True, 'advertisePCAnalyticsSupport': True, 'sendBeaconOnAssociation': True, 'sendBeaconOnRoam': True, 'fastTransitionReassociationTimeout': 0, 'mDNSMode': 'string'},
        id='string',
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_advanced_ssid_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_update_advanced_ssid_configuration_feature_template_v1(
            validator,
            update_advanced_ssid_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_advanced_ssid_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.update_advanced_ssid_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        id='string',
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_advanced_ssid_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_update_advanced_ssid_configuration_feature_template_v1(
            validator,
            update_advanced_ssid_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_advanced_ssid_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_af6a62d6be8f53149d942c35f2b2aef0_v3_1_3_0').validate(obj)
    return True


def get_advanced_ssid_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.get_advanced_ssid_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_advanced_ssid_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_get_advanced_ssid_configuration_feature_template_v1(
            validator,
            get_advanced_ssid_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_advanced_ssid_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.get_advanced_ssid_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_advanced_ssid_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_get_advanced_ssid_configuration_feature_template_v1(
            validator,
            get_advanced_ssid_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_clean_air_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7e8911ba7a8b54be8e443df8ac842e36_v3_1_3_0').validate(obj)
    return True


def create_clean_air_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.create_clean_air_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'radioBand': 'string', 'cleanAir': True, 'cleanAirDeviceReporting': True, 'persistentDevicePropagation': True, 'description': 'string', 'interferersFeatures': {'bleBeacon': True, 'bluetoothPagingInquiry': True, 'bluetoothScoAcl': True, 'continuousTransmitter': True, 'genericDect': True, 'genericTdd': True, 'jammer': True, 'microwaveOven': True, 'motorolaCanopy': True, 'siFhss': True, 'spectrum80211Fh': True, 'spectrum80211NonStandardChannel': True, 'spectrum802154': True, 'spectrumInverted': True, 'superAg': True, 'videoCamera': True, 'wimaxFixed': True, 'wimaxMobile': True, 'xbox': True}},
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_clean_air_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_create_clean_air_configuration_feature_template_v1(
            validator,
            create_clean_air_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_clean_air_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.create_clean_air_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_clean_air_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_create_clean_air_configuration_feature_template_v1(
            validator,
            create_clean_air_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_clean_air_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f336f907fce45b8dbd74dfdf9f434bab_v3_1_3_0').validate(obj)
    return True


def delete_clean_air_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.delete_clean_air_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_clean_air_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_delete_clean_air_configuration_feature_template_v1(
            validator,
            delete_clean_air_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_clean_air_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.delete_clean_air_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_clean_air_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_delete_clean_air_configuration_feature_template_v1(
            validator,
            delete_clean_air_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_clean_air_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f15aaad792fc57fd89c880afc3b84dc4_v3_1_3_0').validate(obj)
    return True


def update_clean_air_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.update_clean_air_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'radioBand': 'string', 'cleanAir': True, 'cleanAirDeviceReporting': True, 'persistentDevicePropagation': True, 'description': 'string', 'interferersFeatures': {'bleBeacon': True, 'bluetoothPagingInquiry': True, 'bluetoothScoAcl': True, 'continuousTransmitter': True, 'genericDect': True, 'genericTdd': True, 'jammer': True, 'microwaveOven': True, 'motorolaCanopy': True, 'siFhss': True, 'spectrum80211Fh': True, 'spectrum80211NonStandardChannel': True, 'spectrum802154': True, 'spectrumInverted': True, 'superAg': True, 'videoCamera': True, 'wimaxFixed': True, 'wimaxMobile': True, 'xbox': True}},
        id='string',
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_clean_air_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_update_clean_air_configuration_feature_template_v1(
            validator,
            update_clean_air_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_clean_air_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.update_clean_air_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        id='string',
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_clean_air_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_update_clean_air_configuration_feature_template_v1(
            validator,
            update_clean_air_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_clean_air_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_90372bb41ef855e290e52b8db9cd0c43_v3_1_3_0').validate(obj)
    return True


def get_clean_air_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.get_clean_air_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_clean_air_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_get_clean_air_configuration_feature_template_v1(
            validator,
            get_clean_air_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_clean_air_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.get_clean_air_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_clean_air_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_get_clean_air_configuration_feature_template_v1(
            validator,
            get_clean_air_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_dot11ax_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ad487b01cede5cb4bdd5ee06695a6020_v3_1_3_0').validate(obj)
    return True


def create_dot11ax_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.create_dot11ax_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'radioBand': 'string', 'bssColor': True, 'targetWaketimeBroadcast': True, 'nonSRGObssPdMaxThreshold': 0, 'multipleBssid': True, 'targetWakeUpTime11ax': True, 'obssPd': True},
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_dot11ax_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_create_dot11ax_configuration_feature_template_v1(
            validator,
            create_dot11ax_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_dot11ax_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.create_dot11ax_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_dot11ax_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_create_dot11ax_configuration_feature_template_v1(
            validator,
            create_dot11ax_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_dot11ax_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_012ca4bbb8be5316a1c97bb12137145c_v3_1_3_0').validate(obj)
    return True


def get_dot11ax_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.get_dot11ax_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_dot11ax_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_get_dot11ax_configuration_feature_template_v1(
            validator,
            get_dot11ax_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_dot11ax_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.get_dot11ax_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_dot11ax_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_get_dot11ax_configuration_feature_template_v1(
            validator,
            get_dot11ax_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_dot11ax_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9dcbc4139ae25e7987213d7fc176663f_v3_1_3_0').validate(obj)
    return True


def delete_dot11ax_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.delete_dot11ax_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_dot11ax_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_delete_dot11ax_configuration_feature_template_v1(
            validator,
            delete_dot11ax_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_dot11ax_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.delete_dot11ax_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_dot11ax_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_delete_dot11ax_configuration_feature_template_v1(
            validator,
            delete_dot11ax_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_dot11ax_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1bfab2e1d87654afb88c77fcfae4e407_v3_1_3_0').validate(obj)
    return True


def update_dot11ax_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.update_dot11ax_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'radioBand': 'string', 'bssColor': True, 'targetWaketimeBroadcast': True, 'nonSRGObssPdMaxThreshold': 0, 'multipleBssid': True, 'targetWakeUpTime11ax': True, 'obssPd': True},
        id='string',
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_dot11ax_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_update_dot11ax_configuration_feature_template_v1(
            validator,
            update_dot11ax_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_dot11ax_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.update_dot11ax_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        id='string',
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_dot11ax_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_update_dot11ax_configuration_feature_template_v1(
            validator,
            update_dot11ax_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_dot11be_status_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a2da4c1e5224542e8474f09eb8d4f32d_v3_1_3_0').validate(obj)
    return True


def create_dot11be_status_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.create_dot11be_status_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'dot11beStatus': True, 'radioBand': 'string'},
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_dot11be_status_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_create_dot11be_status_configuration_feature_template_v1(
            validator,
            create_dot11be_status_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_dot11be_status_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.create_dot11be_status_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_dot11be_status_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_create_dot11be_status_configuration_feature_template_v1(
            validator,
            create_dot11be_status_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_dot11be_status_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_346fe6fe86175ce7bf566b642f7f3da0_v3_1_3_0').validate(obj)
    return True


def delete_dot11be_status_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.delete_dot11be_status_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_dot11be_status_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_delete_dot11be_status_configuration_feature_template_v1(
            validator,
            delete_dot11be_status_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_dot11be_status_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.delete_dot11be_status_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_dot11be_status_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_delete_dot11be_status_configuration_feature_template_v1(
            validator,
            delete_dot11be_status_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_dot11be_status_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4760dfe3872e591f9f3e2a0daa358c1a_v3_1_3_0').validate(obj)
    return True


def update_dot11be_status_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.update_dot11be_status_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'dot11beStatus': True, 'radioBand': 'string'},
        id='string',
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_dot11be_status_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_update_dot11be_status_configuration_feature_template_v1(
            validator,
            update_dot11be_status_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_dot11be_status_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.update_dot11be_status_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        id='string',
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_dot11be_status_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_update_dot11be_status_configuration_feature_template_v1(
            validator,
            update_dot11be_status_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_dot11be_status_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0fb048f95b0f56209a901f6523f10c08_v3_1_3_0').validate(obj)
    return True


def get_dot11be_status_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.get_dot11be_status_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_dot11be_status_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_get_dot11be_status_configuration_feature_template_v1(
            validator,
            get_dot11be_status_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_dot11be_status_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.get_dot11be_status_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_dot11be_status_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_get_dot11be_status_configuration_feature_template_v1(
            validator,
            get_dot11be_status_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_event_driven_r_r_m_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_37e70de44247549f9e49cfa5c6b24de9_v3_1_3_0').validate(obj)
    return True


def create_event_driven_r_r_m_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.create_event_driven_r_r_m_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'radioBand': 'string', 'eventDrivenRrmEnable': True, 'eventDrivenRrmThresholdLevel': 'string', 'eventDrivenRrmCustomThresholdVal': 0},
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_event_driven_r_r_m_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_create_event_driven_r_r_m_configuration_feature_template_v1(
            validator,
            create_event_driven_r_r_m_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_event_driven_r_r_m_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.create_event_driven_r_r_m_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_event_driven_r_r_m_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_create_event_driven_r_r_m_configuration_feature_template_v1(
            validator,
            create_event_driven_r_r_m_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_event_driven_r_r_m_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e6e53e9b17d750009dcbccf6c7731b37_v3_1_3_0').validate(obj)
    return True


def delete_event_driven_r_r_m_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.delete_event_driven_r_r_m_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_event_driven_r_r_m_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_delete_event_driven_r_r_m_configuration_feature_template_v1(
            validator,
            delete_event_driven_r_r_m_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_event_driven_r_r_m_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.delete_event_driven_r_r_m_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_event_driven_r_r_m_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_delete_event_driven_r_r_m_configuration_feature_template_v1(
            validator,
            delete_event_driven_r_r_m_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_event_driven_r_r_m_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_609b1b44ebaa5561a75adcc520b42521_v3_1_3_0').validate(obj)
    return True


def get_event_driven_r_r_m_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.get_event_driven_r_r_m_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_event_driven_r_r_m_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_get_event_driven_r_r_m_configuration_feature_template_v1(
            validator,
            get_event_driven_r_r_m_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_event_driven_r_r_m_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.get_event_driven_r_r_m_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_event_driven_r_r_m_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_get_event_driven_r_r_m_configuration_feature_template_v1(
            validator,
            get_event_driven_r_r_m_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_event_driven_r_r_m_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0b9fbd53af6a5b46b34b17e601680801_v3_1_3_0').validate(obj)
    return True


def update_event_driven_r_r_m_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.update_event_driven_r_r_m_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'radioBand': 'string', 'eventDrivenRrmEnable': True, 'eventDrivenRrmThresholdLevel': 'string', 'eventDrivenRrmCustomThresholdVal': 0},
        id='string',
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_event_driven_r_r_m_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_update_event_driven_r_r_m_configuration_feature_template_v1(
            validator,
            update_event_driven_r_r_m_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_event_driven_r_r_m_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.update_event_driven_r_r_m_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        id='string',
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_event_driven_r_r_m_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_update_event_driven_r_r_m_configuration_feature_template_v1(
            validator,
            update_event_driven_r_r_m_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_flex_connect_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c880bc6a8faa5bb4afbfd6bea38c75fa_v3_1_3_0').validate(obj)
    return True


def create_flex_connect_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.create_flex_connect_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'overlapIpEnable': True},
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_flex_connect_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_create_flex_connect_configuration_feature_template_v1(
            validator,
            create_flex_connect_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_flex_connect_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.create_flex_connect_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_flex_connect_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_create_flex_connect_configuration_feature_template_v1(
            validator,
            create_flex_connect_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_flex_connect_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6ed96d98063c5be9aa0005772dc95fc5_v3_1_3_0').validate(obj)
    return True


def update_flex_connect_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.update_flex_connect_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'overlapIpEnable': True},
        id='string',
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_flex_connect_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_update_flex_connect_configuration_feature_template_v1(
            validator,
            update_flex_connect_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_flex_connect_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.update_flex_connect_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        id='string',
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_flex_connect_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_update_flex_connect_configuration_feature_template_v1(
            validator,
            update_flex_connect_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_flex_connect_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a62d88a29ff654199b64e33a44e4090b_v3_1_3_0').validate(obj)
    return True


def delete_flex_connect_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.delete_flex_connect_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_flex_connect_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_delete_flex_connect_configuration_feature_template_v1(
            validator,
            delete_flex_connect_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_flex_connect_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.delete_flex_connect_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_flex_connect_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_delete_flex_connect_configuration_feature_template_v1(
            validator,
            delete_flex_connect_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_flex_connect_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0917b4c5c0515fd2982f094ed79afad4_v3_1_3_0').validate(obj)
    return True


def get_flex_connect_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.get_flex_connect_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_flex_connect_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_get_flex_connect_configuration_feature_template_v1(
            validator,
            get_flex_connect_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_flex_connect_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.get_flex_connect_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_flex_connect_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_get_flex_connect_configuration_feature_template_v1(
            validator,
            get_flex_connect_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_multicast_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d6451662bd1652e7bdc39053429e87a4_v3_1_3_0').validate(obj)
    return True


def create_multicast_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.create_multicast_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'globalMulticastEnabled': True, 'multicastIpv4Mode': 'string', 'multicastIpv4Address': 'string', 'multicastIpv6Mode': 'string', 'multicastIpv6Address': 'string'},
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_multicast_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_create_multicast_configuration_feature_template_v1(
            validator,
            create_multicast_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_multicast_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.create_multicast_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_multicast_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_create_multicast_configuration_feature_template_v1(
            validator,
            create_multicast_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_multicast_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a4c2d99220755fa2b3be2d16e8dac41d_v3_1_3_0').validate(obj)
    return True


def get_multicast_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.get_multicast_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_multicast_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_get_multicast_configuration_feature_template_v1(
            validator,
            get_multicast_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_multicast_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.get_multicast_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_multicast_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_get_multicast_configuration_feature_template_v1(
            validator,
            get_multicast_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_multicast_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_de576e409f555b209e2bd0d56adef888_v3_1_3_0').validate(obj)
    return True


def delete_multicast_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.delete_multicast_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_multicast_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_delete_multicast_configuration_feature_template_v1(
            validator,
            delete_multicast_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_multicast_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.delete_multicast_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_multicast_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_delete_multicast_configuration_feature_template_v1(
            validator,
            delete_multicast_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_multicast_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_de24de1222a4500cab78b4b34ee299f2_v3_1_3_0').validate(obj)
    return True


def update_multicast_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.update_multicast_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'globalMulticastEnabled': True, 'multicastIpv4Mode': 'string', 'multicastIpv4Address': 'string', 'multicastIpv6Mode': 'string', 'multicastIpv6Address': 'string'},
        id='string',
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_multicast_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_update_multicast_configuration_feature_template_v1(
            validator,
            update_multicast_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_multicast_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.update_multicast_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        id='string',
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_multicast_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_update_multicast_configuration_feature_template_v1(
            validator,
            update_multicast_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_r_r_m_f_r_a_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_66967a25f176554fb407fbe4952f1c4e_v3_1_3_0').validate(obj)
    return True


def create_r_r_m_f_r_a_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.create_r_r_m_f_r_a_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'radioBand': 'string', 'fraFreeze': True, 'fraStatus': True, 'fraInterval': 0, 'fraSensitivity': 'string'},
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_r_r_m_f_r_a_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_create_r_r_m_f_r_a_configuration_feature_template_v1(
            validator,
            create_r_r_m_f_r_a_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_r_r_m_f_r_a_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.create_r_r_m_f_r_a_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_r_r_m_f_r_a_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_create_r_r_m_f_r_a_configuration_feature_template_v1(
            validator,
            create_r_r_m_f_r_a_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_r_r_m_f_r_a_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d56aecb1a1a859d48326e29777afa004_v3_1_3_0').validate(obj)
    return True


def get_r_r_m_f_r_a_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.get_r_r_m_f_r_a_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_r_r_m_f_r_a_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_get_r_r_m_f_r_a_configuration_feature_template_v1(
            validator,
            get_r_r_m_f_r_a_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_r_r_m_f_r_a_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.get_r_r_m_f_r_a_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_r_r_m_f_r_a_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_get_r_r_m_f_r_a_configuration_feature_template_v1(
            validator,
            get_r_r_m_f_r_a_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_r_r_m_f_r_a_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4f829d3e99565937b9d12c873f8faa46_v3_1_3_0').validate(obj)
    return True


def update_r_r_m_f_r_a_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.update_r_r_m_f_r_a_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'radioBand': 'string', 'fraFreeze': True, 'fraStatus': True, 'fraInterval': 0, 'fraSensitivity': 'string'},
        id='string',
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_r_r_m_f_r_a_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_update_r_r_m_f_r_a_configuration_feature_template_v1(
            validator,
            update_r_r_m_f_r_a_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_r_r_m_f_r_a_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.update_r_r_m_f_r_a_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        id='string',
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_r_r_m_f_r_a_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_update_r_r_m_f_r_a_configuration_feature_template_v1(
            validator,
            update_r_r_m_f_r_a_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_r_r_m_f_r_a_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_763373b5fab4517d89246d68c8701bf9_v3_1_3_0').validate(obj)
    return True


def delete_r_r_m_f_r_a_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.delete_r_r_m_f_r_a_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_r_r_m_f_r_a_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_delete_r_r_m_f_r_a_configuration_feature_template_v1(
            validator,
            delete_r_r_m_f_r_a_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_r_r_m_f_r_a_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.delete_r_r_m_f_r_a_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_r_r_m_f_r_a_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_delete_r_r_m_f_r_a_configuration_feature_template_v1(
            validator,
            delete_r_r_m_f_r_a_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_r_r_m_general_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0942717fe8fb526f9b3b8f3c7aaeebac_v3_1_3_0').validate(obj)
    return True


def create_r_r_m_general_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.create_r_r_m_general_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'radioBand': 'string', 'monitoringChannels': 'string', 'neighborDiscoverType': 'string', 'throughputThreshold': 0, 'coverageHoleDetection': True},
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_r_r_m_general_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_create_r_r_m_general_configuration_feature_template_v1(
            validator,
            create_r_r_m_general_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_r_r_m_general_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.create_r_r_m_general_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_r_r_m_general_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_create_r_r_m_general_configuration_feature_template_v1(
            validator,
            create_r_r_m_general_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_r_r_m_general_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_243e5192c5b056df856988b95c2fa275_v3_1_3_0').validate(obj)
    return True


def delete_r_r_m_general_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.delete_r_r_m_general_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_r_r_m_general_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_delete_r_r_m_general_configuration_feature_template_v1(
            validator,
            delete_r_r_m_general_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_r_r_m_general_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.delete_r_r_m_general_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_r_r_m_general_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_delete_r_r_m_general_configuration_feature_template_v1(
            validator,
            delete_r_r_m_general_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_r_r_m_general_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d73fc407278f5eefa67e6a014aeaf742_v3_1_3_0').validate(obj)
    return True


def update_r_r_m_general_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.update_r_r_m_general_configuration_feature_template_v1(
        active_validation=True,
        designName='string',
        featureAttributes={'radioBand': 'string', 'monitoringChannels': 'string', 'neighborDiscoverType': 'string', 'throughputThreshold': 0, 'coverageHoleDetection': True},
        id='string',
        payload=None,
        unlockedAttributes=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_r_r_m_general_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_update_r_r_m_general_configuration_feature_template_v1(
            validator,
            update_r_r_m_general_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_r_r_m_general_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.update_r_r_m_general_configuration_feature_template_v1(
        active_validation=True,
        designName=None,
        featureAttributes=None,
        id='string',
        payload=None,
        unlockedAttributes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_r_r_m_general_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_update_r_r_m_general_configuration_feature_template_v1(
            validator,
            update_r_r_m_general_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_r_r_m_general_configuration_feature_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_84baee7f66985144a20dfd7d40d0e074_v3_1_3_0').validate(obj)
    return True


def get_r_r_m_general_configuration_feature_template_v1(api):
    endpoint_result = api.wireless.get_r_r_m_general_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_r_r_m_general_configuration_feature_template_v1(api, validator):
    try:
        assert is_valid_get_r_r_m_general_configuration_feature_template_v1(
            validator,
            get_r_r_m_general_configuration_feature_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_r_r_m_general_configuration_feature_template_v1_default_val(api):
    endpoint_result = api.wireless.get_r_r_m_general_configuration_feature_template_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_r_r_m_general_configuration_feature_template_v1_default_val(api, validator):
    try:
        assert is_valid_get_r_r_m_general_configuration_feature_template_v1(
            validator,
            get_r_r_m_general_configuration_feature_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_feature_template_summary_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f8ab85968766525783f3fe1a529392b3_v3_1_3_0').validate(obj)
    return True


def get_feature_template_summary_v1(api):
    endpoint_result = api.wireless.get_feature_template_summary_v1(
        design_name='string',
        limit=0,
        offset=0,
        system_template=True,
        type='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_feature_template_summary_v1(api, validator):
    try:
        assert is_valid_get_feature_template_summary_v1(
            validator,
            get_feature_template_summary_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_feature_template_summary_v1_default_val(api):
    endpoint_result = api.wireless.get_feature_template_summary_v1(
        design_name=None,
        limit=None,
        offset=None,
        system_template=None,
        type=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_feature_template_summary_v1_default_val(api, validator):
    try:
        assert is_valid_get_feature_template_summary_v1(
            validator,
            get_feature_template_summary_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_aaa_override_vlan_settings_by_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_34bb5bd77c415e9982e01c07a6b1f165_v3_1_3_0').validate(obj)
    return True


def delete_aaa_override_vlan_settings_by_site_v1(api):
    endpoint_result = api.wireless.delete_aaa_override_vlan_settings_by_site_v1(
        remove_override_in_hierarchy=True,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_aaa_override_vlan_settings_by_site_v1(api, validator):
    try:
        assert is_valid_delete_aaa_override_vlan_settings_by_site_v1(
            validator,
            delete_aaa_override_vlan_settings_by_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_aaa_override_vlan_settings_by_site_v1_default_val(api):
    endpoint_result = api.wireless.delete_aaa_override_vlan_settings_by_site_v1(
        remove_override_in_hierarchy=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_aaa_override_vlan_settings_by_site_v1_default_val(api, validator):
    try:
        assert is_valid_delete_aaa_override_vlan_settings_by_site_v1(
            validator,
            delete_aaa_override_vlan_settings_by_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_aaa_override_vlan_settings_by_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3c3ad5ef56595f45b59c8df890955e02_v3_1_3_0').validate(obj)
    return True


def get_aaa_override_vlan_settings_by_site_v1(api):
    endpoint_result = api.wireless.get_aaa_override_vlan_settings_by_site_v1(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_aaa_override_vlan_settings_by_site_v1(api, validator):
    try:
        assert is_valid_get_aaa_override_vlan_settings_by_site_v1(
            validator,
            get_aaa_override_vlan_settings_by_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_aaa_override_vlan_settings_by_site_v1_default_val(api):
    endpoint_result = api.wireless.get_aaa_override_vlan_settings_by_site_v1(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_aaa_override_vlan_settings_by_site_v1_default_val(api, validator):
    try:
        assert is_valid_get_aaa_override_vlan_settings_by_site_v1(
            validator,
            get_aaa_override_vlan_settings_by_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_aaa_override_vlan_settings_by_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0a41ac8d894e5ee98fc9324fb8488174_v3_1_3_0').validate(obj)
    return True


def update_aaa_override_vlan_settings_by_site_v1(api):
    endpoint_result = api.wireless.update_aaa_override_vlan_settings_by_site_v1(
        active_validation=True,
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_aaa_override_vlan_settings_by_site_v1(api, validator):
    try:
        assert is_valid_update_aaa_override_vlan_settings_by_site_v1(
            validator,
            update_aaa_override_vlan_settings_by_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_aaa_override_vlan_settings_by_site_v1_default_val(api):
    endpoint_result = api.wireless.update_aaa_override_vlan_settings_by_site_v1(
        active_validation=True,
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_aaa_override_vlan_settings_by_site_v1_default_val(api, validator):
    try:
        assert is_valid_update_aaa_override_vlan_settings_by_site_v1(
            validator,
            update_aaa_override_vlan_settings_by_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_native_vlan_settings_by_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_da24bdb30635515395471fe644cdc7b5_v3_1_3_0').validate(obj)
    return True


def update_native_vlan_settings_by_site_v1(api):
    endpoint_result = api.wireless.update_native_vlan_settings_by_site_v1(
        active_validation=True,
        nativeVlanId=0,
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_native_vlan_settings_by_site_v1(api, validator):
    try:
        assert is_valid_update_native_vlan_settings_by_site_v1(
            validator,
            update_native_vlan_settings_by_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_native_vlan_settings_by_site_v1_default_val(api):
    endpoint_result = api.wireless.update_native_vlan_settings_by_site_v1(
        active_validation=True,
        nativeVlanId=None,
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_native_vlan_settings_by_site_v1_default_val(api, validator):
    try:
        assert is_valid_update_native_vlan_settings_by_site_v1(
            validator,
            update_native_vlan_settings_by_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_native_vlan_settings_by_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2456d113be505795a139cbffc189fcd6_v3_1_3_0').validate(obj)
    return True


def delete_native_vlan_settings_by_site_v1(api):
    endpoint_result = api.wireless.delete_native_vlan_settings_by_site_v1(
        remove_override_in_hierarchy=True,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_native_vlan_settings_by_site_v1(api, validator):
    try:
        assert is_valid_delete_native_vlan_settings_by_site_v1(
            validator,
            delete_native_vlan_settings_by_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_native_vlan_settings_by_site_v1_default_val(api):
    endpoint_result = api.wireless.delete_native_vlan_settings_by_site_v1(
        remove_override_in_hierarchy=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_native_vlan_settings_by_site_v1_default_val(api, validator):
    try:
        assert is_valid_delete_native_vlan_settings_by_site_v1(
            validator,
            delete_native_vlan_settings_by_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_native_vlan_settings_by_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8392035a13f951d58006466042473c73_v3_1_3_0').validate(obj)
    return True


def get_native_vlan_settings_by_site_v1(api):
    endpoint_result = api.wireless.get_native_vlan_settings_by_site_v1(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_native_vlan_settings_by_site_v1(api, validator):
    try:
        assert is_valid_get_native_vlan_settings_by_site_v1(
            validator,
            get_native_vlan_settings_by_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_native_vlan_settings_by_site_v1_default_val(api):
    endpoint_result = api.wireless.get_native_vlan_settings_by_site_v1(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_native_vlan_settings_by_site_v1_default_val(api, validator):
    try:
        assert is_valid_get_native_vlan_settings_by_site_v1(
            validator,
            get_native_vlan_settings_by_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_ssid_v1(json_schema_validate, obj):
    json_schema_validate('jsd_aa663ca2bd1f5a3db67c405987495112_v3_1_3_0').validate(obj)
    return True


def create_ssid_v1(api):
    endpoint_result = api.wireless.create_ssid_v1(
        aaaOverride=True,
        acctServers=['string'],
        aclName='string',
        active_validation=True,
        authServer='string',
        authServers=['string'],
        authType='string',
        basicServiceSetClientIdleTimeout=0,
        basicServiceSetMaxIdleEnable=True,
        cckmTsfTolerance=0,
        clientExclusionEnable=True,
        clientExclusionTimeout=0,
        clientRateLimit=0,
        coverageHoleDetectionEnable=True,
        directedMulticastServiceEnable=True,
        egressQos='string',
        externalAuthIpAddress='string',
        fastTransition='string',
        fastTransitionOverTheDistributedSystemEnable=True,
        ghz24Policy='string',
        ghz6PolicyClientSteering=True,
        ingressQos='string',
        isApBeaconProtectionEnabled=True,
        isAuthKey8021x=True,
        isAuthKey8021xPlusFT=True,
        isAuthKey8021x_SHA256=True,
        isAuthKeyEasyPSK=True,
        isAuthKeyOWE=True,
        isAuthKeyPSK=True,
        isAuthKeyPSKPlusFT=True,
        isAuthKeyPSKSHA256=True,
        isAuthKeySae=True,
        isAuthKeySaeExt=True,
        isAuthKeySaeExtPlusFT=True,
        isAuthKeySaePlusFT=True,
        isAuthKeySuiteB1921x=True,
        isAuthKeySuiteB1x=True,
        isBroadcastSSID=True,
        isCckmEnabled=True,
        isEnabled=True,
        isFastLaneEnabled=True,
        isHex=True,
        isMacFilteringEnabled=True,
        isPosturingEnabled=True,
        isRadiusProfilingEnabled=True,
        isRandomMacFilterEnabled=True,
        l3AuthType='string',
        managementFrameProtectionClientprotection='string',
        multiPSKSettings=[{'priority': 0, 'passphraseType': 'string', 'passphrase': 'string'}],
        nasOptions=['string'],
        neighborListEnable=True,
        openSsid='string',
        passphrase='string',
        payload=None,
        policyProfileName='string',
        profileName='string',
        protectedManagementFrame='string',
        rsnCipherSuiteCcmp128=True,
        rsnCipherSuiteCcmp256=True,
        rsnCipherSuiteGcmp128=True,
        rsnCipherSuiteGcmp256=True,
        sessionTimeOut=0,
        sessionTimeOutEnable=True,
        site_id='string',
        sleepingClientEnable=True,
        sleepingClientTimeout=0,
        ssid='string',
        ssidRadioType='string',
        webPassthrough=True,
        wlanBandSelectEnable=True,
        wlanType='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_ssid_v1(api, validator):
    try:
        assert is_valid_create_ssid_v1(
            validator,
            create_ssid_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_ssid_v1_default_val(api):
    endpoint_result = api.wireless.create_ssid_v1(
        aaaOverride=None,
        acctServers=None,
        aclName=None,
        active_validation=True,
        authServer=None,
        authServers=None,
        authType=None,
        basicServiceSetClientIdleTimeout=None,
        basicServiceSetMaxIdleEnable=None,
        cckmTsfTolerance=None,
        clientExclusionEnable=None,
        clientExclusionTimeout=None,
        clientRateLimit=None,
        coverageHoleDetectionEnable=None,
        directedMulticastServiceEnable=None,
        egressQos=None,
        externalAuthIpAddress=None,
        fastTransition=None,
        fastTransitionOverTheDistributedSystemEnable=None,
        ghz24Policy=None,
        ghz6PolicyClientSteering=None,
        ingressQos=None,
        isApBeaconProtectionEnabled=None,
        isAuthKey8021x=None,
        isAuthKey8021xPlusFT=None,
        isAuthKey8021x_SHA256=None,
        isAuthKeyEasyPSK=None,
        isAuthKeyOWE=None,
        isAuthKeyPSK=None,
        isAuthKeyPSKPlusFT=None,
        isAuthKeyPSKSHA256=None,
        isAuthKeySae=None,
        isAuthKeySaeExt=None,
        isAuthKeySaeExtPlusFT=None,
        isAuthKeySaePlusFT=None,
        isAuthKeySuiteB1921x=None,
        isAuthKeySuiteB1x=None,
        isBroadcastSSID=None,
        isCckmEnabled=None,
        isEnabled=None,
        isFastLaneEnabled=None,
        isHex=None,
        isMacFilteringEnabled=None,
        isPosturingEnabled=None,
        isRadiusProfilingEnabled=None,
        isRandomMacFilterEnabled=None,
        l3AuthType=None,
        managementFrameProtectionClientprotection=None,
        multiPSKSettings=None,
        nasOptions=None,
        neighborListEnable=None,
        openSsid=None,
        passphrase=None,
        payload=None,
        policyProfileName=None,
        profileName=None,
        protectedManagementFrame=None,
        rsnCipherSuiteCcmp128=None,
        rsnCipherSuiteCcmp256=None,
        rsnCipherSuiteGcmp128=None,
        rsnCipherSuiteGcmp256=None,
        sessionTimeOut=None,
        sessionTimeOutEnable=None,
        site_id='string',
        sleepingClientEnable=None,
        sleepingClientTimeout=None,
        ssid=None,
        ssidRadioType=None,
        webPassthrough=None,
        wlanBandSelectEnable=None,
        wlanType=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_ssid_v1_default_val(api, validator):
    try:
        assert is_valid_create_ssid_v1(
            validator,
            create_ssid_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ssid_by_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ae5ed21186c55f9c8485a57cebf85562_v3_1_3_0').validate(obj)
    return True


def get_ssid_by_site_v1(api):
    endpoint_result = api.wireless.get_ssid_by_site_v1(
        auth_type='string',
        l3auth_type='string',
        limit=0,
        offset=0,
        site_id='string',
        ssid='string',
        wlan_type='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ssid_by_site_v1(api, validator):
    try:
        assert is_valid_get_ssid_by_site_v1(
            validator,
            get_ssid_by_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ssid_by_site_v1_default_val(api):
    endpoint_result = api.wireless.get_ssid_by_site_v1(
        auth_type=None,
        l3auth_type=None,
        limit=None,
        offset=None,
        site_id='string',
        ssid=None,
        wlan_type=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ssid_by_site_v1_default_val(api, validator):
    try:
        assert is_valid_get_ssid_by_site_v1(
            validator,
            get_ssid_by_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ssid_count_by_site_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1850de3663dc582ebcd90a67635ae18a_v3_1_3_0').validate(obj)
    return True


def get_ssid_count_by_site_v1(api):
    endpoint_result = api.wireless.get_ssid_count_by_site_v1(
        inherited=True,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ssid_count_by_site_v1(api, validator):
    try:
        assert is_valid_get_ssid_count_by_site_v1(
            validator,
            get_ssid_count_by_site_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ssid_count_by_site_v1_default_val(api):
    endpoint_result = api.wireless.get_ssid_count_by_site_v1(
        inherited=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ssid_count_by_site_v1_default_val(api, validator):
    try:
        assert is_valid_get_ssid_count_by_site_v1(
            validator,
            get_ssid_count_by_site_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ssid_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_64c300d8fe965b278388c9aeca543053_v3_1_3_0').validate(obj)
    return True


def get_ssid_by_id_v1(api):
    endpoint_result = api.wireless.get_ssid_by_id_v1(
        id='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ssid_by_id_v1(api, validator):
    try:
        assert is_valid_get_ssid_by_id_v1(
            validator,
            get_ssid_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ssid_by_id_v1_default_val(api):
    endpoint_result = api.wireless.get_ssid_by_id_v1(
        id='string',
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ssid_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_ssid_by_id_v1(
            validator,
            get_ssid_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_ssid_v1(json_schema_validate, obj):
    json_schema_validate('jsd_497a602eee5a56faa64436bade8a240e_v3_1_3_0').validate(obj)
    return True


def update_ssid_v1(api):
    endpoint_result = api.wireless.update_ssid_v1(
        aaaOverride=True,
        acctServers=['string'],
        aclName='string',
        active_validation=True,
        authServer='string',
        authServers=['string'],
        authType='string',
        basicServiceSetClientIdleTimeout=0,
        basicServiceSetMaxIdleEnable=True,
        cckmTsfTolerance=0,
        clientExclusionEnable=True,
        clientExclusionTimeout=0,
        clientRateLimit=0,
        coverageHoleDetectionEnable=True,
        directedMulticastServiceEnable=True,
        egressQos='string',
        externalAuthIpAddress='string',
        fastTransition='string',
        fastTransitionOverTheDistributedSystemEnable=True,
        ghz24Policy='string',
        ghz6PolicyClientSteering=True,
        id='string',
        ingressQos='string',
        isApBeaconProtectionEnabled=True,
        isAuthKey8021x=True,
        isAuthKey8021xPlusFT=True,
        isAuthKey8021x_SHA256=True,
        isAuthKeyEasyPSK=True,
        isAuthKeyOWE=True,
        isAuthKeyPSK=True,
        isAuthKeyPSKPlusFT=True,
        isAuthKeyPSKSHA256=True,
        isAuthKeySae=True,
        isAuthKeySaeExt=True,
        isAuthKeySaeExtPlusFT=True,
        isAuthKeySaePlusFT=True,
        isAuthKeySuiteB1921x=True,
        isAuthKeySuiteB1x=True,
        isBroadcastSSID=True,
        isCckmEnabled=True,
        isEnabled=True,
        isFastLaneEnabled=True,
        isHex=True,
        isMacFilteringEnabled=True,
        isPosturingEnabled=True,
        isRadiusProfilingEnabled=True,
        isRandomMacFilterEnabled=True,
        l3AuthType='string',
        managementFrameProtectionClientprotection='string',
        multiPSKSettings=[{'priority': 0, 'passphraseType': 'string', 'passphrase': 'string'}],
        nasOptions=['string'],
        neighborListEnable=True,
        openSsid='string',
        passphrase='string',
        payload=None,
        policyProfileName='string',
        profileName='string',
        protectedManagementFrame='string',
        rsnCipherSuiteCcmp128=True,
        rsnCipherSuiteCcmp256=True,
        rsnCipherSuiteGcmp128=True,
        rsnCipherSuiteGcmp256=True,
        sessionTimeOut=0,
        sessionTimeOutEnable=True,
        site_id='string',
        sleepingClientEnable=True,
        sleepingClientTimeout=0,
        ssid='string',
        ssidRadioType='string',
        webPassthrough=True,
        wlanBandSelectEnable=True,
        wlanType='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_ssid_v1(api, validator):
    try:
        assert is_valid_update_ssid_v1(
            validator,
            update_ssid_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_ssid_v1_default_val(api):
    endpoint_result = api.wireless.update_ssid_v1(
        aaaOverride=None,
        acctServers=None,
        aclName=None,
        active_validation=True,
        authServer=None,
        authServers=None,
        authType=None,
        basicServiceSetClientIdleTimeout=None,
        basicServiceSetMaxIdleEnable=None,
        cckmTsfTolerance=None,
        clientExclusionEnable=None,
        clientExclusionTimeout=None,
        clientRateLimit=None,
        coverageHoleDetectionEnable=None,
        directedMulticastServiceEnable=None,
        egressQos=None,
        externalAuthIpAddress=None,
        fastTransition=None,
        fastTransitionOverTheDistributedSystemEnable=None,
        ghz24Policy=None,
        ghz6PolicyClientSteering=None,
        id='string',
        ingressQos=None,
        isApBeaconProtectionEnabled=None,
        isAuthKey8021x=None,
        isAuthKey8021xPlusFT=None,
        isAuthKey8021x_SHA256=None,
        isAuthKeyEasyPSK=None,
        isAuthKeyOWE=None,
        isAuthKeyPSK=None,
        isAuthKeyPSKPlusFT=None,
        isAuthKeyPSKSHA256=None,
        isAuthKeySae=None,
        isAuthKeySaeExt=None,
        isAuthKeySaeExtPlusFT=None,
        isAuthKeySaePlusFT=None,
        isAuthKeySuiteB1921x=None,
        isAuthKeySuiteB1x=None,
        isBroadcastSSID=None,
        isCckmEnabled=None,
        isEnabled=None,
        isFastLaneEnabled=None,
        isHex=None,
        isMacFilteringEnabled=None,
        isPosturingEnabled=None,
        isRadiusProfilingEnabled=None,
        isRandomMacFilterEnabled=None,
        l3AuthType=None,
        managementFrameProtectionClientprotection=None,
        multiPSKSettings=None,
        nasOptions=None,
        neighborListEnable=None,
        openSsid=None,
        passphrase=None,
        payload=None,
        policyProfileName=None,
        profileName=None,
        protectedManagementFrame=None,
        rsnCipherSuiteCcmp128=None,
        rsnCipherSuiteCcmp256=None,
        rsnCipherSuiteGcmp128=None,
        rsnCipherSuiteGcmp256=None,
        sessionTimeOut=None,
        sessionTimeOutEnable=None,
        site_id='string',
        sleepingClientEnable=None,
        sleepingClientTimeout=None,
        ssid=None,
        ssidRadioType=None,
        webPassthrough=None,
        wlanBandSelectEnable=None,
        wlanType=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_ssid_v1_default_val(api, validator):
    try:
        assert is_valid_update_ssid_v1(
            validator,
            update_ssid_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_ssid_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0be7fef60e7b5cdbabd4b93f6a0b4b68_v3_1_3_0').validate(obj)
    return True


def delete_ssid_v1(api):
    endpoint_result = api.wireless.delete_ssid_v1(
        id='string',
        remove_override_in_hierarchy=True,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_ssid_v1(api, validator):
    try:
        assert is_valid_delete_ssid_v1(
            validator,
            delete_ssid_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_ssid_v1_default_val(api):
    endpoint_result = api.wireless.delete_ssid_v1(
        id='string',
        remove_override_in_hierarchy=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_ssid_v1_default_val(api, validator):
    try:
        assert is_valid_delete_ssid_v1(
            validator,
            delete_ssid_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_or_overridessid_v1(json_schema_validate, obj):
    json_schema_validate('jsd_04c2a16208da55e8a615348ed3d530ac_v3_1_3_0').validate(obj)
    return True


def update_or_overridessid_v1(api):
    endpoint_result = api.wireless.update_or_overridessid_v1(
        aaaOverride=True,
        acctServers=['string'],
        aclName='string',
        active_validation=True,
        authServer='string',
        authServers=['string'],
        authType='string',
        basicServiceSetClientIdleTimeout=0,
        basicServiceSetMaxIdleEnable=True,
        cckmTsfTolerance=0,
        clientExclusionEnable=True,
        clientExclusionTimeout=0,
        clientRateLimit=0,
        coverageHoleDetectionEnable=True,
        directedMulticastServiceEnable=True,
        egressQos='string',
        externalAuthIpAddress='string',
        fastTransition='string',
        fastTransitionOverTheDistributedSystemEnable=True,
        ghz24Policy='string',
        ghz6PolicyClientSteering=True,
        id='string',
        ingressQos='string',
        isApBeaconProtectionEnabled=True,
        isAuthKey8021x=True,
        isAuthKey8021xPlusFT=True,
        isAuthKey8021x_SHA256=True,
        isAuthKeyEasyPSK=True,
        isAuthKeyOWE=True,
        isAuthKeyPSK=True,
        isAuthKeyPSKPlusFT=True,
        isAuthKeyPSKSHA256=True,
        isAuthKeySae=True,
        isAuthKeySaeExt=True,
        isAuthKeySaeExtPlusFT=True,
        isAuthKeySaePlusFT=True,
        isAuthKeySuiteB1921x=True,
        isAuthKeySuiteB1x=True,
        isBroadcastSSID=True,
        isCckmEnabled=True,
        isEnabled=True,
        isFastLaneEnabled=True,
        isHex=True,
        isMacFilteringEnabled=True,
        isPosturingEnabled=True,
        isRadiusProfilingEnabled=True,
        isRandomMacFilterEnabled=True,
        l3AuthType='string',
        managementFrameProtectionClientprotection='string',
        multiPSKSettings=[{'priority': 0, 'passphraseType': 'string', 'passphrase': 'string'}],
        nasOptions=['string'],
        neighborListEnable=True,
        openSsid='string',
        passphrase='string',
        payload=None,
        policyProfileName='string',
        profileName='string',
        protectedManagementFrame='string',
        rsnCipherSuiteCcmp128=True,
        rsnCipherSuiteCcmp256=True,
        rsnCipherSuiteGcmp128=True,
        rsnCipherSuiteGcmp256=True,
        sessionTimeOut=0,
        sessionTimeOutEnable=True,
        site_id='string',
        sleepingClientEnable=True,
        sleepingClientTimeout=0,
        ssid='string',
        ssidRadioType='string',
        webPassthrough=True,
        wlanBandSelectEnable=True,
        wlanType='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_or_overridessid_v1(api, validator):
    try:
        assert is_valid_update_or_overridessid_v1(
            validator,
            update_or_overridessid_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_or_overridessid_v1_default_val(api):
    endpoint_result = api.wireless.update_or_overridessid_v1(
        aaaOverride=None,
        acctServers=None,
        aclName=None,
        active_validation=True,
        authServer=None,
        authServers=None,
        authType=None,
        basicServiceSetClientIdleTimeout=None,
        basicServiceSetMaxIdleEnable=None,
        cckmTsfTolerance=None,
        clientExclusionEnable=None,
        clientExclusionTimeout=None,
        clientRateLimit=None,
        coverageHoleDetectionEnable=None,
        directedMulticastServiceEnable=None,
        egressQos=None,
        externalAuthIpAddress=None,
        fastTransition=None,
        fastTransitionOverTheDistributedSystemEnable=None,
        ghz24Policy=None,
        ghz6PolicyClientSteering=None,
        id='string',
        ingressQos=None,
        isApBeaconProtectionEnabled=None,
        isAuthKey8021x=None,
        isAuthKey8021xPlusFT=None,
        isAuthKey8021x_SHA256=None,
        isAuthKeyEasyPSK=None,
        isAuthKeyOWE=None,
        isAuthKeyPSK=None,
        isAuthKeyPSKPlusFT=None,
        isAuthKeyPSKSHA256=None,
        isAuthKeySae=None,
        isAuthKeySaeExt=None,
        isAuthKeySaeExtPlusFT=None,
        isAuthKeySaePlusFT=None,
        isAuthKeySuiteB1921x=None,
        isAuthKeySuiteB1x=None,
        isBroadcastSSID=None,
        isCckmEnabled=None,
        isEnabled=None,
        isFastLaneEnabled=None,
        isHex=None,
        isMacFilteringEnabled=None,
        isPosturingEnabled=None,
        isRadiusProfilingEnabled=None,
        isRandomMacFilterEnabled=None,
        l3AuthType=None,
        managementFrameProtectionClientprotection=None,
        multiPSKSettings=None,
        nasOptions=None,
        neighborListEnable=None,
        openSsid=None,
        passphrase=None,
        payload=None,
        policyProfileName=None,
        profileName=None,
        protectedManagementFrame=None,
        rsnCipherSuiteCcmp128=None,
        rsnCipherSuiteCcmp256=None,
        rsnCipherSuiteGcmp128=None,
        rsnCipherSuiteGcmp256=None,
        sessionTimeOut=None,
        sessionTimeOutEnable=None,
        site_id='string',
        sleepingClientEnable=None,
        sleepingClientTimeout=None,
        ssid=None,
        ssidRadioType=None,
        webPassthrough=None,
        wlanBandSelectEnable=None,
        wlanType=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_or_overridessid_v1_default_val(api, validator):
    try:
        assert is_valid_update_or_overridessid_v1(
            validator,
            update_or_overridessid_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_ap_pnp_location_setting_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ba52bb172d495710aa00f7d4d060ec50_v3_1_3_0').validate(obj)
    return True


def update_ap_pnp_location_setting_v1(api):
    endpoint_result = api.wireless.update_ap_pnp_location_setting_v1(
        active_validation=True,
        apPnPLocation='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_ap_pnp_location_setting_v1(api, validator):
    try:
        assert is_valid_update_ap_pnp_location_setting_v1(
            validator,
            update_ap_pnp_location_setting_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_ap_pnp_location_setting_v1_default_val(api):
    endpoint_result = api.wireless.update_ap_pnp_location_setting_v1(
        active_validation=True,
        apPnPLocation=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_ap_pnp_location_setting_v1_default_val(api, validator):
    try:
        assert is_valid_update_ap_pnp_location_setting_v1(
            validator,
            update_ap_pnp_location_setting_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ap_pnp_location_setting_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2ca8a515b6fc5c0eb78955f6218efc2a_v3_1_3_0').validate(obj)
    return True


def get_ap_pnp_location_setting_v1(api):
    endpoint_result = api.wireless.get_ap_pnp_location_setting_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_pnp_location_setting_v1(api, validator):
    try:
        assert is_valid_get_ap_pnp_location_setting_v1(
            validator,
            get_ap_pnp_location_setting_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ap_pnp_location_setting_v1_default_val(api):
    endpoint_result = api.wireless.get_ap_pnp_location_setting_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_pnp_location_setting_v1_default_val(api, validator):
    try:
        assert is_valid_get_ap_pnp_location_setting_v1(
            validator,
            get_ap_pnp_location_setting_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9610a850fb6c5451a7ad20ba76f4ff43_v3_1_3_0').validate(obj)
    return True


def delete_wireless_profile_v1(api):
    endpoint_result = api.wireless.delete_wireless_profile_v1(
        wireless_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_wireless_profile_v1(api, validator):
    try:
        assert is_valid_delete_wireless_profile_v1(
            validator,
            delete_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.delete_wireless_profile_v1(
        wireless_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_delete_wireless_profile_v1(
            validator,
            delete_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_configure_access_points_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6e0bd567c1395531a7f18ab4e14110bd_v3_1_3_0').validate(obj)
    return True


def configure_access_points_v1(api):
    endpoint_result = api.wireless.configure_access_points_v1(
        active_validation=True,
        adminStatus=True,
        apList=[{'apName': 'string', 'macAddress': 'string', 'apNameNew': 'string'}],
        apMode=0,
        configureAdminStatus=True,
        configureApMode=True,
        configureFailoverPriority=True,
        configureHAController=True,
        configureLedBrightnessLevel=True,
        configureLedStatus=True,
        configureLocation=True,
        failoverPriority=0,
        isAssignedSiteAsLocation=True,
        ledBrightnessLevel=0,
        ledStatus=True,
        location='string',
        payload=None,
        primaryControllerName='string',
        primaryIpAddress={'address': 'string'},
        radioConfigurations=[{'configureRadioRoleAssignment': True, 'radioRoleAssignment': 'string', 'radioBand': 'string', 'configureAdminStatus': True, 'adminStatus': True, 'configureAntennaPatternName': True, 'antennaPatternName': 'string', 'antennaGain': 0, 'configureAntennaCable': True, 'antennaCableName': 'string', 'cableLoss': 0, 'configureChannel': True, 'channelAssignmentMode': 0, 'channelNumber': 0, 'configureChannelWidth': True, 'channelWidth': 0, 'configurePower': True, 'powerAssignmentMode': 0, 'powerlevel': 0, 'configureCleanAirSI': True, 'cleanAirSI': 0, 'radioType': 0}],
        secondaryControllerName='string',
        secondaryIpAddress={'address': 'string'},
        tertiaryControllerName='string',
        tertiaryIpAddress={'address': 'string'}
    )
    return endpoint_result


@pytest.mark.wireless
def test_configure_access_points_v1(api, validator):
    try:
        assert is_valid_configure_access_points_v1(
            validator,
            configure_access_points_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def configure_access_points_v1_default_val(api):
    endpoint_result = api.wireless.configure_access_points_v1(
        active_validation=True,
        adminStatus=None,
        apList=None,
        apMode=None,
        configureAdminStatus=None,
        configureApMode=None,
        configureFailoverPriority=None,
        configureHAController=None,
        configureLedBrightnessLevel=None,
        configureLedStatus=None,
        configureLocation=None,
        failoverPriority=None,
        isAssignedSiteAsLocation=None,
        ledBrightnessLevel=None,
        ledStatus=None,
        location=None,
        payload=None,
        primaryControllerName=None,
        primaryIpAddress=None,
        radioConfigurations=None,
        secondaryControllerName=None,
        secondaryIpAddress=None,
        tertiaryControllerName=None,
        tertiaryIpAddress=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_configure_access_points_v1_default_val(api, validator):
    try:
        assert is_valid_configure_access_points_v1(
            validator,
            configure_access_points_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_access_point_configuration_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_85522e2ccd7c54fa91dfe821a7869b84_v3_1_3_0').validate(obj)
    return True


def get_access_point_configuration_count_v1(api):
    endpoint_result = api.wireless.get_access_point_configuration_count_v1(
        ap_mode='string',
        ap_model='string',
        mesh_role='string',
        provisioned='string',
        wlc_ip_address='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_access_point_configuration_count_v1(api, validator):
    try:
        assert is_valid_get_access_point_configuration_count_v1(
            validator,
            get_access_point_configuration_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_access_point_configuration_count_v1_default_val(api):
    endpoint_result = api.wireless.get_access_point_configuration_count_v1(
        ap_mode=None,
        ap_model=None,
        mesh_role=None,
        provisioned=None,
        wlc_ip_address=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_access_point_configuration_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_access_point_configuration_count_v1(
            validator,
            get_access_point_configuration_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_access_point_configuration_task_result_v1(json_schema_validate, obj):
    json_schema_validate('jsd_435cc2c3a5b75a4091350fa84ac872c9_v3_1_3_0').validate(obj)
    return True


def get_access_point_configuration_task_result_v1(api):
    endpoint_result = api.wireless.get_access_point_configuration_task_result_v1(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_access_point_configuration_task_result_v1(api, validator):
    try:
        assert is_valid_get_access_point_configuration_task_result_v1(
            validator,
            get_access_point_configuration_task_result_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_access_point_configuration_task_result_v1_default_val(api):
    endpoint_result = api.wireless.get_access_point_configuration_task_result_v1(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_access_point_configuration_task_result_v1_default_val(api, validator):
    try:
        assert is_valid_get_access_point_configuration_task_result_v1(
            validator,
            get_access_point_configuration_task_result_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_access_point_configuration_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0fb7514b0e8c52be8cfd19dab5e31b06_v3_1_3_0').validate(obj)
    return True


def get_access_point_configuration_v1(api):
    endpoint_result = api.wireless.get_access_point_configuration_v1(
        ap_mode='string',
        ap_model='string',
        key='string',
        limit=0,
        mesh_role='string',
        offset=0,
        provisioned='string',
        wlc_ip_address='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_access_point_configuration_v1(api, validator):
    try:
        assert is_valid_get_access_point_configuration_v1(
            validator,
            get_access_point_configuration_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_access_point_configuration_v1_default_val(api):
    endpoint_result = api.wireless.get_access_point_configuration_v1(
        ap_mode=None,
        ap_model=None,
        key=None,
        limit=None,
        mesh_role=None,
        offset=None,
        provisioned=None,
        wlc_ip_address=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_access_point_configuration_v1_default_val(api, validator):
    try:
        assert is_valid_get_access_point_configuration_v1(
            validator,
            get_access_point_configuration_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_ap_provision_connectivity_v1(json_schema_validate, obj):
    json_schema_validate('jsd_09f790a930d452708353c374f5c0f90f_v3_1_3_0').validate(obj)
    return True


def ap_provision_connectivity_v1(api):
    endpoint_result = api.wireless.ap_provision_connectivity_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_ap_provision_connectivity_v1(api, validator):
    try:
        assert is_valid_ap_provision_connectivity_v1(
            validator,
            ap_provision_connectivity_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def ap_provision_connectivity_v1_default_val(api):
    endpoint_result = api.wireless.ap_provision_connectivity_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_ap_provision_connectivity_v1_default_val(api, validator):
    try:
        assert is_valid_ap_provision_connectivity_v1(
            validator,
            ap_provision_connectivity_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_dynamic_interface_v1(json_schema_validate, obj):
    json_schema_validate('jsd_54ed6ee6a19c5e7da1606b05b7188964_v3_1_3_0').validate(obj)
    return True


def delete_dynamic_interface_v1(api):
    endpoint_result = api.wireless.delete_dynamic_interface_v1(
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_dynamic_interface_v1(api, validator):
    try:
        assert is_valid_delete_dynamic_interface_v1(
            validator,
            delete_dynamic_interface_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_dynamic_interface_v1_default_val(api):
    endpoint_result = api.wireless.delete_dynamic_interface_v1(
        interface_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_dynamic_interface_v1_default_val(api, validator):
    try:
        assert is_valid_delete_dynamic_interface_v1(
            validator,
            delete_dynamic_interface_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_update_dynamic_interface_v1(json_schema_validate, obj):
    json_schema_validate('jsd_36c00df3623b5a74ad41e75487ed9b77_v3_1_3_0').validate(obj)
    return True


def create_update_dynamic_interface_v1(api):
    endpoint_result = api.wireless.create_update_dynamic_interface_v1(
        active_validation=True,
        interfaceName='string',
        payload=None,
        vlanId=0
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_update_dynamic_interface_v1(api, validator):
    try:
        assert is_valid_create_update_dynamic_interface_v1(
            validator,
            create_update_dynamic_interface_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_update_dynamic_interface_v1_default_val(api):
    endpoint_result = api.wireless.create_update_dynamic_interface_v1(
        active_validation=True,
        interfaceName=None,
        payload=None,
        vlanId=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_update_dynamic_interface_v1_default_val(api, validator):
    try:
        assert is_valid_create_update_dynamic_interface_v1(
            validator,
            create_update_dynamic_interface_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_dynamic_interface_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2583c9fb8b0f5c69ba22f920e4044538_v3_1_3_0').validate(obj)
    return True


def get_dynamic_interface_v1(api):
    endpoint_result = api.wireless.get_dynamic_interface_v1(
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_dynamic_interface_v1(api, validator):
    try:
        assert is_valid_get_dynamic_interface_v1(
            validator,
            get_dynamic_interface_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_dynamic_interface_v1_default_val(api):
    endpoint_result = api.wireless.get_dynamic_interface_v1(
        interface_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_dynamic_interface_v1_default_val(api, validator):
    try:
        assert is_valid_get_dynamic_interface_v1(
            validator,
            get_dynamic_interface_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5135bbf7ce025bc2a291b90c37a6b898_v3_1_3_0').validate(obj)
    return True


def update_wireless_profile_v1(api):
    endpoint_result = api.wireless.update_wireless_profile_v1(
        active_validation=True,
        payload=None,
        profileDetails={'name': 'string', 'sites': ['string'], 'ssidDetails': [{'name': 'string', 'enableFabric': True, 'flexConnect': {'enableFlexConnect': True, 'localToVlan': 0}, 'interfaceName': 'string', 'wlanProfileName': 'string', 'policyProfileName': 'string'}]}
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_wireless_profile_v1(api, validator):
    try:
        assert is_valid_update_wireless_profile_v1(
            validator,
            update_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.update_wireless_profile_v1(
        active_validation=True,
        payload=None,
        profileDetails=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_update_wireless_profile_v1(
            validator,
            update_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b95201b6a6905a10b463e036bf591166_v3_1_3_0').validate(obj)
    return True


def create_wireless_profile_v1(api):
    endpoint_result = api.wireless.create_wireless_profile_v1(
        active_validation=True,
        payload=None,
        profileDetails={'name': 'string', 'sites': ['string'], 'ssidDetails': [{'name': 'string', 'enableFabric': True, 'flexConnect': {'enableFlexConnect': True, 'localToVlan': 0}, 'interfaceName': 'string', 'wlanProfileName': 'string', 'policyProfileName': 'string'}]}
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_wireless_profile_v1(api, validator):
    try:
        assert is_valid_create_wireless_profile_v1(
            validator,
            create_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.create_wireless_profile_v1(
        active_validation=True,
        payload=None,
        profileDetails=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_create_wireless_profile_v1(
            validator,
            create_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bbc1866a50505c0695ae243718d51936_v3_1_3_0').validate(obj)
    return True


def get_wireless_profile_v1(api):
    endpoint_result = api.wireless.get_wireless_profile_v1(
        profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_wireless_profile_v1(api, validator):
    try:
        assert is_valid_get_wireless_profile_v1(
            validator,
            get_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.get_wireless_profile_v1(
        profile_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_get_wireless_profile_v1(
            validator,
            get_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_provision_update(json_schema_validate, obj):
    json_schema_validate('jsd_d0aab00569b258b481afedc35e6db392_v3_1_3_0').validate(obj)
    return True


def provision_update(api):
    endpoint_result = api.wireless.provision_update(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_provision_update(api, validator):
    try:
        assert is_valid_provision_update(
            validator,
            provision_update(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def provision_update_default_val(api):
    endpoint_result = api.wireless.provision_update(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_provision_update_default_val(api, validator):
    try:
        assert is_valid_provision_update(
            validator,
            provision_update_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_provision_v1(json_schema_validate, obj):
    json_schema_validate('jsd_359718e31c795964b3bdf85da1b5a2a5_v3_1_3_0').validate(obj)
    return True


def provision_v1(api):
    endpoint_result = api.wireless.provision_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_provision_v1(api, validator):
    try:
        assert is_valid_provision_v1(
            validator,
            provision_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def provision_v1_default_val(api):
    endpoint_result = api.wireless.provision_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_provision_v1_default_val(api, validator):
    try:
        assert is_valid_provision_v1(
            validator,
            provision_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_psk_override(json_schema_validate, obj):
    json_schema_validate('jsd_f99c96c3a9b45ddaabc2c75ff8efa67f_v3_1_3_0').validate(obj)
    return True


def psk_override(api):
    endpoint_result = api.wireless.psk_override(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_psk_override(api, validator):
    try:
        assert is_valid_psk_override(
            validator,
            psk_override(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def psk_override_default_val(api):
    endpoint_result = api.wireless.psk_override(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_psk_override_default_val(api, validator):
    try:
        assert is_valid_psk_override(
            validator,
            psk_override_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_rf_profiles_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ac37d6798c0b593088952123df03bb1b_v3_1_3_0').validate(obj)
    return True


def retrieve_rf_profiles_v1(api):
    endpoint_result = api.wireless.retrieve_rf_profiles_v1(
        rf_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_rf_profiles_v1(api, validator):
    try:
        assert is_valid_retrieve_rf_profiles_v1(
            validator,
            retrieve_rf_profiles_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_rf_profiles_v1_default_val(api):
    endpoint_result = api.wireless.retrieve_rf_profiles_v1(
        rf_profile_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_rf_profiles_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_rf_profiles_v1(
            validator,
            retrieve_rf_profiles_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_or_update_rf_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5f24f6c07641580ba6ed710e92c2da16_v3_1_3_0').validate(obj)
    return True


def create_or_update_rf_profile_v1(api):
    endpoint_result = api.wireless.create_or_update_rf_profile_v1(
        active_validation=True,
        channelWidth='string',
        defaultRfProfile=True,
        enableBrownField=True,
        enableCustom=True,
        enableRadioTypeA=True,
        enableRadioTypeB=True,
        enableRadioTypeC=True,
        name='string',
        payload=None,
        radioTypeAProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'powerThresholdV1': 0, 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0},
        radioTypeBProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'powerThresholdV1': 0, 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0},
        radioTypeCProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0, 'powerThresholdV1': 0}
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_or_update_rf_profile_v1(api, validator):
    try:
        assert is_valid_create_or_update_rf_profile_v1(
            validator,
            create_or_update_rf_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_or_update_rf_profile_v1_default_val(api):
    endpoint_result = api.wireless.create_or_update_rf_profile_v1(
        active_validation=True,
        channelWidth=None,
        defaultRfProfile=None,
        enableBrownField=None,
        enableCustom=None,
        enableRadioTypeA=None,
        enableRadioTypeB=None,
        enableRadioTypeC=None,
        name=None,
        payload=None,
        radioTypeAProperties=None,
        radioTypeBProperties=None,
        radioTypeCProperties=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_or_update_rf_profile_v1_default_val(api, validator):
    try:
        assert is_valid_create_or_update_rf_profile_v1(
            validator,
            create_or_update_rf_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_rf_profiles_v1(json_schema_validate, obj):
    json_schema_validate('jsd_97f3790386da5cd49480cb0503e59047_v3_1_3_0').validate(obj)
    return True


def delete_rf_profiles_v1(api):
    endpoint_result = api.wireless.delete_rf_profiles_v1(
        rf_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_rf_profiles_v1(api, validator):
    try:
        assert is_valid_delete_rf_profiles_v1(
            validator,
            delete_rf_profiles_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_rf_profiles_v1_default_val(api):
    endpoint_result = api.wireless.delete_rf_profiles_v1(
        rf_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_rf_profiles_v1_default_val(api, validator):
    try:
        assert is_valid_delete_rf_profiles_v1(
            validator,
            delete_rf_profiles_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_factory_reset_access_points_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4efa7f7a97b95f5885a00e6981b27b11_v3_1_3_0').validate(obj)
    return True


def factory_reset_access_points_v1(api):
    endpoint_result = api.wireless.factory_reset_access_points_v1(
        active_validation=True,
        apMacAddresses=['string'],
        keepStaticIPConfig=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_factory_reset_access_points_v1(api, validator):
    try:
        assert is_valid_factory_reset_access_points_v1(
            validator,
            factory_reset_access_points_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def factory_reset_access_points_v1_default_val(api):
    endpoint_result = api.wireless.factory_reset_access_points_v1(
        active_validation=True,
        apMacAddresses=None,
        keepStaticIPConfig=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_factory_reset_access_points_v1_default_val(api, validator):
    try:
        assert is_valid_factory_reset_access_points_v1(
            validator,
            factory_reset_access_points_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_access_points_factory_reset_status_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f10b36d381e85181a857e67339105684_v3_1_3_0').validate(obj)
    return True


def get_access_points_factory_reset_status_v1(api):
    endpoint_result = api.wireless.get_access_points_factory_reset_status_v1(
        task_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_access_points_factory_reset_status_v1(api, validator):
    try:
        assert is_valid_get_access_points_factory_reset_status_v1(
            validator,
            get_access_points_factory_reset_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_access_points_factory_reset_status_v1_default_val(api):
    endpoint_result = api.wireless.get_access_points_factory_reset_status_v1(
        task_id=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_access_points_factory_reset_status_v1_default_val(api, validator):
    try:
        assert is_valid_get_access_points_factory_reset_status_v1(
            validator,
            get_access_points_factory_reset_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_ap_provision_v1(json_schema_validate, obj):
    json_schema_validate('jsd_eab4d187be085cac8a53971def40bee0_v3_1_3_0').validate(obj)
    return True


def ap_provision_v1(api):
    endpoint_result = api.wireless.ap_provision_v1(
        active_validation=True,
        apZoneName='string',
        networkDevices=[{'deviceId': 'string', 'meshRole': 'string', 'beamState': 'string'}],
        payload=None,
        rfProfileName='string',
        siteId='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_ap_provision_v1(api, validator):
    try:
        assert is_valid_ap_provision_v1(
            validator,
            ap_provision_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def ap_provision_v1_default_val(api):
    endpoint_result = api.wireless.ap_provision_v1(
        active_validation=True,
        apZoneName=None,
        networkDevices=None,
        payload=None,
        rfProfileName=None,
        siteId=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_ap_provision_v1_default_val(api, validator):
    try:
        assert is_valid_ap_provision_v1(
            validator,
            ap_provision_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_anchor_capable_devices_v1(json_schema_validate, obj):
    json_schema_validate('jsd_946e1c353aa15463bf2867d0716712ca_v3_1_3_0').validate(obj)
    return True


def get_anchor_capable_devices_v1(api):
    endpoint_result = api.wireless.get_anchor_capable_devices_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_anchor_capable_devices_v1(api, validator):
    try:
        assert is_valid_get_anchor_capable_devices_v1(
            validator,
            get_anchor_capable_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_anchor_capable_devices_v1_default_val(api):
    endpoint_result = api.wireless.get_anchor_capable_devices_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_anchor_capable_devices_v1_default_val(api, validator):
    try:
        assert is_valid_get_anchor_capable_devices_v1(
            validator,
            get_anchor_capable_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_mesh_ap_neighbours_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4cc53655bf17533aa570d6eab1bbf706_v3_1_3_0').validate(obj)
    return True


def get_mesh_ap_neighbours_v1(api):
    endpoint_result = api.wireless.get_mesh_ap_neighbours_v1(
        ap_name='string',
        ethernet_mac_address='string',
        wlc_ip_address='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_mesh_ap_neighbours_v1(api, validator):
    try:
        assert is_valid_get_mesh_ap_neighbours_v1(
            validator,
            get_mesh_ap_neighbours_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_mesh_ap_neighbours_v1_default_val(api):
    endpoint_result = api.wireless.get_mesh_ap_neighbours_v1(
        ap_name=None,
        ethernet_mac_address=None,
        wlc_ip_address=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_mesh_ap_neighbours_v1_default_val(api, validator):
    try:
        assert is_valid_get_mesh_ap_neighbours_v1(
            validator,
            get_mesh_ap_neighbours_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_mesh_ap_neighbours_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3896079cd2975404a8d98235775136f7_v3_1_3_0').validate(obj)
    return True


def get_mesh_ap_neighbours_count_v1(api):
    endpoint_result = api.wireless.get_mesh_ap_neighbours_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_mesh_ap_neighbours_count_v1(api, validator):
    try:
        assert is_valid_get_mesh_ap_neighbours_count_v1(
            validator,
            get_mesh_ap_neighbours_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_mesh_ap_neighbours_count_v1_default_val(api):
    endpoint_result = api.wireless.get_mesh_ap_neighbours_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_mesh_ap_neighbours_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_mesh_ap_neighbours_count_v1(
            validator,
            get_mesh_ap_neighbours_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_mobility_groups_v1(json_schema_validate, obj):
    json_schema_validate('jsd_cb3e813f46055a3d945b3f77c58f913d_v3_1_3_0').validate(obj)
    return True


def get_mobility_groups_v1(api):
    endpoint_result = api.wireless.get_mobility_groups_v1(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_mobility_groups_v1(api, validator):
    try:
        assert is_valid_get_mobility_groups_v1(
            validator,
            get_mobility_groups_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_mobility_groups_v1_default_val(api):
    endpoint_result = api.wireless.get_mobility_groups_v1(
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_mobility_groups_v1_default_val(api, validator):
    try:
        assert is_valid_get_mobility_groups_v1(
            validator,
            get_mobility_groups_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_mobility_groups_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_226f0e19cf1f588cbe6fcbd0332a3987_v3_1_3_0').validate(obj)
    return True


def get_mobility_groups_count_v1(api):
    endpoint_result = api.wireless.get_mobility_groups_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_mobility_groups_count_v1(api, validator):
    try:
        assert is_valid_get_mobility_groups_count_v1(
            validator,
            get_mobility_groups_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_mobility_groups_count_v1_default_val(api):
    endpoint_result = api.wireless.get_mobility_groups_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_mobility_groups_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_mobility_groups_count_v1(
            validator,
            get_mobility_groups_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_mobility_provision_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bfd1cc1403c951a99c0fcafd59eaabf3_v3_1_3_0').validate(obj)
    return True


def mobility_provision_v1(api):
    endpoint_result = api.wireless.mobility_provision_v1(
        active_validation=True,
        dataLinkEncryption=True,
        dtlsHighCipher=True,
        macAddress='string',
        managementIp='string',
        mobilityGroupName='string',
        mobilityPeers=[{'peerIp': 'string', 'privateIpAddress': 'string', 'peerDeviceName': 'string', 'peerNetworkDeviceId': 'string', 'mobilityGroupName': 'string', 'memberMacAddress': 'string', 'deviceSeries': 'string', 'hashKey': 'string'}],
        networkDeviceId='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_mobility_provision_v1(api, validator):
    try:
        assert is_valid_mobility_provision_v1(
            validator,
            mobility_provision_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def mobility_provision_v1_default_val(api):
    endpoint_result = api.wireless.mobility_provision_v1(
        active_validation=True,
        dataLinkEncryption=None,
        dtlsHighCipher=None,
        macAddress=None,
        managementIp=None,
        mobilityGroupName=None,
        mobilityPeers=None,
        networkDeviceId=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_mobility_provision_v1_default_val(api, validator):
    try:
        assert is_valid_mobility_provision_v1(
            validator,
            mobility_provision_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_mobility_reset_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a6c4ce7aef8251a2a8646ba0b5c1826a_v3_1_3_0').validate(obj)
    return True


def mobility_reset_v1(api):
    endpoint_result = api.wireless.mobility_reset_v1(
        active_validation=True,
        networkDeviceId='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_mobility_reset_v1(api, validator):
    try:
        assert is_valid_mobility_reset_v1(
            validator,
            mobility_reset_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def mobility_reset_v1_default_val(api):
    endpoint_result = api.wireless.mobility_reset_v1(
        active_validation=True,
        networkDeviceId=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_mobility_reset_v1_default_val(api, validator):
    try:
        assert is_valid_mobility_reset_v1(
            validator,
            mobility_reset_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_managed_ap_locations_for_w_l_c_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7f019a24c5ce50f082d081bb72ff4df9_v3_1_3_0').validate(obj)
    return True


def assign_managed_ap_locations_for_w_l_c_v1(api):
    endpoint_result = api.wireless.assign_managed_ap_locations_for_w_l_c_v1(
        active_validation=True,
        device_id='string',
        payload=None,
        primaryManagedAPLocationsSiteIds=['string'],
        secondaryManagedAPLocationsSiteIds=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_assign_managed_ap_locations_for_w_l_c_v1(api, validator):
    try:
        assert is_valid_assign_managed_ap_locations_for_w_l_c_v1(
            validator,
            assign_managed_ap_locations_for_w_l_c_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_managed_ap_locations_for_w_l_c_v1_default_val(api):
    endpoint_result = api.wireless.assign_managed_ap_locations_for_w_l_c_v1(
        active_validation=True,
        device_id='string',
        payload=None,
        primaryManagedAPLocationsSiteIds=None,
        secondaryManagedAPLocationsSiteIds=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_assign_managed_ap_locations_for_w_l_c_v1_default_val(api, validator):
    try:
        assert is_valid_assign_managed_ap_locations_for_w_l_c_v1(
            validator,
            assign_managed_ap_locations_for_w_l_c_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_wireless_controller_provision_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b0aa8e79d21f5e579908825e70aaccf6_v3_1_3_0').validate(obj)
    return True


def wireless_controller_provision_v1(api):
    endpoint_result = api.wireless.wireless_controller_provision_v1(
        active_validation=True,
        apAuthorizationListName='string',
        authorizeMeshAndNonMeshAccessPoints=True,
        device_id='string',
        featureTemplatesOverridenAttributes={'editFeatureTemplates': [{'featureTemplateId': 'string', 'attributes': {}, 'additionalIdentifiers': {'wlanProfileName': 'string', 'siteUuid': 'string'}, 'excludedAttributes': ['string']}]},
        interfaces=[{'interfaceName': 'string', 'vlanId': 0, 'interfaceIPAddress': 'string', 'interfaceNetmaskInCIDR': 0, 'interfaceGateway': 'string', 'lagOrPortNumber': 0}],
        payload=None,
        rollingApUpgrade={'enableRollingApUpgrade': True, 'apRebootPercentage': 0},
        skipApProvision=True
    )
    return endpoint_result


@pytest.mark.wireless
def test_wireless_controller_provision_v1(api, validator):
    try:
        assert is_valid_wireless_controller_provision_v1(
            validator,
            wireless_controller_provision_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def wireless_controller_provision_v1_default_val(api):
    endpoint_result = api.wireless.wireless_controller_provision_v1(
        active_validation=True,
        apAuthorizationListName=None,
        authorizeMeshAndNonMeshAccessPoints=None,
        device_id='string',
        featureTemplatesOverridenAttributes=None,
        interfaces=None,
        payload=None,
        rollingApUpgrade=None,
        skipApProvision=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_wireless_controller_provision_v1_default_val(api, validator):
    try:
        assert is_valid_wireless_controller_provision_v1(
            validator,
            wireless_controller_provision_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_anchor_managed_ap_locations_for_specific_wireless_controller_v1(json_schema_validate, obj):
    json_schema_validate('jsd_432de386cae35720b6782009e61541c1_v3_1_3_0').validate(obj)
    return True


def get_anchor_managed_ap_locations_for_specific_wireless_controller_v1(api):
    endpoint_result = api.wireless.get_anchor_managed_ap_locations_for_specific_wireless_controller_v1(
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_anchor_managed_ap_locations_for_specific_wireless_controller_v1(api, validator):
    try:
        assert is_valid_get_anchor_managed_ap_locations_for_specific_wireless_controller_v1(
            validator,
            get_anchor_managed_ap_locations_for_specific_wireless_controller_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_anchor_managed_ap_locations_for_specific_wireless_controller_v1_default_val(api):
    endpoint_result = api.wireless.get_anchor_managed_ap_locations_for_specific_wireless_controller_v1(
        limit=None,
        network_device_id='string',
        offset=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_anchor_managed_ap_locations_for_specific_wireless_controller_v1_default_val(api, validator):
    try:
        assert is_valid_get_anchor_managed_ap_locations_for_specific_wireless_controller_v1(
            validator,
            get_anchor_managed_ap_locations_for_specific_wireless_controller_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ap_authorization_list_by_network_device_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e9661bbf6b2f5f0d981695212ff1b5ea_v3_1_3_0').validate(obj)
    return True


def get_ap_authorization_list_by_network_device_id_v1(api):
    endpoint_result = api.wireless.get_ap_authorization_list_by_network_device_id_v1(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_authorization_list_by_network_device_id_v1(api, validator):
    try:
        assert is_valid_get_ap_authorization_list_by_network_device_id_v1(
            validator,
            get_ap_authorization_list_by_network_device_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ap_authorization_list_by_network_device_id_v1_default_val(api):
    endpoint_result = api.wireless.get_ap_authorization_list_by_network_device_id_v1(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_authorization_list_by_network_device_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_ap_authorization_list_by_network_device_id_v1(
            validator,
            get_ap_authorization_list_by_network_device_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_managed_ap_locations_count_for_specific_wireless_controller_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f4a6e8f2c1de51f5b70e9c75c4b6fc1c_v3_1_3_0').validate(obj)
    return True


def get_managed_ap_locations_count_for_specific_wireless_controller_v1(api):
    endpoint_result = api.wireless.get_managed_ap_locations_count_for_specific_wireless_controller_v1(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_managed_ap_locations_count_for_specific_wireless_controller_v1(api, validator):
    try:
        assert is_valid_get_managed_ap_locations_count_for_specific_wireless_controller_v1(
            validator,
            get_managed_ap_locations_count_for_specific_wireless_controller_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_managed_ap_locations_count_for_specific_wireless_controller_v1_default_val(api):
    endpoint_result = api.wireless.get_managed_ap_locations_count_for_specific_wireless_controller_v1(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_managed_ap_locations_count_for_specific_wireless_controller_v1_default_val(api, validator):
    try:
        assert is_valid_get_managed_ap_locations_count_for_specific_wireless_controller_v1(
            validator,
            get_managed_ap_locations_count_for_specific_wireless_controller_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_primary_managed_ap_locations_for_specific_wireless_controller_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e9b5024741155ad880b482720757f661_v3_1_3_0').validate(obj)
    return True


def get_primary_managed_ap_locations_for_specific_wireless_controller_v1(api):
    endpoint_result = api.wireless.get_primary_managed_ap_locations_for_specific_wireless_controller_v1(
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_primary_managed_ap_locations_for_specific_wireless_controller_v1(api, validator):
    try:
        assert is_valid_get_primary_managed_ap_locations_for_specific_wireless_controller_v1(
            validator,
            get_primary_managed_ap_locations_for_specific_wireless_controller_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_primary_managed_ap_locations_for_specific_wireless_controller_v1_default_val(api):
    endpoint_result = api.wireless.get_primary_managed_ap_locations_for_specific_wireless_controller_v1(
        limit=None,
        network_device_id='string',
        offset=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_primary_managed_ap_locations_for_specific_wireless_controller_v1_default_val(api, validator):
    try:
        assert is_valid_get_primary_managed_ap_locations_for_specific_wireless_controller_v1(
            validator,
            get_primary_managed_ap_locations_for_specific_wireless_controller_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_wireless_controller_provision_status_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4c882059a8b25dbeb4e05b2beff82803_v3_1_3_0').validate(obj)
    return True


def wireless_controller_provision_status_v1(api):
    endpoint_result = api.wireless.wireless_controller_provision_status_v1(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_wireless_controller_provision_status_v1(api, validator):
    try:
        assert is_valid_wireless_controller_provision_status_v1(
            validator,
            wireless_controller_provision_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def wireless_controller_provision_status_v1_default_val(api):
    endpoint_result = api.wireless.wireless_controller_provision_status_v1(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_wireless_controller_provision_status_v1_default_val(api, validator):
    try:
        assert is_valid_wireless_controller_provision_status_v1(
            validator,
            wireless_controller_provision_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_secondary_managed_ap_locations_for_specific_wireless_controller_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7a431078850850a5bef6cb4fa9915fb7_v3_1_3_0').validate(obj)
    return True


def get_secondary_managed_ap_locations_for_specific_wireless_controller_v1(api):
    endpoint_result = api.wireless.get_secondary_managed_ap_locations_for_specific_wireless_controller_v1(
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_secondary_managed_ap_locations_for_specific_wireless_controller_v1(api, validator):
    try:
        assert is_valid_get_secondary_managed_ap_locations_for_specific_wireless_controller_v1(
            validator,
            get_secondary_managed_ap_locations_for_specific_wireless_controller_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_secondary_managed_ap_locations_for_specific_wireless_controller_v1_default_val(api):
    endpoint_result = api.wireless.get_secondary_managed_ap_locations_for_specific_wireless_controller_v1(
        limit=None,
        network_device_id='string',
        offset=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_secondary_managed_ap_locations_for_specific_wireless_controller_v1_default_val(api, validator):
    try:
        assert is_valid_get_secondary_managed_ap_locations_for_specific_wireless_controller_v1(
            validator,
            get_secondary_managed_ap_locations_for_specific_wireless_controller_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ssid_details_for_specific_wireless_controller_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6889efdb6b3d51ff9e3e2de942ca96c4_v3_1_3_0').validate(obj)
    return True


def get_ssid_details_for_specific_wireless_controller_v1(api):
    endpoint_result = api.wireless.get_ssid_details_for_specific_wireless_controller_v1(
        admin_status=True,
        limit=0,
        managed=True,
        network_device_id='string',
        offset=0,
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ssid_details_for_specific_wireless_controller_v1(api, validator):
    try:
        assert is_valid_get_ssid_details_for_specific_wireless_controller_v1(
            validator,
            get_ssid_details_for_specific_wireless_controller_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ssid_details_for_specific_wireless_controller_v1_default_val(api):
    endpoint_result = api.wireless.get_ssid_details_for_specific_wireless_controller_v1(
        admin_status=None,
        limit=None,
        managed=None,
        network_device_id='string',
        offset=None,
        ssid_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ssid_details_for_specific_wireless_controller_v1_default_val(api, validator):
    try:
        assert is_valid_get_ssid_details_for_specific_wireless_controller_v1(
            validator,
            get_ssid_details_for_specific_wireless_controller_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ssid_count_for_specific_wireless_controller_v1(json_schema_validate, obj):
    json_schema_validate('jsd_19db60b529835a2e8d3f67c681f1ace4_v3_1_3_0').validate(obj)
    return True


def get_ssid_count_for_specific_wireless_controller_v1(api):
    endpoint_result = api.wireless.get_ssid_count_for_specific_wireless_controller_v1(
        admin_status=True,
        managed=True,
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ssid_count_for_specific_wireless_controller_v1(api, validator):
    try:
        assert is_valid_get_ssid_count_for_specific_wireless_controller_v1(
            validator,
            get_ssid_count_for_specific_wireless_controller_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ssid_count_for_specific_wireless_controller_v1_default_val(api):
    endpoint_result = api.wireless.get_ssid_count_for_specific_wireless_controller_v1(
        admin_status=None,
        managed=None,
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ssid_count_for_specific_wireless_controller_v1_default_val(api, validator):
    try:
        assert is_valid_get_ssid_count_for_specific_wireless_controller_v1(
            validator,
            get_ssid_count_for_specific_wireless_controller_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_wireless_profiles_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6bec142b3bf65c109d752da5705ae2ca_v3_1_3_0').validate(obj)
    return True


def get_wireless_profiles_v1(api):
    endpoint_result = api.wireless.get_wireless_profiles_v1(
        limit=0,
        offset=0,
        wireless_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_wireless_profiles_v1(api, validator):
    try:
        assert is_valid_get_wireless_profiles_v1(
            validator,
            get_wireless_profiles_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_wireless_profiles_v1_default_val(api):
    endpoint_result = api.wireless.get_wireless_profiles_v1(
        limit=None,
        offset=None,
        wireless_profile_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_wireless_profiles_v1_default_val(api, validator):
    try:
        assert is_valid_get_wireless_profiles_v1(
            validator,
            get_wireless_profiles_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_wireless_profile_connectivity_v1(json_schema_validate, obj):
    json_schema_validate('jsd_75cc59d48f8159008f52b29e08738811_v3_1_3_0').validate(obj)
    return True


def create_wireless_profile_connectivity_v1(api):
    endpoint_result = api.wireless.create_wireless_profile_connectivity_v1(
        active_validation=True,
        additionalInterfaces=['string'],
        apZones=[{'apZoneName': 'string', 'rfProfileName': 'string', 'ssids': ['string']}],
        featureTemplates=[{'id': 'string', 'ssids': ['string']}],
        payload=None,
        ssidDetails=[{'ssidName': 'string', 'flexConnect': {'enableFlexConnect': True, 'localToVlan': 0}, 'enableFabric': True, 'wlanProfileName': 'string', 'interfaceName': 'string', 'dot11beProfileId': 'string', 'anchorGroupName': 'string', 'vlanGroupName': 'string', 'policyProfileName': 'string'}],
        wirelessProfileName='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_wireless_profile_connectivity_v1(api, validator):
    try:
        assert is_valid_create_wireless_profile_connectivity_v1(
            validator,
            create_wireless_profile_connectivity_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_wireless_profile_connectivity_v1_default_val(api):
    endpoint_result = api.wireless.create_wireless_profile_connectivity_v1(
        active_validation=True,
        additionalInterfaces=None,
        apZones=None,
        featureTemplates=None,
        payload=None,
        ssidDetails=None,
        wirelessProfileName=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_wireless_profile_connectivity_v1_default_val(api, validator):
    try:
        assert is_valid_create_wireless_profile_connectivity_v1(
            validator,
            create_wireless_profile_connectivity_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_wireless_profiles_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ef56c845d27d59e5974077ade9deedf3_v3_1_3_0').validate(obj)
    return True


def get_wireless_profiles_count_v1(api):
    endpoint_result = api.wireless.get_wireless_profiles_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_wireless_profiles_count_v1(api, validator):
    try:
        assert is_valid_get_wireless_profiles_count_v1(
            validator,
            get_wireless_profiles_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_wireless_profiles_count_v1_default_val(api):
    endpoint_result = api.wireless.get_wireless_profiles_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_wireless_profiles_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_wireless_profiles_count_v1(
            validator,
            get_wireless_profiles_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_wireless_profile_connectivity_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d91a3aad0fd954e7a43aa3256ce433f6_v3_1_3_0').validate(obj)
    return True


def update_wireless_profile_connectivity_v1(api):
    endpoint_result = api.wireless.update_wireless_profile_connectivity_v1(
        active_validation=True,
        additionalInterfaces=['string'],
        apZones=[{'apZoneName': 'string', 'rfProfileName': 'string', 'ssids': ['string']}],
        featureTemplates=[{'id': 'string', 'ssids': ['string']}],
        id='string',
        payload=None,
        ssidDetails=[{'ssidName': 'string', 'flexConnect': {'enableFlexConnect': True, 'localToVlan': 0}, 'enableFabric': True, 'wlanProfileName': 'string', 'interfaceName': 'string', 'dot11beProfileId': 'string', 'anchorGroupName': 'string', 'vlanGroupName': 'string', 'policyProfileName': 'string'}],
        wirelessProfileName='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_wireless_profile_connectivity_v1(api, validator):
    try:
        assert is_valid_update_wireless_profile_connectivity_v1(
            validator,
            update_wireless_profile_connectivity_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_wireless_profile_connectivity_v1_default_val(api):
    endpoint_result = api.wireless.update_wireless_profile_connectivity_v1(
        active_validation=True,
        additionalInterfaces=None,
        apZones=None,
        featureTemplates=None,
        id='string',
        payload=None,
        ssidDetails=None,
        wirelessProfileName=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_wireless_profile_connectivity_v1_default_val(api, validator):
    try:
        assert is_valid_update_wireless_profile_connectivity_v1(
            validator,
            update_wireless_profile_connectivity_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_wireless_profile_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5d89e08ebbe2528088fbdb3b367cb23b_v3_1_3_0').validate(obj)
    return True


def get_wireless_profile_by_id_v1(api):
    endpoint_result = api.wireless.get_wireless_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_wireless_profile_by_id_v1(api, validator):
    try:
        assert is_valid_get_wireless_profile_by_id_v1(
            validator,
            get_wireless_profile_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_wireless_profile_by_id_v1_default_val(api):
    endpoint_result = api.wireless.get_wireless_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_wireless_profile_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_wireless_profile_by_id_v1(
            validator,
            get_wireless_profile_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_wireless_profile_connectivity_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2439792afcc95b9babb1b6a776e065e1_v3_1_3_0').validate(obj)
    return True


def delete_wireless_profile_connectivity_v1(api):
    endpoint_result = api.wireless.delete_wireless_profile_connectivity_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_wireless_profile_connectivity_v1(api, validator):
    try:
        assert is_valid_delete_wireless_profile_connectivity_v1(
            validator,
            delete_wireless_profile_connectivity_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_wireless_profile_connectivity_v1_default_val(api):
    endpoint_result = api.wireless.delete_wireless_profile_connectivity_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_wireless_profile_connectivity_v1_default_val(api, validator):
    try:
        assert is_valid_delete_wireless_profile_connectivity_v1(
            validator,
            delete_wireless_profile_connectivity_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_all_policy_tags_for_a_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_838ea7127c17517d9c507aa279a815a9_v3_1_3_0').validate(obj)
    return True


def retrieve_all_policy_tags_for_a_wireless_profile_v1(api):
    endpoint_result = api.wireless.retrieve_all_policy_tags_for_a_wireless_profile_v1(
        id='string',
        limit=0,
        offset=0,
        policy_tag_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_all_policy_tags_for_a_wireless_profile_v1(api, validator):
    try:
        assert is_valid_retrieve_all_policy_tags_for_a_wireless_profile_v1(
            validator,
            retrieve_all_policy_tags_for_a_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_all_policy_tags_for_a_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.retrieve_all_policy_tags_for_a_wireless_profile_v1(
        id='string',
        limit=None,
        offset=None,
        policy_tag_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_all_policy_tags_for_a_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_all_policy_tags_for_a_wireless_profile_v1(
            validator,
            retrieve_all_policy_tags_for_a_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_multiple_policy_tags_for_a_wireless_profile_in_bulk_v1(json_schema_validate, obj):
    json_schema_validate('jsd_eeb595d249295989a4917261463ea82a_v3_1_3_0').validate(obj)
    return True


def create_multiple_policy_tags_for_a_wireless_profile_in_bulk_v1(api):
    endpoint_result = api.wireless.create_multiple_policy_tags_for_a_wireless_profile_in_bulk_v1(
        active_validation=True,
        id='string',
        items=[[{'siteIds': ['string'], 'policyTagName': 'string', 'apZones': ['string']}]],
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_multiple_policy_tags_for_a_wireless_profile_in_bulk_v1(api, validator):
    try:
        assert is_valid_create_multiple_policy_tags_for_a_wireless_profile_in_bulk_v1(
            validator,
            create_multiple_policy_tags_for_a_wireless_profile_in_bulk_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_multiple_policy_tags_for_a_wireless_profile_in_bulk_v1_default_val(api):
    endpoint_result = api.wireless.create_multiple_policy_tags_for_a_wireless_profile_in_bulk_v1(
        active_validation=True,
        id='string',
        items=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_multiple_policy_tags_for_a_wireless_profile_in_bulk_v1_default_val(api, validator):
    try:
        assert is_valid_create_multiple_policy_tags_for_a_wireless_profile_in_bulk_v1(
            validator,
            create_multiple_policy_tags_for_a_wireless_profile_in_bulk_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_policy_tags_for_a_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_57b4b3d55b8a57549d0836968ba4bb20_v3_1_3_0').validate(obj)
    return True


def retrieve_the_count_of_policy_tags_for_a_wireless_profile_v1(api):
    endpoint_result = api.wireless.retrieve_the_count_of_policy_tags_for_a_wireless_profile_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_the_count_of_policy_tags_for_a_wireless_profile_v1(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_policy_tags_for_a_wireless_profile_v1(
            validator,
            retrieve_the_count_of_policy_tags_for_a_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_policy_tags_for_a_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.retrieve_the_count_of_policy_tags_for_a_wireless_profile_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_the_count_of_policy_tags_for_a_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_policy_tags_for_a_wireless_profile_v1(
            validator,
            retrieve_the_count_of_policy_tags_for_a_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_specific_policy_tag_from_a_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_566ee08c569859cf8518a61fd9ec2045_v3_1_3_0').validate(obj)
    return True


def delete_a_specific_policy_tag_from_a_wireless_profile_v1(api):
    endpoint_result = api.wireless.delete_a_specific_policy_tag_from_a_wireless_profile_v1(
        id='string',
        policy_tag_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_a_specific_policy_tag_from_a_wireless_profile_v1(api, validator):
    try:
        assert is_valid_delete_a_specific_policy_tag_from_a_wireless_profile_v1(
            validator,
            delete_a_specific_policy_tag_from_a_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_specific_policy_tag_from_a_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.delete_a_specific_policy_tag_from_a_wireless_profile_v1(
        id='string',
        policy_tag_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_a_specific_policy_tag_from_a_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_delete_a_specific_policy_tag_from_a_wireless_profile_v1(
            validator,
            delete_a_specific_policy_tag_from_a_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_a_specific_policy_tag_for_a_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1efc2269ee565e23b7be7b49e4fc0322_v3_1_3_0').validate(obj)
    return True


def update_a_specific_policy_tag_for_a_wireless_profile_v1(api):
    endpoint_result = api.wireless.update_a_specific_policy_tag_for_a_wireless_profile_v1(
        active_validation=True,
        apZones=['string'],
        id='string',
        payload=None,
        policyTagName='string',
        policy_tag_id='string',
        siteIds=['string']
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_a_specific_policy_tag_for_a_wireless_profile_v1(api, validator):
    try:
        assert is_valid_update_a_specific_policy_tag_for_a_wireless_profile_v1(
            validator,
            update_a_specific_policy_tag_for_a_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_a_specific_policy_tag_for_a_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.update_a_specific_policy_tag_for_a_wireless_profile_v1(
        active_validation=True,
        apZones=None,
        id='string',
        payload=None,
        policyTagName=None,
        policy_tag_id='string',
        siteIds=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_a_specific_policy_tag_for_a_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_update_a_specific_policy_tag_for_a_wireless_profile_v1(
            validator,
            update_a_specific_policy_tag_for_a_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_specific_policy_tag_for_a_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d80aa0ad4b8b57a4b6aca2ed2e6ff240_v3_1_3_0').validate(obj)
    return True


def retrieve_a_specific_policy_tag_for_a_wireless_profile_v1(api):
    endpoint_result = api.wireless.retrieve_a_specific_policy_tag_for_a_wireless_profile_v1(
        id='string',
        policy_tag_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_a_specific_policy_tag_for_a_wireless_profile_v1(api, validator):
    try:
        assert is_valid_retrieve_a_specific_policy_tag_for_a_wireless_profile_v1(
            validator,
            retrieve_a_specific_policy_tag_for_a_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_specific_policy_tag_for_a_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.retrieve_a_specific_policy_tag_for_a_wireless_profile_v1(
        id='string',
        policy_tag_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_a_specific_policy_tag_for_a_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_specific_policy_tag_for_a_wireless_profile_v1(
            validator,
            retrieve_a_specific_policy_tag_for_a_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_all_site_tags_for_a_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3a13f7910d8f5359a8fc2f0eb1febd5b_v3_1_3_0').validate(obj)
    return True


def retrieve_all_site_tags_for_a_wireless_profile_v1(api):
    endpoint_result = api.wireless.retrieve_all_site_tags_for_a_wireless_profile_v1(
        id='string',
        limit=0,
        offset=0,
        site_tag_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_all_site_tags_for_a_wireless_profile_v1(api, validator):
    try:
        assert is_valid_retrieve_all_site_tags_for_a_wireless_profile_v1(
            validator,
            retrieve_all_site_tags_for_a_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_all_site_tags_for_a_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.retrieve_all_site_tags_for_a_wireless_profile_v1(
        id='string',
        limit=None,
        offset=None,
        site_tag_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_all_site_tags_for_a_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_all_site_tags_for_a_wireless_profile_v1(
            validator,
            retrieve_all_site_tags_for_a_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_multiple_site_tags_for_a_wireless_profile_in_bulk_v1(json_schema_validate, obj):
    json_schema_validate('jsd_40c6506b22335101a465d2adf5ca7f37_v3_1_3_0').validate(obj)
    return True


def create_multiple_site_tags_for_a_wireless_profile_in_bulk_v1(api):
    endpoint_result = api.wireless.create_multiple_site_tags_for_a_wireless_profile_in_bulk_v1(
        active_validation=True,
        id='string',
        items=[[{'siteIds': ['string'], 'siteTagName': 'string', 'flexProfileName': 'string', 'apProfileName': 'string'}]],
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_multiple_site_tags_for_a_wireless_profile_in_bulk_v1(api, validator):
    try:
        assert is_valid_create_multiple_site_tags_for_a_wireless_profile_in_bulk_v1(
            validator,
            create_multiple_site_tags_for_a_wireless_profile_in_bulk_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_multiple_site_tags_for_a_wireless_profile_in_bulk_v1_default_val(api):
    endpoint_result = api.wireless.create_multiple_site_tags_for_a_wireless_profile_in_bulk_v1(
        active_validation=True,
        id='string',
        items=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_multiple_site_tags_for_a_wireless_profile_in_bulk_v1_default_val(api, validator):
    try:
        assert is_valid_create_multiple_site_tags_for_a_wireless_profile_in_bulk_v1(
            validator,
            create_multiple_site_tags_for_a_wireless_profile_in_bulk_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_site_tags_for_a_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4762c49b712c551aabc676c8d3aefb02_v3_1_3_0').validate(obj)
    return True


def retrieve_the_count_of_site_tags_for_a_wireless_profile_v1(api):
    endpoint_result = api.wireless.retrieve_the_count_of_site_tags_for_a_wireless_profile_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_the_count_of_site_tags_for_a_wireless_profile_v1(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_site_tags_for_a_wireless_profile_v1(
            validator,
            retrieve_the_count_of_site_tags_for_a_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_site_tags_for_a_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.retrieve_the_count_of_site_tags_for_a_wireless_profile_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_the_count_of_site_tags_for_a_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_site_tags_for_a_wireless_profile_v1(
            validator,
            retrieve_the_count_of_site_tags_for_a_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_a_specific_site_tag_for_a_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7ba9e0f3a5db5972a55d4b3fcf2b5432_v3_1_3_0').validate(obj)
    return True


def update_a_specific_site_tag_for_a_wireless_profile_v1(api):
    endpoint_result = api.wireless.update_a_specific_site_tag_for_a_wireless_profile_v1(
        active_validation=True,
        apProfileName='string',
        flexProfileName='string',
        id='string',
        payload=None,
        siteIds=['string'],
        siteTagName='string',
        site_tag_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_a_specific_site_tag_for_a_wireless_profile_v1(api, validator):
    try:
        assert is_valid_update_a_specific_site_tag_for_a_wireless_profile_v1(
            validator,
            update_a_specific_site_tag_for_a_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_a_specific_site_tag_for_a_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.update_a_specific_site_tag_for_a_wireless_profile_v1(
        active_validation=True,
        apProfileName=None,
        flexProfileName=None,
        id='string',
        payload=None,
        siteIds=None,
        siteTagName=None,
        site_tag_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_a_specific_site_tag_for_a_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_update_a_specific_site_tag_for_a_wireless_profile_v1(
            validator,
            update_a_specific_site_tag_for_a_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_specific_site_tag_for_a_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4f29ee7d063e54c391da1a3e94b3b6a6_v3_1_3_0').validate(obj)
    return True


def retrieve_a_specific_site_tag_for_a_wireless_profile_v1(api):
    endpoint_result = api.wireless.retrieve_a_specific_site_tag_for_a_wireless_profile_v1(
        id='string',
        site_tag_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_a_specific_site_tag_for_a_wireless_profile_v1(api, validator):
    try:
        assert is_valid_retrieve_a_specific_site_tag_for_a_wireless_profile_v1(
            validator,
            retrieve_a_specific_site_tag_for_a_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_specific_site_tag_for_a_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.retrieve_a_specific_site_tag_for_a_wireless_profile_v1(
        id='string',
        site_tag_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_a_specific_site_tag_for_a_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_specific_site_tag_for_a_wireless_profile_v1(
            validator,
            retrieve_a_specific_site_tag_for_a_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_specific_site_tag_from_a_wireless_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_33797ffb265b5ca6b65a2dbc8faecbe3_v3_1_3_0').validate(obj)
    return True


def delete_a_specific_site_tag_from_a_wireless_profile_v1(api):
    endpoint_result = api.wireless.delete_a_specific_site_tag_from_a_wireless_profile_v1(
        id='string',
        site_tag_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_a_specific_site_tag_from_a_wireless_profile_v1(api, validator):
    try:
        assert is_valid_delete_a_specific_site_tag_from_a_wireless_profile_v1(
            validator,
            delete_a_specific_site_tag_from_a_wireless_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_specific_site_tag_from_a_wireless_profile_v1_default_val(api):
    endpoint_result = api.wireless.delete_a_specific_site_tag_from_a_wireless_profile_v1(
        id='string',
        site_tag_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_a_specific_site_tag_from_a_wireless_profile_v1_default_val(api, validator):
    try:
        assert is_valid_delete_a_specific_site_tag_from_a_wireless_profile_v1(
            validator,
            delete_a_specific_site_tag_from_a_wireless_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_anchor_group_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a5e4452cb2e05682933349833a01d14b_v3_1_3_0').validate(obj)
    return True


def create_anchor_group_v1(api):
    endpoint_result = api.wireless.create_anchor_group_v1(
        active_validation=True,
        anchorGroupName='string',
        mobilityAnchors=[{'deviceName': 'string', 'ipAddress': 'string', 'anchorPriority': 'string', 'managedAnchorWlc': True, 'peerDeviceType': 'string', 'macAddress': 'string', 'mobilityGroupName': 'string', 'privateIp': 'string'}],
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_anchor_group_v1(api, validator):
    try:
        assert is_valid_create_anchor_group_v1(
            validator,
            create_anchor_group_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_anchor_group_v1_default_val(api):
    endpoint_result = api.wireless.create_anchor_group_v1(
        active_validation=True,
        anchorGroupName=None,
        mobilityAnchors=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_anchor_group_v1_default_val(api, validator):
    try:
        assert is_valid_create_anchor_group_v1(
            validator,
            create_anchor_group_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_anchor_groups_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4e7c985b3fbe50f1a63ffe82180ae85f_v3_1_3_0').validate(obj)
    return True


def get_anchor_groups_v1(api):
    endpoint_result = api.wireless.get_anchor_groups_v1(
        limit='string',
        offset='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_anchor_groups_v1(api, validator):
    try:
        assert is_valid_get_anchor_groups_v1(
            validator,
            get_anchor_groups_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_anchor_groups_v1_default_val(api):
    endpoint_result = api.wireless.get_anchor_groups_v1(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_anchor_groups_v1_default_val(api, validator):
    try:
        assert is_valid_get_anchor_groups_v1(
            validator,
            get_anchor_groups_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_anchor_groups_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7d16bdccffaa5e0ba0e2c03a404065e1_v3_1_3_0').validate(obj)
    return True


def get_count_of_anchor_groups_v1(api):
    endpoint_result = api.wireless.get_count_of_anchor_groups_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_count_of_anchor_groups_v1(api, validator):
    try:
        assert is_valid_get_count_of_anchor_groups_v1(
            validator,
            get_count_of_anchor_groups_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_anchor_groups_v1_default_val(api):
    endpoint_result = api.wireless.get_count_of_anchor_groups_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_count_of_anchor_groups_v1_default_val(api, validator):
    try:
        assert is_valid_get_count_of_anchor_groups_v1(
            validator,
            get_count_of_anchor_groups_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_anchor_group_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_964008e45188547287c882c1b01480bd_v3_1_3_0').validate(obj)
    return True


def get_anchor_group_by_id_v1(api):
    endpoint_result = api.wireless.get_anchor_group_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_anchor_group_by_id_v1(api, validator):
    try:
        assert is_valid_get_anchor_group_by_id_v1(
            validator,
            get_anchor_group_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_anchor_group_by_id_v1_default_val(api):
    endpoint_result = api.wireless.get_anchor_group_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_anchor_group_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_anchor_group_by_id_v1(
            validator,
            get_anchor_group_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_anchor_group_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ff2aeab6a8fe5355b362c848d94a3c88_v3_1_3_0').validate(obj)
    return True


def delete_anchor_group_by_id_v1(api):
    endpoint_result = api.wireless.delete_anchor_group_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_anchor_group_by_id_v1(api, validator):
    try:
        assert is_valid_delete_anchor_group_by_id_v1(
            validator,
            delete_anchor_group_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_anchor_group_by_id_v1_default_val(api):
    endpoint_result = api.wireless.delete_anchor_group_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_anchor_group_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_anchor_group_by_id_v1(
            validator,
            delete_anchor_group_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_anchor_group_v1(json_schema_validate, obj):
    json_schema_validate('jsd_093ecfe864dc5012ab9c25d23e2ce9f5_v3_1_3_0').validate(obj)
    return True


def update_anchor_group_v1(api):
    endpoint_result = api.wireless.update_anchor_group_v1(
        active_validation=True,
        anchorGroupName='string',
        id='string',
        mobilityAnchors=[{'deviceName': 'string', 'ipAddress': 'string', 'anchorPriority': 'string', 'managedAnchorWlc': True, 'peerDeviceType': 'string', 'macAddress': 'string', 'mobilityGroupName': 'string', 'privateIp': 'string'}],
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_anchor_group_v1(api, validator):
    try:
        assert is_valid_update_anchor_group_v1(
            validator,
            update_anchor_group_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_anchor_group_v1_default_val(api):
    endpoint_result = api.wireless.update_anchor_group_v1(
        active_validation=True,
        anchorGroupName=None,
        id='string',
        mobilityAnchors=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_anchor_group_v1_default_val(api, validator):
    try:
        assert is_valid_update_anchor_group_v1(
            validator,
            update_anchor_group_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ap_authorization_lists_v1(json_schema_validate, obj):
    json_schema_validate('jsd_56845e07df6057be8775b54b138e6e68_v3_1_3_0').validate(obj)
    return True


def get_ap_authorization_lists_v1(api):
    endpoint_result = api.wireless.get_ap_authorization_lists_v1(
        ap_authorization_list_name='string',
        limit='string',
        offset='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_authorization_lists_v1(api, validator):
    try:
        assert is_valid_get_ap_authorization_lists_v1(
            validator,
            get_ap_authorization_lists_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ap_authorization_lists_v1_default_val(api):
    endpoint_result = api.wireless.get_ap_authorization_lists_v1(
        ap_authorization_list_name=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_authorization_lists_v1_default_val(api, validator):
    try:
        assert is_valid_get_ap_authorization_lists_v1(
            validator,
            get_ap_authorization_lists_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_ap_authorization_list_v1(json_schema_validate, obj):
    json_schema_validate('jsd_bd400dbef41e53ed82541c766f14f1eb_v3_1_3_0').validate(obj)
    return True


def create_ap_authorization_list_v1(api):
    endpoint_result = api.wireless.create_ap_authorization_list_v1(
        active_validation=True,
        apAuthorizationListName='string',
        localAuthorization={'apMacEntries': ['string'], 'apSerialNumberEntries': ['string']},
        payload=None,
        remoteAuthorization={'aaaServers': ['string'], 'authorizeApWithMac': True, 'authorizeApWithSerialNumber': True}
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_ap_authorization_list_v1(api, validator):
    try:
        assert is_valid_create_ap_authorization_list_v1(
            validator,
            create_ap_authorization_list_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_ap_authorization_list_v1_default_val(api):
    endpoint_result = api.wireless.create_ap_authorization_list_v1(
        active_validation=True,
        apAuthorizationListName=None,
        localAuthorization=None,
        payload=None,
        remoteAuthorization=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_ap_authorization_list_v1_default_val(api, validator):
    try:
        assert is_valid_create_ap_authorization_list_v1(
            validator,
            create_ap_authorization_list_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ap_authorization_list_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6281dbb918195bc3a42c095abc5e37fc_v3_1_3_0').validate(obj)
    return True


def get_ap_authorization_list_count_v1(api):
    endpoint_result = api.wireless.get_ap_authorization_list_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_authorization_list_count_v1(api, validator):
    try:
        assert is_valid_get_ap_authorization_list_count_v1(
            validator,
            get_ap_authorization_list_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ap_authorization_list_count_v1_default_val(api):
    endpoint_result = api.wireless.get_ap_authorization_list_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_authorization_list_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_ap_authorization_list_count_v1(
            validator,
            get_ap_authorization_list_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_ap_authorization_list_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0b0a5d8bc0a15df3a53fa81743b965a1_v3_1_3_0').validate(obj)
    return True


def delete_ap_authorization_list_v1(api):
    endpoint_result = api.wireless.delete_ap_authorization_list_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_ap_authorization_list_v1(api, validator):
    try:
        assert is_valid_delete_ap_authorization_list_v1(
            validator,
            delete_ap_authorization_list_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_ap_authorization_list_v1_default_val(api):
    endpoint_result = api.wireless.delete_ap_authorization_list_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_ap_authorization_list_v1_default_val(api, validator):
    try:
        assert is_valid_delete_ap_authorization_list_v1(
            validator,
            delete_ap_authorization_list_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_ap_authorization_list_v1(json_schema_validate, obj):
    json_schema_validate('jsd_84e55cca88065707a6f812a679f69a5d_v3_1_3_0').validate(obj)
    return True


def update_ap_authorization_list_v1(api):
    endpoint_result = api.wireless.update_ap_authorization_list_v1(
        active_validation=True,
        apAuthorizationListName='string',
        id='string',
        localAuthorization={'apMacEntries': ['string'], 'apSerialNumberEntries': ['string']},
        payload=None,
        remoteAuthorization={'aaaServers': ['string'], 'authorizeApWithMac': True, 'authorizeApWithSerialNumber': True}
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_ap_authorization_list_v1(api, validator):
    try:
        assert is_valid_update_ap_authorization_list_v1(
            validator,
            update_ap_authorization_list_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_ap_authorization_list_v1_default_val(api):
    endpoint_result = api.wireless.update_ap_authorization_list_v1(
        active_validation=True,
        apAuthorizationListName=None,
        id='string',
        localAuthorization=None,
        payload=None,
        remoteAuthorization=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_ap_authorization_list_v1_default_val(api, validator):
    try:
        assert is_valid_update_ap_authorization_list_v1(
            validator,
            update_ap_authorization_list_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ap_authorization_list_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ca771ed49fa45c4cb7402bbb76f0d63d_v3_1_3_0').validate(obj)
    return True


def get_ap_authorization_list_by_id_v1(api):
    endpoint_result = api.wireless.get_ap_authorization_list_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_authorization_list_by_id_v1(api, validator):
    try:
        assert is_valid_get_ap_authorization_list_by_id_v1(
            validator,
            get_ap_authorization_list_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ap_authorization_list_by_id_v1_default_val(api):
    endpoint_result = api.wireless.get_ap_authorization_list_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_authorization_list_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_ap_authorization_list_by_id_v1(
            validator,
            get_ap_authorization_list_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_ap_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a0f799d5ec6954d1bd7a25853080a9f1_v3_1_3_0').validate(obj)
    return True


def create_ap_profile_v1(api):
    endpoint_result = api.wireless.create_ap_profile_v1(
        active_validation=True,
        apPowerProfileName='string',
        apProfileName='string',
        awipsEnabled=True,
        awipsForensicEnabled=True,
        calendarPowerProfiles={'powerProfileName': 'string', 'schedulerType': 'string', 'duration': {'schedulerStartTime': 'string', 'schedulerEndTime': 'string', 'schedulerDay': ['string'], 'schedulerDate': ['string']}},
        clientLimit=0,
        countryCode='string',
        description='string',
        managementSetting={'authType': 'string', 'dot1xUsername': 'string', 'dot1xPassword': 'string', 'sshEnabled': True, 'telnetEnabled': True, 'managementUserName': 'string', 'managementPassword': 'string', 'managementEnablePassword': 'string', 'cdpState': True},
        meshEnabled=True,
        meshSetting={'bridgeGroupName': 'string', 'backhaulClientAccess': True, 'range': 0, 'ghz5BackhaulDataRates': 'string', 'ghz24BackhaulDataRates': 'string', 'rapDownlinkBackhaul': 'string'},
        payload=None,
        pmfDenialEnabled=True,
        remoteWorkerEnabled=True,
        rogueDetectionSetting={'rogueDetection': True, 'rogueDetectionMinRssi': 0, 'rogueDetectionTransientInterval': 0, 'rogueDetectionReportInterval': 0},
        timeZone='string',
        timeZoneOffsetHour=0,
        timeZoneOffsetMinutes=0
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_ap_profile_v1(api, validator):
    try:
        assert is_valid_create_ap_profile_v1(
            validator,
            create_ap_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_ap_profile_v1_default_val(api):
    endpoint_result = api.wireless.create_ap_profile_v1(
        active_validation=True,
        apPowerProfileName=None,
        apProfileName=None,
        awipsEnabled=None,
        awipsForensicEnabled=None,
        calendarPowerProfiles=None,
        clientLimit=None,
        countryCode=None,
        description=None,
        managementSetting=None,
        meshEnabled=None,
        meshSetting=None,
        payload=None,
        pmfDenialEnabled=None,
        remoteWorkerEnabled=None,
        rogueDetectionSetting=None,
        timeZone=None,
        timeZoneOffsetHour=None,
        timeZoneOffsetMinutes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_ap_profile_v1_default_val(api, validator):
    try:
        assert is_valid_create_ap_profile_v1(
            validator,
            create_ap_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ap_profiles_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3bfbdf9349a35ef5bd4ef3ee9dfafcc8_v3_1_3_0').validate(obj)
    return True


def get_ap_profiles_v1(api):
    endpoint_result = api.wireless.get_ap_profiles_v1(
        ap_profile_name='string',
        limit='string',
        offset='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_profiles_v1(api, validator):
    try:
        assert is_valid_get_ap_profiles_v1(
            validator,
            get_ap_profiles_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ap_profiles_v1_default_val(api):
    endpoint_result = api.wireless.get_ap_profiles_v1(
        ap_profile_name=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_profiles_v1_default_val(api, validator):
    try:
        assert is_valid_get_ap_profiles_v1(
            validator,
            get_ap_profiles_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ap_profiles_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0b5a1e426fa455e2a07d80a65a03db57_v3_1_3_0').validate(obj)
    return True


def get_ap_profiles_count_v1(api):
    endpoint_result = api.wireless.get_ap_profiles_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_profiles_count_v1(api, validator):
    try:
        assert is_valid_get_ap_profiles_count_v1(
            validator,
            get_ap_profiles_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ap_profiles_count_v1_default_val(api):
    endpoint_result = api.wireless.get_ap_profiles_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_profiles_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_ap_profiles_count_v1(
            validator,
            get_ap_profiles_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_ap_profile_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fe43f12f8092513cba2344d43987cb57_v3_1_3_0').validate(obj)
    return True


def delete_ap_profile_by_id_v1(api):
    endpoint_result = api.wireless.delete_ap_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_ap_profile_by_id_v1(api, validator):
    try:
        assert is_valid_delete_ap_profile_by_id_v1(
            validator,
            delete_ap_profile_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_ap_profile_by_id_v1_default_val(api):
    endpoint_result = api.wireless.delete_ap_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_ap_profile_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_ap_profile_by_id_v1(
            validator,
            delete_ap_profile_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_ap_profile_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4798b42a01655325be161ab2ad60aa68_v3_1_3_0').validate(obj)
    return True


def update_ap_profile_by_id_v1(api):
    endpoint_result = api.wireless.update_ap_profile_by_id_v1(
        active_validation=True,
        apPowerProfileName='string',
        apProfileName='string',
        awipsEnabled=True,
        awipsForensicEnabled=True,
        calendarPowerProfiles={'powerProfileName': 'string', 'schedulerType': 'string', 'duration': {'schedulerStartTime': 'string', 'schedulerEndTime': 'string', 'schedulerDay': ['string'], 'schedulerDate': ['string']}},
        clientLimit=0,
        countryCode='string',
        description='string',
        id='string',
        managementSetting={'authType': 'string', 'dot1xUsername': 'string', 'dot1xPassword': 'string', 'sshEnabled': True, 'telnetEnabled': True, 'managementUserName': 'string', 'managementPassword': 'string', 'managementEnablePassword': 'string', 'cdpState': True},
        meshEnabled=True,
        meshSetting={'bridgeGroupName': 'string', 'backhaulClientAccess': True, 'range': 0, 'ghz5BackhaulDataRates': 'string', 'ghz24BackhaulDataRates': 'string', 'rapDownlinkBackhaul': 'string'},
        payload=None,
        pmfDenialEnabled=True,
        remoteWorkerEnabled=True,
        rogueDetectionSetting={'rogueDetection': True, 'rogueDetectionMinRssi': 0, 'rogueDetectionTransientInterval': 0, 'rogueDetectionReportInterval': 0},
        timeZone='string',
        timeZoneOffsetHour=0,
        timeZoneOffsetMinutes=0
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_ap_profile_by_id_v1(api, validator):
    try:
        assert is_valid_update_ap_profile_by_id_v1(
            validator,
            update_ap_profile_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_ap_profile_by_id_v1_default_val(api):
    endpoint_result = api.wireless.update_ap_profile_by_id_v1(
        active_validation=True,
        apPowerProfileName=None,
        apProfileName=None,
        awipsEnabled=None,
        awipsForensicEnabled=None,
        calendarPowerProfiles=None,
        clientLimit=None,
        countryCode=None,
        description=None,
        id='string',
        managementSetting=None,
        meshEnabled=None,
        meshSetting=None,
        payload=None,
        pmfDenialEnabled=None,
        remoteWorkerEnabled=None,
        rogueDetectionSetting=None,
        timeZone=None,
        timeZoneOffsetHour=None,
        timeZoneOffsetMinutes=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_ap_profile_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_update_ap_profile_by_id_v1(
            validator,
            update_ap_profile_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ap_profile_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6097c9969e72561da513d74a8fecbaff_v3_1_3_0').validate(obj)
    return True


def get_ap_profile_by_id_v1(api):
    endpoint_result = api.wireless.get_ap_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_profile_by_id_v1(api, validator):
    try:
        assert is_valid_get_ap_profile_by_id_v1(
            validator,
            get_ap_profile_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ap_profile_by_id_v1_default_val(api):
    endpoint_result = api.wireless.get_ap_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_ap_profile_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_ap_profile_by_id_v1(
            validator,
            get_ap_profile_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get80211be_profiles_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f2b94a700f80548694685475590d5e0b_v3_1_3_0').validate(obj)
    return True


def get80211be_profiles_v1(api):
    endpoint_result = api.wireless.get80211be_profiles_v1(
        is_mu_mimo_down_link=True,
        is_mu_mimo_up_link=True,
        is_of_dma_down_link=True,
        is_of_dma_multi_ru=True,
        is_of_dma_up_link=True,
        limit=0,
        offset=0,
        profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get80211be_profiles_v1(api, validator):
    try:
        assert is_valid_get80211be_profiles_v1(
            validator,
            get80211be_profiles_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get80211be_profiles_v1_default_val(api):
    endpoint_result = api.wireless.get80211be_profiles_v1(
        is_mu_mimo_down_link=None,
        is_mu_mimo_up_link=None,
        is_of_dma_down_link=None,
        is_of_dma_multi_ru=None,
        is_of_dma_up_link=None,
        limit=None,
        offset=None,
        profile_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get80211be_profiles_v1_default_val(api, validator):
    try:
        assert is_valid_get80211be_profiles_v1(
            validator,
            get80211be_profiles_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_a80211be_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f08eb586113e597a91b1658297570934_v3_1_3_0').validate(obj)
    return True


def create_a80211be_profile_v1(api):
    endpoint_result = api.wireless.create_a80211be_profile_v1(
        active_validation=True,
        muMimoDownLink=True,
        muMimoUpLink=True,
        ofdmaDownLink=True,
        ofdmaMultiRu=True,
        ofdmaUpLink=True,
        payload=None,
        profileName='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_a80211be_profile_v1(api, validator):
    try:
        assert is_valid_create_a80211be_profile_v1(
            validator,
            create_a80211be_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_a80211be_profile_v1_default_val(api):
    endpoint_result = api.wireless.create_a80211be_profile_v1(
        active_validation=True,
        muMimoDownLink=None,
        muMimoUpLink=None,
        ofdmaDownLink=None,
        ofdmaMultiRu=None,
        ofdmaUpLink=None,
        payload=None,
        profileName=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_a80211be_profile_v1_default_val(api, validator):
    try:
        assert is_valid_create_a80211be_profile_v1(
            validator,
            create_a80211be_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get80211be_profiles_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_22b18962654b512e939285910448177d_v3_1_3_0').validate(obj)
    return True


def get80211be_profiles_count_v1(api):
    endpoint_result = api.wireless.get80211be_profiles_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get80211be_profiles_count_v1(api, validator):
    try:
        assert is_valid_get80211be_profiles_count_v1(
            validator,
            get80211be_profiles_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get80211be_profiles_count_v1_default_val(api):
    endpoint_result = api.wireless.get80211be_profiles_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get80211be_profiles_count_v1_default_val(api, validator):
    try:
        assert is_valid_get80211be_profiles_count_v1(
            validator,
            get80211be_profiles_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a80211be_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_9731f08862be5ba89b5c2f50aa30baa0_v3_1_3_0').validate(obj)
    return True


def delete_a80211be_profile_v1(api):
    endpoint_result = api.wireless.delete_a80211be_profile_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_a80211be_profile_v1(api, validator):
    try:
        assert is_valid_delete_a80211be_profile_v1(
            validator,
            delete_a80211be_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a80211be_profile_v1_default_val(api):
    endpoint_result = api.wireless.delete_a80211be_profile_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_a80211be_profile_v1_default_val(api, validator):
    try:
        assert is_valid_delete_a80211be_profile_v1(
            validator,
            delete_a80211be_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update80211be_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_890ef28900485c4e9842b4a68e483d4e_v3_1_3_0').validate(obj)
    return True


def update80211be_profile_v1(api):
    endpoint_result = api.wireless.update80211be_profile_v1(
        active_validation=True,
        id='string',
        muMimoDownLink=True,
        muMimoUpLink=True,
        ofdmaDownLink=True,
        ofdmaMultiRu=True,
        ofdmaUpLink=True,
        payload=None,
        profileName='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update80211be_profile_v1(api, validator):
    try:
        assert is_valid_update80211be_profile_v1(
            validator,
            update80211be_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update80211be_profile_v1_default_val(api):
    endpoint_result = api.wireless.update80211be_profile_v1(
        active_validation=True,
        id='string',
        muMimoDownLink=None,
        muMimoUpLink=None,
        ofdmaDownLink=None,
        ofdmaMultiRu=None,
        ofdmaUpLink=None,
        payload=None,
        profileName=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update80211be_profile_v1_default_val(api, validator):
    try:
        assert is_valid_update80211be_profile_v1(
            validator,
            update80211be_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get80211be_profile_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5ae9378f178355aea0e70e5ece0d430e_v3_1_3_0').validate(obj)
    return True


def get80211be_profile_by_id_v1(api):
    endpoint_result = api.wireless.get80211be_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get80211be_profile_by_id_v1(api, validator):
    try:
        assert is_valid_get80211be_profile_by_id_v1(
            validator,
            get80211be_profile_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get80211be_profile_by_id_v1_default_val(api):
    endpoint_result = api.wireless.get80211be_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get80211be_profile_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get80211be_profile_by_id_v1(
            validator,
            get80211be_profile_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interfaces_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8267d2c4823550d79e07dca86c2e8f66_v3_1_3_0').validate(obj)
    return True


def get_interfaces_v1(api):
    endpoint_result = api.wireless.get_interfaces_v1(
        interface_name='string',
        limit=0,
        offset=0,
        vlan_id=0
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_interfaces_v1(api, validator):
    try:
        assert is_valid_get_interfaces_v1(
            validator,
            get_interfaces_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interfaces_v1_default_val(api):
    endpoint_result = api.wireless.get_interfaces_v1(
        interface_name=None,
        limit=None,
        offset=None,
        vlan_id=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_interfaces_v1_default_val(api, validator):
    try:
        assert is_valid_get_interfaces_v1(
            validator,
            get_interfaces_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_interface_v1(json_schema_validate, obj):
    json_schema_validate('jsd_fb5e152d4d3d59f5afd92f717f3a1eea_v3_1_3_0').validate(obj)
    return True


def create_interface_v1(api):
    endpoint_result = api.wireless.create_interface_v1(
        active_validation=True,
        interfaceName='string',
        payload=None,
        vlanId=0
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_interface_v1(api, validator):
    try:
        assert is_valid_create_interface_v1(
            validator,
            create_interface_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_interface_v1_default_val(api):
    endpoint_result = api.wireless.create_interface_v1(
        active_validation=True,
        interfaceName=None,
        payload=None,
        vlanId=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_interface_v1_default_val(api, validator):
    try:
        assert is_valid_create_interface_v1(
            validator,
            create_interface_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_955feb0798215d52bbdab50542213d44_v3_1_3_0').validate(obj)
    return True


def get_interface_by_id_v1(api):
    endpoint_result = api.wireless.get_interface_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_interface_by_id_v1(api, validator):
    try:
        assert is_valid_get_interface_by_id_v1(
            validator,
            get_interface_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interface_by_id_v1_default_val(api):
    endpoint_result = api.wireless.get_interface_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_interface_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_interface_by_id_v1(
            validator,
            get_interface_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_interface_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0bdfaf07257c5a1190881ddd70dabf1b_v3_1_3_0').validate(obj)
    return True


def delete_interface_v1(api):
    endpoint_result = api.wireless.delete_interface_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_interface_v1(api, validator):
    try:
        assert is_valid_delete_interface_v1(
            validator,
            delete_interface_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_interface_v1_default_val(api):
    endpoint_result = api.wireless.delete_interface_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_interface_v1_default_val(api, validator):
    try:
        assert is_valid_delete_interface_v1(
            validator,
            delete_interface_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_interface_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8ee43cac5fd65c55ab3153d3549d18c0_v3_1_3_0').validate(obj)
    return True


def update_interface_v1(api):
    endpoint_result = api.wireless.update_interface_v1(
        active_validation=True,
        id='string',
        interfaceName='string',
        payload=None,
        vlanId=0
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_interface_v1(api, validator):
    try:
        assert is_valid_update_interface_v1(
            validator,
            update_interface_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_interface_v1_default_val(api):
    endpoint_result = api.wireless.update_interface_v1(
        active_validation=True,
        id='string',
        interfaceName=None,
        payload=None,
        vlanId=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_interface_v1_default_val(api, validator):
    try:
        assert is_valid_update_interface_v1(
            validator,
            update_interface_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_power_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1cc239fa9b185ecbab9e306289850a63_v3_1_3_0').validate(obj)
    return True


def create_power_profile_v1(api):
    endpoint_result = api.wireless.create_power_profile_v1(
        active_validation=True,
        description='string',
        payload=None,
        profileName='string',
        rules=[{'interfaceType': 'string', 'interfaceId': 'string', 'parameterType': 'string', 'parameterValue': 'string'}]
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_power_profile_v1(api, validator):
    try:
        assert is_valid_create_power_profile_v1(
            validator,
            create_power_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_power_profile_v1_default_val(api):
    endpoint_result = api.wireless.create_power_profile_v1(
        active_validation=True,
        description=None,
        payload=None,
        profileName=None,
        rules=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_power_profile_v1_default_val(api, validator):
    try:
        assert is_valid_create_power_profile_v1(
            validator,
            create_power_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_power_profiles_v1(json_schema_validate, obj):
    json_schema_validate('jsd_3ac4ba3554d259989ff8f52fc1ac8b7c_v3_1_3_0').validate(obj)
    return True


def get_power_profiles_v1(api):
    endpoint_result = api.wireless.get_power_profiles_v1(
        limit=0,
        offset=0,
        profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_power_profiles_v1(api, validator):
    try:
        assert is_valid_get_power_profiles_v1(
            validator,
            get_power_profiles_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_power_profiles_v1_default_val(api):
    endpoint_result = api.wireless.get_power_profiles_v1(
        limit=None,
        offset=None,
        profile_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_power_profiles_v1_default_val(api, validator):
    try:
        assert is_valid_get_power_profiles_v1(
            validator,
            get_power_profiles_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_power_profiles_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f71e461c251a5826a88c9eac7d4ed1c0_v3_1_3_0').validate(obj)
    return True


def get_power_profiles_count_v1(api):
    endpoint_result = api.wireless.get_power_profiles_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_power_profiles_count_v1(api, validator):
    try:
        assert is_valid_get_power_profiles_count_v1(
            validator,
            get_power_profiles_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_power_profiles_count_v1_default_val(api):
    endpoint_result = api.wireless.get_power_profiles_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_power_profiles_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_power_profiles_count_v1(
            validator,
            get_power_profiles_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_power_profile_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a82a74143e78550c93b8fcca1fea1041_v3_1_3_0').validate(obj)
    return True


def delete_power_profile_by_id_v1(api):
    endpoint_result = api.wireless.delete_power_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_power_profile_by_id_v1(api, validator):
    try:
        assert is_valid_delete_power_profile_by_id_v1(
            validator,
            delete_power_profile_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_power_profile_by_id_v1_default_val(api):
    endpoint_result = api.wireless.delete_power_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_power_profile_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_delete_power_profile_by_id_v1(
            validator,
            delete_power_profile_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_power_profile_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f0f7b6e1e4e159e7a40001fc3e649dfc_v3_1_3_0').validate(obj)
    return True


def update_power_profile_by_id_v1(api):
    endpoint_result = api.wireless.update_power_profile_by_id_v1(
        active_validation=True,
        description='string',
        id='string',
        payload=None,
        profileName='string',
        rules=[{'interfaceType': 'string', 'interfaceID': 'string', 'parameterType': 'string', 'parameterValue': 'string'}]
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_power_profile_by_id_v1(api, validator):
    try:
        assert is_valid_update_power_profile_by_id_v1(
            validator,
            update_power_profile_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_power_profile_by_id_v1_default_val(api):
    endpoint_result = api.wireless.update_power_profile_by_id_v1(
        active_validation=True,
        description=None,
        id='string',
        payload=None,
        profileName=None,
        rules=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_power_profile_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_update_power_profile_by_id_v1(
            validator,
            update_power_profile_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_power_profile_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_121ed0bc9ed852068ecb2addb8350220_v3_1_3_0').validate(obj)
    return True


def get_power_profile_by_id_v1(api):
    endpoint_result = api.wireless.get_power_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_power_profile_by_id_v1(api, validator):
    try:
        assert is_valid_get_power_profile_by_id_v1(
            validator,
            get_power_profile_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_power_profile_by_id_v1_default_val(api):
    endpoint_result = api.wireless.get_power_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_power_profile_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_power_profile_by_id_v1(
            validator,
            get_power_profile_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_rf_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4bcb1d489d735258975828f845df1769_v3_1_3_0').validate(obj)
    return True


def create_rf_profile_v1(api):
    endpoint_result = api.wireless.create_rf_profile_v1(
        active_validation=True,
        defaultRfProfile=True,
        enableRadioType6GHz=True,
        enableRadioTypeA=True,
        enableRadioTypeB=True,
        payload=None,
        radioType6GHzProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'powerThresholdV1': 0, 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0, 'enableStandardPowerService': True, 'multiBssidProperties': {'dot11axParameters': {'ofdmaDownLink': True, 'ofdmaUpLink': True, 'muMimoUpLink': True, 'muMimoDownLink': True}, 'dot11beParameters': {'ofdmaDownLink': True, 'ofdmaUpLink': True, 'muMimoUpLink': True, 'muMimoDownLink': True, 'ofdmaMultiRu': True}, 'targetWakeTime': True, 'twtBroadcastSupport': True}, 'preamblePuncture': True, 'minDbsWidth': 0, 'maxDbsWidth': 0, 'customRxSopThreshold': 0, 'maxRadioClients': 0, 'pscEnforcingEnabled': True, 'discoveryFrames6GHz': 'string', 'broadcastProbeResponseInterval': 0, 'fraPropertiesC': {'clientResetCount': 0, 'clientUtilizationThreshold': 0}, 'coverageHoleDetectionProperties': {'chdClientLevel': 0, 'chdDataRssiThreshold': 0, 'chdVoiceRssiThreshold': 0, 'chdExceptionLevel': 0}, 'spatialReuseProperties': {'dot11axNonSrgObssPacketDetect': True, 'dot11axNonSrgObssPacketDetectMaxThreshold': 0, 'dot11axSrgObssPacketDetect': True, 'dot11axSrgObssPacketDetectMinThreshold': 0, 'dot11axSrgObssPacketDetectMaxThreshold': 0}},
        radioTypeAProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'powerThresholdV1': 0, 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0, 'channelWidth': 'string', 'preamblePuncture': True, 'zeroWaitDfsEnable': True, 'customRxSopThreshold': 0, 'maxRadioClients': 0, 'fraPropertiesA': {'clientAware': True, 'clientSelect': 0, 'clientReset': 0}, 'coverageHoleDetectionProperties': {'chdClientLevel': 0, 'chdDataRssiThreshold': 0, 'chdVoiceRssiThreshold': 0, 'chdExceptionLevel': 0}, 'spatialReuseProperties': {'dot11axNonSrgObssPacketDetect': True, 'dot11axNonSrgObssPacketDetectMaxThreshold': 0, 'dot11axSrgObssPacketDetect': True, 'dot11axSrgObssPacketDetectMinThreshold': 0, 'dot11axSrgObssPacketDetectMaxThreshold': 0}},
        radioTypeBProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'powerThresholdV1': 0, 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0, 'customRxSopThreshold': 0, 'maxRadioClients': 0, 'coverageHoleDetectionProperties': {'chdClientLevel': 0, 'chdDataRssiThreshold': 0, 'chdVoiceRssiThreshold': 0, 'chdExceptionLevel': 0}, 'spatialReuseProperties': {'dot11axNonSrgObssPacketDetect': True, 'dot11axNonSrgObssPacketDetectMaxThreshold': 0, 'dot11axSrgObssPacketDetect': True, 'dot11axSrgObssPacketDetectMinThreshold': 0, 'dot11axSrgObssPacketDetectMaxThreshold': 0}},
        rfProfileName='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_rf_profile_v1(api, validator):
    try:
        assert is_valid_create_rf_profile_v1(
            validator,
            create_rf_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_rf_profile_v1_default_val(api):
    endpoint_result = api.wireless.create_rf_profile_v1(
        active_validation=True,
        defaultRfProfile=None,
        enableRadioType6GHz=None,
        enableRadioTypeA=None,
        enableRadioTypeB=None,
        payload=None,
        radioType6GHzProperties=None,
        radioTypeAProperties=None,
        radioTypeBProperties=None,
        rfProfileName=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_rf_profile_v1_default_val(api, validator):
    try:
        assert is_valid_create_rf_profile_v1(
            validator,
            create_rf_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_rf_profiles_v1(json_schema_validate, obj):
    json_schema_validate('jsd_26e11599ca71552e960dc2cdd182abb9_v3_1_3_0').validate(obj)
    return True


def get_rf_profiles_v1(api):
    endpoint_result = api.wireless.get_rf_profiles_v1(
        enable_radio_type6_g_hz=True,
        enable_radio_type_a=True,
        enable_radio_type_b=True,
        limit=0,
        offset=0,
        rf_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_rf_profiles_v1(api, validator):
    try:
        assert is_valid_get_rf_profiles_v1(
            validator,
            get_rf_profiles_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_rf_profiles_v1_default_val(api):
    endpoint_result = api.wireless.get_rf_profiles_v1(
        enable_radio_type6_g_hz=None,
        enable_radio_type_a=None,
        enable_radio_type_b=None,
        limit=None,
        offset=None,
        rf_profile_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_rf_profiles_v1_default_val(api, validator):
    try:
        assert is_valid_get_rf_profiles_v1(
            validator,
            get_rf_profiles_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_rf_profiles_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_25f91267d9ae54ae85b4ddad0b92a2dd_v3_1_3_0').validate(obj)
    return True


def get_rf_profiles_count_v1(api):
    endpoint_result = api.wireless.get_rf_profiles_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_rf_profiles_count_v1(api, validator):
    try:
        assert is_valid_get_rf_profiles_count_v1(
            validator,
            get_rf_profiles_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_rf_profiles_count_v1_default_val(api):
    endpoint_result = api.wireless.get_rf_profiles_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_rf_profiles_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_rf_profiles_count_v1(
            validator,
            get_rf_profiles_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_rf_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_dd7b861ab3e8520486d956a1a171dd63_v3_1_3_0').validate(obj)
    return True


def delete_rf_profile_v1(api):
    endpoint_result = api.wireless.delete_rf_profile_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_rf_profile_v1(api, validator):
    try:
        assert is_valid_delete_rf_profile_v1(
            validator,
            delete_rf_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_rf_profile_v1_default_val(api):
    endpoint_result = api.wireless.delete_rf_profile_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_rf_profile_v1_default_val(api, validator):
    try:
        assert is_valid_delete_rf_profile_v1(
            validator,
            delete_rf_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_rf_profile_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f59b09f4f1cb5b1c9ddb50e2b81815ef_v3_1_3_0').validate(obj)
    return True


def get_rf_profile_by_id_v1(api):
    endpoint_result = api.wireless.get_rf_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_rf_profile_by_id_v1(api, validator):
    try:
        assert is_valid_get_rf_profile_by_id_v1(
            validator,
            get_rf_profile_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_rf_profile_by_id_v1_default_val(api):
    endpoint_result = api.wireless.get_rf_profile_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_rf_profile_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_rf_profile_by_id_v1(
            validator,
            get_rf_profile_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_rf_profile_v1(json_schema_validate, obj):
    json_schema_validate('jsd_da455f4be5b75126ba9970c7cc54c7db_v3_1_3_0').validate(obj)
    return True


def update_rf_profile_v1(api):
    endpoint_result = api.wireless.update_rf_profile_v1(
        active_validation=True,
        defaultRfProfile=True,
        enableRadioType6GHz=True,
        enableRadioTypeA=True,
        enableRadioTypeB=True,
        id='string',
        payload=None,
        radioType6GHzProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'powerThresholdV1': 0, 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0, 'enableStandardPowerService': True, 'multiBssidProperties': {'dot11axParameters': {'ofdmaDownLink': True, 'ofdmaUpLink': True, 'muMimoUpLink': True, 'muMimoDownLink': True}, 'dot11beParameters': {'ofdmaDownLink': True, 'ofdmaUpLink': True, 'muMimoUpLink': True, 'muMimoDownLink': True, 'ofdmaMultiRu': True}, 'targetWakeTime': True, 'twtBroadcastSupport': True}, 'preamblePuncture': True, 'minDbsWidth': 0, 'maxDbsWidth': 0, 'customRxSopThreshold': 0, 'maxRadioClients': 0, 'pscEnforcingEnabled': True, 'discoveryFrames6GHz': 'string', 'broadcastProbeResponseInterval': 0, 'fraPropertiesC': {'clientResetCount': 0, 'clientUtilizationThreshold': 0}, 'coverageHoleDetectionProperties': {'chdClientLevel': 0, 'chdDataRssiThreshold': 0, 'chdVoiceRssiThreshold': 0, 'chdExceptionLevel': 0}, 'spatialReuseProperties': {'dot11axNonSrgObssPacketDetect': True, 'dot11axNonSrgObssPacketDetectMaxThreshold': 0, 'dot11axSrgObssPacketDetect': True, 'dot11axSrgObssPacketDetectMinThreshold': 0, 'dot11axSrgObssPacketDetectMaxThreshold': 0}},
        radioTypeAProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'powerThresholdV1': 0, 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0, 'channelWidth': 'string', 'preamblePuncture': True, 'zeroWaitDfsEnable': True, 'customRxSopThreshold': 0, 'maxRadioClients': 0, 'fraPropertiesA': {'clientAware': True, 'clientSelect': 0, 'clientReset': 0}, 'coverageHoleDetectionProperties': {'chdClientLevel': 0, 'chdDataRssiThreshold': 0, 'chdVoiceRssiThreshold': 0, 'chdExceptionLevel': 0}, 'spatialReuseProperties': {'dot11axNonSrgObssPacketDetect': True, 'dot11axNonSrgObssPacketDetectMaxThreshold': 0, 'dot11axSrgObssPacketDetect': True, 'dot11axSrgObssPacketDetectMinThreshold': 0, 'dot11axSrgObssPacketDetectMaxThreshold': 0}},
        radioTypeBProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'powerThresholdV1': 0, 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0, 'customRxSopThreshold': 0, 'maxRadioClients': 0, 'coverageHoleDetectionProperties': {'chdClientLevel': 0, 'chdDataRssiThreshold': 0, 'chdVoiceRssiThreshold': 0, 'chdExceptionLevel': 0}, 'spatialReuseProperties': {'dot11axNonSrgObssPacketDetect': True, 'dot11axNonSrgObssPacketDetectMaxThreshold': 0, 'dot11axSrgObssPacketDetect': True, 'dot11axSrgObssPacketDetectMinThreshold': 0, 'dot11axSrgObssPacketDetectMaxThreshold': 0}},
        rfProfileName='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_rf_profile_v1(api, validator):
    try:
        assert is_valid_update_rf_profile_v1(
            validator,
            update_rf_profile_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_rf_profile_v1_default_val(api):
    endpoint_result = api.wireless.update_rf_profile_v1(
        active_validation=True,
        defaultRfProfile=None,
        enableRadioType6GHz=None,
        enableRadioTypeA=None,
        enableRadioTypeB=None,
        id='string',
        payload=None,
        radioType6GHzProperties=None,
        radioTypeAProperties=None,
        radioTypeBProperties=None,
        rfProfileName=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_rf_profile_v1_default_val(api, validator):
    try:
        assert is_valid_update_rf_profile_v1(
            validator,
            update_rf_profile_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_sites_with_overridden_ssids_v1(json_schema_validate, obj):
    json_schema_validate('jsd_977d3c9ecf485c29b68497b7b6730e83_v3_1_3_0').validate(obj)
    return True


def retrieve_sites_with_overridden_ssids_v1(api):
    endpoint_result = api.wireless.retrieve_sites_with_overridden_ssids_v1(
        limit=0,
        offset=0,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_sites_with_overridden_ssids_v1(api, validator):
    try:
        assert is_valid_retrieve_sites_with_overridden_ssids_v1(
            validator,
            retrieve_sites_with_overridden_ssids_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_sites_with_overridden_ssids_v1_default_val(api):
    endpoint_result = api.wireless.retrieve_sites_with_overridden_ssids_v1(
        limit=None,
        offset=None,
        site_id=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_sites_with_overridden_ssids_v1_default_val(api, validator):
    try:
        assert is_valid_retrieve_sites_with_overridden_ssids_v1(
            validator,
            retrieve_sites_with_overridden_ssids_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_anchor_managed_ap_locations_for_w_l_c_v1(json_schema_validate, obj):
    json_schema_validate('jsd_327af893464e53d2abc8922f4f3310ea_v3_1_3_0').validate(obj)
    return True


def assign_anchor_managed_ap_locations_for_w_l_c_v1(api):
    endpoint_result = api.wireless.assign_anchor_managed_ap_locations_for_w_l_c_v1(
        active_validation=True,
        anchorManagedAPLocationsSiteIds=['string'],
        network_device_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_assign_anchor_managed_ap_locations_for_w_l_c_v1(api, validator):
    try:
        assert is_valid_assign_anchor_managed_ap_locations_for_w_l_c_v1(
            validator,
            assign_anchor_managed_ap_locations_for_w_l_c_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def assign_anchor_managed_ap_locations_for_w_l_c_v1_default_val(api):
    endpoint_result = api.wireless.assign_anchor_managed_ap_locations_for_w_l_c_v1(
        active_validation=True,
        anchorManagedAPLocationsSiteIds=None,
        network_device_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_assign_anchor_managed_ap_locations_for_w_l_c_v1_default_val(api, validator):
    try:
        assert is_valid_assign_anchor_managed_ap_locations_for_w_l_c_v1(
            validator,
            assign_anchor_managed_ap_locations_for_w_l_c_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_configure_access_points_v2(json_schema_validate, obj):
    json_schema_validate('jsd_deb34387d0235811a90985711be9fe2e_v3_1_3_0').validate(obj)
    return True


def configure_access_points_v2(api):
    endpoint_result = api.wireless.configure_access_points_v2(
        active_validation=True,
        adminStatus=True,
        apList=[{'apName': 'string', 'macAddress': 'string', 'apNameNew': 'string'}],
        apMode=0,
        cleanAirSI24=True,
        cleanAirSI5=True,
        cleanAirSI6=True,
        configureAdminStatus=True,
        configureApMode=True,
        configureCleanAirSI24Ghz=True,
        configureCleanAirSI5Ghz=True,
        configureCleanAirSI6Ghz=True,
        configureFailoverPriority=True,
        configureHAController=True,
        configureLedBrightnessLevel=True,
        configureLedStatus=True,
        configureLocation=True,
        failoverPriority=0,
        isAssignedSiteAsLocation=True,
        ledBrightnessLevel=0,
        ledStatus=True,
        location='string',
        payload=None,
        primaryControllerName='string',
        primaryIpAddress={'address': 'string'},
        radioConfigurations=[{'configureRadioRoleAssignment': True, 'radioRoleAssignment': 'string', 'radioBand': 'string', 'configureAdminStatus': True, 'adminStatus': True, 'configureAntennaPatternName': True, 'antennaPatternName': 'string', 'antennaGain': 0, 'configureAntennaCable': True, 'antennaCableName': 'string', 'cableLoss': 0, 'configureChannel': True, 'channelAssignmentMode': 0, 'channelNumber': 0, 'configureChannelWidth': True, 'channelWidth': 0, 'configurePower': True, 'powerAssignmentMode': 0, 'powerlevel': 0, 'radioType': 0}],
        secondaryControllerName='string',
        secondaryIpAddress={'address': 'string'},
        tertiaryControllerName='string',
        tertiaryIpAddress={'address': 'string'}
    )
    return endpoint_result


@pytest.mark.wireless
def test_configure_access_points_v2(api, validator):
    try:
        assert is_valid_configure_access_points_v2(
            validator,
            configure_access_points_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def configure_access_points_v2_default_val(api):
    endpoint_result = api.wireless.configure_access_points_v2(
        active_validation=True,
        adminStatus=None,
        apList=None,
        apMode=None,
        cleanAirSI24=None,
        cleanAirSI5=None,
        cleanAirSI6=None,
        configureAdminStatus=None,
        configureApMode=None,
        configureCleanAirSI24Ghz=None,
        configureCleanAirSI5Ghz=None,
        configureCleanAirSI6Ghz=None,
        configureFailoverPriority=None,
        configureHAController=None,
        configureLedBrightnessLevel=None,
        configureLedStatus=None,
        configureLocation=None,
        failoverPriority=None,
        isAssignedSiteAsLocation=None,
        ledBrightnessLevel=None,
        ledStatus=None,
        location=None,
        payload=None,
        primaryControllerName=None,
        primaryIpAddress=None,
        radioConfigurations=None,
        secondaryControllerName=None,
        secondaryIpAddress=None,
        tertiaryControllerName=None,
        tertiaryIpAddress=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_configure_access_points_v2_default_val(api, validator):
    try:
        assert is_valid_configure_access_points_v2(
            validator,
            configure_access_points_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interfaces_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0776936e2472592d96a069b246c26531_v3_1_3_0').validate(obj)
    return True


def get_interfaces_count_v1(api):
    endpoint_result = api.wireless.get_interfaces_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_interfaces_count_v1(api, validator):
    try:
        assert is_valid_get_interfaces_count_v1(
            validator,
            get_interfaces_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_interfaces_count_v1_default_val(api):
    endpoint_result = api.wireless.get_interfaces_count_v1(

    )
    return endpoint_result


@pytest.mark.wireless
def test_get_interfaces_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_interfaces_count_v1(
            validator,
            get_interfaces_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

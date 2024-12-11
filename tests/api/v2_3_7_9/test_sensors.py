# -*- coding: utf-8 -*-
"""CatalystCenterAPI sensors API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.9', reason='version does not match')


def is_valid_lists_i_cap_packet_capture_files_matching_specified_criteria_v1(json_schema_validate, obj):
    json_schema_validate('jsd_272dbaeabc535e1a8587c92b593cefc3_v2_3_7_9').validate(obj)
    return True


def lists_i_cap_packet_capture_files_matching_specified_criteria_v1(api):
    endpoint_result = api.sensors.lists_i_cap_packet_capture_files_matching_specified_criteria_v1(
        ap_mac='string',
        client_mac='string',
        end_time=0,
        limit=0,
        offset=0,
        order='string',
        sort_by='string',
        start_time=0,
        type='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_lists_i_cap_packet_capture_files_matching_specified_criteria_v1(api, validator):
    try:
        assert is_valid_lists_i_cap_packet_capture_files_matching_specified_criteria_v1(
            validator,
            lists_i_cap_packet_capture_files_matching_specified_criteria_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lists_i_cap_packet_capture_files_matching_specified_criteria_v1_default_val(api):
    endpoint_result = api.sensors.lists_i_cap_packet_capture_files_matching_specified_criteria_v1(
        ap_mac=None,
        client_mac=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        start_time=None,
        type=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_lists_i_cap_packet_capture_files_matching_specified_criteria_v1_default_val(api, validator):
    try:
        assert is_valid_lists_i_cap_packet_capture_files_matching_specified_criteria_v1(
            validator,
            lists_i_cap_packet_capture_files_matching_specified_criteria_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria_v1(json_schema_validate, obj):
    json_schema_validate('jsd_cbb6ff54e6605629a0a8a3555be72613_v2_3_7_9').validate(obj)
    return True


def retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria_v1(api):
    endpoint_result = api.sensors.retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria_v1(
        ap_mac='string',
        client_mac='string',
        end_time=0,
        start_time=0,
        type='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria_v1(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria_v1(
            validator,
            retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria_v1_default_val(api):
    endpoint_result = api.sensors.retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria_v1(
        ap_mac=None,
        client_mac=None,
        end_time=None,
        start_time=None,
        type=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria_v1(
            validator,
            retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_details_of_a_specific_i_cap_packet_capture_file_v1(json_schema_validate, obj):
    json_schema_validate('jsd_be18fdce21365e3ab6833963fefbaa96_v2_3_7_9').validate(obj)
    return True


def retrieves_details_of_a_specific_i_cap_packet_capture_file_v1(api):
    endpoint_result = api.sensors.retrieves_details_of_a_specific_i_cap_packet_capture_file_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_details_of_a_specific_i_cap_packet_capture_file_v1(api, validator):
    try:
        assert is_valid_retrieves_details_of_a_specific_i_cap_packet_capture_file_v1(
            validator,
            retrieves_details_of_a_specific_i_cap_packet_capture_file_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_details_of_a_specific_i_cap_packet_capture_file_v1_default_val(api):
    endpoint_result = api.sensors.retrieves_details_of_a_specific_i_cap_packet_capture_file_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_details_of_a_specific_i_cap_packet_capture_file_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_details_of_a_specific_i_cap_packet_capture_file_v1(
            validator,
            retrieves_details_of_a_specific_i_cap_packet_capture_file_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_downloads_a_specific_i_cap_packet_capture_file_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8aeb8cee149c55a4a49506e07b6c4385_v2_3_7_9').validate(obj)
    return True


def downloads_a_specific_i_cap_packet_capture_file_v1(api):
    endpoint_result = api.sensors.downloads_a_specific_i_cap_packet_capture_file_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_downloads_a_specific_i_cap_packet_capture_file_v1(api, validator):
    try:
        assert is_valid_downloads_a_specific_i_cap_packet_capture_file_v1(
            validator,
            downloads_a_specific_i_cap_packet_capture_file_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def downloads_a_specific_i_cap_packet_capture_file_v1_default_val(api):
    endpoint_result = api.sensors.downloads_a_specific_i_cap_packet_capture_file_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_downloads_a_specific_i_cap_packet_capture_file_v1_default_val(api, validator):
    try:
        assert is_valid_downloads_a_specific_i_cap_packet_capture_file_v1(
            validator,
            downloads_a_specific_i_cap_packet_capture_file_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_specific_client_statistics_over_specified_period_of_time_v1(json_schema_validate, obj):
    json_schema_validate('jsd_04cca68e89d0545dac01a8c7a461ac6e_v2_3_7_9').validate(obj)
    return True


def retrieves_specific_client_statistics_over_specified_period_of_time_v1(api):
    endpoint_result = api.sensors.retrieves_specific_client_statistics_over_specified_period_of_time_v1(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 0}],
        id='string',
        page={'limit': 0, 'offset': 0, 'timeSortOrder': 'string'},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_specific_client_statistics_over_specified_period_of_time_v1(api, validator):
    try:
        assert is_valid_retrieves_specific_client_statistics_over_specified_period_of_time_v1(
            validator,
            retrieves_specific_client_statistics_over_specified_period_of_time_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_specific_client_statistics_over_specified_period_of_time_v1_default_val(api):
    endpoint_result = api.sensors.retrieves_specific_client_statistics_over_specified_period_of_time_v1(
        active_validation=True,
        endTime=None,
        filters=None,
        id='string',
        page=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_specific_client_statistics_over_specified_period_of_time_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_specific_client_statistics_over_specified_period_of_time_v1(
            validator,
            retrieves_specific_client_statistics_over_specified_period_of_time_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_specific_radio_statistics_over_specified_period_of_time_v1(json_schema_validate, obj):
    json_schema_validate('jsd_46733f71d0b2527b8cd13123f9a68cf3_v2_3_7_9').validate(obj)
    return True


def retrieves_specific_radio_statistics_over_specified_period_of_time_v1(api):
    endpoint_result = api.sensors.retrieves_specific_radio_statistics_over_specified_period_of_time_v1(
        active_validation=True,
        endTime=0,
        filters=[{'key': 'string', 'operator': 'string', 'value': 0}],
        id='string',
        page={'limit': 0, 'offset': 0, 'timeSortOrder': 'string'},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_specific_radio_statistics_over_specified_period_of_time_v1(api, validator):
    try:
        assert is_valid_retrieves_specific_radio_statistics_over_specified_period_of_time_v1(
            validator,
            retrieves_specific_radio_statistics_over_specified_period_of_time_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_specific_radio_statistics_over_specified_period_of_time_v1_default_val(api):
    endpoint_result = api.sensors.retrieves_specific_radio_statistics_over_specified_period_of_time_v1(
        active_validation=True,
        endTime=None,
        filters=None,
        id='string',
        page=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_specific_radio_statistics_over_specified_period_of_time_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_specific_radio_statistics_over_specified_period_of_time_v1(
            validator,
            retrieves_specific_radio_statistics_over_specified_period_of_time_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_spectrum_interference_devices_reports_sent_by_w_l_c_for_provided_ap_mac_v1(json_schema_validate, obj):
    json_schema_validate('jsd_20d1233df7e65d6b93c17b6568a9be4f_v2_3_7_9').validate(obj)
    return True


def retrieves_the_spectrum_interference_devices_reports_sent_by_w_l_c_for_provided_ap_mac_v1(api):
    endpoint_result = api.sensors.retrieves_the_spectrum_interference_devices_reports_sent_by_w_l_c_for_provided_ap_mac_v1(
        ap_mac='string',
        end_time=0,
        limit=0,
        offset=0,
        start_time=0,
        time_sort_order='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_the_spectrum_interference_devices_reports_sent_by_w_l_c_for_provided_ap_mac_v1(api, validator):
    try:
        assert is_valid_retrieves_the_spectrum_interference_devices_reports_sent_by_w_l_c_for_provided_ap_mac_v1(
            validator,
            retrieves_the_spectrum_interference_devices_reports_sent_by_w_l_c_for_provided_ap_mac_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_spectrum_interference_devices_reports_sent_by_w_l_c_for_provided_ap_mac_v1_default_val(api):
    endpoint_result = api.sensors.retrieves_the_spectrum_interference_devices_reports_sent_by_w_l_c_for_provided_ap_mac_v1(
        ap_mac=None,
        end_time=None,
        limit=None,
        offset=None,
        start_time=None,
        time_sort_order=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_the_spectrum_interference_devices_reports_sent_by_w_l_c_for_provided_ap_mac_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_spectrum_interference_devices_reports_sent_by_w_l_c_for_provided_ap_mac_v1(
            validator,
            retrieves_the_spectrum_interference_devices_reports_sent_by_w_l_c_for_provided_ap_mac_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_spectrum_sensor_reports_sent_by_w_l_c_for_provided_ap_mac_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1ba6a51cf3055d0da0ba65e43b3030b6_v2_3_7_9').validate(obj)
    return True


def retrieves_the_spectrum_sensor_reports_sent_by_w_l_c_for_provided_ap_mac_v1(api):
    endpoint_result = api.sensors.retrieves_the_spectrum_sensor_reports_sent_by_w_l_c_for_provided_ap_mac_v1(
        ap_mac='string',
        data_type=0,
        end_time=0,
        limit=0,
        offset=0,
        start_time=0,
        time_sort_order='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_the_spectrum_sensor_reports_sent_by_w_l_c_for_provided_ap_mac_v1(api, validator):
    try:
        assert is_valid_retrieves_the_spectrum_sensor_reports_sent_by_w_l_c_for_provided_ap_mac_v1(
            validator,
            retrieves_the_spectrum_sensor_reports_sent_by_w_l_c_for_provided_ap_mac_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_spectrum_sensor_reports_sent_by_w_l_c_for_provided_ap_mac_v1_default_val(api):
    endpoint_result = api.sensors.retrieves_the_spectrum_sensor_reports_sent_by_w_l_c_for_provided_ap_mac_v1(
        ap_mac=None,
        data_type=None,
        end_time=None,
        limit=None,
        offset=None,
        start_time=None,
        time_sort_order=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_the_spectrum_sensor_reports_sent_by_w_l_c_for_provided_ap_mac_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_spectrum_sensor_reports_sent_by_w_l_c_for_provided_ap_mac_v1(
            validator,
            retrieves_the_spectrum_sensor_reports_sent_by_w_l_c_for_provided_ap_mac_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_edit_sensor_test_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e2f9718de3d050819cdc6355a3a43200_v2_3_7_9').validate(obj)
    return True


def edit_sensor_test_template_v1(api):
    endpoint_result = api.sensors.edit_sensor_test_template_v1(
        _id='string',
        actionInProgress='string',
        active_validation=True,
        apCoverage=[{'bands': 'string', 'numberOfApsToTest': 0, 'rssiThreshold': 0}],
        connection='string',
        encryptionMode='string',
        frequency={'value': 0, 'unit': 'string'},
        lastModifiedTime=0,
        location='string',
        locationInfoList=[{'locationId': 'string', 'locationType': 'string', 'allSensors': True, 'siteHierarchy': 'string', 'macAddressList': ['string'], 'managementVlan': 'string', 'customManagementVlan': True}],
        modelVersion=0,
        name='string',
        numAssociatedSensor=0,
        numNeighborAPThreshold=0,
        payload=None,
        profiles=[{'authType': 'string', 'psk': 'string', 'username': 'string', 'password': 'string', 'passwordType': 'string', 'eapMethod': 'string', 'scep': True, 'authProtocol': 'string', 'certfilename': 'string', 'certxferprotocol': 'string', 'certstatus': 'string', 'certpassphrase': 'string', 'certdownloadurl': 'string', 'extWebAuthVirtualIp': 'string', 'extWebAuth': True, 'whiteList': True, 'extWebAuthPortal': 'string', 'extWebAuthAccessUrl': 'string', 'extWebAuthHtmlTag': [{'label': 'string', 'tag': 'string', 'value': 'string'}], 'qosPolicy': 'string', 'tests': [{'name': 'string', 'config': [{'domains': ['string'], 'server': 'string', 'userName': 'string', 'password': 'string', 'url': 'string', 'port': 0, 'protocol': 'string', 'servers': ['string'], 'direction': 'string', 'startPort': 0, 'endPort': 0, 'udpBandwidth': 0, 'probeType': 'string', 'numPackets': 0, 'pathToDownload': 'string', 'transferType': 'string', 'sharedSecret': 'string', 'ndtServer': 'string', 'ndtServerPort': 'string', 'ndtServerPath': 'string', 'uplinkTest': True, 'downlinkTest': True, 'proxyServer': 'string', 'proxyPort': 'string', 'proxyUserName': 'string', 'proxyPassword': 'string', 'userNamePrompt': 'string', 'passwordPrompt': 'string', 'exitCommand': 'string', 'finalPrompt': 'string'}]}], 'profileName': 'string', 'deviceType': 'string', 'vlan': 'string', 'locationVlanList': [{'locationId': 'string', 'vlans': ['string']}]}],
        radioAsSensorRemoved=True,
        rssiThreshold=0,
        runNow='string',
        scheduleInDays=0,
        sensors=[{'name': 'string', 'macAddress': 'string', 'switchMac': 'string', 'switchUuid': 'string', 'switchSerialNumber': 'string', 'markedForUninstall': True, 'ipAddress': 'string', 'hostName': 'string', 'wiredApplicationStatus': 'string', 'wiredApplicationMessage': 'string', 'assigned': True, 'status': 'string', 'xorSensor': True, 'targetAPs': ['string'], 'runNow': 'string', 'locationId': 'string', 'allSensorAddition': True, 'configUpdated': 'string', 'sensorType': 'string', 'testMacAddresses': {}, 'id': 'string', 'servicePolicy': 'string', 'iPerfInfo': {}}],
        showWlcUpgradeBanner=True,
        siteHierarchy='string',
        ssids=[{'bands': 'string', 'ssid': 'string', 'profileName': 'string', 'numAps': 0, 'numSensors': 0, 'layer3webAuthsecurity': 'string', 'layer3webAuthuserName': 'string', 'layer3webAuthpassword': 'string', 'layer3webAuthEmailAddress': 'string', 'thirdParty': {'selected': True}, 'id': 0, 'wlanId': 0, 'wlc': 'string', 'validFrom': 0, 'validTo': 0, 'status': 'string', 'proxyServer': 'string', 'proxyPort': 'string', 'proxyUserName': 'string', 'proxyPassword': 'string', 'authType': 'string', 'psk': 'string', 'username': 'string', 'password': 'string', 'passwordType': 'string', 'eapMethod': 'string', 'scep': True, 'authProtocol': 'string', 'certfilename': 'string', 'certxferprotocol': 'string', 'certstatus': 'string', 'certpassphrase': 'string', 'certdownloadurl': 'string', 'extWebAuthVirtualIp': 'string', 'extWebAuth': True, 'whiteList': True, 'extWebAuthPortal': 'string', 'extWebAuthAccessUrl': 'string', 'extWebAuthHtmlTag': [{'label': 'string', 'tag': 'string', 'value': 'string'}], 'qosPolicy': 'string', 'tests': [{'name': 'string', 'config': [{'domains': ['string'], 'server': 'string', 'userName': 'string', 'password': 'string', 'url': 'string', 'port': 0, 'protocol': 'string', 'servers': ['string'], 'direction': 'string', 'startPort': 0, 'endPort': 0, 'udpBandwidth': 0, 'probeType': 'string', 'numPackets': 0, 'pathToDownload': 'string', 'transferType': 'string', 'sharedSecret': 'string', 'ndtServer': 'string', 'ndtServerPort': 'string', 'ndtServerPath': 'string', 'uplinkTest': True, 'downlinkTest': True, 'proxyServer': 'string', 'proxyPort': 'string', 'proxyUserName': 'string', 'proxyPassword': 'string', 'userNamePrompt': 'string', 'passwordPrompt': 'string', 'exitCommand': 'string', 'finalPrompt': 'string'}]}]}],
        startTime=0,
        status='string',
        templateName='string',
        testScheduleMode='string',
        version=0,
        wlans=['string']
    )
    return endpoint_result


@pytest.mark.sensors
def test_edit_sensor_test_template_v1(api, validator):
    try:
        assert is_valid_edit_sensor_test_template_v1(
            validator,
            edit_sensor_test_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def edit_sensor_test_template_v1_default_val(api):
    endpoint_result = api.sensors.edit_sensor_test_template_v1(
        _id=None,
        actionInProgress=None,
        active_validation=True,
        apCoverage=None,
        connection=None,
        encryptionMode=None,
        frequency=None,
        lastModifiedTime=None,
        location=None,
        locationInfoList=None,
        modelVersion=None,
        name=None,
        numAssociatedSensor=None,
        numNeighborAPThreshold=None,
        payload=None,
        profiles=None,
        radioAsSensorRemoved=None,
        rssiThreshold=None,
        runNow=None,
        scheduleInDays=None,
        sensors=None,
        showWlcUpgradeBanner=None,
        siteHierarchy=None,
        ssids=None,
        startTime=None,
        status=None,
        templateName=None,
        testScheduleMode=None,
        version=None,
        wlans=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_edit_sensor_test_template_v1_default_val(api, validator):
    try:
        assert is_valid_edit_sensor_test_template_v1(
            validator,
            edit_sensor_test_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(json_schema_validate, obj):
    json_schema_validate('jsd_5620fdb9138f5aea88430fda95cbf865_v2_3_7_9').validate(obj)
    return True


def retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(api):
    endpoint_result = api.sensors.retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(
        apid='string',
        capture_status='string',
        capture_type='string',
        client_mac='string',
        limit=0,
        offset=0,
        wlc_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(api, validator):
    try:
        assert is_valid_retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(
            validator,
            retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering_v1_default_val(api):
    endpoint_result = api.sensors.retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(
        apid=None,
        capture_status=None,
        capture_type=None,
        client_mac=None,
        limit=None,
        offset=None,
        wlc_id=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(
            validator,
            retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_an_i_cap_configuration_intent_for_preview_approve_v1(json_schema_validate, obj):
    json_schema_validate('jsd_cb38886d0236502783d431455e3fb880_v2_3_7_9').validate(obj)
    return True


def creates_an_i_cap_configuration_intent_for_preview_approve_v1(api):
    endpoint_result = api.sensors.creates_an_i_cap_configuration_intent_for_preview_approve_v1(
        active_validation=True,
        payload=None,
        preview_description='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_creates_an_i_cap_configuration_intent_for_preview_approve_v1(api, validator):
    try:
        assert is_valid_creates_an_i_cap_configuration_intent_for_preview_approve_v1(
            validator,
            creates_an_i_cap_configuration_intent_for_preview_approve_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_an_i_cap_configuration_intent_for_preview_approve_v1_default_val(api):
    endpoint_result = api.sensors.creates_an_i_cap_configuration_intent_for_preview_approve_v1(
        active_validation=True,
        payload=None,
        preview_description=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_creates_an_i_cap_configuration_intent_for_preview_approve_v1_default_val(api, validator):
    try:
        assert is_valid_creates_an_i_cap_configuration_intent_for_preview_approve_v1(
            validator,
            creates_an_i_cap_configuration_intent_for_preview_approve_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_ai_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f924b4c27d18500b9b23df516b55c182_v2_3_7_9').validate(obj)
    return True


def creates_ai_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device_v1(api):
    endpoint_result = api.sensors.creates_ai_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device_v1(
        active_validation=True,
        id='string',
        object='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_creates_ai_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device_v1(api, validator):
    try:
        assert is_valid_creates_ai_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device_v1(
            validator,
            creates_ai_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_ai_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device_v1_default_val(api):
    endpoint_result = api.sensors.creates_ai_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device_v1(
        active_validation=True,
        id='string',
        object=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_creates_ai_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device_v1_default_val(api, validator):
    try:
        assert is_valid_creates_ai_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device_v1(
            validator,
            creates_ai_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_discards_the_i_cap_configuration_intent_by_activity_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_cd924ed4c4ed5fd3a463d5251896d31c_v2_3_7_9').validate(obj)
    return True


def discards_the_i_cap_configuration_intent_by_activity_id_v1(api):
    endpoint_result = api.sensors.discards_the_i_cap_configuration_intent_by_activity_id_v1(
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_discards_the_i_cap_configuration_intent_by_activity_id_v1(api, validator):
    try:
        assert is_valid_discards_the_i_cap_configuration_intent_by_activity_id_v1(
            validator,
            discards_the_i_cap_configuration_intent_by_activity_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def discards_the_i_cap_configuration_intent_by_activity_id_v1_default_val(api):
    endpoint_result = api.sensors.discards_the_i_cap_configuration_intent_by_activity_id_v1(
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_discards_the_i_cap_configuration_intent_by_activity_id_v1_default_val(api, validator):
    try:
        assert is_valid_discards_the_i_cap_configuration_intent_by_activity_id_v1(
            validator,
            discards_the_i_cap_configuration_intent_by_activity_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploys_the_i_cap_configuration_intent_by_activity_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_de1769e2886b5948b408100225b4a034_v2_3_7_9').validate(obj)
    return True


def deploys_the_i_cap_configuration_intent_by_activity_id_v1(api):
    endpoint_result = api.sensors.deploys_the_i_cap_configuration_intent_by_activity_id_v1(
        active_validation=True,
        object='string',
        payload=None,
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_deploys_the_i_cap_configuration_intent_by_activity_id_v1(api, validator):
    try:
        assert is_valid_deploys_the_i_cap_configuration_intent_by_activity_id_v1(
            validator,
            deploys_the_i_cap_configuration_intent_by_activity_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploys_the_i_cap_configuration_intent_by_activity_id_v1_default_val(api):
    endpoint_result = api.sensors.deploys_the_i_cap_configuration_intent_by_activity_id_v1(
        active_validation=True,
        object=None,
        payload=None,
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_deploys_the_i_cap_configuration_intent_by_activity_id_v1_default_val(api, validator):
    try:
        assert is_valid_deploys_the_i_cap_configuration_intent_by_activity_id_v1(
            validator,
            deploys_the_i_cap_configuration_intent_by_activity_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_i_cap_configuration_status_per_network_device_v1(json_schema_validate, obj):
    json_schema_validate('jsd_997c6f94fda3501dbb0055d06e71e025_v2_3_7_9').validate(obj)
    return True


def get_i_cap_configuration_status_per_network_device_v1(api):
    endpoint_result = api.sensors.get_i_cap_configuration_status_per_network_device_v1(
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_get_i_cap_configuration_status_per_network_device_v1(api, validator):
    try:
        assert is_valid_get_i_cap_configuration_status_per_network_device_v1(
            validator,
            get_i_cap_configuration_status_per_network_device_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_i_cap_configuration_status_per_network_device_v1_default_val(api):
    endpoint_result = api.sensors.get_i_cap_configuration_status_per_network_device_v1(
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_get_i_cap_configuration_status_per_network_device_v1_default_val(api, validator):
    try:
        assert is_valid_get_i_cap_configuration_status_per_network_device_v1(
            validator,
            get_i_cap_configuration_status_per_network_device_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_devices_clis_of_the_i_capintent_v1(json_schema_validate, obj):
    json_schema_validate('jsd_626f657ae3d75ecd87e97be0a1571923_v2_3_7_9').validate(obj)
    return True


def retrieves_the_devices_clis_of_the_i_capintent_v1(api):
    endpoint_result = api.sensors.retrieves_the_devices_clis_of_the_i_capintent_v1(
        network_device_id='string',
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_the_devices_clis_of_the_i_capintent_v1(api, validator):
    try:
        assert is_valid_retrieves_the_devices_clis_of_the_i_capintent_v1(
            validator,
            retrieves_the_devices_clis_of_the_i_capintent_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_devices_clis_of_the_i_capintent_v1_default_val(api):
    endpoint_result = api.sensors.retrieves_the_devices_clis_of_the_i_capintent_v1(
        network_device_id='string',
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_the_devices_clis_of_the_i_capintent_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_devices_clis_of_the_i_capintent_v1(
            validator,
            retrieves_the_devices_clis_of_the_i_capintent_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_generates_the_devices_clis_of_the_i_cap_configuration_intent_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7ac98aec39c95c2d97532514ee9b9f3e_v2_3_7_9').validate(obj)
    return True


def generates_the_devices_clis_of_the_i_cap_configuration_intent_v1(api):
    endpoint_result = api.sensors.generates_the_devices_clis_of_the_i_cap_configuration_intent_v1(
        active_validation=True,
        network_device_id='string',
        object='string',
        payload=None,
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_generates_the_devices_clis_of_the_i_cap_configuration_intent_v1(api, validator):
    try:
        assert is_valid_generates_the_devices_clis_of_the_i_cap_configuration_intent_v1(
            validator,
            generates_the_devices_clis_of_the_i_cap_configuration_intent_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def generates_the_devices_clis_of_the_i_cap_configuration_intent_v1_default_val(api):
    endpoint_result = api.sensors.generates_the_devices_clis_of_the_i_cap_configuration_intent_v1(
        active_validation=True,
        network_device_id='string',
        object=None,
        payload=None,
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_generates_the_devices_clis_of_the_i_cap_configuration_intent_v1_default_val(api, validator):
    try:
        assert is_valid_generates_the_devices_clis_of_the_i_cap_configuration_intent_v1(
            validator,
            generates_the_devices_clis_of_the_i_cap_configuration_intent_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(json_schema_validate, obj):
    json_schema_validate('jsd_1d122ab38d3758cba132f5e883d607c3_v2_3_7_9').validate(obj)
    return True


def retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(api):
    endpoint_result = api.sensors.retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(
        apid='string',
        capture_status='string',
        capture_type='string',
        client_mac='string',
        wlc_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(
            validator,
            retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering_v1_default_val(api):
    endpoint_result = api.sensors.retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(
        apid=None,
        capture_status=None,
        capture_type=None,
        client_mac=None,
        wlc_id=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering_v1_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering_v1(
            validator,
            retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploys_the_given_i_cap_configuration_intent_without_preview_and_approve_v1(json_schema_validate, obj):
    json_schema_validate('jsd_8eea45fca32f5f12adc30a9d03c43ac6_v2_3_7_9').validate(obj)
    return True


def deploys_the_given_i_cap_configuration_intent_without_preview_and_approve_v1(api):
    endpoint_result = api.sensors.deploys_the_given_i_cap_configuration_intent_without_preview_and_approve_v1(
        active_validation=True,
        payload=None,
        preview_description='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_deploys_the_given_i_cap_configuration_intent_without_preview_and_approve_v1(api, validator):
    try:
        assert is_valid_deploys_the_given_i_cap_configuration_intent_without_preview_and_approve_v1(
            validator,
            deploys_the_given_i_cap_configuration_intent_without_preview_and_approve_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploys_the_given_i_cap_configuration_intent_without_preview_and_approve_v1_default_val(api):
    endpoint_result = api.sensors.deploys_the_given_i_cap_configuration_intent_without_preview_and_approve_v1(
        active_validation=True,
        payload=None,
        preview_description=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_deploys_the_given_i_cap_configuration_intent_without_preview_and_approve_v1_default_val(api, validator):
    try:
        assert is_valid_deploys_the_given_i_cap_configuration_intent_without_preview_and_approve_v1(
            validator,
            deploys_the_given_i_cap_configuration_intent_without_preview_and_approve_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_the_i_cap_configuration_on_the_device_without_preview_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e2ec291c2e775df3895aadc639713eea_v2_3_7_9').validate(obj)
    return True


def remove_the_i_cap_configuration_on_the_device_without_preview_v1(api):
    endpoint_result = api.sensors.remove_the_i_cap_configuration_on_the_device_without_preview_v1(
        active_validation=True,
        id='string',
        object='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_remove_the_i_cap_configuration_on_the_device_without_preview_v1(api, validator):
    try:
        assert is_valid_remove_the_i_cap_configuration_on_the_device_without_preview_v1(
            validator,
            remove_the_i_cap_configuration_on_the_device_without_preview_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def remove_the_i_cap_configuration_on_the_device_without_preview_v1_default_val(api):
    endpoint_result = api.sensors.remove_the_i_cap_configuration_on_the_device_without_preview_v1(
        active_validation=True,
        id='string',
        object=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_remove_the_i_cap_configuration_on_the_device_without_preview_v1_default_val(api, validator):
    try:
        assert is_valid_remove_the_i_cap_configuration_on_the_device_without_preview_v1(
            validator,
            remove_the_i_cap_configuration_on_the_device_without_preview_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_deployment_status_v1(json_schema_validate, obj):
    json_schema_validate('jsd_953065bebb4e5aaf8ba6e5284cdbeafb_v2_3_7_9').validate(obj)
    return True


def get_device_deployment_status_v1(api):
    endpoint_result = api.sensors.get_device_deployment_status_v1(
        deploy_activity_id='string',
        limit=0,
        network_device_ids='string',
        offset=0,
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_get_device_deployment_status_v1(api, validator):
    try:
        assert is_valid_get_device_deployment_status_v1(
            validator,
            get_device_deployment_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_deployment_status_v1_default_val(api):
    endpoint_result = api.sensors.get_device_deployment_status_v1(
        deploy_activity_id=None,
        limit=None,
        network_device_ids=None,
        offset=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_get_device_deployment_status_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_deployment_status_v1(
            validator,
            get_device_deployment_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_deployment_status_count_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d04eba6a847958ae9c883f6957081ead_v2_3_7_9').validate(obj)
    return True


def get_device_deployment_status_count_v1(api):
    endpoint_result = api.sensors.get_device_deployment_status_count_v1(
        deploy_activity_id='string',
        network_device_ids='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_get_device_deployment_status_count_v1(api, validator):
    try:
        assert is_valid_get_device_deployment_status_count_v1(
            validator,
            get_device_deployment_status_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_deployment_status_count_v1_default_val(api):
    endpoint_result = api.sensors.get_device_deployment_status_count_v1(
        deploy_activity_id=None,
        network_device_ids=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_get_device_deployment_status_count_v1_default_val(api, validator):
    try:
        assert is_valid_get_device_deployment_status_count_v1(
            validator,
            get_device_deployment_status_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sensor_test_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6f7dd6a6cf8d57499168aae05847ad34_v2_3_7_9').validate(obj)
    return True


def create_sensor_test_template_v1(api):
    endpoint_result = api.sensors.create_sensor_test_template_v1(
        active_validation=True,
        apCoverage=[{'bands': 'string', 'numberOfApsToTest': 0, 'rssiThreshold': 0}],
        connection='string',
        encryptionMode='string',
        locationInfoList=[{'locationId': 'string', 'locationType': 'string', 'allSensors': True, 'siteHierarchy': 'string', 'macAddressList': ['string'], 'managementVlan': 'string', 'customManagementVlan': True}],
        modelVersion=0,
        name='string',
        payload=None,
        profiles=[{'authType': 'string', 'psk': 'string', 'username': 'string', 'password': 'string', 'passwordType': 'string', 'eapMethod': 'string', 'scep': True, 'authProtocol': 'string', 'certfilename': 'string', 'certxferprotocol': 'string', 'certstatus': 'string', 'certpassphrase': 'string', 'certdownloadurl': 'string', 'extWebAuthVirtualIp': 'string', 'extWebAuth': True, 'whiteList': True, 'extWebAuthPortal': 'string', 'extWebAuthAccessUrl': 'string', 'extWebAuthHtmlTag': [{'label': 'string', 'tag': 'string', 'value': 'string'}], 'qosPolicy': 'string', 'tests': [{'name': 'string', 'config': [{'domains': ['string'], 'server': 'string', 'userName': 'string', 'password': 'string', 'url': 'string', 'port': 0, 'protocol': 'string', 'servers': ['string'], 'direction': 'string', 'startPort': 0, 'endPort': 0, 'udpBandwidth': 0, 'probeType': 'string', 'numPackets': 0, 'pathToDownload': 'string', 'transferType': 'string', 'sharedSecret': 'string', 'ndtServer': 'string', 'ndtServerPort': 'string', 'ndtServerPath': 'string', 'uplinkTest': True, 'downlinkTest': True, 'proxyServer': 'string', 'proxyPort': 'string', 'proxyUserName': 'string', 'proxyPassword': 'string', 'userNamePrompt': 'string', 'passwordPrompt': 'string', 'exitCommand': 'string', 'finalPrompt': 'string'}]}], 'profileName': 'string', 'deviceType': 'string', 'vlan': 'string', 'locationVlanList': [{'locationId': 'string', 'vlans': ['string']}]}],
        runNow='string',
        sensors=[{'name': 'string', 'macAddress': 'string', 'switchMac': 'string', 'switchUuid': 'string', 'switchSerialNumber': 'string', 'markedForUninstall': True, 'ipAddress': 'string', 'hostName': 'string', 'wiredApplicationStatus': 'string', 'wiredApplicationMessage': 'string', 'assigned': True, 'status': 'string', 'xorSensor': True, 'targetAPs': ['string'], 'runNow': 'string', 'locationId': 'string', 'allSensorAddition': True, 'configUpdated': 'string', 'sensorType': 'string', 'testMacAddresses': {}, 'id': 'string', 'servicePolicy': 'string', 'iPerfInfo': {}}],
        ssids=[{'bands': 'string', 'ssid': 'string', 'profileName': 'string', 'layer3webAuthsecurity': 'string', 'layer3webAuthuserName': 'string', 'layer3webAuthpassword': 'string', 'layer3webAuthEmailAddress': 'string', 'thirdParty': {'selected': True}, 'wlanId': 0, 'wlc': 'string', 'proxyServer': 'string', 'proxyPort': 'string', 'proxyUserName': 'string', 'proxyPassword': 'string', 'authType': 'string', 'psk': 'string', 'username': 'string', 'password': 'string', 'passwordType': 'string', 'eapMethod': 'string', 'scep': True, 'authProtocol': 'string', 'certfilename': 'string', 'certxferprotocol': 'string', 'certstatus': 'string', 'certpassphrase': 'string', 'certdownloadurl': 'string', 'extWebAuthVirtualIp': 'string', 'extWebAuth': True, 'whiteList': True, 'extWebAuthPortal': 'string', 'extWebAuthAccessUrl': 'string', 'extWebAuthHtmlTag': [{'label': 'string', 'tag': 'string', 'value': 'string'}], 'qosPolicy': 'string', 'tests': [{'name': 'string', 'config': [{'domains': ['string'], 'server': 'string', 'userName': 'string', 'password': 'string', 'url': 'string', 'port': 0, 'protocol': 'string', 'servers': ['string'], 'direction': 'string', 'startPort': 0, 'endPort': 0, 'udpBandwidth': 0, 'probeType': 'string', 'numPackets': 0, 'pathToDownload': 'string', 'transferType': 'string', 'sharedSecret': 'string', 'ndtServer': 'string', 'ndtServerPort': 'string', 'ndtServerPath': 'string', 'uplinkTest': True, 'downlinkTest': True, 'proxyServer': 'string', 'proxyPort': 'string', 'proxyUserName': 'string', 'proxyPassword': 'string', 'userNamePrompt': 'string', 'passwordPrompt': 'string', 'exitCommand': 'string', 'finalPrompt': 'string'}]}]}],
        version=0
    )
    return endpoint_result


@pytest.mark.sensors
def test_create_sensor_test_template_v1(api, validator):
    try:
        assert is_valid_create_sensor_test_template_v1(
            validator,
            create_sensor_test_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_sensor_test_template_v1_default_val(api):
    endpoint_result = api.sensors.create_sensor_test_template_v1(
        active_validation=True,
        apCoverage=None,
        connection=None,
        encryptionMode=None,
        locationInfoList=None,
        modelVersion=None,
        name=None,
        payload=None,
        profiles=None,
        runNow=None,
        sensors=None,
        ssids=None,
        version=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_create_sensor_test_template_v1_default_val(api, validator):
    try:
        assert is_valid_create_sensor_test_template_v1(
            validator,
            create_sensor_test_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sensor_test_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a1c0ac4386555300b7f4a541d8dba625_v2_3_7_9').validate(obj)
    return True


def delete_sensor_test_v1(api):
    endpoint_result = api.sensors.delete_sensor_test_v1(
        template_name='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_delete_sensor_test_v1(api, validator):
    try:
        assert is_valid_delete_sensor_test_v1(
            validator,
            delete_sensor_test_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_sensor_test_v1_default_val(api):
    endpoint_result = api.sensors.delete_sensor_test_v1(
        template_name=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_delete_sensor_test_v1_default_val(api, validator):
    try:
        assert is_valid_delete_sensor_test_v1(
            validator,
            delete_sensor_test_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sensors_v1(json_schema_validate, obj):
    json_schema_validate('jsd_49925cda740c5bdc92fd150c334d0e4e_v2_3_7_9').validate(obj)
    return True


def sensors_v1(api):
    endpoint_result = api.sensors.sensors_v1(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_sensors_v1(api, validator):
    try:
        assert is_valid_sensors_v1(
            validator,
            sensors_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def sensors_v1_default_val(api):
    endpoint_result = api.sensors.sensors_v1(
        site_id=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_sensors_v1_default_val(api, validator):
    try:
        assert is_valid_sensors_v1(
            validator,
            sensors_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_run_now_sensor_test_v1(json_schema_validate, obj):
    json_schema_validate('jsd_cfadc5e4c912588389f4f63d2fb6e4ed_v2_3_7_9').validate(obj)
    return True


def run_now_sensor_test_v1(api):
    endpoint_result = api.sensors.run_now_sensor_test_v1(
        active_validation=True,
        payload=None,
        templateName='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_run_now_sensor_test_v1(api, validator):
    try:
        assert is_valid_run_now_sensor_test_v1(
            validator,
            run_now_sensor_test_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def run_now_sensor_test_v1_default_val(api):
    endpoint_result = api.sensors.run_now_sensor_test_v1(
        active_validation=True,
        payload=None,
        templateName=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_run_now_sensor_test_v1_default_val(api, validator):
    try:
        assert is_valid_run_now_sensor_test_v1(
            validator,
            run_now_sensor_test_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_duplicate_sensor_test_template_v1(json_schema_validate, obj):
    json_schema_validate('jsd_a352f6280e445075b3ea7cbf868c2d94_v2_3_7_9').validate(obj)
    return True


def duplicate_sensor_test_template_v1(api):
    endpoint_result = api.sensors.duplicate_sensor_test_template_v1(
        active_validation=True,
        newTemplateName='string',
        payload=None,
        templateName='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_duplicate_sensor_test_template_v1(api, validator):
    try:
        assert is_valid_duplicate_sensor_test_template_v1(
            validator,
            duplicate_sensor_test_template_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def duplicate_sensor_test_template_v1_default_val(api):
    endpoint_result = api.sensors.duplicate_sensor_test_template_v1(
        active_validation=True,
        newTemplateName=None,
        payload=None,
        templateName=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_duplicate_sensor_test_template_v1_default_val(api, validator):
    try:
        assert is_valid_duplicate_sensor_test_template_v1(
            validator,
            duplicate_sensor_test_template_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI sensors API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.3', reason='version does not match')


def is_valid_edit_sensor_test_template(json_schema_validate, obj):
    json_schema_validate('jsd_e2f9718de3d050819cdc6355a3a43200_v2_3_7_3').validate(obj)
    return True


def edit_sensor_test_template(api):
    endpoint_result = api.sensors.edit_sensor_test_template(
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
def test_edit_sensor_test_template(api, validator):
    try:
        assert is_valid_edit_sensor_test_template(
            validator,
            edit_sensor_test_template(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def edit_sensor_test_template_default_val(api):
    endpoint_result = api.sensors.edit_sensor_test_template(
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
def test_edit_sensor_test_template_default_val(api, validator):
    try:
        assert is_valid_edit_sensor_test_template(
            validator,
            edit_sensor_test_template_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sensor_test_template(json_schema_validate, obj):
    json_schema_validate('jsd_6f7dd6a6cf8d57499168aae05847ad34_v2_3_7_3').validate(obj)
    return True


def create_sensor_test_template(api):
    endpoint_result = api.sensors.create_sensor_test_template(
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
def test_create_sensor_test_template(api, validator):
    try:
        assert is_valid_create_sensor_test_template(
            validator,
            create_sensor_test_template(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_sensor_test_template_default_val(api):
    endpoint_result = api.sensors.create_sensor_test_template(
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
def test_create_sensor_test_template_default_val(api, validator):
    try:
        assert is_valid_create_sensor_test_template(
            validator,
            create_sensor_test_template_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sensor_test(json_schema_validate, obj):
    json_schema_validate('jsd_a1c0ac4386555300b7f4a541d8dba625_v2_3_7_3').validate(obj)
    return True


def delete_sensor_test(api):
    endpoint_result = api.sensors.delete_sensor_test(
        template_name='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_delete_sensor_test(api, validator):
    try:
        assert is_valid_delete_sensor_test(
            validator,
            delete_sensor_test(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_sensor_test_default_val(api):
    endpoint_result = api.sensors.delete_sensor_test(
        template_name=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_delete_sensor_test_default_val(api, validator):
    try:
        assert is_valid_delete_sensor_test(
            validator,
            delete_sensor_test_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sensors(json_schema_validate, obj):
    json_schema_validate('jsd_49925cda740c5bdc92fd150c334d0e4e_v2_3_7_3').validate(obj)
    return True


def sensors(api):
    endpoint_result = api.sensors.sensors(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_sensors(api, validator):
    try:
        assert is_valid_sensors(
            validator,
            sensors(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def sensors_default_val(api):
    endpoint_result = api.sensors.sensors(
        site_id=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_sensors_default_val(api, validator):
    try:
        assert is_valid_sensors(
            validator,
            sensors_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_run_now_sensor_test(json_schema_validate, obj):
    json_schema_validate('jsd_cfadc5e4c912588389f4f63d2fb6e4ed_v2_3_7_3').validate(obj)
    return True


def run_now_sensor_test(api):
    endpoint_result = api.sensors.run_now_sensor_test(
        active_validation=True,
        payload=None,
        templateName='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_run_now_sensor_test(api, validator):
    try:
        assert is_valid_run_now_sensor_test(
            validator,
            run_now_sensor_test(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def run_now_sensor_test_default_val(api):
    endpoint_result = api.sensors.run_now_sensor_test(
        active_validation=True,
        payload=None,
        templateName=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_run_now_sensor_test_default_val(api, validator):
    try:
        assert is_valid_run_now_sensor_test(
            validator,
            run_now_sensor_test_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_duplicate_sensor_test_template(json_schema_validate, obj):
    json_schema_validate('jsd_a352f6280e445075b3ea7cbf868c2d94_v2_3_7_3').validate(obj)
    return True


def duplicate_sensor_test_template(api):
    endpoint_result = api.sensors.duplicate_sensor_test_template(
        active_validation=True,
        newTemplateName='string',
        payload=None,
        templateName='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_duplicate_sensor_test_template(api, validator):
    try:
        assert is_valid_duplicate_sensor_test_template(
            validator,
            duplicate_sensor_test_template(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def duplicate_sensor_test_template_default_val(api):
    endpoint_result = api.sensors.duplicate_sensor_test_template(
        active_validation=True,
        newTemplateName=None,
        payload=None,
        templateName=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_duplicate_sensor_test_template_default_val(api, validator):
    try:
        assert is_valid_duplicate_sensor_test_template(
            validator,
            duplicate_sensor_test_template_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

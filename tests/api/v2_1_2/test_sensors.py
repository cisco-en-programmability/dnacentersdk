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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.1.2', reason='version does not match')


def is_valid_create_sensor_test_template(json_schema_validate, obj):
    json_schema_validate('jsd_08bd88834a68a2e6_v2_1_2').validate(obj)
    return True


def create_sensor_test_template(api):
    endpoint_result = api.sensors.create_sensor_test_template(
        active_validation=True,
        apCoverage=[{'bands': 'string', 'numberOfApsToTest': 'string', 'rssiThreshold': 'string'}],
        connection='string',
        modelVersion=0,
        name='string',
        payload=None,
        ssids=[{'ssid': 'string', 'profileName': 'string', 'authType': 'string', 'thirdParty': {'selected': True}, 'psk': 'string', 'tests': [{'name': 'string', 'config': [{}]}], 'categories': ['string'], 'qosPolicy': 'string'}]
    )
    return endpoint_result


@pytest.mark.sensors
def test_create_sensor_test_template(api, validator):
    assert is_valid_create_sensor_test_template(
        validator,
        create_sensor_test_template(api)
    )


def create_sensor_test_template_default(api):
    endpoint_result = api.sensors.create_sensor_test_template(
        active_validation=True,
        apCoverage=None,
        connection=None,
        modelVersion=None,
        name=None,
        payload=None,
        ssids=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_create_sensor_test_template_default(api, validator):
    try:
        assert is_valid_create_sensor_test_template(
            validator,
            create_sensor_test_template_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sensor_test(json_schema_validate, obj):
    json_schema_validate('jsd_5bbb28ff442a825f_v2_1_2').validate(obj)
    return True


def delete_sensor_test(api):
    endpoint_result = api.sensors.delete_sensor_test(
        template_name='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_delete_sensor_test(api, validator):
    assert is_valid_delete_sensor_test(
        validator,
        delete_sensor_test(api)
    )


def delete_sensor_test_default(api):
    endpoint_result = api.sensors.delete_sensor_test(
        template_name=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_delete_sensor_test_default(api, validator):
    try:
        assert is_valid_delete_sensor_test(
            validator,
            delete_sensor_test_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_duplicate_sensor_test_template(json_schema_validate, obj):
    json_schema_validate('jsd_85a2883749099021_v2_1_2').validate(obj)
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
    assert is_valid_duplicate_sensor_test_template(
        validator,
        duplicate_sensor_test_template(api)
    )


def duplicate_sensor_test_template_default(api):
    endpoint_result = api.sensors.duplicate_sensor_test_template(
        active_validation=True,
        newTemplateName=None,
        payload=None,
        templateName=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_duplicate_sensor_test_template_default(api, validator):
    try:
        assert is_valid_duplicate_sensor_test_template(
            validator,
            duplicate_sensor_test_template_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sensors(json_schema_validate, obj):
    json_schema_validate('jsd_71a12bb745699cc5_v2_1_2').validate(obj)
    return True


def sensors(api):
    endpoint_result = api.sensors.sensors(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_sensors(api, validator):
    assert is_valid_sensors(
        validator,
        sensors(api)
    )


def sensors_default(api):
    endpoint_result = api.sensors.sensors(
        site_id=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_sensors_default(api, validator):
    try:
        assert is_valid_sensors(
            validator,
            sensors_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_edit_sensor_test_template(json_schema_validate, obj):
    json_schema_validate('jsd_c085eaf54f89ba34_v2_1_2').validate(obj)
    return True


def edit_sensor_test_template(api):
    endpoint_result = api.sensors.edit_sensor_test_template(
        active_validation=True,
        locationInfoList=[{'locationId': 'string', 'locationType': 'string', 'siteHierarchy': 'string', 'allSensors': True}],
        payload=None,
        schedule={'testScheduleMode': 'string', 'frequency': {'unit': 'string', 'value': 0}, 'scheduleRange': [{'day': 'string', 'timeRange': [{'from': 'string', 'to': 'string', 'frequency': {'unit': 'string', 'value': 0}}]}]},
        templateName='string'
    )
    return endpoint_result


@pytest.mark.sensors
def test_edit_sensor_test_template(api, validator):
    assert is_valid_edit_sensor_test_template(
        validator,
        edit_sensor_test_template(api)
    )


def edit_sensor_test_template_default(api):
    endpoint_result = api.sensors.edit_sensor_test_template(
        active_validation=True,
        locationInfoList=None,
        payload=None,
        schedule=None,
        templateName=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_edit_sensor_test_template_default(api, validator):
    try:
        assert is_valid_edit_sensor_test_template(
            validator,
            edit_sensor_test_template_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_run_now_sensor_test(json_schema_validate, obj):
    json_schema_validate('jsd_f1a7a8e74cf99c8f_v2_1_2').validate(obj)
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
    assert is_valid_run_now_sensor_test(
        validator,
        run_now_sensor_test(api)
    )


def run_now_sensor_test_default(api):
    endpoint_result = api.sensors.run_now_sensor_test(
        active_validation=True,
        payload=None,
        templateName=None
    )
    return endpoint_result


@pytest.mark.sensors
def test_run_now_sensor_test_default(api, validator):
    try:
        assert is_valid_run_now_sensor_test(
            validator,
            run_now_sensor_test_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

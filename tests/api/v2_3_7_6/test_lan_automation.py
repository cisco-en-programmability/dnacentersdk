# -*- coding: utf-8 -*-
"""DNACenterAPI lan_automation API fixtures and tests.

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

pytestmark = pytest.mark.skipif(
    DNA_CENTER_VERSION != "2.3.7.6", reason="version does not match"
)


def is_valid_lan_automation_start_v1(json_schema_validate, obj):
    json_schema_validate("jsd_b119a4d455e35cc3b2cc6695a045cbfa_v2_3_7_6").validate(obj)
    return True


def lan_automation_start_v1(api):
    endpoint_result = api.lan_automation.lan_automation_start_v1(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_start_v1(api, validator):
    try:
        assert is_valid_lan_automation_start_v1(validator, lan_automation_start_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_start_v1_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_start_v1(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_start_v1_default_val(api, validator):
    try:
        assert is_valid_lan_automation_start_v1(
            validator, lan_automation_start_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_session_count_v1(json_schema_validate, obj):
    json_schema_validate("jsd_130eea014edd5807925df3a414a92ed4_v2_3_7_6").validate(obj)
    return True


def lan_automation_session_count_v1(api):
    endpoint_result = api.lan_automation.lan_automation_session_count_v1()
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_session_count_v1(api, validator):
    try:
        assert is_valid_lan_automation_session_count_v1(
            validator, lan_automation_session_count_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_session_count_v1_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_session_count_v1()
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_session_count_v1_default_val(api, validator):
    try:
        assert is_valid_lan_automation_session_count_v1(
            validator, lan_automation_session_count_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_log_v1(json_schema_validate, obj):
    json_schema_validate("jsd_3173e37f6c9650b68e0aaac866a162cf_v2_3_7_6").validate(obj)
    return True


def lan_automation_log_v1(api):
    endpoint_result = api.lan_automation.lan_automation_log_v1(limit=0, offset=0)
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_log_v1(api, validator):
    try:
        assert is_valid_lan_automation_log_v1(validator, lan_automation_log_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_log_v1_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_log_v1(limit=None, offset=None)
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_log_v1_default_val(api, validator):
    try:
        assert is_valid_lan_automation_log_v1(
            validator, lan_automation_log_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_log_by_id_v1(json_schema_validate, obj):
    json_schema_validate("jsd_60e98b744fde50a1b53761251c43bfb0_v2_3_7_6").validate(obj)
    return True


def lan_automation_log_by_id_v1(api):
    endpoint_result = api.lan_automation.lan_automation_log_by_id_v1(id="string")
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_log_by_id_v1(api, validator):
    try:
        assert is_valid_lan_automation_log_by_id_v1(
            validator, lan_automation_log_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_log_by_id_v1_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_log_by_id_v1(id="string")
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_log_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_lan_automation_log_by_id_v1(
            validator, lan_automation_log_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_logs_for_individual_devices_v1(json_schema_validate, obj):
    json_schema_validate("jsd_26485c3441f7507a98d02579c25814f4_v2_3_7_6").validate(obj)
    return True


def lan_automation_logs_for_individual_devices_v1(api):
    endpoint_result = api.lan_automation.lan_automation_logs_for_individual_devices_v1(
        id="string", log_level="string", serial_number="string"
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_logs_for_individual_devices_v1(api, validator):
    try:
        assert is_valid_lan_automation_logs_for_individual_devices_v1(
            validator, lan_automation_logs_for_individual_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_logs_for_individual_devices_v1_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_logs_for_individual_devices_v1(
        id="string", log_level=None, serial_number="string"
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_logs_for_individual_devices_v1_default_val(api, validator):
    try:
        assert is_valid_lan_automation_logs_for_individual_devices_v1(
            validator, lan_automation_logs_for_individual_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_active_sessions_v1(json_schema_validate, obj):
    json_schema_validate("jsd_5a19cf2241e75c648220d7172e9e4013_v2_3_7_6").validate(obj)
    return True


def lan_automation_active_sessions_v1(api):
    endpoint_result = api.lan_automation.lan_automation_active_sessions_v1()
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_active_sessions_v1(api, validator):
    try:
        assert is_valid_lan_automation_active_sessions_v1(
            validator, lan_automation_active_sessions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_active_sessions_v1_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_active_sessions_v1()
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_active_sessions_v1_default_val(api, validator):
    try:
        assert is_valid_lan_automation_active_sessions_v1(
            validator, lan_automation_active_sessions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_status_v1(json_schema_validate, obj):
    json_schema_validate("jsd_40c56a6c58fd5b71b7949036855ee25b_v2_3_7_6").validate(obj)
    return True


def lan_automation_status_v1(api):
    endpoint_result = api.lan_automation.lan_automation_status_v1(limit=0, offset=0)
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_status_v1(api, validator):
    try:
        assert is_valid_lan_automation_status_v1(
            validator, lan_automation_status_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_status_v1_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_status_v1(
        limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_status_v1_default_val(api, validator):
    try:
        assert is_valid_lan_automation_status_v1(
            validator, lan_automation_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_status_by_id_v1(json_schema_validate, obj):
    json_schema_validate("jsd_d5727c4bdb1056308cd10e99dff2acb8_v2_3_7_6").validate(obj)
    return True


def lan_automation_status_by_id_v1(api):
    endpoint_result = api.lan_automation.lan_automation_status_by_id_v1(id="string")
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_status_by_id_v1(api, validator):
    try:
        assert is_valid_lan_automation_status_by_id_v1(
            validator, lan_automation_status_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_status_by_id_v1_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_status_by_id_v1(id="string")
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_status_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_lan_automation_status_by_id_v1(
            validator, lan_automation_status_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_device_update_v1(json_schema_validate, obj):
    json_schema_validate("jsd_932aac9ba55e5043b4d5e0995c566dce_v2_3_7_6").validate(obj)
    return True


def lan_automation_device_update_v1(api):
    endpoint_result = api.lan_automation.lan_automation_device_update_v1(
        active_validation=True,
        feature="string",
        hostnameUpdateDevices=[
            {"deviceManagementIPAddress": "string", "newHostName": "string"}
        ],
        linkUpdate={
            "sourceDeviceManagementIPAddress": "string",
            "sourceDeviceInterfaceName": "string",
            "destinationDeviceManagementIPAddress": "string",
            "destinationDeviceInterfaceName": "string",
            "ipPoolName": "string",
        },
        loopbackUpdateDeviceList=[
            {"deviceManagementIPAddress": "string", "newLoopback0IPAddress": "string"}
        ],
        payload=None,
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_device_update_v1(api, validator):
    try:
        assert is_valid_lan_automation_device_update_v1(
            validator, lan_automation_device_update_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_device_update_v1_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_device_update_v1(
        active_validation=True,
        feature=None,
        hostnameUpdateDevices=None,
        linkUpdate=None,
        loopbackUpdateDeviceList=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_device_update_v1_default_val(api, validator):
    try:
        assert is_valid_lan_automation_device_update_v1(
            validator, lan_automation_device_update_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_stop_v1(json_schema_validate, obj):
    json_schema_validate("jsd_ed815ca3e5ab5ae48720795217ec776b_v2_3_7_6").validate(obj)
    return True


def lan_automation_stop_v1(api):
    endpoint_result = api.lan_automation.lan_automation_stop_v1(id="string")
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop_v1(api, validator):
    try:
        assert is_valid_lan_automation_stop_v1(validator, lan_automation_stop_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_stop_v1_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_stop_v1(id="string")
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop_v1_default_val(api, validator):
    try:
        assert is_valid_lan_automation_stop_v1(
            validator, lan_automation_stop_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_stop_and_update_devices_v1(json_schema_validate, obj):
    json_schema_validate("jsd_d413a3d054ac50fa921ca8cf7fdf5449_v2_3_7_6").validate(obj)
    return True


def lan_automation_stop_and_update_devices_v1(api):
    endpoint_result = api.lan_automation.lan_automation_stop_and_update_devices_v1(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop_and_update_devices_v1(api, validator):
    try:
        assert is_valid_lan_automation_stop_and_update_devices_v1(
            validator, lan_automation_stop_and_update_devices_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_stop_and_update_devices_v1_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_stop_and_update_devices_v1(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop_and_update_devices_v1_default_val(api, validator):
    try:
        assert is_valid_lan_automation_stop_and_update_devices_v1(
            validator, lan_automation_stop_and_update_devices_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_start_v2(json_schema_validate, obj):
    json_schema_validate("jsd_dc5d352dfaeb5b17800b0af2858c2f5c_v2_3_7_6").validate(obj)
    return True


def lan_automation_start_v2(api):
    endpoint_result = api.lan_automation.lan_automation_start_v2(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_start_v2(api, validator):
    try:
        assert is_valid_lan_automation_start_v2(validator, lan_automation_start_v2(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_start_v2_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_start_v2(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_start_v2_default_val(api, validator):
    try:
        assert is_valid_lan_automation_start_v2(
            validator, lan_automation_start_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_stop_and_update_devices_v2(json_schema_validate, obj):
    json_schema_validate("jsd_4421504ad0cb5a12a76384ba4644e55e_v2_3_7_6").validate(obj)
    return True


def lan_automation_stop_and_update_devices_v2(api):
    endpoint_result = api.lan_automation.lan_automation_stop_and_update_devices_v2(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop_and_update_devices_v2(api, validator):
    try:
        assert is_valid_lan_automation_stop_and_update_devices_v2(
            validator, lan_automation_stop_and_update_devices_v2(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_stop_and_update_devices_v2_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_stop_and_update_devices_v2(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop_and_update_devices_v2_default_val(api, validator):
    try:
        assert is_valid_lan_automation_stop_and_update_devices_v2(
            validator, lan_automation_stop_and_update_devices_v2_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

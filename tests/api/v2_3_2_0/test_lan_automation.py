# -*- coding: utf-8 -*-
"""DNACenterAPI lan_automation API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.2.0', reason='version does not match')


def is_valid_lan_automation_start(json_schema_validate, obj):
    json_schema_validate('jsd_b119a4d455e35cc3b2cc6695a045cbfa_v2_3_2_0').validate(obj)
    return True


def lan_automation_start(api):
    endpoint_result = api.lan_automation.lan_automation_start(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_start(api, validator):
    try:
        assert is_valid_lan_automation_start(
            validator,
            lan_automation_start(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_start_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_start(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_start_default_val(api, validator):
    try:
        assert is_valid_lan_automation_start(
            validator,
            lan_automation_start_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_session_count(json_schema_validate, obj):
    json_schema_validate('jsd_130eea014edd5807925df3a414a92ed4_v2_3_2_0').validate(obj)
    return True


def lan_automation_session_count(api):
    endpoint_result = api.lan_automation.lan_automation_session_count(

    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_session_count(api, validator):
    try:
        assert is_valid_lan_automation_session_count(
            validator,
            lan_automation_session_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_session_count_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_session_count(

    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_session_count_default_val(api, validator):
    try:
        assert is_valid_lan_automation_session_count(
            validator,
            lan_automation_session_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_log(json_schema_validate, obj):
    json_schema_validate('jsd_3173e37f6c9650b68e0aaac866a162cf_v2_3_2_0').validate(obj)
    return True


def lan_automation_log(api):
    endpoint_result = api.lan_automation.lan_automation_log(
        limit='string',
        offset='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_log(api, validator):
    try:
        assert is_valid_lan_automation_log(
            validator,
            lan_automation_log(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_log_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_log(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_log_default_val(api, validator):
    try:
        assert is_valid_lan_automation_log(
            validator,
            lan_automation_log_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_log_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_60e98b744fde50a1b53761251c43bfb0_v2_3_2_0').validate(obj)
    return True


def lan_automation_log_by_id(api):
    endpoint_result = api.lan_automation.lan_automation_log_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_log_by_id(api, validator):
    try:
        assert is_valid_lan_automation_log_by_id(
            validator,
            lan_automation_log_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_log_by_id_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_log_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_log_by_id_default_val(api, validator):
    try:
        assert is_valid_lan_automation_log_by_id(
            validator,
            lan_automation_log_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_status(json_schema_validate, obj):
    json_schema_validate('jsd_40c56a6c58fd5b71b7949036855ee25b_v2_3_2_0').validate(obj)
    return True


def lan_automation_status(api):
    endpoint_result = api.lan_automation.lan_automation_status(
        limit='string',
        offset='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_status(api, validator):
    try:
        assert is_valid_lan_automation_status(
            validator,
            lan_automation_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_status_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_status(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_status_default_val(api, validator):
    try:
        assert is_valid_lan_automation_status(
            validator,
            lan_automation_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_status_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_d5727c4bdb1056308cd10e99dff2acb8_v2_3_2_0').validate(obj)
    return True


def lan_automation_status_by_id(api):
    endpoint_result = api.lan_automation.lan_automation_status_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_status_by_id(api, validator):
    try:
        assert is_valid_lan_automation_status_by_id(
            validator,
            lan_automation_status_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_status_by_id_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_status_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_status_by_id_default_val(api, validator):
    try:
        assert is_valid_lan_automation_status_by_id(
            validator,
            lan_automation_status_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lan_automation_stop(json_schema_validate, obj):
    json_schema_validate('jsd_ed815ca3e5ab5ae48720795217ec776b_v2_3_2_0').validate(obj)
    return True


def lan_automation_stop(api):
    endpoint_result = api.lan_automation.lan_automation_stop(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop(api, validator):
    try:
        assert is_valid_lan_automation_stop(
            validator,
            lan_automation_stop(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def lan_automation_stop_default_val(api):
    endpoint_result = api.lan_automation.lan_automation_stop(
        id='string'
    )
    return endpoint_result


@pytest.mark.lan_automation
def test_lan_automation_stop_default_val(api, validator):
    try:
        assert is_valid_lan_automation_stop(
            validator,
            lan_automation_stop_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI command_runner API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.2.3', reason='version does not match')


def is_valid_get_all_keywords_of_clis_accepted(json_schema_validate, obj):
    json_schema_validate('jsd_53e946adf864590082fe3111a2a2fa74_v2_2_2_3').validate(obj)
    return True


def get_all_keywords_of_clis_accepted(api):
    endpoint_result = api.command_runner.get_all_keywords_of_clis_accepted(

    )
    return endpoint_result


@pytest.mark.command_runner
def test_get_all_keywords_of_clis_accepted(api, validator):
    try:
        assert is_valid_get_all_keywords_of_clis_accepted(
            validator,
            get_all_keywords_of_clis_accepted(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_keywords_of_clis_accepted_default_val(api):
    endpoint_result = api.command_runner.get_all_keywords_of_clis_accepted(

    )
    return endpoint_result


@pytest.mark.command_runner
def test_get_all_keywords_of_clis_accepted_default_val(api, validator):
    try:
        assert is_valid_get_all_keywords_of_clis_accepted(
            validator,
            get_all_keywords_of_clis_accepted_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_run_read_only_commands_on_devices(json_schema_validate, obj):
    json_schema_validate('jsd_b2dae3b41636596aa02c3ad0a4bcb8d7_v2_2_2_3').validate(obj)
    return True


def run_read_only_commands_on_devices(api):
    endpoint_result = api.command_runner.run_read_only_commands_on_devices(
        active_validation=True,
        commands=['string'],
        description='string',
        deviceUuids=['string'],
        name='string',
        payload=None,
        timeout=0
    )
    return endpoint_result


@pytest.mark.command_runner
def test_run_read_only_commands_on_devices(api, validator):
    try:
        assert is_valid_run_read_only_commands_on_devices(
            validator,
            run_read_only_commands_on_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def run_read_only_commands_on_devices_default_val(api):
    endpoint_result = api.command_runner.run_read_only_commands_on_devices(
        active_validation=True,
        commands=None,
        description=None,
        deviceUuids=None,
        name=None,
        payload=None,
        timeout=None
    )
    return endpoint_result


@pytest.mark.command_runner
def test_run_read_only_commands_on_devices_default_val(api, validator):
    try:
        assert is_valid_run_read_only_commands_on_devices(
            validator,
            run_read_only_commands_on_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

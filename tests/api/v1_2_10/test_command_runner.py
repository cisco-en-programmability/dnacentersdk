# -*- coding: utf-8 -*-
"""DNACenterAPI command_runner API fixtures and tests.

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
import dnacentersdk
import time
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate
from .test_devices import get_device_list


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_get_all_keywords_of_clis_accepted(obj):
    json_schema_validate('jsd_33bb2b9d40199e14_v1_2_10').validate(obj)
    return True


def get_all_keywords_of_clis_accepted(api):
    endpoint_result = api.command_runner.get_all_keywords_of_clis_accepted(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.command_runner
def test_get_all_keywords_of_clis_accepted(api):
    assert is_valid_get_all_keywords_of_clis_accepted(
        get_all_keywords_of_clis_accepted(api)
    )


def is_valid_run_read_only_commands_on_devices(obj):
    json_schema_validate('jsd_d6b8ca774739adf4_v1_2_10').validate(obj)
    return True


def run_read_only_commands_on_devices(api):
    endpoint_result = api.command_runner.run_read_only_commands_on_devices(
        commands=['show'],
        description=None,
        deviceUuids=[get_device_list(api).response[0].id],
        name=None,
        timeout=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.command_runner
def test_run_read_only_commands_on_devices(api):
    assert is_valid_run_read_only_commands_on_devices(
        run_read_only_commands_on_devices(api)
    )

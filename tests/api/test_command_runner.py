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


from .test_devices import get_device_list


# 33bb-2b9d-4019-9e14
def is_valid_get_all_keywords_of_clis_accepted_by_command_runner(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_all_keywords_of_clis_accepted_by_command_runner(api):
    endpoint_result = api.command_runner.get_all_keywords_of_clis_accepted_by_command_runner( payload = '' )
    return endpoint_result


def test_get_all_keywords_of_clis_accepted_by_command_runner(api):
    assert is_valid_get_all_keywords_of_clis_accepted_by_command_runner(get_all_keywords_of_clis_accepted_by_command_runner(api))


# d6b8-ca77-4739-adf4
def is_valid_run_read_only_commands_on_devices_to_get_their_real_time_configuration(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def run_read_only_commands_on_devices_to_get_their_real_time_configuration(api):
    endpoint_result = api.command_runner.run_read_only_commands_on_devices_to_get_their_real_time_configuration( rq_commands = [ get_all_keywords_of_clis_accepted_by_command_runner(api).response[0] ], rq_description = None, rq_deviceUuids = [ get_device_list(api).response[0].id ], rq_name = None, rq_timeout = None, payload = '' )
    return endpoint_result


def test_run_read_only_commands_on_devices_to_get_their_real_time_configuration(api):
    assert is_valid_run_read_only_commands_on_devices_to_get_their_real_time_configuration(run_read_only_commands_on_devices_to_get_their_real_time_configuration(api))


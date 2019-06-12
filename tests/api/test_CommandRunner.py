# command_runner

import pytest
import dnacentersdk


def is_valid_get_all_keywords_of_clis_accepted_by_command_runner(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_all_keywords_of_clis_accepted_by_command_runner(api):
    endpoint_result = api.command_runner.get_all_keywords_of_clis_accepted_by_command_runner( )
    assert is_valid_get_all_keywords_of_clis_accepted_by_command_runner(endpoint_result)


def is_valid_run_read_only_commands_on_devices_to_get_their_real_time_configuration(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_run_read_only_commands_on_devices_to_get_their_real_time_configuration(api):
    endpoint_result = api.command_runner.run_read_only_commands_on_devices_to_get_their_real_time_configuration( rq_commands = ['show ver | inc RELEASE'], rq_description = None, rq_deviceUuids = ['1904ca0d-01be-4d13-88e5-4f4f9980b512'], rq_name = None, rq_timeout = None)
    assert is_valid_run_read_only_commands_on_devices_to_get_their_real_time_configuration(endpoint_result)


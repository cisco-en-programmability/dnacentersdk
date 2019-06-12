# file

import pytest
import dnacentersdk


def is_valid_get_list_of_available_namespaces(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_list_of_available_namespaces(api):
    endpoint_result = api.file.get_list_of_available_namespaces( )
    assert is_valid_get_list_of_available_namespaces(endpoint_result)


def is_valid_get_list_of_files(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_list_of_files(api):
    endpoint_result = api.file.get_list_of_files( path_param_name_space = 'group_export')
    assert is_valid_get_list_of_files(endpoint_result)


def is_valid_download_a_file_by_fileid(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_download_a_file_by_fileid(api):
    endpoint_result = api.file.download_a_file_by_fileid( path_param_file_id = '5363d7b6-fb63-4de8-8422-8a3abd9f6682')
    assert is_valid_download_a_file_by_fileid(endpoint_result)


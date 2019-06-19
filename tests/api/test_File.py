# file

import pytest
import dnacentersdk


# 3f89-bbfc-4f6b-8b50
def is_valid_get_list_of_available_namespaces(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 3f89-bbfc-4f6b-8b50
def get_list_of_available_namespaces(api):
    endpoint_result = api.file.get_list_of_available_namespaces(  )
    return endpoint_result

# 3f89-bbfc-4f6b-8b50
def test_get_list_of_available_namespaces(api):
    assert is_valid_get_list_of_available_namespaces(get_list_of_available_namespaces(api))


# 42b6-a86e-44b8-bdfc
def is_valid_get_list_of_files(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 42b6-a86e-44b8-bdfc
def get_list_of_files(api):
    endpoint_result = api.file.get_list_of_files( path_param_name_space = get_list_of_available_namespaces(api).response[0] )
    return endpoint_result

# 42b6-a86e-44b8-bdfc
def test_get_list_of_files(api):
    assert is_valid_get_list_of_files(get_list_of_files(api))


# 9698-c8ec-4a0b-8c1a
def is_valid_download_a_file_by_fileid(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# 9698-c8ec-4a0b-8c1a
def download_a_file_by_fileid(api):
    endpoint_result = api.file.download_a_file_by_fileid( path_param_file_id = get_list_of_files(api).response[0].id )
    return endpoint_result

# 9698-c8ec-4a0b-8c1a
def test_download_a_file_by_fileid(api):
    assert is_valid_download_a_file_by_fileid(download_a_file_by_fileid(api))


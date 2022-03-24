# -*- coding: utf-8 -*-
"""DNACenterAPI file API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.3.3', reason='version does not match')


def is_valid_get_list_of_available_namespaces(json_schema_validate, obj):
    json_schema_validate('jsd_b7fc125c901c5d4488b7a2b75fa292bc_v2_2_3_3').validate(obj)
    return True


def get_list_of_available_namespaces(api):
    endpoint_result = api.file.get_list_of_available_namespaces(

    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_available_namespaces(api, validator):
    try:
        assert is_valid_get_list_of_available_namespaces(
            validator,
            get_list_of_available_namespaces(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_list_of_available_namespaces_default_val(api):
    endpoint_result = api.file.get_list_of_available_namespaces(

    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_available_namespaces_default_val(api, validator):
    try:
        assert is_valid_get_list_of_available_namespaces(
            validator,
            get_list_of_available_namespaces_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_list_of_files(json_schema_validate, obj):
    json_schema_validate('jsd_b7d63a5ae65b59a5a35d43edc58b6db5_v2_2_3_3').validate(obj)
    return True


def get_list_of_files(api):
    endpoint_result = api.file.get_list_of_files(
        name_space='string'
    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_files(api, validator):
    try:
        assert is_valid_get_list_of_files(
            validator,
            get_list_of_files(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_list_of_files_default_val(api):
    endpoint_result = api.file.get_list_of_files(
        name_space='string'
    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_files_default_val(api, validator):
    try:
        assert is_valid_get_list_of_files(
            validator,
            get_list_of_files_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_download_a_file_by_fileid(json_schema_validate, obj):
    json_schema_validate('jsd_1282fa4ab7605a75aafa6c7da6ac3f13_v2_2_3_3').validate(obj)
    return True


def download_a_file_by_fileid(api):
    endpoint_result = api.file.download_a_file_by_fileid(
        dirpath=None,
        save_file=None,
        filename=None,
        file_id='string'
    )
    return endpoint_result


@pytest.mark.file
def test_download_a_file_by_fileid(api, validator):
    try:
        assert is_valid_download_a_file_by_fileid(
            validator,
            download_a_file_by_fileid(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def download_a_file_by_fileid_default_val(api):
    endpoint_result = api.file.download_a_file_by_fileid(
        dirpath=None,
        save_file=None,
        filename=None,
        file_id='string'
    )
    return endpoint_result


@pytest.mark.file
def test_download_a_file_by_fileid_default_val(api, validator):
    try:
        assert is_valid_download_a_file_by_fileid(
            validator,
            download_a_file_by_fileid_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

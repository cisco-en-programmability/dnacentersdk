# -*- coding: utf-8 -*-
"""DNACenterAPI file API fixtures and tests.

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
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.1', reason='version does not match')


def is_valid_get_list_of_available_namespaces(obj):
    json_schema_validate('jsd_3f89bbfc4f6b8b50_v1_3_1').validate(obj)
    return True


def get_list_of_available_namespaces(api):
    endpoint_result = api.file.get_list_of_available_namespaces(

    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_available_namespaces(api):
    assert is_valid_get_list_of_available_namespaces(
        get_list_of_available_namespaces(api)
    )


def get_list_of_available_namespaces_default(api):
    endpoint_result = api.file.get_list_of_available_namespaces(

    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_available_namespaces_default(api):
    try:
        assert is_valid_get_list_of_available_namespaces(
            get_list_of_available_namespaces_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_list_of_files(obj):
    json_schema_validate('jsd_42b6a86e44b8bdfc_v1_3_1').validate(obj)
    return True


def get_list_of_files(api):
    endpoint_result = api.file.get_list_of_files(
        name_space='string'
    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_files(api):
    assert is_valid_get_list_of_files(
        get_list_of_files(api)
    )


def get_list_of_files_default(api):
    endpoint_result = api.file.get_list_of_files(
        name_space='string'
    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_files_default(api):
    try:
        assert is_valid_get_list_of_files(
            get_list_of_files_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_download_a_file_by_fileid(obj):
    json_schema_validate('jsd_9698c8ec4a0b8c1a_v1_3_1').validate(obj)
    return True


def download_a_file_by_fileid(api):
    endpoint_result = api.file.download_a_file_by_fileid(
        dirpath=None,
        save_file=None,
        file_id='string'
    )
    return endpoint_result


@pytest.mark.file
def test_download_a_file_by_fileid(api):
    assert is_valid_download_a_file_by_fileid(
        download_a_file_by_fileid(api)
    )


def download_a_file_by_fileid_default(api):
    endpoint_result = api.file.download_a_file_by_fileid(
        dirpath=None,
        save_file=None,
        file_id='string'
    )
    return endpoint_result


@pytest.mark.file
def test_download_a_file_by_fileid_default(api):
    try:
        assert is_valid_download_a_file_by_fileid(
            download_a_file_by_fileid_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

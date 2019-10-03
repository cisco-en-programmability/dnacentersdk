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
import dnacentersdk
import time
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_get_list_of_available_namespaces(obj):
    json_schema_validate('jsd_3f89bbfc4f6b8b50_v1_2_10').validate(obj)
    return True


def get_list_of_available_namespaces(api):
    endpoint_result = api.file.get_list_of_available_namespaces(
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_available_namespaces(api):
    assert is_valid_get_list_of_available_namespaces(
        get_list_of_available_namespaces(api)
    )


def is_valid_get_list_of_files(obj):
    json_schema_validate('jsd_42b6a86e44b8bdfc_v1_2_10').validate(obj)
    return True


def get_list_of_files(api):
    endpoint_result = api.file.get_list_of_files(
        name_space=get_list_of_available_namespaces(api).response[0],
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_files(api):
    assert is_valid_get_list_of_files(
        get_list_of_files(api)
    )


def is_valid_download_a_file_by_fileid(obj):
    json_schema_validate('jsd_9698c8ec4a0b8c1a_v1_2_10').validate(obj)
    return True


def download_a_file_by_fileid(api):
    endpoint_result = api.file.download_a_file_by_fileid(
        file_id=get_list_of_files(api).response[0].id,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.file
def test_download_a_file_by_fileid(api):
    assert is_valid_download_a_file_by_fileid(
        download_a_file_by_fileid(api)
    )

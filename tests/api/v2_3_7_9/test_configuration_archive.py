# -*- coding: utf-8 -*-
"""CatalystCenterAPI configuration_archive API fixtures and tests.

Copyright (c) 2024 Cisco Systems.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.9', reason='version does not match')


def is_valid_export_device_configurations_v1(json_schema_validate, obj):
    json_schema_validate('jsd_e85b40c5ca055f4c82281617a8f95644_v2_3_7_9').validate(obj)
    return True


def export_device_configurations_v1(api):
    endpoint_result = api.configuration_archive.export_device_configurations_v1(
        active_validation=True,
        deviceId=['string'],
        password='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_export_device_configurations_v1(api, validator):
    try:
        assert is_valid_export_device_configurations_v1(
            validator,
            export_device_configurations_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def export_device_configurations_v1_default_val(api):
    endpoint_result = api.configuration_archive.export_device_configurations_v1(
        active_validation=True,
        deviceId=None,
        password=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_export_device_configurations_v1_default_val(api, validator):
    try:
        assert is_valid_export_device_configurations_v1(
            validator,
            export_device_configurations_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_configuration_archive_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_4ff699112d3854d99557dc1f48987f09_v2_3_7_9').validate(obj)
    return True


def get_configuration_archive_details_v1(api):
    endpoint_result = api.configuration_archive.get_configuration_archive_details_v1(
        created_by='string',
        created_time='string',
        device_id='string',
        file_type='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_get_configuration_archive_details_v1(api, validator):
    try:
        assert is_valid_get_configuration_archive_details_v1(
            validator,
            get_configuration_archive_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_configuration_archive_details_v1_default_val(api):
    endpoint_result = api.configuration_archive.get_configuration_archive_details_v1(
        created_by=None,
        created_time=None,
        device_id=None,
        file_type=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_get_configuration_archive_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_configuration_archive_details_v1(
            validator,
            get_configuration_archive_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device_configuration_file_details_v1(json_schema_validate, obj):
    json_schema_validate('jsd_73c07ca5c25f5084ae4148ce8b1ce940_v2_3_7_9').validate(obj)
    return True


def get_network_device_configuration_file_details_v1(api):
    endpoint_result = api.configuration_archive.get_network_device_configuration_file_details_v1(
        file_type='string',
        id='string',
        limit=0,
        network_device_id='string',
        offset=0
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_get_network_device_configuration_file_details_v1(api, validator):
    try:
        assert is_valid_get_network_device_configuration_file_details_v1(
            validator,
            get_network_device_configuration_file_details_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_device_configuration_file_details_v1_default_val(api):
    endpoint_result = api.configuration_archive.get_network_device_configuration_file_details_v1(
        file_type=None,
        id=None,
        limit=None,
        network_device_id=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_get_network_device_configuration_file_details_v1_default_val(api, validator):
    try:
        assert is_valid_get_network_device_configuration_file_details_v1(
            validator,
            get_network_device_configuration_file_details_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_of_network_device_configuration_files_v1(json_schema_validate, obj):
    json_schema_validate('jsd_789af5e273c15f6abc150e9328e4d070_v2_3_7_9').validate(obj)
    return True


def count_of_network_device_configuration_files_v1(api):
    endpoint_result = api.configuration_archive.count_of_network_device_configuration_files_v1(
        file_type='string',
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_count_of_network_device_configuration_files_v1(api, validator):
    try:
        assert is_valid_count_of_network_device_configuration_files_v1(
            validator,
            count_of_network_device_configuration_files_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def count_of_network_device_configuration_files_v1_default_val(api):
    endpoint_result = api.configuration_archive.count_of_network_device_configuration_files_v1(
        file_type=None,
        id=None,
        network_device_id=None
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_count_of_network_device_configuration_files_v1_default_val(api, validator):
    try:
        assert is_valid_count_of_network_device_configuration_files_v1(
            validator,
            count_of_network_device_configuration_files_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_configuration_file_details_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_0e8878000b5e5810be1b2630e70a5118_v2_3_7_9').validate(obj)
    return True


def get_configuration_file_details_by_id_v1(api):
    endpoint_result = api.configuration_archive.get_configuration_file_details_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_get_configuration_file_details_by_id_v1(api, validator):
    try:
        assert is_valid_get_configuration_file_details_by_id_v1(
            validator,
            get_configuration_file_details_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_configuration_file_details_by_id_v1_default_val(api):
    endpoint_result = api.configuration_archive.get_configuration_file_details_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_get_configuration_file_details_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_configuration_file_details_by_id_v1(
            validator,
            get_configuration_file_details_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_download_masked_device_configuration_v1(json_schema_validate, obj):
    json_schema_validate('jsd_36fe0e28b3465084b5ee60a43602be1c_v2_3_7_9').validate(obj)
    return True


def download_masked_device_configuration_v1(api):
    endpoint_result = api.configuration_archive.download_masked_device_configuration_v1(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_download_masked_device_configuration_v1(api, validator):
    try:
        assert is_valid_download_masked_device_configuration_v1(
            validator,
            download_masked_device_configuration_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def download_masked_device_configuration_v1_default_val(api):
    endpoint_result = api.configuration_archive.download_masked_device_configuration_v1(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_download_masked_device_configuration_v1_default_val(api, validator):
    try:
        assert is_valid_download_masked_device_configuration_v1(
            validator,
            download_masked_device_configuration_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_download_unmaskedraw_device_configuration_as_z_ip_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d8fcd6dbb7ff53b58f7398c49b27ded2_v2_3_7_9').validate(obj)
    return True


def download_unmaskedraw_device_configuration_as_z_ip_v1(api):
    endpoint_result = api.configuration_archive.download_unmaskedraw_device_configuration_as_z_ip_v1(
        active_validation=True,
        id='string',
        password='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_download_unmaskedraw_device_configuration_as_z_ip_v1(api, validator):
    try:
        assert is_valid_download_unmaskedraw_device_configuration_as_z_ip_v1(
            validator,
            download_unmaskedraw_device_configuration_as_z_ip_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def download_unmaskedraw_device_configuration_as_z_ip_v1_default_val(api):
    endpoint_result = api.configuration_archive.download_unmaskedraw_device_configuration_as_z_ip_v1(
        active_validation=True,
        id='string',
        password=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.configuration_archive
def test_download_unmaskedraw_device_configuration_as_z_ip_v1_default_val(api, validator):
    try:
        assert is_valid_download_unmaskedraw_device_configuration_as_z_ip_v1(
            validator,
            download_unmaskedraw_device_configuration_as_z_ip_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
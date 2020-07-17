# -*- coding: utf-8 -*-
"""DNACenterAPI network_settings API fixtures and tests.

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


def is_valid_get_device_credential_details(obj):
    json_schema_validate('jsd_899f08e7401b82dd_v1_3_1').validate(obj)
    return True


def get_device_credential_details(api):
    endpoint_result = api.network_settings.get_device_credential_details(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_details(api):
    assert is_valid_get_device_credential_details(
        get_device_credential_details(api)
    )


def get_device_credential_details_default(api):
    endpoint_result = api.network_settings.get_device_credential_details(
        site_id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_details_default(api):
    try:
        assert is_valid_get_device_credential_details(
            get_device_credential_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_global_pool(obj):
    json_schema_validate('jsd_c0bca85643c8b58d_v1_3_1').validate(obj)
    return True


def get_global_pool(api):
    endpoint_result = api.network_settings.get_global_pool(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_global_pool(api):
    assert is_valid_get_global_pool(
        get_global_pool(api)
    )


def get_global_pool_default(api):
    endpoint_result = api.network_settings.get_global_pool(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_global_pool_default(api):
    try:
        assert is_valid_get_global_pool(
            get_global_pool_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_device_credential(obj):
    json_schema_validate('jsd_259eab3045988958_v1_3_1').validate(obj)
    return True


def delete_device_credential(api):
    endpoint_result = api.network_settings.delete_device_credential(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_device_credential(api):
    assert is_valid_delete_device_credential(
        delete_device_credential(api)
    )


def delete_device_credential_default(api):
    endpoint_result = api.network_settings.delete_device_credential(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_device_credential_default(api):
    try:
        assert is_valid_delete_device_credential(
            delete_device_credential_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_sp_profile(obj):
    json_schema_validate('jsd_4ca2db1143ebb5d7_v1_3_1').validate(obj)
    return True


def delete_sp_profile(api):
    endpoint_result = api.network_settings.delete_sp_profile(
        sp_profile_name='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile(api):
    assert is_valid_delete_sp_profile(
        delete_sp_profile(api)
    )


def delete_sp_profile_default(api):
    endpoint_result = api.network_settings.delete_sp_profile(
        sp_profile_name='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile_default(api):
    try:
        assert is_valid_delete_sp_profile(
            delete_sp_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_service_provider_details(obj):
    json_schema_validate('jsd_70847bdc4d89a437_v1_3_1').validate(obj)
    return True


def get_service_provider_details(api):
    endpoint_result = api.network_settings.get_service_provider_details(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details(api):
    assert is_valid_get_service_provider_details(
        get_service_provider_details(api)
    )


def get_service_provider_details_default(api):
    endpoint_result = api.network_settings.get_service_provider_details(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details_default(api):
    try:
        assert is_valid_get_service_provider_details(
            get_service_provider_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_global_ip_pool(obj):
    json_schema_validate('jsd_1eaa8b2148ab81de_v1_3_1').validate(obj)
    return True


def delete_global_ip_pool(api):
    endpoint_result = api.network_settings.delete_global_ip_pool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_global_ip_pool(api):
    assert is_valid_delete_global_ip_pool(
        delete_global_ip_pool(api)
    )


def delete_global_ip_pool_default(api):
    endpoint_result = api.network_settings.delete_global_ip_pool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_global_ip_pool_default(api):
    try:
        assert is_valid_delete_global_ip_pool(
            delete_global_ip_pool_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

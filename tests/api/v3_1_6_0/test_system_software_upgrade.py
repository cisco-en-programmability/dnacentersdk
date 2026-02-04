# -*- coding: utf-8 -*-
"""DNACenterAPI system_software_upgrade API fixtures and tests.

Copyright (c) 2025 Cisco Systems.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '3.1.6.0', reason='version does not match')


def is_valid_delete_downloaded_release(json_schema_validate, obj):
    json_schema_validate('jsd_87119b57f9a355d58e4a951d3db3f293_v3_1_6_0').validate(obj)
    return True


def delete_downloaded_release(api):
    endpoint_result = api.system_software_upgrade.delete_downloaded_release(
        release_name='string',
        release_version='string'
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_delete_downloaded_release(api, validator):
    try:
        assert is_valid_delete_downloaded_release(
            validator,
            delete_downloaded_release(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_downloaded_release_default_val(api):
    endpoint_result = api.system_software_upgrade.delete_downloaded_release(
        release_name=None,
        release_version=None
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_delete_downloaded_release_default_val(api, validator):
    try:
        assert is_valid_delete_downloaded_release(
            validator,
            delete_downloaded_release_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_download_release(json_schema_validate, obj):
    json_schema_validate('jsd_07f57dc44184564cb97a6573a44ad394_v3_1_6_0').validate(obj)
    return True


def download_release(api):
    endpoint_result = api.system_software_upgrade.download_release(
        active_validation=True,
        optionalPackages=['string'],
        payload=None,
        releaseName='string',
        releaseVersion='string'
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_download_release(api, validator):
    try:
        assert is_valid_download_release(
            validator,
            download_release(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def download_release_default_val(api):
    endpoint_result = api.system_software_upgrade.download_release(
        active_validation=True,
        optionalPackages=None,
        payload=None,
        releaseName=None,
        releaseVersion=None
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_download_release_default_val(api, validator):
    try:
        assert is_valid_download_release(
            validator,
            download_release_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_downloaded_release(json_schema_validate, obj):
    json_schema_validate('jsd_e4ddf9b60efb59ac8f6a200a563d9d72_v3_1_6_0').validate(obj)
    return True


def update_downloaded_release(api):
    endpoint_result = api.system_software_upgrade.update_downloaded_release(
        active_validation=True,
        optionalPackages=['string'],
        payload=None,
        releaseName='string',
        releaseVersion='string'
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_update_downloaded_release(api, validator):
    try:
        assert is_valid_update_downloaded_release(
            validator,
            update_downloaded_release(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_downloaded_release_default_val(api):
    endpoint_result = api.system_software_upgrade.update_downloaded_release(
        active_validation=True,
        optionalPackages=None,
        payload=None,
        releaseName=None,
        releaseVersion=None
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_update_downloaded_release_default_val(api, validator):
    try:
        assert is_valid_update_downloaded_release(
            validator,
            update_downloaded_release_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_install_optional_packages(json_schema_validate, obj):
    json_schema_validate('jsd_5f2dc0b2dd265d3bb69c5aeb5cff2f13_v3_1_6_0').validate(obj)
    return True


def install_optional_packages(api):
    endpoint_result = api.system_software_upgrade.install_optional_packages(
        active_validation=True,
        optionalPackages=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_install_optional_packages(api, validator):
    try:
        assert is_valid_install_optional_packages(
            validator,
            install_optional_packages(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def install_optional_packages_default_val(api):
    endpoint_result = api.system_software_upgrade.install_optional_packages(
        active_validation=True,
        optionalPackages=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_install_optional_packages_default_val(api, validator):
    try:
        assert is_valid_install_optional_packages(
            validator,
            install_optional_packages_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_installed_release_details(json_schema_validate, obj):
    json_schema_validate('jsd_81af1fd1bd1557b880106f71c5db9f66_v3_1_6_0').validate(obj)
    return True


def get_installed_release_details(api):
    endpoint_result = api.system_software_upgrade.get_installed_release_details(

    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_get_installed_release_details(api, validator):
    try:
        assert is_valid_get_installed_release_details(
            validator,
            get_installed_release_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_installed_release_details_default_val(api):
    endpoint_result = api.system_software_upgrade.get_installed_release_details(

    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_get_installed_release_details_default_val(api, validator):
    try:
        assert is_valid_get_installed_release_details(
            validator,
            get_installed_release_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_release(json_schema_validate, obj):
    json_schema_validate('jsd_fc2a12b907a35a92a47b7877b5207c4d_v3_1_6_0').validate(obj)
    return True


def get_all_release(api):
    endpoint_result = api.system_software_upgrade.get_all_release(

    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_get_all_release(api, validator):
    try:
        assert is_valid_get_all_release(
            validator,
            get_all_release(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_release_default_val(api):
    endpoint_result = api.system_software_upgrade.get_all_release(

    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_get_all_release_default_val(api, validator):
    try:
        assert is_valid_get_all_release(
            validator,
            get_all_release_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_release_detail(json_schema_validate, obj):
    json_schema_validate('jsd_a0c33ecb0a475f55b3518736d8a9c601_v3_1_6_0').validate(obj)
    return True


def get_release_detail(api):
    endpoint_result = api.system_software_upgrade.get_release_detail(
        release_name='string',
        release_version='string'
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_get_release_detail(api, validator):
    try:
        assert is_valid_get_release_detail(
            validator,
            get_release_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_release_detail_default_val(api):
    endpoint_result = api.system_software_upgrade.get_release_detail(
        release_name=None,
        release_version=None
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_get_release_detail_default_val(api, validator):
    try:
        assert is_valid_get_release_detail(
            validator,
            get_release_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_software_management_execution_details(json_schema_validate, obj):
    json_schema_validate('jsd_fc20a7cd31655bf1ae775e4bf645a9e1_v3_1_6_0').validate(obj)
    return True


def get_software_management_execution_details(api):
    endpoint_result = api.system_software_upgrade.get_software_management_execution_details(
        id='string'
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_get_software_management_execution_details(api, validator):
    try:
        assert is_valid_get_software_management_execution_details(
            validator,
            get_software_management_execution_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_software_management_execution_details_default_val(api):
    endpoint_result = api.system_software_upgrade.get_software_management_execution_details(
        id='string'
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_get_software_management_execution_details_default_val(api, validator):
    try:
        assert is_valid_get_software_management_execution_details(
            validator,
            get_software_management_execution_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_uninstall_optional_packages(json_schema_validate, obj):
    json_schema_validate('jsd_460d0456ad1d5bda99f7d9254f8a1ec3_v3_1_6_0').validate(obj)
    return True


def uninstall_optional_packages(api):
    endpoint_result = api.system_software_upgrade.uninstall_optional_packages(
        active_validation=True,
        optionalPackages=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_uninstall_optional_packages(api, validator):
    try:
        assert is_valid_uninstall_optional_packages(
            validator,
            uninstall_optional_packages(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def uninstall_optional_packages_default_val(api):
    endpoint_result = api.system_software_upgrade.uninstall_optional_packages(
        active_validation=True,
        optionalPackages=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_uninstall_optional_packages_default_val(api, validator):
    try:
        assert is_valid_uninstall_optional_packages(
            validator,
            uninstall_optional_packages_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_upgrade_release(json_schema_validate, obj):
    json_schema_validate('jsd_09791c90586f562b8fc0451b7e71b35a_v3_1_6_0').validate(obj)
    return True


def upgrade_release(api):
    endpoint_result = api.system_software_upgrade.upgrade_release(
        active_validation=True,
        optionalPackages=['string'],
        payload=None,
        releaseName='string',
        releaseVersion='string'
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_upgrade_release(api, validator):
    try:
        assert is_valid_upgrade_release(
            validator,
            upgrade_release(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def upgrade_release_default_val(api):
    endpoint_result = api.system_software_upgrade.upgrade_release(
        active_validation=True,
        optionalPackages=None,
        payload=None,
        releaseName=None,
        releaseVersion=None
    )
    return endpoint_result


@pytest.mark.system_software_upgrade
def test_upgrade_release_default_val(api, validator):
    try:
        assert is_valid_upgrade_release(
            validator,
            upgrade_release_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

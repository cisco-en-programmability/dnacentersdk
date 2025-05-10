# -*- coding: utf-8 -*-
"""CatalystCenterAPI backup API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '3.1.3.0', reason='version does not match')


def is_valid_get_backup_configuration_v1(json_schema_validate, obj):
    json_schema_validate('jsd_dd47c40ef6e75dfeb079b162f5e1d594_v3_1_3_0').validate(obj)
    return True


def get_backup_configuration_v1(api):
    endpoint_result = api.backup.get_backup_configuration_v1(

    )
    return endpoint_result


@pytest.mark.backup
def test_get_backup_configuration_v1(api, validator):
    try:
        assert is_valid_get_backup_configuration_v1(
            validator,
            get_backup_configuration_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_backup_configuration_v1_default_val(api):
    endpoint_result = api.backup.get_backup_configuration_v1(

    )
    return endpoint_result


@pytest.mark.backup
def test_get_backup_configuration_v1_default_val(api, validator):
    try:
        assert is_valid_get_backup_configuration_v1(
            validator,
            get_backup_configuration_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_backup_configuration_v1(json_schema_validate, obj):
    json_schema_validate('jsd_b843a90c86875472af1f351e78dd5521_v3_1_3_0').validate(obj)
    return True


def create_backup_configuration_v1(api):
    endpoint_result = api.backup.create_backup_configuration_v1(
        active_validation=True,
        dataRetention=0,
        encryptionPassphrase='string',
        mountPath='string',
        payload=None,
        type='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_create_backup_configuration_v1(api, validator):
    try:
        assert is_valid_create_backup_configuration_v1(
            validator,
            create_backup_configuration_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_backup_configuration_v1_default_val(api):
    endpoint_result = api.backup.create_backup_configuration_v1(
        active_validation=True,
        dataRetention=None,
        encryptionPassphrase=None,
        mountPath=None,
        payload=None,
        type=None
    )
    return endpoint_result


@pytest.mark.backup
def test_create_backup_configuration_v1_default_val(api, validator):
    try:
        assert is_valid_create_backup_configuration_v1(
            validator,
            create_backup_configuration_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_n_f_s_configuration_v1(json_schema_validate, obj):
    json_schema_validate('jsd_2e9c39175d785a0eb9d6f402f378a2ba_v3_1_3_0').validate(obj)
    return True


def create_n_f_s_configuration_v1(api):
    endpoint_result = api.backup.create_n_f_s_configuration_v1(
        active_validation=True,
        nfsPort=0,
        nfsVersion='string',
        payload=None,
        portMapperPort=0,
        server='string',
        sourcePath='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_create_n_f_s_configuration_v1(api, validator):
    try:
        assert is_valid_create_n_f_s_configuration_v1(
            validator,
            create_n_f_s_configuration_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_n_f_s_configuration_v1_default_val(api):
    endpoint_result = api.backup.create_n_f_s_configuration_v1(
        active_validation=True,
        nfsPort=None,
        nfsVersion=None,
        payload=None,
        portMapperPort=None,
        server=None,
        sourcePath=None
    )
    return endpoint_result


@pytest.mark.backup
def test_create_n_f_s_configuration_v1_default_val(api, validator):
    try:
        assert is_valid_create_n_f_s_configuration_v1(
            validator,
            create_n_f_s_configuration_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_n_f_s_configurations_v1(json_schema_validate, obj):
    json_schema_validate('jsd_f7ccd6a28585516e9858e43b24f5f63d_v3_1_3_0').validate(obj)
    return True


def get_all_n_f_s_configurations_v1(api):
    endpoint_result = api.backup.get_all_n_f_s_configurations_v1(

    )
    return endpoint_result


@pytest.mark.backup
def test_get_all_n_f_s_configurations_v1(api, validator):
    try:
        assert is_valid_get_all_n_f_s_configurations_v1(
            validator,
            get_all_n_f_s_configurations_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_n_f_s_configurations_v1_default_val(api):
    endpoint_result = api.backup.get_all_n_f_s_configurations_v1(

    )
    return endpoint_result


@pytest.mark.backup
def test_get_all_n_f_s_configurations_v1_default_val(api, validator):
    try:
        assert is_valid_get_all_n_f_s_configurations_v1(
            validator,
            get_all_n_f_s_configurations_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_n_f_s_configuration_v1(json_schema_validate, obj):
    json_schema_validate('jsd_d7282ec01a275f5d9c093c2a4b2cf6af_v3_1_3_0').validate(obj)
    return True


def delete_n_f_s_configuration_v1(api):
    endpoint_result = api.backup.delete_n_f_s_configuration_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_delete_n_f_s_configuration_v1(api, validator):
    try:
        assert is_valid_delete_n_f_s_configuration_v1(
            validator,
            delete_n_f_s_configuration_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_n_f_s_configuration_v1_default_val(api):
    endpoint_result = api.backup.delete_n_f_s_configuration_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_delete_n_f_s_configuration_v1_default_val(api, validator):
    try:
        assert is_valid_delete_n_f_s_configuration_v1(
            validator,
            delete_n_f_s_configuration_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_backup_and_restore_executions_v1(json_schema_validate, obj):
    json_schema_validate('jsd_07e87332fa345c06b01cc351ca31a35c_v3_1_3_0').validate(obj)
    return True


def get_backup_and_restore_executions_v1(api):
    endpoint_result = api.backup.get_backup_and_restore_executions_v1(
        backup_id='string',
        job_type='string',
        limit=0,
        offset=0,
        order='string',
        sort_by='string',
        status='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_get_backup_and_restore_executions_v1(api, validator):
    try:
        assert is_valid_get_backup_and_restore_executions_v1(
            validator,
            get_backup_and_restore_executions_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_backup_and_restore_executions_v1_default_val(api):
    endpoint_result = api.backup.get_backup_and_restore_executions_v1(
        backup_id=None,
        job_type=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        status=None
    )
    return endpoint_result


@pytest.mark.backup
def test_get_backup_and_restore_executions_v1_default_val(api, validator):
    try:
        assert is_valid_get_backup_and_restore_executions_v1(
            validator,
            get_backup_and_restore_executions_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_backup_and_restore_execution_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6461aa285ec05ff68b1101c7a15254e3_v3_1_3_0').validate(obj)
    return True


def get_backup_and_restore_execution_v1(api):
    endpoint_result = api.backup.get_backup_and_restore_execution_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_get_backup_and_restore_execution_v1(api, validator):
    try:
        assert is_valid_get_backup_and_restore_execution_v1(
            validator,
            get_backup_and_restore_execution_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_backup_and_restore_execution_v1_default_val(api):
    endpoint_result = api.backup.get_backup_and_restore_execution_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_get_backup_and_restore_execution_v1_default_val(api, validator):
    try:
        assert is_valid_get_backup_and_restore_execution_v1(
            validator,
            get_backup_and_restore_execution_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_backup_storages_v1(json_schema_validate, obj):
    json_schema_validate('jsd_adbfee1ef7015fbfb1bd47020ab90f89_v3_1_3_0').validate(obj)
    return True


def get_backup_storages_v1(api):
    endpoint_result = api.backup.get_backup_storages_v1(
        storage_type='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_get_backup_storages_v1(api, validator):
    try:
        assert is_valid_get_backup_storages_v1(
            validator,
            get_backup_storages_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_backup_storages_v1_default_val(api):
    endpoint_result = api.backup.get_backup_storages_v1(
        storage_type=None
    )
    return endpoint_result


@pytest.mark.backup
def test_get_backup_storages_v1_default_val(api, validator):
    try:
        assert is_valid_get_backup_storages_v1(
            validator,
            get_backup_storages_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_backup_v1(json_schema_validate, obj):
    json_schema_validate('jsd_6f09b1316bea5602aaadebe1102b8b86_v3_1_3_0').validate(obj)
    return True


def get_all_backup_v1(api):
    endpoint_result = api.backup.get_all_backup_v1(
        limit=0,
        offset=0,
        order='string',
        query='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_get_all_backup_v1(api, validator):
    try:
        assert is_valid_get_all_backup_v1(
            validator,
            get_all_backup_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_backup_v1_default_val(api):
    endpoint_result = api.backup.get_all_backup_v1(
        limit=None,
        offset=None,
        order=None,
        query=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.backup
def test_get_all_backup_v1_default_val(api, validator):
    try:
        assert is_valid_get_all_backup_v1(
            validator,
            get_all_backup_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_backup_v1(json_schema_validate, obj):
    json_schema_validate('jsd_7c9d3ba6208e5d6eb45fa5c9b8f7e327_v3_1_3_0').validate(obj)
    return True


def create_backup_v1(api):
    endpoint_result = api.backup.create_backup_v1(
        active_validation=True,
        name='string',
        payload=None,
        scope='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_create_backup_v1(api, validator):
    try:
        assert is_valid_create_backup_v1(
            validator,
            create_backup_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_backup_v1_default_val(api):
    endpoint_result = api.backup.create_backup_v1(
        active_validation=True,
        name=None,
        payload=None,
        scope=None
    )
    return endpoint_result


@pytest.mark.backup
def test_create_backup_v1_default_val(api, validator):
    try:
        assert is_valid_create_backup_v1(
            validator,
            create_backup_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_backup_by_id_v1(json_schema_validate, obj):
    json_schema_validate('jsd_efd1d42f31af56dd8b395df3685dd465_v3_1_3_0').validate(obj)
    return True


def get_backup_by_id_v1(api):
    endpoint_result = api.backup.get_backup_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_get_backup_by_id_v1(api, validator):
    try:
        assert is_valid_get_backup_by_id_v1(
            validator,
            get_backup_by_id_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_backup_by_id_v1_default_val(api):
    endpoint_result = api.backup.get_backup_by_id_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_get_backup_by_id_v1_default_val(api, validator):
    try:
        assert is_valid_get_backup_by_id_v1(
            validator,
            get_backup_by_id_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_backup_v1(json_schema_validate, obj):
    json_schema_validate('jsd_c468255fb65851c2b356d2dcf5397cd6_v3_1_3_0').validate(obj)
    return True


def delete_backup_v1(api):
    endpoint_result = api.backup.delete_backup_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_delete_backup_v1(api, validator):
    try:
        assert is_valid_delete_backup_v1(
            validator,
            delete_backup_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_backup_v1_default_val(api):
    endpoint_result = api.backup.delete_backup_v1(
        id='string'
    )
    return endpoint_result


@pytest.mark.backup
def test_delete_backup_v1_default_val(api, validator):
    try:
        assert is_valid_delete_backup_v1(
            validator,
            delete_backup_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

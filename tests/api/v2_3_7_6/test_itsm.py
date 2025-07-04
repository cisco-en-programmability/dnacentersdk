# -*- coding: utf-8 -*-
"""DNACenterAPI itsm API fixtures and tests.

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

pytestmark = pytest.mark.skipif(
    DNA_CENTER_VERSION != "2.3.7.6", reason="version does not match"
)


def is_valid_get_cmdb_sync_status_v1(json_schema_validate, obj):
    json_schema_validate("jsd_46eb1bf346225a4ba24f18408ffca7c9_v2_3_7_6").validate(obj)
    return True


def get_cmdb_sync_status_v1(api):
    endpoint_result = api.itsm.get_cmdb_sync_status_v1(date="string", status="string")
    return endpoint_result


@pytest.mark.itsm
def test_get_cmdb_sync_status_v1(api, validator):
    try:
        assert is_valid_get_cmdb_sync_status_v1(validator, get_cmdb_sync_status_v1(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_cmdb_sync_status_v1_default_val(api):
    endpoint_result = api.itsm.get_cmdb_sync_status_v1(date=None, status=None)
    return endpoint_result


@pytest.mark.itsm
def test_get_cmdb_sync_status_v1_default_val(api, validator):
    try:
        assert is_valid_get_cmdb_sync_status_v1(
            validator, get_cmdb_sync_status_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_failed_itsm_events_v1(json_schema_validate, obj):
    json_schema_validate("jsd_da70082b298a5a908edb780a61bd4ca6_v2_3_7_6").validate(obj)
    return True


def get_failed_itsm_events_v1(api):
    endpoint_result = api.itsm.get_failed_itsm_events_v1(instance_id="string")
    return endpoint_result


@pytest.mark.itsm
def test_get_failed_itsm_events_v1(api, validator):
    try:
        assert is_valid_get_failed_itsm_events_v1(
            validator, get_failed_itsm_events_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_failed_itsm_events_v1_default_val(api):
    endpoint_result = api.itsm.get_failed_itsm_events_v1(instance_id=None)
    return endpoint_result


@pytest.mark.itsm
def test_get_failed_itsm_events_v1_default_val(api, validator):
    try:
        assert is_valid_get_failed_itsm_events_v1(
            validator, get_failed_itsm_events_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retry_integration_events_v1(json_schema_validate, obj):
    json_schema_validate("jsd_25624cfb1d6e52878d057740de275896_v2_3_7_6").validate(obj)
    return True


def retry_integration_events_v1(api):
    endpoint_result = api.itsm.retry_integration_events_v1(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.itsm
def test_retry_integration_events_v1(api, validator):
    try:
        assert is_valid_retry_integration_events_v1(
            validator, retry_integration_events_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retry_integration_events_v1_default_val(api):
    endpoint_result = api.itsm.retry_integration_events_v1(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.itsm
def test_retry_integration_events_v1_default_val(api, validator):
    try:
        assert is_valid_retry_integration_events_v1(
            validator, retry_integration_events_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

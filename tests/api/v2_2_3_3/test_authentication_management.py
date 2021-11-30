# -*- coding: utf-8 -*-
"""DNACenterAPI authentication_management API fixtures and tests.

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


def is_valid_import_certificate(json_schema_validate, obj):
    json_schema_validate('jsd_b19d7e8de2ca5329930d06f041a4a173_v2_2_3_3').validate(obj)
    return True


def import_certificate(api):
    endpoint_result = api.authentication_management.import_certificate(
        multipart_fields={'file': ('test-1592357065255.csv', open('./tests/test-1592357065255.csv', 'rb'))},
        multipart_monitor_callback=None,
        active_validation=True,
        list_of_users='value1,value2',
        payload=None,
        pk_password='string'
    )
    return endpoint_result


@pytest.mark.authentication_management
def test_import_certificate(api, validator):
    try:
        assert is_valid_import_certificate(
            validator,
            import_certificate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_certificate_default_val(api):
    endpoint_result = api.authentication_management.import_certificate(
        multipart_fields={'file': ('test-1592357065255.csv', open('./tests/test-1592357065255.csv', 'rb'))},
        multipart_monitor_callback=None,
        active_validation=True,
        list_of_users=None,
        payload=None,
        pk_password=None
    )
    return endpoint_result


@pytest.mark.authentication_management
def test_import_certificate_default_val(api, validator):
    try:
        assert is_valid_import_certificate(
            validator,
            import_certificate_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_certificate_p12(json_schema_validate, obj):
    json_schema_validate('jsd_c80e660c2e36582f939a7403ef15de22_v2_2_3_3').validate(obj)
    return True


def import_certificate_p12(api):
    endpoint_result = api.authentication_management.import_certificate_p12(
        multipart_fields={'file': ('test-1592357065255.csv', open('./tests/test-1592357065255.csv', 'rb'))},
        multipart_monitor_callback=None,
        active_validation=True,
        list_of_users='value1,value2',
        p12_password='string',
        payload=None,
        pk_password='string'
    )
    return endpoint_result


@pytest.mark.authentication_management
def test_import_certificate_p12(api, validator):
    try:
        assert is_valid_import_certificate_p12(
            validator,
            import_certificate_p12(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_certificate_p12_default_val(api):
    endpoint_result = api.authentication_management.import_certificate_p12(
        multipart_fields={'file': ('test-1592357065255.csv', open('./tests/test-1592357065255.csv', 'rb'))},
        multipart_monitor_callback=None,
        active_validation=True,
        list_of_users=None,
        p12_password=None,
        payload=None,
        pk_password=None
    )
    return endpoint_result


@pytest.mark.authentication_management
def test_import_certificate_p12_default_val(api, validator):
    try:
        assert is_valid_import_certificate_p12(
            validator,
            import_certificate_p12_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

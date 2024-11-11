# -*- coding: utf-8 -*-
"""DNACenterAPI cisco_trusted_certificates API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.6', reason='version does not match')


def is_valid_import_trusted_certificate_v1(json_schema_validate, obj):
    json_schema_validate('jsd_ebe0eab8e1785bec83a1e155112fb70e_v2_3_7_6').validate(obj)
    return True


def import_trusted_certificate_v1(api):
    endpoint_result = api.cisco_trusted_certificates.import_trusted_certificate_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.cisco_trusted_certificates
def test_import_trusted_certificate_v1(api, validator):
    try:
        assert is_valid_import_trusted_certificate_v1(
            validator,
            import_trusted_certificate_v1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def import_trusted_certificate_v1_default_val(api):
    endpoint_result = api.cisco_trusted_certificates.import_trusted_certificate_v1(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.cisco_trusted_certificates
def test_import_trusted_certificate_v1_default_val(api, validator):
    try:
        assert is_valid_import_trusted_certificate_v1(
            validator,
            import_trusted_certificate_v1_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

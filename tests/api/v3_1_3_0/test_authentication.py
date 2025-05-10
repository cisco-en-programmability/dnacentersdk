# -*- coding: utf-8 -*-
"""CatalystCenterAPI authentication API fixtures and tests.

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
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '3.1.3.0', reason='version does not match')


def is_valid_authentication_api(json_schema_validate, obj):
    json_schema_validate('jsd_ac8ae94c4e69a09d_v3_1_3_0').validate(obj)
    return True


def authentication_api(api):
    endpoint_result = api.authentication.authentication_api(
        username='CATALYST_CENTER_USERNAME',
        password='CATALYST_CENTER_PASSWORD'
    )
    return endpoint_result


@pytest.mark.authentication
def test_authentication_api(api, validator):
    assert is_valid_authentication_api(
        validator,
        authentication_api(api)
    )


def authentication_api_default(api):
    endpoint_result = api.authentication.authentication_api(
        username='CATALYST_CENTER_USERNAME',
        password='CATALYST_CENTER_PASSWORD'
    )
    return endpoint_result


@pytest.mark.authentication
def test_authentication_api_default(api, validator):
    try:
        assert is_valid_authentication_api(
            validator,
            authentication_api_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

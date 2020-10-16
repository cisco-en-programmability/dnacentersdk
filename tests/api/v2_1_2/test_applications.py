# -*- coding: utf-8 -*-
"""DNACenterAPI applications API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.1.2', reason='version does not match')


def is_valid_applications(json_schema_validate, obj):
    json_schema_validate('jsd_2db58a1f4fea9242_v2_1_2').validate(obj)
    return True


def applications(api):
    endpoint_result = api.applications.applications(
        application_health='string',
        device_id='string',
        end_time=0,
        limit=0,
        mac_address='string',
        offset=0,
        site_id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.applications
def test_applications(api, validator):
    assert is_valid_applications(
        validator,
        applications(api)
    )


def applications_default(api):
    endpoint_result = api.applications.applications(
        application_health=None,
        device_id=None,
        end_time=None,
        limit=None,
        mac_address=None,
        offset=None,
        site_id=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.applications
def test_applications_default(api, validator):
    try:
        assert is_valid_applications(
            validator,
            applications_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

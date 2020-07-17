# -*- coding: utf-8 -*-
"""DNACenterAPI itsm API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.1.1', reason='version does not match')


def is_valid_get_failed_itsm_events(obj):
    json_schema_validate('jsd_a293b82a42a8ab15_v2_1_1').validate(obj)
    return True


def get_failed_itsm_events(api):
    endpoint_result = api.itsm.get_failed_itsm_events(
        instance_id='string'
    )
    return endpoint_result


@pytest.mark.itsm
def test_get_failed_itsm_events(api):
    assert is_valid_get_failed_itsm_events(
        get_failed_itsm_events(api)
    )


def get_failed_itsm_events_default(api):
    endpoint_result = api.itsm.get_failed_itsm_events(
        instance_id=None
    )
    return endpoint_result


@pytest.mark.itsm
def test_get_failed_itsm_events_default(api):
    try:
        assert is_valid_get_failed_itsm_events(
            get_failed_itsm_events_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_retry_integration_events(obj):
    json_schema_validate('jsd_fa9a98174129af50_v2_1_1').validate(obj)
    return True


def retry_integration_events(api):
    endpoint_result = api.itsm.retry_integration_events(
        active_validation=True,
        payload=['string']
    )
    return endpoint_result


@pytest.mark.itsm
def test_retry_integration_events(api):
    assert is_valid_retry_integration_events(
        retry_integration_events(api)
    )


def retry_integration_events_default(api):
    endpoint_result = api.itsm.retry_integration_events(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.itsm
def test_retry_integration_events_default(api):
    try:
        assert is_valid_retry_integration_events(
            retry_integration_events_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

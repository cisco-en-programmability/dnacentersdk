# -*- coding: utf-8 -*-
"""DNACenterAPI security_advisories API fixtures and tests.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.1', reason='version does not match')


def is_valid_get_advisories_summary(json_schema_validate, obj):
    json_schema_validate('jsd_3ebf898d482b9207_v2_2_1').validate(obj)
    return True


def get_advisories_summary(api):
    endpoint_result = api.security_advisories.get_advisories_summary(

    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisories_summary(api, validator):
    assert is_valid_get_advisories_summary(
        validator,
        get_advisories_summary(api)
    )


def get_advisories_summary_default(api):
    endpoint_result = api.security_advisories.get_advisories_summary(

    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisories_summary_default(api, validator):
    try:
        assert is_valid_get_advisories_summary(
            validator,
            get_advisories_summary_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_advisories_list(json_schema_validate, obj):
    json_schema_validate('jsd_42950bf84939ac35_v2_2_1').validate(obj)
    return True


def get_advisories_list(api):
    endpoint_result = api.security_advisories.get_advisories_list(

    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisories_list(api, validator):
    assert is_valid_get_advisories_list(
        validator,
        get_advisories_list(api)
    )


def get_advisories_list_default(api):
    endpoint_result = api.security_advisories.get_advisories_list(

    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisories_list_default(api, validator):
    try:
        assert is_valid_get_advisories_list(
            validator,
            get_advisories_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_advisories_per_device(json_schema_validate, obj):
    json_schema_validate('jsd_42a6c9a14ea9b002_v2_2_1').validate(obj)
    return True


def get_advisories_per_device(api):
    endpoint_result = api.security_advisories.get_advisories_per_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisories_per_device(api, validator):
    assert is_valid_get_advisories_per_device(
        validator,
        get_advisories_per_device(api)
    )


def get_advisories_per_device_default(api):
    endpoint_result = api.security_advisories.get_advisories_per_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisories_per_device_default(api, validator):
    try:
        assert is_valid_get_advisories_per_device(
            validator,
            get_advisories_per_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_devices_per_advisory(json_schema_validate, obj):
    json_schema_validate('jsd_f49c4ae043fa8352_v2_2_1').validate(obj)
    return True


def get_devices_per_advisory(api):
    endpoint_result = api.security_advisories.get_devices_per_advisory(
        advisory_id='string'
    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_devices_per_advisory(api, validator):
    assert is_valid_get_devices_per_advisory(
        validator,
        get_devices_per_advisory(api)
    )


def get_devices_per_advisory_default(api):
    endpoint_result = api.security_advisories.get_devices_per_advisory(
        advisory_id='string'
    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_devices_per_advisory_default(api, validator):
    try:
        assert is_valid_get_devices_per_advisory(
            validator,
            get_devices_per_advisory_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_advisory_ids_per_device(json_schema_validate, obj):
    json_schema_validate('jsd_e29509d0420b8cc4_v2_2_1').validate(obj)
    return True


def get_advisory_ids_per_device(api):
    endpoint_result = api.security_advisories.get_advisory_ids_per_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisory_ids_per_device(api, validator):
    assert is_valid_get_advisory_ids_per_device(
        validator,
        get_advisory_ids_per_device(api)
    )


def get_advisory_ids_per_device_default(api):
    endpoint_result = api.security_advisories.get_advisory_ids_per_device(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.security_advisories
def test_get_advisory_ids_per_device_default(api, validator):
    try:
        assert is_valid_get_advisory_ids_per_device(
            validator,
            get_advisory_ids_per_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI sites API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.0', reason='version does not match')


def is_valid_get_site_health(obj):
    json_schema_validate('jsd_17a82ac94cf99ab0_v1_3_0').validate(obj)
    return True


def get_site_health(api):
    endpoint_result = api.sites.get_site_health(
        timestamp=0
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_health(api):
    assert is_valid_get_site_health(
        get_site_health(api)
    )


def get_site_health_default(api):
    endpoint_result = api.sites.get_site_health(
        timestamp=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_health_default(api):
    try:
        assert is_valid_get_site_health(
            get_site_health_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_update_site(obj):
    json_schema_validate('jsd_33aab9b842388023_v1_3_0').validate(obj)
    return True


def update_site(api):
    endpoint_result = api.sites.update_site(
        active_validation=True,
        payload=None,
        site={'area': {'name': 'string', 'parentName': 'string'}, 'building': {'name': 'string', 'address': 'string', 'parentName': 'string', 'latitude': 0, 'longitude': 0}, 'floor': {'name': 'string', 'rfModel': 'Cubes And Walled Offices', 'width': 0, 'length': 0, 'height': 0}},
        site_id='string',
        type='area'
    )
    return endpoint_result


@pytest.mark.sites
def test_update_site(api):
    assert is_valid_update_site(
        update_site(api)
    )


def update_site_default(api):
    endpoint_result = api.sites.update_site(
        active_validation=True,
        payload=None,
        site=None,
        site_id='string',
        type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_update_site_default(api):
    try:
        assert is_valid_update_site(
            update_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_create_site(obj):
    json_schema_validate('jsd_23896b124bd8b9bf_v1_3_0').validate(obj)
    return True


def create_site(api):
    endpoint_result = api.sites.create_site(
        active_validation=True,
        payload=None,
        site={'area': {'name': 'string', 'parentName': 'string'}, 'building': {'name': 'string', 'address': 'string', 'parentName': 'string', 'latitude': 0, 'longitude': 0}, 'floor': {'name': 'string', 'parentName': 'string', 'rfModel': 'Cubes And Walled Offices', 'width': 0, 'length': 0, 'height': 0}},
        type='area'
    )
    return endpoint_result


@pytest.mark.sites
def test_create_site(api):
    assert is_valid_create_site(
        create_site(api)
    )


def create_site_default(api):
    endpoint_result = api.sites.create_site(
        active_validation=True,
        payload=None,
        site=None,
        type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_create_site_default(api):
    try:
        assert is_valid_create_site(
            create_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_site(obj):
    json_schema_validate('jsd_209509d247599e19_v1_3_0').validate(obj)
    return True


def get_site(api):
    endpoint_result = api.sites.get_site(
        limit=0,
        name='string',
        offset=0,
        site_id='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site(api):
    assert is_valid_get_site(
        get_site(api)
    )


def get_site_default(api):
    endpoint_result = api.sites.get_site(
        limit=None,
        name=None,
        offset=None,
        site_id=None,
        type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_default(api):
    try:
        assert is_valid_get_site(
            get_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_delete_site(obj):
    json_schema_validate('jsd_92acda91406aa050_v1_3_0').validate(obj)
    return True


def delete_site(api):
    endpoint_result = api.sites.delete_site(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_delete_site(api):
    assert is_valid_delete_site(
        delete_site(api)
    )


def delete_site_default(api):
    endpoint_result = api.sites.delete_site(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_delete_site_default(api):
    try:
        assert is_valid_delete_site(
            delete_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_site_count(obj):
    json_schema_validate('jsd_d9bdb9034df99dba_v1_3_0').validate(obj)
    return True


def get_site_count(api):
    endpoint_result = api.sites.get_site_count(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_count(api):
    assert is_valid_get_site_count(
        get_site_count(api)
    )


def get_site_count_default(api):
    endpoint_result = api.sites.get_site_count(
        site_id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_count_default(api):
    try:
        assert is_valid_get_site_count(
            get_site_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_assign_device_to_site(obj):
    json_schema_validate('jsd_eeb168eb41988e07_v1_3_0').validate(obj)
    return True


def assign_device_to_site(api):
    endpoint_result = api.sites.assign_device_to_site(
        active_validation=True,
        device=[{'ip': 'string'}],
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_assign_device_to_site(api):
    assert is_valid_assign_device_to_site(
        assign_device_to_site(api)
    )


def assign_device_to_site_default(api):
    endpoint_result = api.sites.assign_device_to_site(
        active_validation=True,
        device=None,
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_assign_device_to_site_default(api):
    try:
        assert is_valid_assign_device_to_site(
            assign_device_to_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_get_membership(obj):
    json_schema_validate('jsd_eba669054e08a60e_v1_3_0').validate(obj)
    return True


def get_membership(api):
    endpoint_result = api.sites.get_membership(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_membership(api):
    assert is_valid_get_membership(
        get_membership(api)
    )


def get_membership_default(api):
    endpoint_result = api.sites.get_membership(
        site_id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_membership_default(api):
    try:
        assert is_valid_get_membership(
            get_membership_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

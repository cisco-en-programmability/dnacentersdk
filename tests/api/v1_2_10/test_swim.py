# -*- coding: utf-8 -*-
"""DNACenterAPI swim API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_get_software_image_details(obj):
    json_schema_validate('jsd_0c8f7a0b49b9aedd_v1_2_10').validate(obj)
    return True


def get_software_image_details(api):
    endpoint_result = api.swim.get_software_image_details(
        application_type='string',
        created_time=0,
        family='string',
        image_integrity_status='string',
        image_name='string',
        image_series='string',
        image_size_greater_than=0,
        image_size_lesser_than=0,
        image_uuid='string',
        is_cco_latest=True,
        is_cco_recommended=True,
        is_tagged_golden=True,
        limit=0,
        name='string',
        offset=0,
        sort_by='string',
        sort_order='asc',
        version='string'
    )
    return endpoint_result


@pytest.mark.swim
def test_get_software_image_details(api):
    assert is_valid_get_software_image_details(
        get_software_image_details(api)
    )


def get_software_image_details_default(api):
    endpoint_result = api.swim.get_software_image_details(
        application_type=None,
        created_time=None,
        family=None,
        image_integrity_status=None,
        image_name=None,
        image_series=None,
        image_size_greater_than=None,
        image_size_lesser_than=None,
        image_uuid=None,
        is_cco_latest=None,
        is_cco_recommended=None,
        is_tagged_golden=None,
        limit=None,
        name=None,
        offset=None,
        sort_by=None,
        sort_order=None,
        version=None
    )
    return endpoint_result


@pytest.mark.swim
def test_get_software_image_details_default(api):
    try:
        assert is_valid_get_software_image_details(
            get_software_image_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_trigger_software_image_distribution(obj):
    json_schema_validate('jsd_8cb6783b4faba1f4_v1_2_10').validate(obj)
    return True


def trigger_software_image_distribution(api):
    endpoint_result = api.swim.trigger_software_image_distribution(
        active_validation=True,
        payload=[{'deviceUuid': 'string', 'imageUuid': 'string'}]
    )
    return endpoint_result


@pytest.mark.swim
def test_trigger_software_image_distribution(api):
    assert is_valid_trigger_software_image_distribution(
        trigger_software_image_distribution(api)
    )


def trigger_software_image_distribution_default(api):
    endpoint_result = api.swim.trigger_software_image_distribution(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.swim
def test_trigger_software_image_distribution_default(api):
    try:
        assert is_valid_trigger_software_image_distribution(
            trigger_software_image_distribution_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_import_local_software_image(obj):
    json_schema_validate('jsd_4dbe3bc743a891bc_v1_2_10').validate(obj)
    return True


def import_local_software_image(api):
    endpoint_result = api.swim.import_local_software_image(
        multipart_fields={'file': ('test-1592357065255.csv', open('./tests/test-1592357065255.csv', 'rb'))},
        multipart_monitor_callback=None,
        is_third_party=True,
        third_party_application_type='string',
        third_party_image_family='string',
        third_party_vendor='string'
    )
    return endpoint_result


@pytest.mark.swim
def test_import_local_software_image(api):
    assert is_valid_import_local_software_image(
        import_local_software_image(api)
    )


def import_local_software_image_default(api):
    endpoint_result = api.swim.import_local_software_image(
        multipart_fields={'file': ('test-1592357065255.csv', open('./tests/test-1592357065255.csv', 'rb'))},
        multipart_monitor_callback=None,
        is_third_party=None,
        third_party_application_type=None,
        third_party_image_family=None,
        third_party_vendor=None
    )
    return endpoint_result


@pytest.mark.swim
def test_import_local_software_image_default(api):
    try:
        assert is_valid_import_local_software_image(
            import_local_software_image_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_import_software_image_via_url(obj):
    json_schema_validate('jsd_bc8aab4746ca883d_v1_2_10').validate(obj)
    return True


def import_software_image_via_url(api):
    endpoint_result = api.swim.import_software_image_via_url(
        active_validation=True,
        payload=[{'applicationType': 'string', 'imageFamily': 'string', 'sourceURL': 'string', 'thirdParty': True, 'vendor': 'string'}],
        schedule_at='string',
        schedule_desc='string',
        schedule_origin='string'
    )
    return endpoint_result


@pytest.mark.swim
def test_import_software_image_via_url(api):
    assert is_valid_import_software_image_via_url(
        import_software_image_via_url(api)
    )


def import_software_image_via_url_default(api):
    endpoint_result = api.swim.import_software_image_via_url(
        active_validation=True,
        payload=None,
        schedule_at=None,
        schedule_desc=None,
        schedule_origin=None
    )
    return endpoint_result


@pytest.mark.swim
def test_import_software_image_via_url_default(api):
    try:
        assert is_valid_import_software_image_via_url(
            import_software_image_via_url_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e


def is_valid_trigger_software_image_activation(obj):
    json_schema_validate('jsd_fb9beb664f2aba4c_v1_2_10').validate(obj)
    return True


def trigger_software_image_activation(api):
    endpoint_result = api.swim.trigger_software_image_activation(
        active_validation=True,
        payload=[{'activateLowerImageVersion': True, 'deviceUpgradeMode': 'string', 'deviceUuid': 'string', 'distributeIfNeeded': True, 'imageUuidList': ['string'], 'smuImageUuidList': ['string']}],
        schedule_validate=True
    )
    return endpoint_result


@pytest.mark.swim
def test_trigger_software_image_activation(api):
    assert is_valid_trigger_software_image_activation(
        trigger_software_image_activation(api)
    )


def trigger_software_image_activation_default(api):
    endpoint_result = api.swim.trigger_software_image_activation(
        active_validation=True,
        payload=None,
        schedule_validate=None
    )
    return endpoint_result


@pytest.mark.swim
def test_trigger_software_image_activation_default(api):
    try:
        assert is_valid_trigger_software_image_activation(
            trigger_software_image_activation_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

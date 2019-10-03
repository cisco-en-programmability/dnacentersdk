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
import dnacentersdk
import time
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate
from tests.config import LOCAL_SOFTWARE_IMAGE_PATH, LOCAL_SOFTWARE_IMAGE_NAME
from tests.config import DEFAULT_BASE_URL
from .test_file import get_list_of_files
from .test_devices import get_device_list


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_get_software_image_details(obj):
    json_schema_validate('jsd_0c8f7a0b49b9aedd_v1_2_10').validate(obj)
    return True


def get_software_image_details(api):
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
        sort_order='asc',
        version=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.swim
def test_get_software_image_details(api):
    assert is_valid_get_software_image_details(
        get_software_image_details(api)
    )


def is_valid_import_local_software_image(obj):
    json_schema_validate('jsd_4dbe3bc743a891bc_v1_2_10').validate(obj)
    return True


def import_local_software_image(api):
    endpoint_result = api.swim.import_local_software_image(
        is_third_party=None,
        third_party_application_type=None,
        third_party_image_family=None,
        third_party_vendor=None,
        multipart_fields={'file': (LOCAL_SOFTWARE_IMAGE_NAME,
                                   open(LOCAL_SOFTWARE_IMAGE_PATH, 'rb'))},
        multipart_monitor_callback=None,
        payload=None,
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([LOCAL_SOFTWARE_IMAGE_PATH, LOCAL_SOFTWARE_IMAGE_PATH]) is True,
                    reason="tests.config values required not present")
@pytest.mark.swim
def test_import_local_software_image(api):
    assert is_valid_import_local_software_image(
        import_local_software_image(api)
    )


def is_valid_import_software_image_via_url(obj):
    json_schema_validate('jsd_bc8aab4746ca883d_v1_2_10').validate(obj)
    return True


def import_software_image_via_url(api):
    image_details = get_software_image_details(api).response[0]
    files = get_list_of_files(api).response[0].downloadPath
    endpoint_result = api.swim.import_software_image_via_url(
        schedule_at=None,
        schedule_desc=None,
        schedule_origin=None,
        payload=[{
            'applicationType': image_details.applicationType,
            'vendor': image_details.vendor,
            'imageFamily': image_details.family,
            'sourceURL': DEFAULT_BASE_URL + '/dna/intent/api/v1/' + files
        }],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.skipif(not all([DEFAULT_BASE_URL]) is True,
                    reason="tests.config values required not present")
@pytest.mark.swim
def test_import_software_image_via_url(api):
    assert is_valid_import_software_image_via_url(
        import_software_image_via_url(api)
    )


def is_valid_trigger_software_image_activation(obj):
    json_schema_validate('jsd_fb9beb664f2aba4c_v1_2_10').validate(obj)
    return True


def trigger_software_image_activation(api):
    endpoint_result = api.swim.trigger_software_image_activation(
        schedule_validate=None,
        payload=[{
            'activateLowerImageVersion': True,
            'deviceUuid': get_device_list(api).response[0].id,
            'distributeIfNeeded': True,
            'imageUuidList': [get_software_image_details(api).response[0].imageUuid],
        }],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.swim
def test_trigger_software_image_activation(api):
    assert is_valid_trigger_software_image_activation(
        trigger_software_image_activation(api)
    )


def is_valid_trigger_software_image_distribution(obj):
    json_schema_validate('jsd_8cb6783b4faba1f4_v1_2_10').validate(obj)
    return True


def trigger_software_image_distribution(api):
    endpoint_result = api.swim.trigger_software_image_distribution(
        payload=[{
            'deviceUuid': get_device_list(api).response[0].id,
            'imageUuid': get_software_image_details(api).response[0].imageUuid
        }],
        active_validation=True
    )
    return endpoint_result


@pytest.mark.swim
def test_trigger_software_image_distribution(api):
    assert is_valid_trigger_software_image_distribution(
        trigger_software_image_distribution(api)
    )

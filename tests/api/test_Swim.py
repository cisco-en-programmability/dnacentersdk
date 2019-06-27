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


from .test_file import get_list_of_files
from .test_devices import get_device_list


# 0c8f-7a0b-49b9-aedd
def is_valid_get_software_image_details(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_software_image_details(api):
    endpoint_result = api.swim.get_software_image_details( param_application_type = None, param_created_time = None, param_family = None, param_image_integrity_status = None, param_image_name = None, param_image_series = None, param_image_size_greater_than = None, param_image_size_lesser_than = None, param_image_uuid = None, param_is_cco_latest = None, param_is_cco_recommended = None, param_is_tagged_golden = None, param_limit = None, param_name = None, param_offset = None, param_sort_by = None, param_sort_order = 'asc', param_version = None, payload = '' )
    return endpoint_result


def test_get_software_image_details(api):
    assert is_valid_get_software_image_details(get_software_image_details(api))


# 4dbe-3bc7-43a8-91bc
def is_valid_import_local_software_image(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def import_local_software_image(api):
    endpoint_result = api.swim.import_local_software_image( param_is_third_party = None, param_third_party_application_type = None, param_third_party_image_family = None, param_third_party_vendor = None, payload = '' )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_import_local_software_image(api):
    assert is_valid_import_local_software_image(import_local_software_image(api))


# bc8a-ab47-46ca-883d
def is_valid_import_software_image_via_url(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def import_software_image_via_url(api):
    endpoint_result = api.swim.import_software_image_via_url( param_schedule_at = None, param_schedule_desc = None, param_schedule_origin = None, payload = [{
        'applicationType': get_software_image_details(api).response[0].applicationType, 
        'vendor': get_software_image_details(api).response[0].vendor, 
        'imageFamily': get_software_image_details(api).response[0].family, 
        'sourceURL': 'https://sandboxdnac.cisco.com:443/dna/intent/api/v1/' + get_list_of_files(api).response[0].downloadPath
      }] )
    return endpoint_result


def test_import_software_image_via_url(api):
    assert is_valid_import_software_image_via_url(import_software_image_via_url(api))


# fb9b-eb66-4f2a-ba4c
def is_valid_trigger_software_image_activation(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def trigger_software_image_activation(api):
    endpoint_result = api.swim.trigger_software_image_activation( param_schedule_validate = None, payload = [{
        'activateLowerImageVersion': True, 
        'deviceUuid': get_device_list(api).response[0].id, 
        'distributeIfNeeded': True, 
        'imageUuidList': [ get_software_image_details(api).response[0].imageUuid ],
      }] )
    return endpoint_result


def test_trigger_software_image_activation(api):
    assert is_valid_trigger_software_image_activation(trigger_software_image_activation(api))


# 8cb6-783b-4fab-a1f4
def is_valid_trigger_software_image_distribution(obj):
    some_keys = [ 'response' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def trigger_software_image_distribution(api):
    endpoint_result = api.swim.trigger_software_image_distribution( payload = [{
        'deviceUuid': get_device_list(api).response[0].id,
        'imageUuid': get_software_image_details(api).response[0].imageUuid
      }] )
    return endpoint_result


def test_trigger_software_image_distribution(api):
    assert is_valid_trigger_software_image_distribution(trigger_software_image_distribution(api))


# -*- coding: utf-8 -*-
"""DNACenterAPI fabric_wired API fixtures and tests.

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




# a4b5-6a5f-478a-97dd
def is_valid_adds_border_device_in_sda_fabric(obj):
    some_keys = [ 'status', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def adds_border_device_in_sda_fabric(api):
    endpoint_result = api.fabric_wired.adds_border_device_in_sda_fabric( payload = '' )
    return endpoint_result


def test_adds_border_device_in_sda_fabric(api):
    assert is_valid_adds_border_device_in_sda_fabric(adds_border_device_in_sda_fabric(api))


# d0b3-593c-4a7a-af22
def is_valid_gets_border_device_details_from_sda_fabric(obj):
    some_keys = [ 'status', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def gets_border_device_details_from_sda_fabric(api):
    endpoint_result = api.fabric_wired.gets_border_device_details_from_sda_fabric( path_param_device_ip_address = '', payload = '' )
    return endpoint_result


def test_gets_border_device_details_from_sda_fabric(api):
    assert is_valid_gets_border_device_details_from_sda_fabric(gets_border_device_details_from_sda_fabric(api))


# 1e80-bb50-430b-8634
def is_valid_deletes_border_device_from_sda_fabric(obj):
    some_keys = [ 'status', 'description' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def deletes_border_device_from_sda_fabric(api):
    endpoint_result = api.fabric_wired.deletes_border_device_from_sda_fabric( path_param_device_ip_address = '', payload = '' )
    return endpoint_result


def test_deletes_border_device_from_sda_fabric(api):
    assert is_valid_deletes_border_device_from_sda_fabric(deletes_border_device_from_sda_fabric(api))


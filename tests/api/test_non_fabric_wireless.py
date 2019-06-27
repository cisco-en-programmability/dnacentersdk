# -*- coding: utf-8 -*-
"""DNACenterAPI non_fabric_wireless API fixtures and tests.

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




# 8a96-fb95-4d09-a349
def is_valid_create_enterprise_ssid(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def create_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.create_enterprise_ssid( rq_enableBroadcastSSID = None, rq_enableFastLane = None, rq_enableMACFiltering = None, rq_fastTransition = None, rq_name = None, rq_passphrase = None, rq_radioPolicy = None, rq_securityLevel = None, rq_trafficType = None, payload = {'name': 'string', 'securityLevel': 'WPA2_ENTERPRISE', 'passphrase': 'string', 'enableFastLane': True, 'enableMACFiltering': True, 'trafficType': 'voicedata', 'radioPolicy': 'Dual band operation (2.4GHz and 5GHz)', 'enableBroadcastSSID': True, 'fastTransition': 'Adaptive'} )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_create_enterprise_ssid(api):
    assert is_valid_create_enterprise_ssid(create_enterprise_ssid(api))


# cca5-19ba-45eb-b423
def is_valid_get_enterprise_ssid(obj):
    return len(obj) > 0 and all([ item for item in obj ])


def get_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.get_enterprise_ssid( param_ssid_name = None, payload = '' )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_enterprise_ssid(api):
    assert is_valid_get_enterprise_ssid(get_enterprise_ssid(api))


# c7a6-592b-4b98-a369
def is_valid_delete_enterprise_ssid(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def delete_enterprise_ssid(api):
    endpoint_result = api.non_fabric_wireless.delete_enterprise_ssid( path_param_ssid_name = '', payload = '' )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_enterprise_ssid(api):
    assert is_valid_delete_enterprise_ssid(delete_enterprise_ssid(api))


# db9f-997f-4e59-aec1
def is_valid_create_and_provision_ssid(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def create_and_provision_ssid(api):
    endpoint_result = api.non_fabric_wireless.create_and_provision_ssid( rq_enableFabric = None, rq_flexConnect = None, rq_managedAPLocations = None, rq_ssidDetails = None, rq_ssidType = None, rq_vlanAndDynamicInterfaceDetails = None, payload = {'managedAPLocations': ['string'], 'ssidDetails': {'name': 'string', 'securityLevel': 'WPA2_ENTERPRISE', 'enableFastLane': True, 'passphrase': 'string', 'trafficType': 'data', 'enableBroadcastSSID': True, 'radioPolicy': 'Dual band operation (2.4GHz and 5GHz)', 'enableMACFiltering': True, 'fastTransition': 'Adaptive', 'webAuthURL': 'string'}, 'ssidType': 'Guest', 'enableFabric': True, 'flexConnect': {'enableFlexConnect': True, 'localToVlan': 0}, 'vlanAndDynamicInterfaceDetails': {'managedAPLocation': {'interfaceIPAddress': 'string', 'interfaceNetmaskInCIDR': 0, 'interfaceGateway': 'string', 'lagOrPortNumber': 0}, 'vlanId': 0, 'vlanName': 'string'}} )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_create_and_provision_ssid(api):
    assert is_valid_create_and_provision_ssid(create_and_provision_ssid(api))


# cca0-9834-4a48-9dfa
def is_valid_delete_and_provision_ssid(obj):
    some_keys = [ 'executionId', 'executionStatusUrl' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def delete_and_provision_ssid(api):
    endpoint_result = api.non_fabric_wireless.delete_and_provision_ssid( path_param_managed_aplocations = '', path_param_ssid_name = '', payload = '' )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_delete_and_provision_ssid(api):
    assert is_valid_delete_and_provision_ssid(delete_and_provision_ssid(api))


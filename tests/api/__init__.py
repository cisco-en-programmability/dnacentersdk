# -*- coding: utf-8 -*-
"""DNACenterAPI fixtures and tests.

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

import os

import pytest

import dnacentersdk
from tests.environment import (
    DNA_CENTER_USERNAME, DNA_CENTER_PASSWORD,
    DNA_CENTER_ENCODED_AUTH, DNA_CENTER_VERSION,
)

from dnacentersdk.api.authentication import Authentication
from dnacentersdk.api.v1_2_10.clients import \
    Clients as Clients_v1_2_10
from dnacentersdk.api.v1_2_10.command_runner import \
    CommandRunner as CommandRunner_v1_2_10
from dnacentersdk.api.v1_2_10.devices import \
    Devices as Devices_v1_2_10
from dnacentersdk.api.v1_2_10.fabric_wired import \
    FabricWired as FabricWired_v1_2_10
from dnacentersdk.api.v1_2_10.file import \
    File as File_v1_2_10
from dnacentersdk.api.v1_2_10.network_discovery import \
    NetworkDiscovery as NetworkDiscovery_v1_2_10
from dnacentersdk.api.v1_2_10.networks import \
    Networks as Networks_v1_2_10
from dnacentersdk.api.v1_2_10.non_fabric_wireless import \
    NonFabricWireless as NonFabricWireless_v1_2_10
from dnacentersdk.api.v1_2_10.path_trace import \
    PathTrace as PathTrace_v1_2_10
from dnacentersdk.api.v1_2_10.pnp import \
    Pnp as Pnp_v1_2_10
from dnacentersdk.api.v1_2_10.swim import \
    Swim as Swim_v1_2_10
from dnacentersdk.api.v1_2_10.site_profile import \
    SiteProfile as SiteProfile_v1_2_10
from dnacentersdk.api.v1_2_10.sites import \
    Sites as Sites_v1_2_10
from dnacentersdk.api.v1_2_10.tag import \
    Tag as Tag_v1_2_10
from dnacentersdk.api.v1_2_10.task import \
    Task as Task_v1_2_10
from dnacentersdk.api.v1_2_10.template_programmer import \
    TemplateProgrammer as TemplateProgrammer_v1_2_10
from dnacentersdk.api.v1_3_0.clients import \
    Clients as Clients_v1_3_0
from dnacentersdk.api.v1_3_0.command_runner import \
    CommandRunner as CommandRunner_v1_3_0
from dnacentersdk.api.v1_3_0.devices import \
    Devices as Devices_v1_3_0
from dnacentersdk.api.v1_3_0.fabric_wired import \
    FabricWired as FabricWired_v1_3_0
from dnacentersdk.api.v1_3_0.file import \
    File as File_v1_3_0
from dnacentersdk.api.v1_3_0.network_discovery import \
    NetworkDiscovery as NetworkDiscovery_v1_3_0
from dnacentersdk.api.v1_3_0.networks import \
    Networks as Networks_v1_3_0
from dnacentersdk.api.v1_3_0.non_fabric_wireless import \
    NonFabricWireless as NonFabricWireless_v1_3_0
from dnacentersdk.api.v1_3_0.path_trace import \
    PathTrace as PathTrace_v1_3_0
from dnacentersdk.api.v1_3_0.pnp import \
    Pnp as Pnp_v1_3_0
from dnacentersdk.api.v1_3_0.swim import \
    Swim as Swim_v1_3_0
from dnacentersdk.api.v1_3_0.site_profile import \
    SiteProfile as SiteProfile_v1_3_0
from dnacentersdk.api.v1_3_0.sites import \
    Sites as Sites_v1_3_0
from dnacentersdk.api.v1_3_0.tag import \
    Tag as Tag_v1_3_0
from dnacentersdk.api.v1_3_0.task import \
    Task as Task_v1_3_0
from dnacentersdk.api.v1_3_0.template_programmer import \
    TemplateProgrammer as TemplateProgrammer_v1_3_0
from dnacentersdk.api.custom_caller import CustomCaller

from tests.config import (
    DEFAULT_BASE_URL, DEFAULT_VERIFY,
    DEFAULT_SINGLE_REQUEST_TIMEOUT, DEFAULT_WAIT_ON_RATE_LIMIT
)


# Fixtures

@pytest.fixture(scope="session")
def api():
    return dnacentersdk.DNACenterAPI(username=DNA_CENTER_USERNAME,
                                     password=DNA_CENTER_PASSWORD,
                                     encoded_auth=DNA_CENTER_ENCODED_AUTH,
                                     base_url=DEFAULT_BASE_URL,
                                     single_request_timeout=DEFAULT_SINGLE_REQUEST_TIMEOUT,
                                     wait_on_rate_limit=DEFAULT_WAIT_ON_RATE_LIMIT,
                                     verify=DEFAULT_VERIFY,
                                     version=DNA_CENTER_VERSION)


def test_default_base_url(api):
    assert api.base_url == DEFAULT_BASE_URL


def test_custom_base_url():
    custom_url = "https://custom.domain.com/v1/"
    connection_object = dnacentersdk.DNACenterAPI(
        username=DNA_CENTER_USERNAME,
        password=DNA_CENTER_PASSWORD,
        encoded_auth=DNA_CENTER_ENCODED_AUTH,
        base_url=custom_url,
        verify=DEFAULT_VERIFY,
        version=DNA_CENTER_VERSION)
    assert connection_object.base_url == custom_url


def test_default_single_request_timeout(api):
    assert api.single_request_timeout == \
        DEFAULT_SINGLE_REQUEST_TIMEOUT


def test_custom_single_request_timeout():
    custom_timeout = 10
    connection_object = dnacentersdk.DNACenterAPI(
        username=DNA_CENTER_USERNAME,
        password=DNA_CENTER_PASSWORD,
        encoded_auth=DNA_CENTER_ENCODED_AUTH,
        base_url=DEFAULT_BASE_URL,
        single_request_timeout=custom_timeout,
        verify=DEFAULT_VERIFY,
        version=DNA_CENTER_VERSION,
    )
    assert connection_object.single_request_timeout == custom_timeout


def test_default_wait_on_rate_limit(api):
    assert api.wait_on_rate_limit == \
        DEFAULT_WAIT_ON_RATE_LIMIT


def test_non_default_wait_on_rate_limit():
    connection_object = dnacentersdk.DNACenterAPI(
        username=DNA_CENTER_USERNAME,
        password=DNA_CENTER_PASSWORD,
        encoded_auth=DNA_CENTER_ENCODED_AUTH,
        base_url=DEFAULT_BASE_URL,
        wait_on_rate_limit=not DEFAULT_WAIT_ON_RATE_LIMIT,
        verify=DEFAULT_VERIFY,
        version=DNA_CENTER_VERSION,
    )
    assert connection_object.wait_on_rate_limit != \
        DEFAULT_WAIT_ON_RATE_LIMIT


def test_api_object_creation(api):
    assert isinstance(api.authentication, Authentication)
    assert isinstance(api.custom_caller, CustomCaller)
    if api.version == '1.2.10':
        assert isinstance(api.clients, Clients_v1_2_10)
        assert isinstance(api.command_runner, CommandRunner_v1_2_10)
        assert isinstance(api.devices, Devices_v1_2_10)
        assert isinstance(api.fabric_wired, FabricWired_v1_2_10)
        assert isinstance(api.file, File_v1_2_10)
        assert isinstance(api.network_discovery, NetworkDiscovery_v1_2_10)
        assert isinstance(api.networks, Networks_v1_2_10)
        assert isinstance(api.non_fabric_wireless, NonFabricWireless_v1_2_10)
        assert isinstance(api.path_trace, PathTrace_v1_2_10)
        assert isinstance(api.pnp, Pnp_v1_2_10)
        assert isinstance(api.swim, Swim_v1_2_10)
        assert isinstance(api.site_profile, SiteProfile_v1_2_10)
        assert isinstance(api.sites, Sites_v1_2_10)
        assert isinstance(api.tag, Tag_v1_2_10)
        assert isinstance(api.task, Task_v1_2_10)
        assert isinstance(api.template_programmer, TemplateProgrammer_v1_2_10)
    if api.version == '1.3.0':
        assert isinstance(api.clients, Clients_v1_3_0)
        assert isinstance(api.command_runner, CommandRunner_v1_3_0)
        assert isinstance(api.devices, Devices_v1_3_0)
        assert isinstance(api.fabric_wired, FabricWired_v1_3_0)
        assert isinstance(api.file, File_v1_3_0)
        assert isinstance(api.network_discovery, NetworkDiscovery_v1_3_0)
        assert isinstance(api.networks, Networks_v1_3_0)
        assert isinstance(api.non_fabric_wireless, NonFabricWireless_v1_3_0)
        assert isinstance(api.path_trace, PathTrace_v1_3_0)
        assert isinstance(api.pnp, Pnp_v1_3_0)
        assert isinstance(api.swim, Swim_v1_3_0)
        assert isinstance(api.site_profile, SiteProfile_v1_3_0)
        assert isinstance(api.sites, Sites_v1_3_0)
        assert isinstance(api.tag, Tag_v1_3_0)
        assert isinstance(api.task, Task_v1_3_0)
        assert isinstance(api.template_programmer, TemplateProgrammer_v1_3_0)

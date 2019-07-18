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
    DNA_CENTER_ENCODED_AUTH
)

from dnacentersdk.api.template_programmer import TemplateProgrammer
from dnacentersdk.api.tag import Tag
from dnacentersdk.api.network_discovery import NetworkDiscovery
from dnacentersdk.api.task import Task
from dnacentersdk.api.command_runner import CommandRunner
from dnacentersdk.api.file import File
from dnacentersdk.api.path_trace import PathTrace
from dnacentersdk.api.swim import Swim
from dnacentersdk.api.pnp import Pnp
from dnacentersdk.api.site_profile import SiteProfile
from dnacentersdk.api.devices import Devices
from dnacentersdk.api.sites import Sites
from dnacentersdk.api.networks import Networks
from dnacentersdk.api.clients import Clients
from dnacentersdk.api.non_fabric_wireless import NonFabricWireless
from dnacentersdk.api.fabric_wired import FabricWired
from dnacentersdk.api.authentication import Authentication

from tests.config import (
    DEFAULT_BASE_URL, DEFAULT_VERIFY,
    DEFAULT_SINGLE_REQUEST_TIMEOUT, DEFAULT_WAIT_ON_RATE_LIMIT
)


# Fixtures

@pytest.fixture(scope="session")  # If failure because auth, try: @pytest.fixture(scope="module") which is slower
def api():
    return dnacentersdk.DNACenterAPI(username=DNA_CENTER_USERNAME,
                                     password=DNA_CENTER_PASSWORD,
                                     encoded_auth=DNA_CENTER_ENCODED_AUTH,
                                     base_url=DEFAULT_BASE_URL,
                                     single_request_timeout=DEFAULT_SINGLE_REQUEST_TIMEOUT,
                                     wait_on_rate_limit=DEFAULT_WAIT_ON_RATE_LIMIT,
                                     verify=DEFAULT_VERIFY)


def test_default_base_url(api):
    assert api.base_url == DEFAULT_BASE_URL


def test_custom_base_url():
    custom_url = "https://custom.domain.com/v1/"
    connection_object = dnacentersdk.DNACenterAPI(
        username=DNA_CENTER_USERNAME,
        password=DNA_CENTER_PASSWORD,
        encoded_auth=DNA_CENTER_ENCODED_AUTH,
        base_url=custom_url,
        verify=DEFAULT_VERIFY)
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
        verify=DEFAULT_VERIFY
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
        verify=DEFAULT_VERIFY
    )
    assert connection_object.wait_on_rate_limit != \
        DEFAULT_WAIT_ON_RATE_LIMIT


def test_template_programmer_api_object_creation(api):
    assert isinstance(api.template_programmer, TemplateProgrammer)


def test_tag_api_object_creation(api):
    assert isinstance(api.tag, Tag)


def test_network_discovery_api_object_creation(api):
    assert isinstance(api.network_discovery, NetworkDiscovery)


def test_task_api_object_creation(api):
    assert isinstance(api.task, Task)


def test_command_runner_api_object_creation(api):
    assert isinstance(api.command_runner, CommandRunner)


def test_file_api_object_creation(api):
    assert isinstance(api.file, File)


def test_path_trace_api_object_creation(api):
    assert isinstance(api.path_trace, PathTrace)


def test_swim_api_object_creation(api):
    assert isinstance(api.swim, Swim)


def test_pnp_api_object_creation(api):
    assert isinstance(api.pnp, Pnp)


def test_site_profile_api_object_creation(api):
    assert isinstance(api.site_profile, SiteProfile)


def test_devices_api_object_creation(api):
    assert isinstance(api.devices, Devices)


def test_sites_api_object_creation(api):
    assert isinstance(api.sites, Sites)


def test_networks_api_object_creation(api):
    assert isinstance(api.networks, Networks)


def test_clients_api_object_creation(api):
    assert isinstance(api.clients, Clients)


def test_non_fabric_wireless_api_object_creation(api):
    assert isinstance(api.non_fabric_wireless, NonFabricWireless)


def test_fabric_wired_api_object_creation(api):
    assert isinstance(api.fabric_wired, FabricWired)


def test_authentication_api_object_creation(api):
    assert isinstance(api.authentication, Authentication)

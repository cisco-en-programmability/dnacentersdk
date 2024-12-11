# -*- coding: utf-8 -*-
"""pytest configuration and top-level fixtures.

Copyright (c) 2019-2021 Cisco Systems.

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

pytest_plugins = [
    'tests.test_importsdk',
    'tests.test_dnacentersdk',
    'tests.api',
    'tests.api.v2_2_2_3',
    'tests.api.v2_2_3_3',
    'tests.api.v2_3_3_0',
    'tests.api.v2_3_5_3',
    'tests.api.v2_3_7_6',
    'tests.api.v2_3_7_9',
]


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "ratelimit: run a ratelimit test",
    )
    config.addinivalue_line(
        "markers", "dnacentersdk: package mark"
    )
    config.addinivalue_line(
        "markers", "api: dnacentersdk mark"
    )
    config.addinivalue_line(
        "markers", "application_policy: application_policy wrapper test"
    )
    config.addinivalue_line(
        "markers", "applications: applications wrapper test"
    )
    config.addinivalue_line(
        "markers", "authentication: authentication wrapper test"
    )
    config.addinivalue_line(
        "markers", "authentication_management: authentication_management wrapper test"
    )
    config.addinivalue_line(
        "markers", "cisco_dna_center_system: cisco_dna_center_system wrapper test"
    )
    config.addinivalue_line(
        "markers", "clients: clients wrapper test"
    )
    config.addinivalue_line(
        "markers", "command_runner: command_runner wrapper test"
    )
    config.addinivalue_line(
        "markers", "compliance: compliance wrapper test"
    )
    config.addinivalue_line(
        "markers", "configuration_archive: configuration_archive wrapper test"
    )
    config.addinivalue_line(
        "markers", "configuration_templates: configuration_templates wrapper test"
    )
    config.addinivalue_line(
        "markers", "custom_caller: custom_caller wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_onboarding_pnp: device_onboarding_pnp wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_replacement: device_replacement wrapper test"
    )
    config.addinivalue_line(
        "markers", "devices: devices wrapper test"
    )
    config.addinivalue_line(
        "markers", "disaster_recovery: disaster_recovery wrapper test"
    )
    config.addinivalue_line(
        "markers", "discovery: discovery wrapper test"
    )
    config.addinivalue_line(
        "markers", "eox: eox wrapper test"
    )
    config.addinivalue_line(
        "markers", "event_management: event_management wrapper test"
    )
    config.addinivalue_line(
        "markers", "fabric_wireless: fabric_wireless wrapper test"
    )
    config.addinivalue_line(
        "markers", "file: file wrapper test"
    )
    config.addinivalue_line(
        "markers", "health_and_performance: health_and_performance wrapper test"
    )
    config.addinivalue_line(
        "markers", "itsm: itsm wrapper test"
    )
    config.addinivalue_line(
        "markers", "itsm_integration: itsm_integration wrapper test"
    )
    config.addinivalue_line(
        "markers", "issues: issues wrapper test"
    )
    config.addinivalue_line(
        "markers", "lan_automation: lan_automation wrapper test"
    )
    config.addinivalue_line(
        "markers", "licenses: licenses wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_settings: network_settings wrapper test"
    )
    config.addinivalue_line(
        "markers", "path_trace: path_trace wrapper test"
    )
    config.addinivalue_line(
        "markers", "platform: platform wrapper test"
    )
    config.addinivalue_line(
        "markers", "platform_configuration: platform_configuration wrapper test"
    )
    config.addinivalue_line(
        "markers", "policy: policy wrapper test"
    )
    config.addinivalue_line(
        "markers", "reports: reports wrapper test"
    )
    config.addinivalue_line(
        "markers", "sda: sda wrapper test"
    )
    config.addinivalue_line(
        "markers", "security_advisories: security_advisories wrapper test"
    )
    config.addinivalue_line(
        "markers", "sensors: sensors wrapper test"
    )
    config.addinivalue_line(
        "markers", "site_design: site_design wrapper test"
    )
    config.addinivalue_line(
        "markers", "sites: sites wrapper test"
    )
    config.addinivalue_line(
        "markers", "software_image_management_swim: software_image_management_swim wrapper test"
    )
    config.addinivalue_line(
        "markers", "system_settings: system_settings wrapper test"
    )
    config.addinivalue_line(
        "markers", "tag: tag wrapper test"
    )
    config.addinivalue_line(
        "markers", "task: task wrapper test"
    )
    config.addinivalue_line(
        "markers", "topology: topology wrapper test"
    )
    config.addinivalue_line(
        "markers", "user_and_roles: user_and_roles wrapper test"
    )
    config.addinivalue_line(
        "markers", "users: users wrapper test"
    )
    config.addinivalue_line(
        "markers", "wireless: wireless wrapper test"
    )

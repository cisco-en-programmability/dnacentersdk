
# -*- coding: utf-8 -*-
"""Test suite for the community-developed Python SDK for the DNA Center APIs.

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

import dnacentersdk
import requests
from tests.environment import (
    DNA_CENTER_USERNAME, DNA_CENTER_PASSWORD,
    DNA_CENTER_ENCODED_AUTH, DNA_CENTER_VERSION,
)

from dnacentersdk.api.authentication import Authentication


from dnacentersdk.api.v2_3_5_3.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.applications import \
    Applications as Applications_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.authentication_management import \
    AuthenticationManagement as AuthenticationManagement_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.cisco_dna_center_system import \
    CiscoDnaCenterSystem as CiscoDnaCenterSystem_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.clients import \
    Clients as Clients_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.command_runner import \
    CommandRunner as CommandRunner_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.compliance import \
    Compliance as Compliance_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.devices import \
    Devices as Devices_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.discovery import \
    Discovery as Discovery_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.eox import \
    Eox as Eox_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.event_management import \
    EventManagement as EventManagement_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.fabric_wireless import \
    FabricWireless as FabricWireless_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.file import \
    File as File_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.health_and_performance import \
    HealthAndPerformance as HealthAndPerformance_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.itsm import \
    Itsm as Itsm_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.itsm_integration import \
    ItsmIntegration as ItsmIntegration_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.issues import \
    Issues as Issues_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.lan_automation import \
    LanAutomation as LanAutomation_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.licenses import \
    Licenses as Licenses_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.network_settings import \
    NetworkSettings as NetworkSettings_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.path_trace import \
    PathTrace as PathTrace_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.platform import \
    Platform as Platform_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.reports import \
    Reports as Reports_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.sda import \
    Sda as Sda_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.sensors import \
    Sensors as Sensors_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.site_design import \
    SiteDesign as SiteDesign_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.sites import \
    Sites as Sites_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.system_settings import \
    SystemSettings as SystemSettings_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.tag import \
    Tag as Tag_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.task import \
    Task as Task_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.topology import \
    Topology as Topology_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.user_and_roles import \
    UserandRoles as UserandRoles_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.users import \
    Users as Users_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.wireless import \
    Wireless as Wireless_v2_3_5_3
from dnacentersdk.api.v2_3_7_6.ai_endpoint_analytics import \
    AIEndpointAnalytics as AIEndpointAnalytics_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.applications import \
    Applications as Applications_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.authentication_management import \
    AuthenticationManagement as AuthenticationManagement_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.cisco_trusted_certificates import \
    CiscoTrustedCertificates as CiscoTrustedCertificates_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.clients import \
    Clients as Clients_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.command_runner import \
    CommandRunner as CommandRunner_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.compliance import \
    Compliance as Compliance_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.devices import \
    Devices as Devices_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.disaster_recovery import \
    DisasterRecovery as DisasterRecovery_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.discovery import \
    Discovery as Discovery_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.eox import \
    EoX as EoX_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.event_management import \
    EventManagement as EventManagement_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.fabric_wireless import \
    FabricWireless as FabricWireless_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.file import \
    File as File_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.health_and_performance import \
    HealthAndPerformance as HealthAndPerformance_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.itsm import \
    Itsm as Itsm_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.itsm_integration import \
    ItsmIntegration as ItsmIntegration_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.issues import \
    Issues as Issues_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.lan_automation import \
    LanAutomation as LanAutomation_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.licenses import \
    Licenses as Licenses_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.network_settings import \
    NetworkSettings as NetworkSettings_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.path_trace import \
    PathTrace as PathTrace_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.platform import \
    Platform as Platform_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.reports import \
    Reports as Reports_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.sda import \
    Sda as Sda_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.sensors import \
    Sensors as Sensors_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.site_design import \
    SiteDesign as SiteDesign_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.sites import \
    Sites as Sites_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.system_settings import \
    SystemSettings as SystemSettings_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.tag import \
    Tag as Tag_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.task import \
    Task as Task_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.topology import \
    Topology as Topology_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.user_and_roles import \
    UserandRoles as UserandRoles_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.users import \
    Users as Users_v2_3_7_6
from dnacentersdk.api.v2_3_7_6.wireless import \
    Wireless as Wireless_v2_3_7_6

from dnacentersdk.api.v2_3_7_9.ai_endpoint_analytics import \
    AIEndpointAnalytics as AIEndpointAnalytics_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.applications import \
    Applications as Applications_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.authentication_management import \
    AuthenticationManagement as AuthenticationManagement_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.cisco_i_m_c import \
    CiscoIMC as CiscoIMC_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.cisco_trusted_certificates import \
    CiscoTrustedCertificates as CiscoTrustedCertificates_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.clients import \
    Clients as Clients_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.command_runner import \
    CommandRunner as CommandRunner_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.compliance import \
    Compliance as Compliance_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.devices import \
    Devices as Devices_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.disaster_recovery import \
    DisasterRecovery as DisasterRecovery_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.discovery import \
    Discovery as Discovery_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.eox import \
    EoX as EoX_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.event_management import \
    EventManagement as EventManagement_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.fabric_wireless import \
    FabricWireless as FabricWireless_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.file import \
    File as File_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.health_and_performance import \
    HealthAndPerformance as HealthAndPerformance_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.itsm import \
    Itsm as Itsm_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.itsm_integration import \
    ItsmIntegration as ItsmIntegration_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.issues import \
    Issues as Issues_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.lan_automation import \
    LanAutomation as LanAutomation_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.licenses import \
    Licenses as Licenses_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.network_settings import \
    NetworkSettings as NetworkSettings_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.path_trace import \
    PathTrace as PathTrace_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.platform import \
    Platform as Platform_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.reports import \
    Reports as Reports_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.sda import \
    Sda as Sda_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.sensors import \
    Sensors as Sensors_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.site_design import \
    SiteDesign as SiteDesign_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.sites import \
    Sites as Sites_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.system_settings import \
    SystemSettings as SystemSettings_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.tag import \
    Tag as Tag_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.task import \
    Task as Task_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.topology import \
    Topology as Topology_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.user_and_roles import \
    UserandRoles as UserandRoles_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.users import \
    Users as Users_v2_3_7_9
from dnacentersdk.api.v2_3_7_9.wireless import \
    Wireless as Wireless_v2_3_7_9

from dnacentersdk.api.v3_1_3_0.ai_endpoint_analytics import \
    AIEndpointAnalytics as AIEndpointAnalytics_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.applications import \
    Applications as Applications_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.authentication_management import \
    AuthenticationManagement as AuthenticationManagement_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.backup import \
    Backup as Backup_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.cisco_i_m_c import \
    CiscoIMC as CiscoIMC_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.cisco_trusted_certificates import \
    CiscoTrustedCertificates as CiscoTrustedCertificates_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.clients import \
    Clients as Clients_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.command_runner import \
    CommandRunner as CommandRunner_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.compliance import \
    Compliance as Compliance_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.device_replacement import \
    DeviceReplacement as DeviceReplacement_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.devices import \
    Devices as Devices_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.disaster_recovery import \
    DisasterRecovery as DisasterRecovery_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.discovery import \
    Discovery as Discovery_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.eox import \
    EoX as Eox_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.event_management import \
    EventManagement as EventManagement_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.fabric_wireless import \
    FabricWireless as FabricWireless_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.file import \
    File as File_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.health_and_performance import \
    HealthAndPerformance as HealthAndPerformance_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.itsm import \
    Itsm as Itsm_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.itsm_integration import \
    ItsmIntegration as ItsmIntegration_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.industrial_configuration import \
    IndustrialConfiguration as IndustrialConfiguration_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.issues import \
    Issues as Issues_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.know_your_network import \
    KnowYourNetwork as KnowYourNetwork_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.lan_automation import \
    LanAutomation as LanAutomation_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.licenses import \
    Licenses as Licenses_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.network_settings import \
    NetworkSettings as NetworkSettings_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.path_trace import \
    PathTrace as PathTrace_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.platform import \
    Platform as Platform_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.reports import \
    Reports as Reports_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.restore import \
    Restore as Restore_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.sda import \
    Sda as Sda_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.sensors import \
    Sensors as Sensors_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.site_design import \
    SiteDesign as SiteDesign_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.sites import \
    Sites as Sites_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.system_settings import \
    SystemSettings as SystemSettings_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.tag import \
    Tag as Tag_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.task import \
    Task as Task_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.topology import \
    Topology as Topology_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.user_and_roles import \
    UserandRoles as UserandRoles_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.users import \
    Users as Users_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.wired import \
    Wired as Wired_v3_1_3_0
from dnacentersdk.api.v3_1_3_0.wireless import \
    Wireless as Wireless_v3_1_3_0
from dnacentersdk.api.custom_caller import CustomCaller

from tests.config import (
    DEFAULT_VERIFY,
    DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_WAIT_ON_RATE_LIMIT
)
import pytest


@pytest.mark.dnacentersdk
class TestDNACenterSDK:
    """Test the package-level code."""

    def test_package_contents(self):
        """Ensure the package contains the correct top-level objects."""
        # DNA Center API Wrapper
        assert hasattr(dnacentersdk, "DNACenterAPI")

        # Exceptions
        assert hasattr(dnacentersdk, "AccessTokenError")
        assert hasattr(dnacentersdk, "ApiError")
        assert hasattr(dnacentersdk, "dnacentersdkException")
        assert hasattr(dnacentersdk, "DownloadFailure")
        assert hasattr(dnacentersdk, "MalformedRequest")
        assert hasattr(dnacentersdk, "RateLimitError")
        assert hasattr(dnacentersdk, "RateLimitWarning")
        assert hasattr(dnacentersdk, "VersionError")

        # Data Models
        assert hasattr(dnacentersdk, "mydict_data_factory")

    @pytest.mark.dnacentersdk
    def test_default_base_url(self, api, base_url):
        assert api.base_url == base_url

    @pytest.mark.dnacentersdk
    def test_custom_base_url(self):
        custom_url = "https://custom.domain.com/v1/"
        with pytest.raises((dnacentersdk.exceptions.ApiError, requests.exceptions.RequestException)):
            dnacentersdk.DNACenterAPI(username=DNA_CENTER_USERNAME,
                                      password=DNA_CENTER_PASSWORD,
                                      encoded_auth=DNA_CENTER_ENCODED_AUTH,
                                      base_url=custom_url,
                                      verify=DEFAULT_VERIFY,
                                      version=DNA_CENTER_VERSION)

    @pytest.mark.dnacentersdk
    def test_default_single_request_timeout(self, api):
        assert api.single_request_timeout == \
            DEFAULT_SINGLE_REQUEST_TIMEOUT

    @pytest.mark.dnacentersdk
    def test_custom_single_request_timeout(self, base_url):
        custom_timeout = 10
        connection_object = dnacentersdk.DNACenterAPI(username=DNA_CENTER_USERNAME,
                                                      password=DNA_CENTER_PASSWORD,
                                                      encoded_auth=DNA_CENTER_ENCODED_AUTH,
                                                      base_url=base_url,
                                                      single_request_timeout=custom_timeout,
                                                      verify=DEFAULT_VERIFY,
                                                      version=DNA_CENTER_VERSION)
        assert connection_object.single_request_timeout == custom_timeout

    @pytest.mark.dnacentersdk
    def test_default_wait_on_rate_limit(self, api):
        assert api.wait_on_rate_limit == \
            DEFAULT_WAIT_ON_RATE_LIMIT

    @pytest.mark.dnacentersdk
    def test_non_default_wait_on_rate_limit(self, base_url):
        connection_object = dnacentersdk.DNACenterAPI(username=DNA_CENTER_USERNAME,
                                                      password=DNA_CENTER_PASSWORD,
                                                      encoded_auth=DNA_CENTER_ENCODED_AUTH,
                                                      base_url=base_url,
                                                      wait_on_rate_limit=not DEFAULT_WAIT_ON_RATE_LIMIT,
                                                      verify=DEFAULT_VERIFY,
                                                      version=DNA_CENTER_VERSION)
        assert connection_object.wait_on_rate_limit != \
            DEFAULT_WAIT_ON_RATE_LIMIT

    @pytest.mark.dnacentersdk
    def test_api_object_creation(self, api):
        assert isinstance(api.authentication, Authentication)
        assert isinstance(api.custom_caller, CustomCaller)


        if api.version == '2.3.5.3':
            assert isinstance(api.application_policy, ApplicationPolicy_v2_3_5_3)
            assert isinstance(api.applications, Applications_v2_3_5_3)
            assert isinstance(api.authentication_management, AuthenticationManagement_v2_3_5_3)
            assert isinstance(api.cisco_dna_center_system, CiscoDnaCenterSystem_v2_3_5_3)
            assert isinstance(api.clients, Clients_v2_3_5_3)
            assert isinstance(api.command_runner, CommandRunner_v2_3_5_3)
            assert isinstance(api.compliance, Compliance_v2_3_5_3)
            assert isinstance(api.configuration_archive, ConfigurationArchive_v2_3_5_3)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v2_3_5_3)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v2_3_5_3)
            assert isinstance(api.device_replacement, DeviceReplacement_v2_3_5_3)
            assert isinstance(api.devices, Devices_v2_3_5_3)
            assert isinstance(api.discovery, Discovery_v2_3_5_3)
            assert isinstance(api.eox, Eox_v2_3_5_3)
            assert isinstance(api.event_management, EventManagement_v2_3_5_3)
            assert isinstance(api.fabric_wireless, FabricWireless_v2_3_5_3)
            assert isinstance(api.file, File_v2_3_5_3)
            assert isinstance(api.health_and_performance, HealthAndPerformance_v2_3_5_3)
            assert isinstance(api.itsm, Itsm_v2_3_5_3)
            assert isinstance(api.itsm_integration, ItsmIntegration_v2_3_5_3)
            assert isinstance(api.issues, Issues_v2_3_5_3)
            assert isinstance(api.lan_automation, LanAutomation_v2_3_5_3)
            assert isinstance(api.licenses, Licenses_v2_3_5_3)
            assert isinstance(api.network_settings, NetworkSettings_v2_3_5_3)
            assert isinstance(api.path_trace, PathTrace_v2_3_5_3)
            assert isinstance(api.platform, Platform_v2_3_5_3)
            assert isinstance(api.reports, Reports_v2_3_5_3)
            assert isinstance(api.sda, Sda_v2_3_5_3)
            assert isinstance(api.security_advisories, SecurityAdvisories_v2_3_5_3)
            assert isinstance(api.sensors, Sensors_v2_3_5_3)
            assert isinstance(api.site_design, SiteDesign_v2_3_5_3)
            assert isinstance(api.sites, Sites_v2_3_5_3)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v2_3_5_3)
            assert isinstance(api.system_settings, SystemSettings_v2_3_5_3)
            assert isinstance(api.tag, Tag_v2_3_5_3)
            assert isinstance(api.task, Task_v2_3_5_3)
            assert isinstance(api.topology, Topology_v2_3_5_3)
            assert isinstance(api.user_and_roles, UserandRoles_v2_3_5_3)
            assert isinstance(api.users, Users_v2_3_5_3)
            assert isinstance(api.wireless, Wireless_v2_3_5_3)
        if api.version == '2.3.7.6':
            assert isinstance(api.ai_endpoint_analytics, AIEndpointAnalytics_v2_3_7_6)
            assert isinstance(api.application_policy, ApplicationPolicy_v2_3_7_6)
            assert isinstance(api.applications, Applications_v2_3_7_6)
            assert isinstance(api.authentication_management, AuthenticationManagement_v2_3_7_6)
            assert isinstance(api.cisco_trusted_certificates, CiscoTrustedCertificates_v2_3_7_6)
            assert isinstance(api.clients, Clients_v2_3_7_6)
            assert isinstance(api.command_runner, CommandRunner_v2_3_7_6)
            assert isinstance(api.compliance, Compliance_v2_3_7_6)
            assert isinstance(api.configuration_archive, ConfigurationArchive_v2_3_7_6)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v2_3_7_6)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v2_3_7_6)
            assert isinstance(api.device_replacement, DeviceReplacement_v2_3_7_6)
            assert isinstance(api.devices, Devices_v2_3_7_6)
            assert isinstance(api.disaster_recovery, DisasterRecovery_v2_3_7_6)
            assert isinstance(api.discovery, Discovery_v2_3_7_6)
            assert isinstance(api.eox, EoX_v2_3_7_6)
            assert isinstance(api.event_management, EventManagement_v2_3_7_6)
            assert isinstance(api.fabric_wireless, FabricWireless_v2_3_7_6)
            assert isinstance(api.file, File_v2_3_7_6)
            assert isinstance(api.health_and_performance, HealthAndPerformance_v2_3_7_6)
            assert isinstance(api.itsm, Itsm_v2_3_7_6)
            assert isinstance(api.itsm_integration, ItsmIntegration_v2_3_7_6)
            assert isinstance(api.issues, Issues_v2_3_7_6)
            assert isinstance(api.lan_automation, LanAutomation_v2_3_7_6)
            assert isinstance(api.licenses, Licenses_v2_3_7_6)
            assert isinstance(api.network_settings, NetworkSettings_v2_3_7_6)
            assert isinstance(api.path_trace, PathTrace_v2_3_7_6)
            assert isinstance(api.platform, Platform_v2_3_7_6)
            assert isinstance(api.reports, Reports_v2_3_7_6)
            assert isinstance(api.sda, Sda_v2_3_7_6)
            assert isinstance(api.security_advisories, SecurityAdvisories_v2_3_7_6)
            assert isinstance(api.sensors, Sensors_v2_3_7_6)
            assert isinstance(api.site_design, SiteDesign_v2_3_7_6)
            assert isinstance(api.sites, Sites_v2_3_7_6)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v2_3_7_6)
            assert isinstance(api.system_settings, SystemSettings_v2_3_7_6)
            assert isinstance(api.tag, Tag_v2_3_7_6)
            assert isinstance(api.task, Task_v2_3_7_6)
            assert isinstance(api.topology, Topology_v2_3_7_6)
            assert isinstance(api.user_and_roles, UserandRoles_v2_3_7_6)
            assert isinstance(api.users, Users_v2_3_7_6)
            assert isinstance(api.wireless, Wireless_v2_3_7_6)
        if api.version == '2.3.7.9':
            assert isinstance(api.ai_endpoint_analytics, AIEndpointAnalytics_v2_3_7_9)
            assert isinstance(api.application_policy, ApplicationPolicy_v2_3_7_9)
            assert isinstance(api.applications, Applications_v2_3_7_9)
            assert isinstance(api.authentication_management, AuthenticationManagement_v2_3_7_9)
            assert isinstance(api.cisco_i_m_c, CiscoIMC_v2_3_7_9)
            assert isinstance(api.cisco_trusted_certificates, CiscoTrustedCertificates_v2_3_7_9)
            assert isinstance(api.clients, Clients_v2_3_7_9)
            assert isinstance(api.command_runner, CommandRunner_v2_3_7_9)
            assert isinstance(api.compliance, Compliance_v2_3_7_9)
            assert isinstance(api.configuration_archive, ConfigurationArchive_v2_3_7_9)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v2_3_7_9)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v2_3_7_9)
            assert isinstance(api.device_replacement, DeviceReplacement_v2_3_7_9)
            assert isinstance(api.devices, Devices_v2_3_7_9)
            assert isinstance(api.disaster_recovery, DisasterRecovery_v2_3_7_9)
            assert isinstance(api.discovery, Discovery_v2_3_7_9)
            assert isinstance(api.eox, EoX_v2_3_7_9)
            assert isinstance(api.event_management, EventManagement_v2_3_7_9)
            assert isinstance(api.fabric_wireless, FabricWireless_v2_3_7_9)
            assert isinstance(api.file, File_v2_3_7_9)
            assert isinstance(api.health_and_performance, HealthAndPerformance_v2_3_7_9)
            assert isinstance(api.itsm, Itsm_v2_3_7_9)
            assert isinstance(api.itsm_integration, ItsmIntegration_v2_3_7_9)
            assert isinstance(api.issues, Issues_v2_3_7_9)
            assert isinstance(api.lan_automation, LanAutomation_v2_3_7_9)
            assert isinstance(api.licenses, Licenses_v2_3_7_9)
            assert isinstance(api.network_settings, NetworkSettings_v2_3_7_9)
            assert isinstance(api.path_trace, PathTrace_v2_3_7_9)
            assert isinstance(api.platform, Platform_v2_3_7_9)
            assert isinstance(api.reports, Reports_v2_3_7_9)
            assert isinstance(api.sda, Sda_v2_3_7_9)
            assert isinstance(api.security_advisories, SecurityAdvisories_v2_3_7_9)
            assert isinstance(api.sensors, Sensors_v2_3_7_9)
            assert isinstance(api.site_design, SiteDesign_v2_3_7_9)
            assert isinstance(api.sites, Sites_v2_3_7_9)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v2_3_7_9)
            assert isinstance(api.system_settings, SystemSettings_v2_3_7_9)
            assert isinstance(api.tag, Tag_v2_3_7_9)
            assert isinstance(api.task, Task_v2_3_7_9)
            assert isinstance(api.topology, Topology_v2_3_7_9)
            assert isinstance(api.user_and_roles, UserandRoles_v2_3_7_9)
            assert isinstance(api.users, Users_v2_3_7_9)
            assert isinstance(api.wireless, Wireless_v2_3_7_9)
        if api.version == '3.1.3.0':
            assert isinstance(api.a_i_endpoint_analytics, AIEndpointAnalytics_v3_1_3_0)
            assert isinstance(api.application_policy, ApplicationPolicy_v3_1_3_0)
            assert isinstance(api.applications, Applications_v3_1_3_0)
            assert isinstance(api.authentication_management, AuthenticationManagement_v3_1_3_0)
            assert isinstance(api.backup, Backup_v3_1_3_0)
            assert isinstance(api.cisco_i_m_c, CiscoIMC_v3_1_3_0)
            assert isinstance(api.cisco_trusted_certificates, CiscoTrustedCertificates_v3_1_3_0)
            assert isinstance(api.clients, Clients_v3_1_3_0)
            assert isinstance(api.command_runner, CommandRunner_v3_1_3_0)
            assert isinstance(api.compliance, Compliance_v3_1_3_0)
            assert isinstance(api.configuration_archive, ConfigurationArchive_v3_1_3_0)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v3_1_3_0)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v3_1_3_0)
            assert isinstance(api.device_replacement, DeviceReplacement_v3_1_3_0)
            assert isinstance(api.devices, Devices_v3_1_3_0)
            assert isinstance(api.disaster_recovery, DisasterRecovery_v3_1_3_0)
            assert isinstance(api.discovery, Discovery_v3_1_3_0)
            assert isinstance(api.eox, Eox_v3_1_3_0)
            assert isinstance(api.event_management, EventManagement_v3_1_3_0)
            assert isinstance(api.fabric_wireless, FabricWireless_v3_1_3_0)
            assert isinstance(api.file, File_v3_1_3_0)
            assert isinstance(api.health_and_performance, HealthAndPerformance_v3_1_3_0)
            assert isinstance(api.itsm, Itsm_v3_1_3_0)
            assert isinstance(api.itsm_integration, ItsmIntegration_v3_1_3_0)
            assert isinstance(api.industrial_configuration, IndustrialConfiguration_v3_1_3_0)
            assert isinstance(api.issues, Issues_v3_1_3_0)
            assert isinstance(api.know_your_network, KnowYourNetwork_v3_1_3_0)
            assert isinstance(api.lan_automation, LanAutomation_v3_1_3_0)
            assert isinstance(api.licenses, Licenses_v3_1_3_0)
            assert isinstance(api.network_settings, NetworkSettings_v3_1_3_0)
            assert isinstance(api.path_trace, PathTrace_v3_1_3_0)
            assert isinstance(api.platform, Platform_v3_1_3_0)
            assert isinstance(api.reports, Reports_v3_1_3_0)
            assert isinstance(api.restore, Restore_v3_1_3_0)
            assert isinstance(api.sda, Sda_v3_1_3_0)
            assert isinstance(api.security_advisories, SecurityAdvisories_v3_1_3_0)
            assert isinstance(api.sensors, Sensors_v3_1_3_0)
            assert isinstance(api.site_design, SiteDesign_v3_1_3_0)
            assert isinstance(api.sites, Sites_v3_1_3_0)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v3_1_3_0)
            assert isinstance(api.system_settings, SystemSettings_v3_1_3_0)
            assert isinstance(api.tag, Tag_v3_1_3_0)
            assert isinstance(api.task, Task_v3_1_3_0)
            assert isinstance(api.topology, Topology_v3_1_3_0)
            assert isinstance(api.user_and_roles, UserandRoles_v3_1_3_0)
            assert isinstance(api.users, Users_v3_1_3_0)
            assert isinstance(api.wired, Wired_v3_1_3_0)
            assert isinstance(api.wireless, Wireless_v3_1_3_0)

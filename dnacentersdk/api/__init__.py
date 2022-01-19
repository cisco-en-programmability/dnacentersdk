# -*- coding: utf-8 -*-
"""Cisco DNA Center API wrappers.

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

from past.types import basestring

from dnacentersdk.config import (
    DEFAULT_DEBUG,
    DEFAULT_VERSION,
    DEFAULT_BASE_URL,
    DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_WAIT_ON_RATE_LIMIT,
    DEFAULT_VERIFY,
)
import dnacentersdk.environment as dnacenter_environment
from dnacentersdk.exceptions import AccessTokenError, VersionError
from dnacentersdk.models.mydict import mydict_data_factory
from dnacentersdk.models.schema_validator import SchemaValidator
from dnacentersdk.restsession import RestSession
from dnacentersdk.utils import check_type

from .authentication import Authentication
from .v1_2_10.clients import \
    Clients as Clients_v1_2_10
from .v1_2_10.command_runner import \
    CommandRunner as CommandRunner_v1_2_10
from .v1_2_10.devices import \
    Devices as Devices_v1_2_10
from .v1_2_10.fabric_wired import \
    FabricWired as FabricWired_v1_2_10
from .v1_2_10.file import \
    File as File_v1_2_10
from .v1_2_10.network_discovery import \
    NetworkDiscovery as NetworkDiscovery_v1_2_10
from .v1_2_10.networks import \
    Networks as Networks_v1_2_10
from .v1_2_10.non_fabric_wireless import \
    NonFabricWireless as NonFabricWireless_v1_2_10
from .v1_2_10.path_trace import \
    PathTrace as PathTrace_v1_2_10
from .v1_2_10.pnp import \
    Pnp as Pnp_v1_2_10
from .v1_2_10.swim import \
    Swim as Swim_v1_2_10
from .v1_2_10.site_profile import \
    SiteProfile as SiteProfile_v1_2_10
from .v1_2_10.sites import \
    Sites as Sites_v1_2_10
from .v1_2_10.tag import \
    Tag as Tag_v1_2_10
from .v1_2_10.task import \
    Task as Task_v1_2_10
from .v1_2_10.template_programmer import \
    TemplateProgrammer as TemplateProgrammer_v1_2_10
from .v1_3_0.clients import \
    Clients as Clients_v1_3_0
from .v1_3_0.command_runner import \
    CommandRunner as CommandRunner_v1_3_0
from .v1_3_0.devices import \
    Devices as Devices_v1_3_0
from .v1_3_0.fabric_wired import \
    FabricWired as FabricWired_v1_3_0
from .v1_3_0.file import \
    File as File_v1_3_0
from .v1_3_0.network_discovery import \
    NetworkDiscovery as NetworkDiscovery_v1_3_0
from .v1_3_0.networks import \
    Networks as Networks_v1_3_0
from .v1_3_0.non_fabric_wireless import \
    NonFabricWireless as NonFabricWireless_v1_3_0
from .v1_3_0.path_trace import \
    PathTrace as PathTrace_v1_3_0
from .v1_3_0.pnp import \
    Pnp as Pnp_v1_3_0
from .v1_3_0.swim import \
    Swim as Swim_v1_3_0
from .v1_3_0.site_profile import \
    SiteProfile as SiteProfile_v1_3_0
from .v1_3_0.sites import \
    Sites as Sites_v1_3_0
from .v1_3_0.tag import \
    Tag as Tag_v1_3_0
from .v1_3_0.task import \
    Task as Task_v1_3_0
from .v1_3_0.template_programmer import \
    TemplateProgrammer as TemplateProgrammer_v1_3_0
from .v1_3_1.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v1_3_1
from .v1_3_1.clients import \
    Clients as Clients_v1_3_1
from .v1_3_1.command_runner import \
    CommandRunner as CommandRunner_v1_3_1
from .v1_3_1.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v1_3_1
from .v1_3_1.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v1_3_1
from .v1_3_1.devices import \
    Devices as Devices_v1_3_1
from .v1_3_1.event_management import \
    EventManagement as EventManagement_v1_3_1
from .v1_3_1.fabric_wired import \
    FabricWired as FabricWired_v1_3_1
from .v1_3_1.file import \
    File as File_v1_3_1
from .v1_3_1.issues import \
    Issues as Issues_v1_3_1
from .v1_3_1.network_discovery import \
    NetworkDiscovery as NetworkDiscovery_v1_3_1
from .v1_3_1.network_settings import \
    NetworkSettings as NetworkSettings_v1_3_1
from .v1_3_1.non_fabric_wireless import \
    NonFabricWireless as NonFabricWireless_v1_3_1
from .v1_3_1.path_trace import \
    PathTrace as PathTrace_v1_3_1
from .v1_3_1.site_design import \
    SiteDesign as SiteDesign_v1_3_1
from .v1_3_1.sites import \
    Sites as Sites_v1_3_1
from .v1_3_1.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v1_3_1
from .v1_3_1.tag import \
    Tag as Tag_v1_3_1
from .v1_3_1.task import \
    Task as Task_v1_3_1
from .v1_3_1.topology import \
    Topology as Topology_v1_3_1
from .v1_3_1.users import \
    Users as Users_v1_3_1
from .v1_3_3.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v1_3_3
from .v1_3_3.clients import \
    Clients as Clients_v1_3_3
from .v1_3_3.command_runner import \
    CommandRunner as CommandRunner_v1_3_3
from .v1_3_3.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v1_3_3
from .v1_3_3.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v1_3_3
from .v1_3_3.devices import \
    Devices as Devices_v1_3_3
from .v1_3_3.discovery import \
    Discovery as Discovery_v1_3_3
from .v1_3_3.event_management import \
    EventManagement as EventManagement_v1_3_3
from .v1_3_3.file import \
    File as File_v1_3_3
from .v1_3_3.issues import \
    Issues as Issues_v1_3_3
from .v1_3_3.network_settings import \
    NetworkSettings as NetworkSettings_v1_3_3
from .v1_3_3.path_trace import \
    PathTrace as PathTrace_v1_3_3
from .v1_3_3.sda import \
    Sda as Sda_v1_3_3
from .v1_3_3.site_design import \
    SiteDesign as SiteDesign_v1_3_3
from .v1_3_3.sites import \
    Sites as Sites_v1_3_3
from .v1_3_3.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v1_3_3
from .v1_3_3.tag import \
    Tag as Tag_v1_3_3
from .v1_3_3.task import \
    Task as Task_v1_3_3
from .v1_3_3.topology import \
    Topology as Topology_v1_3_3
from .v1_3_3.users import \
    Users as Users_v1_3_3
from .v1_3_3.wireless import \
    Wireless as Wireless_v1_3_3
from .v2_1_1.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_1_1
from .v2_1_1.clients import \
    Clients as Clients_v2_1_1
from .v2_1_1.command_runner import \
    CommandRunner as CommandRunner_v2_1_1
from .v2_1_1.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_1_1
from .v2_1_1.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_1_1
from .v2_1_1.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_1_1
from .v2_1_1.devices import \
    Devices as Devices_v2_1_1
from .v2_1_1.discovery import \
    Discovery as Discovery_v2_1_1
from .v2_1_1.event_management import \
    EventManagement as EventManagement_v2_1_1
from .v2_1_1.file import \
    File as File_v2_1_1
from .v2_1_1.itsm import \
    Itsm as Itsm_v2_1_1
from .v2_1_1.issues import \
    Issues as Issues_v2_1_1
from .v2_1_1.network_settings import \
    NetworkSettings as NetworkSettings_v2_1_1
from .v2_1_1.path_trace import \
    PathTrace as PathTrace_v2_1_1
from .v2_1_1.sda import \
    Sda as Sda_v2_1_1
from .v2_1_1.site_design import \
    SiteDesign as SiteDesign_v2_1_1
from .v2_1_1.sites import \
    Sites as Sites_v2_1_1
from .v2_1_1.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_1_1
from .v2_1_1.tag import \
    Tag as Tag_v2_1_1
from .v2_1_1.task import \
    Task as Task_v2_1_1
from .v2_1_1.topology import \
    Topology as Topology_v2_1_1
from .v2_1_1.users import \
    Users as Users_v2_1_1
from .v2_1_1.wireless import \
    Wireless as Wireless_v2_1_1
from .v2_1_2.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_1_2
from .v2_1_2.applications import \
    Applications as Applications_v2_1_2
from .v2_1_2.clients import \
    Clients as Clients_v2_1_2
from .v2_1_2.command_runner import \
    CommandRunner as CommandRunner_v2_1_2
from .v2_1_2.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_1_2
from .v2_1_2.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_1_2
from .v2_1_2.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_1_2
from .v2_1_2.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_1_2
from .v2_1_2.devices import \
    Devices as Devices_v2_1_2
from .v2_1_2.discovery import \
    Discovery as Discovery_v2_1_2
from .v2_1_2.event_management import \
    EventManagement as EventManagement_v2_1_2
from .v2_1_2.file import \
    File as File_v2_1_2
from .v2_1_2.itsm import \
    Itsm as Itsm_v2_1_2
from .v2_1_2.issues import \
    Issues as Issues_v2_1_2
from .v2_1_2.network_settings import \
    NetworkSettings as NetworkSettings_v2_1_2
from .v2_1_2.path_trace import \
    PathTrace as PathTrace_v2_1_2
from .v2_1_2.sda import \
    Sda as Sda_v2_1_2
from .v2_1_2.sensors import \
    Sensors as Sensors_v2_1_2
from .v2_1_2.site_design import \
    SiteDesign as SiteDesign_v2_1_2
from .v2_1_2.sites import \
    Sites as Sites_v2_1_2
from .v2_1_2.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_1_2
from .v2_1_2.tag import \
    Tag as Tag_v2_1_2
from .v2_1_2.task import \
    Task as Task_v2_1_2
from .v2_1_2.topology import \
    Topology as Topology_v2_1_2
from .v2_1_2.users import \
    Users as Users_v2_1_2
from .v2_1_2.wireless import \
    Wireless as Wireless_v2_1_2
from .v2_2_1.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_2_1
from .v2_2_1.applications import \
    Applications as Applications_v2_2_1
from .v2_2_1.clients import \
    Clients as Clients_v2_2_1
from .v2_2_1.command_runner import \
    CommandRunner as CommandRunner_v2_2_1
from .v2_2_1.compliance import \
    Compliance as Compliance_v2_2_1
from .v2_2_1.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_2_1
from .v2_2_1.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_2_1
from .v2_2_1.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_2_1
from .v2_2_1.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_2_1
from .v2_2_1.devices import \
    Devices as Devices_v2_2_1
from .v2_2_1.discovery import \
    Discovery as Discovery_v2_2_1
from .v2_2_1.event_management import \
    EventManagement as EventManagement_v2_2_1
from .v2_2_1.file import \
    File as File_v2_2_1
from .v2_2_1.itsm import \
    Itsm as Itsm_v2_2_1
from .v2_2_1.issues import \
    Issues as Issues_v2_2_1
from .v2_2_1.network_settings import \
    NetworkSettings as NetworkSettings_v2_2_1
from .v2_2_1.path_trace import \
    PathTrace as PathTrace_v2_2_1
from .v2_2_1.reports import \
    Reports as Reports_v2_2_1
from .v2_2_1.sda import \
    Sda as Sda_v2_2_1
from .v2_2_1.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v2_2_1
from .v2_2_1.sensors import \
    Sensors as Sensors_v2_2_1
from .v2_2_1.site_design import \
    SiteDesign as SiteDesign_v2_2_1
from .v2_2_1.sites import \
    Sites as Sites_v2_2_1
from .v2_2_1.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_2_1
from .v2_2_1.tag import \
    Tag as Tag_v2_2_1
from .v2_2_1.task import \
    Task as Task_v2_2_1
from .v2_2_1.topology import \
    Topology as Topology_v2_2_1
from .v2_2_1.users import \
    Users as Users_v2_2_1
from .v2_2_1.wireless import \
    Wireless as Wireless_v2_2_1
from .v2_2_2_3.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_2_2_3
from .v2_2_2_3.applications import \
    Applications as Applications_v2_2_2_3
from .v2_2_2_3.authentication_management import \
    AuthenticationManagement as AuthenticationManagement_v2_2_2_3
from .v2_2_2_3.clients import \
    Clients as Clients_v2_2_2_3
from .v2_2_2_3.command_runner import \
    CommandRunner as CommandRunner_v2_2_2_3
from .v2_2_2_3.compliance import \
    Compliance as Compliance_v2_2_2_3
from .v2_2_2_3.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_2_2_3
from .v2_2_2_3.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_2_2_3
from .v2_2_2_3.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_2_2_3
from .v2_2_2_3.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_2_2_3
from .v2_2_2_3.devices import \
    Devices as Devices_v2_2_2_3
from .v2_2_2_3.discovery import \
    Discovery as Discovery_v2_2_2_3
from .v2_2_2_3.event_management import \
    EventManagement as EventManagement_v2_2_2_3
from .v2_2_2_3.file import \
    File as File_v2_2_2_3
from .v2_2_2_3.health_and_performance import \
    HealthAndPerformance as HealthAndPerformance_v2_2_2_3
from .v2_2_2_3.itsm import \
    Itsm as Itsm_v2_2_2_3
from .v2_2_2_3.issues import \
    Issues as Issues_v2_2_2_3
from .v2_2_2_3.licenses import \
    Licenses as Licenses_v2_2_2_3
from .v2_2_2_3.network_settings import \
    NetworkSettings as NetworkSettings_v2_2_2_3
from .v2_2_2_3.path_trace import \
    PathTrace as PathTrace_v2_2_2_3
from .v2_2_2_3.platform_configuration import \
    PlatformConfiguration as PlatformConfiguration_v2_2_2_3
from .v2_2_2_3.reports import \
    Reports as Reports_v2_2_2_3
from .v2_2_2_3.sda import \
    Sda as Sda_v2_2_2_3
from .v2_2_2_3.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v2_2_2_3
from .v2_2_2_3.sensors import \
    Sensors as Sensors_v2_2_2_3
from .v2_2_2_3.site_design import \
    SiteDesign as SiteDesign_v2_2_2_3
from .v2_2_2_3.sites import \
    Sites as Sites_v2_2_2_3
from .v2_2_2_3.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_2_2_3
from .v2_2_2_3.tag import \
    Tag as Tag_v2_2_2_3
from .v2_2_2_3.task import \
    Task as Task_v2_2_2_3
from .v2_2_2_3.topology import \
    Topology as Topology_v2_2_2_3
from .v2_2_2_3.users import \
    Users as Users_v2_2_2_3
from .v2_2_2_3.wireless import \
    Wireless as Wireless_v2_2_2_3
from .v2_2_3_3.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_2_3_3
from .v2_2_3_3.applications import \
    Applications as Applications_v2_2_3_3
from .v2_2_3_3.authentication_management import \
    AuthenticationManagement as AuthenticationManagement_v2_2_3_3
from .v2_2_3_3.clients import \
    Clients as Clients_v2_2_3_3
from .v2_2_3_3.command_runner import \
    CommandRunner as CommandRunner_v2_2_3_3
from .v2_2_3_3.compliance import \
    Compliance as Compliance_v2_2_3_3
from .v2_2_3_3.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_2_3_3
from .v2_2_3_3.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_2_3_3
from .v2_2_3_3.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_2_3_3
from .v2_2_3_3.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_2_3_3
from .v2_2_3_3.devices import \
    Devices as Devices_v2_2_3_3
from .v2_2_3_3.disaster_recovery import \
    DisasterRecovery as DisasterRecovery_v2_2_3_3
from .v2_2_3_3.discovery import \
    Discovery as Discovery_v2_2_3_3
from .v2_2_3_3.event_management import \
    EventManagement as EventManagement_v2_2_3_3
from .v2_2_3_3.fabric_wireless import \
    FabricWireless as FabricWireless_v2_2_3_3
from .v2_2_3_3.file import \
    File as File_v2_2_3_3
from .v2_2_3_3.health_and_performance import \
    HealthAndPerformance as HealthAndPerformance_v2_2_3_3
from .v2_2_3_3.itsm import \
    Itsm as Itsm_v2_2_3_3
from .v2_2_3_3.issues import \
    Issues as Issues_v2_2_3_3
from .v2_2_3_3.licenses import \
    Licenses as Licenses_v2_2_3_3
from .v2_2_3_3.network_settings import \
    NetworkSettings as NetworkSettings_v2_2_3_3
from .v2_2_3_3.path_trace import \
    PathTrace as PathTrace_v2_2_3_3
from .v2_2_3_3.platform_configuration import \
    PlatformConfiguration as PlatformConfiguration_v2_2_3_3
from .v2_2_3_3.policy import \
    Policy as Policy_v2_2_3_3
from .v2_2_3_3.reports import \
    Reports as Reports_v2_2_3_3
from .v2_2_3_3.sda import \
    Sda as Sda_v2_2_3_3
from .v2_2_3_3.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v2_2_3_3
from .v2_2_3_3.sensors import \
    Sensors as Sensors_v2_2_3_3
from .v2_2_3_3.site_design import \
    SiteDesign as SiteDesign_v2_2_3_3
from .v2_2_3_3.sites import \
    Sites as Sites_v2_2_3_3
from .v2_2_3_3.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_2_3_3
from .v2_2_3_3.tag import \
    Tag as Tag_v2_2_3_3
from .v2_2_3_3.task import \
    Task as Task_v2_2_3_3
from .v2_2_3_3.topology import \
    Topology as Topology_v2_2_3_3
from .v2_2_3_3.users import \
    Users as Users_v2_2_3_3
from .v2_2_3_3.wireless import \
    Wireless as Wireless_v2_2_3_3
from .custom_caller import CustomCaller


class DNACenterAPI(object):
    """Cisco DNA Center API wrapper.

    Creates a 'session' for all API calls through a created DNACenterAPI
    object.  The 'session' handles authentication, provides the needed headers,
    and checks all responses for error conditions.

    DNACenterAPI wraps all of the individual DNA Center APIs and represents
    them in a simple hierarchical structure.
    """

    def __init__(self, username=None,
                 password=None,
                 encoded_auth=None,
                 base_url=None,
                 single_request_timeout=None,
                 wait_on_rate_limit=None,
                 verify=None,
                 version=None,
                 debug=None,
                 object_factory=mydict_data_factory,
                 validator=SchemaValidator):
        """Create a new DNACenterAPI object.
        An access token is required to interact with the DNA Center APIs.
        This package supports two methods for you to generate the
        authorization token:

          1. Provide a encoded_auth value (username:password encoded in
          base 64). *This has priority over the following method*

          2. Provide username and password values.

        This package supports two methods for you to set those values:

          1. Provide the parameter. That is the encoded_auth or
          username and password parameters.

          2. If an argument is not supplied, the package checks for
          its environment variable counterpart. That is the
          DNA_CENTER_ENCODED_AUTH, DNA_CENTER_USERNAME,
          DNA_CENTER_PASSWORD.

        When not given enough parameters an AccessTokenError is raised.

        Args:
            base_url(basestring): The base URL to be prefixed to the
                individual API endpoint suffixes.
                Defaults to the DNA_CENTER_BASE_URL environment variable or
                dnacentersdk.config.DEFAULT_BASE_URL
                if the environment variable is not set.
            username(basestring): HTTP Basic Auth username.
            password(basestring): HTTP Basic Auth password.
            encoded_auth(basestring): HTTP Basic Auth base64 encoded string.
            single_request_timeout(int): Timeout (in seconds) for RESTful HTTP
                requests. Defaults to the DNA_CENTER_SINGLE_REQUEST_TIMEOUT
                environment variable or
                dnacentersdk.config.DEFAULT_SINGLE_REQUEST_TIMEOUT
                if the environment variable is not set.
            wait_on_rate_limit(bool): Enables or disables automatic rate-limit
                handling. Defaults to the DNA_CENTER_WAIT_ON_RATE_LIMIT
                environment variable or
                dnacentersdk.config.DEFAULT_WAIT_ON_RATE_LIMIT
                if the environment variable is not set.
            verify(bool,basestring): Controls whether we verify the server's
                TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use. Defaults to the DNA_CENTER_VERIFY
                (or DNA_CENTER_VERIFY_STRING) environment variable or
                dnacentersdk.config.DEFAULT_VERIFY if the environment
                variables are not set.
            version(basestring): Controls which version of DNA_CENTER to use.
                Defaults to the DNA_CENTER_VERSION environment variable or
                dnacentersdk.config.DEFAULT_VERSION
                if the environment variable is not set.
            debug(bool,basestring): Controls whether to log information about
                DNA Center APIs' request and response process.
                Defaults to the DNA_CENTER_DEBUG environment variable or False
                if the environment variable is not set.
            object_factory(callable): The factory function to use to create
                Python objects from the returned DNA Center JSON data objects.
            validator(callable): The factory function to use to validate
                Python objects sent in the body of the request.

        Returns:
            DNACenterAPI: A new DNACenterAPI object.

        Raises:
            TypeError: If the parameter types are incorrect.
            AccessTokenError: If an access token is not provided via the
                access_token argument or an environment variable.
            VersionError: If the version is not provided via the version
                argument or an environment variable, or it is not a
                DNA Center API supported version
                ['1.2.10', '1.3.0', '1.3.1', '1.3.3', '2.1.1', '2.1.2',
                '2.2.1', '2.2.2.3', '2.2.3.3'].

        """
        username = username or dnacenter_environment.get_env_username()
        password = password or dnacenter_environment.get_env_password()
        encoded_auth = encoded_auth or dnacenter_environment.get_env_encoded_auth()
        base_url = base_url or dnacenter_environment.get_env_base_url() or DEFAULT_BASE_URL

        if single_request_timeout is None:
            single_request_timeout = dnacenter_environment.get_env_single_request_timeout() or DEFAULT_SINGLE_REQUEST_TIMEOUT

        if wait_on_rate_limit is None:
            wait_on_rate_limit = dnacenter_environment.get_env_wait_on_rate_limit() or DEFAULT_WAIT_ON_RATE_LIMIT

        if verify is None:
            verify = dnacenter_environment.get_env_verify() or DEFAULT_VERIFY

        version = version or dnacenter_environment.get_env_version() or DEFAULT_VERSION

        if debug is None:
            debug = dnacenter_environment.get_env_debug() or DEFAULT_DEBUG

        check_type(base_url, basestring)
        check_type(single_request_timeout, int)
        check_type(wait_on_rate_limit, bool)
        check_type(debug, (bool, basestring), may_be_none=True)
        check_type(username, basestring, may_be_none=True)
        check_type(password, basestring, may_be_none=True)
        check_type(encoded_auth, basestring, may_be_none=True)
        check_type(verify, (bool, basestring), may_be_none=False)
        check_type(version, basestring, may_be_none=False)

        if version not in ['1.2.10', '1.3.0', '1.3.1', '1.3.3', '2.1.1',
                           '2.1.2', '2.2.1',
                           '2.2.2.3', '2.2.3.3']:
            raise VersionError(
                'Unknown API version, '
                + 'known versions are {}'.format(
                    '1.2.10, 1.3.0, 1.3.1, 1.3.3, 2.1.1, 2.1.2, 2.2.1, 2.2.2.3'
                    + 'and 2.2.3.3.'
                )
            )

        if isinstance(debug, str):
            debug = 'true' in debug.lower()

        # Init Authentication wrapper early to use for basicAuth requests
        self.authentication = Authentication(
            base_url, object_factory,
            single_request_timeout=single_request_timeout,
            verify=verify,
        )

        # Check if the user has provided the required basicAuth parameters
        if encoded_auth is None and (username is None or password is None):
            raise AccessTokenError(
                "You need an access token to interact with the DNA Center"
                " APIs. DNA Center uses HTTP Basic Auth to create an access"
                " token. You must provide the username and password or just"
                " the encoded_auth, either by setting each parameter or its"
                " environment variable counterpart ("
                "DNA_CENTER_USERNAME, DNA_CENTER_PASSWORD,"
                " DNA_CENTER_ENCODED_AUTH)."
            )

        def get_access_token():
            return self.authentication.authentication_api(
                username=username,
                password=password,
                encoded_auth=encoded_auth).Token

        # Create the API session
        # All of the API calls associated with a DNACenterAPI object will
        # leverage a single RESTful 'session' connecting to the DNA Center
        # cloud.
        self._session = RestSession(
            get_access_token=get_access_token,
            access_token=get_access_token(),
            base_url=base_url,
            single_request_timeout=single_request_timeout,
            wait_on_rate_limit=wait_on_rate_limit,
            verify=verify,
            version=version,
            debug=debug,
        )

        _validator = validator(version).json_schema_validate

        # API wrappers
        if version == '1.2.10':
            self.clients = \
                Clients_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.command_runner = \
                CommandRunner_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.devices = \
                Devices_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.fabric_wired = \
                FabricWired_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.file = \
                File_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.network_discovery = \
                NetworkDiscovery_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.networks = \
                Networks_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.non_fabric_wireless = \
                NonFabricWireless_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.path_trace = \
                PathTrace_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.pnp = \
                Pnp_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.swim = \
                Swim_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.site_profile = \
                SiteProfile_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.sites = \
                Sites_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.tag = \
                Tag_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.task = \
                Task_v1_2_10(
                    self._session, object_factory, _validator
                )
            self.template_programmer = \
                TemplateProgrammer_v1_2_10(
                    self._session, object_factory, _validator
                )
        if version == '1.3.0':
            self.clients = \
                Clients_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.command_runner = \
                CommandRunner_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.devices = \
                Devices_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.fabric_wired = \
                FabricWired_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.file = \
                File_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.network_discovery = \
                NetworkDiscovery_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.networks = \
                Networks_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.non_fabric_wireless = \
                NonFabricWireless_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.path_trace = \
                PathTrace_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.pnp = \
                Pnp_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.swim = \
                Swim_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.site_profile = \
                SiteProfile_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.sites = \
                Sites_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.tag = \
                Tag_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.task = \
                Task_v1_3_0(
                    self._session, object_factory, _validator
                )
            self.template_programmer = \
                TemplateProgrammer_v1_3_0(
                    self._session, object_factory, _validator
                )
        if version == '1.3.1':
            self.application_policy = \
                ApplicationPolicy_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.clients = \
                Clients_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.command_runner = \
                CommandRunner_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.configuration_templates = \
                ConfigurationTemplates_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.device_onboarding_pnp = \
                DeviceOnboardingPnp_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.devices = \
                Devices_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.event_management = \
                EventManagement_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.fabric_wired = \
                FabricWired_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.file = \
                File_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.issues = \
                Issues_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.network_discovery = \
                NetworkDiscovery_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.network_settings = \
                NetworkSettings_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.non_fabric_wireless = \
                NonFabricWireless_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.path_trace = \
                PathTrace_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.site_design = \
                SiteDesign_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.sites = \
                Sites_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.software_image_management_swim = \
                SoftwareImageManagementSwim_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.tag = \
                Tag_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.task = \
                Task_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.topology = \
                Topology_v1_3_1(
                    self._session, object_factory, _validator
                )
            self.users = \
                Users_v1_3_1(
                    self._session, object_factory, _validator
                )
        if version == '1.3.3':
            self.application_policy = \
                ApplicationPolicy_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.clients = \
                Clients_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.command_runner = \
                CommandRunner_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.configuration_templates = \
                ConfigurationTemplates_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.device_onboarding_pnp = \
                DeviceOnboardingPnp_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.devices = \
                Devices_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.discovery = \
                Discovery_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.event_management = \
                EventManagement_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.file = \
                File_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.issues = \
                Issues_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.network_settings = \
                NetworkSettings_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.path_trace = \
                PathTrace_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.sda = \
                Sda_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.site_design = \
                SiteDesign_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.sites = \
                Sites_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.software_image_management_swim = \
                SoftwareImageManagementSwim_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.tag = \
                Tag_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.task = \
                Task_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.topology = \
                Topology_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.users = \
                Users_v1_3_3(
                    self._session, object_factory, _validator
                )
            self.wireless = \
                Wireless_v1_3_3(
                    self._session, object_factory, _validator
                )
        if version == '2.1.1':
            self.application_policy = \
                ApplicationPolicy_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.clients = \
                Clients_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.command_runner = \
                CommandRunner_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.configuration_templates = \
                ConfigurationTemplates_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.device_onboarding_pnp = \
                DeviceOnboardingPnp_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.device_replacement = \
                DeviceReplacement_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.devices = \
                Devices_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.discovery = \
                Discovery_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.event_management = \
                EventManagement_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.file = \
                File_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.itsm = \
                Itsm_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.issues = \
                Issues_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.network_settings = \
                NetworkSettings_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.path_trace = \
                PathTrace_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.sda = \
                Sda_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.site_design = \
                SiteDesign_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.sites = \
                Sites_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.software_image_management_swim = \
                SoftwareImageManagementSwim_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.tag = \
                Tag_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.task = \
                Task_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.topology = \
                Topology_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.users = \
                Users_v2_1_1(
                    self._session, object_factory, _validator
                )
            self.wireless = \
                Wireless_v2_1_1(
                    self._session, object_factory, _validator
                )
        if version == '2.1.2':
            self.application_policy = \
                ApplicationPolicy_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.applications = \
                Applications_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.clients = \
                Clients_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.command_runner = \
                CommandRunner_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.configuration_archive = \
                ConfigurationArchive_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.configuration_templates = \
                ConfigurationTemplates_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.device_onboarding_pnp = \
                DeviceOnboardingPnp_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.device_replacement = \
                DeviceReplacement_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.devices = \
                Devices_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.discovery = \
                Discovery_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.event_management = \
                EventManagement_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.file = \
                File_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.itsm = \
                Itsm_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.issues = \
                Issues_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.network_settings = \
                NetworkSettings_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.path_trace = \
                PathTrace_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.sda = \
                Sda_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.sensors = \
                Sensors_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.site_design = \
                SiteDesign_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.sites = \
                Sites_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.software_image_management_swim = \
                SoftwareImageManagementSwim_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.tag = \
                Tag_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.task = \
                Task_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.topology = \
                Topology_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.users = \
                Users_v2_1_2(
                    self._session, object_factory, _validator
                )
            self.wireless = \
                Wireless_v2_1_2(
                    self._session, object_factory, _validator
                )
        if version == '2.2.1':
            self.application_policy = \
                ApplicationPolicy_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.applications = \
                Applications_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.clients = \
                Clients_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.command_runner = \
                CommandRunner_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.compliance = \
                Compliance_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.configuration_archive = \
                ConfigurationArchive_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.configuration_templates = \
                ConfigurationTemplates_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.device_onboarding_pnp = \
                DeviceOnboardingPnp_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.device_replacement = \
                DeviceReplacement_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.devices = \
                Devices_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.discovery = \
                Discovery_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.event_management = \
                EventManagement_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.file = \
                File_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.itsm = \
                Itsm_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.issues = \
                Issues_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.network_settings = \
                NetworkSettings_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.path_trace = \
                PathTrace_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.reports = \
                Reports_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.sda = \
                Sda_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.security_advisories = \
                SecurityAdvisories_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.sensors = \
                Sensors_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.site_design = \
                SiteDesign_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.sites = \
                Sites_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.software_image_management_swim = \
                SoftwareImageManagementSwim_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.tag = \
                Tag_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.task = \
                Task_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.topology = \
                Topology_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.users = \
                Users_v2_2_1(
                    self._session, object_factory, _validator
                )
            self.wireless = \
                Wireless_v2_2_1(
                    self._session, object_factory, _validator
                )
        if version == '2.2.2.3':
            self.application_policy = \
                ApplicationPolicy_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.applications = \
                Applications_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.authentication_management = \
                AuthenticationManagement_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.clients = \
                Clients_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.command_runner = \
                CommandRunner_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.compliance = \
                Compliance_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.configuration_archive = \
                ConfigurationArchive_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.configuration_templates = \
                ConfigurationTemplates_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.device_onboarding_pnp = \
                DeviceOnboardingPnp_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.device_replacement = \
                DeviceReplacement_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.devices = \
                Devices_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.discovery = \
                Discovery_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.event_management = \
                EventManagement_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.file = \
                File_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.health_and_performance = \
                HealthAndPerformance_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.itsm = \
                Itsm_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.issues = \
                Issues_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.licenses = \
                Licenses_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.network_settings = \
                NetworkSettings_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.path_trace = \
                PathTrace_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.platform_configuration = \
                PlatformConfiguration_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.reports = \
                Reports_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.sda = \
                Sda_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.security_advisories = \
                SecurityAdvisories_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.sensors = \
                Sensors_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.site_design = \
                SiteDesign_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.sites = \
                Sites_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.software_image_management_swim = \
                SoftwareImageManagementSwim_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.tag = \
                Tag_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.task = \
                Task_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.topology = \
                Topology_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.users = \
                Users_v2_2_2_3(
                    self._session, object_factory, _validator
                )
            self.wireless = \
                Wireless_v2_2_2_3(
                    self._session, object_factory, _validator
                )
        if version == '2.2.3.3':
            self.application_policy = \
                ApplicationPolicy_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.applications = \
                Applications_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.authentication_management = \
                AuthenticationManagement_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.clients = \
                Clients_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.command_runner = \
                CommandRunner_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.compliance = \
                Compliance_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.configuration_archive = \
                ConfigurationArchive_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.configuration_templates = \
                ConfigurationTemplates_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.device_onboarding_pnp = \
                DeviceOnboardingPnp_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.device_replacement = \
                DeviceReplacement_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.devices = \
                Devices_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.disaster_recovery = \
                DisasterRecovery_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.discovery = \
                Discovery_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.event_management = \
                EventManagement_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.fabric_wireless = \
                FabricWireless_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.file = \
                File_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.health_and_performance = \
                HealthAndPerformance_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.itsm = \
                Itsm_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.issues = \
                Issues_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.licenses = \
                Licenses_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.network_settings = \
                NetworkSettings_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.path_trace = \
                PathTrace_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.platform_configuration = \
                PlatformConfiguration_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.policy = \
                Policy_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.reports = \
                Reports_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.sda = \
                Sda_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.security_advisories = \
                SecurityAdvisories_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.sensors = \
                Sensors_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.site_design = \
                SiteDesign_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.sites = \
                Sites_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.software_image_management_swim = \
                SoftwareImageManagementSwim_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.tag = \
                Tag_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.task = \
                Task_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.topology = \
                Topology_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.users = \
                Users_v2_2_3_3(
                    self._session, object_factory, _validator
                )
            self.wireless = \
                Wireless_v2_2_3_3(
                    self._session, object_factory, _validator
                )
        self.custom_caller = \
            CustomCaller(self._session, object_factory)

    @property
    def session(self):
        """The DNA Center API session."""
        return self._session

    @property
    def access_token(self):
        """The access token used for API calls to the DNA Center service."""
        return self._session.access_token

    @property
    def base_url(self):
        """The base URL prefixed to the individual API endpoint suffixes."""
        return self._session.base_url

    @property
    def single_request_timeout(self):
        """Timeout (in seconds) for an single HTTP request."""
        return self._session.single_request_timeout

    @property
    def wait_on_rate_limit(self):
        """Automatic rate-limit handling enabled / disabled."""
        return self._session.wait_on_rate_limit

    @property
    def verify(self):
        """The verify (TLS Certificate) for the API endpoints."""
        return self._session._verify

    @property
    def version(self):
        """The API version of DNA Center."""
        return self._session._version

    @verify.setter
    def verify(self, value):
        """The verify (TLS Certificate) for the API endpoints."""
        self.authentication.verify = value
        self._session.verify = value

    @base_url.setter
    def base_url(self, value):
        """The base URL for the API endpoints."""
        self._session.base_url = value

    @single_request_timeout.setter
    def single_request_timeout(self, value):
        """The timeout (seconds) for a single HTTP REST API request."""
        self.authentication.single_request_timeout = value
        self._session.single_request_timeout = value

    @wait_on_rate_limit.setter
    def wait_on_rate_limit(self, value):
        """Enable or disable automatic rate-limit handling."""
        self._session.wait_on_rate_limit = value
